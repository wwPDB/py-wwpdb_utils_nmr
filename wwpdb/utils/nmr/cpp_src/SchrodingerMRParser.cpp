
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SchrodingerMRParser.g4 by ANTLR 4.13.0


#include "SchrodingerMRParserVisitor.h"

#include "SchrodingerMRParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct SchrodingerMRParserStaticData final {
  SchrodingerMRParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  SchrodingerMRParserStaticData(const SchrodingerMRParserStaticData&) = delete;
  SchrodingerMRParserStaticData(SchrodingerMRParserStaticData&&) = delete;
  SchrodingerMRParserStaticData& operator=(const SchrodingerMRParserStaticData&) = delete;
  SchrodingerMRParserStaticData& operator=(SchrodingerMRParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag schrodingermrparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
SchrodingerMRParserStaticData *schrodingermrparserParserStaticData = nullptr;

void schrodingermrparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (schrodingermrparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(schrodingermrparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<SchrodingerMRParserStaticData>(
    std::vector<std::string>{
      "schrodinger_mr", "import_structure", "struct_statement", "distance_restraint", 
      "dihedral_angle_restraint", "angle_restraint", "distance_statement", 
      "distance_assign", "distance_assign_by_number", "dihedral_angle_statement", 
      "dihedral_angle_assign", "dihedral_angle_assign_by_number", "angle_statement", 
      "angle_assign", "angle_assign_by_number", "fxdi_statement", "fxdi_assign", 
      "fxdi_assign_by_number", "fxta_statement", "fxta_assign", "fxta_assign_by_number", 
      "fxba_statement", "fxba_assign", "fxba_assign_by_number", "fxhb_statement", 
      "fxhb_assign", "fxhb_assign_by_number", "selection", "selection_expression", 
      "term", "factor", "number", "number_f", "parameter_statement"
    },
    std::vector<std::string>{
      "", "'set'", "'&STRUCT'", "'&DIST'", "'&TROS'", "'&ANGLE'", "", "'atom1'", 
      "'atom2'", "'atom3'", "'atom4'", "'lo'", "'up'", "'fc'", "'target'", 
      "','", "'FXDI'", "'FXBA'", "'FXTA'", "'FXHB'", "", "", "", "", "", 
      "'backbone'", "'sidechain'", "", "'/C3(-H1)(-H1)(-H1)/'", "'/C2(=O2)-N2-H2/'", 
      "'smarts.'", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "'fillres'", 
      "'fillmol'", "'within'", "'beyond'", "'withinbonds'", "'beyondbonds'", 
      "", "", "", "", "", "", "", "", "", "", "'('", "')'", "'<'", "'>'", 
      "'<='", "'>='"
    },
    std::vector<std::string>{
      "", "Set", "Struct", "Dist", "Tors", "Angle", "End", "Atom1", "Atom2", 
      "Atom3", "Atom4", "Lo", "Up", "Fc", "Target", "Comma", "FXDI", "FXBA", 
      "FXTA", "FXHB", "Entry", "Molecule", "Chain", "Residue", "Atom", "Backbone", 
      "Sidechain", "Water", "Methyl", "Amide", "Smarts", "Entry_name", "Molecule_number", 
      "Molecule_modulo", "Molecule_entrynum", "Molecule_atoms", "Molecule_weight", 
      "Chain_name", "Residue_name_or_number", "Residue_ptype", "Residue_mtype", 
      "Residue_polarity", "Residue_secondary_structure", "Residue_position", 
      "Residue_inscode", "Atom_ptype", "Atom_name", "Atom_number", "Atom_molnum", 
      "Atom_entrynum", "Atom_mtype", "Atom_element", "Atom_attachements", 
      "Atom_atomicnumber", "Atom_charge", "Atom_formalcharge", "Atom_displayed", 
      "Atom_selected", "Or_op", "And_op", "Not_op", "Fillres_op", "Fillmol_op", 
      "Within_op", "Beyond_op", "Withinbonds_op", "Beyondbonds_op", "Integer", 
      "IntRange", "Float", "FloatRange", "Slash_quote_string", "SMCLN_COMMENT", 
      "COMMENT", "Simple_name", "Simple_names", "Integers", "L_paren", "R_paren", 
      "Lt_op", "Gt_op", "Leq_op", "Geq_op", "Equ_op", "SPACE", "ENCLOSE_COMMENT", 
      "SECTION_COMMENT", "LINE_COMMENT", "Param_name", "Equ_op_SM", "SPACE_SM", 
      "RETURN_SM", "End_SM", "Hydrophilic", "Hydrophobic", "Non_polar", 
      "Polar", "Charged", "Positive", "Negative", "IGNORE_SPACE_PM", "Helix_or_strand", 
      "Strand_or_loop", "Helix_or_loop", "Helix", "Strand", "Loop", "IGNORE_SPACE_SSM"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,107,593,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,1,0,1,0,1,0,1,0,
  	1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,81,8,0,10,0,12,0,84,9,0,1,0,1,0,1,
  	1,1,1,4,1,90,8,1,11,1,12,1,91,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
  	1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,120,
  	8,6,11,6,12,6,121,1,6,4,6,125,8,6,11,6,12,6,126,3,6,129,8,6,1,7,1,7,1,
  	7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
  	4,9,151,8,9,11,9,12,9,152,1,9,4,9,156,8,9,11,9,12,9,157,3,9,160,8,9,1,
  	10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
  	12,1,12,1,12,1,12,1,12,1,12,1,12,4,12,183,8,12,11,12,12,12,184,1,12,4,
  	12,188,8,12,11,12,12,12,189,3,12,192,8,12,1,13,1,13,1,13,1,13,1,13,1,
  	13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,4,15,207,8,15,11,15,12,15,208,1,
  	15,4,15,212,8,15,11,15,12,15,213,3,15,216,8,15,1,16,1,16,1,16,1,16,1,
  	16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
  	17,1,17,1,18,4,18,239,8,18,11,18,12,18,240,1,18,4,18,244,8,18,11,18,12,
  	18,245,3,18,248,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
  	1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,4,21,271,8,21,
  	11,21,12,21,272,1,21,4,21,276,8,21,11,21,12,21,277,3,21,280,8,21,1,22,
  	1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,
  	1,23,1,23,1,23,1,23,1,24,4,24,302,8,24,11,24,12,24,303,1,24,4,24,307,
  	8,24,11,24,12,24,308,3,24,311,8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
  	1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,
  	1,27,1,28,1,28,1,28,5,28,338,8,28,10,28,12,28,341,9,28,1,29,1,29,3,29,
  	345,8,29,1,29,5,29,348,8,29,10,29,12,29,351,9,29,1,30,1,30,1,30,1,30,
  	1,30,1,30,1,30,1,30,5,30,361,8,30,10,30,12,30,364,9,30,1,30,1,30,1,30,
  	1,30,1,30,1,30,5,30,372,8,30,10,30,12,30,375,9,30,3,30,377,8,30,1,30,
  	1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,389,8,30,1,30,1,30,
  	1,30,1,30,1,30,3,30,396,8,30,1,30,1,30,1,30,1,30,5,30,402,8,30,10,30,
  	12,30,405,9,30,1,30,1,30,1,30,1,30,1,30,3,30,412,8,30,1,30,1,30,1,30,
  	5,30,417,8,30,10,30,12,30,420,9,30,3,30,422,8,30,1,30,1,30,1,30,1,30,
  	5,30,428,8,30,10,30,12,30,431,9,30,1,30,1,30,1,30,1,30,5,30,437,8,30,
  	10,30,12,30,440,9,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
  	1,30,1,30,1,30,1,30,5,30,456,8,30,10,30,12,30,459,9,30,1,30,1,30,1,30,
  	1,30,5,30,465,8,30,10,30,12,30,468,9,30,1,30,1,30,1,30,1,30,1,30,5,30,
  	475,8,30,10,30,12,30,478,9,30,3,30,480,8,30,1,30,1,30,1,30,1,30,1,30,
  	5,30,487,8,30,10,30,12,30,490,9,30,3,30,492,8,30,1,30,1,30,1,30,1,30,
  	1,30,5,30,499,8,30,10,30,12,30,502,9,30,3,30,504,8,30,1,30,1,30,1,30,
  	1,30,5,30,510,8,30,10,30,12,30,513,9,30,1,30,1,30,1,30,1,30,5,30,519,
  	8,30,10,30,12,30,522,9,30,1,30,1,30,1,30,1,30,1,30,3,30,529,8,30,1,30,
  	1,30,1,30,1,30,1,30,3,30,536,8,30,1,30,1,30,1,30,1,30,1,30,3,30,543,8,
  	30,1,30,1,30,1,30,1,30,1,30,3,30,550,8,30,1,30,1,30,1,30,1,30,1,30,1,
  	30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,
  	30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,583,8,
  	30,1,31,1,31,1,32,1,32,1,33,1,33,1,33,1,33,1,33,0,0,34,0,2,4,6,8,10,12,
  	14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
  	60,62,64,66,0,11,2,0,20,20,31,31,1,0,74,75,2,0,21,21,32,32,1,0,79,83,
  	2,0,22,22,37,37,2,0,67,67,74,75,2,0,23,23,38,38,1,0,93,99,1,0,101,106,
  	2,0,24,24,47,47,2,0,67,67,69,69,676,0,82,1,0,0,0,2,87,1,0,0,0,4,95,1,
  	0,0,0,6,100,1,0,0,0,8,104,1,0,0,0,10,108,1,0,0,0,12,128,1,0,0,0,14,130,
  	1,0,0,0,16,136,1,0,0,0,18,159,1,0,0,0,20,161,1,0,0,0,22,168,1,0,0,0,24,
  	191,1,0,0,0,26,193,1,0,0,0,28,199,1,0,0,0,30,215,1,0,0,0,32,217,1,0,0,
  	0,34,227,1,0,0,0,36,247,1,0,0,0,38,249,1,0,0,0,40,259,1,0,0,0,42,279,
  	1,0,0,0,44,281,1,0,0,0,46,290,1,0,0,0,48,310,1,0,0,0,50,312,1,0,0,0,52,
  	320,1,0,0,0,54,330,1,0,0,0,56,334,1,0,0,0,58,342,1,0,0,0,60,582,1,0,0,
  	0,62,584,1,0,0,0,64,586,1,0,0,0,66,588,1,0,0,0,68,81,3,2,1,0,69,81,3,
  	6,3,0,70,81,3,8,4,0,71,81,3,10,5,0,72,81,3,14,7,0,73,81,3,20,10,0,74,
  	81,3,26,13,0,75,81,3,66,33,0,76,81,3,30,15,0,77,81,3,36,18,0,78,81,3,
  	42,21,0,79,81,3,48,24,0,80,68,1,0,0,0,80,69,1,0,0,0,80,70,1,0,0,0,80,
  	71,1,0,0,0,80,72,1,0,0,0,80,73,1,0,0,0,80,74,1,0,0,0,80,75,1,0,0,0,80,
  	76,1,0,0,0,80,77,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,84,1,0,0,0,82,
  	80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,5,0,0,1,86,
  	1,1,0,0,0,87,89,5,2,0,0,88,90,3,4,2,0,89,88,1,0,0,0,90,91,1,0,0,0,91,
  	89,1,0,0,0,91,92,1,0,0,0,92,93,1,0,0,0,93,94,5,92,0,0,94,3,1,0,0,0,95,
  	96,5,88,0,0,96,97,5,89,0,0,97,98,5,88,0,0,98,99,5,91,0,0,99,5,1,0,0,0,
  	100,101,5,3,0,0,101,102,3,12,6,0,102,103,5,6,0,0,103,7,1,0,0,0,104,105,
  	5,4,0,0,105,106,3,18,9,0,106,107,5,6,0,0,107,9,1,0,0,0,108,109,5,5,0,
  	0,109,110,3,24,12,0,110,111,5,6,0,0,111,11,1,0,0,0,112,129,3,66,33,0,
  	113,114,5,7,0,0,114,115,5,8,0,0,115,116,5,11,0,0,116,117,5,12,0,0,117,
  	129,5,13,0,0,118,120,3,14,7,0,119,118,1,0,0,0,120,121,1,0,0,0,121,119,
  	1,0,0,0,121,122,1,0,0,0,122,129,1,0,0,0,123,125,3,16,8,0,124,123,1,0,
  	0,0,125,126,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,129,1,0,0,0,128,
  	112,1,0,0,0,128,113,1,0,0,0,128,119,1,0,0,0,128,124,1,0,0,0,129,13,1,
  	0,0,0,130,131,3,54,27,0,131,132,3,54,27,0,132,133,3,62,31,0,133,134,3,
  	62,31,0,134,135,3,62,31,0,135,15,1,0,0,0,136,137,5,67,0,0,137,138,5,67,
  	0,0,138,139,3,62,31,0,139,140,3,62,31,0,140,141,3,62,31,0,141,17,1,0,
  	0,0,142,160,3,66,33,0,143,144,5,7,0,0,144,145,5,8,0,0,145,146,5,9,0,0,
  	146,147,5,10,0,0,147,148,5,14,0,0,148,160,5,13,0,0,149,151,3,20,10,0,
  	150,149,1,0,0,0,151,152,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,160,
  	1,0,0,0,154,156,3,22,11,0,155,154,1,0,0,0,156,157,1,0,0,0,157,155,1,0,
  	0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,142,1,0,0,0,159,143,1,0,0,0,159,
  	150,1,0,0,0,159,155,1,0,0,0,160,19,1,0,0,0,161,162,3,54,27,0,162,163,
  	3,54,27,0,163,164,3,54,27,0,164,165,3,54,27,0,165,166,3,62,31,0,166,167,
  	3,62,31,0,167,21,1,0,0,0,168,169,5,67,0,0,169,170,5,67,0,0,170,171,5,
  	67,0,0,171,172,5,67,0,0,172,173,3,62,31,0,173,174,3,62,31,0,174,23,1,
  	0,0,0,175,192,3,66,33,0,176,177,5,7,0,0,177,178,5,8,0,0,178,179,5,9,0,
  	0,179,180,5,14,0,0,180,192,5,13,0,0,181,183,3,26,13,0,182,181,1,0,0,0,
  	183,184,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,192,1,0,0,0,186,188,
  	3,28,14,0,187,186,1,0,0,0,188,189,1,0,0,0,189,187,1,0,0,0,189,190,1,0,
  	0,0,190,192,1,0,0,0,191,175,1,0,0,0,191,176,1,0,0,0,191,182,1,0,0,0,191,
  	187,1,0,0,0,192,25,1,0,0,0,193,194,3,54,27,0,194,195,3,54,27,0,195,196,
  	3,54,27,0,196,197,3,62,31,0,197,198,3,62,31,0,198,27,1,0,0,0,199,200,
  	5,67,0,0,200,201,5,67,0,0,201,202,5,67,0,0,202,203,3,62,31,0,203,204,
  	3,62,31,0,204,29,1,0,0,0,205,207,3,32,16,0,206,205,1,0,0,0,207,208,1,
  	0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,216,1,0,0,0,210,212,3,34,17,
  	0,211,210,1,0,0,0,212,213,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,
  	216,1,0,0,0,215,206,1,0,0,0,215,211,1,0,0,0,216,31,1,0,0,0,217,218,5,
  	16,0,0,218,219,3,54,27,0,219,220,3,54,27,0,220,221,5,67,0,0,221,222,5,
  	67,0,0,222,223,3,62,31,0,223,224,3,62,31,0,224,225,3,62,31,0,225,226,
  	3,62,31,0,226,33,1,0,0,0,227,228,5,16,0,0,228,229,5,67,0,0,229,230,5,
  	67,0,0,230,231,5,67,0,0,231,232,5,67,0,0,232,233,3,62,31,0,233,234,3,
  	62,31,0,234,235,3,62,31,0,235,236,3,62,31,0,236,35,1,0,0,0,237,239,3,
  	38,19,0,238,237,1,0,0,0,239,240,1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,
  	0,241,248,1,0,0,0,242,244,3,40,20,0,243,242,1,0,0,0,244,245,1,0,0,0,245,
  	243,1,0,0,0,245,246,1,0,0,0,246,248,1,0,0,0,247,238,1,0,0,0,247,243,1,
  	0,0,0,248,37,1,0,0,0,249,250,5,18,0,0,250,251,3,54,27,0,251,252,3,54,
  	27,0,252,253,3,54,27,0,253,254,3,54,27,0,254,255,3,62,31,0,255,256,3,
  	62,31,0,256,257,3,62,31,0,257,258,3,62,31,0,258,39,1,0,0,0,259,260,5,
  	18,0,0,260,261,5,67,0,0,261,262,5,67,0,0,262,263,5,67,0,0,263,264,5,67,
  	0,0,264,265,3,62,31,0,265,266,3,62,31,0,266,267,3,62,31,0,267,268,3,62,
  	31,0,268,41,1,0,0,0,269,271,3,44,22,0,270,269,1,0,0,0,271,272,1,0,0,0,
  	272,270,1,0,0,0,272,273,1,0,0,0,273,280,1,0,0,0,274,276,3,46,23,0,275,
  	274,1,0,0,0,276,277,1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,280,1,
  	0,0,0,279,270,1,0,0,0,279,275,1,0,0,0,280,43,1,0,0,0,281,282,5,17,0,0,
  	282,283,3,54,27,0,283,284,3,54,27,0,284,285,3,54,27,0,285,286,5,67,0,
  	0,286,287,3,62,31,0,287,288,3,62,31,0,288,289,3,62,31,0,289,45,1,0,0,
  	0,290,291,5,17,0,0,291,292,5,67,0,0,292,293,5,67,0,0,293,294,5,67,0,0,
  	294,295,5,67,0,0,295,296,3,62,31,0,296,297,3,62,31,0,297,298,3,62,31,
  	0,298,299,3,62,31,0,299,47,1,0,0,0,300,302,3,50,25,0,301,300,1,0,0,0,
  	302,303,1,0,0,0,303,301,1,0,0,0,303,304,1,0,0,0,304,311,1,0,0,0,305,307,
  	3,52,26,0,306,305,1,0,0,0,307,308,1,0,0,0,308,306,1,0,0,0,308,309,1,0,
  	0,0,309,311,1,0,0,0,310,301,1,0,0,0,310,306,1,0,0,0,311,49,1,0,0,0,312,
  	313,5,19,0,0,313,314,3,54,27,0,314,315,3,54,27,0,315,316,3,54,27,0,316,
  	317,5,67,0,0,317,318,3,62,31,0,318,319,3,62,31,0,319,51,1,0,0,0,320,321,
  	5,19,0,0,321,322,5,67,0,0,322,323,5,67,0,0,323,324,5,67,0,0,324,325,5,
  	67,0,0,325,326,3,62,31,0,326,327,3,62,31,0,327,328,3,62,31,0,328,329,
  	3,62,31,0,329,53,1,0,0,0,330,331,5,77,0,0,331,332,3,56,28,0,332,333,5,
  	78,0,0,333,55,1,0,0,0,334,339,3,58,29,0,335,336,5,58,0,0,336,338,3,58,
  	29,0,337,335,1,0,0,0,338,341,1,0,0,0,339,337,1,0,0,0,339,340,1,0,0,0,
  	340,57,1,0,0,0,341,339,1,0,0,0,342,349,3,60,30,0,343,345,5,59,0,0,344,
  	343,1,0,0,0,344,345,1,0,0,0,345,346,1,0,0,0,346,348,3,60,30,0,347,344,
  	1,0,0,0,348,351,1,0,0,0,349,347,1,0,0,0,349,350,1,0,0,0,350,59,1,0,0,
  	0,351,349,1,0,0,0,352,353,5,77,0,0,353,354,3,56,28,0,354,355,5,78,0,0,
  	355,583,1,0,0,0,356,357,7,0,0,0,357,362,7,1,0,0,358,359,5,15,0,0,359,
  	361,7,1,0,0,360,358,1,0,0,0,361,364,1,0,0,0,362,360,1,0,0,0,362,363,1,
  	0,0,0,363,583,1,0,0,0,364,362,1,0,0,0,365,376,7,2,0,0,366,377,5,76,0,
  	0,367,377,5,68,0,0,368,373,5,67,0,0,369,370,5,15,0,0,370,372,5,67,0,0,
  	371,369,1,0,0,0,372,375,1,0,0,0,373,371,1,0,0,0,373,374,1,0,0,0,374,377,
  	1,0,0,0,375,373,1,0,0,0,376,366,1,0,0,0,376,367,1,0,0,0,376,368,1,0,0,
  	0,377,583,1,0,0,0,378,379,5,33,0,0,379,380,5,67,0,0,380,583,5,67,0,0,
  	381,382,5,34,0,0,382,583,5,67,0,0,383,388,5,35,0,0,384,389,5,68,0,0,385,
  	389,5,67,0,0,386,387,7,3,0,0,387,389,5,67,0,0,388,384,1,0,0,0,388,385,
  	1,0,0,0,388,386,1,0,0,0,389,583,1,0,0,0,390,395,5,36,0,0,391,396,5,68,
  	0,0,392,396,5,67,0,0,393,394,7,3,0,0,394,396,5,67,0,0,395,391,1,0,0,0,
  	395,392,1,0,0,0,395,393,1,0,0,0,396,583,1,0,0,0,397,398,7,4,0,0,398,403,
  	7,5,0,0,399,400,5,15,0,0,400,402,7,5,0,0,401,399,1,0,0,0,402,405,1,0,
  	0,0,403,401,1,0,0,0,403,404,1,0,0,0,404,583,1,0,0,0,405,403,1,0,0,0,406,
  	421,7,6,0,0,407,412,5,68,0,0,408,412,5,67,0,0,409,410,7,3,0,0,410,412,
  	5,67,0,0,411,407,1,0,0,0,411,408,1,0,0,0,411,409,1,0,0,0,412,422,1,0,
  	0,0,413,418,7,1,0,0,414,415,5,15,0,0,415,417,7,1,0,0,416,414,1,0,0,0,
  	417,420,1,0,0,0,418,416,1,0,0,0,418,419,1,0,0,0,419,422,1,0,0,0,420,418,
  	1,0,0,0,421,411,1,0,0,0,421,413,1,0,0,0,422,583,1,0,0,0,423,424,5,39,
  	0,0,424,429,7,1,0,0,425,426,5,15,0,0,426,428,7,1,0,0,427,425,1,0,0,0,
  	428,431,1,0,0,0,429,427,1,0,0,0,429,430,1,0,0,0,430,583,1,0,0,0,431,429,
  	1,0,0,0,432,433,5,40,0,0,433,438,7,1,0,0,434,435,5,15,0,0,435,437,7,1,
  	0,0,436,434,1,0,0,0,437,440,1,0,0,0,438,436,1,0,0,0,438,439,1,0,0,0,439,
  	583,1,0,0,0,440,438,1,0,0,0,441,442,5,41,0,0,442,583,7,7,0,0,443,444,
  	5,42,0,0,444,583,7,8,0,0,445,446,5,43,0,0,446,447,3,64,32,0,447,448,3,
  	64,32,0,448,583,1,0,0,0,449,450,5,44,0,0,450,583,5,74,0,0,451,452,5,45,
  	0,0,452,457,7,1,0,0,453,454,5,15,0,0,454,456,7,1,0,0,455,453,1,0,0,0,
  	456,459,1,0,0,0,457,455,1,0,0,0,457,458,1,0,0,0,458,583,1,0,0,0,459,457,
  	1,0,0,0,460,461,5,46,0,0,461,466,7,1,0,0,462,463,5,15,0,0,463,465,7,1,
  	0,0,464,462,1,0,0,0,465,468,1,0,0,0,466,464,1,0,0,0,466,467,1,0,0,0,467,
  	583,1,0,0,0,468,466,1,0,0,0,469,479,7,9,0,0,470,480,5,68,0,0,471,476,
  	5,67,0,0,472,473,5,15,0,0,473,475,5,67,0,0,474,472,1,0,0,0,475,478,1,
  	0,0,0,476,474,1,0,0,0,476,477,1,0,0,0,477,480,1,0,0,0,478,476,1,0,0,0,
  	479,470,1,0,0,0,479,471,1,0,0,0,480,583,1,0,0,0,481,491,5,48,0,0,482,
  	492,5,68,0,0,483,488,5,67,0,0,484,485,5,15,0,0,485,487,5,67,0,0,486,484,
  	1,0,0,0,487,490,1,0,0,0,488,486,1,0,0,0,488,489,1,0,0,0,489,492,1,0,0,
  	0,490,488,1,0,0,0,491,482,1,0,0,0,491,483,1,0,0,0,492,583,1,0,0,0,493,
  	503,5,49,0,0,494,504,5,68,0,0,495,500,5,67,0,0,496,497,5,15,0,0,497,499,
  	5,67,0,0,498,496,1,0,0,0,499,502,1,0,0,0,500,498,1,0,0,0,500,501,1,0,
  	0,0,501,504,1,0,0,0,502,500,1,0,0,0,503,494,1,0,0,0,503,495,1,0,0,0,504,
  	583,1,0,0,0,505,506,5,50,0,0,506,511,7,1,0,0,507,508,5,15,0,0,508,510,
  	7,1,0,0,509,507,1,0,0,0,510,513,1,0,0,0,511,509,1,0,0,0,511,512,1,0,0,
  	0,512,583,1,0,0,0,513,511,1,0,0,0,514,515,5,51,0,0,515,520,7,1,0,0,516,
  	517,5,15,0,0,517,519,7,1,0,0,518,516,1,0,0,0,519,522,1,0,0,0,520,518,
  	1,0,0,0,520,521,1,0,0,0,521,583,1,0,0,0,522,520,1,0,0,0,523,528,5,52,
  	0,0,524,529,5,68,0,0,525,529,5,67,0,0,526,527,7,3,0,0,527,529,5,67,0,
  	0,528,524,1,0,0,0,528,525,1,0,0,0,528,526,1,0,0,0,529,583,1,0,0,0,530,
  	535,5,53,0,0,531,536,5,68,0,0,532,536,5,67,0,0,533,534,7,3,0,0,534,536,
  	5,67,0,0,535,531,1,0,0,0,535,532,1,0,0,0,535,533,1,0,0,0,536,583,1,0,
  	0,0,537,542,5,54,0,0,538,543,5,70,0,0,539,543,5,69,0,0,540,541,7,3,0,
  	0,541,543,5,69,0,0,542,538,1,0,0,0,542,539,1,0,0,0,542,540,1,0,0,0,543,
  	583,1,0,0,0,544,549,5,55,0,0,545,550,5,68,0,0,546,550,5,67,0,0,547,548,
  	7,3,0,0,548,550,5,67,0,0,549,545,1,0,0,0,549,546,1,0,0,0,549,547,1,0,
  	0,0,550,583,1,0,0,0,551,583,5,56,0,0,552,583,5,57,0,0,553,554,5,61,0,
  	0,554,583,3,60,30,0,555,556,5,62,0,0,556,583,3,60,30,0,557,558,5,63,0,
  	0,558,559,3,64,32,0,559,560,3,60,30,0,560,583,1,0,0,0,561,562,5,64,0,
  	0,562,563,3,64,32,0,563,564,3,60,30,0,564,583,1,0,0,0,565,566,5,65,0,
  	0,566,567,5,67,0,0,567,583,3,60,30,0,568,569,5,66,0,0,569,570,5,67,0,
  	0,570,583,3,60,30,0,571,583,5,25,0,0,572,583,5,26,0,0,573,583,5,27,0,
  	0,574,583,5,28,0,0,575,583,5,29,0,0,576,577,5,30,0,0,577,583,5,74,0,0,
  	578,583,5,71,0,0,579,580,5,60,0,0,580,583,3,60,30,0,581,583,5,74,0,0,
  	582,352,1,0,0,0,582,356,1,0,0,0,582,365,1,0,0,0,582,378,1,0,0,0,582,381,
  	1,0,0,0,582,383,1,0,0,0,582,390,1,0,0,0,582,397,1,0,0,0,582,406,1,0,0,
  	0,582,423,1,0,0,0,582,432,1,0,0,0,582,441,1,0,0,0,582,443,1,0,0,0,582,
  	445,1,0,0,0,582,449,1,0,0,0,582,451,1,0,0,0,582,460,1,0,0,0,582,469,1,
  	0,0,0,582,481,1,0,0,0,582,493,1,0,0,0,582,505,1,0,0,0,582,514,1,0,0,0,
  	582,523,1,0,0,0,582,530,1,0,0,0,582,537,1,0,0,0,582,544,1,0,0,0,582,551,
  	1,0,0,0,582,552,1,0,0,0,582,553,1,0,0,0,582,555,1,0,0,0,582,557,1,0,0,
  	0,582,561,1,0,0,0,582,565,1,0,0,0,582,568,1,0,0,0,582,571,1,0,0,0,582,
  	572,1,0,0,0,582,573,1,0,0,0,582,574,1,0,0,0,582,575,1,0,0,0,582,576,1,
  	0,0,0,582,578,1,0,0,0,582,579,1,0,0,0,582,581,1,0,0,0,583,61,1,0,0,0,
  	584,585,7,10,0,0,585,63,1,0,0,0,586,587,7,10,0,0,587,65,1,0,0,0,588,589,
  	5,1,0,0,589,590,5,74,0,0,590,591,3,56,28,0,591,67,1,0,0,0,53,80,82,91,
  	121,126,128,152,157,159,184,189,191,208,213,215,240,245,247,272,277,279,
  	303,308,310,339,344,349,362,373,376,388,395,403,411,418,421,429,438,457,
  	466,476,479,488,491,500,503,511,520,528,535,542,549,582
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  schrodingermrparserParserStaticData = staticData.release();
}

}

SchrodingerMRParser::SchrodingerMRParser(TokenStream *input) : SchrodingerMRParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

SchrodingerMRParser::SchrodingerMRParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  SchrodingerMRParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *schrodingermrparserParserStaticData->atn, schrodingermrparserParserStaticData->decisionToDFA, schrodingermrparserParserStaticData->sharedContextCache, options);
}

SchrodingerMRParser::~SchrodingerMRParser() {
  delete _interpreter;
}

const atn::ATN& SchrodingerMRParser::getATN() const {
  return *schrodingermrparserParserStaticData->atn;
}

std::string SchrodingerMRParser::getGrammarFileName() const {
  return "SchrodingerMRParser.g4";
}

const std::vector<std::string>& SchrodingerMRParser::getRuleNames() const {
  return schrodingermrparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& SchrodingerMRParser::getVocabulary() const {
  return schrodingermrparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView SchrodingerMRParser::getSerializedATN() const {
  return schrodingermrparserParserStaticData->serializedATN;
}


//----------------- Schrodinger_mrContext ------------------------------------------------------------------

SchrodingerMRParser::Schrodinger_mrContext::Schrodinger_mrContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Schrodinger_mrContext::EOF() {
  return getToken(SchrodingerMRParser::EOF, 0);
}

std::vector<SchrodingerMRParser::Import_structureContext *> SchrodingerMRParser::Schrodinger_mrContext::import_structure() {
  return getRuleContexts<SchrodingerMRParser::Import_structureContext>();
}

SchrodingerMRParser::Import_structureContext* SchrodingerMRParser::Schrodinger_mrContext::import_structure(size_t i) {
  return getRuleContext<SchrodingerMRParser::Import_structureContext>(i);
}

std::vector<SchrodingerMRParser::Distance_restraintContext *> SchrodingerMRParser::Schrodinger_mrContext::distance_restraint() {
  return getRuleContexts<SchrodingerMRParser::Distance_restraintContext>();
}

SchrodingerMRParser::Distance_restraintContext* SchrodingerMRParser::Schrodinger_mrContext::distance_restraint(size_t i) {
  return getRuleContext<SchrodingerMRParser::Distance_restraintContext>(i);
}

std::vector<SchrodingerMRParser::Dihedral_angle_restraintContext *> SchrodingerMRParser::Schrodinger_mrContext::dihedral_angle_restraint() {
  return getRuleContexts<SchrodingerMRParser::Dihedral_angle_restraintContext>();
}

SchrodingerMRParser::Dihedral_angle_restraintContext* SchrodingerMRParser::Schrodinger_mrContext::dihedral_angle_restraint(size_t i) {
  return getRuleContext<SchrodingerMRParser::Dihedral_angle_restraintContext>(i);
}

std::vector<SchrodingerMRParser::Angle_restraintContext *> SchrodingerMRParser::Schrodinger_mrContext::angle_restraint() {
  return getRuleContexts<SchrodingerMRParser::Angle_restraintContext>();
}

SchrodingerMRParser::Angle_restraintContext* SchrodingerMRParser::Schrodinger_mrContext::angle_restraint(size_t i) {
  return getRuleContext<SchrodingerMRParser::Angle_restraintContext>(i);
}

std::vector<SchrodingerMRParser::Distance_assignContext *> SchrodingerMRParser::Schrodinger_mrContext::distance_assign() {
  return getRuleContexts<SchrodingerMRParser::Distance_assignContext>();
}

SchrodingerMRParser::Distance_assignContext* SchrodingerMRParser::Schrodinger_mrContext::distance_assign(size_t i) {
  return getRuleContext<SchrodingerMRParser::Distance_assignContext>(i);
}

std::vector<SchrodingerMRParser::Dihedral_angle_assignContext *> SchrodingerMRParser::Schrodinger_mrContext::dihedral_angle_assign() {
  return getRuleContexts<SchrodingerMRParser::Dihedral_angle_assignContext>();
}

SchrodingerMRParser::Dihedral_angle_assignContext* SchrodingerMRParser::Schrodinger_mrContext::dihedral_angle_assign(size_t i) {
  return getRuleContext<SchrodingerMRParser::Dihedral_angle_assignContext>(i);
}

std::vector<SchrodingerMRParser::Angle_assignContext *> SchrodingerMRParser::Schrodinger_mrContext::angle_assign() {
  return getRuleContexts<SchrodingerMRParser::Angle_assignContext>();
}

SchrodingerMRParser::Angle_assignContext* SchrodingerMRParser::Schrodinger_mrContext::angle_assign(size_t i) {
  return getRuleContext<SchrodingerMRParser::Angle_assignContext>(i);
}

std::vector<SchrodingerMRParser::Parameter_statementContext *> SchrodingerMRParser::Schrodinger_mrContext::parameter_statement() {
  return getRuleContexts<SchrodingerMRParser::Parameter_statementContext>();
}

SchrodingerMRParser::Parameter_statementContext* SchrodingerMRParser::Schrodinger_mrContext::parameter_statement(size_t i) {
  return getRuleContext<SchrodingerMRParser::Parameter_statementContext>(i);
}

std::vector<SchrodingerMRParser::Fxdi_statementContext *> SchrodingerMRParser::Schrodinger_mrContext::fxdi_statement() {
  return getRuleContexts<SchrodingerMRParser::Fxdi_statementContext>();
}

SchrodingerMRParser::Fxdi_statementContext* SchrodingerMRParser::Schrodinger_mrContext::fxdi_statement(size_t i) {
  return getRuleContext<SchrodingerMRParser::Fxdi_statementContext>(i);
}

std::vector<SchrodingerMRParser::Fxta_statementContext *> SchrodingerMRParser::Schrodinger_mrContext::fxta_statement() {
  return getRuleContexts<SchrodingerMRParser::Fxta_statementContext>();
}

SchrodingerMRParser::Fxta_statementContext* SchrodingerMRParser::Schrodinger_mrContext::fxta_statement(size_t i) {
  return getRuleContext<SchrodingerMRParser::Fxta_statementContext>(i);
}

std::vector<SchrodingerMRParser::Fxba_statementContext *> SchrodingerMRParser::Schrodinger_mrContext::fxba_statement() {
  return getRuleContexts<SchrodingerMRParser::Fxba_statementContext>();
}

SchrodingerMRParser::Fxba_statementContext* SchrodingerMRParser::Schrodinger_mrContext::fxba_statement(size_t i) {
  return getRuleContext<SchrodingerMRParser::Fxba_statementContext>(i);
}

std::vector<SchrodingerMRParser::Fxhb_statementContext *> SchrodingerMRParser::Schrodinger_mrContext::fxhb_statement() {
  return getRuleContexts<SchrodingerMRParser::Fxhb_statementContext>();
}

SchrodingerMRParser::Fxhb_statementContext* SchrodingerMRParser::Schrodinger_mrContext::fxhb_statement(size_t i) {
  return getRuleContext<SchrodingerMRParser::Fxhb_statementContext>(i);
}


size_t SchrodingerMRParser::Schrodinger_mrContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleSchrodinger_mr;
}


std::any SchrodingerMRParser::Schrodinger_mrContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitSchrodinger_mr(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Schrodinger_mrContext* SchrodingerMRParser::schrodinger_mr() {
  Schrodinger_mrContext *_localctx = _tracker.createInstance<Schrodinger_mrContext>(_ctx, getState());
  enterRule(_localctx, 0, SchrodingerMRParser::RuleSchrodinger_mr);
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
    setState(82);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 983102) != 0) || _la == SchrodingerMRParser::L_paren) {
      setState(80);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
      case 1: {
        setState(68);
        import_structure();
        break;
      }

      case 2: {
        setState(69);
        distance_restraint();
        break;
      }

      case 3: {
        setState(70);
        dihedral_angle_restraint();
        break;
      }

      case 4: {
        setState(71);
        angle_restraint();
        break;
      }

      case 5: {
        setState(72);
        distance_assign();
        break;
      }

      case 6: {
        setState(73);
        dihedral_angle_assign();
        break;
      }

      case 7: {
        setState(74);
        angle_assign();
        break;
      }

      case 8: {
        setState(75);
        parameter_statement();
        break;
      }

      case 9: {
        setState(76);
        fxdi_statement();
        break;
      }

      case 10: {
        setState(77);
        fxta_statement();
        break;
      }

      case 11: {
        setState(78);
        fxba_statement();
        break;
      }

      case 12: {
        setState(79);
        fxhb_statement();
        break;
      }

      default:
        break;
      }
      setState(84);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(85);
    match(SchrodingerMRParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Import_structureContext ------------------------------------------------------------------

SchrodingerMRParser::Import_structureContext::Import_structureContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Import_structureContext::Struct() {
  return getToken(SchrodingerMRParser::Struct, 0);
}

tree::TerminalNode* SchrodingerMRParser::Import_structureContext::End_SM() {
  return getToken(SchrodingerMRParser::End_SM, 0);
}

std::vector<SchrodingerMRParser::Struct_statementContext *> SchrodingerMRParser::Import_structureContext::struct_statement() {
  return getRuleContexts<SchrodingerMRParser::Struct_statementContext>();
}

SchrodingerMRParser::Struct_statementContext* SchrodingerMRParser::Import_structureContext::struct_statement(size_t i) {
  return getRuleContext<SchrodingerMRParser::Struct_statementContext>(i);
}


size_t SchrodingerMRParser::Import_structureContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleImport_structure;
}


std::any SchrodingerMRParser::Import_structureContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitImport_structure(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Import_structureContext* SchrodingerMRParser::import_structure() {
  Import_structureContext *_localctx = _tracker.createInstance<Import_structureContext>(_ctx, getState());
  enterRule(_localctx, 2, SchrodingerMRParser::RuleImport_structure);
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
    setState(87);
    match(SchrodingerMRParser::Struct);
    setState(89); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(88);
      struct_statement();
      setState(91); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == SchrodingerMRParser::Param_name);
    setState(93);
    match(SchrodingerMRParser::End_SM);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Struct_statementContext ------------------------------------------------------------------

SchrodingerMRParser::Struct_statementContext::Struct_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::Struct_statementContext::Param_name() {
  return getTokens(SchrodingerMRParser::Param_name);
}

tree::TerminalNode* SchrodingerMRParser::Struct_statementContext::Param_name(size_t i) {
  return getToken(SchrodingerMRParser::Param_name, i);
}

tree::TerminalNode* SchrodingerMRParser::Struct_statementContext::Equ_op_SM() {
  return getToken(SchrodingerMRParser::Equ_op_SM, 0);
}

tree::TerminalNode* SchrodingerMRParser::Struct_statementContext::RETURN_SM() {
  return getToken(SchrodingerMRParser::RETURN_SM, 0);
}


size_t SchrodingerMRParser::Struct_statementContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleStruct_statement;
}


std::any SchrodingerMRParser::Struct_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitStruct_statement(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Struct_statementContext* SchrodingerMRParser::struct_statement() {
  Struct_statementContext *_localctx = _tracker.createInstance<Struct_statementContext>(_ctx, getState());
  enterRule(_localctx, 4, SchrodingerMRParser::RuleStruct_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(95);
    match(SchrodingerMRParser::Param_name);
    setState(96);
    match(SchrodingerMRParser::Equ_op_SM);
    setState(97);
    match(SchrodingerMRParser::Param_name);
    setState(98);
    match(SchrodingerMRParser::RETURN_SM);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_restraintContext ------------------------------------------------------------------

SchrodingerMRParser::Distance_restraintContext::Distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Distance_restraintContext::Dist() {
  return getToken(SchrodingerMRParser::Dist, 0);
}

SchrodingerMRParser::Distance_statementContext* SchrodingerMRParser::Distance_restraintContext::distance_statement() {
  return getRuleContext<SchrodingerMRParser::Distance_statementContext>(0);
}

tree::TerminalNode* SchrodingerMRParser::Distance_restraintContext::End() {
  return getToken(SchrodingerMRParser::End, 0);
}


size_t SchrodingerMRParser::Distance_restraintContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleDistance_restraint;
}


std::any SchrodingerMRParser::Distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraint(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Distance_restraintContext* SchrodingerMRParser::distance_restraint() {
  Distance_restraintContext *_localctx = _tracker.createInstance<Distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 6, SchrodingerMRParser::RuleDistance_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(100);
    match(SchrodingerMRParser::Dist);
    setState(101);
    distance_statement();
    setState(102);
    match(SchrodingerMRParser::End);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_restraintContext ------------------------------------------------------------------

SchrodingerMRParser::Dihedral_angle_restraintContext::Dihedral_angle_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Dihedral_angle_restraintContext::Tors() {
  return getToken(SchrodingerMRParser::Tors, 0);
}

SchrodingerMRParser::Dihedral_angle_statementContext* SchrodingerMRParser::Dihedral_angle_restraintContext::dihedral_angle_statement() {
  return getRuleContext<SchrodingerMRParser::Dihedral_angle_statementContext>(0);
}

tree::TerminalNode* SchrodingerMRParser::Dihedral_angle_restraintContext::End() {
  return getToken(SchrodingerMRParser::End, 0);
}


size_t SchrodingerMRParser::Dihedral_angle_restraintContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleDihedral_angle_restraint;
}


std::any SchrodingerMRParser::Dihedral_angle_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_restraint(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Dihedral_angle_restraintContext* SchrodingerMRParser::dihedral_angle_restraint() {
  Dihedral_angle_restraintContext *_localctx = _tracker.createInstance<Dihedral_angle_restraintContext>(_ctx, getState());
  enterRule(_localctx, 8, SchrodingerMRParser::RuleDihedral_angle_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(104);
    match(SchrodingerMRParser::Tors);
    setState(105);
    dihedral_angle_statement();
    setState(106);
    match(SchrodingerMRParser::End);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Angle_restraintContext ------------------------------------------------------------------

SchrodingerMRParser::Angle_restraintContext::Angle_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Angle_restraintContext::Angle() {
  return getToken(SchrodingerMRParser::Angle, 0);
}

SchrodingerMRParser::Angle_statementContext* SchrodingerMRParser::Angle_restraintContext::angle_statement() {
  return getRuleContext<SchrodingerMRParser::Angle_statementContext>(0);
}

tree::TerminalNode* SchrodingerMRParser::Angle_restraintContext::End() {
  return getToken(SchrodingerMRParser::End, 0);
}


size_t SchrodingerMRParser::Angle_restraintContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleAngle_restraint;
}


std::any SchrodingerMRParser::Angle_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitAngle_restraint(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Angle_restraintContext* SchrodingerMRParser::angle_restraint() {
  Angle_restraintContext *_localctx = _tracker.createInstance<Angle_restraintContext>(_ctx, getState());
  enterRule(_localctx, 10, SchrodingerMRParser::RuleAngle_restraint);

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
    match(SchrodingerMRParser::Angle);
    setState(109);
    angle_statement();
    setState(110);
    match(SchrodingerMRParser::End);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_statementContext ------------------------------------------------------------------

SchrodingerMRParser::Distance_statementContext::Distance_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

SchrodingerMRParser::Parameter_statementContext* SchrodingerMRParser::Distance_statementContext::parameter_statement() {
  return getRuleContext<SchrodingerMRParser::Parameter_statementContext>(0);
}

tree::TerminalNode* SchrodingerMRParser::Distance_statementContext::Atom1() {
  return getToken(SchrodingerMRParser::Atom1, 0);
}

tree::TerminalNode* SchrodingerMRParser::Distance_statementContext::Atom2() {
  return getToken(SchrodingerMRParser::Atom2, 0);
}

tree::TerminalNode* SchrodingerMRParser::Distance_statementContext::Lo() {
  return getToken(SchrodingerMRParser::Lo, 0);
}

tree::TerminalNode* SchrodingerMRParser::Distance_statementContext::Up() {
  return getToken(SchrodingerMRParser::Up, 0);
}

tree::TerminalNode* SchrodingerMRParser::Distance_statementContext::Fc() {
  return getToken(SchrodingerMRParser::Fc, 0);
}

std::vector<SchrodingerMRParser::Distance_assignContext *> SchrodingerMRParser::Distance_statementContext::distance_assign() {
  return getRuleContexts<SchrodingerMRParser::Distance_assignContext>();
}

SchrodingerMRParser::Distance_assignContext* SchrodingerMRParser::Distance_statementContext::distance_assign(size_t i) {
  return getRuleContext<SchrodingerMRParser::Distance_assignContext>(i);
}

std::vector<SchrodingerMRParser::Distance_assign_by_numberContext *> SchrodingerMRParser::Distance_statementContext::distance_assign_by_number() {
  return getRuleContexts<SchrodingerMRParser::Distance_assign_by_numberContext>();
}

SchrodingerMRParser::Distance_assign_by_numberContext* SchrodingerMRParser::Distance_statementContext::distance_assign_by_number(size_t i) {
  return getRuleContext<SchrodingerMRParser::Distance_assign_by_numberContext>(i);
}


size_t SchrodingerMRParser::Distance_statementContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleDistance_statement;
}


std::any SchrodingerMRParser::Distance_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_statement(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Distance_statementContext* SchrodingerMRParser::distance_statement() {
  Distance_statementContext *_localctx = _tracker.createInstance<Distance_statementContext>(_ctx, getState());
  enterRule(_localctx, 12, SchrodingerMRParser::RuleDistance_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(128);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case SchrodingerMRParser::Set: {
        enterOuterAlt(_localctx, 1);
        setState(112);
        parameter_statement();
        break;
      }

      case SchrodingerMRParser::Atom1: {
        enterOuterAlt(_localctx, 2);
        setState(113);
        match(SchrodingerMRParser::Atom1);
        setState(114);
        match(SchrodingerMRParser::Atom2);
        setState(115);
        match(SchrodingerMRParser::Lo);
        setState(116);
        match(SchrodingerMRParser::Up);
        setState(117);
        match(SchrodingerMRParser::Fc);
        break;
      }

      case SchrodingerMRParser::L_paren: {
        enterOuterAlt(_localctx, 3);
        setState(119); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(118);
          distance_assign();
          setState(121); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SchrodingerMRParser::L_paren);
        break;
      }

      case SchrodingerMRParser::Integer: {
        enterOuterAlt(_localctx, 4);
        setState(124); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(123);
          distance_assign_by_number();
          setState(126); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SchrodingerMRParser::Integer);
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

//----------------- Distance_assignContext ------------------------------------------------------------------

SchrodingerMRParser::Distance_assignContext::Distance_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<SchrodingerMRParser::SelectionContext *> SchrodingerMRParser::Distance_assignContext::selection() {
  return getRuleContexts<SchrodingerMRParser::SelectionContext>();
}

SchrodingerMRParser::SelectionContext* SchrodingerMRParser::Distance_assignContext::selection(size_t i) {
  return getRuleContext<SchrodingerMRParser::SelectionContext>(i);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Distance_assignContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Distance_assignContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Distance_assignContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleDistance_assign;
}


std::any SchrodingerMRParser::Distance_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_assign(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Distance_assignContext* SchrodingerMRParser::distance_assign() {
  Distance_assignContext *_localctx = _tracker.createInstance<Distance_assignContext>(_ctx, getState());
  enterRule(_localctx, 14, SchrodingerMRParser::RuleDistance_assign);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(130);
    selection();
    setState(131);
    selection();
    setState(132);
    number();
    setState(133);
    number();
    setState(134);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_assign_by_numberContext ------------------------------------------------------------------

SchrodingerMRParser::Distance_assign_by_numberContext::Distance_assign_by_numberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::Distance_assign_by_numberContext::Integer() {
  return getTokens(SchrodingerMRParser::Integer);
}

tree::TerminalNode* SchrodingerMRParser::Distance_assign_by_numberContext::Integer(size_t i) {
  return getToken(SchrodingerMRParser::Integer, i);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Distance_assign_by_numberContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Distance_assign_by_numberContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Distance_assign_by_numberContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleDistance_assign_by_number;
}


std::any SchrodingerMRParser::Distance_assign_by_numberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_assign_by_number(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Distance_assign_by_numberContext* SchrodingerMRParser::distance_assign_by_number() {
  Distance_assign_by_numberContext *_localctx = _tracker.createInstance<Distance_assign_by_numberContext>(_ctx, getState());
  enterRule(_localctx, 16, SchrodingerMRParser::RuleDistance_assign_by_number);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(136);
    match(SchrodingerMRParser::Integer);
    setState(137);
    match(SchrodingerMRParser::Integer);
    setState(138);
    number();
    setState(139);
    number();
    setState(140);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_statementContext ------------------------------------------------------------------

SchrodingerMRParser::Dihedral_angle_statementContext::Dihedral_angle_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

SchrodingerMRParser::Parameter_statementContext* SchrodingerMRParser::Dihedral_angle_statementContext::parameter_statement() {
  return getRuleContext<SchrodingerMRParser::Parameter_statementContext>(0);
}

tree::TerminalNode* SchrodingerMRParser::Dihedral_angle_statementContext::Atom1() {
  return getToken(SchrodingerMRParser::Atom1, 0);
}

tree::TerminalNode* SchrodingerMRParser::Dihedral_angle_statementContext::Atom2() {
  return getToken(SchrodingerMRParser::Atom2, 0);
}

tree::TerminalNode* SchrodingerMRParser::Dihedral_angle_statementContext::Atom3() {
  return getToken(SchrodingerMRParser::Atom3, 0);
}

tree::TerminalNode* SchrodingerMRParser::Dihedral_angle_statementContext::Atom4() {
  return getToken(SchrodingerMRParser::Atom4, 0);
}

tree::TerminalNode* SchrodingerMRParser::Dihedral_angle_statementContext::Target() {
  return getToken(SchrodingerMRParser::Target, 0);
}

tree::TerminalNode* SchrodingerMRParser::Dihedral_angle_statementContext::Fc() {
  return getToken(SchrodingerMRParser::Fc, 0);
}

std::vector<SchrodingerMRParser::Dihedral_angle_assignContext *> SchrodingerMRParser::Dihedral_angle_statementContext::dihedral_angle_assign() {
  return getRuleContexts<SchrodingerMRParser::Dihedral_angle_assignContext>();
}

SchrodingerMRParser::Dihedral_angle_assignContext* SchrodingerMRParser::Dihedral_angle_statementContext::dihedral_angle_assign(size_t i) {
  return getRuleContext<SchrodingerMRParser::Dihedral_angle_assignContext>(i);
}

std::vector<SchrodingerMRParser::Dihedral_angle_assign_by_numberContext *> SchrodingerMRParser::Dihedral_angle_statementContext::dihedral_angle_assign_by_number() {
  return getRuleContexts<SchrodingerMRParser::Dihedral_angle_assign_by_numberContext>();
}

SchrodingerMRParser::Dihedral_angle_assign_by_numberContext* SchrodingerMRParser::Dihedral_angle_statementContext::dihedral_angle_assign_by_number(size_t i) {
  return getRuleContext<SchrodingerMRParser::Dihedral_angle_assign_by_numberContext>(i);
}


size_t SchrodingerMRParser::Dihedral_angle_statementContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleDihedral_angle_statement;
}


std::any SchrodingerMRParser::Dihedral_angle_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_statement(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Dihedral_angle_statementContext* SchrodingerMRParser::dihedral_angle_statement() {
  Dihedral_angle_statementContext *_localctx = _tracker.createInstance<Dihedral_angle_statementContext>(_ctx, getState());
  enterRule(_localctx, 18, SchrodingerMRParser::RuleDihedral_angle_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(159);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case SchrodingerMRParser::Set: {
        enterOuterAlt(_localctx, 1);
        setState(142);
        parameter_statement();
        break;
      }

      case SchrodingerMRParser::Atom1: {
        enterOuterAlt(_localctx, 2);
        setState(143);
        match(SchrodingerMRParser::Atom1);
        setState(144);
        match(SchrodingerMRParser::Atom2);
        setState(145);
        match(SchrodingerMRParser::Atom3);
        setState(146);
        match(SchrodingerMRParser::Atom4);
        setState(147);
        match(SchrodingerMRParser::Target);
        setState(148);
        match(SchrodingerMRParser::Fc);
        break;
      }

      case SchrodingerMRParser::L_paren: {
        enterOuterAlt(_localctx, 3);
        setState(150); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(149);
          dihedral_angle_assign();
          setState(152); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SchrodingerMRParser::L_paren);
        break;
      }

      case SchrodingerMRParser::Integer: {
        enterOuterAlt(_localctx, 4);
        setState(155); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(154);
          dihedral_angle_assign_by_number();
          setState(157); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SchrodingerMRParser::Integer);
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

//----------------- Dihedral_angle_assignContext ------------------------------------------------------------------

SchrodingerMRParser::Dihedral_angle_assignContext::Dihedral_angle_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<SchrodingerMRParser::SelectionContext *> SchrodingerMRParser::Dihedral_angle_assignContext::selection() {
  return getRuleContexts<SchrodingerMRParser::SelectionContext>();
}

SchrodingerMRParser::SelectionContext* SchrodingerMRParser::Dihedral_angle_assignContext::selection(size_t i) {
  return getRuleContext<SchrodingerMRParser::SelectionContext>(i);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Dihedral_angle_assignContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Dihedral_angle_assignContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Dihedral_angle_assignContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleDihedral_angle_assign;
}


std::any SchrodingerMRParser::Dihedral_angle_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_assign(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Dihedral_angle_assignContext* SchrodingerMRParser::dihedral_angle_assign() {
  Dihedral_angle_assignContext *_localctx = _tracker.createInstance<Dihedral_angle_assignContext>(_ctx, getState());
  enterRule(_localctx, 20, SchrodingerMRParser::RuleDihedral_angle_assign);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(161);
    selection();
    setState(162);
    selection();
    setState(163);
    selection();
    setState(164);
    selection();
    setState(165);
    number();
    setState(166);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_assign_by_numberContext ------------------------------------------------------------------

SchrodingerMRParser::Dihedral_angle_assign_by_numberContext::Dihedral_angle_assign_by_numberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::Dihedral_angle_assign_by_numberContext::Integer() {
  return getTokens(SchrodingerMRParser::Integer);
}

tree::TerminalNode* SchrodingerMRParser::Dihedral_angle_assign_by_numberContext::Integer(size_t i) {
  return getToken(SchrodingerMRParser::Integer, i);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Dihedral_angle_assign_by_numberContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Dihedral_angle_assign_by_numberContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Dihedral_angle_assign_by_numberContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleDihedral_angle_assign_by_number;
}


std::any SchrodingerMRParser::Dihedral_angle_assign_by_numberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_assign_by_number(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Dihedral_angle_assign_by_numberContext* SchrodingerMRParser::dihedral_angle_assign_by_number() {
  Dihedral_angle_assign_by_numberContext *_localctx = _tracker.createInstance<Dihedral_angle_assign_by_numberContext>(_ctx, getState());
  enterRule(_localctx, 22, SchrodingerMRParser::RuleDihedral_angle_assign_by_number);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(168);
    match(SchrodingerMRParser::Integer);
    setState(169);
    match(SchrodingerMRParser::Integer);
    setState(170);
    match(SchrodingerMRParser::Integer);
    setState(171);
    match(SchrodingerMRParser::Integer);
    setState(172);
    number();
    setState(173);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Angle_statementContext ------------------------------------------------------------------

SchrodingerMRParser::Angle_statementContext::Angle_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

SchrodingerMRParser::Parameter_statementContext* SchrodingerMRParser::Angle_statementContext::parameter_statement() {
  return getRuleContext<SchrodingerMRParser::Parameter_statementContext>(0);
}

tree::TerminalNode* SchrodingerMRParser::Angle_statementContext::Atom1() {
  return getToken(SchrodingerMRParser::Atom1, 0);
}

tree::TerminalNode* SchrodingerMRParser::Angle_statementContext::Atom2() {
  return getToken(SchrodingerMRParser::Atom2, 0);
}

tree::TerminalNode* SchrodingerMRParser::Angle_statementContext::Atom3() {
  return getToken(SchrodingerMRParser::Atom3, 0);
}

tree::TerminalNode* SchrodingerMRParser::Angle_statementContext::Target() {
  return getToken(SchrodingerMRParser::Target, 0);
}

tree::TerminalNode* SchrodingerMRParser::Angle_statementContext::Fc() {
  return getToken(SchrodingerMRParser::Fc, 0);
}

std::vector<SchrodingerMRParser::Angle_assignContext *> SchrodingerMRParser::Angle_statementContext::angle_assign() {
  return getRuleContexts<SchrodingerMRParser::Angle_assignContext>();
}

SchrodingerMRParser::Angle_assignContext* SchrodingerMRParser::Angle_statementContext::angle_assign(size_t i) {
  return getRuleContext<SchrodingerMRParser::Angle_assignContext>(i);
}

std::vector<SchrodingerMRParser::Angle_assign_by_numberContext *> SchrodingerMRParser::Angle_statementContext::angle_assign_by_number() {
  return getRuleContexts<SchrodingerMRParser::Angle_assign_by_numberContext>();
}

SchrodingerMRParser::Angle_assign_by_numberContext* SchrodingerMRParser::Angle_statementContext::angle_assign_by_number(size_t i) {
  return getRuleContext<SchrodingerMRParser::Angle_assign_by_numberContext>(i);
}


size_t SchrodingerMRParser::Angle_statementContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleAngle_statement;
}


std::any SchrodingerMRParser::Angle_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitAngle_statement(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Angle_statementContext* SchrodingerMRParser::angle_statement() {
  Angle_statementContext *_localctx = _tracker.createInstance<Angle_statementContext>(_ctx, getState());
  enterRule(_localctx, 24, SchrodingerMRParser::RuleAngle_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(191);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case SchrodingerMRParser::Set: {
        enterOuterAlt(_localctx, 1);
        setState(175);
        parameter_statement();
        break;
      }

      case SchrodingerMRParser::Atom1: {
        enterOuterAlt(_localctx, 2);
        setState(176);
        match(SchrodingerMRParser::Atom1);
        setState(177);
        match(SchrodingerMRParser::Atom2);
        setState(178);
        match(SchrodingerMRParser::Atom3);
        setState(179);
        match(SchrodingerMRParser::Target);
        setState(180);
        match(SchrodingerMRParser::Fc);
        break;
      }

      case SchrodingerMRParser::L_paren: {
        enterOuterAlt(_localctx, 3);
        setState(182); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(181);
          angle_assign();
          setState(184); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SchrodingerMRParser::L_paren);
        break;
      }

      case SchrodingerMRParser::Integer: {
        enterOuterAlt(_localctx, 4);
        setState(187); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(186);
          angle_assign_by_number();
          setState(189); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SchrodingerMRParser::Integer);
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

//----------------- Angle_assignContext ------------------------------------------------------------------

SchrodingerMRParser::Angle_assignContext::Angle_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<SchrodingerMRParser::SelectionContext *> SchrodingerMRParser::Angle_assignContext::selection() {
  return getRuleContexts<SchrodingerMRParser::SelectionContext>();
}

SchrodingerMRParser::SelectionContext* SchrodingerMRParser::Angle_assignContext::selection(size_t i) {
  return getRuleContext<SchrodingerMRParser::SelectionContext>(i);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Angle_assignContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Angle_assignContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Angle_assignContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleAngle_assign;
}


std::any SchrodingerMRParser::Angle_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitAngle_assign(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Angle_assignContext* SchrodingerMRParser::angle_assign() {
  Angle_assignContext *_localctx = _tracker.createInstance<Angle_assignContext>(_ctx, getState());
  enterRule(_localctx, 26, SchrodingerMRParser::RuleAngle_assign);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(193);
    selection();
    setState(194);
    selection();
    setState(195);
    selection();
    setState(196);
    number();
    setState(197);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Angle_assign_by_numberContext ------------------------------------------------------------------

SchrodingerMRParser::Angle_assign_by_numberContext::Angle_assign_by_numberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::Angle_assign_by_numberContext::Integer() {
  return getTokens(SchrodingerMRParser::Integer);
}

tree::TerminalNode* SchrodingerMRParser::Angle_assign_by_numberContext::Integer(size_t i) {
  return getToken(SchrodingerMRParser::Integer, i);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Angle_assign_by_numberContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Angle_assign_by_numberContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Angle_assign_by_numberContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleAngle_assign_by_number;
}


std::any SchrodingerMRParser::Angle_assign_by_numberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitAngle_assign_by_number(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Angle_assign_by_numberContext* SchrodingerMRParser::angle_assign_by_number() {
  Angle_assign_by_numberContext *_localctx = _tracker.createInstance<Angle_assign_by_numberContext>(_ctx, getState());
  enterRule(_localctx, 28, SchrodingerMRParser::RuleAngle_assign_by_number);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(199);
    match(SchrodingerMRParser::Integer);
    setState(200);
    match(SchrodingerMRParser::Integer);
    setState(201);
    match(SchrodingerMRParser::Integer);
    setState(202);
    number();
    setState(203);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fxdi_statementContext ------------------------------------------------------------------

SchrodingerMRParser::Fxdi_statementContext::Fxdi_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<SchrodingerMRParser::Fxdi_assignContext *> SchrodingerMRParser::Fxdi_statementContext::fxdi_assign() {
  return getRuleContexts<SchrodingerMRParser::Fxdi_assignContext>();
}

SchrodingerMRParser::Fxdi_assignContext* SchrodingerMRParser::Fxdi_statementContext::fxdi_assign(size_t i) {
  return getRuleContext<SchrodingerMRParser::Fxdi_assignContext>(i);
}

std::vector<SchrodingerMRParser::Fxdi_assign_by_numberContext *> SchrodingerMRParser::Fxdi_statementContext::fxdi_assign_by_number() {
  return getRuleContexts<SchrodingerMRParser::Fxdi_assign_by_numberContext>();
}

SchrodingerMRParser::Fxdi_assign_by_numberContext* SchrodingerMRParser::Fxdi_statementContext::fxdi_assign_by_number(size_t i) {
  return getRuleContext<SchrodingerMRParser::Fxdi_assign_by_numberContext>(i);
}


size_t SchrodingerMRParser::Fxdi_statementContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFxdi_statement;
}


std::any SchrodingerMRParser::Fxdi_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFxdi_statement(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Fxdi_statementContext* SchrodingerMRParser::fxdi_statement() {
  Fxdi_statementContext *_localctx = _tracker.createInstance<Fxdi_statementContext>(_ctx, getState());
  enterRule(_localctx, 30, SchrodingerMRParser::RuleFxdi_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    setState(215);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(206); 
      _errHandler->sync(this);
      alt = 1;
      do {
        switch (alt) {
          case 1: {
                setState(205);
                fxdi_assign();
                break;
              }

        default:
          throw NoViableAltException(this);
        }
        setState(208); 
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 12, _ctx);
      } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(211); 
      _errHandler->sync(this);
      alt = 1;
      do {
        switch (alt) {
          case 1: {
                setState(210);
                fxdi_assign_by_number();
                break;
              }

        default:
          throw NoViableAltException(this);
        }
        setState(213); 
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 13, _ctx);
      } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
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

//----------------- Fxdi_assignContext ------------------------------------------------------------------

SchrodingerMRParser::Fxdi_assignContext::Fxdi_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Fxdi_assignContext::FXDI() {
  return getToken(SchrodingerMRParser::FXDI, 0);
}

std::vector<SchrodingerMRParser::SelectionContext *> SchrodingerMRParser::Fxdi_assignContext::selection() {
  return getRuleContexts<SchrodingerMRParser::SelectionContext>();
}

SchrodingerMRParser::SelectionContext* SchrodingerMRParser::Fxdi_assignContext::selection(size_t i) {
  return getRuleContext<SchrodingerMRParser::SelectionContext>(i);
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::Fxdi_assignContext::Integer() {
  return getTokens(SchrodingerMRParser::Integer);
}

tree::TerminalNode* SchrodingerMRParser::Fxdi_assignContext::Integer(size_t i) {
  return getToken(SchrodingerMRParser::Integer, i);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Fxdi_assignContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Fxdi_assignContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Fxdi_assignContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFxdi_assign;
}


std::any SchrodingerMRParser::Fxdi_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFxdi_assign(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Fxdi_assignContext* SchrodingerMRParser::fxdi_assign() {
  Fxdi_assignContext *_localctx = _tracker.createInstance<Fxdi_assignContext>(_ctx, getState());
  enterRule(_localctx, 32, SchrodingerMRParser::RuleFxdi_assign);

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
    match(SchrodingerMRParser::FXDI);
    setState(218);
    selection();
    setState(219);
    selection();
    setState(220);
    match(SchrodingerMRParser::Integer);
    setState(221);
    match(SchrodingerMRParser::Integer);
    setState(222);
    number();
    setState(223);
    number();
    setState(224);
    number();
    setState(225);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fxdi_assign_by_numberContext ------------------------------------------------------------------

SchrodingerMRParser::Fxdi_assign_by_numberContext::Fxdi_assign_by_numberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Fxdi_assign_by_numberContext::FXDI() {
  return getToken(SchrodingerMRParser::FXDI, 0);
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::Fxdi_assign_by_numberContext::Integer() {
  return getTokens(SchrodingerMRParser::Integer);
}

tree::TerminalNode* SchrodingerMRParser::Fxdi_assign_by_numberContext::Integer(size_t i) {
  return getToken(SchrodingerMRParser::Integer, i);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Fxdi_assign_by_numberContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Fxdi_assign_by_numberContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Fxdi_assign_by_numberContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFxdi_assign_by_number;
}


std::any SchrodingerMRParser::Fxdi_assign_by_numberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFxdi_assign_by_number(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Fxdi_assign_by_numberContext* SchrodingerMRParser::fxdi_assign_by_number() {
  Fxdi_assign_by_numberContext *_localctx = _tracker.createInstance<Fxdi_assign_by_numberContext>(_ctx, getState());
  enterRule(_localctx, 34, SchrodingerMRParser::RuleFxdi_assign_by_number);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(227);
    match(SchrodingerMRParser::FXDI);
    setState(228);
    match(SchrodingerMRParser::Integer);
    setState(229);
    match(SchrodingerMRParser::Integer);
    setState(230);
    match(SchrodingerMRParser::Integer);
    setState(231);
    match(SchrodingerMRParser::Integer);
    setState(232);
    number();
    setState(233);
    number();
    setState(234);
    number();
    setState(235);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fxta_statementContext ------------------------------------------------------------------

SchrodingerMRParser::Fxta_statementContext::Fxta_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<SchrodingerMRParser::Fxta_assignContext *> SchrodingerMRParser::Fxta_statementContext::fxta_assign() {
  return getRuleContexts<SchrodingerMRParser::Fxta_assignContext>();
}

SchrodingerMRParser::Fxta_assignContext* SchrodingerMRParser::Fxta_statementContext::fxta_assign(size_t i) {
  return getRuleContext<SchrodingerMRParser::Fxta_assignContext>(i);
}

std::vector<SchrodingerMRParser::Fxta_assign_by_numberContext *> SchrodingerMRParser::Fxta_statementContext::fxta_assign_by_number() {
  return getRuleContexts<SchrodingerMRParser::Fxta_assign_by_numberContext>();
}

SchrodingerMRParser::Fxta_assign_by_numberContext* SchrodingerMRParser::Fxta_statementContext::fxta_assign_by_number(size_t i) {
  return getRuleContext<SchrodingerMRParser::Fxta_assign_by_numberContext>(i);
}


size_t SchrodingerMRParser::Fxta_statementContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFxta_statement;
}


std::any SchrodingerMRParser::Fxta_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFxta_statement(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Fxta_statementContext* SchrodingerMRParser::fxta_statement() {
  Fxta_statementContext *_localctx = _tracker.createInstance<Fxta_statementContext>(_ctx, getState());
  enterRule(_localctx, 36, SchrodingerMRParser::RuleFxta_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    setState(247);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(238); 
      _errHandler->sync(this);
      alt = 1;
      do {
        switch (alt) {
          case 1: {
                setState(237);
                fxta_assign();
                break;
              }

        default:
          throw NoViableAltException(this);
        }
        setState(240); 
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 15, _ctx);
      } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(243); 
      _errHandler->sync(this);
      alt = 1;
      do {
        switch (alt) {
          case 1: {
                setState(242);
                fxta_assign_by_number();
                break;
              }

        default:
          throw NoViableAltException(this);
        }
        setState(245); 
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 16, _ctx);
      } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
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

//----------------- Fxta_assignContext ------------------------------------------------------------------

SchrodingerMRParser::Fxta_assignContext::Fxta_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Fxta_assignContext::FXTA() {
  return getToken(SchrodingerMRParser::FXTA, 0);
}

std::vector<SchrodingerMRParser::SelectionContext *> SchrodingerMRParser::Fxta_assignContext::selection() {
  return getRuleContexts<SchrodingerMRParser::SelectionContext>();
}

SchrodingerMRParser::SelectionContext* SchrodingerMRParser::Fxta_assignContext::selection(size_t i) {
  return getRuleContext<SchrodingerMRParser::SelectionContext>(i);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Fxta_assignContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Fxta_assignContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Fxta_assignContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFxta_assign;
}


std::any SchrodingerMRParser::Fxta_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFxta_assign(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Fxta_assignContext* SchrodingerMRParser::fxta_assign() {
  Fxta_assignContext *_localctx = _tracker.createInstance<Fxta_assignContext>(_ctx, getState());
  enterRule(_localctx, 38, SchrodingerMRParser::RuleFxta_assign);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(249);
    match(SchrodingerMRParser::FXTA);
    setState(250);
    selection();
    setState(251);
    selection();
    setState(252);
    selection();
    setState(253);
    selection();
    setState(254);
    number();
    setState(255);
    number();
    setState(256);
    number();
    setState(257);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fxta_assign_by_numberContext ------------------------------------------------------------------

SchrodingerMRParser::Fxta_assign_by_numberContext::Fxta_assign_by_numberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Fxta_assign_by_numberContext::FXTA() {
  return getToken(SchrodingerMRParser::FXTA, 0);
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::Fxta_assign_by_numberContext::Integer() {
  return getTokens(SchrodingerMRParser::Integer);
}

tree::TerminalNode* SchrodingerMRParser::Fxta_assign_by_numberContext::Integer(size_t i) {
  return getToken(SchrodingerMRParser::Integer, i);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Fxta_assign_by_numberContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Fxta_assign_by_numberContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Fxta_assign_by_numberContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFxta_assign_by_number;
}


std::any SchrodingerMRParser::Fxta_assign_by_numberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFxta_assign_by_number(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Fxta_assign_by_numberContext* SchrodingerMRParser::fxta_assign_by_number() {
  Fxta_assign_by_numberContext *_localctx = _tracker.createInstance<Fxta_assign_by_numberContext>(_ctx, getState());
  enterRule(_localctx, 40, SchrodingerMRParser::RuleFxta_assign_by_number);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(259);
    match(SchrodingerMRParser::FXTA);
    setState(260);
    match(SchrodingerMRParser::Integer);
    setState(261);
    match(SchrodingerMRParser::Integer);
    setState(262);
    match(SchrodingerMRParser::Integer);
    setState(263);
    match(SchrodingerMRParser::Integer);
    setState(264);
    number();
    setState(265);
    number();
    setState(266);
    number();
    setState(267);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fxba_statementContext ------------------------------------------------------------------

SchrodingerMRParser::Fxba_statementContext::Fxba_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<SchrodingerMRParser::Fxba_assignContext *> SchrodingerMRParser::Fxba_statementContext::fxba_assign() {
  return getRuleContexts<SchrodingerMRParser::Fxba_assignContext>();
}

SchrodingerMRParser::Fxba_assignContext* SchrodingerMRParser::Fxba_statementContext::fxba_assign(size_t i) {
  return getRuleContext<SchrodingerMRParser::Fxba_assignContext>(i);
}

std::vector<SchrodingerMRParser::Fxba_assign_by_numberContext *> SchrodingerMRParser::Fxba_statementContext::fxba_assign_by_number() {
  return getRuleContexts<SchrodingerMRParser::Fxba_assign_by_numberContext>();
}

SchrodingerMRParser::Fxba_assign_by_numberContext* SchrodingerMRParser::Fxba_statementContext::fxba_assign_by_number(size_t i) {
  return getRuleContext<SchrodingerMRParser::Fxba_assign_by_numberContext>(i);
}


size_t SchrodingerMRParser::Fxba_statementContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFxba_statement;
}


std::any SchrodingerMRParser::Fxba_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFxba_statement(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Fxba_statementContext* SchrodingerMRParser::fxba_statement() {
  Fxba_statementContext *_localctx = _tracker.createInstance<Fxba_statementContext>(_ctx, getState());
  enterRule(_localctx, 42, SchrodingerMRParser::RuleFxba_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    setState(279);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 20, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(270); 
      _errHandler->sync(this);
      alt = 1;
      do {
        switch (alt) {
          case 1: {
                setState(269);
                fxba_assign();
                break;
              }

        default:
          throw NoViableAltException(this);
        }
        setState(272); 
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx);
      } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(275); 
      _errHandler->sync(this);
      alt = 1;
      do {
        switch (alt) {
          case 1: {
                setState(274);
                fxba_assign_by_number();
                break;
              }

        default:
          throw NoViableAltException(this);
        }
        setState(277); 
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 19, _ctx);
      } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
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

//----------------- Fxba_assignContext ------------------------------------------------------------------

SchrodingerMRParser::Fxba_assignContext::Fxba_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Fxba_assignContext::FXBA() {
  return getToken(SchrodingerMRParser::FXBA, 0);
}

std::vector<SchrodingerMRParser::SelectionContext *> SchrodingerMRParser::Fxba_assignContext::selection() {
  return getRuleContexts<SchrodingerMRParser::SelectionContext>();
}

SchrodingerMRParser::SelectionContext* SchrodingerMRParser::Fxba_assignContext::selection(size_t i) {
  return getRuleContext<SchrodingerMRParser::SelectionContext>(i);
}

tree::TerminalNode* SchrodingerMRParser::Fxba_assignContext::Integer() {
  return getToken(SchrodingerMRParser::Integer, 0);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Fxba_assignContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Fxba_assignContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Fxba_assignContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFxba_assign;
}


std::any SchrodingerMRParser::Fxba_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFxba_assign(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Fxba_assignContext* SchrodingerMRParser::fxba_assign() {
  Fxba_assignContext *_localctx = _tracker.createInstance<Fxba_assignContext>(_ctx, getState());
  enterRule(_localctx, 44, SchrodingerMRParser::RuleFxba_assign);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(281);
    match(SchrodingerMRParser::FXBA);
    setState(282);
    selection();
    setState(283);
    selection();
    setState(284);
    selection();
    setState(285);
    match(SchrodingerMRParser::Integer);
    setState(286);
    number();
    setState(287);
    number();
    setState(288);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fxba_assign_by_numberContext ------------------------------------------------------------------

SchrodingerMRParser::Fxba_assign_by_numberContext::Fxba_assign_by_numberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Fxba_assign_by_numberContext::FXBA() {
  return getToken(SchrodingerMRParser::FXBA, 0);
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::Fxba_assign_by_numberContext::Integer() {
  return getTokens(SchrodingerMRParser::Integer);
}

tree::TerminalNode* SchrodingerMRParser::Fxba_assign_by_numberContext::Integer(size_t i) {
  return getToken(SchrodingerMRParser::Integer, i);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Fxba_assign_by_numberContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Fxba_assign_by_numberContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Fxba_assign_by_numberContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFxba_assign_by_number;
}


std::any SchrodingerMRParser::Fxba_assign_by_numberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFxba_assign_by_number(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Fxba_assign_by_numberContext* SchrodingerMRParser::fxba_assign_by_number() {
  Fxba_assign_by_numberContext *_localctx = _tracker.createInstance<Fxba_assign_by_numberContext>(_ctx, getState());
  enterRule(_localctx, 46, SchrodingerMRParser::RuleFxba_assign_by_number);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(290);
    match(SchrodingerMRParser::FXBA);
    setState(291);
    match(SchrodingerMRParser::Integer);
    setState(292);
    match(SchrodingerMRParser::Integer);
    setState(293);
    match(SchrodingerMRParser::Integer);
    setState(294);
    match(SchrodingerMRParser::Integer);
    setState(295);
    number();
    setState(296);
    number();
    setState(297);
    number();
    setState(298);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fxhb_statementContext ------------------------------------------------------------------

SchrodingerMRParser::Fxhb_statementContext::Fxhb_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<SchrodingerMRParser::Fxhb_assignContext *> SchrodingerMRParser::Fxhb_statementContext::fxhb_assign() {
  return getRuleContexts<SchrodingerMRParser::Fxhb_assignContext>();
}

SchrodingerMRParser::Fxhb_assignContext* SchrodingerMRParser::Fxhb_statementContext::fxhb_assign(size_t i) {
  return getRuleContext<SchrodingerMRParser::Fxhb_assignContext>(i);
}

std::vector<SchrodingerMRParser::Fxhb_assign_by_numberContext *> SchrodingerMRParser::Fxhb_statementContext::fxhb_assign_by_number() {
  return getRuleContexts<SchrodingerMRParser::Fxhb_assign_by_numberContext>();
}

SchrodingerMRParser::Fxhb_assign_by_numberContext* SchrodingerMRParser::Fxhb_statementContext::fxhb_assign_by_number(size_t i) {
  return getRuleContext<SchrodingerMRParser::Fxhb_assign_by_numberContext>(i);
}


size_t SchrodingerMRParser::Fxhb_statementContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFxhb_statement;
}


std::any SchrodingerMRParser::Fxhb_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFxhb_statement(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Fxhb_statementContext* SchrodingerMRParser::fxhb_statement() {
  Fxhb_statementContext *_localctx = _tracker.createInstance<Fxhb_statementContext>(_ctx, getState());
  enterRule(_localctx, 48, SchrodingerMRParser::RuleFxhb_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    setState(310);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(301); 
      _errHandler->sync(this);
      alt = 1;
      do {
        switch (alt) {
          case 1: {
                setState(300);
                fxhb_assign();
                break;
              }

        default:
          throw NoViableAltException(this);
        }
        setState(303); 
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 21, _ctx);
      } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(306); 
      _errHandler->sync(this);
      alt = 1;
      do {
        switch (alt) {
          case 1: {
                setState(305);
                fxhb_assign_by_number();
                break;
              }

        default:
          throw NoViableAltException(this);
        }
        setState(308); 
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 22, _ctx);
      } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
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

//----------------- Fxhb_assignContext ------------------------------------------------------------------

SchrodingerMRParser::Fxhb_assignContext::Fxhb_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Fxhb_assignContext::FXHB() {
  return getToken(SchrodingerMRParser::FXHB, 0);
}

std::vector<SchrodingerMRParser::SelectionContext *> SchrodingerMRParser::Fxhb_assignContext::selection() {
  return getRuleContexts<SchrodingerMRParser::SelectionContext>();
}

SchrodingerMRParser::SelectionContext* SchrodingerMRParser::Fxhb_assignContext::selection(size_t i) {
  return getRuleContext<SchrodingerMRParser::SelectionContext>(i);
}

tree::TerminalNode* SchrodingerMRParser::Fxhb_assignContext::Integer() {
  return getToken(SchrodingerMRParser::Integer, 0);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Fxhb_assignContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Fxhb_assignContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Fxhb_assignContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFxhb_assign;
}


std::any SchrodingerMRParser::Fxhb_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFxhb_assign(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Fxhb_assignContext* SchrodingerMRParser::fxhb_assign() {
  Fxhb_assignContext *_localctx = _tracker.createInstance<Fxhb_assignContext>(_ctx, getState());
  enterRule(_localctx, 50, SchrodingerMRParser::RuleFxhb_assign);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(312);
    match(SchrodingerMRParser::FXHB);
    setState(313);
    selection();
    setState(314);
    selection();
    setState(315);
    selection();
    setState(316);
    match(SchrodingerMRParser::Integer);
    setState(317);
    number();
    setState(318);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fxhb_assign_by_numberContext ------------------------------------------------------------------

SchrodingerMRParser::Fxhb_assign_by_numberContext::Fxhb_assign_by_numberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Fxhb_assign_by_numberContext::FXHB() {
  return getToken(SchrodingerMRParser::FXHB, 0);
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::Fxhb_assign_by_numberContext::Integer() {
  return getTokens(SchrodingerMRParser::Integer);
}

tree::TerminalNode* SchrodingerMRParser::Fxhb_assign_by_numberContext::Integer(size_t i) {
  return getToken(SchrodingerMRParser::Integer, i);
}

std::vector<SchrodingerMRParser::NumberContext *> SchrodingerMRParser::Fxhb_assign_by_numberContext::number() {
  return getRuleContexts<SchrodingerMRParser::NumberContext>();
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::Fxhb_assign_by_numberContext::number(size_t i) {
  return getRuleContext<SchrodingerMRParser::NumberContext>(i);
}


size_t SchrodingerMRParser::Fxhb_assign_by_numberContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFxhb_assign_by_number;
}


std::any SchrodingerMRParser::Fxhb_assign_by_numberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFxhb_assign_by_number(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Fxhb_assign_by_numberContext* SchrodingerMRParser::fxhb_assign_by_number() {
  Fxhb_assign_by_numberContext *_localctx = _tracker.createInstance<Fxhb_assign_by_numberContext>(_ctx, getState());
  enterRule(_localctx, 52, SchrodingerMRParser::RuleFxhb_assign_by_number);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(320);
    match(SchrodingerMRParser::FXHB);
    setState(321);
    match(SchrodingerMRParser::Integer);
    setState(322);
    match(SchrodingerMRParser::Integer);
    setState(323);
    match(SchrodingerMRParser::Integer);
    setState(324);
    match(SchrodingerMRParser::Integer);
    setState(325);
    number();
    setState(326);
    number();
    setState(327);
    number();
    setState(328);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- SelectionContext ------------------------------------------------------------------

SchrodingerMRParser::SelectionContext::SelectionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::SelectionContext::L_paren() {
  return getToken(SchrodingerMRParser::L_paren, 0);
}

SchrodingerMRParser::Selection_expressionContext* SchrodingerMRParser::SelectionContext::selection_expression() {
  return getRuleContext<SchrodingerMRParser::Selection_expressionContext>(0);
}

tree::TerminalNode* SchrodingerMRParser::SelectionContext::R_paren() {
  return getToken(SchrodingerMRParser::R_paren, 0);
}


size_t SchrodingerMRParser::SelectionContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleSelection;
}


std::any SchrodingerMRParser::SelectionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitSelection(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::SelectionContext* SchrodingerMRParser::selection() {
  SelectionContext *_localctx = _tracker.createInstance<SelectionContext>(_ctx, getState());
  enterRule(_localctx, 54, SchrodingerMRParser::RuleSelection);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(330);
    match(SchrodingerMRParser::L_paren);
    setState(331);
    selection_expression();
    setState(332);
    match(SchrodingerMRParser::R_paren);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Selection_expressionContext ------------------------------------------------------------------

SchrodingerMRParser::Selection_expressionContext::Selection_expressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<SchrodingerMRParser::TermContext *> SchrodingerMRParser::Selection_expressionContext::term() {
  return getRuleContexts<SchrodingerMRParser::TermContext>();
}

SchrodingerMRParser::TermContext* SchrodingerMRParser::Selection_expressionContext::term(size_t i) {
  return getRuleContext<SchrodingerMRParser::TermContext>(i);
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::Selection_expressionContext::Or_op() {
  return getTokens(SchrodingerMRParser::Or_op);
}

tree::TerminalNode* SchrodingerMRParser::Selection_expressionContext::Or_op(size_t i) {
  return getToken(SchrodingerMRParser::Or_op, i);
}


size_t SchrodingerMRParser::Selection_expressionContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleSelection_expression;
}


std::any SchrodingerMRParser::Selection_expressionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitSelection_expression(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Selection_expressionContext* SchrodingerMRParser::selection_expression() {
  Selection_expressionContext *_localctx = _tracker.createInstance<Selection_expressionContext>(_ctx, getState());
  enterRule(_localctx, 56, SchrodingerMRParser::RuleSelection_expression);
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
    setState(334);
    term();
    setState(339);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == SchrodingerMRParser::Or_op) {
      setState(335);
      match(SchrodingerMRParser::Or_op);
      setState(336);
      term();
      setState(341);
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

//----------------- TermContext ------------------------------------------------------------------

SchrodingerMRParser::TermContext::TermContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<SchrodingerMRParser::FactorContext *> SchrodingerMRParser::TermContext::factor() {
  return getRuleContexts<SchrodingerMRParser::FactorContext>();
}

SchrodingerMRParser::FactorContext* SchrodingerMRParser::TermContext::factor(size_t i) {
  return getRuleContext<SchrodingerMRParser::FactorContext>(i);
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::TermContext::And_op() {
  return getTokens(SchrodingerMRParser::And_op);
}

tree::TerminalNode* SchrodingerMRParser::TermContext::And_op(size_t i) {
  return getToken(SchrodingerMRParser::And_op, i);
}


size_t SchrodingerMRParser::TermContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleTerm;
}


std::any SchrodingerMRParser::TermContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitTerm(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::TermContext* SchrodingerMRParser::term() {
  TermContext *_localctx = _tracker.createInstance<TermContext>(_ctx, getState());
  enterRule(_localctx, 58, SchrodingerMRParser::RuleTerm);
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
    setState(342);
    factor();
    setState(349);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 26, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(344);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == SchrodingerMRParser::And_op) {
          setState(343);
          match(SchrodingerMRParser::And_op);
        }
        setState(346);
        factor(); 
      }
      setState(351);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 26, _ctx);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- FactorContext ------------------------------------------------------------------

SchrodingerMRParser::FactorContext::FactorContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::L_paren() {
  return getToken(SchrodingerMRParser::L_paren, 0);
}

SchrodingerMRParser::Selection_expressionContext* SchrodingerMRParser::FactorContext::selection_expression() {
  return getRuleContext<SchrodingerMRParser::Selection_expressionContext>(0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::R_paren() {
  return getToken(SchrodingerMRParser::R_paren, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Entry() {
  return getToken(SchrodingerMRParser::Entry, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Entry_name() {
  return getToken(SchrodingerMRParser::Entry_name, 0);
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::FactorContext::Simple_names() {
  return getTokens(SchrodingerMRParser::Simple_names);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Simple_names(size_t i) {
  return getToken(SchrodingerMRParser::Simple_names, i);
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::FactorContext::Simple_name() {
  return getTokens(SchrodingerMRParser::Simple_name);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Simple_name(size_t i) {
  return getToken(SchrodingerMRParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::FactorContext::Comma() {
  return getTokens(SchrodingerMRParser::Comma);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Comma(size_t i) {
  return getToken(SchrodingerMRParser::Comma, i);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Molecule() {
  return getToken(SchrodingerMRParser::Molecule, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Molecule_number() {
  return getToken(SchrodingerMRParser::Molecule_number, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Integers() {
  return getToken(SchrodingerMRParser::Integers, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::IntRange() {
  return getToken(SchrodingerMRParser::IntRange, 0);
}

std::vector<tree::TerminalNode *> SchrodingerMRParser::FactorContext::Integer() {
  return getTokens(SchrodingerMRParser::Integer);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Integer(size_t i) {
  return getToken(SchrodingerMRParser::Integer, i);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Molecule_modulo() {
  return getToken(SchrodingerMRParser::Molecule_modulo, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Molecule_entrynum() {
  return getToken(SchrodingerMRParser::Molecule_entrynum, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Molecule_atoms() {
  return getToken(SchrodingerMRParser::Molecule_atoms, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Equ_op() {
  return getToken(SchrodingerMRParser::Equ_op, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Lt_op() {
  return getToken(SchrodingerMRParser::Lt_op, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Gt_op() {
  return getToken(SchrodingerMRParser::Gt_op, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Leq_op() {
  return getToken(SchrodingerMRParser::Leq_op, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Geq_op() {
  return getToken(SchrodingerMRParser::Geq_op, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Molecule_weight() {
  return getToken(SchrodingerMRParser::Molecule_weight, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Chain() {
  return getToken(SchrodingerMRParser::Chain, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Chain_name() {
  return getToken(SchrodingerMRParser::Chain_name, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Residue() {
  return getToken(SchrodingerMRParser::Residue, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Residue_name_or_number() {
  return getToken(SchrodingerMRParser::Residue_name_or_number, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Residue_ptype() {
  return getToken(SchrodingerMRParser::Residue_ptype, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Residue_mtype() {
  return getToken(SchrodingerMRParser::Residue_mtype, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Residue_polarity() {
  return getToken(SchrodingerMRParser::Residue_polarity, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Hydrophilic() {
  return getToken(SchrodingerMRParser::Hydrophilic, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Hydrophobic() {
  return getToken(SchrodingerMRParser::Hydrophobic, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Non_polar() {
  return getToken(SchrodingerMRParser::Non_polar, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Polar() {
  return getToken(SchrodingerMRParser::Polar, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Charged() {
  return getToken(SchrodingerMRParser::Charged, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Positive() {
  return getToken(SchrodingerMRParser::Positive, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Negative() {
  return getToken(SchrodingerMRParser::Negative, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Residue_secondary_structure() {
  return getToken(SchrodingerMRParser::Residue_secondary_structure, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Helix_or_strand() {
  return getToken(SchrodingerMRParser::Helix_or_strand, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Strand_or_loop() {
  return getToken(SchrodingerMRParser::Strand_or_loop, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Helix_or_loop() {
  return getToken(SchrodingerMRParser::Helix_or_loop, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Helix() {
  return getToken(SchrodingerMRParser::Helix, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Strand() {
  return getToken(SchrodingerMRParser::Strand, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Loop() {
  return getToken(SchrodingerMRParser::Loop, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Residue_position() {
  return getToken(SchrodingerMRParser::Residue_position, 0);
}

std::vector<SchrodingerMRParser::Number_fContext *> SchrodingerMRParser::FactorContext::number_f() {
  return getRuleContexts<SchrodingerMRParser::Number_fContext>();
}

SchrodingerMRParser::Number_fContext* SchrodingerMRParser::FactorContext::number_f(size_t i) {
  return getRuleContext<SchrodingerMRParser::Number_fContext>(i);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Residue_inscode() {
  return getToken(SchrodingerMRParser::Residue_inscode, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_ptype() {
  return getToken(SchrodingerMRParser::Atom_ptype, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_name() {
  return getToken(SchrodingerMRParser::Atom_name, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom() {
  return getToken(SchrodingerMRParser::Atom, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_number() {
  return getToken(SchrodingerMRParser::Atom_number, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_molnum() {
  return getToken(SchrodingerMRParser::Atom_molnum, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_entrynum() {
  return getToken(SchrodingerMRParser::Atom_entrynum, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_mtype() {
  return getToken(SchrodingerMRParser::Atom_mtype, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_element() {
  return getToken(SchrodingerMRParser::Atom_element, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_attachements() {
  return getToken(SchrodingerMRParser::Atom_attachements, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_atomicnumber() {
  return getToken(SchrodingerMRParser::Atom_atomicnumber, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_charge() {
  return getToken(SchrodingerMRParser::Atom_charge, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::FloatRange() {
  return getToken(SchrodingerMRParser::FloatRange, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Float() {
  return getToken(SchrodingerMRParser::Float, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_formalcharge() {
  return getToken(SchrodingerMRParser::Atom_formalcharge, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_displayed() {
  return getToken(SchrodingerMRParser::Atom_displayed, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Atom_selected() {
  return getToken(SchrodingerMRParser::Atom_selected, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Fillres_op() {
  return getToken(SchrodingerMRParser::Fillres_op, 0);
}

SchrodingerMRParser::FactorContext* SchrodingerMRParser::FactorContext::factor() {
  return getRuleContext<SchrodingerMRParser::FactorContext>(0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Fillmol_op() {
  return getToken(SchrodingerMRParser::Fillmol_op, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Within_op() {
  return getToken(SchrodingerMRParser::Within_op, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Beyond_op() {
  return getToken(SchrodingerMRParser::Beyond_op, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Withinbonds_op() {
  return getToken(SchrodingerMRParser::Withinbonds_op, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Beyondbonds_op() {
  return getToken(SchrodingerMRParser::Beyondbonds_op, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Backbone() {
  return getToken(SchrodingerMRParser::Backbone, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Sidechain() {
  return getToken(SchrodingerMRParser::Sidechain, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Water() {
  return getToken(SchrodingerMRParser::Water, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Methyl() {
  return getToken(SchrodingerMRParser::Methyl, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Amide() {
  return getToken(SchrodingerMRParser::Amide, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Smarts() {
  return getToken(SchrodingerMRParser::Smarts, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Slash_quote_string() {
  return getToken(SchrodingerMRParser::Slash_quote_string, 0);
}

tree::TerminalNode* SchrodingerMRParser::FactorContext::Not_op() {
  return getToken(SchrodingerMRParser::Not_op, 0);
}


size_t SchrodingerMRParser::FactorContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleFactor;
}


std::any SchrodingerMRParser::FactorContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitFactor(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::FactorContext* SchrodingerMRParser::factor() {
  FactorContext *_localctx = _tracker.createInstance<FactorContext>(_ctx, getState());
  enterRule(_localctx, 60, SchrodingerMRParser::RuleFactor);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(582);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case SchrodingerMRParser::L_paren: {
        enterOuterAlt(_localctx, 1);
        setState(352);
        match(SchrodingerMRParser::L_paren);
        setState(353);
        selection_expression();
        setState(354);
        match(SchrodingerMRParser::R_paren);
        break;
      }

      case SchrodingerMRParser::Entry:
      case SchrodingerMRParser::Entry_name: {
        enterOuterAlt(_localctx, 2);
        setState(356);
        _la = _input->LA(1);
        if (!(_la == SchrodingerMRParser::Entry

        || _la == SchrodingerMRParser::Entry_name)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }

        setState(357);
        _la = _input->LA(1);
        if (!(_la == SchrodingerMRParser::Simple_name

        || _la == SchrodingerMRParser::Simple_names)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(362);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == SchrodingerMRParser::Comma) {
          setState(358);
          match(SchrodingerMRParser::Comma);
          setState(359);
          _la = _input->LA(1);
          if (!(_la == SchrodingerMRParser::Simple_name

          || _la == SchrodingerMRParser::Simple_names)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(364);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        break;
      }

      case SchrodingerMRParser::Molecule:
      case SchrodingerMRParser::Molecule_number: {
        enterOuterAlt(_localctx, 3);
        setState(365);
        _la = _input->LA(1);
        if (!(_la == SchrodingerMRParser::Molecule

        || _la == SchrodingerMRParser::Molecule_number)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(376);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case SchrodingerMRParser::Integers: {
            setState(366);
            match(SchrodingerMRParser::Integers);
            break;
          }

          case SchrodingerMRParser::IntRange: {
            setState(367);
            match(SchrodingerMRParser::IntRange);
            break;
          }

          case SchrodingerMRParser::Integer: {
            setState(368);
            match(SchrodingerMRParser::Integer);
            setState(373);
            _errHandler->sync(this);
            _la = _input->LA(1);
            while (_la == SchrodingerMRParser::Comma) {
              setState(369);
              match(SchrodingerMRParser::Comma);
              setState(370);
              match(SchrodingerMRParser::Integer);
              setState(375);
              _errHandler->sync(this);
              _la = _input->LA(1);
            }
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case SchrodingerMRParser::Molecule_modulo: {
        enterOuterAlt(_localctx, 4);
        setState(378);
        match(SchrodingerMRParser::Molecule_modulo);
        setState(379);
        match(SchrodingerMRParser::Integer);
        setState(380);
        match(SchrodingerMRParser::Integer);
        break;
      }

      case SchrodingerMRParser::Molecule_entrynum: {
        enterOuterAlt(_localctx, 5);
        setState(381);
        match(SchrodingerMRParser::Molecule_entrynum);
        setState(382);
        match(SchrodingerMRParser::Integer);
        break;
      }

      case SchrodingerMRParser::Molecule_atoms: {
        enterOuterAlt(_localctx, 6);
        setState(383);
        match(SchrodingerMRParser::Molecule_atoms);
        setState(388);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case SchrodingerMRParser::IntRange: {
            setState(384);
            match(SchrodingerMRParser::IntRange);
            break;
          }

          case SchrodingerMRParser::Integer: {
            setState(385);
            match(SchrodingerMRParser::Integer);
            break;
          }

          case SchrodingerMRParser::Lt_op:
          case SchrodingerMRParser::Gt_op:
          case SchrodingerMRParser::Leq_op:
          case SchrodingerMRParser::Geq_op:
          case SchrodingerMRParser::Equ_op: {
            setState(386);
            _la = _input->LA(1);
            if (!(((((_la - 79) & ~ 0x3fULL) == 0) &&
              ((1ULL << (_la - 79)) & 31) != 0))) {
            _errHandler->recoverInline(this);
            }
            else {
              _errHandler->reportMatch(this);
              consume();
            }
            setState(387);
            match(SchrodingerMRParser::Integer);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case SchrodingerMRParser::Molecule_weight: {
        enterOuterAlt(_localctx, 7);
        setState(390);
        match(SchrodingerMRParser::Molecule_weight);
        setState(395);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case SchrodingerMRParser::IntRange: {
            setState(391);
            match(SchrodingerMRParser::IntRange);
            break;
          }

          case SchrodingerMRParser::Integer: {
            setState(392);
            match(SchrodingerMRParser::Integer);
            break;
          }

          case SchrodingerMRParser::Lt_op:
          case SchrodingerMRParser::Gt_op:
          case SchrodingerMRParser::Leq_op:
          case SchrodingerMRParser::Geq_op:
          case SchrodingerMRParser::Equ_op: {
            setState(393);
            _la = _input->LA(1);
            if (!(((((_la - 79) & ~ 0x3fULL) == 0) &&
              ((1ULL << (_la - 79)) & 31) != 0))) {
            _errHandler->recoverInline(this);
            }
            else {
              _errHandler->reportMatch(this);
              consume();
            }
            setState(394);
            match(SchrodingerMRParser::Integer);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case SchrodingerMRParser::Chain:
      case SchrodingerMRParser::Chain_name: {
        enterOuterAlt(_localctx, 8);
        setState(397);
        _la = _input->LA(1);
        if (!(_la == SchrodingerMRParser::Chain

        || _la == SchrodingerMRParser::Chain_name)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }

        setState(398);
        _la = _input->LA(1);
        if (!(((((_la - 67) & ~ 0x3fULL) == 0) &&
          ((1ULL << (_la - 67)) & 385) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(403);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == SchrodingerMRParser::Comma) {
          setState(399);
          match(SchrodingerMRParser::Comma);
          setState(400);
          _la = _input->LA(1);
          if (!(((((_la - 67) & ~ 0x3fULL) == 0) &&
            ((1ULL << (_la - 67)) & 385) != 0))) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(405);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        break;
      }

      case SchrodingerMRParser::Residue:
      case SchrodingerMRParser::Residue_name_or_number: {
        enterOuterAlt(_localctx, 9);
        setState(406);
        _la = _input->LA(1);
        if (!(_la == SchrodingerMRParser::Residue

        || _la == SchrodingerMRParser::Residue_name_or_number)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(421);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case SchrodingerMRParser::Integer:
          case SchrodingerMRParser::IntRange:
          case SchrodingerMRParser::Lt_op:
          case SchrodingerMRParser::Gt_op:
          case SchrodingerMRParser::Leq_op:
          case SchrodingerMRParser::Geq_op:
          case SchrodingerMRParser::Equ_op: {
            setState(411);
            _errHandler->sync(this);
            switch (_input->LA(1)) {
              case SchrodingerMRParser::IntRange: {
                setState(407);
                match(SchrodingerMRParser::IntRange);
                break;
              }

              case SchrodingerMRParser::Integer: {
                setState(408);
                match(SchrodingerMRParser::Integer);
                break;
              }

              case SchrodingerMRParser::Lt_op:
              case SchrodingerMRParser::Gt_op:
              case SchrodingerMRParser::Leq_op:
              case SchrodingerMRParser::Geq_op:
              case SchrodingerMRParser::Equ_op: {
                setState(409);
                _la = _input->LA(1);
                if (!(((((_la - 79) & ~ 0x3fULL) == 0) &&
                  ((1ULL << (_la - 79)) & 31) != 0))) {
                _errHandler->recoverInline(this);
                }
                else {
                  _errHandler->reportMatch(this);
                  consume();
                }
                setState(410);
                match(SchrodingerMRParser::Integer);
                break;
              }

            default:
              throw NoViableAltException(this);
            }
            break;
          }

          case SchrodingerMRParser::Simple_name:
          case SchrodingerMRParser::Simple_names: {
            setState(413);
            _la = _input->LA(1);
            if (!(_la == SchrodingerMRParser::Simple_name

            || _la == SchrodingerMRParser::Simple_names)) {
            _errHandler->recoverInline(this);
            }
            else {
              _errHandler->reportMatch(this);
              consume();
            }
            setState(418);
            _errHandler->sync(this);
            _la = _input->LA(1);
            while (_la == SchrodingerMRParser::Comma) {
              setState(414);
              match(SchrodingerMRParser::Comma);
              setState(415);
              _la = _input->LA(1);
              if (!(_la == SchrodingerMRParser::Simple_name

              || _la == SchrodingerMRParser::Simple_names)) {
              _errHandler->recoverInline(this);
              }
              else {
                _errHandler->reportMatch(this);
                consume();
              }
              setState(420);
              _errHandler->sync(this);
              _la = _input->LA(1);
            }
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case SchrodingerMRParser::Residue_ptype: {
        enterOuterAlt(_localctx, 10);
        setState(423);
        match(SchrodingerMRParser::Residue_ptype);

        setState(424);
        _la = _input->LA(1);
        if (!(_la == SchrodingerMRParser::Simple_name

        || _la == SchrodingerMRParser::Simple_names)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(429);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == SchrodingerMRParser::Comma) {
          setState(425);
          match(SchrodingerMRParser::Comma);
          setState(426);
          _la = _input->LA(1);
          if (!(_la == SchrodingerMRParser::Simple_name

          || _la == SchrodingerMRParser::Simple_names)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(431);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        break;
      }

      case SchrodingerMRParser::Residue_mtype: {
        enterOuterAlt(_localctx, 11);
        setState(432);
        match(SchrodingerMRParser::Residue_mtype);

        setState(433);
        _la = _input->LA(1);
        if (!(_la == SchrodingerMRParser::Simple_name

        || _la == SchrodingerMRParser::Simple_names)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(438);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == SchrodingerMRParser::Comma) {
          setState(434);
          match(SchrodingerMRParser::Comma);
          setState(435);
          _la = _input->LA(1);
          if (!(_la == SchrodingerMRParser::Simple_name

          || _la == SchrodingerMRParser::Simple_names)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(440);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        break;
      }

      case SchrodingerMRParser::Residue_polarity: {
        enterOuterAlt(_localctx, 12);
        setState(441);
        match(SchrodingerMRParser::Residue_polarity);
        setState(442);
        _la = _input->LA(1);
        if (!(((((_la - 93) & ~ 0x3fULL) == 0) &&
          ((1ULL << (_la - 93)) & 127) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        break;
      }

      case SchrodingerMRParser::Residue_secondary_structure: {
        enterOuterAlt(_localctx, 13);
        setState(443);
        match(SchrodingerMRParser::Residue_secondary_structure);
        setState(444);
        _la = _input->LA(1);
        if (!(((((_la - 101) & ~ 0x3fULL) == 0) &&
          ((1ULL << (_la - 101)) & 63) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        break;
      }

      case SchrodingerMRParser::Residue_position: {
        enterOuterAlt(_localctx, 14);
        setState(445);
        match(SchrodingerMRParser::Residue_position);
        setState(446);
        number_f();
        setState(447);
        number_f();
        break;
      }

      case SchrodingerMRParser::Residue_inscode: {
        enterOuterAlt(_localctx, 15);
        setState(449);
        match(SchrodingerMRParser::Residue_inscode);
        setState(450);
        match(SchrodingerMRParser::Simple_name);
        break;
      }

      case SchrodingerMRParser::Atom_ptype: {
        enterOuterAlt(_localctx, 16);
        setState(451);
        match(SchrodingerMRParser::Atom_ptype);

        setState(452);
        _la = _input->LA(1);
        if (!(_la == SchrodingerMRParser::Simple_name

        || _la == SchrodingerMRParser::Simple_names)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(457);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == SchrodingerMRParser::Comma) {
          setState(453);
          match(SchrodingerMRParser::Comma);
          setState(454);
          _la = _input->LA(1);
          if (!(_la == SchrodingerMRParser::Simple_name

          || _la == SchrodingerMRParser::Simple_names)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(459);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        break;
      }

      case SchrodingerMRParser::Atom_name: {
        enterOuterAlt(_localctx, 17);
        setState(460);
        match(SchrodingerMRParser::Atom_name);

        setState(461);
        _la = _input->LA(1);
        if (!(_la == SchrodingerMRParser::Simple_name

        || _la == SchrodingerMRParser::Simple_names)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(466);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == SchrodingerMRParser::Comma) {
          setState(462);
          match(SchrodingerMRParser::Comma);
          setState(463);
          _la = _input->LA(1);
          if (!(_la == SchrodingerMRParser::Simple_name

          || _la == SchrodingerMRParser::Simple_names)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(468);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        break;
      }

      case SchrodingerMRParser::Atom:
      case SchrodingerMRParser::Atom_number: {
        enterOuterAlt(_localctx, 18);
        setState(469);
        _la = _input->LA(1);
        if (!(_la == SchrodingerMRParser::Atom

        || _la == SchrodingerMRParser::Atom_number)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(479);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case SchrodingerMRParser::IntRange: {
            setState(470);
            match(SchrodingerMRParser::IntRange);
            break;
          }

          case SchrodingerMRParser::Integer: {
            setState(471);
            match(SchrodingerMRParser::Integer);
            setState(476);
            _errHandler->sync(this);
            _la = _input->LA(1);
            while (_la == SchrodingerMRParser::Comma) {
              setState(472);
              match(SchrodingerMRParser::Comma);
              setState(473);
              match(SchrodingerMRParser::Integer);
              setState(478);
              _errHandler->sync(this);
              _la = _input->LA(1);
            }
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case SchrodingerMRParser::Atom_molnum: {
        enterOuterAlt(_localctx, 19);
        setState(481);
        match(SchrodingerMRParser::Atom_molnum);
        setState(491);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case SchrodingerMRParser::IntRange: {
            setState(482);
            match(SchrodingerMRParser::IntRange);
            break;
          }

          case SchrodingerMRParser::Integer: {
            setState(483);
            match(SchrodingerMRParser::Integer);
            setState(488);
            _errHandler->sync(this);
            _la = _input->LA(1);
            while (_la == SchrodingerMRParser::Comma) {
              setState(484);
              match(SchrodingerMRParser::Comma);
              setState(485);
              match(SchrodingerMRParser::Integer);
              setState(490);
              _errHandler->sync(this);
              _la = _input->LA(1);
            }
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case SchrodingerMRParser::Atom_entrynum: {
        enterOuterAlt(_localctx, 20);
        setState(493);
        match(SchrodingerMRParser::Atom_entrynum);
        setState(503);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case SchrodingerMRParser::IntRange: {
            setState(494);
            match(SchrodingerMRParser::IntRange);
            break;
          }

          case SchrodingerMRParser::Integer: {
            setState(495);
            match(SchrodingerMRParser::Integer);
            setState(500);
            _errHandler->sync(this);
            _la = _input->LA(1);
            while (_la == SchrodingerMRParser::Comma) {
              setState(496);
              match(SchrodingerMRParser::Comma);
              setState(497);
              match(SchrodingerMRParser::Integer);
              setState(502);
              _errHandler->sync(this);
              _la = _input->LA(1);
            }
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case SchrodingerMRParser::Atom_mtype: {
        enterOuterAlt(_localctx, 21);
        setState(505);
        match(SchrodingerMRParser::Atom_mtype);

        setState(506);
        _la = _input->LA(1);
        if (!(_la == SchrodingerMRParser::Simple_name

        || _la == SchrodingerMRParser::Simple_names)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(511);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == SchrodingerMRParser::Comma) {
          setState(507);
          match(SchrodingerMRParser::Comma);
          setState(508);
          _la = _input->LA(1);
          if (!(_la == SchrodingerMRParser::Simple_name

          || _la == SchrodingerMRParser::Simple_names)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(513);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        break;
      }

      case SchrodingerMRParser::Atom_element: {
        enterOuterAlt(_localctx, 22);
        setState(514);
        match(SchrodingerMRParser::Atom_element);

        setState(515);
        _la = _input->LA(1);
        if (!(_la == SchrodingerMRParser::Simple_name

        || _la == SchrodingerMRParser::Simple_names)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(520);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == SchrodingerMRParser::Comma) {
          setState(516);
          match(SchrodingerMRParser::Comma);
          setState(517);
          _la = _input->LA(1);
          if (!(_la == SchrodingerMRParser::Simple_name

          || _la == SchrodingerMRParser::Simple_names)) {
          _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(522);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        break;
      }

      case SchrodingerMRParser::Atom_attachements: {
        enterOuterAlt(_localctx, 23);
        setState(523);
        match(SchrodingerMRParser::Atom_attachements);
        setState(528);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case SchrodingerMRParser::IntRange: {
            setState(524);
            match(SchrodingerMRParser::IntRange);
            break;
          }

          case SchrodingerMRParser::Integer: {
            setState(525);
            match(SchrodingerMRParser::Integer);
            break;
          }

          case SchrodingerMRParser::Lt_op:
          case SchrodingerMRParser::Gt_op:
          case SchrodingerMRParser::Leq_op:
          case SchrodingerMRParser::Geq_op:
          case SchrodingerMRParser::Equ_op: {
            setState(526);
            _la = _input->LA(1);
            if (!(((((_la - 79) & ~ 0x3fULL) == 0) &&
              ((1ULL << (_la - 79)) & 31) != 0))) {
            _errHandler->recoverInline(this);
            }
            else {
              _errHandler->reportMatch(this);
              consume();
            }
            setState(527);
            match(SchrodingerMRParser::Integer);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case SchrodingerMRParser::Atom_atomicnumber: {
        enterOuterAlt(_localctx, 24);
        setState(530);
        match(SchrodingerMRParser::Atom_atomicnumber);
        setState(535);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case SchrodingerMRParser::IntRange: {
            setState(531);
            match(SchrodingerMRParser::IntRange);
            break;
          }

          case SchrodingerMRParser::Integer: {
            setState(532);
            match(SchrodingerMRParser::Integer);
            break;
          }

          case SchrodingerMRParser::Lt_op:
          case SchrodingerMRParser::Gt_op:
          case SchrodingerMRParser::Leq_op:
          case SchrodingerMRParser::Geq_op:
          case SchrodingerMRParser::Equ_op: {
            setState(533);
            _la = _input->LA(1);
            if (!(((((_la - 79) & ~ 0x3fULL) == 0) &&
              ((1ULL << (_la - 79)) & 31) != 0))) {
            _errHandler->recoverInline(this);
            }
            else {
              _errHandler->reportMatch(this);
              consume();
            }
            setState(534);
            match(SchrodingerMRParser::Integer);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case SchrodingerMRParser::Atom_charge: {
        enterOuterAlt(_localctx, 25);
        setState(537);
        match(SchrodingerMRParser::Atom_charge);
        setState(542);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case SchrodingerMRParser::FloatRange: {
            setState(538);
            match(SchrodingerMRParser::FloatRange);
            break;
          }

          case SchrodingerMRParser::Float: {
            setState(539);
            match(SchrodingerMRParser::Float);
            break;
          }

          case SchrodingerMRParser::Lt_op:
          case SchrodingerMRParser::Gt_op:
          case SchrodingerMRParser::Leq_op:
          case SchrodingerMRParser::Geq_op:
          case SchrodingerMRParser::Equ_op: {
            setState(540);
            _la = _input->LA(1);
            if (!(((((_la - 79) & ~ 0x3fULL) == 0) &&
              ((1ULL << (_la - 79)) & 31) != 0))) {
            _errHandler->recoverInline(this);
            }
            else {
              _errHandler->reportMatch(this);
              consume();
            }
            setState(541);
            match(SchrodingerMRParser::Float);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case SchrodingerMRParser::Atom_formalcharge: {
        enterOuterAlt(_localctx, 26);
        setState(544);
        match(SchrodingerMRParser::Atom_formalcharge);
        setState(549);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case SchrodingerMRParser::IntRange: {
            setState(545);
            match(SchrodingerMRParser::IntRange);
            break;
          }

          case SchrodingerMRParser::Integer: {
            setState(546);
            match(SchrodingerMRParser::Integer);
            break;
          }

          case SchrodingerMRParser::Lt_op:
          case SchrodingerMRParser::Gt_op:
          case SchrodingerMRParser::Leq_op:
          case SchrodingerMRParser::Geq_op:
          case SchrodingerMRParser::Equ_op: {
            setState(547);
            _la = _input->LA(1);
            if (!(((((_la - 79) & ~ 0x3fULL) == 0) &&
              ((1ULL << (_la - 79)) & 31) != 0))) {
            _errHandler->recoverInline(this);
            }
            else {
              _errHandler->reportMatch(this);
              consume();
            }
            setState(548);
            match(SchrodingerMRParser::Integer);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case SchrodingerMRParser::Atom_displayed: {
        enterOuterAlt(_localctx, 27);
        setState(551);
        match(SchrodingerMRParser::Atom_displayed);
        break;
      }

      case SchrodingerMRParser::Atom_selected: {
        enterOuterAlt(_localctx, 28);
        setState(552);
        match(SchrodingerMRParser::Atom_selected);
        break;
      }

      case SchrodingerMRParser::Fillres_op: {
        enterOuterAlt(_localctx, 29);
        setState(553);
        match(SchrodingerMRParser::Fillres_op);
        setState(554);
        factor();
        break;
      }

      case SchrodingerMRParser::Fillmol_op: {
        enterOuterAlt(_localctx, 30);
        setState(555);
        match(SchrodingerMRParser::Fillmol_op);
        setState(556);
        factor();
        break;
      }

      case SchrodingerMRParser::Within_op: {
        enterOuterAlt(_localctx, 31);
        setState(557);
        match(SchrodingerMRParser::Within_op);
        setState(558);
        number_f();
        setState(559);
        factor();
        break;
      }

      case SchrodingerMRParser::Beyond_op: {
        enterOuterAlt(_localctx, 32);
        setState(561);
        match(SchrodingerMRParser::Beyond_op);
        setState(562);
        number_f();
        setState(563);
        factor();
        break;
      }

      case SchrodingerMRParser::Withinbonds_op: {
        enterOuterAlt(_localctx, 33);
        setState(565);
        match(SchrodingerMRParser::Withinbonds_op);
        setState(566);
        match(SchrodingerMRParser::Integer);
        setState(567);
        factor();
        break;
      }

      case SchrodingerMRParser::Beyondbonds_op: {
        enterOuterAlt(_localctx, 34);
        setState(568);
        match(SchrodingerMRParser::Beyondbonds_op);
        setState(569);
        match(SchrodingerMRParser::Integer);
        setState(570);
        factor();
        break;
      }

      case SchrodingerMRParser::Backbone: {
        enterOuterAlt(_localctx, 35);
        setState(571);
        match(SchrodingerMRParser::Backbone);
        break;
      }

      case SchrodingerMRParser::Sidechain: {
        enterOuterAlt(_localctx, 36);
        setState(572);
        match(SchrodingerMRParser::Sidechain);
        break;
      }

      case SchrodingerMRParser::Water: {
        enterOuterAlt(_localctx, 37);
        setState(573);
        match(SchrodingerMRParser::Water);
        break;
      }

      case SchrodingerMRParser::Methyl: {
        enterOuterAlt(_localctx, 38);
        setState(574);
        match(SchrodingerMRParser::Methyl);
        break;
      }

      case SchrodingerMRParser::Amide: {
        enterOuterAlt(_localctx, 39);
        setState(575);
        match(SchrodingerMRParser::Amide);
        break;
      }

      case SchrodingerMRParser::Smarts: {
        enterOuterAlt(_localctx, 40);
        setState(576);
        match(SchrodingerMRParser::Smarts);
        setState(577);
        match(SchrodingerMRParser::Simple_name);
        break;
      }

      case SchrodingerMRParser::Slash_quote_string: {
        enterOuterAlt(_localctx, 41);
        setState(578);
        match(SchrodingerMRParser::Slash_quote_string);
        break;
      }

      case SchrodingerMRParser::Not_op: {
        enterOuterAlt(_localctx, 42);
        setState(579);
        match(SchrodingerMRParser::Not_op);
        setState(580);
        factor();
        break;
      }

      case SchrodingerMRParser::Simple_name: {
        enterOuterAlt(_localctx, 43);
        setState(581);
        match(SchrodingerMRParser::Simple_name);
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

//----------------- NumberContext ------------------------------------------------------------------

SchrodingerMRParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::NumberContext::Float() {
  return getToken(SchrodingerMRParser::Float, 0);
}

tree::TerminalNode* SchrodingerMRParser::NumberContext::Integer() {
  return getToken(SchrodingerMRParser::Integer, 0);
}


size_t SchrodingerMRParser::NumberContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleNumber;
}


std::any SchrodingerMRParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::NumberContext* SchrodingerMRParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 62, SchrodingerMRParser::RuleNumber);
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
    setState(584);
    _la = _input->LA(1);
    if (!(_la == SchrodingerMRParser::Integer

    || _la == SchrodingerMRParser::Float)) {
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

SchrodingerMRParser::Number_fContext::Number_fContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Number_fContext::Float() {
  return getToken(SchrodingerMRParser::Float, 0);
}

tree::TerminalNode* SchrodingerMRParser::Number_fContext::Integer() {
  return getToken(SchrodingerMRParser::Integer, 0);
}


size_t SchrodingerMRParser::Number_fContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleNumber_f;
}


std::any SchrodingerMRParser::Number_fContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber_f(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Number_fContext* SchrodingerMRParser::number_f() {
  Number_fContext *_localctx = _tracker.createInstance<Number_fContext>(_ctx, getState());
  enterRule(_localctx, 64, SchrodingerMRParser::RuleNumber_f);
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
    setState(586);
    _la = _input->LA(1);
    if (!(_la == SchrodingerMRParser::Integer

    || _la == SchrodingerMRParser::Float)) {
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

//----------------- Parameter_statementContext ------------------------------------------------------------------

SchrodingerMRParser::Parameter_statementContext::Parameter_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SchrodingerMRParser::Parameter_statementContext::Set() {
  return getToken(SchrodingerMRParser::Set, 0);
}

tree::TerminalNode* SchrodingerMRParser::Parameter_statementContext::Simple_name() {
  return getToken(SchrodingerMRParser::Simple_name, 0);
}

SchrodingerMRParser::Selection_expressionContext* SchrodingerMRParser::Parameter_statementContext::selection_expression() {
  return getRuleContext<SchrodingerMRParser::Selection_expressionContext>(0);
}


size_t SchrodingerMRParser::Parameter_statementContext::getRuleIndex() const {
  return SchrodingerMRParser::RuleParameter_statement;
}


std::any SchrodingerMRParser::Parameter_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SchrodingerMRParserVisitor*>(visitor))
    return parserVisitor->visitParameter_statement(this);
  else
    return visitor->visitChildren(this);
}

SchrodingerMRParser::Parameter_statementContext* SchrodingerMRParser::parameter_statement() {
  Parameter_statementContext *_localctx = _tracker.createInstance<Parameter_statementContext>(_ctx, getState());
  enterRule(_localctx, 66, SchrodingerMRParser::RuleParameter_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(588);
    match(SchrodingerMRParser::Set);
    setState(589);
    match(SchrodingerMRParser::Simple_name);
    setState(590);
    selection_expression();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

void SchrodingerMRParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  schrodingermrparserParserInitialize();
#else
  ::antlr4::internal::call_once(schrodingermrparserParserOnceFlag, schrodingermrparserParserInitialize);
#endif
}
