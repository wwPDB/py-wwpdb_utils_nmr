
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AmberPTParser.g4 by ANTLR 4.13.2


#include "AmberPTParserVisitor.h"

#include "AmberPTParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct AmberPTParserStaticData final {
  AmberPTParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  AmberPTParserStaticData(const AmberPTParserStaticData&) = delete;
  AmberPTParserStaticData(AmberPTParserStaticData&&) = delete;
  AmberPTParserStaticData& operator=(const AmberPTParserStaticData&) = delete;
  AmberPTParserStaticData& operator=(AmberPTParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag amberptparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<AmberPTParserStaticData> amberptparserParserStaticData = nullptr;

void amberptparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (amberptparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(amberptparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<AmberPTParserStaticData>(
    std::vector<std::string>{
      "amber_pt", "version_statement", "amber_atom_type_statement", "angle_equil_value_statement", 
      "angle_force_constant_statement", "angles_inc_hydrogen_statement", 
      "angles_without_hydrogen_statement", "atomic_number_statement", "atom_name_statement", 
      "atom_type_index_statement", "atoms_per_molecule_statement", "bond_equil_value_statement", 
      "bond_force_constant_statement", "bonds_inc_hydrogen_statement", "bonds_without_hydrogen_statement", 
      "box_dimensions_statement", "cap_info_statement", "cap_info2_statement", 
      "charge_statement", "cmap_count_statement", "cmap_resolution_statement", 
      "cmap_parameter_statement", "cmap_index_statement", "dihedral_force_constant_statement", 
      "dihedral_periodicity_statement", "dihedral_phase_statement", "dihedrals_inc_hydrogen_statement", 
      "dihedrals_without_hydrogen_statement", "excluded_atoms_list_statement", 
      "hbcut_statement", "hbond_acoef_statement", "hbond_bcoef_statement", 
      "ipol_statement", "irotat_statement", "join_array_statement", "lennard_jones_acoef_statement", 
      "lennard_jones_bcoef_statement", "mass_statement", "nonbonded_parm_index_statement", 
      "number_excluded_atoms_statement", "pointers_statement", "polarizability_statement", 
      "radii_statement", "radius_set_statement", "residue_label_statement", 
      "residue_pointer_statement", "scee_scale_factor_statement", "scnb_scale_factor_statement", 
      "screen_statement", "solty_statement", "solvent_pointers_statement", 
      "title_statement", "tree_chain_classification_statement", "format_function"
    },
    std::vector<std::string>{
      "", "'%VERSION'", "", "'AMBER_ATOM_TYPE'", "'ANGLE_EQUIL_VALUE'", 
      "'ANGLE_FORCE_CONSTANT'", "'ANGLES_INC_HYDROGEN'", "'ANGLES_WITHOUT_HYDROGEN'", 
      "'ATOMIC_NUMBER'", "'ATOM_NAME'", "'ATOM_TYPE_INDEX'", "'ATOMS_PER_MOLECULE'", 
      "'BOND_EQUIL_VALUE'", "'BOND_FORCE_CONSTANT'", "'BONDS_INC_HYDROGEN'", 
      "'BONDS_WITHOUT_HYDROGEN'", "'BOX_DIMENSIONS'", "'CAP_INFO'", "'CAP_INFO2'", 
      "'CHARGE'", "'CMAP_COUNT'", "'CMAP_RESOLUTION'", "'CMAP_PARAMETER_01'", 
      "'CMAP_PARAMETER_02'", "'CMAP_PARAMETER_03'", "'CMAP_PARAMETER_04'", 
      "'CMAP_PARAMETER_05'", "'CMAP_PARAMETER_06'", "'CMAP_PARAMETER_07'", 
      "'CMAP_PARAMETER_08'", "'CMAP_PARAMETER_09'", "'CMAP_PARAMETER_10'", 
      "'CMAP_PARAMETER_11'", "'CMAP_PARAMETER_12'", "'CMAP_PARAMETER_13'", 
      "'CMAP_PARAMETER_14'", "'CMAP_INDEX'", "'DIHEDRAL_FORCE_CONSTANT'", 
      "'DIHEDRAL_PERIODICITY'", "'DIHEDRAL_PHASE'", "'DIHEDRALS_INC_HYDROGEN'", 
      "'DIHEDRALS_WITHOUT_HYDROGEN'", "'EXCLUDED_ATOMS_LIST'", "'HBCUT'", 
      "'HBOND_ACOEF'", "'HBOND_BCOEF'", "'IPOL'", "'IROTAT'", "'JOIN_ARRAY'", 
      "'LENNARD_JONES_ACOEF'", "'LENNARD_JONES_BCOEF'", "'MASS'", "'NONBONDED_PARM_INDEX'", 
      "'NUMBER_EXCLUDED_ATOMS'", "'POINTERS'", "'POLARIZABILITY'", "'RADII'", 
      "'RADIUS_SET'", "'RESIDUE_LABEL'", "'RESIDUE_POINTER'", "'SCEE_SCALE_FACTOR'", 
      "'SCNB_SCALE_FACTOR'", "'SCREEN'", "'SOLTY'", "'SOLVENT_POINTERS'", 
      "'TITLE'", "'TREE_CHAIN_CLASSIFICATION'", "", "", "", "'%FORMAT'", 
      "", "", "'VERSION_STAMP'", "'DATE'", "'='"
    },
    std::vector<std::string>{
      "", "VERSION", "FLAG", "AMBER_ATOM_TYPE", "ANGLE_EQUIL_VALUE", "ANGLE_FORCE_CONSTANT", 
      "ANGLES_INC_HYDROGEN", "ANGLES_WITHOUT_HYDROGEN", "ATOMIC_NUMBER", 
      "ATOM_NAME", "ATOM_TYPE_INDEX", "ATOMS_PER_MOLECULE", "BOND_EQUIL_VALUE", 
      "BOND_FORCE_CONSTANT", "BONDS_INC_HYDROGEN", "BONDS_WITHOUT_HYDROGEN", 
      "BOX_DIMENSIONS", "CAP_INFO", "CAP_INFO2", "CHARGE", "CMAP_COUNT", 
      "CMAP_RESOLUTION", "CMAP_PARAMETER_01", "CMAP_PARAMETER_02", "CMAP_PARAMETER_03", 
      "CMAP_PARAMETER_04", "CMAP_PARAMETER_05", "CMAP_PARAMETER_06", "CMAP_PARAMETER_07", 
      "CMAP_PARAMETER_08", "CMAP_PARAMETER_09", "CMAP_PARAMETER_10", "CMAP_PARAMETER_11", 
      "CMAP_PARAMETER_12", "CMAP_PARAMETER_13", "CMAP_PARAMETER_14", "CMAP_INDEX", 
      "DIHEDRAL_FORCE_CONSTANT", "DIHEDRAL_PERIODICITY", "DIHEDRAL_PHASE", 
      "DIHEDRALS_INC_HYDROGEN", "DIHEDRALS_WITHOUT_HYDROGEN", "EXCLUDED_ATOMS_LIST", 
      "HBCUT", "HBOND_ACOEF", "HBOND_BCOEF", "IPOL", "IROTAT", "JOIN_ARRAY", 
      "LENNARD_JONES_ACOEF", "LENNARD_JONES_BCOEF", "MASS", "NONBONDED_PARM_INDEX", 
      "NUMBER_EXCLUDED_ATOMS", "POINTERS", "POLARIZABILITY", "RADII", "RADIUS_SET", 
      "RESIDUE_LABEL", "RESIDUE_POINTER", "SCEE_SCALE_FACTOR", "SCNB_SCALE_FACTOR", 
      "SCREEN", "SOLTY", "SOLVENT_POINTERS", "TITLE", "TREE_CHAIN_CLASSIFICATION", 
      "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", "FORMAT", "SPACE", 
      "LINE_COMMENT", "VERSION_STAMP", "DATE", "Equ_op", "Version", "Date_time", 
      "SPACE_VS", "FLAG_VS", "Fortran_format_A", "Fortran_format_I", "Fortran_format_E", 
      "Simple_name", "SPACE_AA", "FLAG_AA", "Integer", "SPACE_IA", "FLAG_IA", 
      "Real", "SPACE_EA", "FLAG_EA"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,91,695,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,
  	35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,
  	42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,
  	49,2,50,7,50,2,51,7,51,2,52,7,52,2,53,7,53,1,0,1,0,3,0,111,8,0,1,0,1,
  	0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
  	1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
  	0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,164,8,0,
  	10,0,12,0,167,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,179,8,1,
  	1,1,1,1,1,2,1,2,1,2,5,2,186,8,2,10,2,12,2,189,9,2,1,2,1,2,1,3,1,3,1,3,
  	5,3,196,8,3,10,3,12,3,199,9,3,1,3,1,3,1,4,1,4,1,4,5,4,206,8,4,10,4,12,
  	4,209,9,4,1,4,1,4,1,5,1,5,1,5,5,5,216,8,5,10,5,12,5,219,9,5,1,5,1,5,1,
  	6,1,6,1,6,5,6,226,8,6,10,6,12,6,229,9,6,1,6,1,6,1,7,1,7,1,7,5,7,236,8,
  	7,10,7,12,7,239,9,7,1,7,1,7,1,8,1,8,1,8,5,8,246,8,8,10,8,12,8,249,9,8,
  	1,8,1,8,1,9,1,9,1,9,5,9,256,8,9,10,9,12,9,259,9,9,1,9,1,9,1,10,1,10,1,
  	10,5,10,266,8,10,10,10,12,10,269,9,10,1,10,1,10,1,11,1,11,1,11,5,11,276,
  	8,11,10,11,12,11,279,9,11,1,11,1,11,1,12,1,12,1,12,5,12,286,8,12,10,12,
  	12,12,289,9,12,1,12,1,12,1,13,1,13,1,13,5,13,296,8,13,10,13,12,13,299,
  	9,13,1,13,1,13,1,14,1,14,1,14,5,14,306,8,14,10,14,12,14,309,9,14,1,14,
  	1,14,1,15,1,15,1,15,5,15,316,8,15,10,15,12,15,319,9,15,1,15,1,15,1,16,
  	1,16,1,16,5,16,326,8,16,10,16,12,16,329,9,16,1,16,1,16,1,17,1,17,1,17,
  	5,17,336,8,17,10,17,12,17,339,9,17,1,17,1,17,1,18,1,18,1,18,5,18,346,
  	8,18,10,18,12,18,349,9,18,1,18,1,18,1,19,1,19,1,19,5,19,356,8,19,10,19,
  	12,19,359,9,19,1,19,1,19,1,20,1,20,1,20,5,20,366,8,20,10,20,12,20,369,
  	9,20,1,20,1,20,1,21,1,21,1,21,5,21,376,8,21,10,21,12,21,379,9,21,1,21,
  	1,21,1,22,1,22,1,22,5,22,386,8,22,10,22,12,22,389,9,22,1,22,1,22,1,23,
  	1,23,1,23,5,23,396,8,23,10,23,12,23,399,9,23,1,23,1,23,1,24,1,24,1,24,
  	5,24,406,8,24,10,24,12,24,409,9,24,1,24,1,24,1,25,1,25,1,25,5,25,416,
  	8,25,10,25,12,25,419,9,25,1,25,1,25,1,26,1,26,1,26,5,26,426,8,26,10,26,
  	12,26,429,9,26,1,26,1,26,1,27,1,27,1,27,5,27,436,8,27,10,27,12,27,439,
  	9,27,1,27,1,27,1,28,1,28,1,28,5,28,446,8,28,10,28,12,28,449,9,28,1,28,
  	1,28,1,29,1,29,1,29,5,29,456,8,29,10,29,12,29,459,9,29,1,29,1,29,1,30,
  	1,30,1,30,5,30,466,8,30,10,30,12,30,469,9,30,1,30,1,30,1,31,1,31,1,31,
  	5,31,476,8,31,10,31,12,31,479,9,31,1,31,1,31,1,32,1,32,1,32,5,32,486,
  	8,32,10,32,12,32,489,9,32,1,32,1,32,1,33,1,33,1,33,5,33,496,8,33,10,33,
  	12,33,499,9,33,1,33,1,33,1,34,1,34,1,34,5,34,506,8,34,10,34,12,34,509,
  	9,34,1,34,1,34,1,35,1,35,1,35,5,35,516,8,35,10,35,12,35,519,9,35,1,35,
  	1,35,1,36,1,36,1,36,5,36,526,8,36,10,36,12,36,529,9,36,1,36,1,36,1,37,
  	1,37,1,37,5,37,536,8,37,10,37,12,37,539,9,37,1,37,1,37,1,38,1,38,1,38,
  	5,38,546,8,38,10,38,12,38,549,9,38,1,38,1,38,1,39,1,39,1,39,5,39,556,
  	8,39,10,39,12,39,559,9,39,1,39,1,39,1,40,1,40,1,40,5,40,566,8,40,10,40,
  	12,40,569,9,40,1,40,1,40,1,41,1,41,1,41,5,41,576,8,41,10,41,12,41,579,
  	9,41,1,41,1,41,1,42,1,42,1,42,5,42,586,8,42,10,42,12,42,589,9,42,1,42,
  	1,42,1,43,1,43,1,43,5,43,596,8,43,10,43,12,43,599,9,43,1,43,1,43,1,44,
  	1,44,1,44,5,44,606,8,44,10,44,12,44,609,9,44,1,44,1,44,1,45,1,45,1,45,
  	4,45,616,8,45,11,45,12,45,617,1,45,1,45,1,46,1,46,1,46,5,46,625,8,46,
  	10,46,12,46,628,9,46,1,46,1,46,1,47,1,47,1,47,5,47,635,8,47,10,47,12,
  	47,638,9,47,1,47,1,47,1,48,1,48,1,48,5,48,645,8,48,10,48,12,48,648,9,
  	48,1,48,1,48,1,49,1,49,1,49,5,49,655,8,49,10,49,12,49,658,9,49,1,49,1,
  	49,1,50,1,50,1,50,5,50,665,8,50,10,50,12,50,668,9,50,1,50,1,50,1,51,1,
  	51,1,51,5,51,675,8,51,10,51,12,51,678,9,51,1,51,1,51,1,52,1,52,1,52,5,
  	52,685,8,52,10,52,12,52,688,9,52,1,52,1,52,1,53,1,53,1,53,1,53,0,0,54,
  	0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
  	50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,
  	96,98,100,102,104,106,0,6,1,1,79,79,1,1,85,85,1,1,91,91,1,1,88,88,1,0,
  	22,35,1,0,80,82,744,0,110,1,0,0,0,2,170,1,0,0,0,4,182,1,0,0,0,6,192,1,
  	0,0,0,8,202,1,0,0,0,10,212,1,0,0,0,12,222,1,0,0,0,14,232,1,0,0,0,16,242,
  	1,0,0,0,18,252,1,0,0,0,20,262,1,0,0,0,22,272,1,0,0,0,24,282,1,0,0,0,26,
  	292,1,0,0,0,28,302,1,0,0,0,30,312,1,0,0,0,32,322,1,0,0,0,34,332,1,0,0,
  	0,36,342,1,0,0,0,38,352,1,0,0,0,40,362,1,0,0,0,42,372,1,0,0,0,44,382,
  	1,0,0,0,46,392,1,0,0,0,48,402,1,0,0,0,50,412,1,0,0,0,52,422,1,0,0,0,54,
  	432,1,0,0,0,56,442,1,0,0,0,58,452,1,0,0,0,60,462,1,0,0,0,62,472,1,0,0,
  	0,64,482,1,0,0,0,66,492,1,0,0,0,68,502,1,0,0,0,70,512,1,0,0,0,72,522,
  	1,0,0,0,74,532,1,0,0,0,76,542,1,0,0,0,78,552,1,0,0,0,80,562,1,0,0,0,82,
  	572,1,0,0,0,84,582,1,0,0,0,86,592,1,0,0,0,88,602,1,0,0,0,90,612,1,0,0,
  	0,92,621,1,0,0,0,94,631,1,0,0,0,96,641,1,0,0,0,98,651,1,0,0,0,100,661,
  	1,0,0,0,102,671,1,0,0,0,104,681,1,0,0,0,106,691,1,0,0,0,108,111,3,2,1,
  	0,109,111,5,2,0,0,110,108,1,0,0,0,110,109,1,0,0,0,111,165,1,0,0,0,112,
  	164,3,4,2,0,113,164,3,6,3,0,114,164,3,8,4,0,115,164,3,10,5,0,116,164,
  	3,12,6,0,117,164,3,14,7,0,118,164,3,16,8,0,119,164,3,18,9,0,120,164,3,
  	20,10,0,121,164,3,22,11,0,122,164,3,24,12,0,123,164,3,26,13,0,124,164,
  	3,28,14,0,125,164,3,30,15,0,126,164,3,32,16,0,127,164,3,34,17,0,128,164,
  	3,36,18,0,129,164,3,38,19,0,130,164,3,40,20,0,131,164,3,42,21,0,132,164,
  	3,44,22,0,133,164,3,46,23,0,134,164,3,48,24,0,135,164,3,50,25,0,136,164,
  	3,52,26,0,137,164,3,54,27,0,138,164,3,56,28,0,139,164,3,58,29,0,140,164,
  	3,60,30,0,141,164,3,62,31,0,142,164,3,64,32,0,143,164,3,66,33,0,144,164,
  	3,68,34,0,145,164,3,70,35,0,146,164,3,72,36,0,147,164,3,74,37,0,148,164,
  	3,76,38,0,149,164,3,78,39,0,150,164,3,80,40,0,151,164,3,82,41,0,152,164,
  	3,84,42,0,153,164,3,86,43,0,154,164,3,88,44,0,155,164,3,90,45,0,156,164,
  	3,92,46,0,157,164,3,94,47,0,158,164,3,96,48,0,159,164,3,98,49,0,160,164,
  	3,100,50,0,161,164,3,102,51,0,162,164,3,104,52,0,163,112,1,0,0,0,163,
  	113,1,0,0,0,163,114,1,0,0,0,163,115,1,0,0,0,163,116,1,0,0,0,163,117,1,
  	0,0,0,163,118,1,0,0,0,163,119,1,0,0,0,163,120,1,0,0,0,163,121,1,0,0,0,
  	163,122,1,0,0,0,163,123,1,0,0,0,163,124,1,0,0,0,163,125,1,0,0,0,163,126,
  	1,0,0,0,163,127,1,0,0,0,163,128,1,0,0,0,163,129,1,0,0,0,163,130,1,0,0,
  	0,163,131,1,0,0,0,163,132,1,0,0,0,163,133,1,0,0,0,163,134,1,0,0,0,163,
  	135,1,0,0,0,163,136,1,0,0,0,163,137,1,0,0,0,163,138,1,0,0,0,163,139,1,
  	0,0,0,163,140,1,0,0,0,163,141,1,0,0,0,163,142,1,0,0,0,163,143,1,0,0,0,
  	163,144,1,0,0,0,163,145,1,0,0,0,163,146,1,0,0,0,163,147,1,0,0,0,163,148,
  	1,0,0,0,163,149,1,0,0,0,163,150,1,0,0,0,163,151,1,0,0,0,163,152,1,0,0,
  	0,163,153,1,0,0,0,163,154,1,0,0,0,163,155,1,0,0,0,163,156,1,0,0,0,163,
  	157,1,0,0,0,163,158,1,0,0,0,163,159,1,0,0,0,163,160,1,0,0,0,163,161,1,
  	0,0,0,163,162,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,
  	166,168,1,0,0,0,167,165,1,0,0,0,168,169,5,0,0,1,169,1,1,0,0,0,170,171,
  	5,1,0,0,171,172,5,73,0,0,172,173,5,75,0,0,173,174,5,76,0,0,174,175,5,
  	74,0,0,175,176,5,75,0,0,176,178,5,77,0,0,177,179,5,77,0,0,178,177,1,0,
  	0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,181,7,0,0,0,181,3,1,0,0,0,182,
  	183,5,3,0,0,183,187,3,106,53,0,184,186,5,83,0,0,185,184,1,0,0,0,186,189,
  	1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,187,1,0,0,
  	0,190,191,7,1,0,0,191,5,1,0,0,0,192,193,5,4,0,0,193,197,3,106,53,0,194,
  	196,5,89,0,0,195,194,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,
  	1,0,0,0,198,200,1,0,0,0,199,197,1,0,0,0,200,201,7,2,0,0,201,7,1,0,0,0,
  	202,203,5,5,0,0,203,207,3,106,53,0,204,206,5,89,0,0,205,204,1,0,0,0,206,
  	209,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,210,1,0,0,0,209,207,1,
  	0,0,0,210,211,7,2,0,0,211,9,1,0,0,0,212,213,5,6,0,0,213,217,3,106,53,
  	0,214,216,5,86,0,0,215,214,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,
  	218,1,0,0,0,218,220,1,0,0,0,219,217,1,0,0,0,220,221,7,3,0,0,221,11,1,
  	0,0,0,222,223,5,7,0,0,223,227,3,106,53,0,224,226,5,86,0,0,225,224,1,0,
  	0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,230,1,0,0,0,229,
  	227,1,0,0,0,230,231,7,3,0,0,231,13,1,0,0,0,232,233,5,8,0,0,233,237,3,
  	106,53,0,234,236,5,86,0,0,235,234,1,0,0,0,236,239,1,0,0,0,237,235,1,0,
  	0,0,237,238,1,0,0,0,238,240,1,0,0,0,239,237,1,0,0,0,240,241,7,3,0,0,241,
  	15,1,0,0,0,242,243,5,9,0,0,243,247,3,106,53,0,244,246,5,83,0,0,245,244,
  	1,0,0,0,246,249,1,0,0,0,247,245,1,0,0,0,247,248,1,0,0,0,248,250,1,0,0,
  	0,249,247,1,0,0,0,250,251,7,1,0,0,251,17,1,0,0,0,252,253,5,10,0,0,253,
  	257,3,106,53,0,254,256,5,86,0,0,255,254,1,0,0,0,256,259,1,0,0,0,257,255,
  	1,0,0,0,257,258,1,0,0,0,258,260,1,0,0,0,259,257,1,0,0,0,260,261,7,3,0,
  	0,261,19,1,0,0,0,262,263,5,11,0,0,263,267,3,106,53,0,264,266,5,86,0,0,
  	265,264,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,270,
  	1,0,0,0,269,267,1,0,0,0,270,271,7,3,0,0,271,21,1,0,0,0,272,273,5,12,0,
  	0,273,277,3,106,53,0,274,276,5,89,0,0,275,274,1,0,0,0,276,279,1,0,0,0,
  	277,275,1,0,0,0,277,278,1,0,0,0,278,280,1,0,0,0,279,277,1,0,0,0,280,281,
  	7,2,0,0,281,23,1,0,0,0,282,283,5,13,0,0,283,287,3,106,53,0,284,286,5,
  	89,0,0,285,284,1,0,0,0,286,289,1,0,0,0,287,285,1,0,0,0,287,288,1,0,0,
  	0,288,290,1,0,0,0,289,287,1,0,0,0,290,291,7,2,0,0,291,25,1,0,0,0,292,
  	293,5,14,0,0,293,297,3,106,53,0,294,296,5,86,0,0,295,294,1,0,0,0,296,
  	299,1,0,0,0,297,295,1,0,0,0,297,298,1,0,0,0,298,300,1,0,0,0,299,297,1,
  	0,0,0,300,301,7,3,0,0,301,27,1,0,0,0,302,303,5,15,0,0,303,307,3,106,53,
  	0,304,306,5,86,0,0,305,304,1,0,0,0,306,309,1,0,0,0,307,305,1,0,0,0,307,
  	308,1,0,0,0,308,310,1,0,0,0,309,307,1,0,0,0,310,311,7,3,0,0,311,29,1,
  	0,0,0,312,313,5,16,0,0,313,317,3,106,53,0,314,316,5,89,0,0,315,314,1,
  	0,0,0,316,319,1,0,0,0,317,315,1,0,0,0,317,318,1,0,0,0,318,320,1,0,0,0,
  	319,317,1,0,0,0,320,321,7,2,0,0,321,31,1,0,0,0,322,323,5,17,0,0,323,327,
  	3,106,53,0,324,326,5,86,0,0,325,324,1,0,0,0,326,329,1,0,0,0,327,325,1,
  	0,0,0,327,328,1,0,0,0,328,330,1,0,0,0,329,327,1,0,0,0,330,331,7,3,0,0,
  	331,33,1,0,0,0,332,333,5,18,0,0,333,337,3,106,53,0,334,336,5,89,0,0,335,
  	334,1,0,0,0,336,339,1,0,0,0,337,335,1,0,0,0,337,338,1,0,0,0,338,340,1,
  	0,0,0,339,337,1,0,0,0,340,341,7,2,0,0,341,35,1,0,0,0,342,343,5,19,0,0,
  	343,347,3,106,53,0,344,346,5,89,0,0,345,344,1,0,0,0,346,349,1,0,0,0,347,
  	345,1,0,0,0,347,348,1,0,0,0,348,350,1,0,0,0,349,347,1,0,0,0,350,351,7,
  	2,0,0,351,37,1,0,0,0,352,353,5,20,0,0,353,357,3,106,53,0,354,356,5,86,
  	0,0,355,354,1,0,0,0,356,359,1,0,0,0,357,355,1,0,0,0,357,358,1,0,0,0,358,
  	360,1,0,0,0,359,357,1,0,0,0,360,361,7,3,0,0,361,39,1,0,0,0,362,363,5,
  	21,0,0,363,367,3,106,53,0,364,366,5,86,0,0,365,364,1,0,0,0,366,369,1,
  	0,0,0,367,365,1,0,0,0,367,368,1,0,0,0,368,370,1,0,0,0,369,367,1,0,0,0,
  	370,371,7,3,0,0,371,41,1,0,0,0,372,373,7,4,0,0,373,377,3,106,53,0,374,
  	376,5,89,0,0,375,374,1,0,0,0,376,379,1,0,0,0,377,375,1,0,0,0,377,378,
  	1,0,0,0,378,380,1,0,0,0,379,377,1,0,0,0,380,381,7,2,0,0,381,43,1,0,0,
  	0,382,383,5,36,0,0,383,387,3,106,53,0,384,386,5,86,0,0,385,384,1,0,0,
  	0,386,389,1,0,0,0,387,385,1,0,0,0,387,388,1,0,0,0,388,390,1,0,0,0,389,
  	387,1,0,0,0,390,391,7,3,0,0,391,45,1,0,0,0,392,393,5,37,0,0,393,397,3,
  	106,53,0,394,396,5,89,0,0,395,394,1,0,0,0,396,399,1,0,0,0,397,395,1,0,
  	0,0,397,398,1,0,0,0,398,400,1,0,0,0,399,397,1,0,0,0,400,401,7,2,0,0,401,
  	47,1,0,0,0,402,403,5,38,0,0,403,407,3,106,53,0,404,406,5,89,0,0,405,404,
  	1,0,0,0,406,409,1,0,0,0,407,405,1,0,0,0,407,408,1,0,0,0,408,410,1,0,0,
  	0,409,407,1,0,0,0,410,411,7,2,0,0,411,49,1,0,0,0,412,413,5,39,0,0,413,
  	417,3,106,53,0,414,416,5,89,0,0,415,414,1,0,0,0,416,419,1,0,0,0,417,415,
  	1,0,0,0,417,418,1,0,0,0,418,420,1,0,0,0,419,417,1,0,0,0,420,421,7,2,0,
  	0,421,51,1,0,0,0,422,423,5,40,0,0,423,427,3,106,53,0,424,426,5,86,0,0,
  	425,424,1,0,0,0,426,429,1,0,0,0,427,425,1,0,0,0,427,428,1,0,0,0,428,430,
  	1,0,0,0,429,427,1,0,0,0,430,431,7,3,0,0,431,53,1,0,0,0,432,433,5,41,0,
  	0,433,437,3,106,53,0,434,436,5,86,0,0,435,434,1,0,0,0,436,439,1,0,0,0,
  	437,435,1,0,0,0,437,438,1,0,0,0,438,440,1,0,0,0,439,437,1,0,0,0,440,441,
  	7,3,0,0,441,55,1,0,0,0,442,443,5,42,0,0,443,447,3,106,53,0,444,446,5,
  	86,0,0,445,444,1,0,0,0,446,449,1,0,0,0,447,445,1,0,0,0,447,448,1,0,0,
  	0,448,450,1,0,0,0,449,447,1,0,0,0,450,451,7,3,0,0,451,57,1,0,0,0,452,
  	453,5,43,0,0,453,457,3,106,53,0,454,456,5,89,0,0,455,454,1,0,0,0,456,
  	459,1,0,0,0,457,455,1,0,0,0,457,458,1,0,0,0,458,460,1,0,0,0,459,457,1,
  	0,0,0,460,461,7,2,0,0,461,59,1,0,0,0,462,463,5,44,0,0,463,467,3,106,53,
  	0,464,466,5,89,0,0,465,464,1,0,0,0,466,469,1,0,0,0,467,465,1,0,0,0,467,
  	468,1,0,0,0,468,470,1,0,0,0,469,467,1,0,0,0,470,471,7,2,0,0,471,61,1,
  	0,0,0,472,473,5,45,0,0,473,477,3,106,53,0,474,476,5,89,0,0,475,474,1,
  	0,0,0,476,479,1,0,0,0,477,475,1,0,0,0,477,478,1,0,0,0,478,480,1,0,0,0,
  	479,477,1,0,0,0,480,481,7,2,0,0,481,63,1,0,0,0,482,483,5,46,0,0,483,487,
  	3,106,53,0,484,486,5,86,0,0,485,484,1,0,0,0,486,489,1,0,0,0,487,485,1,
  	0,0,0,487,488,1,0,0,0,488,490,1,0,0,0,489,487,1,0,0,0,490,491,7,3,0,0,
  	491,65,1,0,0,0,492,493,5,47,0,0,493,497,3,106,53,0,494,496,5,86,0,0,495,
  	494,1,0,0,0,496,499,1,0,0,0,497,495,1,0,0,0,497,498,1,0,0,0,498,500,1,
  	0,0,0,499,497,1,0,0,0,500,501,7,3,0,0,501,67,1,0,0,0,502,503,5,48,0,0,
  	503,507,3,106,53,0,504,506,5,86,0,0,505,504,1,0,0,0,506,509,1,0,0,0,507,
  	505,1,0,0,0,507,508,1,0,0,0,508,510,1,0,0,0,509,507,1,0,0,0,510,511,7,
  	3,0,0,511,69,1,0,0,0,512,513,5,49,0,0,513,517,3,106,53,0,514,516,5,89,
  	0,0,515,514,1,0,0,0,516,519,1,0,0,0,517,515,1,0,0,0,517,518,1,0,0,0,518,
  	520,1,0,0,0,519,517,1,0,0,0,520,521,7,2,0,0,521,71,1,0,0,0,522,523,5,
  	50,0,0,523,527,3,106,53,0,524,526,5,89,0,0,525,524,1,0,0,0,526,529,1,
  	0,0,0,527,525,1,0,0,0,527,528,1,0,0,0,528,530,1,0,0,0,529,527,1,0,0,0,
  	530,531,7,2,0,0,531,73,1,0,0,0,532,533,5,51,0,0,533,537,3,106,53,0,534,
  	536,5,89,0,0,535,534,1,0,0,0,536,539,1,0,0,0,537,535,1,0,0,0,537,538,
  	1,0,0,0,538,540,1,0,0,0,539,537,1,0,0,0,540,541,7,2,0,0,541,75,1,0,0,
  	0,542,543,5,52,0,0,543,547,3,106,53,0,544,546,5,86,0,0,545,544,1,0,0,
  	0,546,549,1,0,0,0,547,545,1,0,0,0,547,548,1,0,0,0,548,550,1,0,0,0,549,
  	547,1,0,0,0,550,551,7,3,0,0,551,77,1,0,0,0,552,553,5,53,0,0,553,557,3,
  	106,53,0,554,556,5,86,0,0,555,554,1,0,0,0,556,559,1,0,0,0,557,555,1,0,
  	0,0,557,558,1,0,0,0,558,560,1,0,0,0,559,557,1,0,0,0,560,561,7,3,0,0,561,
  	79,1,0,0,0,562,563,5,54,0,0,563,567,3,106,53,0,564,566,5,86,0,0,565,564,
  	1,0,0,0,566,569,1,0,0,0,567,565,1,0,0,0,567,568,1,0,0,0,568,570,1,0,0,
  	0,569,567,1,0,0,0,570,571,7,3,0,0,571,81,1,0,0,0,572,573,5,55,0,0,573,
  	577,3,106,53,0,574,576,5,89,0,0,575,574,1,0,0,0,576,579,1,0,0,0,577,575,
  	1,0,0,0,577,578,1,0,0,0,578,580,1,0,0,0,579,577,1,0,0,0,580,581,7,2,0,
  	0,581,83,1,0,0,0,582,583,5,56,0,0,583,587,3,106,53,0,584,586,5,89,0,0,
  	585,584,1,0,0,0,586,589,1,0,0,0,587,585,1,0,0,0,587,588,1,0,0,0,588,590,
  	1,0,0,0,589,587,1,0,0,0,590,591,7,2,0,0,591,85,1,0,0,0,592,593,5,57,0,
  	0,593,597,3,106,53,0,594,596,5,83,0,0,595,594,1,0,0,0,596,599,1,0,0,0,
  	597,595,1,0,0,0,597,598,1,0,0,0,598,600,1,0,0,0,599,597,1,0,0,0,600,601,
  	7,1,0,0,601,87,1,0,0,0,602,603,5,58,0,0,603,607,3,106,53,0,604,606,5,
  	83,0,0,605,604,1,0,0,0,606,609,1,0,0,0,607,605,1,0,0,0,607,608,1,0,0,
  	0,608,610,1,0,0,0,609,607,1,0,0,0,610,611,7,1,0,0,611,89,1,0,0,0,612,
  	613,5,59,0,0,613,615,3,106,53,0,614,616,5,86,0,0,615,614,1,0,0,0,616,
  	617,1,0,0,0,617,615,1,0,0,0,617,618,1,0,0,0,618,619,1,0,0,0,619,620,7,
  	3,0,0,620,91,1,0,0,0,621,622,5,60,0,0,622,626,3,106,53,0,623,625,5,89,
  	0,0,624,623,1,0,0,0,625,628,1,0,0,0,626,624,1,0,0,0,626,627,1,0,0,0,627,
  	629,1,0,0,0,628,626,1,0,0,0,629,630,7,2,0,0,630,93,1,0,0,0,631,632,5,
  	61,0,0,632,636,3,106,53,0,633,635,5,89,0,0,634,633,1,0,0,0,635,638,1,
  	0,0,0,636,634,1,0,0,0,636,637,1,0,0,0,637,639,1,0,0,0,638,636,1,0,0,0,
  	639,640,7,2,0,0,640,95,1,0,0,0,641,642,5,62,0,0,642,646,3,106,53,0,643,
  	645,5,89,0,0,644,643,1,0,0,0,645,648,1,0,0,0,646,644,1,0,0,0,646,647,
  	1,0,0,0,647,649,1,0,0,0,648,646,1,0,0,0,649,650,7,2,0,0,650,97,1,0,0,
  	0,651,652,5,63,0,0,652,656,3,106,53,0,653,655,5,89,0,0,654,653,1,0,0,
  	0,655,658,1,0,0,0,656,654,1,0,0,0,656,657,1,0,0,0,657,659,1,0,0,0,658,
  	656,1,0,0,0,659,660,7,2,0,0,660,99,1,0,0,0,661,662,5,64,0,0,662,666,3,
  	106,53,0,663,665,5,86,0,0,664,663,1,0,0,0,665,668,1,0,0,0,666,664,1,0,
  	0,0,666,667,1,0,0,0,667,669,1,0,0,0,668,666,1,0,0,0,669,670,7,3,0,0,670,
  	101,1,0,0,0,671,672,5,65,0,0,672,676,3,106,53,0,673,675,5,83,0,0,674,
  	673,1,0,0,0,675,678,1,0,0,0,676,674,1,0,0,0,676,677,1,0,0,0,677,679,1,
  	0,0,0,678,676,1,0,0,0,679,680,7,1,0,0,680,103,1,0,0,0,681,682,5,66,0,
  	0,682,686,3,106,53,0,683,685,5,83,0,0,684,683,1,0,0,0,685,688,1,0,0,0,
  	686,684,1,0,0,0,686,687,1,0,0,0,687,689,1,0,0,0,688,686,1,0,0,0,689,690,
  	7,1,0,0,690,105,1,0,0,0,691,692,5,70,0,0,692,693,7,5,0,0,693,107,1,0,
  	0,0,55,110,163,165,178,187,197,207,217,227,237,247,257,267,277,287,297,
  	307,317,327,337,347,357,367,377,387,397,407,417,427,437,447,457,467,477,
  	487,497,507,517,527,537,547,557,567,577,587,597,607,617,626,636,646,656,
  	666,676,686
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  amberptparserParserStaticData = std::move(staticData);
}

}

AmberPTParser::AmberPTParser(TokenStream *input) : AmberPTParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

AmberPTParser::AmberPTParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  AmberPTParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *amberptparserParserStaticData->atn, amberptparserParserStaticData->decisionToDFA, amberptparserParserStaticData->sharedContextCache, options);
}

AmberPTParser::~AmberPTParser() {
  delete _interpreter;
}

const atn::ATN& AmberPTParser::getATN() const {
  return *amberptparserParserStaticData->atn;
}

std::string AmberPTParser::getGrammarFileName() const {
  return "AmberPTParser.g4";
}

const std::vector<std::string>& AmberPTParser::getRuleNames() const {
  return amberptparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& AmberPTParser::getVocabulary() const {
  return amberptparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView AmberPTParser::getSerializedATN() const {
  return amberptparserParserStaticData->serializedATN;
}


//----------------- Amber_ptContext ------------------------------------------------------------------

AmberPTParser::Amber_ptContext::Amber_ptContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Amber_ptContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

AmberPTParser::Version_statementContext* AmberPTParser::Amber_ptContext::version_statement() {
  return getRuleContext<AmberPTParser::Version_statementContext>(0);
}

tree::TerminalNode* AmberPTParser::Amber_ptContext::FLAG() {
  return getToken(AmberPTParser::FLAG, 0);
}

std::vector<AmberPTParser::Amber_atom_type_statementContext *> AmberPTParser::Amber_ptContext::amber_atom_type_statement() {
  return getRuleContexts<AmberPTParser::Amber_atom_type_statementContext>();
}

AmberPTParser::Amber_atom_type_statementContext* AmberPTParser::Amber_ptContext::amber_atom_type_statement(size_t i) {
  return getRuleContext<AmberPTParser::Amber_atom_type_statementContext>(i);
}

std::vector<AmberPTParser::Angle_equil_value_statementContext *> AmberPTParser::Amber_ptContext::angle_equil_value_statement() {
  return getRuleContexts<AmberPTParser::Angle_equil_value_statementContext>();
}

AmberPTParser::Angle_equil_value_statementContext* AmberPTParser::Amber_ptContext::angle_equil_value_statement(size_t i) {
  return getRuleContext<AmberPTParser::Angle_equil_value_statementContext>(i);
}

std::vector<AmberPTParser::Angle_force_constant_statementContext *> AmberPTParser::Amber_ptContext::angle_force_constant_statement() {
  return getRuleContexts<AmberPTParser::Angle_force_constant_statementContext>();
}

AmberPTParser::Angle_force_constant_statementContext* AmberPTParser::Amber_ptContext::angle_force_constant_statement(size_t i) {
  return getRuleContext<AmberPTParser::Angle_force_constant_statementContext>(i);
}

std::vector<AmberPTParser::Angles_inc_hydrogen_statementContext *> AmberPTParser::Amber_ptContext::angles_inc_hydrogen_statement() {
  return getRuleContexts<AmberPTParser::Angles_inc_hydrogen_statementContext>();
}

AmberPTParser::Angles_inc_hydrogen_statementContext* AmberPTParser::Amber_ptContext::angles_inc_hydrogen_statement(size_t i) {
  return getRuleContext<AmberPTParser::Angles_inc_hydrogen_statementContext>(i);
}

std::vector<AmberPTParser::Angles_without_hydrogen_statementContext *> AmberPTParser::Amber_ptContext::angles_without_hydrogen_statement() {
  return getRuleContexts<AmberPTParser::Angles_without_hydrogen_statementContext>();
}

AmberPTParser::Angles_without_hydrogen_statementContext* AmberPTParser::Amber_ptContext::angles_without_hydrogen_statement(size_t i) {
  return getRuleContext<AmberPTParser::Angles_without_hydrogen_statementContext>(i);
}

std::vector<AmberPTParser::Atomic_number_statementContext *> AmberPTParser::Amber_ptContext::atomic_number_statement() {
  return getRuleContexts<AmberPTParser::Atomic_number_statementContext>();
}

AmberPTParser::Atomic_number_statementContext* AmberPTParser::Amber_ptContext::atomic_number_statement(size_t i) {
  return getRuleContext<AmberPTParser::Atomic_number_statementContext>(i);
}

std::vector<AmberPTParser::Atom_name_statementContext *> AmberPTParser::Amber_ptContext::atom_name_statement() {
  return getRuleContexts<AmberPTParser::Atom_name_statementContext>();
}

AmberPTParser::Atom_name_statementContext* AmberPTParser::Amber_ptContext::atom_name_statement(size_t i) {
  return getRuleContext<AmberPTParser::Atom_name_statementContext>(i);
}

std::vector<AmberPTParser::Atom_type_index_statementContext *> AmberPTParser::Amber_ptContext::atom_type_index_statement() {
  return getRuleContexts<AmberPTParser::Atom_type_index_statementContext>();
}

AmberPTParser::Atom_type_index_statementContext* AmberPTParser::Amber_ptContext::atom_type_index_statement(size_t i) {
  return getRuleContext<AmberPTParser::Atom_type_index_statementContext>(i);
}

std::vector<AmberPTParser::Atoms_per_molecule_statementContext *> AmberPTParser::Amber_ptContext::atoms_per_molecule_statement() {
  return getRuleContexts<AmberPTParser::Atoms_per_molecule_statementContext>();
}

AmberPTParser::Atoms_per_molecule_statementContext* AmberPTParser::Amber_ptContext::atoms_per_molecule_statement(size_t i) {
  return getRuleContext<AmberPTParser::Atoms_per_molecule_statementContext>(i);
}

std::vector<AmberPTParser::Bond_equil_value_statementContext *> AmberPTParser::Amber_ptContext::bond_equil_value_statement() {
  return getRuleContexts<AmberPTParser::Bond_equil_value_statementContext>();
}

AmberPTParser::Bond_equil_value_statementContext* AmberPTParser::Amber_ptContext::bond_equil_value_statement(size_t i) {
  return getRuleContext<AmberPTParser::Bond_equil_value_statementContext>(i);
}

std::vector<AmberPTParser::Bond_force_constant_statementContext *> AmberPTParser::Amber_ptContext::bond_force_constant_statement() {
  return getRuleContexts<AmberPTParser::Bond_force_constant_statementContext>();
}

AmberPTParser::Bond_force_constant_statementContext* AmberPTParser::Amber_ptContext::bond_force_constant_statement(size_t i) {
  return getRuleContext<AmberPTParser::Bond_force_constant_statementContext>(i);
}

std::vector<AmberPTParser::Bonds_inc_hydrogen_statementContext *> AmberPTParser::Amber_ptContext::bonds_inc_hydrogen_statement() {
  return getRuleContexts<AmberPTParser::Bonds_inc_hydrogen_statementContext>();
}

AmberPTParser::Bonds_inc_hydrogen_statementContext* AmberPTParser::Amber_ptContext::bonds_inc_hydrogen_statement(size_t i) {
  return getRuleContext<AmberPTParser::Bonds_inc_hydrogen_statementContext>(i);
}

std::vector<AmberPTParser::Bonds_without_hydrogen_statementContext *> AmberPTParser::Amber_ptContext::bonds_without_hydrogen_statement() {
  return getRuleContexts<AmberPTParser::Bonds_without_hydrogen_statementContext>();
}

AmberPTParser::Bonds_without_hydrogen_statementContext* AmberPTParser::Amber_ptContext::bonds_without_hydrogen_statement(size_t i) {
  return getRuleContext<AmberPTParser::Bonds_without_hydrogen_statementContext>(i);
}

std::vector<AmberPTParser::Box_dimensions_statementContext *> AmberPTParser::Amber_ptContext::box_dimensions_statement() {
  return getRuleContexts<AmberPTParser::Box_dimensions_statementContext>();
}

AmberPTParser::Box_dimensions_statementContext* AmberPTParser::Amber_ptContext::box_dimensions_statement(size_t i) {
  return getRuleContext<AmberPTParser::Box_dimensions_statementContext>(i);
}

std::vector<AmberPTParser::Cap_info_statementContext *> AmberPTParser::Amber_ptContext::cap_info_statement() {
  return getRuleContexts<AmberPTParser::Cap_info_statementContext>();
}

AmberPTParser::Cap_info_statementContext* AmberPTParser::Amber_ptContext::cap_info_statement(size_t i) {
  return getRuleContext<AmberPTParser::Cap_info_statementContext>(i);
}

std::vector<AmberPTParser::Cap_info2_statementContext *> AmberPTParser::Amber_ptContext::cap_info2_statement() {
  return getRuleContexts<AmberPTParser::Cap_info2_statementContext>();
}

AmberPTParser::Cap_info2_statementContext* AmberPTParser::Amber_ptContext::cap_info2_statement(size_t i) {
  return getRuleContext<AmberPTParser::Cap_info2_statementContext>(i);
}

std::vector<AmberPTParser::Charge_statementContext *> AmberPTParser::Amber_ptContext::charge_statement() {
  return getRuleContexts<AmberPTParser::Charge_statementContext>();
}

AmberPTParser::Charge_statementContext* AmberPTParser::Amber_ptContext::charge_statement(size_t i) {
  return getRuleContext<AmberPTParser::Charge_statementContext>(i);
}

std::vector<AmberPTParser::Cmap_count_statementContext *> AmberPTParser::Amber_ptContext::cmap_count_statement() {
  return getRuleContexts<AmberPTParser::Cmap_count_statementContext>();
}

AmberPTParser::Cmap_count_statementContext* AmberPTParser::Amber_ptContext::cmap_count_statement(size_t i) {
  return getRuleContext<AmberPTParser::Cmap_count_statementContext>(i);
}

std::vector<AmberPTParser::Cmap_resolution_statementContext *> AmberPTParser::Amber_ptContext::cmap_resolution_statement() {
  return getRuleContexts<AmberPTParser::Cmap_resolution_statementContext>();
}

AmberPTParser::Cmap_resolution_statementContext* AmberPTParser::Amber_ptContext::cmap_resolution_statement(size_t i) {
  return getRuleContext<AmberPTParser::Cmap_resolution_statementContext>(i);
}

std::vector<AmberPTParser::Cmap_parameter_statementContext *> AmberPTParser::Amber_ptContext::cmap_parameter_statement() {
  return getRuleContexts<AmberPTParser::Cmap_parameter_statementContext>();
}

AmberPTParser::Cmap_parameter_statementContext* AmberPTParser::Amber_ptContext::cmap_parameter_statement(size_t i) {
  return getRuleContext<AmberPTParser::Cmap_parameter_statementContext>(i);
}

std::vector<AmberPTParser::Cmap_index_statementContext *> AmberPTParser::Amber_ptContext::cmap_index_statement() {
  return getRuleContexts<AmberPTParser::Cmap_index_statementContext>();
}

AmberPTParser::Cmap_index_statementContext* AmberPTParser::Amber_ptContext::cmap_index_statement(size_t i) {
  return getRuleContext<AmberPTParser::Cmap_index_statementContext>(i);
}

std::vector<AmberPTParser::Dihedral_force_constant_statementContext *> AmberPTParser::Amber_ptContext::dihedral_force_constant_statement() {
  return getRuleContexts<AmberPTParser::Dihedral_force_constant_statementContext>();
}

AmberPTParser::Dihedral_force_constant_statementContext* AmberPTParser::Amber_ptContext::dihedral_force_constant_statement(size_t i) {
  return getRuleContext<AmberPTParser::Dihedral_force_constant_statementContext>(i);
}

std::vector<AmberPTParser::Dihedral_periodicity_statementContext *> AmberPTParser::Amber_ptContext::dihedral_periodicity_statement() {
  return getRuleContexts<AmberPTParser::Dihedral_periodicity_statementContext>();
}

AmberPTParser::Dihedral_periodicity_statementContext* AmberPTParser::Amber_ptContext::dihedral_periodicity_statement(size_t i) {
  return getRuleContext<AmberPTParser::Dihedral_periodicity_statementContext>(i);
}

std::vector<AmberPTParser::Dihedral_phase_statementContext *> AmberPTParser::Amber_ptContext::dihedral_phase_statement() {
  return getRuleContexts<AmberPTParser::Dihedral_phase_statementContext>();
}

AmberPTParser::Dihedral_phase_statementContext* AmberPTParser::Amber_ptContext::dihedral_phase_statement(size_t i) {
  return getRuleContext<AmberPTParser::Dihedral_phase_statementContext>(i);
}

std::vector<AmberPTParser::Dihedrals_inc_hydrogen_statementContext *> AmberPTParser::Amber_ptContext::dihedrals_inc_hydrogen_statement() {
  return getRuleContexts<AmberPTParser::Dihedrals_inc_hydrogen_statementContext>();
}

AmberPTParser::Dihedrals_inc_hydrogen_statementContext* AmberPTParser::Amber_ptContext::dihedrals_inc_hydrogen_statement(size_t i) {
  return getRuleContext<AmberPTParser::Dihedrals_inc_hydrogen_statementContext>(i);
}

std::vector<AmberPTParser::Dihedrals_without_hydrogen_statementContext *> AmberPTParser::Amber_ptContext::dihedrals_without_hydrogen_statement() {
  return getRuleContexts<AmberPTParser::Dihedrals_without_hydrogen_statementContext>();
}

AmberPTParser::Dihedrals_without_hydrogen_statementContext* AmberPTParser::Amber_ptContext::dihedrals_without_hydrogen_statement(size_t i) {
  return getRuleContext<AmberPTParser::Dihedrals_without_hydrogen_statementContext>(i);
}

std::vector<AmberPTParser::Excluded_atoms_list_statementContext *> AmberPTParser::Amber_ptContext::excluded_atoms_list_statement() {
  return getRuleContexts<AmberPTParser::Excluded_atoms_list_statementContext>();
}

AmberPTParser::Excluded_atoms_list_statementContext* AmberPTParser::Amber_ptContext::excluded_atoms_list_statement(size_t i) {
  return getRuleContext<AmberPTParser::Excluded_atoms_list_statementContext>(i);
}

std::vector<AmberPTParser::Hbcut_statementContext *> AmberPTParser::Amber_ptContext::hbcut_statement() {
  return getRuleContexts<AmberPTParser::Hbcut_statementContext>();
}

AmberPTParser::Hbcut_statementContext* AmberPTParser::Amber_ptContext::hbcut_statement(size_t i) {
  return getRuleContext<AmberPTParser::Hbcut_statementContext>(i);
}

std::vector<AmberPTParser::Hbond_acoef_statementContext *> AmberPTParser::Amber_ptContext::hbond_acoef_statement() {
  return getRuleContexts<AmberPTParser::Hbond_acoef_statementContext>();
}

AmberPTParser::Hbond_acoef_statementContext* AmberPTParser::Amber_ptContext::hbond_acoef_statement(size_t i) {
  return getRuleContext<AmberPTParser::Hbond_acoef_statementContext>(i);
}

std::vector<AmberPTParser::Hbond_bcoef_statementContext *> AmberPTParser::Amber_ptContext::hbond_bcoef_statement() {
  return getRuleContexts<AmberPTParser::Hbond_bcoef_statementContext>();
}

AmberPTParser::Hbond_bcoef_statementContext* AmberPTParser::Amber_ptContext::hbond_bcoef_statement(size_t i) {
  return getRuleContext<AmberPTParser::Hbond_bcoef_statementContext>(i);
}

std::vector<AmberPTParser::Ipol_statementContext *> AmberPTParser::Amber_ptContext::ipol_statement() {
  return getRuleContexts<AmberPTParser::Ipol_statementContext>();
}

AmberPTParser::Ipol_statementContext* AmberPTParser::Amber_ptContext::ipol_statement(size_t i) {
  return getRuleContext<AmberPTParser::Ipol_statementContext>(i);
}

std::vector<AmberPTParser::Irotat_statementContext *> AmberPTParser::Amber_ptContext::irotat_statement() {
  return getRuleContexts<AmberPTParser::Irotat_statementContext>();
}

AmberPTParser::Irotat_statementContext* AmberPTParser::Amber_ptContext::irotat_statement(size_t i) {
  return getRuleContext<AmberPTParser::Irotat_statementContext>(i);
}

std::vector<AmberPTParser::Join_array_statementContext *> AmberPTParser::Amber_ptContext::join_array_statement() {
  return getRuleContexts<AmberPTParser::Join_array_statementContext>();
}

AmberPTParser::Join_array_statementContext* AmberPTParser::Amber_ptContext::join_array_statement(size_t i) {
  return getRuleContext<AmberPTParser::Join_array_statementContext>(i);
}

std::vector<AmberPTParser::Lennard_jones_acoef_statementContext *> AmberPTParser::Amber_ptContext::lennard_jones_acoef_statement() {
  return getRuleContexts<AmberPTParser::Lennard_jones_acoef_statementContext>();
}

AmberPTParser::Lennard_jones_acoef_statementContext* AmberPTParser::Amber_ptContext::lennard_jones_acoef_statement(size_t i) {
  return getRuleContext<AmberPTParser::Lennard_jones_acoef_statementContext>(i);
}

std::vector<AmberPTParser::Lennard_jones_bcoef_statementContext *> AmberPTParser::Amber_ptContext::lennard_jones_bcoef_statement() {
  return getRuleContexts<AmberPTParser::Lennard_jones_bcoef_statementContext>();
}

AmberPTParser::Lennard_jones_bcoef_statementContext* AmberPTParser::Amber_ptContext::lennard_jones_bcoef_statement(size_t i) {
  return getRuleContext<AmberPTParser::Lennard_jones_bcoef_statementContext>(i);
}

std::vector<AmberPTParser::Mass_statementContext *> AmberPTParser::Amber_ptContext::mass_statement() {
  return getRuleContexts<AmberPTParser::Mass_statementContext>();
}

AmberPTParser::Mass_statementContext* AmberPTParser::Amber_ptContext::mass_statement(size_t i) {
  return getRuleContext<AmberPTParser::Mass_statementContext>(i);
}

std::vector<AmberPTParser::Nonbonded_parm_index_statementContext *> AmberPTParser::Amber_ptContext::nonbonded_parm_index_statement() {
  return getRuleContexts<AmberPTParser::Nonbonded_parm_index_statementContext>();
}

AmberPTParser::Nonbonded_parm_index_statementContext* AmberPTParser::Amber_ptContext::nonbonded_parm_index_statement(size_t i) {
  return getRuleContext<AmberPTParser::Nonbonded_parm_index_statementContext>(i);
}

std::vector<AmberPTParser::Number_excluded_atoms_statementContext *> AmberPTParser::Amber_ptContext::number_excluded_atoms_statement() {
  return getRuleContexts<AmberPTParser::Number_excluded_atoms_statementContext>();
}

AmberPTParser::Number_excluded_atoms_statementContext* AmberPTParser::Amber_ptContext::number_excluded_atoms_statement(size_t i) {
  return getRuleContext<AmberPTParser::Number_excluded_atoms_statementContext>(i);
}

std::vector<AmberPTParser::Pointers_statementContext *> AmberPTParser::Amber_ptContext::pointers_statement() {
  return getRuleContexts<AmberPTParser::Pointers_statementContext>();
}

AmberPTParser::Pointers_statementContext* AmberPTParser::Amber_ptContext::pointers_statement(size_t i) {
  return getRuleContext<AmberPTParser::Pointers_statementContext>(i);
}

std::vector<AmberPTParser::Polarizability_statementContext *> AmberPTParser::Amber_ptContext::polarizability_statement() {
  return getRuleContexts<AmberPTParser::Polarizability_statementContext>();
}

AmberPTParser::Polarizability_statementContext* AmberPTParser::Amber_ptContext::polarizability_statement(size_t i) {
  return getRuleContext<AmberPTParser::Polarizability_statementContext>(i);
}

std::vector<AmberPTParser::Radii_statementContext *> AmberPTParser::Amber_ptContext::radii_statement() {
  return getRuleContexts<AmberPTParser::Radii_statementContext>();
}

AmberPTParser::Radii_statementContext* AmberPTParser::Amber_ptContext::radii_statement(size_t i) {
  return getRuleContext<AmberPTParser::Radii_statementContext>(i);
}

std::vector<AmberPTParser::Radius_set_statementContext *> AmberPTParser::Amber_ptContext::radius_set_statement() {
  return getRuleContexts<AmberPTParser::Radius_set_statementContext>();
}

AmberPTParser::Radius_set_statementContext* AmberPTParser::Amber_ptContext::radius_set_statement(size_t i) {
  return getRuleContext<AmberPTParser::Radius_set_statementContext>(i);
}

std::vector<AmberPTParser::Residue_label_statementContext *> AmberPTParser::Amber_ptContext::residue_label_statement() {
  return getRuleContexts<AmberPTParser::Residue_label_statementContext>();
}

AmberPTParser::Residue_label_statementContext* AmberPTParser::Amber_ptContext::residue_label_statement(size_t i) {
  return getRuleContext<AmberPTParser::Residue_label_statementContext>(i);
}

std::vector<AmberPTParser::Residue_pointer_statementContext *> AmberPTParser::Amber_ptContext::residue_pointer_statement() {
  return getRuleContexts<AmberPTParser::Residue_pointer_statementContext>();
}

AmberPTParser::Residue_pointer_statementContext* AmberPTParser::Amber_ptContext::residue_pointer_statement(size_t i) {
  return getRuleContext<AmberPTParser::Residue_pointer_statementContext>(i);
}

std::vector<AmberPTParser::Scee_scale_factor_statementContext *> AmberPTParser::Amber_ptContext::scee_scale_factor_statement() {
  return getRuleContexts<AmberPTParser::Scee_scale_factor_statementContext>();
}

AmberPTParser::Scee_scale_factor_statementContext* AmberPTParser::Amber_ptContext::scee_scale_factor_statement(size_t i) {
  return getRuleContext<AmberPTParser::Scee_scale_factor_statementContext>(i);
}

std::vector<AmberPTParser::Scnb_scale_factor_statementContext *> AmberPTParser::Amber_ptContext::scnb_scale_factor_statement() {
  return getRuleContexts<AmberPTParser::Scnb_scale_factor_statementContext>();
}

AmberPTParser::Scnb_scale_factor_statementContext* AmberPTParser::Amber_ptContext::scnb_scale_factor_statement(size_t i) {
  return getRuleContext<AmberPTParser::Scnb_scale_factor_statementContext>(i);
}

std::vector<AmberPTParser::Screen_statementContext *> AmberPTParser::Amber_ptContext::screen_statement() {
  return getRuleContexts<AmberPTParser::Screen_statementContext>();
}

AmberPTParser::Screen_statementContext* AmberPTParser::Amber_ptContext::screen_statement(size_t i) {
  return getRuleContext<AmberPTParser::Screen_statementContext>(i);
}

std::vector<AmberPTParser::Solty_statementContext *> AmberPTParser::Amber_ptContext::solty_statement() {
  return getRuleContexts<AmberPTParser::Solty_statementContext>();
}

AmberPTParser::Solty_statementContext* AmberPTParser::Amber_ptContext::solty_statement(size_t i) {
  return getRuleContext<AmberPTParser::Solty_statementContext>(i);
}

std::vector<AmberPTParser::Solvent_pointers_statementContext *> AmberPTParser::Amber_ptContext::solvent_pointers_statement() {
  return getRuleContexts<AmberPTParser::Solvent_pointers_statementContext>();
}

AmberPTParser::Solvent_pointers_statementContext* AmberPTParser::Amber_ptContext::solvent_pointers_statement(size_t i) {
  return getRuleContext<AmberPTParser::Solvent_pointers_statementContext>(i);
}

std::vector<AmberPTParser::Title_statementContext *> AmberPTParser::Amber_ptContext::title_statement() {
  return getRuleContexts<AmberPTParser::Title_statementContext>();
}

AmberPTParser::Title_statementContext* AmberPTParser::Amber_ptContext::title_statement(size_t i) {
  return getRuleContext<AmberPTParser::Title_statementContext>(i);
}

std::vector<AmberPTParser::Tree_chain_classification_statementContext *> AmberPTParser::Amber_ptContext::tree_chain_classification_statement() {
  return getRuleContexts<AmberPTParser::Tree_chain_classification_statementContext>();
}

AmberPTParser::Tree_chain_classification_statementContext* AmberPTParser::Amber_ptContext::tree_chain_classification_statement(size_t i) {
  return getRuleContext<AmberPTParser::Tree_chain_classification_statementContext>(i);
}


size_t AmberPTParser::Amber_ptContext::getRuleIndex() const {
  return AmberPTParser::RuleAmber_pt;
}


std::any AmberPTParser::Amber_ptContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitAmber_pt(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Amber_ptContext* AmberPTParser::amber_pt() {
  Amber_ptContext *_localctx = _tracker.createInstance<Amber_ptContext>(_ctx, getState());
  enterRule(_localctx, 0, AmberPTParser::RuleAmber_pt);
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
    setState(110);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case AmberPTParser::VERSION: {
        setState(108);
        version_statement();
        break;
      }

      case AmberPTParser::FLAG: {
        setState(109);
        match(AmberPTParser::FLAG);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(165);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((((_la - 3) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 3)) & -1) != 0)) {
      setState(163);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case AmberPTParser::AMBER_ATOM_TYPE: {
          setState(112);
          amber_atom_type_statement();
          break;
        }

        case AmberPTParser::ANGLE_EQUIL_VALUE: {
          setState(113);
          angle_equil_value_statement();
          break;
        }

        case AmberPTParser::ANGLE_FORCE_CONSTANT: {
          setState(114);
          angle_force_constant_statement();
          break;
        }

        case AmberPTParser::ANGLES_INC_HYDROGEN: {
          setState(115);
          angles_inc_hydrogen_statement();
          break;
        }

        case AmberPTParser::ANGLES_WITHOUT_HYDROGEN: {
          setState(116);
          angles_without_hydrogen_statement();
          break;
        }

        case AmberPTParser::ATOMIC_NUMBER: {
          setState(117);
          atomic_number_statement();
          break;
        }

        case AmberPTParser::ATOM_NAME: {
          setState(118);
          atom_name_statement();
          break;
        }

        case AmberPTParser::ATOM_TYPE_INDEX: {
          setState(119);
          atom_type_index_statement();
          break;
        }

        case AmberPTParser::ATOMS_PER_MOLECULE: {
          setState(120);
          atoms_per_molecule_statement();
          break;
        }

        case AmberPTParser::BOND_EQUIL_VALUE: {
          setState(121);
          bond_equil_value_statement();
          break;
        }

        case AmberPTParser::BOND_FORCE_CONSTANT: {
          setState(122);
          bond_force_constant_statement();
          break;
        }

        case AmberPTParser::BONDS_INC_HYDROGEN: {
          setState(123);
          bonds_inc_hydrogen_statement();
          break;
        }

        case AmberPTParser::BONDS_WITHOUT_HYDROGEN: {
          setState(124);
          bonds_without_hydrogen_statement();
          break;
        }

        case AmberPTParser::BOX_DIMENSIONS: {
          setState(125);
          box_dimensions_statement();
          break;
        }

        case AmberPTParser::CAP_INFO: {
          setState(126);
          cap_info_statement();
          break;
        }

        case AmberPTParser::CAP_INFO2: {
          setState(127);
          cap_info2_statement();
          break;
        }

        case AmberPTParser::CHARGE: {
          setState(128);
          charge_statement();
          break;
        }

        case AmberPTParser::CMAP_COUNT: {
          setState(129);
          cmap_count_statement();
          break;
        }

        case AmberPTParser::CMAP_RESOLUTION: {
          setState(130);
          cmap_resolution_statement();
          break;
        }

        case AmberPTParser::CMAP_PARAMETER_01:
        case AmberPTParser::CMAP_PARAMETER_02:
        case AmberPTParser::CMAP_PARAMETER_03:
        case AmberPTParser::CMAP_PARAMETER_04:
        case AmberPTParser::CMAP_PARAMETER_05:
        case AmberPTParser::CMAP_PARAMETER_06:
        case AmberPTParser::CMAP_PARAMETER_07:
        case AmberPTParser::CMAP_PARAMETER_08:
        case AmberPTParser::CMAP_PARAMETER_09:
        case AmberPTParser::CMAP_PARAMETER_10:
        case AmberPTParser::CMAP_PARAMETER_11:
        case AmberPTParser::CMAP_PARAMETER_12:
        case AmberPTParser::CMAP_PARAMETER_13:
        case AmberPTParser::CMAP_PARAMETER_14: {
          setState(131);
          cmap_parameter_statement();
          break;
        }

        case AmberPTParser::CMAP_INDEX: {
          setState(132);
          cmap_index_statement();
          break;
        }

        case AmberPTParser::DIHEDRAL_FORCE_CONSTANT: {
          setState(133);
          dihedral_force_constant_statement();
          break;
        }

        case AmberPTParser::DIHEDRAL_PERIODICITY: {
          setState(134);
          dihedral_periodicity_statement();
          break;
        }

        case AmberPTParser::DIHEDRAL_PHASE: {
          setState(135);
          dihedral_phase_statement();
          break;
        }

        case AmberPTParser::DIHEDRALS_INC_HYDROGEN: {
          setState(136);
          dihedrals_inc_hydrogen_statement();
          break;
        }

        case AmberPTParser::DIHEDRALS_WITHOUT_HYDROGEN: {
          setState(137);
          dihedrals_without_hydrogen_statement();
          break;
        }

        case AmberPTParser::EXCLUDED_ATOMS_LIST: {
          setState(138);
          excluded_atoms_list_statement();
          break;
        }

        case AmberPTParser::HBCUT: {
          setState(139);
          hbcut_statement();
          break;
        }

        case AmberPTParser::HBOND_ACOEF: {
          setState(140);
          hbond_acoef_statement();
          break;
        }

        case AmberPTParser::HBOND_BCOEF: {
          setState(141);
          hbond_bcoef_statement();
          break;
        }

        case AmberPTParser::IPOL: {
          setState(142);
          ipol_statement();
          break;
        }

        case AmberPTParser::IROTAT: {
          setState(143);
          irotat_statement();
          break;
        }

        case AmberPTParser::JOIN_ARRAY: {
          setState(144);
          join_array_statement();
          break;
        }

        case AmberPTParser::LENNARD_JONES_ACOEF: {
          setState(145);
          lennard_jones_acoef_statement();
          break;
        }

        case AmberPTParser::LENNARD_JONES_BCOEF: {
          setState(146);
          lennard_jones_bcoef_statement();
          break;
        }

        case AmberPTParser::MASS: {
          setState(147);
          mass_statement();
          break;
        }

        case AmberPTParser::NONBONDED_PARM_INDEX: {
          setState(148);
          nonbonded_parm_index_statement();
          break;
        }

        case AmberPTParser::NUMBER_EXCLUDED_ATOMS: {
          setState(149);
          number_excluded_atoms_statement();
          break;
        }

        case AmberPTParser::POINTERS: {
          setState(150);
          pointers_statement();
          break;
        }

        case AmberPTParser::POLARIZABILITY: {
          setState(151);
          polarizability_statement();
          break;
        }

        case AmberPTParser::RADII: {
          setState(152);
          radii_statement();
          break;
        }

        case AmberPTParser::RADIUS_SET: {
          setState(153);
          radius_set_statement();
          break;
        }

        case AmberPTParser::RESIDUE_LABEL: {
          setState(154);
          residue_label_statement();
          break;
        }

        case AmberPTParser::RESIDUE_POINTER: {
          setState(155);
          residue_pointer_statement();
          break;
        }

        case AmberPTParser::SCEE_SCALE_FACTOR: {
          setState(156);
          scee_scale_factor_statement();
          break;
        }

        case AmberPTParser::SCNB_SCALE_FACTOR: {
          setState(157);
          scnb_scale_factor_statement();
          break;
        }

        case AmberPTParser::SCREEN: {
          setState(158);
          screen_statement();
          break;
        }

        case AmberPTParser::SOLTY: {
          setState(159);
          solty_statement();
          break;
        }

        case AmberPTParser::SOLVENT_POINTERS: {
          setState(160);
          solvent_pointers_statement();
          break;
        }

        case AmberPTParser::TITLE: {
          setState(161);
          title_statement();
          break;
        }

        case AmberPTParser::TREE_CHAIN_CLASSIFICATION: {
          setState(162);
          tree_chain_classification_statement();
          break;
        }

      default:
        throw NoViableAltException(this);
      }
      setState(167);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(168);
    match(AmberPTParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Version_statementContext ------------------------------------------------------------------

AmberPTParser::Version_statementContext::Version_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Version_statementContext::VERSION() {
  return getToken(AmberPTParser::VERSION, 0);
}

tree::TerminalNode* AmberPTParser::Version_statementContext::VERSION_STAMP() {
  return getToken(AmberPTParser::VERSION_STAMP, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Version_statementContext::Equ_op() {
  return getTokens(AmberPTParser::Equ_op);
}

tree::TerminalNode* AmberPTParser::Version_statementContext::Equ_op(size_t i) {
  return getToken(AmberPTParser::Equ_op, i);
}

tree::TerminalNode* AmberPTParser::Version_statementContext::Version() {
  return getToken(AmberPTParser::Version, 0);
}

tree::TerminalNode* AmberPTParser::Version_statementContext::DATE() {
  return getToken(AmberPTParser::DATE, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Version_statementContext::Date_time() {
  return getTokens(AmberPTParser::Date_time);
}

tree::TerminalNode* AmberPTParser::Version_statementContext::Date_time(size_t i) {
  return getToken(AmberPTParser::Date_time, i);
}

tree::TerminalNode* AmberPTParser::Version_statementContext::FLAG_VS() {
  return getToken(AmberPTParser::FLAG_VS, 0);
}

tree::TerminalNode* AmberPTParser::Version_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}


size_t AmberPTParser::Version_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleVersion_statement;
}


std::any AmberPTParser::Version_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitVersion_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Version_statementContext* AmberPTParser::version_statement() {
  Version_statementContext *_localctx = _tracker.createInstance<Version_statementContext>(_ctx, getState());
  enterRule(_localctx, 2, AmberPTParser::RuleVersion_statement);
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
    setState(170);
    match(AmberPTParser::VERSION);
    setState(171);
    match(AmberPTParser::VERSION_STAMP);
    setState(172);
    match(AmberPTParser::Equ_op);
    setState(173);
    match(AmberPTParser::Version);
    setState(174);
    match(AmberPTParser::DATE);
    setState(175);
    match(AmberPTParser::Equ_op);
    setState(176);
    match(AmberPTParser::Date_time);
    setState(178);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == AmberPTParser::Date_time) {
      setState(177);
      match(AmberPTParser::Date_time);
    }
    setState(180);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_VS)) {
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

//----------------- Amber_atom_type_statementContext ------------------------------------------------------------------

AmberPTParser::Amber_atom_type_statementContext::Amber_atom_type_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Amber_atom_type_statementContext::AMBER_ATOM_TYPE() {
  return getToken(AmberPTParser::AMBER_ATOM_TYPE, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Amber_atom_type_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Amber_atom_type_statementContext::FLAG_AA() {
  return getToken(AmberPTParser::FLAG_AA, 0);
}

tree::TerminalNode* AmberPTParser::Amber_atom_type_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Amber_atom_type_statementContext::Simple_name() {
  return getTokens(AmberPTParser::Simple_name);
}

tree::TerminalNode* AmberPTParser::Amber_atom_type_statementContext::Simple_name(size_t i) {
  return getToken(AmberPTParser::Simple_name, i);
}


size_t AmberPTParser::Amber_atom_type_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleAmber_atom_type_statement;
}


std::any AmberPTParser::Amber_atom_type_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitAmber_atom_type_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Amber_atom_type_statementContext* AmberPTParser::amber_atom_type_statement() {
  Amber_atom_type_statementContext *_localctx = _tracker.createInstance<Amber_atom_type_statementContext>(_ctx, getState());
  enterRule(_localctx, 4, AmberPTParser::RuleAmber_atom_type_statement);
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
    setState(182);
    match(AmberPTParser::AMBER_ATOM_TYPE);
    setState(183);
    format_function();
    setState(187);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Simple_name) {
      setState(184);
      match(AmberPTParser::Simple_name);
      setState(189);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(190);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_AA)) {
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

//----------------- Angle_equil_value_statementContext ------------------------------------------------------------------

AmberPTParser::Angle_equil_value_statementContext::Angle_equil_value_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Angle_equil_value_statementContext::ANGLE_EQUIL_VALUE() {
  return getToken(AmberPTParser::ANGLE_EQUIL_VALUE, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Angle_equil_value_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Angle_equil_value_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Angle_equil_value_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Angle_equil_value_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Angle_equil_value_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Angle_equil_value_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleAngle_equil_value_statement;
}


std::any AmberPTParser::Angle_equil_value_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitAngle_equil_value_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Angle_equil_value_statementContext* AmberPTParser::angle_equil_value_statement() {
  Angle_equil_value_statementContext *_localctx = _tracker.createInstance<Angle_equil_value_statementContext>(_ctx, getState());
  enterRule(_localctx, 6, AmberPTParser::RuleAngle_equil_value_statement);
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
    setState(192);
    match(AmberPTParser::ANGLE_EQUIL_VALUE);
    setState(193);
    format_function();
    setState(197);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(194);
      match(AmberPTParser::Real);
      setState(199);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(200);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Angle_force_constant_statementContext ------------------------------------------------------------------

AmberPTParser::Angle_force_constant_statementContext::Angle_force_constant_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Angle_force_constant_statementContext::ANGLE_FORCE_CONSTANT() {
  return getToken(AmberPTParser::ANGLE_FORCE_CONSTANT, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Angle_force_constant_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Angle_force_constant_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Angle_force_constant_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Angle_force_constant_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Angle_force_constant_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Angle_force_constant_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleAngle_force_constant_statement;
}


std::any AmberPTParser::Angle_force_constant_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitAngle_force_constant_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Angle_force_constant_statementContext* AmberPTParser::angle_force_constant_statement() {
  Angle_force_constant_statementContext *_localctx = _tracker.createInstance<Angle_force_constant_statementContext>(_ctx, getState());
  enterRule(_localctx, 8, AmberPTParser::RuleAngle_force_constant_statement);
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
    setState(202);
    match(AmberPTParser::ANGLE_FORCE_CONSTANT);
    setState(203);
    format_function();
    setState(207);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(204);
      match(AmberPTParser::Real);
      setState(209);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(210);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Angles_inc_hydrogen_statementContext ------------------------------------------------------------------

AmberPTParser::Angles_inc_hydrogen_statementContext::Angles_inc_hydrogen_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Angles_inc_hydrogen_statementContext::ANGLES_INC_HYDROGEN() {
  return getToken(AmberPTParser::ANGLES_INC_HYDROGEN, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Angles_inc_hydrogen_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Angles_inc_hydrogen_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Angles_inc_hydrogen_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Angles_inc_hydrogen_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Angles_inc_hydrogen_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Angles_inc_hydrogen_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleAngles_inc_hydrogen_statement;
}


std::any AmberPTParser::Angles_inc_hydrogen_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitAngles_inc_hydrogen_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Angles_inc_hydrogen_statementContext* AmberPTParser::angles_inc_hydrogen_statement() {
  Angles_inc_hydrogen_statementContext *_localctx = _tracker.createInstance<Angles_inc_hydrogen_statementContext>(_ctx, getState());
  enterRule(_localctx, 10, AmberPTParser::RuleAngles_inc_hydrogen_statement);
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
    setState(212);
    match(AmberPTParser::ANGLES_INC_HYDROGEN);
    setState(213);
    format_function();
    setState(217);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(214);
      match(AmberPTParser::Integer);
      setState(219);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(220);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Angles_without_hydrogen_statementContext ------------------------------------------------------------------

AmberPTParser::Angles_without_hydrogen_statementContext::Angles_without_hydrogen_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Angles_without_hydrogen_statementContext::ANGLES_WITHOUT_HYDROGEN() {
  return getToken(AmberPTParser::ANGLES_WITHOUT_HYDROGEN, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Angles_without_hydrogen_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Angles_without_hydrogen_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Angles_without_hydrogen_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Angles_without_hydrogen_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Angles_without_hydrogen_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Angles_without_hydrogen_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleAngles_without_hydrogen_statement;
}


std::any AmberPTParser::Angles_without_hydrogen_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitAngles_without_hydrogen_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Angles_without_hydrogen_statementContext* AmberPTParser::angles_without_hydrogen_statement() {
  Angles_without_hydrogen_statementContext *_localctx = _tracker.createInstance<Angles_without_hydrogen_statementContext>(_ctx, getState());
  enterRule(_localctx, 12, AmberPTParser::RuleAngles_without_hydrogen_statement);
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
    setState(222);
    match(AmberPTParser::ANGLES_WITHOUT_HYDROGEN);
    setState(223);
    format_function();
    setState(227);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(224);
      match(AmberPTParser::Integer);
      setState(229);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(230);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Atomic_number_statementContext ------------------------------------------------------------------

AmberPTParser::Atomic_number_statementContext::Atomic_number_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Atomic_number_statementContext::ATOMIC_NUMBER() {
  return getToken(AmberPTParser::ATOMIC_NUMBER, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Atomic_number_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Atomic_number_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Atomic_number_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Atomic_number_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Atomic_number_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Atomic_number_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleAtomic_number_statement;
}


std::any AmberPTParser::Atomic_number_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitAtomic_number_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Atomic_number_statementContext* AmberPTParser::atomic_number_statement() {
  Atomic_number_statementContext *_localctx = _tracker.createInstance<Atomic_number_statementContext>(_ctx, getState());
  enterRule(_localctx, 14, AmberPTParser::RuleAtomic_number_statement);
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
    setState(232);
    match(AmberPTParser::ATOMIC_NUMBER);
    setState(233);
    format_function();
    setState(237);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(234);
      match(AmberPTParser::Integer);
      setState(239);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(240);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Atom_name_statementContext ------------------------------------------------------------------

AmberPTParser::Atom_name_statementContext::Atom_name_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Atom_name_statementContext::ATOM_NAME() {
  return getToken(AmberPTParser::ATOM_NAME, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Atom_name_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Atom_name_statementContext::FLAG_AA() {
  return getToken(AmberPTParser::FLAG_AA, 0);
}

tree::TerminalNode* AmberPTParser::Atom_name_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Atom_name_statementContext::Simple_name() {
  return getTokens(AmberPTParser::Simple_name);
}

tree::TerminalNode* AmberPTParser::Atom_name_statementContext::Simple_name(size_t i) {
  return getToken(AmberPTParser::Simple_name, i);
}


size_t AmberPTParser::Atom_name_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleAtom_name_statement;
}


std::any AmberPTParser::Atom_name_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitAtom_name_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Atom_name_statementContext* AmberPTParser::atom_name_statement() {
  Atom_name_statementContext *_localctx = _tracker.createInstance<Atom_name_statementContext>(_ctx, getState());
  enterRule(_localctx, 16, AmberPTParser::RuleAtom_name_statement);
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
    setState(242);
    match(AmberPTParser::ATOM_NAME);
    setState(243);
    format_function();
    setState(247);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Simple_name) {
      setState(244);
      match(AmberPTParser::Simple_name);
      setState(249);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(250);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_AA)) {
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

//----------------- Atom_type_index_statementContext ------------------------------------------------------------------

AmberPTParser::Atom_type_index_statementContext::Atom_type_index_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Atom_type_index_statementContext::ATOM_TYPE_INDEX() {
  return getToken(AmberPTParser::ATOM_TYPE_INDEX, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Atom_type_index_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Atom_type_index_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Atom_type_index_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Atom_type_index_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Atom_type_index_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Atom_type_index_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleAtom_type_index_statement;
}


std::any AmberPTParser::Atom_type_index_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitAtom_type_index_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Atom_type_index_statementContext* AmberPTParser::atom_type_index_statement() {
  Atom_type_index_statementContext *_localctx = _tracker.createInstance<Atom_type_index_statementContext>(_ctx, getState());
  enterRule(_localctx, 18, AmberPTParser::RuleAtom_type_index_statement);
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
    setState(252);
    match(AmberPTParser::ATOM_TYPE_INDEX);
    setState(253);
    format_function();
    setState(257);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(254);
      match(AmberPTParser::Integer);
      setState(259);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(260);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Atoms_per_molecule_statementContext ------------------------------------------------------------------

AmberPTParser::Atoms_per_molecule_statementContext::Atoms_per_molecule_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Atoms_per_molecule_statementContext::ATOMS_PER_MOLECULE() {
  return getToken(AmberPTParser::ATOMS_PER_MOLECULE, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Atoms_per_molecule_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Atoms_per_molecule_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Atoms_per_molecule_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Atoms_per_molecule_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Atoms_per_molecule_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Atoms_per_molecule_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleAtoms_per_molecule_statement;
}


std::any AmberPTParser::Atoms_per_molecule_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitAtoms_per_molecule_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Atoms_per_molecule_statementContext* AmberPTParser::atoms_per_molecule_statement() {
  Atoms_per_molecule_statementContext *_localctx = _tracker.createInstance<Atoms_per_molecule_statementContext>(_ctx, getState());
  enterRule(_localctx, 20, AmberPTParser::RuleAtoms_per_molecule_statement);
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
    setState(262);
    match(AmberPTParser::ATOMS_PER_MOLECULE);
    setState(263);
    format_function();
    setState(267);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(264);
      match(AmberPTParser::Integer);
      setState(269);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(270);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Bond_equil_value_statementContext ------------------------------------------------------------------

AmberPTParser::Bond_equil_value_statementContext::Bond_equil_value_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Bond_equil_value_statementContext::BOND_EQUIL_VALUE() {
  return getToken(AmberPTParser::BOND_EQUIL_VALUE, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Bond_equil_value_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Bond_equil_value_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Bond_equil_value_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Bond_equil_value_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Bond_equil_value_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Bond_equil_value_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleBond_equil_value_statement;
}


std::any AmberPTParser::Bond_equil_value_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitBond_equil_value_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Bond_equil_value_statementContext* AmberPTParser::bond_equil_value_statement() {
  Bond_equil_value_statementContext *_localctx = _tracker.createInstance<Bond_equil_value_statementContext>(_ctx, getState());
  enterRule(_localctx, 22, AmberPTParser::RuleBond_equil_value_statement);
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
    setState(272);
    match(AmberPTParser::BOND_EQUIL_VALUE);
    setState(273);
    format_function();
    setState(277);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(274);
      match(AmberPTParser::Real);
      setState(279);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(280);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Bond_force_constant_statementContext ------------------------------------------------------------------

AmberPTParser::Bond_force_constant_statementContext::Bond_force_constant_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Bond_force_constant_statementContext::BOND_FORCE_CONSTANT() {
  return getToken(AmberPTParser::BOND_FORCE_CONSTANT, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Bond_force_constant_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Bond_force_constant_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Bond_force_constant_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Bond_force_constant_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Bond_force_constant_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Bond_force_constant_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleBond_force_constant_statement;
}


std::any AmberPTParser::Bond_force_constant_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitBond_force_constant_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Bond_force_constant_statementContext* AmberPTParser::bond_force_constant_statement() {
  Bond_force_constant_statementContext *_localctx = _tracker.createInstance<Bond_force_constant_statementContext>(_ctx, getState());
  enterRule(_localctx, 24, AmberPTParser::RuleBond_force_constant_statement);
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
    setState(282);
    match(AmberPTParser::BOND_FORCE_CONSTANT);
    setState(283);
    format_function();
    setState(287);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(284);
      match(AmberPTParser::Real);
      setState(289);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(290);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Bonds_inc_hydrogen_statementContext ------------------------------------------------------------------

AmberPTParser::Bonds_inc_hydrogen_statementContext::Bonds_inc_hydrogen_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Bonds_inc_hydrogen_statementContext::BONDS_INC_HYDROGEN() {
  return getToken(AmberPTParser::BONDS_INC_HYDROGEN, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Bonds_inc_hydrogen_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Bonds_inc_hydrogen_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Bonds_inc_hydrogen_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Bonds_inc_hydrogen_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Bonds_inc_hydrogen_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Bonds_inc_hydrogen_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleBonds_inc_hydrogen_statement;
}


std::any AmberPTParser::Bonds_inc_hydrogen_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitBonds_inc_hydrogen_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Bonds_inc_hydrogen_statementContext* AmberPTParser::bonds_inc_hydrogen_statement() {
  Bonds_inc_hydrogen_statementContext *_localctx = _tracker.createInstance<Bonds_inc_hydrogen_statementContext>(_ctx, getState());
  enterRule(_localctx, 26, AmberPTParser::RuleBonds_inc_hydrogen_statement);
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
    setState(292);
    match(AmberPTParser::BONDS_INC_HYDROGEN);
    setState(293);
    format_function();
    setState(297);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(294);
      match(AmberPTParser::Integer);
      setState(299);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(300);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Bonds_without_hydrogen_statementContext ------------------------------------------------------------------

AmberPTParser::Bonds_without_hydrogen_statementContext::Bonds_without_hydrogen_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Bonds_without_hydrogen_statementContext::BONDS_WITHOUT_HYDROGEN() {
  return getToken(AmberPTParser::BONDS_WITHOUT_HYDROGEN, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Bonds_without_hydrogen_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Bonds_without_hydrogen_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Bonds_without_hydrogen_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Bonds_without_hydrogen_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Bonds_without_hydrogen_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Bonds_without_hydrogen_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleBonds_without_hydrogen_statement;
}


std::any AmberPTParser::Bonds_without_hydrogen_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitBonds_without_hydrogen_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Bonds_without_hydrogen_statementContext* AmberPTParser::bonds_without_hydrogen_statement() {
  Bonds_without_hydrogen_statementContext *_localctx = _tracker.createInstance<Bonds_without_hydrogen_statementContext>(_ctx, getState());
  enterRule(_localctx, 28, AmberPTParser::RuleBonds_without_hydrogen_statement);
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
    setState(302);
    match(AmberPTParser::BONDS_WITHOUT_HYDROGEN);
    setState(303);
    format_function();
    setState(307);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(304);
      match(AmberPTParser::Integer);
      setState(309);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(310);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Box_dimensions_statementContext ------------------------------------------------------------------

AmberPTParser::Box_dimensions_statementContext::Box_dimensions_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Box_dimensions_statementContext::BOX_DIMENSIONS() {
  return getToken(AmberPTParser::BOX_DIMENSIONS, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Box_dimensions_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Box_dimensions_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Box_dimensions_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Box_dimensions_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Box_dimensions_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Box_dimensions_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleBox_dimensions_statement;
}


std::any AmberPTParser::Box_dimensions_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitBox_dimensions_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Box_dimensions_statementContext* AmberPTParser::box_dimensions_statement() {
  Box_dimensions_statementContext *_localctx = _tracker.createInstance<Box_dimensions_statementContext>(_ctx, getState());
  enterRule(_localctx, 30, AmberPTParser::RuleBox_dimensions_statement);
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
    setState(312);
    match(AmberPTParser::BOX_DIMENSIONS);
    setState(313);
    format_function();
    setState(317);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(314);
      match(AmberPTParser::Real);
      setState(319);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(320);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Cap_info_statementContext ------------------------------------------------------------------

AmberPTParser::Cap_info_statementContext::Cap_info_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Cap_info_statementContext::CAP_INFO() {
  return getToken(AmberPTParser::CAP_INFO, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Cap_info_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Cap_info_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Cap_info_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Cap_info_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Cap_info_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Cap_info_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleCap_info_statement;
}


std::any AmberPTParser::Cap_info_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitCap_info_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Cap_info_statementContext* AmberPTParser::cap_info_statement() {
  Cap_info_statementContext *_localctx = _tracker.createInstance<Cap_info_statementContext>(_ctx, getState());
  enterRule(_localctx, 32, AmberPTParser::RuleCap_info_statement);
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
    setState(322);
    match(AmberPTParser::CAP_INFO);
    setState(323);
    format_function();
    setState(327);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(324);
      match(AmberPTParser::Integer);
      setState(329);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(330);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Cap_info2_statementContext ------------------------------------------------------------------

AmberPTParser::Cap_info2_statementContext::Cap_info2_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Cap_info2_statementContext::CAP_INFO2() {
  return getToken(AmberPTParser::CAP_INFO2, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Cap_info2_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Cap_info2_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Cap_info2_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Cap_info2_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Cap_info2_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Cap_info2_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleCap_info2_statement;
}


std::any AmberPTParser::Cap_info2_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitCap_info2_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Cap_info2_statementContext* AmberPTParser::cap_info2_statement() {
  Cap_info2_statementContext *_localctx = _tracker.createInstance<Cap_info2_statementContext>(_ctx, getState());
  enterRule(_localctx, 34, AmberPTParser::RuleCap_info2_statement);
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
    setState(332);
    match(AmberPTParser::CAP_INFO2);
    setState(333);
    format_function();
    setState(337);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(334);
      match(AmberPTParser::Real);
      setState(339);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(340);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Charge_statementContext ------------------------------------------------------------------

AmberPTParser::Charge_statementContext::Charge_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Charge_statementContext::CHARGE() {
  return getToken(AmberPTParser::CHARGE, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Charge_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Charge_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Charge_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Charge_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Charge_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Charge_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleCharge_statement;
}


std::any AmberPTParser::Charge_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitCharge_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Charge_statementContext* AmberPTParser::charge_statement() {
  Charge_statementContext *_localctx = _tracker.createInstance<Charge_statementContext>(_ctx, getState());
  enterRule(_localctx, 36, AmberPTParser::RuleCharge_statement);
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
    setState(342);
    match(AmberPTParser::CHARGE);
    setState(343);
    format_function();
    setState(347);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(344);
      match(AmberPTParser::Real);
      setState(349);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(350);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Cmap_count_statementContext ------------------------------------------------------------------

AmberPTParser::Cmap_count_statementContext::Cmap_count_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Cmap_count_statementContext::CMAP_COUNT() {
  return getToken(AmberPTParser::CMAP_COUNT, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Cmap_count_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Cmap_count_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_count_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Cmap_count_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Cmap_count_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Cmap_count_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleCmap_count_statement;
}


std::any AmberPTParser::Cmap_count_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitCmap_count_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Cmap_count_statementContext* AmberPTParser::cmap_count_statement() {
  Cmap_count_statementContext *_localctx = _tracker.createInstance<Cmap_count_statementContext>(_ctx, getState());
  enterRule(_localctx, 38, AmberPTParser::RuleCmap_count_statement);
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
    match(AmberPTParser::CMAP_COUNT);
    setState(353);
    format_function();
    setState(357);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(354);
      match(AmberPTParser::Integer);
      setState(359);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(360);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Cmap_resolution_statementContext ------------------------------------------------------------------

AmberPTParser::Cmap_resolution_statementContext::Cmap_resolution_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Cmap_resolution_statementContext::CMAP_RESOLUTION() {
  return getToken(AmberPTParser::CMAP_RESOLUTION, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Cmap_resolution_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Cmap_resolution_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_resolution_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Cmap_resolution_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Cmap_resolution_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Cmap_resolution_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleCmap_resolution_statement;
}


std::any AmberPTParser::Cmap_resolution_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitCmap_resolution_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Cmap_resolution_statementContext* AmberPTParser::cmap_resolution_statement() {
  Cmap_resolution_statementContext *_localctx = _tracker.createInstance<Cmap_resolution_statementContext>(_ctx, getState());
  enterRule(_localctx, 40, AmberPTParser::RuleCmap_resolution_statement);
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
    setState(362);
    match(AmberPTParser::CMAP_RESOLUTION);
    setState(363);
    format_function();
    setState(367);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(364);
      match(AmberPTParser::Integer);
      setState(369);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(370);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Cmap_parameter_statementContext ------------------------------------------------------------------

AmberPTParser::Cmap_parameter_statementContext::Cmap_parameter_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

AmberPTParser::Format_functionContext* AmberPTParser::Cmap_parameter_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_01() {
  return getToken(AmberPTParser::CMAP_PARAMETER_01, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_02() {
  return getToken(AmberPTParser::CMAP_PARAMETER_02, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_03() {
  return getToken(AmberPTParser::CMAP_PARAMETER_03, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_04() {
  return getToken(AmberPTParser::CMAP_PARAMETER_04, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_05() {
  return getToken(AmberPTParser::CMAP_PARAMETER_05, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_06() {
  return getToken(AmberPTParser::CMAP_PARAMETER_06, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_07() {
  return getToken(AmberPTParser::CMAP_PARAMETER_07, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_08() {
  return getToken(AmberPTParser::CMAP_PARAMETER_08, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_09() {
  return getToken(AmberPTParser::CMAP_PARAMETER_09, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_10() {
  return getToken(AmberPTParser::CMAP_PARAMETER_10, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_11() {
  return getToken(AmberPTParser::CMAP_PARAMETER_11, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_12() {
  return getToken(AmberPTParser::CMAP_PARAMETER_12, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_13() {
  return getToken(AmberPTParser::CMAP_PARAMETER_13, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::CMAP_PARAMETER_14() {
  return getToken(AmberPTParser::CMAP_PARAMETER_14, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Cmap_parameter_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Cmap_parameter_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Cmap_parameter_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleCmap_parameter_statement;
}


std::any AmberPTParser::Cmap_parameter_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitCmap_parameter_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Cmap_parameter_statementContext* AmberPTParser::cmap_parameter_statement() {
  Cmap_parameter_statementContext *_localctx = _tracker.createInstance<Cmap_parameter_statementContext>(_ctx, getState());
  enterRule(_localctx, 42, AmberPTParser::RuleCmap_parameter_statement);
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
    setState(372);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 68715282432) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(373);
    format_function();
    setState(377);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(374);
      match(AmberPTParser::Real);
      setState(379);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(380);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Cmap_index_statementContext ------------------------------------------------------------------

AmberPTParser::Cmap_index_statementContext::Cmap_index_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Cmap_index_statementContext::CMAP_INDEX() {
  return getToken(AmberPTParser::CMAP_INDEX, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Cmap_index_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Cmap_index_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Cmap_index_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Cmap_index_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Cmap_index_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Cmap_index_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleCmap_index_statement;
}


std::any AmberPTParser::Cmap_index_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitCmap_index_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Cmap_index_statementContext* AmberPTParser::cmap_index_statement() {
  Cmap_index_statementContext *_localctx = _tracker.createInstance<Cmap_index_statementContext>(_ctx, getState());
  enterRule(_localctx, 44, AmberPTParser::RuleCmap_index_statement);
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
    setState(382);
    match(AmberPTParser::CMAP_INDEX);
    setState(383);
    format_function();
    setState(387);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(384);
      match(AmberPTParser::Integer);
      setState(389);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(390);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Dihedral_force_constant_statementContext ------------------------------------------------------------------

AmberPTParser::Dihedral_force_constant_statementContext::Dihedral_force_constant_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Dihedral_force_constant_statementContext::DIHEDRAL_FORCE_CONSTANT() {
  return getToken(AmberPTParser::DIHEDRAL_FORCE_CONSTANT, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Dihedral_force_constant_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Dihedral_force_constant_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Dihedral_force_constant_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Dihedral_force_constant_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Dihedral_force_constant_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Dihedral_force_constant_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleDihedral_force_constant_statement;
}


std::any AmberPTParser::Dihedral_force_constant_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_force_constant_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Dihedral_force_constant_statementContext* AmberPTParser::dihedral_force_constant_statement() {
  Dihedral_force_constant_statementContext *_localctx = _tracker.createInstance<Dihedral_force_constant_statementContext>(_ctx, getState());
  enterRule(_localctx, 46, AmberPTParser::RuleDihedral_force_constant_statement);
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
    setState(392);
    match(AmberPTParser::DIHEDRAL_FORCE_CONSTANT);
    setState(393);
    format_function();
    setState(397);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(394);
      match(AmberPTParser::Real);
      setState(399);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(400);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Dihedral_periodicity_statementContext ------------------------------------------------------------------

AmberPTParser::Dihedral_periodicity_statementContext::Dihedral_periodicity_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Dihedral_periodicity_statementContext::DIHEDRAL_PERIODICITY() {
  return getToken(AmberPTParser::DIHEDRAL_PERIODICITY, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Dihedral_periodicity_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Dihedral_periodicity_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Dihedral_periodicity_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Dihedral_periodicity_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Dihedral_periodicity_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Dihedral_periodicity_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleDihedral_periodicity_statement;
}


std::any AmberPTParser::Dihedral_periodicity_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_periodicity_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Dihedral_periodicity_statementContext* AmberPTParser::dihedral_periodicity_statement() {
  Dihedral_periodicity_statementContext *_localctx = _tracker.createInstance<Dihedral_periodicity_statementContext>(_ctx, getState());
  enterRule(_localctx, 48, AmberPTParser::RuleDihedral_periodicity_statement);
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
    setState(402);
    match(AmberPTParser::DIHEDRAL_PERIODICITY);
    setState(403);
    format_function();
    setState(407);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(404);
      match(AmberPTParser::Real);
      setState(409);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(410);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Dihedral_phase_statementContext ------------------------------------------------------------------

AmberPTParser::Dihedral_phase_statementContext::Dihedral_phase_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Dihedral_phase_statementContext::DIHEDRAL_PHASE() {
  return getToken(AmberPTParser::DIHEDRAL_PHASE, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Dihedral_phase_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Dihedral_phase_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Dihedral_phase_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Dihedral_phase_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Dihedral_phase_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Dihedral_phase_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleDihedral_phase_statement;
}


std::any AmberPTParser::Dihedral_phase_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_phase_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Dihedral_phase_statementContext* AmberPTParser::dihedral_phase_statement() {
  Dihedral_phase_statementContext *_localctx = _tracker.createInstance<Dihedral_phase_statementContext>(_ctx, getState());
  enterRule(_localctx, 50, AmberPTParser::RuleDihedral_phase_statement);
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
    setState(412);
    match(AmberPTParser::DIHEDRAL_PHASE);
    setState(413);
    format_function();
    setState(417);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(414);
      match(AmberPTParser::Real);
      setState(419);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(420);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Dihedrals_inc_hydrogen_statementContext ------------------------------------------------------------------

AmberPTParser::Dihedrals_inc_hydrogen_statementContext::Dihedrals_inc_hydrogen_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Dihedrals_inc_hydrogen_statementContext::DIHEDRALS_INC_HYDROGEN() {
  return getToken(AmberPTParser::DIHEDRALS_INC_HYDROGEN, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Dihedrals_inc_hydrogen_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Dihedrals_inc_hydrogen_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Dihedrals_inc_hydrogen_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Dihedrals_inc_hydrogen_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Dihedrals_inc_hydrogen_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Dihedrals_inc_hydrogen_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleDihedrals_inc_hydrogen_statement;
}


std::any AmberPTParser::Dihedrals_inc_hydrogen_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitDihedrals_inc_hydrogen_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Dihedrals_inc_hydrogen_statementContext* AmberPTParser::dihedrals_inc_hydrogen_statement() {
  Dihedrals_inc_hydrogen_statementContext *_localctx = _tracker.createInstance<Dihedrals_inc_hydrogen_statementContext>(_ctx, getState());
  enterRule(_localctx, 52, AmberPTParser::RuleDihedrals_inc_hydrogen_statement);
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
    setState(422);
    match(AmberPTParser::DIHEDRALS_INC_HYDROGEN);
    setState(423);
    format_function();
    setState(427);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(424);
      match(AmberPTParser::Integer);
      setState(429);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(430);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Dihedrals_without_hydrogen_statementContext ------------------------------------------------------------------

AmberPTParser::Dihedrals_without_hydrogen_statementContext::Dihedrals_without_hydrogen_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Dihedrals_without_hydrogen_statementContext::DIHEDRALS_WITHOUT_HYDROGEN() {
  return getToken(AmberPTParser::DIHEDRALS_WITHOUT_HYDROGEN, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Dihedrals_without_hydrogen_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Dihedrals_without_hydrogen_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Dihedrals_without_hydrogen_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Dihedrals_without_hydrogen_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Dihedrals_without_hydrogen_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Dihedrals_without_hydrogen_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleDihedrals_without_hydrogen_statement;
}


std::any AmberPTParser::Dihedrals_without_hydrogen_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitDihedrals_without_hydrogen_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Dihedrals_without_hydrogen_statementContext* AmberPTParser::dihedrals_without_hydrogen_statement() {
  Dihedrals_without_hydrogen_statementContext *_localctx = _tracker.createInstance<Dihedrals_without_hydrogen_statementContext>(_ctx, getState());
  enterRule(_localctx, 54, AmberPTParser::RuleDihedrals_without_hydrogen_statement);
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
    setState(432);
    match(AmberPTParser::DIHEDRALS_WITHOUT_HYDROGEN);
    setState(433);
    format_function();
    setState(437);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(434);
      match(AmberPTParser::Integer);
      setState(439);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(440);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Excluded_atoms_list_statementContext ------------------------------------------------------------------

AmberPTParser::Excluded_atoms_list_statementContext::Excluded_atoms_list_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Excluded_atoms_list_statementContext::EXCLUDED_ATOMS_LIST() {
  return getToken(AmberPTParser::EXCLUDED_ATOMS_LIST, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Excluded_atoms_list_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Excluded_atoms_list_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Excluded_atoms_list_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Excluded_atoms_list_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Excluded_atoms_list_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Excluded_atoms_list_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleExcluded_atoms_list_statement;
}


std::any AmberPTParser::Excluded_atoms_list_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitExcluded_atoms_list_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Excluded_atoms_list_statementContext* AmberPTParser::excluded_atoms_list_statement() {
  Excluded_atoms_list_statementContext *_localctx = _tracker.createInstance<Excluded_atoms_list_statementContext>(_ctx, getState());
  enterRule(_localctx, 56, AmberPTParser::RuleExcluded_atoms_list_statement);
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
    setState(442);
    match(AmberPTParser::EXCLUDED_ATOMS_LIST);
    setState(443);
    format_function();
    setState(447);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(444);
      match(AmberPTParser::Integer);
      setState(449);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(450);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Hbcut_statementContext ------------------------------------------------------------------

AmberPTParser::Hbcut_statementContext::Hbcut_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Hbcut_statementContext::HBCUT() {
  return getToken(AmberPTParser::HBCUT, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Hbcut_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Hbcut_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Hbcut_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Hbcut_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Hbcut_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Hbcut_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleHbcut_statement;
}


std::any AmberPTParser::Hbcut_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitHbcut_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Hbcut_statementContext* AmberPTParser::hbcut_statement() {
  Hbcut_statementContext *_localctx = _tracker.createInstance<Hbcut_statementContext>(_ctx, getState());
  enterRule(_localctx, 58, AmberPTParser::RuleHbcut_statement);
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
    setState(452);
    match(AmberPTParser::HBCUT);
    setState(453);
    format_function();
    setState(457);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(454);
      match(AmberPTParser::Real);
      setState(459);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(460);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Hbond_acoef_statementContext ------------------------------------------------------------------

AmberPTParser::Hbond_acoef_statementContext::Hbond_acoef_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Hbond_acoef_statementContext::HBOND_ACOEF() {
  return getToken(AmberPTParser::HBOND_ACOEF, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Hbond_acoef_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Hbond_acoef_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Hbond_acoef_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Hbond_acoef_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Hbond_acoef_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Hbond_acoef_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleHbond_acoef_statement;
}


std::any AmberPTParser::Hbond_acoef_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitHbond_acoef_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Hbond_acoef_statementContext* AmberPTParser::hbond_acoef_statement() {
  Hbond_acoef_statementContext *_localctx = _tracker.createInstance<Hbond_acoef_statementContext>(_ctx, getState());
  enterRule(_localctx, 60, AmberPTParser::RuleHbond_acoef_statement);
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
    setState(462);
    match(AmberPTParser::HBOND_ACOEF);
    setState(463);
    format_function();
    setState(467);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(464);
      match(AmberPTParser::Real);
      setState(469);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(470);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Hbond_bcoef_statementContext ------------------------------------------------------------------

AmberPTParser::Hbond_bcoef_statementContext::Hbond_bcoef_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Hbond_bcoef_statementContext::HBOND_BCOEF() {
  return getToken(AmberPTParser::HBOND_BCOEF, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Hbond_bcoef_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Hbond_bcoef_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Hbond_bcoef_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Hbond_bcoef_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Hbond_bcoef_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Hbond_bcoef_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleHbond_bcoef_statement;
}


std::any AmberPTParser::Hbond_bcoef_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitHbond_bcoef_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Hbond_bcoef_statementContext* AmberPTParser::hbond_bcoef_statement() {
  Hbond_bcoef_statementContext *_localctx = _tracker.createInstance<Hbond_bcoef_statementContext>(_ctx, getState());
  enterRule(_localctx, 62, AmberPTParser::RuleHbond_bcoef_statement);
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
    match(AmberPTParser::HBOND_BCOEF);
    setState(473);
    format_function();
    setState(477);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(474);
      match(AmberPTParser::Real);
      setState(479);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(480);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Ipol_statementContext ------------------------------------------------------------------

AmberPTParser::Ipol_statementContext::Ipol_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Ipol_statementContext::IPOL() {
  return getToken(AmberPTParser::IPOL, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Ipol_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Ipol_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Ipol_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Ipol_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Ipol_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Ipol_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleIpol_statement;
}


std::any AmberPTParser::Ipol_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitIpol_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Ipol_statementContext* AmberPTParser::ipol_statement() {
  Ipol_statementContext *_localctx = _tracker.createInstance<Ipol_statementContext>(_ctx, getState());
  enterRule(_localctx, 64, AmberPTParser::RuleIpol_statement);
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
    setState(482);
    match(AmberPTParser::IPOL);
    setState(483);
    format_function();
    setState(487);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(484);
      match(AmberPTParser::Integer);
      setState(489);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(490);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Irotat_statementContext ------------------------------------------------------------------

AmberPTParser::Irotat_statementContext::Irotat_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Irotat_statementContext::IROTAT() {
  return getToken(AmberPTParser::IROTAT, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Irotat_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Irotat_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Irotat_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Irotat_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Irotat_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Irotat_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleIrotat_statement;
}


std::any AmberPTParser::Irotat_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitIrotat_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Irotat_statementContext* AmberPTParser::irotat_statement() {
  Irotat_statementContext *_localctx = _tracker.createInstance<Irotat_statementContext>(_ctx, getState());
  enterRule(_localctx, 66, AmberPTParser::RuleIrotat_statement);
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
    match(AmberPTParser::IROTAT);
    setState(493);
    format_function();
    setState(497);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(494);
      match(AmberPTParser::Integer);
      setState(499);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(500);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Join_array_statementContext ------------------------------------------------------------------

AmberPTParser::Join_array_statementContext::Join_array_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Join_array_statementContext::JOIN_ARRAY() {
  return getToken(AmberPTParser::JOIN_ARRAY, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Join_array_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Join_array_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Join_array_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Join_array_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Join_array_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Join_array_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleJoin_array_statement;
}


std::any AmberPTParser::Join_array_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitJoin_array_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Join_array_statementContext* AmberPTParser::join_array_statement() {
  Join_array_statementContext *_localctx = _tracker.createInstance<Join_array_statementContext>(_ctx, getState());
  enterRule(_localctx, 68, AmberPTParser::RuleJoin_array_statement);
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
    setState(502);
    match(AmberPTParser::JOIN_ARRAY);
    setState(503);
    format_function();
    setState(507);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(504);
      match(AmberPTParser::Integer);
      setState(509);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(510);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Lennard_jones_acoef_statementContext ------------------------------------------------------------------

AmberPTParser::Lennard_jones_acoef_statementContext::Lennard_jones_acoef_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Lennard_jones_acoef_statementContext::LENNARD_JONES_ACOEF() {
  return getToken(AmberPTParser::LENNARD_JONES_ACOEF, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Lennard_jones_acoef_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Lennard_jones_acoef_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Lennard_jones_acoef_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Lennard_jones_acoef_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Lennard_jones_acoef_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Lennard_jones_acoef_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleLennard_jones_acoef_statement;
}


std::any AmberPTParser::Lennard_jones_acoef_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitLennard_jones_acoef_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Lennard_jones_acoef_statementContext* AmberPTParser::lennard_jones_acoef_statement() {
  Lennard_jones_acoef_statementContext *_localctx = _tracker.createInstance<Lennard_jones_acoef_statementContext>(_ctx, getState());
  enterRule(_localctx, 70, AmberPTParser::RuleLennard_jones_acoef_statement);
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
    setState(512);
    match(AmberPTParser::LENNARD_JONES_ACOEF);
    setState(513);
    format_function();
    setState(517);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(514);
      match(AmberPTParser::Real);
      setState(519);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(520);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Lennard_jones_bcoef_statementContext ------------------------------------------------------------------

AmberPTParser::Lennard_jones_bcoef_statementContext::Lennard_jones_bcoef_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Lennard_jones_bcoef_statementContext::LENNARD_JONES_BCOEF() {
  return getToken(AmberPTParser::LENNARD_JONES_BCOEF, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Lennard_jones_bcoef_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Lennard_jones_bcoef_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Lennard_jones_bcoef_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Lennard_jones_bcoef_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Lennard_jones_bcoef_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Lennard_jones_bcoef_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleLennard_jones_bcoef_statement;
}


std::any AmberPTParser::Lennard_jones_bcoef_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitLennard_jones_bcoef_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Lennard_jones_bcoef_statementContext* AmberPTParser::lennard_jones_bcoef_statement() {
  Lennard_jones_bcoef_statementContext *_localctx = _tracker.createInstance<Lennard_jones_bcoef_statementContext>(_ctx, getState());
  enterRule(_localctx, 72, AmberPTParser::RuleLennard_jones_bcoef_statement);
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
    setState(522);
    match(AmberPTParser::LENNARD_JONES_BCOEF);
    setState(523);
    format_function();
    setState(527);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(524);
      match(AmberPTParser::Real);
      setState(529);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(530);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Mass_statementContext ------------------------------------------------------------------

AmberPTParser::Mass_statementContext::Mass_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Mass_statementContext::MASS() {
  return getToken(AmberPTParser::MASS, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Mass_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Mass_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Mass_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Mass_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Mass_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Mass_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleMass_statement;
}


std::any AmberPTParser::Mass_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitMass_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Mass_statementContext* AmberPTParser::mass_statement() {
  Mass_statementContext *_localctx = _tracker.createInstance<Mass_statementContext>(_ctx, getState());
  enterRule(_localctx, 74, AmberPTParser::RuleMass_statement);
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
    setState(532);
    match(AmberPTParser::MASS);
    setState(533);
    format_function();
    setState(537);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(534);
      match(AmberPTParser::Real);
      setState(539);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(540);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Nonbonded_parm_index_statementContext ------------------------------------------------------------------

AmberPTParser::Nonbonded_parm_index_statementContext::Nonbonded_parm_index_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Nonbonded_parm_index_statementContext::NONBONDED_PARM_INDEX() {
  return getToken(AmberPTParser::NONBONDED_PARM_INDEX, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Nonbonded_parm_index_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Nonbonded_parm_index_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Nonbonded_parm_index_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Nonbonded_parm_index_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Nonbonded_parm_index_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Nonbonded_parm_index_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleNonbonded_parm_index_statement;
}


std::any AmberPTParser::Nonbonded_parm_index_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitNonbonded_parm_index_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Nonbonded_parm_index_statementContext* AmberPTParser::nonbonded_parm_index_statement() {
  Nonbonded_parm_index_statementContext *_localctx = _tracker.createInstance<Nonbonded_parm_index_statementContext>(_ctx, getState());
  enterRule(_localctx, 76, AmberPTParser::RuleNonbonded_parm_index_statement);
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
    setState(542);
    match(AmberPTParser::NONBONDED_PARM_INDEX);
    setState(543);
    format_function();
    setState(547);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(544);
      match(AmberPTParser::Integer);
      setState(549);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(550);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Number_excluded_atoms_statementContext ------------------------------------------------------------------

AmberPTParser::Number_excluded_atoms_statementContext::Number_excluded_atoms_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Number_excluded_atoms_statementContext::NUMBER_EXCLUDED_ATOMS() {
  return getToken(AmberPTParser::NUMBER_EXCLUDED_ATOMS, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Number_excluded_atoms_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Number_excluded_atoms_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Number_excluded_atoms_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Number_excluded_atoms_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Number_excluded_atoms_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Number_excluded_atoms_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleNumber_excluded_atoms_statement;
}


std::any AmberPTParser::Number_excluded_atoms_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitNumber_excluded_atoms_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Number_excluded_atoms_statementContext* AmberPTParser::number_excluded_atoms_statement() {
  Number_excluded_atoms_statementContext *_localctx = _tracker.createInstance<Number_excluded_atoms_statementContext>(_ctx, getState());
  enterRule(_localctx, 78, AmberPTParser::RuleNumber_excluded_atoms_statement);
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
    setState(552);
    match(AmberPTParser::NUMBER_EXCLUDED_ATOMS);
    setState(553);
    format_function();
    setState(557);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(554);
      match(AmberPTParser::Integer);
      setState(559);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(560);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Pointers_statementContext ------------------------------------------------------------------

AmberPTParser::Pointers_statementContext::Pointers_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Pointers_statementContext::POINTERS() {
  return getToken(AmberPTParser::POINTERS, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Pointers_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Pointers_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Pointers_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Pointers_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Pointers_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Pointers_statementContext::getRuleIndex() const {
  return AmberPTParser::RulePointers_statement;
}


std::any AmberPTParser::Pointers_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitPointers_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Pointers_statementContext* AmberPTParser::pointers_statement() {
  Pointers_statementContext *_localctx = _tracker.createInstance<Pointers_statementContext>(_ctx, getState());
  enterRule(_localctx, 80, AmberPTParser::RulePointers_statement);
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
    setState(562);
    match(AmberPTParser::POINTERS);
    setState(563);
    format_function();
    setState(567);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(564);
      match(AmberPTParser::Integer);
      setState(569);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(570);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Polarizability_statementContext ------------------------------------------------------------------

AmberPTParser::Polarizability_statementContext::Polarizability_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Polarizability_statementContext::POLARIZABILITY() {
  return getToken(AmberPTParser::POLARIZABILITY, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Polarizability_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Polarizability_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Polarizability_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Polarizability_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Polarizability_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Polarizability_statementContext::getRuleIndex() const {
  return AmberPTParser::RulePolarizability_statement;
}


std::any AmberPTParser::Polarizability_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitPolarizability_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Polarizability_statementContext* AmberPTParser::polarizability_statement() {
  Polarizability_statementContext *_localctx = _tracker.createInstance<Polarizability_statementContext>(_ctx, getState());
  enterRule(_localctx, 82, AmberPTParser::RulePolarizability_statement);
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
    setState(572);
    match(AmberPTParser::POLARIZABILITY);
    setState(573);
    format_function();
    setState(577);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(574);
      match(AmberPTParser::Real);
      setState(579);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(580);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Radii_statementContext ------------------------------------------------------------------

AmberPTParser::Radii_statementContext::Radii_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Radii_statementContext::RADII() {
  return getToken(AmberPTParser::RADII, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Radii_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Radii_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Radii_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Radii_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Radii_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Radii_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleRadii_statement;
}


std::any AmberPTParser::Radii_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitRadii_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Radii_statementContext* AmberPTParser::radii_statement() {
  Radii_statementContext *_localctx = _tracker.createInstance<Radii_statementContext>(_ctx, getState());
  enterRule(_localctx, 84, AmberPTParser::RuleRadii_statement);
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
    setState(582);
    match(AmberPTParser::RADII);
    setState(583);
    format_function();
    setState(587);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(584);
      match(AmberPTParser::Real);
      setState(589);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(590);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Radius_set_statementContext ------------------------------------------------------------------

AmberPTParser::Radius_set_statementContext::Radius_set_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Radius_set_statementContext::RADIUS_SET() {
  return getToken(AmberPTParser::RADIUS_SET, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Radius_set_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Radius_set_statementContext::FLAG_AA() {
  return getToken(AmberPTParser::FLAG_AA, 0);
}

tree::TerminalNode* AmberPTParser::Radius_set_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Radius_set_statementContext::Simple_name() {
  return getTokens(AmberPTParser::Simple_name);
}

tree::TerminalNode* AmberPTParser::Radius_set_statementContext::Simple_name(size_t i) {
  return getToken(AmberPTParser::Simple_name, i);
}


size_t AmberPTParser::Radius_set_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleRadius_set_statement;
}


std::any AmberPTParser::Radius_set_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitRadius_set_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Radius_set_statementContext* AmberPTParser::radius_set_statement() {
  Radius_set_statementContext *_localctx = _tracker.createInstance<Radius_set_statementContext>(_ctx, getState());
  enterRule(_localctx, 86, AmberPTParser::RuleRadius_set_statement);
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
    setState(592);
    match(AmberPTParser::RADIUS_SET);
    setState(593);
    format_function();
    setState(597);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Simple_name) {
      setState(594);
      match(AmberPTParser::Simple_name);
      setState(599);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(600);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_AA)) {
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

//----------------- Residue_label_statementContext ------------------------------------------------------------------

AmberPTParser::Residue_label_statementContext::Residue_label_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Residue_label_statementContext::RESIDUE_LABEL() {
  return getToken(AmberPTParser::RESIDUE_LABEL, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Residue_label_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Residue_label_statementContext::FLAG_AA() {
  return getToken(AmberPTParser::FLAG_AA, 0);
}

tree::TerminalNode* AmberPTParser::Residue_label_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Residue_label_statementContext::Simple_name() {
  return getTokens(AmberPTParser::Simple_name);
}

tree::TerminalNode* AmberPTParser::Residue_label_statementContext::Simple_name(size_t i) {
  return getToken(AmberPTParser::Simple_name, i);
}


size_t AmberPTParser::Residue_label_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleResidue_label_statement;
}


std::any AmberPTParser::Residue_label_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitResidue_label_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Residue_label_statementContext* AmberPTParser::residue_label_statement() {
  Residue_label_statementContext *_localctx = _tracker.createInstance<Residue_label_statementContext>(_ctx, getState());
  enterRule(_localctx, 88, AmberPTParser::RuleResidue_label_statement);
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
    setState(602);
    match(AmberPTParser::RESIDUE_LABEL);
    setState(603);
    format_function();
    setState(607);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Simple_name) {
      setState(604);
      match(AmberPTParser::Simple_name);
      setState(609);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(610);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_AA)) {
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

//----------------- Residue_pointer_statementContext ------------------------------------------------------------------

AmberPTParser::Residue_pointer_statementContext::Residue_pointer_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Residue_pointer_statementContext::RESIDUE_POINTER() {
  return getToken(AmberPTParser::RESIDUE_POINTER, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Residue_pointer_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Residue_pointer_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Residue_pointer_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Residue_pointer_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Residue_pointer_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Residue_pointer_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleResidue_pointer_statement;
}


std::any AmberPTParser::Residue_pointer_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitResidue_pointer_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Residue_pointer_statementContext* AmberPTParser::residue_pointer_statement() {
  Residue_pointer_statementContext *_localctx = _tracker.createInstance<Residue_pointer_statementContext>(_ctx, getState());
  enterRule(_localctx, 90, AmberPTParser::RuleResidue_pointer_statement);
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
    setState(612);
    match(AmberPTParser::RESIDUE_POINTER);
    setState(613);
    format_function();
    setState(615); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(614);
      match(AmberPTParser::Integer);
      setState(617); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == AmberPTParser::Integer);
    setState(619);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Scee_scale_factor_statementContext ------------------------------------------------------------------

AmberPTParser::Scee_scale_factor_statementContext::Scee_scale_factor_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Scee_scale_factor_statementContext::SCEE_SCALE_FACTOR() {
  return getToken(AmberPTParser::SCEE_SCALE_FACTOR, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Scee_scale_factor_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Scee_scale_factor_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Scee_scale_factor_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Scee_scale_factor_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Scee_scale_factor_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Scee_scale_factor_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleScee_scale_factor_statement;
}


std::any AmberPTParser::Scee_scale_factor_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitScee_scale_factor_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Scee_scale_factor_statementContext* AmberPTParser::scee_scale_factor_statement() {
  Scee_scale_factor_statementContext *_localctx = _tracker.createInstance<Scee_scale_factor_statementContext>(_ctx, getState());
  enterRule(_localctx, 92, AmberPTParser::RuleScee_scale_factor_statement);
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
    setState(621);
    match(AmberPTParser::SCEE_SCALE_FACTOR);
    setState(622);
    format_function();
    setState(626);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(623);
      match(AmberPTParser::Real);
      setState(628);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(629);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Scnb_scale_factor_statementContext ------------------------------------------------------------------

AmberPTParser::Scnb_scale_factor_statementContext::Scnb_scale_factor_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Scnb_scale_factor_statementContext::SCNB_SCALE_FACTOR() {
  return getToken(AmberPTParser::SCNB_SCALE_FACTOR, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Scnb_scale_factor_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Scnb_scale_factor_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Scnb_scale_factor_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Scnb_scale_factor_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Scnb_scale_factor_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Scnb_scale_factor_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleScnb_scale_factor_statement;
}


std::any AmberPTParser::Scnb_scale_factor_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitScnb_scale_factor_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Scnb_scale_factor_statementContext* AmberPTParser::scnb_scale_factor_statement() {
  Scnb_scale_factor_statementContext *_localctx = _tracker.createInstance<Scnb_scale_factor_statementContext>(_ctx, getState());
  enterRule(_localctx, 94, AmberPTParser::RuleScnb_scale_factor_statement);
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
    setState(631);
    match(AmberPTParser::SCNB_SCALE_FACTOR);
    setState(632);
    format_function();
    setState(636);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(633);
      match(AmberPTParser::Real);
      setState(638);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(639);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Screen_statementContext ------------------------------------------------------------------

AmberPTParser::Screen_statementContext::Screen_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Screen_statementContext::SCREEN() {
  return getToken(AmberPTParser::SCREEN, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Screen_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Screen_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Screen_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Screen_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Screen_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Screen_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleScreen_statement;
}


std::any AmberPTParser::Screen_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitScreen_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Screen_statementContext* AmberPTParser::screen_statement() {
  Screen_statementContext *_localctx = _tracker.createInstance<Screen_statementContext>(_ctx, getState());
  enterRule(_localctx, 96, AmberPTParser::RuleScreen_statement);
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
    setState(641);
    match(AmberPTParser::SCREEN);
    setState(642);
    format_function();
    setState(646);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(643);
      match(AmberPTParser::Real);
      setState(648);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(649);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Solty_statementContext ------------------------------------------------------------------

AmberPTParser::Solty_statementContext::Solty_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Solty_statementContext::SOLTY() {
  return getToken(AmberPTParser::SOLTY, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Solty_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Solty_statementContext::FLAG_EA() {
  return getToken(AmberPTParser::FLAG_EA, 0);
}

tree::TerminalNode* AmberPTParser::Solty_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Solty_statementContext::Real() {
  return getTokens(AmberPTParser::Real);
}

tree::TerminalNode* AmberPTParser::Solty_statementContext::Real(size_t i) {
  return getToken(AmberPTParser::Real, i);
}


size_t AmberPTParser::Solty_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleSolty_statement;
}


std::any AmberPTParser::Solty_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitSolty_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Solty_statementContext* AmberPTParser::solty_statement() {
  Solty_statementContext *_localctx = _tracker.createInstance<Solty_statementContext>(_ctx, getState());
  enterRule(_localctx, 98, AmberPTParser::RuleSolty_statement);
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
    setState(651);
    match(AmberPTParser::SOLTY);
    setState(652);
    format_function();
    setState(656);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Real) {
      setState(653);
      match(AmberPTParser::Real);
      setState(658);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(659);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_EA)) {
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

//----------------- Solvent_pointers_statementContext ------------------------------------------------------------------

AmberPTParser::Solvent_pointers_statementContext::Solvent_pointers_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Solvent_pointers_statementContext::SOLVENT_POINTERS() {
  return getToken(AmberPTParser::SOLVENT_POINTERS, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Solvent_pointers_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Solvent_pointers_statementContext::FLAG_IA() {
  return getToken(AmberPTParser::FLAG_IA, 0);
}

tree::TerminalNode* AmberPTParser::Solvent_pointers_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Solvent_pointers_statementContext::Integer() {
  return getTokens(AmberPTParser::Integer);
}

tree::TerminalNode* AmberPTParser::Solvent_pointers_statementContext::Integer(size_t i) {
  return getToken(AmberPTParser::Integer, i);
}


size_t AmberPTParser::Solvent_pointers_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleSolvent_pointers_statement;
}


std::any AmberPTParser::Solvent_pointers_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitSolvent_pointers_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Solvent_pointers_statementContext* AmberPTParser::solvent_pointers_statement() {
  Solvent_pointers_statementContext *_localctx = _tracker.createInstance<Solvent_pointers_statementContext>(_ctx, getState());
  enterRule(_localctx, 100, AmberPTParser::RuleSolvent_pointers_statement);
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
    setState(661);
    match(AmberPTParser::SOLVENT_POINTERS);
    setState(662);
    format_function();
    setState(666);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Integer) {
      setState(663);
      match(AmberPTParser::Integer);
      setState(668);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(669);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_IA)) {
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

//----------------- Title_statementContext ------------------------------------------------------------------

AmberPTParser::Title_statementContext::Title_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Title_statementContext::TITLE() {
  return getToken(AmberPTParser::TITLE, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Title_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Title_statementContext::FLAG_AA() {
  return getToken(AmberPTParser::FLAG_AA, 0);
}

tree::TerminalNode* AmberPTParser::Title_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Title_statementContext::Simple_name() {
  return getTokens(AmberPTParser::Simple_name);
}

tree::TerminalNode* AmberPTParser::Title_statementContext::Simple_name(size_t i) {
  return getToken(AmberPTParser::Simple_name, i);
}


size_t AmberPTParser::Title_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleTitle_statement;
}


std::any AmberPTParser::Title_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitTitle_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Title_statementContext* AmberPTParser::title_statement() {
  Title_statementContext *_localctx = _tracker.createInstance<Title_statementContext>(_ctx, getState());
  enterRule(_localctx, 102, AmberPTParser::RuleTitle_statement);
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
    setState(671);
    match(AmberPTParser::TITLE);
    setState(672);
    format_function();
    setState(676);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Simple_name) {
      setState(673);
      match(AmberPTParser::Simple_name);
      setState(678);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(679);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_AA)) {
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

//----------------- Tree_chain_classification_statementContext ------------------------------------------------------------------

AmberPTParser::Tree_chain_classification_statementContext::Tree_chain_classification_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Tree_chain_classification_statementContext::TREE_CHAIN_CLASSIFICATION() {
  return getToken(AmberPTParser::TREE_CHAIN_CLASSIFICATION, 0);
}

AmberPTParser::Format_functionContext* AmberPTParser::Tree_chain_classification_statementContext::format_function() {
  return getRuleContext<AmberPTParser::Format_functionContext>(0);
}

tree::TerminalNode* AmberPTParser::Tree_chain_classification_statementContext::FLAG_AA() {
  return getToken(AmberPTParser::FLAG_AA, 0);
}

tree::TerminalNode* AmberPTParser::Tree_chain_classification_statementContext::EOF() {
  return getToken(AmberPTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> AmberPTParser::Tree_chain_classification_statementContext::Simple_name() {
  return getTokens(AmberPTParser::Simple_name);
}

tree::TerminalNode* AmberPTParser::Tree_chain_classification_statementContext::Simple_name(size_t i) {
  return getToken(AmberPTParser::Simple_name, i);
}


size_t AmberPTParser::Tree_chain_classification_statementContext::getRuleIndex() const {
  return AmberPTParser::RuleTree_chain_classification_statement;
}


std::any AmberPTParser::Tree_chain_classification_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitTree_chain_classification_statement(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Tree_chain_classification_statementContext* AmberPTParser::tree_chain_classification_statement() {
  Tree_chain_classification_statementContext *_localctx = _tracker.createInstance<Tree_chain_classification_statementContext>(_ctx, getState());
  enterRule(_localctx, 104, AmberPTParser::RuleTree_chain_classification_statement);
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
    setState(681);
    match(AmberPTParser::TREE_CHAIN_CLASSIFICATION);
    setState(682);
    format_function();
    setState(686);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == AmberPTParser::Simple_name) {
      setState(683);
      match(AmberPTParser::Simple_name);
      setState(688);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(689);
    _la = _input->LA(1);
    if (!(_la == AmberPTParser::EOF || _la == AmberPTParser::FLAG_AA)) {
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

//----------------- Format_functionContext ------------------------------------------------------------------

AmberPTParser::Format_functionContext::Format_functionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AmberPTParser::Format_functionContext::FORMAT() {
  return getToken(AmberPTParser::FORMAT, 0);
}

tree::TerminalNode* AmberPTParser::Format_functionContext::Fortran_format_A() {
  return getToken(AmberPTParser::Fortran_format_A, 0);
}

tree::TerminalNode* AmberPTParser::Format_functionContext::Fortran_format_I() {
  return getToken(AmberPTParser::Fortran_format_I, 0);
}

tree::TerminalNode* AmberPTParser::Format_functionContext::Fortran_format_E() {
  return getToken(AmberPTParser::Fortran_format_E, 0);
}


size_t AmberPTParser::Format_functionContext::getRuleIndex() const {
  return AmberPTParser::RuleFormat_function;
}


std::any AmberPTParser::Format_functionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AmberPTParserVisitor*>(visitor))
    return parserVisitor->visitFormat_function(this);
  else
    return visitor->visitChildren(this);
}

AmberPTParser::Format_functionContext* AmberPTParser::format_function() {
  Format_functionContext *_localctx = _tracker.createInstance<Format_functionContext>(_ctx, getState());
  enterRule(_localctx, 106, AmberPTParser::RuleFormat_function);
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
    setState(691);
    match(AmberPTParser::FORMAT);
    setState(692);
    _la = _input->LA(1);
    if (!(((((_la - 80) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 80)) & 7) != 0))) {
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

void AmberPTParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  amberptparserParserInitialize();
#else
  ::antlr4::internal::call_once(amberptparserParserOnceFlag, amberptparserParserInitialize);
#endif
}
