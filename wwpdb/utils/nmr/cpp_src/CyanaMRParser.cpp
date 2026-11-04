
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaMRParser.g4 by ANTLR 4.13.2


#include "CyanaMRParserVisitor.h"

#include "CyanaMRParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct CyanaMRParserStaticData final {
  CyanaMRParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  CyanaMRParserStaticData(const CyanaMRParserStaticData&) = delete;
  CyanaMRParserStaticData(CyanaMRParserStaticData&&) = delete;
  CyanaMRParserStaticData& operator=(const CyanaMRParserStaticData&) = delete;
  CyanaMRParserStaticData& operator=(CyanaMRParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag cyanamrparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<CyanaMRParserStaticData> cyanamrparserParserStaticData = nullptr;

void cyanamrparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (cyanamrparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(cyanamrparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<CyanaMRParserStaticData>(
    std::vector<std::string>{
      "cyana_mr", "comment", "distance_restraints", "distance_restraint", 
      "torsion_angle_restraints", "torsion_angle_restraint", "rdc_restraints", 
      "rdc_parameter", "rdc_restraint", "pcs_restraints", "pcs_parameter", 
      "pcs_restraint", "fixres_distance_restraints", "fixres_distance_restraint", 
      "fixresw_distance_restraints", "fixresw_distance_restraint", "fixresw2_distance_restraints", 
      "fixresw2_distance_restraint", "fixatm_distance_restraints", "fixatm_distance_restraint", 
      "fixatmw_distance_restraints", "fixatmw_distance_restraint", "fixatmw2_distance_restraints", 
      "fixatmw2_distance_restraint", "diana_distance_restraints", "diana_distance_restraint", 
      "diana_ssbond_restraints", "diana_ssbond_restraint", "diana_hbond_restraints", 
      "diana_hbond_restraint", "diana_torsion_angle_restraints", "diana_torsion_angle_restraint", 
      "diana_coupling_constant_restraints", "diana_coupling_constant_restraint", 
      "diana_stereoassign_macro", "diana_chemical_shifts", "diana_chemical_shift", 
      "distance_w_chain_restraints", "distance_w_chain_restraint", "distance_w_chain2_restraints", 
      "distance_w_chain2_restraint", "distance_w_chain3_restraints", "distance_w_chain3_restraint", 
      "torsion_angle_w_chain_restraints", "torsion_angle_w_chain_restraint", 
      "cco_restraints", "cco_restraint", "ssbond_macro", "hbond_macro", 
      "link_statement", "stereoassign_macro", "declare_variable", "set_variable", 
      "unset_variable", "print_macro", "unambig_atom_name_mapping", "mapping_list", 
      "ambig_atom_name_mapping", "ambig_list", "number", "gen_res_num", 
      "gen_simple_name", "gen_atom_name"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "", "'NOEUPP'", "'NOELOW'", "'NOEUPLO'", 
      "'HBUPP'", "'HBLOW'", "'SSUPP'", "'SSLOW'", "'JCOUPL'", "'ANGLE'", 
      "'STEREO'", "'SHIFTS'", "'TYPE'", "", "'OR'", "'SSBOND'", "", "'HBOND'", 
      "'LINK'", "", "'VAR'", "'UNSET'", "", "'PRINT'", "'RESIDUE'", "'MAPPING'", 
      "'AMBIG'", "", "", "", "", "", "", "", "", "", "", "'ATOM1'", "'ATOM2'", 
      "'RESIDUE1'", "'RESIDUE2'", "", "'ATOM1='", "'ATOM2='", "'RESIDUE1='", 
      "'RESIDUE2='"
    },
    std::vector<std::string>{
      "", "Ambig_code", "Integer", "Float", "Float_DecimalComma", "Orientation_header", 
      "Tensor_header", "SMCLN_COMMENT", "COMMENT", "NoeUpp", "NoeLow", "NoeUpLo", 
      "HBUpp", "HBLow", "SSUpp", "SSLow", "Jcoupl", "Angle", "Stereo", "Shifts", 
      "Type", "Equ_op", "Or", "Ssbond", "Ssbond_resids", "Hbond", "Link", 
      "Atom_stereo", "Var", "Unset", "SetVar", "Print", "Residue", "Mapping", 
      "Ambig", "Capital_integer", "Integer_capital", "Simple_name", "SPACE", 
      "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT", "Any_name", 
      "SPACE_CM", "RETURN_CM", "Atom1", "Atom2", "Residue1", "Residue2", 
      "Equ_op_HB", "Atom1_equ", "Atom2_equ", "Residue1_equ", "Residue2_equ", 
      "Concat_atom_1", "Concat_atom_2", "Concat_res_1", "Concat_res_2", 
      "Integer_HB", "Simple_name_HB", "SPACE_HB", "RETURN_HB", "LINE_COMMENT_HB", 
      "Double_quote_string", "SPACE_PR", "RETURN_PR", "LINE_COMMENT_PR", 
      "Simple_name_VA", "SPACE_VA", "RETURN_VA", "LINE_COMMENT_VA", "Ambig_code_MP", 
      "Integer_MP", "Simple_name_MP", "Equ_op_MP", "SPACE_MP", "RETURN_MP", 
      "LINE_COMMENT_MP"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,77,848,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,
  	35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,
  	42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,
  	49,2,50,7,50,2,51,7,51,2,52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,
  	56,2,57,7,57,2,58,7,58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,1,0,1,
  	0,4,0,129,8,0,11,0,12,0,130,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
  	0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
  	1,0,1,0,1,0,1,0,1,0,5,0,166,8,0,10,0,12,0,169,9,0,1,0,1,0,1,1,1,1,5,1,
  	175,8,1,10,1,12,1,178,9,1,1,1,1,1,1,2,4,2,183,8,2,11,2,12,2,184,1,3,1,
  	3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,195,8,3,1,3,3,3,198,8,3,1,3,3,3,201,8,3,
  	1,3,3,3,204,8,3,1,3,3,3,207,8,3,1,4,4,4,210,8,4,11,4,12,4,211,1,5,1,5,
  	1,5,1,5,1,5,1,5,3,5,220,8,5,1,5,1,5,1,5,3,5,225,8,5,1,5,3,5,228,8,5,1,
  	6,4,6,231,8,6,11,6,12,6,232,1,6,1,6,1,6,4,6,238,8,6,11,6,12,6,239,1,7,
  	1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,258,8,
  	8,1,9,4,9,261,8,9,11,9,12,9,262,1,9,1,9,1,9,4,9,268,8,9,11,9,12,9,269,
  	1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,
  	4,12,286,8,12,11,12,12,12,287,1,13,1,13,1,13,3,13,293,8,13,1,13,1,13,
  	1,13,1,13,1,13,1,13,1,13,4,13,302,8,13,11,13,12,13,303,1,14,4,14,307,
  	8,14,11,14,12,14,308,1,15,1,15,1,15,3,15,314,8,15,1,15,1,15,1,15,1,15,
  	1,15,1,15,1,15,1,15,4,15,324,8,15,11,15,12,15,325,1,16,4,16,329,8,16,
  	11,16,12,16,330,1,17,1,17,1,17,3,17,336,8,17,1,17,1,17,1,17,1,17,1,17,
  	1,17,1,17,1,17,1,17,4,17,347,8,17,11,17,12,17,348,1,18,4,18,352,8,18,
  	11,18,12,18,353,1,19,1,19,1,19,1,19,3,19,360,8,19,1,19,1,19,1,19,1,19,
  	1,19,1,19,4,19,368,8,19,11,19,12,19,369,1,20,4,20,373,8,20,11,20,12,20,
  	374,1,21,1,21,1,21,1,21,3,21,381,8,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
  	21,4,21,390,8,21,11,21,12,21,391,1,22,4,22,395,8,22,11,22,12,22,396,1,
  	23,1,23,1,23,1,23,3,23,403,8,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
  	23,4,23,413,8,23,11,23,12,23,414,1,24,4,24,418,8,24,11,24,12,24,419,1,
  	25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,431,8,25,1,25,1,25,1,
  	25,1,25,1,25,1,25,3,25,439,8,25,1,25,3,25,442,8,25,1,25,3,25,445,8,25,
  	1,26,4,26,448,8,26,11,26,12,26,449,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
  	1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,466,8,27,1,27,3,27,469,8,27,1,
  	27,3,27,472,8,27,1,28,4,28,475,8,28,11,28,12,28,476,1,29,1,29,1,29,1,
  	29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,493,8,29,1,
  	29,3,29,496,8,29,1,29,3,29,499,8,29,1,30,4,30,502,8,30,11,30,12,30,503,
  	1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,516,8,31,1,31,
  	3,31,519,8,31,1,31,3,31,522,8,31,1,32,4,32,525,8,32,11,32,12,32,526,1,
  	33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,536,8,33,1,33,1,33,1,33,1,33,3,
  	33,542,8,33,3,33,544,8,33,1,33,3,33,547,8,33,1,33,3,33,550,8,33,1,34,
  	1,34,1,34,1,34,4,34,556,8,34,11,34,12,34,557,1,34,3,34,561,8,34,1,35,
  	4,35,564,8,35,11,35,12,35,565,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,
  	5,36,576,8,36,10,36,12,36,579,9,36,1,36,3,36,582,8,36,1,36,3,36,585,8,
  	36,1,37,4,37,588,8,37,11,37,12,37,589,1,38,1,38,1,38,1,38,1,38,1,38,1,
  	38,1,38,1,38,1,38,3,38,602,8,38,1,38,3,38,605,8,38,1,38,3,38,608,8,38,
  	1,38,3,38,611,8,38,1,38,3,38,614,8,38,1,39,4,39,617,8,39,11,39,12,39,
  	618,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,631,8,40,1,
  	40,3,40,634,8,40,1,40,3,40,637,8,40,1,40,3,40,640,8,40,1,40,3,40,643,
  	8,40,1,41,4,41,646,8,41,11,41,12,41,647,1,42,1,42,1,42,1,42,1,42,1,42,
  	1,42,1,42,1,42,1,42,3,42,660,8,42,1,42,3,42,663,8,42,1,42,3,42,666,8,
  	42,1,42,3,42,669,8,42,1,42,3,42,672,8,42,1,43,4,43,675,8,43,11,43,12,
  	43,676,1,44,1,44,1,44,1,44,1,44,1,44,1,44,3,44,686,8,44,1,44,1,44,1,44,
  	3,44,691,8,44,1,44,3,44,694,8,44,1,45,4,45,697,8,45,11,45,12,45,698,1,
  	46,1,46,1,46,1,46,1,46,1,46,3,46,707,8,46,1,46,3,46,710,8,46,1,46,3,46,
  	713,8,46,1,46,3,46,716,8,46,1,46,3,46,719,8,46,1,47,1,47,1,47,1,48,1,
  	48,1,48,1,48,3,48,728,8,48,1,48,1,48,3,48,732,8,48,1,48,1,48,1,48,3,48,
  	737,8,48,1,48,1,48,3,48,741,8,48,1,48,1,48,1,48,3,48,746,8,48,1,48,1,
  	48,3,48,750,8,48,1,48,1,48,1,48,3,48,755,8,48,1,48,1,48,3,48,759,8,48,
  	1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,51,1,51,
  	5,51,775,8,51,10,51,12,51,778,9,51,1,51,1,51,1,52,1,52,1,53,1,53,5,53,
  	786,8,53,10,53,12,53,789,9,53,1,53,1,53,1,54,1,54,1,54,1,54,1,55,1,55,
  	1,55,3,55,800,8,55,1,55,1,55,4,55,804,8,55,11,55,12,55,805,1,56,1,56,
  	1,56,1,56,4,56,812,8,56,11,56,12,56,813,1,56,1,56,1,57,1,57,1,57,3,57,
  	821,8,57,1,57,1,57,4,57,825,8,57,11,57,12,57,826,1,58,1,58,1,58,1,58,
  	1,58,4,58,834,8,58,11,58,12,58,835,1,58,1,58,1,59,1,59,1,60,1,60,1,61,
  	1,61,1,62,1,62,1,62,0,0,63,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
  	32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,
  	78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,
  	118,120,122,124,0,10,1,1,44,44,2,0,2,2,35,37,1,0,9,11,1,0,14,15,1,0,12,
  	13,2,0,71,71,73,73,1,0,2,4,2,0,2,2,35,36,1,0,35,37,2,0,1,1,35,37,943,
  	0,167,1,0,0,0,2,172,1,0,0,0,4,182,1,0,0,0,6,186,1,0,0,0,8,209,1,0,0,0,
  	10,213,1,0,0,0,12,230,1,0,0,0,14,241,1,0,0,0,16,246,1,0,0,0,18,260,1,
  	0,0,0,20,271,1,0,0,0,22,276,1,0,0,0,24,285,1,0,0,0,26,289,1,0,0,0,28,
  	306,1,0,0,0,30,310,1,0,0,0,32,328,1,0,0,0,34,332,1,0,0,0,36,351,1,0,0,
  	0,38,355,1,0,0,0,40,372,1,0,0,0,42,376,1,0,0,0,44,394,1,0,0,0,46,398,
  	1,0,0,0,48,417,1,0,0,0,50,421,1,0,0,0,52,447,1,0,0,0,54,451,1,0,0,0,56,
  	474,1,0,0,0,58,478,1,0,0,0,60,501,1,0,0,0,62,505,1,0,0,0,64,524,1,0,0,
  	0,66,528,1,0,0,0,68,551,1,0,0,0,70,563,1,0,0,0,72,567,1,0,0,0,74,587,
  	1,0,0,0,76,591,1,0,0,0,78,616,1,0,0,0,80,620,1,0,0,0,82,645,1,0,0,0,84,
  	649,1,0,0,0,86,674,1,0,0,0,88,678,1,0,0,0,90,696,1,0,0,0,92,700,1,0,0,
  	0,94,720,1,0,0,0,96,723,1,0,0,0,98,762,1,0,0,0,100,768,1,0,0,0,102,772,
  	1,0,0,0,104,781,1,0,0,0,106,783,1,0,0,0,108,792,1,0,0,0,110,796,1,0,0,
  	0,112,807,1,0,0,0,114,817,1,0,0,0,116,828,1,0,0,0,118,839,1,0,0,0,120,
  	841,1,0,0,0,122,843,1,0,0,0,124,845,1,0,0,0,126,166,5,5,0,0,127,129,5,
  	6,0,0,128,127,1,0,0,0,129,130,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,
  	131,166,1,0,0,0,132,166,3,2,1,0,133,166,3,4,2,0,134,166,3,24,12,0,135,
  	166,3,28,14,0,136,166,3,32,16,0,137,166,3,36,18,0,138,166,3,40,20,0,139,
  	166,3,44,22,0,140,166,3,48,24,0,141,166,3,52,26,0,142,166,3,56,28,0,143,
  	166,3,60,30,0,144,166,3,64,32,0,145,166,3,68,34,0,146,166,3,70,35,0,147,
  	166,3,74,37,0,148,166,3,78,39,0,149,166,3,82,41,0,150,166,3,8,4,0,151,
  	166,3,86,43,0,152,166,3,12,6,0,153,166,3,18,9,0,154,166,3,90,45,0,155,
  	166,3,94,47,0,156,166,3,96,48,0,157,166,3,98,49,0,158,166,3,100,50,0,
  	159,166,3,102,51,0,160,166,3,104,52,0,161,166,3,106,53,0,162,166,3,108,
  	54,0,163,166,3,110,55,0,164,166,3,114,57,0,165,126,1,0,0,0,165,128,1,
  	0,0,0,165,132,1,0,0,0,165,133,1,0,0,0,165,134,1,0,0,0,165,135,1,0,0,0,
  	165,136,1,0,0,0,165,137,1,0,0,0,165,138,1,0,0,0,165,139,1,0,0,0,165,140,
  	1,0,0,0,165,141,1,0,0,0,165,142,1,0,0,0,165,143,1,0,0,0,165,144,1,0,0,
  	0,165,145,1,0,0,0,165,146,1,0,0,0,165,147,1,0,0,0,165,148,1,0,0,0,165,
  	149,1,0,0,0,165,150,1,0,0,0,165,151,1,0,0,0,165,152,1,0,0,0,165,153,1,
  	0,0,0,165,154,1,0,0,0,165,155,1,0,0,0,165,156,1,0,0,0,165,157,1,0,0,0,
  	165,158,1,0,0,0,165,159,1,0,0,0,165,160,1,0,0,0,165,161,1,0,0,0,165,162,
  	1,0,0,0,165,163,1,0,0,0,165,164,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,
  	0,167,168,1,0,0,0,168,170,1,0,0,0,169,167,1,0,0,0,170,171,5,0,0,1,171,
  	1,1,0,0,0,172,176,5,8,0,0,173,175,5,42,0,0,174,173,1,0,0,0,175,178,1,
  	0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,179,1,0,0,0,178,176,1,0,0,0,
  	179,180,7,0,0,0,180,3,1,0,0,0,181,183,3,6,3,0,182,181,1,0,0,0,183,184,
  	1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,5,1,0,0,0,186,187,3,120,60,
  	0,187,188,3,122,61,0,188,189,3,124,62,0,189,190,3,120,60,0,190,191,3,
  	122,61,0,191,192,3,124,62,0,192,194,3,118,59,0,193,195,3,118,59,0,194,
  	193,1,0,0,0,194,195,1,0,0,0,195,197,1,0,0,0,196,198,3,118,59,0,197,196,
  	1,0,0,0,197,198,1,0,0,0,198,200,1,0,0,0,199,201,3,118,59,0,200,199,1,
  	0,0,0,200,201,1,0,0,0,201,203,1,0,0,0,202,204,3,118,59,0,203,202,1,0,
  	0,0,203,204,1,0,0,0,204,206,1,0,0,0,205,207,3,118,59,0,206,205,1,0,0,
  	0,206,207,1,0,0,0,207,7,1,0,0,0,208,210,3,10,5,0,209,208,1,0,0,0,210,
  	211,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,9,1,0,0,0,213,214,3,120,
  	60,0,214,215,3,122,61,0,215,216,3,122,61,0,216,217,3,118,59,0,217,219,
  	3,118,59,0,218,220,3,118,59,0,219,218,1,0,0,0,219,220,1,0,0,0,220,224,
  	1,0,0,0,221,222,5,20,0,0,222,223,5,21,0,0,223,225,5,2,0,0,224,221,1,0,
  	0,0,224,225,1,0,0,0,225,227,1,0,0,0,226,228,5,22,0,0,227,226,1,0,0,0,
  	227,228,1,0,0,0,228,11,1,0,0,0,229,231,3,14,7,0,230,229,1,0,0,0,231,232,
  	1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,237,1,0,0,0,234,238,5,5,0,
  	0,235,238,3,2,1,0,236,238,3,16,8,0,237,234,1,0,0,0,237,235,1,0,0,0,237,
  	236,1,0,0,0,238,239,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,13,1,
  	0,0,0,241,242,5,2,0,0,242,243,3,118,59,0,243,244,3,118,59,0,244,245,7,
  	1,0,0,245,15,1,0,0,0,246,247,3,120,60,0,247,248,3,122,61,0,248,249,3,
  	122,61,0,249,250,3,120,60,0,250,251,3,122,61,0,251,252,3,122,61,0,252,
  	253,3,118,59,0,253,254,3,118,59,0,254,255,3,118,59,0,255,257,5,2,0,0,
  	256,258,3,118,59,0,257,256,1,0,0,0,257,258,1,0,0,0,258,17,1,0,0,0,259,
  	261,3,20,10,0,260,259,1,0,0,0,261,262,1,0,0,0,262,260,1,0,0,0,262,263,
  	1,0,0,0,263,267,1,0,0,0,264,268,5,5,0,0,265,268,3,2,1,0,266,268,3,22,
  	11,0,267,264,1,0,0,0,267,265,1,0,0,0,267,266,1,0,0,0,268,269,1,0,0,0,
  	269,267,1,0,0,0,269,270,1,0,0,0,270,19,1,0,0,0,271,272,5,2,0,0,272,273,
  	3,118,59,0,273,274,3,118,59,0,274,275,7,1,0,0,275,21,1,0,0,0,276,277,
  	3,120,60,0,277,278,3,122,61,0,278,279,3,122,61,0,279,280,3,118,59,0,280,
  	281,3,118,59,0,281,282,3,118,59,0,282,283,5,2,0,0,283,23,1,0,0,0,284,
  	286,3,26,13,0,285,284,1,0,0,0,286,287,1,0,0,0,287,285,1,0,0,0,287,288,
  	1,0,0,0,288,25,1,0,0,0,289,290,3,120,60,0,290,292,3,122,61,0,291,293,
  	3,2,1,0,292,291,1,0,0,0,292,293,1,0,0,0,293,301,1,0,0,0,294,295,3,122,
  	61,0,295,296,3,120,60,0,296,297,3,122,61,0,297,298,3,122,61,0,298,299,
  	3,118,59,0,299,302,1,0,0,0,300,302,3,2,1,0,301,294,1,0,0,0,301,300,1,
  	0,0,0,302,303,1,0,0,0,303,301,1,0,0,0,303,304,1,0,0,0,304,27,1,0,0,0,
  	305,307,3,30,15,0,306,305,1,0,0,0,307,308,1,0,0,0,308,306,1,0,0,0,308,
  	309,1,0,0,0,309,29,1,0,0,0,310,311,3,120,60,0,311,313,3,122,61,0,312,
  	314,3,2,1,0,313,312,1,0,0,0,313,314,1,0,0,0,314,323,1,0,0,0,315,316,3,
  	122,61,0,316,317,3,120,60,0,317,318,3,122,61,0,318,319,3,122,61,0,319,
  	320,3,118,59,0,320,321,3,118,59,0,321,324,1,0,0,0,322,324,3,2,1,0,323,
  	315,1,0,0,0,323,322,1,0,0,0,324,325,1,0,0,0,325,323,1,0,0,0,325,326,1,
  	0,0,0,326,31,1,0,0,0,327,329,3,34,17,0,328,327,1,0,0,0,329,330,1,0,0,
  	0,330,328,1,0,0,0,330,331,1,0,0,0,331,33,1,0,0,0,332,333,3,120,60,0,333,
  	335,3,122,61,0,334,336,3,2,1,0,335,334,1,0,0,0,335,336,1,0,0,0,336,346,
  	1,0,0,0,337,338,3,122,61,0,338,339,3,120,60,0,339,340,3,122,61,0,340,
  	341,3,122,61,0,341,342,3,118,59,0,342,343,3,118,59,0,343,344,3,118,59,
  	0,344,347,1,0,0,0,345,347,3,2,1,0,346,337,1,0,0,0,346,345,1,0,0,0,347,
  	348,1,0,0,0,348,346,1,0,0,0,348,349,1,0,0,0,349,35,1,0,0,0,350,352,3,
  	38,19,0,351,350,1,0,0,0,352,353,1,0,0,0,353,351,1,0,0,0,353,354,1,0,0,
  	0,354,37,1,0,0,0,355,356,3,120,60,0,356,357,3,122,61,0,357,359,3,122,
  	61,0,358,360,3,2,1,0,359,358,1,0,0,0,359,360,1,0,0,0,360,367,1,0,0,0,
  	361,362,3,120,60,0,362,363,3,122,61,0,363,364,3,122,61,0,364,365,3,118,
  	59,0,365,368,1,0,0,0,366,368,3,2,1,0,367,361,1,0,0,0,367,366,1,0,0,0,
  	368,369,1,0,0,0,369,367,1,0,0,0,369,370,1,0,0,0,370,39,1,0,0,0,371,373,
  	3,42,21,0,372,371,1,0,0,0,373,374,1,0,0,0,374,372,1,0,0,0,374,375,1,0,
  	0,0,375,41,1,0,0,0,376,377,3,120,60,0,377,378,3,122,61,0,378,380,3,122,
  	61,0,379,381,3,2,1,0,380,379,1,0,0,0,380,381,1,0,0,0,381,389,1,0,0,0,
  	382,383,3,120,60,0,383,384,3,122,61,0,384,385,3,122,61,0,385,386,3,118,
  	59,0,386,387,3,118,59,0,387,390,1,0,0,0,388,390,3,2,1,0,389,382,1,0,0,
  	0,389,388,1,0,0,0,390,391,1,0,0,0,391,389,1,0,0,0,391,392,1,0,0,0,392,
  	43,1,0,0,0,393,395,3,46,23,0,394,393,1,0,0,0,395,396,1,0,0,0,396,394,
  	1,0,0,0,396,397,1,0,0,0,397,45,1,0,0,0,398,399,3,120,60,0,399,400,3,122,
  	61,0,400,402,3,122,61,0,401,403,3,2,1,0,402,401,1,0,0,0,402,403,1,0,0,
  	0,403,412,1,0,0,0,404,405,3,120,60,0,405,406,3,122,61,0,406,407,3,122,
  	61,0,407,408,3,118,59,0,408,409,3,118,59,0,409,410,3,118,59,0,410,413,
  	1,0,0,0,411,413,3,2,1,0,412,404,1,0,0,0,412,411,1,0,0,0,413,414,1,0,0,
  	0,414,412,1,0,0,0,414,415,1,0,0,0,415,47,1,0,0,0,416,418,3,50,25,0,417,
  	416,1,0,0,0,418,419,1,0,0,0,419,417,1,0,0,0,419,420,1,0,0,0,420,49,1,
  	0,0,0,421,422,7,2,0,0,422,423,3,122,61,0,423,424,3,120,60,0,424,425,3,
  	122,61,0,425,426,3,122,61,0,426,427,3,120,60,0,427,428,3,122,61,0,428,
  	430,3,118,59,0,429,431,3,118,59,0,430,429,1,0,0,0,430,431,1,0,0,0,431,
  	438,1,0,0,0,432,433,3,122,61,0,433,434,3,122,61,0,434,435,3,120,60,0,
  	435,436,3,122,61,0,436,437,3,118,59,0,437,439,1,0,0,0,438,432,1,0,0,0,
  	438,439,1,0,0,0,439,441,1,0,0,0,440,442,5,37,0,0,441,440,1,0,0,0,441,
  	442,1,0,0,0,442,444,1,0,0,0,443,445,5,2,0,0,444,443,1,0,0,0,444,445,1,
  	0,0,0,445,51,1,0,0,0,446,448,3,54,27,0,447,446,1,0,0,0,448,449,1,0,0,
  	0,449,447,1,0,0,0,449,450,1,0,0,0,450,53,1,0,0,0,451,452,7,3,0,0,452,
  	453,3,122,61,0,453,454,3,120,60,0,454,455,3,122,61,0,455,456,3,122,61,
  	0,456,457,3,120,60,0,457,458,3,122,61,0,458,465,3,118,59,0,459,460,3,
  	122,61,0,460,461,3,122,61,0,461,462,3,120,60,0,462,463,3,122,61,0,463,
  	464,3,118,59,0,464,466,1,0,0,0,465,459,1,0,0,0,465,466,1,0,0,0,466,468,
  	1,0,0,0,467,469,5,37,0,0,468,467,1,0,0,0,468,469,1,0,0,0,469,471,1,0,
  	0,0,470,472,5,2,0,0,471,470,1,0,0,0,471,472,1,0,0,0,472,55,1,0,0,0,473,
  	475,3,58,29,0,474,473,1,0,0,0,475,476,1,0,0,0,476,474,1,0,0,0,476,477,
  	1,0,0,0,477,57,1,0,0,0,478,479,7,4,0,0,479,480,3,122,61,0,480,481,3,120,
  	60,0,481,482,3,122,61,0,482,483,3,122,61,0,483,484,3,120,60,0,484,485,
  	3,122,61,0,485,492,3,118,59,0,486,487,3,122,61,0,487,488,3,122,61,0,488,
  	489,3,120,60,0,489,490,3,122,61,0,490,491,3,118,59,0,491,493,1,0,0,0,
  	492,486,1,0,0,0,492,493,1,0,0,0,493,495,1,0,0,0,494,496,5,37,0,0,495,
  	494,1,0,0,0,495,496,1,0,0,0,496,498,1,0,0,0,497,499,5,2,0,0,498,497,1,
  	0,0,0,498,499,1,0,0,0,499,59,1,0,0,0,500,502,3,62,31,0,501,500,1,0,0,
  	0,502,503,1,0,0,0,503,501,1,0,0,0,503,504,1,0,0,0,504,61,1,0,0,0,505,
  	506,5,17,0,0,506,507,3,122,61,0,507,508,3,120,60,0,508,509,3,122,61,0,
  	509,510,3,118,59,0,510,515,3,118,59,0,511,512,3,122,61,0,512,513,3,118,
  	59,0,513,514,3,118,59,0,514,516,1,0,0,0,515,511,1,0,0,0,515,516,1,0,0,
  	0,516,518,1,0,0,0,517,519,5,37,0,0,518,517,1,0,0,0,518,519,1,0,0,0,519,
  	521,1,0,0,0,520,522,5,2,0,0,521,520,1,0,0,0,521,522,1,0,0,0,522,63,1,
  	0,0,0,523,525,3,66,33,0,524,523,1,0,0,0,525,526,1,0,0,0,526,524,1,0,0,
  	0,526,527,1,0,0,0,527,65,1,0,0,0,528,529,5,16,0,0,529,530,3,122,61,0,
  	530,531,3,120,60,0,531,532,3,122,61,0,532,533,3,122,61,0,533,535,3,118,
  	59,0,534,536,3,118,59,0,535,534,1,0,0,0,535,536,1,0,0,0,536,543,1,0,0,
  	0,537,538,3,122,61,0,538,539,3,122,61,0,539,541,3,118,59,0,540,542,3,
  	118,59,0,541,540,1,0,0,0,541,542,1,0,0,0,542,544,1,0,0,0,543,537,1,0,
  	0,0,543,544,1,0,0,0,544,546,1,0,0,0,545,547,5,37,0,0,546,545,1,0,0,0,
  	546,547,1,0,0,0,547,549,1,0,0,0,548,550,5,2,0,0,549,548,1,0,0,0,549,550,
  	1,0,0,0,550,67,1,0,0,0,551,552,5,18,0,0,552,553,3,122,61,0,553,555,3,
  	120,60,0,554,556,3,122,61,0,555,554,1,0,0,0,556,557,1,0,0,0,557,555,1,
  	0,0,0,557,558,1,0,0,0,558,560,1,0,0,0,559,561,5,2,0,0,560,559,1,0,0,0,
  	560,561,1,0,0,0,561,69,1,0,0,0,562,564,3,72,36,0,563,562,1,0,0,0,564,
  	565,1,0,0,0,565,563,1,0,0,0,565,566,1,0,0,0,566,71,1,0,0,0,567,568,5,
  	19,0,0,568,569,3,122,61,0,569,570,3,120,60,0,570,571,3,122,61,0,571,577,
  	3,118,59,0,572,573,3,122,61,0,573,574,3,118,59,0,574,576,1,0,0,0,575,
  	572,1,0,0,0,576,579,1,0,0,0,577,575,1,0,0,0,577,578,1,0,0,0,578,581,1,
  	0,0,0,579,577,1,0,0,0,580,582,5,37,0,0,581,580,1,0,0,0,581,582,1,0,0,
  	0,582,584,1,0,0,0,583,585,5,2,0,0,584,583,1,0,0,0,584,585,1,0,0,0,585,
  	73,1,0,0,0,586,588,3,76,38,0,587,586,1,0,0,0,588,589,1,0,0,0,589,587,
  	1,0,0,0,589,590,1,0,0,0,590,75,1,0,0,0,591,592,5,2,0,0,592,593,3,122,
  	61,0,593,594,3,122,61,0,594,595,3,122,61,0,595,596,5,2,0,0,596,597,3,
  	122,61,0,597,598,3,122,61,0,598,599,3,122,61,0,599,601,3,118,59,0,600,
  	602,3,118,59,0,601,600,1,0,0,0,601,602,1,0,0,0,602,604,1,0,0,0,603,605,
  	3,118,59,0,604,603,1,0,0,0,604,605,1,0,0,0,605,607,1,0,0,0,606,608,3,
  	118,59,0,607,606,1,0,0,0,607,608,1,0,0,0,608,610,1,0,0,0,609,611,3,118,
  	59,0,610,609,1,0,0,0,610,611,1,0,0,0,611,613,1,0,0,0,612,614,3,118,59,
  	0,613,612,1,0,0,0,613,614,1,0,0,0,614,77,1,0,0,0,615,617,3,80,40,0,616,
  	615,1,0,0,0,617,618,1,0,0,0,618,616,1,0,0,0,618,619,1,0,0,0,619,79,1,
  	0,0,0,620,621,3,122,61,0,621,622,5,2,0,0,622,623,3,122,61,0,623,624,3,
  	122,61,0,624,625,3,122,61,0,625,626,5,2,0,0,626,627,3,122,61,0,627,628,
  	3,122,61,0,628,630,3,118,59,0,629,631,3,118,59,0,630,629,1,0,0,0,630,
  	631,1,0,0,0,631,633,1,0,0,0,632,634,3,118,59,0,633,632,1,0,0,0,633,634,
  	1,0,0,0,634,636,1,0,0,0,635,637,3,118,59,0,636,635,1,0,0,0,636,637,1,
  	0,0,0,637,639,1,0,0,0,638,640,3,118,59,0,639,638,1,0,0,0,639,640,1,0,
  	0,0,640,642,1,0,0,0,641,643,3,118,59,0,642,641,1,0,0,0,642,643,1,0,0,
  	0,643,81,1,0,0,0,644,646,3,84,42,0,645,644,1,0,0,0,646,647,1,0,0,0,647,
  	645,1,0,0,0,647,648,1,0,0,0,648,83,1,0,0,0,649,650,3,122,61,0,650,651,
  	3,122,61,0,651,652,5,2,0,0,652,653,3,122,61,0,653,654,3,122,61,0,654,
  	655,3,122,61,0,655,656,5,2,0,0,656,657,3,122,61,0,657,659,3,118,59,0,
  	658,660,3,118,59,0,659,658,1,0,0,0,659,660,1,0,0,0,660,662,1,0,0,0,661,
  	663,3,118,59,0,662,661,1,0,0,0,662,663,1,0,0,0,663,665,1,0,0,0,664,666,
  	3,118,59,0,665,664,1,0,0,0,665,666,1,0,0,0,666,668,1,0,0,0,667,669,3,
  	118,59,0,668,667,1,0,0,0,668,669,1,0,0,0,669,671,1,0,0,0,670,672,3,118,
  	59,0,671,670,1,0,0,0,671,672,1,0,0,0,672,85,1,0,0,0,673,675,3,88,44,0,
  	674,673,1,0,0,0,675,676,1,0,0,0,676,674,1,0,0,0,676,677,1,0,0,0,677,87,
  	1,0,0,0,678,679,3,122,61,0,679,680,5,2,0,0,680,681,3,122,61,0,681,682,
  	3,122,61,0,682,683,3,118,59,0,683,685,3,118,59,0,684,686,3,118,59,0,685,
  	684,1,0,0,0,685,686,1,0,0,0,686,690,1,0,0,0,687,688,5,20,0,0,688,689,
  	5,21,0,0,689,691,5,2,0,0,690,687,1,0,0,0,690,691,1,0,0,0,691,693,1,0,
  	0,0,692,694,5,22,0,0,693,692,1,0,0,0,693,694,1,0,0,0,694,89,1,0,0,0,695,
  	697,3,92,46,0,696,695,1,0,0,0,697,698,1,0,0,0,698,696,1,0,0,0,698,699,
  	1,0,0,0,699,91,1,0,0,0,700,701,3,120,60,0,701,702,3,122,61,0,702,703,
  	3,122,61,0,703,704,3,122,61,0,704,706,3,118,59,0,705,707,3,118,59,0,706,
  	705,1,0,0,0,706,707,1,0,0,0,707,709,1,0,0,0,708,710,3,118,59,0,709,708,
  	1,0,0,0,709,710,1,0,0,0,710,712,1,0,0,0,711,713,3,118,59,0,712,711,1,
  	0,0,0,712,713,1,0,0,0,713,715,1,0,0,0,714,716,3,118,59,0,715,714,1,0,
  	0,0,715,716,1,0,0,0,716,718,1,0,0,0,717,719,3,118,59,0,718,717,1,0,0,
  	0,718,719,1,0,0,0,719,93,1,0,0,0,720,721,5,23,0,0,721,722,5,24,0,0,722,
  	95,1,0,0,0,723,731,5,25,0,0,724,725,5,45,0,0,725,728,5,49,0,0,726,728,
  	5,50,0,0,727,724,1,0,0,0,727,726,1,0,0,0,727,728,1,0,0,0,728,729,1,0,
  	0,0,729,732,5,59,0,0,730,732,5,54,0,0,731,727,1,0,0,0,731,730,1,0,0,0,
  	732,740,1,0,0,0,733,734,5,47,0,0,734,737,5,49,0,0,735,737,5,52,0,0,736,
  	733,1,0,0,0,736,735,1,0,0,0,736,737,1,0,0,0,737,738,1,0,0,0,738,741,5,
  	58,0,0,739,741,5,56,0,0,740,736,1,0,0,0,740,739,1,0,0,0,741,749,1,0,0,
  	0,742,743,5,46,0,0,743,746,5,49,0,0,744,746,5,51,0,0,745,742,1,0,0,0,
  	745,744,1,0,0,0,745,746,1,0,0,0,746,747,1,0,0,0,747,750,5,59,0,0,748,
  	750,5,55,0,0,749,745,1,0,0,0,749,748,1,0,0,0,750,758,1,0,0,0,751,752,
  	5,48,0,0,752,755,5,49,0,0,753,755,5,53,0,0,754,751,1,0,0,0,754,753,1,
  	0,0,0,754,755,1,0,0,0,755,756,1,0,0,0,756,759,5,58,0,0,757,759,5,57,0,
  	0,758,754,1,0,0,0,758,757,1,0,0,0,759,760,1,0,0,0,760,761,5,61,0,0,761,
  	97,1,0,0,0,762,763,5,26,0,0,763,764,3,122,61,0,764,765,3,120,60,0,765,
  	766,3,122,61,0,766,767,3,120,60,0,767,99,1,0,0,0,768,769,5,27,0,0,769,
  	770,5,63,0,0,770,771,5,65,0,0,771,101,1,0,0,0,772,776,5,28,0,0,773,775,
  	5,67,0,0,774,773,1,0,0,0,775,778,1,0,0,0,776,774,1,0,0,0,776,777,1,0,
  	0,0,777,779,1,0,0,0,778,776,1,0,0,0,779,780,5,69,0,0,780,103,1,0,0,0,
  	781,782,5,30,0,0,782,105,1,0,0,0,783,787,5,29,0,0,784,786,5,67,0,0,785,
  	784,1,0,0,0,786,789,1,0,0,0,787,785,1,0,0,0,787,788,1,0,0,0,788,790,1,
  	0,0,0,789,787,1,0,0,0,790,791,5,69,0,0,791,107,1,0,0,0,792,793,5,31,0,
  	0,793,794,5,63,0,0,794,795,5,65,0,0,795,109,1,0,0,0,796,797,5,32,0,0,
  	797,799,3,122,61,0,798,800,3,2,1,0,799,798,1,0,0,0,799,800,1,0,0,0,800,
  	803,1,0,0,0,801,804,3,112,56,0,802,804,3,2,1,0,803,801,1,0,0,0,803,802,
  	1,0,0,0,804,805,1,0,0,0,805,803,1,0,0,0,805,806,1,0,0,0,806,111,1,0,0,
  	0,807,808,5,33,0,0,808,809,5,73,0,0,809,811,5,74,0,0,810,812,5,73,0,0,
  	811,810,1,0,0,0,812,813,1,0,0,0,813,811,1,0,0,0,813,814,1,0,0,0,814,815,
  	1,0,0,0,815,816,5,76,0,0,816,113,1,0,0,0,817,818,5,32,0,0,818,820,3,122,
  	61,0,819,821,3,2,1,0,820,819,1,0,0,0,820,821,1,0,0,0,821,824,1,0,0,0,
  	822,825,3,116,58,0,823,825,3,2,1,0,824,822,1,0,0,0,824,823,1,0,0,0,825,
  	826,1,0,0,0,826,824,1,0,0,0,826,827,1,0,0,0,827,115,1,0,0,0,828,829,5,
  	34,0,0,829,830,7,5,0,0,830,833,5,74,0,0,831,832,5,73,0,0,832,834,5,72,
  	0,0,833,831,1,0,0,0,834,835,1,0,0,0,835,833,1,0,0,0,835,836,1,0,0,0,836,
  	837,1,0,0,0,837,838,5,76,0,0,838,117,1,0,0,0,839,840,7,6,0,0,840,119,
  	1,0,0,0,841,842,7,7,0,0,842,121,1,0,0,0,843,844,7,8,0,0,844,123,1,0,0,
  	0,845,846,7,9,0,0,846,125,1,0,0,0,120,130,165,167,176,184,194,197,200,
  	203,206,211,219,224,227,232,237,239,257,262,267,269,287,292,301,303,308,
  	313,323,325,330,335,346,348,353,359,367,369,374,380,389,391,396,402,412,
  	414,419,430,438,441,444,449,465,468,471,476,492,495,498,503,515,518,521,
  	526,535,541,543,546,549,557,560,565,577,581,584,589,601,604,607,610,613,
  	618,630,633,636,639,642,647,659,662,665,668,671,676,685,690,693,698,706,
  	709,712,715,718,727,731,736,740,745,749,754,758,776,787,799,803,805,813,
  	820,824,826,835
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  cyanamrparserParserStaticData = std::move(staticData);
}

}

CyanaMRParser::CyanaMRParser(TokenStream *input) : CyanaMRParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

CyanaMRParser::CyanaMRParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  CyanaMRParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *cyanamrparserParserStaticData->atn, cyanamrparserParserStaticData->decisionToDFA, cyanamrparserParserStaticData->sharedContextCache, options);
}

CyanaMRParser::~CyanaMRParser() {
  delete _interpreter;
}

const atn::ATN& CyanaMRParser::getATN() const {
  return *cyanamrparserParserStaticData->atn;
}

std::string CyanaMRParser::getGrammarFileName() const {
  return "CyanaMRParser.g4";
}

const std::vector<std::string>& CyanaMRParser::getRuleNames() const {
  return cyanamrparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& CyanaMRParser::getVocabulary() const {
  return cyanamrparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView CyanaMRParser::getSerializedATN() const {
  return cyanamrparserParserStaticData->serializedATN;
}


//----------------- Cyana_mrContext ------------------------------------------------------------------

CyanaMRParser::Cyana_mrContext::Cyana_mrContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Cyana_mrContext::EOF() {
  return getToken(CyanaMRParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Cyana_mrContext::Orientation_header() {
  return getTokens(CyanaMRParser::Orientation_header);
}

tree::TerminalNode* CyanaMRParser::Cyana_mrContext::Orientation_header(size_t i) {
  return getToken(CyanaMRParser::Orientation_header, i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Cyana_mrContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Cyana_mrContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::Distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::distance_restraints() {
  return getRuleContexts<CyanaMRParser::Distance_restraintsContext>();
}

CyanaMRParser::Distance_restraintsContext* CyanaMRParser::Cyana_mrContext::distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Fixres_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::fixres_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Fixres_distance_restraintsContext>();
}

CyanaMRParser::Fixres_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::fixres_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Fixres_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Fixresw_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::fixresw_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Fixresw_distance_restraintsContext>();
}

CyanaMRParser::Fixresw_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::fixresw_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Fixresw_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Fixresw2_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::fixresw2_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Fixresw2_distance_restraintsContext>();
}

CyanaMRParser::Fixresw2_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::fixresw2_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Fixresw2_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Fixatm_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::fixatm_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Fixatm_distance_restraintsContext>();
}

CyanaMRParser::Fixatm_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::fixatm_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Fixatm_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Fixatmw_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::fixatmw_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Fixatmw_distance_restraintsContext>();
}

CyanaMRParser::Fixatmw_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::fixatmw_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Fixatmw_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Fixatmw2_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::fixatmw2_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Fixatmw2_distance_restraintsContext>();
}

CyanaMRParser::Fixatmw2_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::fixatmw2_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Fixatmw2_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Diana_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::diana_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Diana_distance_restraintsContext>();
}

CyanaMRParser::Diana_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::diana_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Diana_ssbond_restraintsContext *> CyanaMRParser::Cyana_mrContext::diana_ssbond_restraints() {
  return getRuleContexts<CyanaMRParser::Diana_ssbond_restraintsContext>();
}

CyanaMRParser::Diana_ssbond_restraintsContext* CyanaMRParser::Cyana_mrContext::diana_ssbond_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_ssbond_restraintsContext>(i);
}

std::vector<CyanaMRParser::Diana_hbond_restraintsContext *> CyanaMRParser::Cyana_mrContext::diana_hbond_restraints() {
  return getRuleContexts<CyanaMRParser::Diana_hbond_restraintsContext>();
}

CyanaMRParser::Diana_hbond_restraintsContext* CyanaMRParser::Cyana_mrContext::diana_hbond_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_hbond_restraintsContext>(i);
}

std::vector<CyanaMRParser::Diana_torsion_angle_restraintsContext *> CyanaMRParser::Cyana_mrContext::diana_torsion_angle_restraints() {
  return getRuleContexts<CyanaMRParser::Diana_torsion_angle_restraintsContext>();
}

CyanaMRParser::Diana_torsion_angle_restraintsContext* CyanaMRParser::Cyana_mrContext::diana_torsion_angle_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_torsion_angle_restraintsContext>(i);
}

std::vector<CyanaMRParser::Diana_coupling_constant_restraintsContext *> CyanaMRParser::Cyana_mrContext::diana_coupling_constant_restraints() {
  return getRuleContexts<CyanaMRParser::Diana_coupling_constant_restraintsContext>();
}

CyanaMRParser::Diana_coupling_constant_restraintsContext* CyanaMRParser::Cyana_mrContext::diana_coupling_constant_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_coupling_constant_restraintsContext>(i);
}

std::vector<CyanaMRParser::Diana_stereoassign_macroContext *> CyanaMRParser::Cyana_mrContext::diana_stereoassign_macro() {
  return getRuleContexts<CyanaMRParser::Diana_stereoassign_macroContext>();
}

CyanaMRParser::Diana_stereoassign_macroContext* CyanaMRParser::Cyana_mrContext::diana_stereoassign_macro(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_stereoassign_macroContext>(i);
}

std::vector<CyanaMRParser::Diana_chemical_shiftsContext *> CyanaMRParser::Cyana_mrContext::diana_chemical_shifts() {
  return getRuleContexts<CyanaMRParser::Diana_chemical_shiftsContext>();
}

CyanaMRParser::Diana_chemical_shiftsContext* CyanaMRParser::Cyana_mrContext::diana_chemical_shifts(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_chemical_shiftsContext>(i);
}

std::vector<CyanaMRParser::Distance_w_chain_restraintsContext *> CyanaMRParser::Cyana_mrContext::distance_w_chain_restraints() {
  return getRuleContexts<CyanaMRParser::Distance_w_chain_restraintsContext>();
}

CyanaMRParser::Distance_w_chain_restraintsContext* CyanaMRParser::Cyana_mrContext::distance_w_chain_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_w_chain_restraintsContext>(i);
}

std::vector<CyanaMRParser::Distance_w_chain2_restraintsContext *> CyanaMRParser::Cyana_mrContext::distance_w_chain2_restraints() {
  return getRuleContexts<CyanaMRParser::Distance_w_chain2_restraintsContext>();
}

CyanaMRParser::Distance_w_chain2_restraintsContext* CyanaMRParser::Cyana_mrContext::distance_w_chain2_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_w_chain2_restraintsContext>(i);
}

std::vector<CyanaMRParser::Distance_w_chain3_restraintsContext *> CyanaMRParser::Cyana_mrContext::distance_w_chain3_restraints() {
  return getRuleContexts<CyanaMRParser::Distance_w_chain3_restraintsContext>();
}

CyanaMRParser::Distance_w_chain3_restraintsContext* CyanaMRParser::Cyana_mrContext::distance_w_chain3_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_w_chain3_restraintsContext>(i);
}

std::vector<CyanaMRParser::Torsion_angle_restraintsContext *> CyanaMRParser::Cyana_mrContext::torsion_angle_restraints() {
  return getRuleContexts<CyanaMRParser::Torsion_angle_restraintsContext>();
}

CyanaMRParser::Torsion_angle_restraintsContext* CyanaMRParser::Cyana_mrContext::torsion_angle_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Torsion_angle_restraintsContext>(i);
}

std::vector<CyanaMRParser::Torsion_angle_w_chain_restraintsContext *> CyanaMRParser::Cyana_mrContext::torsion_angle_w_chain_restraints() {
  return getRuleContexts<CyanaMRParser::Torsion_angle_w_chain_restraintsContext>();
}

CyanaMRParser::Torsion_angle_w_chain_restraintsContext* CyanaMRParser::Cyana_mrContext::torsion_angle_w_chain_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Torsion_angle_w_chain_restraintsContext>(i);
}

std::vector<CyanaMRParser::Rdc_restraintsContext *> CyanaMRParser::Cyana_mrContext::rdc_restraints() {
  return getRuleContexts<CyanaMRParser::Rdc_restraintsContext>();
}

CyanaMRParser::Rdc_restraintsContext* CyanaMRParser::Cyana_mrContext::rdc_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Rdc_restraintsContext>(i);
}

std::vector<CyanaMRParser::Pcs_restraintsContext *> CyanaMRParser::Cyana_mrContext::pcs_restraints() {
  return getRuleContexts<CyanaMRParser::Pcs_restraintsContext>();
}

CyanaMRParser::Pcs_restraintsContext* CyanaMRParser::Cyana_mrContext::pcs_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Pcs_restraintsContext>(i);
}

std::vector<CyanaMRParser::Cco_restraintsContext *> CyanaMRParser::Cyana_mrContext::cco_restraints() {
  return getRuleContexts<CyanaMRParser::Cco_restraintsContext>();
}

CyanaMRParser::Cco_restraintsContext* CyanaMRParser::Cyana_mrContext::cco_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Cco_restraintsContext>(i);
}

std::vector<CyanaMRParser::Ssbond_macroContext *> CyanaMRParser::Cyana_mrContext::ssbond_macro() {
  return getRuleContexts<CyanaMRParser::Ssbond_macroContext>();
}

CyanaMRParser::Ssbond_macroContext* CyanaMRParser::Cyana_mrContext::ssbond_macro(size_t i) {
  return getRuleContext<CyanaMRParser::Ssbond_macroContext>(i);
}

std::vector<CyanaMRParser::Hbond_macroContext *> CyanaMRParser::Cyana_mrContext::hbond_macro() {
  return getRuleContexts<CyanaMRParser::Hbond_macroContext>();
}

CyanaMRParser::Hbond_macroContext* CyanaMRParser::Cyana_mrContext::hbond_macro(size_t i) {
  return getRuleContext<CyanaMRParser::Hbond_macroContext>(i);
}

std::vector<CyanaMRParser::Link_statementContext *> CyanaMRParser::Cyana_mrContext::link_statement() {
  return getRuleContexts<CyanaMRParser::Link_statementContext>();
}

CyanaMRParser::Link_statementContext* CyanaMRParser::Cyana_mrContext::link_statement(size_t i) {
  return getRuleContext<CyanaMRParser::Link_statementContext>(i);
}

std::vector<CyanaMRParser::Stereoassign_macroContext *> CyanaMRParser::Cyana_mrContext::stereoassign_macro() {
  return getRuleContexts<CyanaMRParser::Stereoassign_macroContext>();
}

CyanaMRParser::Stereoassign_macroContext* CyanaMRParser::Cyana_mrContext::stereoassign_macro(size_t i) {
  return getRuleContext<CyanaMRParser::Stereoassign_macroContext>(i);
}

std::vector<CyanaMRParser::Declare_variableContext *> CyanaMRParser::Cyana_mrContext::declare_variable() {
  return getRuleContexts<CyanaMRParser::Declare_variableContext>();
}

CyanaMRParser::Declare_variableContext* CyanaMRParser::Cyana_mrContext::declare_variable(size_t i) {
  return getRuleContext<CyanaMRParser::Declare_variableContext>(i);
}

std::vector<CyanaMRParser::Set_variableContext *> CyanaMRParser::Cyana_mrContext::set_variable() {
  return getRuleContexts<CyanaMRParser::Set_variableContext>();
}

CyanaMRParser::Set_variableContext* CyanaMRParser::Cyana_mrContext::set_variable(size_t i) {
  return getRuleContext<CyanaMRParser::Set_variableContext>(i);
}

std::vector<CyanaMRParser::Unset_variableContext *> CyanaMRParser::Cyana_mrContext::unset_variable() {
  return getRuleContexts<CyanaMRParser::Unset_variableContext>();
}

CyanaMRParser::Unset_variableContext* CyanaMRParser::Cyana_mrContext::unset_variable(size_t i) {
  return getRuleContext<CyanaMRParser::Unset_variableContext>(i);
}

std::vector<CyanaMRParser::Print_macroContext *> CyanaMRParser::Cyana_mrContext::print_macro() {
  return getRuleContexts<CyanaMRParser::Print_macroContext>();
}

CyanaMRParser::Print_macroContext* CyanaMRParser::Cyana_mrContext::print_macro(size_t i) {
  return getRuleContext<CyanaMRParser::Print_macroContext>(i);
}

std::vector<CyanaMRParser::Unambig_atom_name_mappingContext *> CyanaMRParser::Cyana_mrContext::unambig_atom_name_mapping() {
  return getRuleContexts<CyanaMRParser::Unambig_atom_name_mappingContext>();
}

CyanaMRParser::Unambig_atom_name_mappingContext* CyanaMRParser::Cyana_mrContext::unambig_atom_name_mapping(size_t i) {
  return getRuleContext<CyanaMRParser::Unambig_atom_name_mappingContext>(i);
}

std::vector<CyanaMRParser::Ambig_atom_name_mappingContext *> CyanaMRParser::Cyana_mrContext::ambig_atom_name_mapping() {
  return getRuleContexts<CyanaMRParser::Ambig_atom_name_mappingContext>();
}

CyanaMRParser::Ambig_atom_name_mappingContext* CyanaMRParser::Cyana_mrContext::ambig_atom_name_mapping(size_t i) {
  return getRuleContext<CyanaMRParser::Ambig_atom_name_mappingContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Cyana_mrContext::Tensor_header() {
  return getTokens(CyanaMRParser::Tensor_header);
}

tree::TerminalNode* CyanaMRParser::Cyana_mrContext::Tensor_header(size_t i) {
  return getToken(CyanaMRParser::Tensor_header, i);
}


size_t CyanaMRParser::Cyana_mrContext::getRuleIndex() const {
  return CyanaMRParser::RuleCyana_mr;
}


std::any CyanaMRParser::Cyana_mrContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitCyana_mr(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Cyana_mrContext* CyanaMRParser::cyana_mr() {
  Cyana_mrContext *_localctx = _tracker.createInstance<Cyana_mrContext>(_ctx, getState());
  enterRule(_localctx, 0, CyanaMRParser::RuleCyana_mr);
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
    setState(167);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 249083985764) != 0)) {
      setState(165);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(126);
        match(CyanaMRParser::Orientation_header);
        break;
      }

      case 2: {
        setState(128); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(127);
                  match(CyanaMRParser::Tensor_header);
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(130); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 3: {
        setState(132);
        comment();
        break;
      }

      case 4: {
        setState(133);
        distance_restraints();
        break;
      }

      case 5: {
        setState(134);
        fixres_distance_restraints();
        break;
      }

      case 6: {
        setState(135);
        fixresw_distance_restraints();
        break;
      }

      case 7: {
        setState(136);
        fixresw2_distance_restraints();
        break;
      }

      case 8: {
        setState(137);
        fixatm_distance_restraints();
        break;
      }

      case 9: {
        setState(138);
        fixatmw_distance_restraints();
        break;
      }

      case 10: {
        setState(139);
        fixatmw2_distance_restraints();
        break;
      }

      case 11: {
        setState(140);
        diana_distance_restraints();
        break;
      }

      case 12: {
        setState(141);
        diana_ssbond_restraints();
        break;
      }

      case 13: {
        setState(142);
        diana_hbond_restraints();
        break;
      }

      case 14: {
        setState(143);
        diana_torsion_angle_restraints();
        break;
      }

      case 15: {
        setState(144);
        diana_coupling_constant_restraints();
        break;
      }

      case 16: {
        setState(145);
        diana_stereoassign_macro();
        break;
      }

      case 17: {
        setState(146);
        diana_chemical_shifts();
        break;
      }

      case 18: {
        setState(147);
        distance_w_chain_restraints();
        break;
      }

      case 19: {
        setState(148);
        distance_w_chain2_restraints();
        break;
      }

      case 20: {
        setState(149);
        distance_w_chain3_restraints();
        break;
      }

      case 21: {
        setState(150);
        torsion_angle_restraints();
        break;
      }

      case 22: {
        setState(151);
        torsion_angle_w_chain_restraints();
        break;
      }

      case 23: {
        setState(152);
        rdc_restraints();
        break;
      }

      case 24: {
        setState(153);
        pcs_restraints();
        break;
      }

      case 25: {
        setState(154);
        cco_restraints();
        break;
      }

      case 26: {
        setState(155);
        ssbond_macro();
        break;
      }

      case 27: {
        setState(156);
        hbond_macro();
        break;
      }

      case 28: {
        setState(157);
        link_statement();
        break;
      }

      case 29: {
        setState(158);
        stereoassign_macro();
        break;
      }

      case 30: {
        setState(159);
        declare_variable();
        break;
      }

      case 31: {
        setState(160);
        set_variable();
        break;
      }

      case 32: {
        setState(161);
        unset_variable();
        break;
      }

      case 33: {
        setState(162);
        print_macro();
        break;
      }

      case 34: {
        setState(163);
        unambig_atom_name_mapping();
        break;
      }

      case 35: {
        setState(164);
        ambig_atom_name_mapping();
        break;
      }

      default:
        break;
      }
      setState(169);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(170);
    match(CyanaMRParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CommentContext ------------------------------------------------------------------

CyanaMRParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::CommentContext::COMMENT() {
  return getToken(CyanaMRParser::COMMENT, 0);
}

tree::TerminalNode* CyanaMRParser::CommentContext::RETURN_CM() {
  return getToken(CyanaMRParser::RETURN_CM, 0);
}

tree::TerminalNode* CyanaMRParser::CommentContext::EOF() {
  return getToken(CyanaMRParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::CommentContext::Any_name() {
  return getTokens(CyanaMRParser::Any_name);
}

tree::TerminalNode* CyanaMRParser::CommentContext::Any_name(size_t i) {
  return getToken(CyanaMRParser::Any_name, i);
}


size_t CyanaMRParser::CommentContext::getRuleIndex() const {
  return CyanaMRParser::RuleComment;
}


std::any CyanaMRParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::CommentContext* CyanaMRParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 2, CyanaMRParser::RuleComment);
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
    setState(172);
    match(CyanaMRParser::COMMENT);
    setState(176);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Any_name) {
      setState(173);
      match(CyanaMRParser::Any_name);
      setState(178);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(179);
    _la = _input->LA(1);
    if (!(_la == CyanaMRParser::EOF

    || _la == CyanaMRParser::RETURN_CM)) {
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

//----------------- Distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Distance_restraintsContext::Distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Distance_restraintContext *> CyanaMRParser::Distance_restraintsContext::distance_restraint() {
  return getRuleContexts<CyanaMRParser::Distance_restraintContext>();
}

CyanaMRParser::Distance_restraintContext* CyanaMRParser::Distance_restraintsContext::distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_restraintContext>(i);
}


size_t CyanaMRParser::Distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_restraints;
}


std::any CyanaMRParser::Distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_restraintsContext* CyanaMRParser::distance_restraints() {
  Distance_restraintsContext *_localctx = _tracker.createInstance<Distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 4, CyanaMRParser::RuleDistance_restraints);

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
    setState(182); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(181);
              distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(184); 
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

//----------------- Distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Distance_restraintContext::Distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::Gen_atom_nameContext *> CyanaMRParser::Distance_restraintContext::gen_atom_name() {
  return getRuleContexts<CyanaMRParser::Gen_atom_nameContext>();
}

CyanaMRParser::Gen_atom_nameContext* CyanaMRParser::Distance_restraintContext::gen_atom_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_atom_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_restraint;
}


std::any CyanaMRParser::Distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_restraintContext* CyanaMRParser::distance_restraint() {
  Distance_restraintContext *_localctx = _tracker.createInstance<Distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 6, CyanaMRParser::RuleDistance_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(186);
    gen_res_num();
    setState(187);
    gen_simple_name();
    setState(188);
    gen_atom_name();
    setState(189);
    gen_res_num();
    setState(190);
    gen_simple_name();
    setState(191);
    gen_atom_name();
    setState(192);
    number();
    setState(194);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx)) {
    case 1: {
      setState(193);
      number();
      break;
    }

    default:
      break;
    }
    setState(197);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 6, _ctx)) {
    case 1: {
      setState(196);
      number();
      break;
    }

    default:
      break;
    }
    setState(200);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx)) {
    case 1: {
      setState(199);
      number();
      break;
    }

    default:
      break;
    }
    setState(203);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx)) {
    case 1: {
      setState(202);
      number();
      break;
    }

    default:
      break;
    }
    setState(206);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx)) {
    case 1: {
      setState(205);
      number();
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

//----------------- Torsion_angle_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Torsion_angle_restraintsContext::Torsion_angle_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Torsion_angle_restraintContext *> CyanaMRParser::Torsion_angle_restraintsContext::torsion_angle_restraint() {
  return getRuleContexts<CyanaMRParser::Torsion_angle_restraintContext>();
}

CyanaMRParser::Torsion_angle_restraintContext* CyanaMRParser::Torsion_angle_restraintsContext::torsion_angle_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Torsion_angle_restraintContext>(i);
}


size_t CyanaMRParser::Torsion_angle_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleTorsion_angle_restraints;
}


std::any CyanaMRParser::Torsion_angle_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitTorsion_angle_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Torsion_angle_restraintsContext* CyanaMRParser::torsion_angle_restraints() {
  Torsion_angle_restraintsContext *_localctx = _tracker.createInstance<Torsion_angle_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 8, CyanaMRParser::RuleTorsion_angle_restraints);

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
    setState(209); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(208);
              torsion_angle_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(211); 
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

//----------------- Torsion_angle_restraintContext ------------------------------------------------------------------

CyanaMRParser::Torsion_angle_restraintContext::Torsion_angle_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Torsion_angle_restraintContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Torsion_angle_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Torsion_angle_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Torsion_angle_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Torsion_angle_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_restraintContext::Type() {
  return getToken(CyanaMRParser::Type, 0);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_restraintContext::Equ_op() {
  return getToken(CyanaMRParser::Equ_op, 0);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_restraintContext::Or() {
  return getToken(CyanaMRParser::Or, 0);
}


size_t CyanaMRParser::Torsion_angle_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleTorsion_angle_restraint;
}


std::any CyanaMRParser::Torsion_angle_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitTorsion_angle_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Torsion_angle_restraintContext* CyanaMRParser::torsion_angle_restraint() {
  Torsion_angle_restraintContext *_localctx = _tracker.createInstance<Torsion_angle_restraintContext>(_ctx, getState());
  enterRule(_localctx, 10, CyanaMRParser::RuleTorsion_angle_restraint);
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
    setState(213);
    gen_res_num();
    setState(214);
    gen_simple_name();
    setState(215);
    gen_simple_name();
    setState(216);
    number();
    setState(217);
    number();
    setState(219);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx)) {
    case 1: {
      setState(218);
      number();
      break;
    }

    default:
      break;
    }
    setState(224);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Type) {
      setState(221);
      match(CyanaMRParser::Type);
      setState(222);
      match(CyanaMRParser::Equ_op);
      setState(223);
      match(CyanaMRParser::Integer);
    }
    setState(227);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Or) {
      setState(226);
      match(CyanaMRParser::Or);
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

CyanaMRParser::Rdc_restraintsContext::Rdc_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Rdc_parameterContext *> CyanaMRParser::Rdc_restraintsContext::rdc_parameter() {
  return getRuleContexts<CyanaMRParser::Rdc_parameterContext>();
}

CyanaMRParser::Rdc_parameterContext* CyanaMRParser::Rdc_restraintsContext::rdc_parameter(size_t i) {
  return getRuleContext<CyanaMRParser::Rdc_parameterContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Rdc_restraintsContext::Orientation_header() {
  return getTokens(CyanaMRParser::Orientation_header);
}

tree::TerminalNode* CyanaMRParser::Rdc_restraintsContext::Orientation_header(size_t i) {
  return getToken(CyanaMRParser::Orientation_header, i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Rdc_restraintsContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Rdc_restraintsContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::Rdc_restraintContext *> CyanaMRParser::Rdc_restraintsContext::rdc_restraint() {
  return getRuleContexts<CyanaMRParser::Rdc_restraintContext>();
}

CyanaMRParser::Rdc_restraintContext* CyanaMRParser::Rdc_restraintsContext::rdc_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Rdc_restraintContext>(i);
}


size_t CyanaMRParser::Rdc_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleRdc_restraints;
}


std::any CyanaMRParser::Rdc_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitRdc_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Rdc_restraintsContext* CyanaMRParser::rdc_restraints() {
  Rdc_restraintsContext *_localctx = _tracker.createInstance<Rdc_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 12, CyanaMRParser::RuleRdc_restraints);

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
    setState(230); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(229);
              rdc_parameter();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(232); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(237); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(237);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Orientation_header: {
                  setState(234);
                  match(CyanaMRParser::Orientation_header);
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(235);
                  comment();
                  break;
                }

                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(236);
                  rdc_restraint();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(239); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 16, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Rdc_parameterContext ------------------------------------------------------------------

CyanaMRParser::Rdc_parameterContext::Rdc_parameterContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> CyanaMRParser::Rdc_parameterContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Rdc_parameterContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Rdc_parameterContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Rdc_parameterContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Rdc_parameterContext::Capital_integer() {
  return getToken(CyanaMRParser::Capital_integer, 0);
}

tree::TerminalNode* CyanaMRParser::Rdc_parameterContext::Integer_capital() {
  return getToken(CyanaMRParser::Integer_capital, 0);
}

tree::TerminalNode* CyanaMRParser::Rdc_parameterContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}


size_t CyanaMRParser::Rdc_parameterContext::getRuleIndex() const {
  return CyanaMRParser::RuleRdc_parameter;
}


std::any CyanaMRParser::Rdc_parameterContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitRdc_parameter(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Rdc_parameterContext* CyanaMRParser::rdc_parameter() {
  Rdc_parameterContext *_localctx = _tracker.createInstance<Rdc_parameterContext>(_ctx, getState());
  enterRule(_localctx, 14, CyanaMRParser::RuleRdc_parameter);
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
    setState(241);
    match(CyanaMRParser::Integer);
    setState(242);
    number();
    setState(243);
    number();
    setState(244);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 240518168580) != 0))) {
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

//----------------- Rdc_restraintContext ------------------------------------------------------------------

CyanaMRParser::Rdc_restraintContext::Rdc_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Rdc_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Rdc_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Rdc_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Rdc_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Rdc_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Rdc_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Rdc_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Rdc_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleRdc_restraint;
}


std::any CyanaMRParser::Rdc_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitRdc_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Rdc_restraintContext* CyanaMRParser::rdc_restraint() {
  Rdc_restraintContext *_localctx = _tracker.createInstance<Rdc_restraintContext>(_ctx, getState());
  enterRule(_localctx, 16, CyanaMRParser::RuleRdc_restraint);

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
    gen_res_num();
    setState(247);
    gen_simple_name();
    setState(248);
    gen_simple_name();
    setState(249);
    gen_res_num();
    setState(250);
    gen_simple_name();
    setState(251);
    gen_simple_name();
    setState(252);
    number();
    setState(253);
    number();
    setState(254);
    number();
    setState(255);
    match(CyanaMRParser::Integer);
    setState(257);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx)) {
    case 1: {
      setState(256);
      number();
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

//----------------- Pcs_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Pcs_restraintsContext::Pcs_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Pcs_parameterContext *> CyanaMRParser::Pcs_restraintsContext::pcs_parameter() {
  return getRuleContexts<CyanaMRParser::Pcs_parameterContext>();
}

CyanaMRParser::Pcs_parameterContext* CyanaMRParser::Pcs_restraintsContext::pcs_parameter(size_t i) {
  return getRuleContext<CyanaMRParser::Pcs_parameterContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Pcs_restraintsContext::Orientation_header() {
  return getTokens(CyanaMRParser::Orientation_header);
}

tree::TerminalNode* CyanaMRParser::Pcs_restraintsContext::Orientation_header(size_t i) {
  return getToken(CyanaMRParser::Orientation_header, i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Pcs_restraintsContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Pcs_restraintsContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::Pcs_restraintContext *> CyanaMRParser::Pcs_restraintsContext::pcs_restraint() {
  return getRuleContexts<CyanaMRParser::Pcs_restraintContext>();
}

CyanaMRParser::Pcs_restraintContext* CyanaMRParser::Pcs_restraintsContext::pcs_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Pcs_restraintContext>(i);
}


size_t CyanaMRParser::Pcs_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RulePcs_restraints;
}


std::any CyanaMRParser::Pcs_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitPcs_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Pcs_restraintsContext* CyanaMRParser::pcs_restraints() {
  Pcs_restraintsContext *_localctx = _tracker.createInstance<Pcs_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 18, CyanaMRParser::RulePcs_restraints);

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
    setState(260); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(259);
              pcs_parameter();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(262); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(267); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(267);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Orientation_header: {
                  setState(264);
                  match(CyanaMRParser::Orientation_header);
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(265);
                  comment();
                  break;
                }

                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(266);
                  pcs_restraint();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(269); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 20, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pcs_parameterContext ------------------------------------------------------------------

CyanaMRParser::Pcs_parameterContext::Pcs_parameterContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> CyanaMRParser::Pcs_parameterContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Pcs_parameterContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Pcs_parameterContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Pcs_parameterContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Pcs_parameterContext::Capital_integer() {
  return getToken(CyanaMRParser::Capital_integer, 0);
}

tree::TerminalNode* CyanaMRParser::Pcs_parameterContext::Integer_capital() {
  return getToken(CyanaMRParser::Integer_capital, 0);
}

tree::TerminalNode* CyanaMRParser::Pcs_parameterContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}


size_t CyanaMRParser::Pcs_parameterContext::getRuleIndex() const {
  return CyanaMRParser::RulePcs_parameter;
}


std::any CyanaMRParser::Pcs_parameterContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitPcs_parameter(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Pcs_parameterContext* CyanaMRParser::pcs_parameter() {
  Pcs_parameterContext *_localctx = _tracker.createInstance<Pcs_parameterContext>(_ctx, getState());
  enterRule(_localctx, 20, CyanaMRParser::RulePcs_parameter);
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
    setState(271);
    match(CyanaMRParser::Integer);
    setState(272);
    number();
    setState(273);
    number();
    setState(274);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 240518168580) != 0))) {
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

//----------------- Pcs_restraintContext ------------------------------------------------------------------

CyanaMRParser::Pcs_restraintContext::Pcs_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Pcs_restraintContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Pcs_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Pcs_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Pcs_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Pcs_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Pcs_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Pcs_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RulePcs_restraint;
}


std::any CyanaMRParser::Pcs_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitPcs_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Pcs_restraintContext* CyanaMRParser::pcs_restraint() {
  Pcs_restraintContext *_localctx = _tracker.createInstance<Pcs_restraintContext>(_ctx, getState());
  enterRule(_localctx, 22, CyanaMRParser::RulePcs_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(276);
    gen_res_num();
    setState(277);
    gen_simple_name();
    setState(278);
    gen_simple_name();
    setState(279);
    number();
    setState(280);
    number();
    setState(281);
    number();
    setState(282);
    match(CyanaMRParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixres_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Fixres_distance_restraintsContext::Fixres_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Fixres_distance_restraintContext *> CyanaMRParser::Fixres_distance_restraintsContext::fixres_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Fixres_distance_restraintContext>();
}

CyanaMRParser::Fixres_distance_restraintContext* CyanaMRParser::Fixres_distance_restraintsContext::fixres_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Fixres_distance_restraintContext>(i);
}


size_t CyanaMRParser::Fixres_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixres_distance_restraints;
}


std::any CyanaMRParser::Fixres_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixres_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixres_distance_restraintsContext* CyanaMRParser::fixres_distance_restraints() {
  Fixres_distance_restraintsContext *_localctx = _tracker.createInstance<Fixres_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 24, CyanaMRParser::RuleFixres_distance_restraints);

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
    setState(285); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(284);
              fixres_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(287); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 21, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixres_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Fixres_distance_restraintContext::Fixres_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Fixres_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Fixres_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Fixres_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Fixres_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Fixres_distance_restraintContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Fixres_distance_restraintContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Fixres_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Fixres_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Fixres_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixres_distance_restraint;
}


std::any CyanaMRParser::Fixres_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixres_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixres_distance_restraintContext* CyanaMRParser::fixres_distance_restraint() {
  Fixres_distance_restraintContext *_localctx = _tracker.createInstance<Fixres_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 26, CyanaMRParser::RuleFixres_distance_restraint);

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
    setState(289);
    gen_res_num();
    setState(290);
    gen_simple_name();
    setState(292);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 22, _ctx)) {
    case 1: {
      setState(291);
      comment();
      break;
    }

    default:
      break;
    }
    setState(301); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(301);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(294);
                  gen_simple_name();
                  setState(295);
                  gen_res_num();
                  setState(296);
                  gen_simple_name();
                  setState(297);
                  gen_simple_name();
                  setState(298);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(300);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(303); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 24, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixresw_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Fixresw_distance_restraintsContext::Fixresw_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Fixresw_distance_restraintContext *> CyanaMRParser::Fixresw_distance_restraintsContext::fixresw_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Fixresw_distance_restraintContext>();
}

CyanaMRParser::Fixresw_distance_restraintContext* CyanaMRParser::Fixresw_distance_restraintsContext::fixresw_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Fixresw_distance_restraintContext>(i);
}


size_t CyanaMRParser::Fixresw_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixresw_distance_restraints;
}


std::any CyanaMRParser::Fixresw_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixresw_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixresw_distance_restraintsContext* CyanaMRParser::fixresw_distance_restraints() {
  Fixresw_distance_restraintsContext *_localctx = _tracker.createInstance<Fixresw_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 28, CyanaMRParser::RuleFixresw_distance_restraints);

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
    setState(306); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(305);
              fixresw_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(308); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 25, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixresw_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Fixresw_distance_restraintContext::Fixresw_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Fixresw_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Fixresw_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Fixresw_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Fixresw_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Fixresw_distance_restraintContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Fixresw_distance_restraintContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Fixresw_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Fixresw_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Fixresw_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixresw_distance_restraint;
}


std::any CyanaMRParser::Fixresw_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixresw_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixresw_distance_restraintContext* CyanaMRParser::fixresw_distance_restraint() {
  Fixresw_distance_restraintContext *_localctx = _tracker.createInstance<Fixresw_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 30, CyanaMRParser::RuleFixresw_distance_restraint);

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
    setState(310);
    gen_res_num();
    setState(311);
    gen_simple_name();
    setState(313);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 26, _ctx)) {
    case 1: {
      setState(312);
      comment();
      break;
    }

    default:
      break;
    }
    setState(323); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(323);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(315);
                  gen_simple_name();
                  setState(316);
                  gen_res_num();
                  setState(317);
                  gen_simple_name();
                  setState(318);
                  gen_simple_name();
                  setState(319);
                  number();
                  setState(320);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(322);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(325); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 28, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixresw2_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Fixresw2_distance_restraintsContext::Fixresw2_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Fixresw2_distance_restraintContext *> CyanaMRParser::Fixresw2_distance_restraintsContext::fixresw2_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Fixresw2_distance_restraintContext>();
}

CyanaMRParser::Fixresw2_distance_restraintContext* CyanaMRParser::Fixresw2_distance_restraintsContext::fixresw2_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Fixresw2_distance_restraintContext>(i);
}


size_t CyanaMRParser::Fixresw2_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixresw2_distance_restraints;
}


std::any CyanaMRParser::Fixresw2_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixresw2_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixresw2_distance_restraintsContext* CyanaMRParser::fixresw2_distance_restraints() {
  Fixresw2_distance_restraintsContext *_localctx = _tracker.createInstance<Fixresw2_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 32, CyanaMRParser::RuleFixresw2_distance_restraints);

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
    setState(328); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(327);
              fixresw2_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(330); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 29, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixresw2_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Fixresw2_distance_restraintContext::Fixresw2_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Fixresw2_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Fixresw2_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Fixresw2_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Fixresw2_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Fixresw2_distance_restraintContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Fixresw2_distance_restraintContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Fixresw2_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Fixresw2_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Fixresw2_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixresw2_distance_restraint;
}


std::any CyanaMRParser::Fixresw2_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixresw2_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixresw2_distance_restraintContext* CyanaMRParser::fixresw2_distance_restraint() {
  Fixresw2_distance_restraintContext *_localctx = _tracker.createInstance<Fixresw2_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 34, CyanaMRParser::RuleFixresw2_distance_restraint);

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
    setState(332);
    gen_res_num();
    setState(333);
    gen_simple_name();
    setState(335);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 30, _ctx)) {
    case 1: {
      setState(334);
      comment();
      break;
    }

    default:
      break;
    }
    setState(346); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(346);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(337);
                  gen_simple_name();
                  setState(338);
                  gen_res_num();
                  setState(339);
                  gen_simple_name();
                  setState(340);
                  gen_simple_name();
                  setState(341);
                  number();
                  setState(342);
                  number();
                  setState(343);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(345);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(348); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 32, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixatm_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Fixatm_distance_restraintsContext::Fixatm_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Fixatm_distance_restraintContext *> CyanaMRParser::Fixatm_distance_restraintsContext::fixatm_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Fixatm_distance_restraintContext>();
}

CyanaMRParser::Fixatm_distance_restraintContext* CyanaMRParser::Fixatm_distance_restraintsContext::fixatm_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Fixatm_distance_restraintContext>(i);
}


size_t CyanaMRParser::Fixatm_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixatm_distance_restraints;
}


std::any CyanaMRParser::Fixatm_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixatm_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixatm_distance_restraintsContext* CyanaMRParser::fixatm_distance_restraints() {
  Fixatm_distance_restraintsContext *_localctx = _tracker.createInstance<Fixatm_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 36, CyanaMRParser::RuleFixatm_distance_restraints);

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
    setState(351); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(350);
              fixatm_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(353); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 33, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixatm_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Fixatm_distance_restraintContext::Fixatm_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Fixatm_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Fixatm_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Fixatm_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Fixatm_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Fixatm_distance_restraintContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Fixatm_distance_restraintContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Fixatm_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Fixatm_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Fixatm_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixatm_distance_restraint;
}


std::any CyanaMRParser::Fixatm_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixatm_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixatm_distance_restraintContext* CyanaMRParser::fixatm_distance_restraint() {
  Fixatm_distance_restraintContext *_localctx = _tracker.createInstance<Fixatm_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 38, CyanaMRParser::RuleFixatm_distance_restraint);

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
    setState(355);
    gen_res_num();
    setState(356);
    gen_simple_name();
    setState(357);
    gen_simple_name();
    setState(359);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 34, _ctx)) {
    case 1: {
      setState(358);
      comment();
      break;
    }

    default:
      break;
    }
    setState(367); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(367);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(361);
                  gen_res_num();
                  setState(362);
                  gen_simple_name();
                  setState(363);
                  gen_simple_name();
                  setState(364);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(366);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(369); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 36, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixatmw_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Fixatmw_distance_restraintsContext::Fixatmw_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Fixatmw_distance_restraintContext *> CyanaMRParser::Fixatmw_distance_restraintsContext::fixatmw_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Fixatmw_distance_restraintContext>();
}

CyanaMRParser::Fixatmw_distance_restraintContext* CyanaMRParser::Fixatmw_distance_restraintsContext::fixatmw_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Fixatmw_distance_restraintContext>(i);
}


size_t CyanaMRParser::Fixatmw_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixatmw_distance_restraints;
}


std::any CyanaMRParser::Fixatmw_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixatmw_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixatmw_distance_restraintsContext* CyanaMRParser::fixatmw_distance_restraints() {
  Fixatmw_distance_restraintsContext *_localctx = _tracker.createInstance<Fixatmw_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 40, CyanaMRParser::RuleFixatmw_distance_restraints);

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
    setState(372); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(371);
              fixatmw_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(374); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 37, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixatmw_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Fixatmw_distance_restraintContext::Fixatmw_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Fixatmw_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Fixatmw_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Fixatmw_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Fixatmw_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Fixatmw_distance_restraintContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Fixatmw_distance_restraintContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Fixatmw_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Fixatmw_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Fixatmw_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixatmw_distance_restraint;
}


std::any CyanaMRParser::Fixatmw_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixatmw_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixatmw_distance_restraintContext* CyanaMRParser::fixatmw_distance_restraint() {
  Fixatmw_distance_restraintContext *_localctx = _tracker.createInstance<Fixatmw_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 42, CyanaMRParser::RuleFixatmw_distance_restraint);

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
    setState(376);
    gen_res_num();
    setState(377);
    gen_simple_name();
    setState(378);
    gen_simple_name();
    setState(380);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 38, _ctx)) {
    case 1: {
      setState(379);
      comment();
      break;
    }

    default:
      break;
    }
    setState(389); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(389);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(382);
                  gen_res_num();
                  setState(383);
                  gen_simple_name();
                  setState(384);
                  gen_simple_name();
                  setState(385);
                  number();
                  setState(386);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(388);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(391); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 40, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixatmw2_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Fixatmw2_distance_restraintsContext::Fixatmw2_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Fixatmw2_distance_restraintContext *> CyanaMRParser::Fixatmw2_distance_restraintsContext::fixatmw2_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Fixatmw2_distance_restraintContext>();
}

CyanaMRParser::Fixatmw2_distance_restraintContext* CyanaMRParser::Fixatmw2_distance_restraintsContext::fixatmw2_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Fixatmw2_distance_restraintContext>(i);
}


size_t CyanaMRParser::Fixatmw2_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixatmw2_distance_restraints;
}


std::any CyanaMRParser::Fixatmw2_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixatmw2_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixatmw2_distance_restraintsContext* CyanaMRParser::fixatmw2_distance_restraints() {
  Fixatmw2_distance_restraintsContext *_localctx = _tracker.createInstance<Fixatmw2_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 44, CyanaMRParser::RuleFixatmw2_distance_restraints);

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
    setState(394); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(393);
              fixatmw2_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(396); 
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

//----------------- Fixatmw2_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Fixatmw2_distance_restraintContext::Fixatmw2_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Fixatmw2_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Fixatmw2_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Fixatmw2_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Fixatmw2_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Fixatmw2_distance_restraintContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Fixatmw2_distance_restraintContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Fixatmw2_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Fixatmw2_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Fixatmw2_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixatmw2_distance_restraint;
}


std::any CyanaMRParser::Fixatmw2_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixatmw2_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixatmw2_distance_restraintContext* CyanaMRParser::fixatmw2_distance_restraint() {
  Fixatmw2_distance_restraintContext *_localctx = _tracker.createInstance<Fixatmw2_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 46, CyanaMRParser::RuleFixatmw2_distance_restraint);

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
    setState(398);
    gen_res_num();
    setState(399);
    gen_simple_name();
    setState(400);
    gen_simple_name();
    setState(402);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 42, _ctx)) {
    case 1: {
      setState(401);
      comment();
      break;
    }

    default:
      break;
    }
    setState(412); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(412);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(404);
                  gen_res_num();
                  setState(405);
                  gen_simple_name();
                  setState(406);
                  gen_simple_name();
                  setState(407);
                  number();
                  setState(408);
                  number();
                  setState(409);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(411);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(414); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 44, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Diana_distance_restraintsContext::Diana_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Diana_distance_restraintContext *> CyanaMRParser::Diana_distance_restraintsContext::diana_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Diana_distance_restraintContext>();
}

CyanaMRParser::Diana_distance_restraintContext* CyanaMRParser::Diana_distance_restraintsContext::diana_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_distance_restraintContext>(i);
}


size_t CyanaMRParser::Diana_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_distance_restraints;
}


std::any CyanaMRParser::Diana_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_distance_restraintsContext* CyanaMRParser::diana_distance_restraints() {
  Diana_distance_restraintsContext *_localctx = _tracker.createInstance<Diana_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 48, CyanaMRParser::RuleDiana_distance_restraints);

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
    setState(417); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(416);
              diana_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(419); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 45, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Diana_distance_restraintContext::Diana_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Diana_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Diana_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Diana_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Diana_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Diana_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Diana_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_distance_restraintContext::NoeUpp() {
  return getToken(CyanaMRParser::NoeUpp, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_distance_restraintContext::NoeLow() {
  return getToken(CyanaMRParser::NoeLow, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_distance_restraintContext::NoeUpLo() {
  return getToken(CyanaMRParser::NoeUpLo, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_distance_restraintContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_distance_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Diana_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_distance_restraint;
}


std::any CyanaMRParser::Diana_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_distance_restraintContext* CyanaMRParser::diana_distance_restraint() {
  Diana_distance_restraintContext *_localctx = _tracker.createInstance<Diana_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 50, CyanaMRParser::RuleDiana_distance_restraint);
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
    setState(421);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 3584) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(422);
    gen_simple_name();
    setState(423);
    gen_res_num();
    setState(424);
    gen_simple_name();
    setState(425);
    gen_simple_name();
    setState(426);
    gen_res_num();
    setState(427);
    gen_simple_name();
    setState(428);
    number();
    setState(430);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 46, _ctx)) {
    case 1: {
      setState(429);
      number();
      break;
    }

    default:
      break;
    }
    setState(438);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 47, _ctx)) {
    case 1: {
      setState(432);
      gen_simple_name();
      setState(433);
      gen_simple_name();
      setState(434);
      gen_res_num();
      setState(435);
      gen_simple_name();
      setState(436);
      number();
      break;
    }

    default:
      break;
    }
    setState(441);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 48, _ctx)) {
    case 1: {
      setState(440);
      match(CyanaMRParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(444);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 49, _ctx)) {
    case 1: {
      setState(443);
      match(CyanaMRParser::Integer);
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

//----------------- Diana_ssbond_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Diana_ssbond_restraintsContext::Diana_ssbond_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Diana_ssbond_restraintContext *> CyanaMRParser::Diana_ssbond_restraintsContext::diana_ssbond_restraint() {
  return getRuleContexts<CyanaMRParser::Diana_ssbond_restraintContext>();
}

CyanaMRParser::Diana_ssbond_restraintContext* CyanaMRParser::Diana_ssbond_restraintsContext::diana_ssbond_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_ssbond_restraintContext>(i);
}


size_t CyanaMRParser::Diana_ssbond_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_ssbond_restraints;
}


std::any CyanaMRParser::Diana_ssbond_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_ssbond_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_ssbond_restraintsContext* CyanaMRParser::diana_ssbond_restraints() {
  Diana_ssbond_restraintsContext *_localctx = _tracker.createInstance<Diana_ssbond_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 52, CyanaMRParser::RuleDiana_ssbond_restraints);

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
    setState(447); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(446);
              diana_ssbond_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(449); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 50, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_ssbond_restraintContext ------------------------------------------------------------------

CyanaMRParser::Diana_ssbond_restraintContext::Diana_ssbond_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Diana_ssbond_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Diana_ssbond_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Diana_ssbond_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Diana_ssbond_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Diana_ssbond_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Diana_ssbond_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::SSUpp() {
  return getToken(CyanaMRParser::SSUpp, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::SSLow() {
  return getToken(CyanaMRParser::SSLow, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Diana_ssbond_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_ssbond_restraint;
}


std::any CyanaMRParser::Diana_ssbond_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_ssbond_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_ssbond_restraintContext* CyanaMRParser::diana_ssbond_restraint() {
  Diana_ssbond_restraintContext *_localctx = _tracker.createInstance<Diana_ssbond_restraintContext>(_ctx, getState());
  enterRule(_localctx, 54, CyanaMRParser::RuleDiana_ssbond_restraint);
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
    setState(451);
    _la = _input->LA(1);
    if (!(_la == CyanaMRParser::SSUpp

    || _la == CyanaMRParser::SSLow)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(452);
    gen_simple_name();
    setState(453);
    gen_res_num();
    setState(454);
    gen_simple_name();
    setState(455);
    gen_simple_name();
    setState(456);
    gen_res_num();
    setState(457);
    gen_simple_name();
    setState(458);
    number();
    setState(465);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 51, _ctx)) {
    case 1: {
      setState(459);
      gen_simple_name();
      setState(460);
      gen_simple_name();
      setState(461);
      gen_res_num();
      setState(462);
      gen_simple_name();
      setState(463);
      number();
      break;
    }

    default:
      break;
    }
    setState(468);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 52, _ctx)) {
    case 1: {
      setState(467);
      match(CyanaMRParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(471);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 53, _ctx)) {
    case 1: {
      setState(470);
      match(CyanaMRParser::Integer);
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

//----------------- Diana_hbond_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Diana_hbond_restraintsContext::Diana_hbond_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Diana_hbond_restraintContext *> CyanaMRParser::Diana_hbond_restraintsContext::diana_hbond_restraint() {
  return getRuleContexts<CyanaMRParser::Diana_hbond_restraintContext>();
}

CyanaMRParser::Diana_hbond_restraintContext* CyanaMRParser::Diana_hbond_restraintsContext::diana_hbond_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_hbond_restraintContext>(i);
}


size_t CyanaMRParser::Diana_hbond_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_hbond_restraints;
}


std::any CyanaMRParser::Diana_hbond_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_hbond_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_hbond_restraintsContext* CyanaMRParser::diana_hbond_restraints() {
  Diana_hbond_restraintsContext *_localctx = _tracker.createInstance<Diana_hbond_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 56, CyanaMRParser::RuleDiana_hbond_restraints);

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
    setState(474); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(473);
              diana_hbond_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(476); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 54, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_hbond_restraintContext ------------------------------------------------------------------

CyanaMRParser::Diana_hbond_restraintContext::Diana_hbond_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Diana_hbond_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Diana_hbond_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Diana_hbond_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Diana_hbond_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Diana_hbond_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Diana_hbond_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_hbond_restraintContext::HBUpp() {
  return getToken(CyanaMRParser::HBUpp, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_hbond_restraintContext::HBLow() {
  return getToken(CyanaMRParser::HBLow, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_hbond_restraintContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_hbond_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Diana_hbond_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_hbond_restraint;
}


std::any CyanaMRParser::Diana_hbond_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_hbond_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_hbond_restraintContext* CyanaMRParser::diana_hbond_restraint() {
  Diana_hbond_restraintContext *_localctx = _tracker.createInstance<Diana_hbond_restraintContext>(_ctx, getState());
  enterRule(_localctx, 58, CyanaMRParser::RuleDiana_hbond_restraint);
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
    setState(478);
    _la = _input->LA(1);
    if (!(_la == CyanaMRParser::HBUpp

    || _la == CyanaMRParser::HBLow)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(479);
    gen_simple_name();
    setState(480);
    gen_res_num();
    setState(481);
    gen_simple_name();
    setState(482);
    gen_simple_name();
    setState(483);
    gen_res_num();
    setState(484);
    gen_simple_name();
    setState(485);
    number();
    setState(492);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 55, _ctx)) {
    case 1: {
      setState(486);
      gen_simple_name();
      setState(487);
      gen_simple_name();
      setState(488);
      gen_res_num();
      setState(489);
      gen_simple_name();
      setState(490);
      number();
      break;
    }

    default:
      break;
    }
    setState(495);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 56, _ctx)) {
    case 1: {
      setState(494);
      match(CyanaMRParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(498);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 57, _ctx)) {
    case 1: {
      setState(497);
      match(CyanaMRParser::Integer);
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

//----------------- Diana_torsion_angle_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Diana_torsion_angle_restraintsContext::Diana_torsion_angle_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Diana_torsion_angle_restraintContext *> CyanaMRParser::Diana_torsion_angle_restraintsContext::diana_torsion_angle_restraint() {
  return getRuleContexts<CyanaMRParser::Diana_torsion_angle_restraintContext>();
}

CyanaMRParser::Diana_torsion_angle_restraintContext* CyanaMRParser::Diana_torsion_angle_restraintsContext::diana_torsion_angle_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_torsion_angle_restraintContext>(i);
}


size_t CyanaMRParser::Diana_torsion_angle_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_torsion_angle_restraints;
}


std::any CyanaMRParser::Diana_torsion_angle_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_torsion_angle_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_torsion_angle_restraintsContext* CyanaMRParser::diana_torsion_angle_restraints() {
  Diana_torsion_angle_restraintsContext *_localctx = _tracker.createInstance<Diana_torsion_angle_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 60, CyanaMRParser::RuleDiana_torsion_angle_restraints);

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
    setState(501); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(500);
              diana_torsion_angle_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(503); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 58, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_torsion_angle_restraintContext ------------------------------------------------------------------

CyanaMRParser::Diana_torsion_angle_restraintContext::Diana_torsion_angle_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Diana_torsion_angle_restraintContext::Angle() {
  return getToken(CyanaMRParser::Angle, 0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Diana_torsion_angle_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Diana_torsion_angle_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Diana_torsion_angle_restraintContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Diana_torsion_angle_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Diana_torsion_angle_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_torsion_angle_restraintContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_torsion_angle_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Diana_torsion_angle_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_torsion_angle_restraint;
}


std::any CyanaMRParser::Diana_torsion_angle_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_torsion_angle_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_torsion_angle_restraintContext* CyanaMRParser::diana_torsion_angle_restraint() {
  Diana_torsion_angle_restraintContext *_localctx = _tracker.createInstance<Diana_torsion_angle_restraintContext>(_ctx, getState());
  enterRule(_localctx, 62, CyanaMRParser::RuleDiana_torsion_angle_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(505);
    match(CyanaMRParser::Angle);
    setState(506);
    gen_simple_name();
    setState(507);
    gen_res_num();
    setState(508);
    gen_simple_name();
    setState(509);
    number();
    setState(510);
    number();
    setState(515);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 59, _ctx)) {
    case 1: {
      setState(511);
      gen_simple_name();
      setState(512);
      number();
      setState(513);
      number();
      break;
    }

    default:
      break;
    }
    setState(518);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 60, _ctx)) {
    case 1: {
      setState(517);
      match(CyanaMRParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(521);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 61, _ctx)) {
    case 1: {
      setState(520);
      match(CyanaMRParser::Integer);
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

//----------------- Diana_coupling_constant_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Diana_coupling_constant_restraintsContext::Diana_coupling_constant_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Diana_coupling_constant_restraintContext *> CyanaMRParser::Diana_coupling_constant_restraintsContext::diana_coupling_constant_restraint() {
  return getRuleContexts<CyanaMRParser::Diana_coupling_constant_restraintContext>();
}

CyanaMRParser::Diana_coupling_constant_restraintContext* CyanaMRParser::Diana_coupling_constant_restraintsContext::diana_coupling_constant_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_coupling_constant_restraintContext>(i);
}


size_t CyanaMRParser::Diana_coupling_constant_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_coupling_constant_restraints;
}


std::any CyanaMRParser::Diana_coupling_constant_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_coupling_constant_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_coupling_constant_restraintsContext* CyanaMRParser::diana_coupling_constant_restraints() {
  Diana_coupling_constant_restraintsContext *_localctx = _tracker.createInstance<Diana_coupling_constant_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 64, CyanaMRParser::RuleDiana_coupling_constant_restraints);

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
    setState(524); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(523);
              diana_coupling_constant_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(526); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 62, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_coupling_constant_restraintContext ------------------------------------------------------------------

CyanaMRParser::Diana_coupling_constant_restraintContext::Diana_coupling_constant_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Diana_coupling_constant_restraintContext::Jcoupl() {
  return getToken(CyanaMRParser::Jcoupl, 0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Diana_coupling_constant_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Diana_coupling_constant_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Diana_coupling_constant_restraintContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Diana_coupling_constant_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Diana_coupling_constant_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_coupling_constant_restraintContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_coupling_constant_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Diana_coupling_constant_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_coupling_constant_restraint;
}


std::any CyanaMRParser::Diana_coupling_constant_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_coupling_constant_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_coupling_constant_restraintContext* CyanaMRParser::diana_coupling_constant_restraint() {
  Diana_coupling_constant_restraintContext *_localctx = _tracker.createInstance<Diana_coupling_constant_restraintContext>(_ctx, getState());
  enterRule(_localctx, 66, CyanaMRParser::RuleDiana_coupling_constant_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(528);
    match(CyanaMRParser::Jcoupl);
    setState(529);
    gen_simple_name();
    setState(530);
    gen_res_num();
    setState(531);
    gen_simple_name();
    setState(532);
    gen_simple_name();
    setState(533);
    number();
    setState(535);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 63, _ctx)) {
    case 1: {
      setState(534);
      number();
      break;
    }

    default:
      break;
    }
    setState(543);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 65, _ctx)) {
    case 1: {
      setState(537);
      gen_simple_name();
      setState(538);
      gen_simple_name();
      setState(539);
      number();
      setState(541);
      _errHandler->sync(this);

      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 64, _ctx)) {
      case 1: {
        setState(540);
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
    setState(546);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 66, _ctx)) {
    case 1: {
      setState(545);
      match(CyanaMRParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(549);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 67, _ctx)) {
    case 1: {
      setState(548);
      match(CyanaMRParser::Integer);
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

//----------------- Diana_stereoassign_macroContext ------------------------------------------------------------------

CyanaMRParser::Diana_stereoassign_macroContext::Diana_stereoassign_macroContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Diana_stereoassign_macroContext::Stereo() {
  return getToken(CyanaMRParser::Stereo, 0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Diana_stereoassign_macroContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Diana_stereoassign_macroContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Diana_stereoassign_macroContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

tree::TerminalNode* CyanaMRParser::Diana_stereoassign_macroContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Diana_stereoassign_macroContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_stereoassign_macro;
}


std::any CyanaMRParser::Diana_stereoassign_macroContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_stereoassign_macro(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_stereoassign_macroContext* CyanaMRParser::diana_stereoassign_macro() {
  Diana_stereoassign_macroContext *_localctx = _tracker.createInstance<Diana_stereoassign_macroContext>(_ctx, getState());
  enterRule(_localctx, 68, CyanaMRParser::RuleDiana_stereoassign_macro);

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
    setState(551);
    match(CyanaMRParser::Stereo);
    setState(552);
    gen_simple_name();
    setState(553);
    gen_res_num();
    setState(555); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(554);
              gen_simple_name();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(557); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 68, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(560);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 69, _ctx)) {
    case 1: {
      setState(559);
      match(CyanaMRParser::Integer);
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

//----------------- Diana_chemical_shiftsContext ------------------------------------------------------------------

CyanaMRParser::Diana_chemical_shiftsContext::Diana_chemical_shiftsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Diana_chemical_shiftContext *> CyanaMRParser::Diana_chemical_shiftsContext::diana_chemical_shift() {
  return getRuleContexts<CyanaMRParser::Diana_chemical_shiftContext>();
}

CyanaMRParser::Diana_chemical_shiftContext* CyanaMRParser::Diana_chemical_shiftsContext::diana_chemical_shift(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_chemical_shiftContext>(i);
}


size_t CyanaMRParser::Diana_chemical_shiftsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_chemical_shifts;
}


std::any CyanaMRParser::Diana_chemical_shiftsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_chemical_shifts(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_chemical_shiftsContext* CyanaMRParser::diana_chemical_shifts() {
  Diana_chemical_shiftsContext *_localctx = _tracker.createInstance<Diana_chemical_shiftsContext>(_ctx, getState());
  enterRule(_localctx, 70, CyanaMRParser::RuleDiana_chemical_shifts);

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
    setState(563); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(562);
              diana_chemical_shift();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(565); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 70, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_chemical_shiftContext ------------------------------------------------------------------

CyanaMRParser::Diana_chemical_shiftContext::Diana_chemical_shiftContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Diana_chemical_shiftContext::Shifts() {
  return getToken(CyanaMRParser::Shifts, 0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Diana_chemical_shiftContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Diana_chemical_shiftContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Diana_chemical_shiftContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Diana_chemical_shiftContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Diana_chemical_shiftContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_chemical_shiftContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_chemical_shiftContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Diana_chemical_shiftContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_chemical_shift;
}


std::any CyanaMRParser::Diana_chemical_shiftContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_chemical_shift(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_chemical_shiftContext* CyanaMRParser::diana_chemical_shift() {
  Diana_chemical_shiftContext *_localctx = _tracker.createInstance<Diana_chemical_shiftContext>(_ctx, getState());
  enterRule(_localctx, 72, CyanaMRParser::RuleDiana_chemical_shift);

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
    setState(567);
    match(CyanaMRParser::Shifts);
    setState(568);
    gen_simple_name();
    setState(569);
    gen_res_num();
    setState(570);
    gen_simple_name();
    setState(571);
    number();
    setState(577);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 71, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(572);
        gen_simple_name();
        setState(573);
        number(); 
      }
      setState(579);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 71, _ctx);
    }
    setState(581);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 72, _ctx)) {
    case 1: {
      setState(580);
      match(CyanaMRParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(584);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 73, _ctx)) {
    case 1: {
      setState(583);
      match(CyanaMRParser::Integer);
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

//----------------- Distance_w_chain_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Distance_w_chain_restraintsContext::Distance_w_chain_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Distance_w_chain_restraintContext *> CyanaMRParser::Distance_w_chain_restraintsContext::distance_w_chain_restraint() {
  return getRuleContexts<CyanaMRParser::Distance_w_chain_restraintContext>();
}

CyanaMRParser::Distance_w_chain_restraintContext* CyanaMRParser::Distance_w_chain_restraintsContext::distance_w_chain_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_w_chain_restraintContext>(i);
}


size_t CyanaMRParser::Distance_w_chain_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_w_chain_restraints;
}


std::any CyanaMRParser::Distance_w_chain_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_w_chain_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_w_chain_restraintsContext* CyanaMRParser::distance_w_chain_restraints() {
  Distance_w_chain_restraintsContext *_localctx = _tracker.createInstance<Distance_w_chain_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 74, CyanaMRParser::RuleDistance_w_chain_restraints);

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
    setState(587); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(586);
              distance_w_chain_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(589); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 74, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_w_chain_restraintContext ------------------------------------------------------------------

CyanaMRParser::Distance_w_chain_restraintContext::Distance_w_chain_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> CyanaMRParser::Distance_w_chain_restraintContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Distance_w_chain_restraintContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Distance_w_chain_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Distance_w_chain_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Distance_w_chain_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Distance_w_chain_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Distance_w_chain_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_w_chain_restraint;
}


std::any CyanaMRParser::Distance_w_chain_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_w_chain_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_w_chain_restraintContext* CyanaMRParser::distance_w_chain_restraint() {
  Distance_w_chain_restraintContext *_localctx = _tracker.createInstance<Distance_w_chain_restraintContext>(_ctx, getState());
  enterRule(_localctx, 76, CyanaMRParser::RuleDistance_w_chain_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(591);
    match(CyanaMRParser::Integer);
    setState(592);
    gen_simple_name();
    setState(593);
    gen_simple_name();
    setState(594);
    gen_simple_name();
    setState(595);
    match(CyanaMRParser::Integer);
    setState(596);
    gen_simple_name();
    setState(597);
    gen_simple_name();
    setState(598);
    gen_simple_name();
    setState(599);
    number();
    setState(601);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 75, _ctx)) {
    case 1: {
      setState(600);
      number();
      break;
    }

    default:
      break;
    }
    setState(604);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 76, _ctx)) {
    case 1: {
      setState(603);
      number();
      break;
    }

    default:
      break;
    }
    setState(607);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 77, _ctx)) {
    case 1: {
      setState(606);
      number();
      break;
    }

    default:
      break;
    }
    setState(610);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 78, _ctx)) {
    case 1: {
      setState(609);
      number();
      break;
    }

    default:
      break;
    }
    setState(613);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 79, _ctx)) {
    case 1: {
      setState(612);
      number();
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

//----------------- Distance_w_chain2_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Distance_w_chain2_restraintsContext::Distance_w_chain2_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Distance_w_chain2_restraintContext *> CyanaMRParser::Distance_w_chain2_restraintsContext::distance_w_chain2_restraint() {
  return getRuleContexts<CyanaMRParser::Distance_w_chain2_restraintContext>();
}

CyanaMRParser::Distance_w_chain2_restraintContext* CyanaMRParser::Distance_w_chain2_restraintsContext::distance_w_chain2_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_w_chain2_restraintContext>(i);
}


size_t CyanaMRParser::Distance_w_chain2_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_w_chain2_restraints;
}


std::any CyanaMRParser::Distance_w_chain2_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_w_chain2_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_w_chain2_restraintsContext* CyanaMRParser::distance_w_chain2_restraints() {
  Distance_w_chain2_restraintsContext *_localctx = _tracker.createInstance<Distance_w_chain2_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 78, CyanaMRParser::RuleDistance_w_chain2_restraints);

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
    setState(616); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(615);
              distance_w_chain2_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(618); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 80, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_w_chain2_restraintContext ------------------------------------------------------------------

CyanaMRParser::Distance_w_chain2_restraintContext::Distance_w_chain2_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Distance_w_chain2_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Distance_w_chain2_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Distance_w_chain2_restraintContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Distance_w_chain2_restraintContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Distance_w_chain2_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Distance_w_chain2_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Distance_w_chain2_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_w_chain2_restraint;
}


std::any CyanaMRParser::Distance_w_chain2_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_w_chain2_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_w_chain2_restraintContext* CyanaMRParser::distance_w_chain2_restraint() {
  Distance_w_chain2_restraintContext *_localctx = _tracker.createInstance<Distance_w_chain2_restraintContext>(_ctx, getState());
  enterRule(_localctx, 80, CyanaMRParser::RuleDistance_w_chain2_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(620);
    gen_simple_name();
    setState(621);
    match(CyanaMRParser::Integer);
    setState(622);
    gen_simple_name();
    setState(623);
    gen_simple_name();
    setState(624);
    gen_simple_name();
    setState(625);
    match(CyanaMRParser::Integer);
    setState(626);
    gen_simple_name();
    setState(627);
    gen_simple_name();
    setState(628);
    number();
    setState(630);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 81, _ctx)) {
    case 1: {
      setState(629);
      number();
      break;
    }

    default:
      break;
    }
    setState(633);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 82, _ctx)) {
    case 1: {
      setState(632);
      number();
      break;
    }

    default:
      break;
    }
    setState(636);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 83, _ctx)) {
    case 1: {
      setState(635);
      number();
      break;
    }

    default:
      break;
    }
    setState(639);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 84, _ctx)) {
    case 1: {
      setState(638);
      number();
      break;
    }

    default:
      break;
    }
    setState(642);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 85, _ctx)) {
    case 1: {
      setState(641);
      number();
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

//----------------- Distance_w_chain3_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Distance_w_chain3_restraintsContext::Distance_w_chain3_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Distance_w_chain3_restraintContext *> CyanaMRParser::Distance_w_chain3_restraintsContext::distance_w_chain3_restraint() {
  return getRuleContexts<CyanaMRParser::Distance_w_chain3_restraintContext>();
}

CyanaMRParser::Distance_w_chain3_restraintContext* CyanaMRParser::Distance_w_chain3_restraintsContext::distance_w_chain3_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_w_chain3_restraintContext>(i);
}


size_t CyanaMRParser::Distance_w_chain3_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_w_chain3_restraints;
}


std::any CyanaMRParser::Distance_w_chain3_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_w_chain3_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_w_chain3_restraintsContext* CyanaMRParser::distance_w_chain3_restraints() {
  Distance_w_chain3_restraintsContext *_localctx = _tracker.createInstance<Distance_w_chain3_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 82, CyanaMRParser::RuleDistance_w_chain3_restraints);

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
    setState(645); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(644);
              distance_w_chain3_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(647); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 86, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_w_chain3_restraintContext ------------------------------------------------------------------

CyanaMRParser::Distance_w_chain3_restraintContext::Distance_w_chain3_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Distance_w_chain3_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Distance_w_chain3_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Distance_w_chain3_restraintContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Distance_w_chain3_restraintContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Distance_w_chain3_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Distance_w_chain3_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Distance_w_chain3_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_w_chain3_restraint;
}


std::any CyanaMRParser::Distance_w_chain3_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_w_chain3_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_w_chain3_restraintContext* CyanaMRParser::distance_w_chain3_restraint() {
  Distance_w_chain3_restraintContext *_localctx = _tracker.createInstance<Distance_w_chain3_restraintContext>(_ctx, getState());
  enterRule(_localctx, 84, CyanaMRParser::RuleDistance_w_chain3_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(649);
    gen_simple_name();
    setState(650);
    gen_simple_name();
    setState(651);
    match(CyanaMRParser::Integer);
    setState(652);
    gen_simple_name();
    setState(653);
    gen_simple_name();
    setState(654);
    gen_simple_name();
    setState(655);
    match(CyanaMRParser::Integer);
    setState(656);
    gen_simple_name();
    setState(657);
    number();
    setState(659);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 87, _ctx)) {
    case 1: {
      setState(658);
      number();
      break;
    }

    default:
      break;
    }
    setState(662);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 88, _ctx)) {
    case 1: {
      setState(661);
      number();
      break;
    }

    default:
      break;
    }
    setState(665);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 89, _ctx)) {
    case 1: {
      setState(664);
      number();
      break;
    }

    default:
      break;
    }
    setState(668);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 90, _ctx)) {
    case 1: {
      setState(667);
      number();
      break;
    }

    default:
      break;
    }
    setState(671);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 91, _ctx)) {
    case 1: {
      setState(670);
      number();
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

//----------------- Torsion_angle_w_chain_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Torsion_angle_w_chain_restraintsContext::Torsion_angle_w_chain_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Torsion_angle_w_chain_restraintContext *> CyanaMRParser::Torsion_angle_w_chain_restraintsContext::torsion_angle_w_chain_restraint() {
  return getRuleContexts<CyanaMRParser::Torsion_angle_w_chain_restraintContext>();
}

CyanaMRParser::Torsion_angle_w_chain_restraintContext* CyanaMRParser::Torsion_angle_w_chain_restraintsContext::torsion_angle_w_chain_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Torsion_angle_w_chain_restraintContext>(i);
}


size_t CyanaMRParser::Torsion_angle_w_chain_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleTorsion_angle_w_chain_restraints;
}


std::any CyanaMRParser::Torsion_angle_w_chain_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitTorsion_angle_w_chain_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Torsion_angle_w_chain_restraintsContext* CyanaMRParser::torsion_angle_w_chain_restraints() {
  Torsion_angle_w_chain_restraintsContext *_localctx = _tracker.createInstance<Torsion_angle_w_chain_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 86, CyanaMRParser::RuleTorsion_angle_w_chain_restraints);

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
    setState(674); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(673);
              torsion_angle_w_chain_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(676); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 92, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Torsion_angle_w_chain_restraintContext ------------------------------------------------------------------

CyanaMRParser::Torsion_angle_w_chain_restraintContext::Torsion_angle_w_chain_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Torsion_angle_w_chain_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Torsion_angle_w_chain_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Torsion_angle_w_chain_restraintContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_w_chain_restraintContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Torsion_angle_w_chain_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Torsion_angle_w_chain_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_w_chain_restraintContext::Type() {
  return getToken(CyanaMRParser::Type, 0);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_w_chain_restraintContext::Equ_op() {
  return getToken(CyanaMRParser::Equ_op, 0);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_w_chain_restraintContext::Or() {
  return getToken(CyanaMRParser::Or, 0);
}


size_t CyanaMRParser::Torsion_angle_w_chain_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleTorsion_angle_w_chain_restraint;
}


std::any CyanaMRParser::Torsion_angle_w_chain_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitTorsion_angle_w_chain_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Torsion_angle_w_chain_restraintContext* CyanaMRParser::torsion_angle_w_chain_restraint() {
  Torsion_angle_w_chain_restraintContext *_localctx = _tracker.createInstance<Torsion_angle_w_chain_restraintContext>(_ctx, getState());
  enterRule(_localctx, 88, CyanaMRParser::RuleTorsion_angle_w_chain_restraint);
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
    setState(678);
    gen_simple_name();
    setState(679);
    match(CyanaMRParser::Integer);
    setState(680);
    gen_simple_name();
    setState(681);
    gen_simple_name();
    setState(682);
    number();
    setState(683);
    number();
    setState(685);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 93, _ctx)) {
    case 1: {
      setState(684);
      number();
      break;
    }

    default:
      break;
    }
    setState(690);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Type) {
      setState(687);
      match(CyanaMRParser::Type);
      setState(688);
      match(CyanaMRParser::Equ_op);
      setState(689);
      match(CyanaMRParser::Integer);
    }
    setState(693);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Or) {
      setState(692);
      match(CyanaMRParser::Or);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Cco_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Cco_restraintsContext::Cco_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Cco_restraintContext *> CyanaMRParser::Cco_restraintsContext::cco_restraint() {
  return getRuleContexts<CyanaMRParser::Cco_restraintContext>();
}

CyanaMRParser::Cco_restraintContext* CyanaMRParser::Cco_restraintsContext::cco_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Cco_restraintContext>(i);
}


size_t CyanaMRParser::Cco_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleCco_restraints;
}


std::any CyanaMRParser::Cco_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitCco_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Cco_restraintsContext* CyanaMRParser::cco_restraints() {
  Cco_restraintsContext *_localctx = _tracker.createInstance<Cco_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 90, CyanaMRParser::RuleCco_restraints);

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
    setState(696); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(695);
              cco_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(698); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 96, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Cco_restraintContext ------------------------------------------------------------------

CyanaMRParser::Cco_restraintContext::Cco_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Cco_restraintContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Cco_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Cco_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Cco_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Cco_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Cco_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleCco_restraint;
}


std::any CyanaMRParser::Cco_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitCco_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Cco_restraintContext* CyanaMRParser::cco_restraint() {
  Cco_restraintContext *_localctx = _tracker.createInstance<Cco_restraintContext>(_ctx, getState());
  enterRule(_localctx, 92, CyanaMRParser::RuleCco_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(700);
    gen_res_num();
    setState(701);
    gen_simple_name();
    setState(702);
    gen_simple_name();
    setState(703);
    gen_simple_name();
    setState(704);
    number();
    setState(706);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 97, _ctx)) {
    case 1: {
      setState(705);
      number();
      break;
    }

    default:
      break;
    }
    setState(709);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 98, _ctx)) {
    case 1: {
      setState(708);
      number();
      break;
    }

    default:
      break;
    }
    setState(712);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 99, _ctx)) {
    case 1: {
      setState(711);
      number();
      break;
    }

    default:
      break;
    }
    setState(715);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 100, _ctx)) {
    case 1: {
      setState(714);
      number();
      break;
    }

    default:
      break;
    }
    setState(718);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 101, _ctx)) {
    case 1: {
      setState(717);
      number();
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

//----------------- Ssbond_macroContext ------------------------------------------------------------------

CyanaMRParser::Ssbond_macroContext::Ssbond_macroContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Ssbond_macroContext::Ssbond() {
  return getToken(CyanaMRParser::Ssbond, 0);
}

tree::TerminalNode* CyanaMRParser::Ssbond_macroContext::Ssbond_resids() {
  return getToken(CyanaMRParser::Ssbond_resids, 0);
}


size_t CyanaMRParser::Ssbond_macroContext::getRuleIndex() const {
  return CyanaMRParser::RuleSsbond_macro;
}


std::any CyanaMRParser::Ssbond_macroContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitSsbond_macro(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Ssbond_macroContext* CyanaMRParser::ssbond_macro() {
  Ssbond_macroContext *_localctx = _tracker.createInstance<Ssbond_macroContext>(_ctx, getState());
  enterRule(_localctx, 94, CyanaMRParser::RuleSsbond_macro);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(720);
    match(CyanaMRParser::Ssbond);
    setState(721);
    match(CyanaMRParser::Ssbond_resids);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Hbond_macroContext ------------------------------------------------------------------

CyanaMRParser::Hbond_macroContext::Hbond_macroContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Hbond() {
  return getToken(CyanaMRParser::Hbond, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::RETURN_HB() {
  return getToken(CyanaMRParser::RETURN_HB, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Hbond_macroContext::Simple_name_HB() {
  return getTokens(CyanaMRParser::Simple_name_HB);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Simple_name_HB(size_t i) {
  return getToken(CyanaMRParser::Simple_name_HB, i);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Concat_atom_1() {
  return getToken(CyanaMRParser::Concat_atom_1, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Hbond_macroContext::Integer_HB() {
  return getTokens(CyanaMRParser::Integer_HB);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Integer_HB(size_t i) {
  return getToken(CyanaMRParser::Integer_HB, i);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Concat_res_1() {
  return getToken(CyanaMRParser::Concat_res_1, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Concat_atom_2() {
  return getToken(CyanaMRParser::Concat_atom_2, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Concat_res_2() {
  return getToken(CyanaMRParser::Concat_res_2, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Atom1() {
  return getToken(CyanaMRParser::Atom1, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Hbond_macroContext::Equ_op_HB() {
  return getTokens(CyanaMRParser::Equ_op_HB);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Equ_op_HB(size_t i) {
  return getToken(CyanaMRParser::Equ_op_HB, i);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Atom1_equ() {
  return getToken(CyanaMRParser::Atom1_equ, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Residue1() {
  return getToken(CyanaMRParser::Residue1, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Residue1_equ() {
  return getToken(CyanaMRParser::Residue1_equ, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Atom2() {
  return getToken(CyanaMRParser::Atom2, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Atom2_equ() {
  return getToken(CyanaMRParser::Atom2_equ, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Residue2() {
  return getToken(CyanaMRParser::Residue2, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Residue2_equ() {
  return getToken(CyanaMRParser::Residue2_equ, 0);
}


size_t CyanaMRParser::Hbond_macroContext::getRuleIndex() const {
  return CyanaMRParser::RuleHbond_macro;
}


std::any CyanaMRParser::Hbond_macroContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitHbond_macro(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Hbond_macroContext* CyanaMRParser::hbond_macro() {
  Hbond_macroContext *_localctx = _tracker.createInstance<Hbond_macroContext>(_ctx, getState());
  enterRule(_localctx, 96, CyanaMRParser::RuleHbond_macro);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(723);
    match(CyanaMRParser::Hbond);
    setState(731);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Atom1:
      case CyanaMRParser::Atom1_equ:
      case CyanaMRParser::Simple_name_HB: {
        setState(727);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CyanaMRParser::Atom1: {
            setState(724);
            match(CyanaMRParser::Atom1);
            setState(725);
            match(CyanaMRParser::Equ_op_HB);
            break;
          }

          case CyanaMRParser::Atom1_equ: {
            setState(726);
            match(CyanaMRParser::Atom1_equ);
            break;
          }

          case CyanaMRParser::Simple_name_HB: {
            break;
          }

        default:
          break;
        }
        setState(729);
        match(CyanaMRParser::Simple_name_HB);
        break;
      }

      case CyanaMRParser::Concat_atom_1: {
        setState(730);
        match(CyanaMRParser::Concat_atom_1);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(740);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Residue1:
      case CyanaMRParser::Residue1_equ:
      case CyanaMRParser::Integer_HB: {
        setState(736);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CyanaMRParser::Residue1: {
            setState(733);
            match(CyanaMRParser::Residue1);
            setState(734);
            match(CyanaMRParser::Equ_op_HB);
            break;
          }

          case CyanaMRParser::Residue1_equ: {
            setState(735);
            match(CyanaMRParser::Residue1_equ);
            break;
          }

          case CyanaMRParser::Integer_HB: {
            break;
          }

        default:
          break;
        }
        setState(738);
        match(CyanaMRParser::Integer_HB);
        break;
      }

      case CyanaMRParser::Concat_res_1: {
        setState(739);
        match(CyanaMRParser::Concat_res_1);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(749);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Atom2:
      case CyanaMRParser::Atom2_equ:
      case CyanaMRParser::Simple_name_HB: {
        setState(745);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CyanaMRParser::Atom2: {
            setState(742);
            match(CyanaMRParser::Atom2);
            setState(743);
            match(CyanaMRParser::Equ_op_HB);
            break;
          }

          case CyanaMRParser::Atom2_equ: {
            setState(744);
            match(CyanaMRParser::Atom2_equ);
            break;
          }

          case CyanaMRParser::Simple_name_HB: {
            break;
          }

        default:
          break;
        }
        setState(747);
        match(CyanaMRParser::Simple_name_HB);
        break;
      }

      case CyanaMRParser::Concat_atom_2: {
        setState(748);
        match(CyanaMRParser::Concat_atom_2);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(758);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Residue2:
      case CyanaMRParser::Residue2_equ:
      case CyanaMRParser::Integer_HB: {
        setState(754);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CyanaMRParser::Residue2: {
            setState(751);
            match(CyanaMRParser::Residue2);
            setState(752);
            match(CyanaMRParser::Equ_op_HB);
            break;
          }

          case CyanaMRParser::Residue2_equ: {
            setState(753);
            match(CyanaMRParser::Residue2_equ);
            break;
          }

          case CyanaMRParser::Integer_HB: {
            break;
          }

        default:
          break;
        }
        setState(756);
        match(CyanaMRParser::Integer_HB);
        break;
      }

      case CyanaMRParser::Concat_res_2: {
        setState(757);
        match(CyanaMRParser::Concat_res_2);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(760);
    match(CyanaMRParser::RETURN_HB);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Link_statementContext ------------------------------------------------------------------

CyanaMRParser::Link_statementContext::Link_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Link_statementContext::Link() {
  return getToken(CyanaMRParser::Link, 0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Link_statementContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Link_statementContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Link_statementContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Link_statementContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}


size_t CyanaMRParser::Link_statementContext::getRuleIndex() const {
  return CyanaMRParser::RuleLink_statement;
}


std::any CyanaMRParser::Link_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitLink_statement(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Link_statementContext* CyanaMRParser::link_statement() {
  Link_statementContext *_localctx = _tracker.createInstance<Link_statementContext>(_ctx, getState());
  enterRule(_localctx, 98, CyanaMRParser::RuleLink_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(762);
    match(CyanaMRParser::Link);
    setState(763);
    gen_simple_name();
    setState(764);
    gen_res_num();
    setState(765);
    gen_simple_name();
    setState(766);
    gen_res_num();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Stereoassign_macroContext ------------------------------------------------------------------

CyanaMRParser::Stereoassign_macroContext::Stereoassign_macroContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Stereoassign_macroContext::Atom_stereo() {
  return getToken(CyanaMRParser::Atom_stereo, 0);
}

tree::TerminalNode* CyanaMRParser::Stereoassign_macroContext::Double_quote_string() {
  return getToken(CyanaMRParser::Double_quote_string, 0);
}

tree::TerminalNode* CyanaMRParser::Stereoassign_macroContext::RETURN_PR() {
  return getToken(CyanaMRParser::RETURN_PR, 0);
}


size_t CyanaMRParser::Stereoassign_macroContext::getRuleIndex() const {
  return CyanaMRParser::RuleStereoassign_macro;
}


std::any CyanaMRParser::Stereoassign_macroContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitStereoassign_macro(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Stereoassign_macroContext* CyanaMRParser::stereoassign_macro() {
  Stereoassign_macroContext *_localctx = _tracker.createInstance<Stereoassign_macroContext>(_ctx, getState());
  enterRule(_localctx, 100, CyanaMRParser::RuleStereoassign_macro);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(768);
    match(CyanaMRParser::Atom_stereo);
    setState(769);
    match(CyanaMRParser::Double_quote_string);
    setState(770);
    match(CyanaMRParser::RETURN_PR);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Declare_variableContext ------------------------------------------------------------------

CyanaMRParser::Declare_variableContext::Declare_variableContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Declare_variableContext::Var() {
  return getToken(CyanaMRParser::Var, 0);
}

tree::TerminalNode* CyanaMRParser::Declare_variableContext::RETURN_VA() {
  return getToken(CyanaMRParser::RETURN_VA, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Declare_variableContext::Simple_name_VA() {
  return getTokens(CyanaMRParser::Simple_name_VA);
}

tree::TerminalNode* CyanaMRParser::Declare_variableContext::Simple_name_VA(size_t i) {
  return getToken(CyanaMRParser::Simple_name_VA, i);
}


size_t CyanaMRParser::Declare_variableContext::getRuleIndex() const {
  return CyanaMRParser::RuleDeclare_variable;
}


std::any CyanaMRParser::Declare_variableContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDeclare_variable(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Declare_variableContext* CyanaMRParser::declare_variable() {
  Declare_variableContext *_localctx = _tracker.createInstance<Declare_variableContext>(_ctx, getState());
  enterRule(_localctx, 102, CyanaMRParser::RuleDeclare_variable);
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
    setState(772);
    match(CyanaMRParser::Var);
    setState(776);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Simple_name_VA) {
      setState(773);
      match(CyanaMRParser::Simple_name_VA);
      setState(778);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(779);
    match(CyanaMRParser::RETURN_VA);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Set_variableContext ------------------------------------------------------------------

CyanaMRParser::Set_variableContext::Set_variableContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Set_variableContext::SetVar() {
  return getToken(CyanaMRParser::SetVar, 0);
}


size_t CyanaMRParser::Set_variableContext::getRuleIndex() const {
  return CyanaMRParser::RuleSet_variable;
}


std::any CyanaMRParser::Set_variableContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitSet_variable(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Set_variableContext* CyanaMRParser::set_variable() {
  Set_variableContext *_localctx = _tracker.createInstance<Set_variableContext>(_ctx, getState());
  enterRule(_localctx, 104, CyanaMRParser::RuleSet_variable);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(781);
    match(CyanaMRParser::SetVar);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Unset_variableContext ------------------------------------------------------------------

CyanaMRParser::Unset_variableContext::Unset_variableContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Unset_variableContext::Unset() {
  return getToken(CyanaMRParser::Unset, 0);
}

tree::TerminalNode* CyanaMRParser::Unset_variableContext::RETURN_VA() {
  return getToken(CyanaMRParser::RETURN_VA, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Unset_variableContext::Simple_name_VA() {
  return getTokens(CyanaMRParser::Simple_name_VA);
}

tree::TerminalNode* CyanaMRParser::Unset_variableContext::Simple_name_VA(size_t i) {
  return getToken(CyanaMRParser::Simple_name_VA, i);
}


size_t CyanaMRParser::Unset_variableContext::getRuleIndex() const {
  return CyanaMRParser::RuleUnset_variable;
}


std::any CyanaMRParser::Unset_variableContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitUnset_variable(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Unset_variableContext* CyanaMRParser::unset_variable() {
  Unset_variableContext *_localctx = _tracker.createInstance<Unset_variableContext>(_ctx, getState());
  enterRule(_localctx, 106, CyanaMRParser::RuleUnset_variable);
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
    setState(783);
    match(CyanaMRParser::Unset);
    setState(787);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Simple_name_VA) {
      setState(784);
      match(CyanaMRParser::Simple_name_VA);
      setState(789);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(790);
    match(CyanaMRParser::RETURN_VA);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Print_macroContext ------------------------------------------------------------------

CyanaMRParser::Print_macroContext::Print_macroContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Print_macroContext::Print() {
  return getToken(CyanaMRParser::Print, 0);
}

tree::TerminalNode* CyanaMRParser::Print_macroContext::Double_quote_string() {
  return getToken(CyanaMRParser::Double_quote_string, 0);
}

tree::TerminalNode* CyanaMRParser::Print_macroContext::RETURN_PR() {
  return getToken(CyanaMRParser::RETURN_PR, 0);
}


size_t CyanaMRParser::Print_macroContext::getRuleIndex() const {
  return CyanaMRParser::RulePrint_macro;
}


std::any CyanaMRParser::Print_macroContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitPrint_macro(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Print_macroContext* CyanaMRParser::print_macro() {
  Print_macroContext *_localctx = _tracker.createInstance<Print_macroContext>(_ctx, getState());
  enterRule(_localctx, 108, CyanaMRParser::RulePrint_macro);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(792);
    match(CyanaMRParser::Print);
    setState(793);
    match(CyanaMRParser::Double_quote_string);
    setState(794);
    match(CyanaMRParser::RETURN_PR);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Unambig_atom_name_mappingContext ------------------------------------------------------------------

CyanaMRParser::Unambig_atom_name_mappingContext::Unambig_atom_name_mappingContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Unambig_atom_name_mappingContext::Residue() {
  return getToken(CyanaMRParser::Residue, 0);
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Unambig_atom_name_mappingContext::gen_simple_name() {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(0);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Unambig_atom_name_mappingContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Unambig_atom_name_mappingContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::Mapping_listContext *> CyanaMRParser::Unambig_atom_name_mappingContext::mapping_list() {
  return getRuleContexts<CyanaMRParser::Mapping_listContext>();
}

CyanaMRParser::Mapping_listContext* CyanaMRParser::Unambig_atom_name_mappingContext::mapping_list(size_t i) {
  return getRuleContext<CyanaMRParser::Mapping_listContext>(i);
}


size_t CyanaMRParser::Unambig_atom_name_mappingContext::getRuleIndex() const {
  return CyanaMRParser::RuleUnambig_atom_name_mapping;
}


std::any CyanaMRParser::Unambig_atom_name_mappingContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitUnambig_atom_name_mapping(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Unambig_atom_name_mappingContext* CyanaMRParser::unambig_atom_name_mapping() {
  Unambig_atom_name_mappingContext *_localctx = _tracker.createInstance<Unambig_atom_name_mappingContext>(_ctx, getState());
  enterRule(_localctx, 110, CyanaMRParser::RuleUnambig_atom_name_mapping);

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
    setState(796);
    match(CyanaMRParser::Residue);
    setState(797);
    gen_simple_name();
    setState(799);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 112, _ctx)) {
    case 1: {
      setState(798);
      comment();
      break;
    }

    default:
      break;
    }
    setState(803); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(803);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Mapping: {
                  setState(801);
                  mapping_list();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(802);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(805); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 114, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Mapping_listContext ------------------------------------------------------------------

CyanaMRParser::Mapping_listContext::Mapping_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Mapping_listContext::Mapping() {
  return getToken(CyanaMRParser::Mapping, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Mapping_listContext::Simple_name_MP() {
  return getTokens(CyanaMRParser::Simple_name_MP);
}

tree::TerminalNode* CyanaMRParser::Mapping_listContext::Simple_name_MP(size_t i) {
  return getToken(CyanaMRParser::Simple_name_MP, i);
}

tree::TerminalNode* CyanaMRParser::Mapping_listContext::Equ_op_MP() {
  return getToken(CyanaMRParser::Equ_op_MP, 0);
}

tree::TerminalNode* CyanaMRParser::Mapping_listContext::RETURN_MP() {
  return getToken(CyanaMRParser::RETURN_MP, 0);
}


size_t CyanaMRParser::Mapping_listContext::getRuleIndex() const {
  return CyanaMRParser::RuleMapping_list;
}


std::any CyanaMRParser::Mapping_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitMapping_list(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Mapping_listContext* CyanaMRParser::mapping_list() {
  Mapping_listContext *_localctx = _tracker.createInstance<Mapping_listContext>(_ctx, getState());
  enterRule(_localctx, 112, CyanaMRParser::RuleMapping_list);
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
    setState(807);
    match(CyanaMRParser::Mapping);
    setState(808);
    match(CyanaMRParser::Simple_name_MP);
    setState(809);
    match(CyanaMRParser::Equ_op_MP);
    setState(811); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(810);
      match(CyanaMRParser::Simple_name_MP);
      setState(813); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == CyanaMRParser::Simple_name_MP);
    setState(815);
    match(CyanaMRParser::RETURN_MP);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ambig_atom_name_mappingContext ------------------------------------------------------------------

CyanaMRParser::Ambig_atom_name_mappingContext::Ambig_atom_name_mappingContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Ambig_atom_name_mappingContext::Residue() {
  return getToken(CyanaMRParser::Residue, 0);
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Ambig_atom_name_mappingContext::gen_simple_name() {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(0);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Ambig_atom_name_mappingContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Ambig_atom_name_mappingContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::Ambig_listContext *> CyanaMRParser::Ambig_atom_name_mappingContext::ambig_list() {
  return getRuleContexts<CyanaMRParser::Ambig_listContext>();
}

CyanaMRParser::Ambig_listContext* CyanaMRParser::Ambig_atom_name_mappingContext::ambig_list(size_t i) {
  return getRuleContext<CyanaMRParser::Ambig_listContext>(i);
}


size_t CyanaMRParser::Ambig_atom_name_mappingContext::getRuleIndex() const {
  return CyanaMRParser::RuleAmbig_atom_name_mapping;
}


std::any CyanaMRParser::Ambig_atom_name_mappingContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitAmbig_atom_name_mapping(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Ambig_atom_name_mappingContext* CyanaMRParser::ambig_atom_name_mapping() {
  Ambig_atom_name_mappingContext *_localctx = _tracker.createInstance<Ambig_atom_name_mappingContext>(_ctx, getState());
  enterRule(_localctx, 114, CyanaMRParser::RuleAmbig_atom_name_mapping);

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
    setState(817);
    match(CyanaMRParser::Residue);
    setState(818);
    gen_simple_name();
    setState(820);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 116, _ctx)) {
    case 1: {
      setState(819);
      comment();
      break;
    }

    default:
      break;
    }
    setState(824); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(824);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Ambig: {
                  setState(822);
                  ambig_list();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(823);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(826); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 118, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ambig_listContext ------------------------------------------------------------------

CyanaMRParser::Ambig_listContext::Ambig_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Ambig_listContext::Ambig() {
  return getToken(CyanaMRParser::Ambig, 0);
}

tree::TerminalNode* CyanaMRParser::Ambig_listContext::Equ_op_MP() {
  return getToken(CyanaMRParser::Equ_op_MP, 0);
}

tree::TerminalNode* CyanaMRParser::Ambig_listContext::RETURN_MP() {
  return getToken(CyanaMRParser::RETURN_MP, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Ambig_listContext::Simple_name_MP() {
  return getTokens(CyanaMRParser::Simple_name_MP);
}

tree::TerminalNode* CyanaMRParser::Ambig_listContext::Simple_name_MP(size_t i) {
  return getToken(CyanaMRParser::Simple_name_MP, i);
}

tree::TerminalNode* CyanaMRParser::Ambig_listContext::Ambig_code_MP() {
  return getToken(CyanaMRParser::Ambig_code_MP, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Ambig_listContext::Integer_MP() {
  return getTokens(CyanaMRParser::Integer_MP);
}

tree::TerminalNode* CyanaMRParser::Ambig_listContext::Integer_MP(size_t i) {
  return getToken(CyanaMRParser::Integer_MP, i);
}


size_t CyanaMRParser::Ambig_listContext::getRuleIndex() const {
  return CyanaMRParser::RuleAmbig_list;
}


std::any CyanaMRParser::Ambig_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitAmbig_list(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Ambig_listContext* CyanaMRParser::ambig_list() {
  Ambig_listContext *_localctx = _tracker.createInstance<Ambig_listContext>(_ctx, getState());
  enterRule(_localctx, 116, CyanaMRParser::RuleAmbig_list);
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
    setState(828);
    match(CyanaMRParser::Ambig);
    setState(829);
    _la = _input->LA(1);
    if (!(_la == CyanaMRParser::Ambig_code_MP

    || _la == CyanaMRParser::Simple_name_MP)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(830);
    match(CyanaMRParser::Equ_op_MP);
    setState(833); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(831);
      match(CyanaMRParser::Simple_name_MP);
      setState(832);
      match(CyanaMRParser::Integer_MP);
      setState(835); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == CyanaMRParser::Simple_name_MP);
    setState(837);
    match(CyanaMRParser::RETURN_MP);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberContext ------------------------------------------------------------------

CyanaMRParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::NumberContext::Float() {
  return getToken(CyanaMRParser::Float, 0);
}

tree::TerminalNode* CyanaMRParser::NumberContext::Float_DecimalComma() {
  return getToken(CyanaMRParser::Float_DecimalComma, 0);
}

tree::TerminalNode* CyanaMRParser::NumberContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::NumberContext::getRuleIndex() const {
  return CyanaMRParser::RuleNumber;
}


std::any CyanaMRParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::NumberContext* CyanaMRParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 118, CyanaMRParser::RuleNumber);
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
    setState(839);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 28) != 0))) {
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

CyanaMRParser::Gen_res_numContext::Gen_res_numContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Gen_res_numContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_res_numContext::Capital_integer() {
  return getToken(CyanaMRParser::Capital_integer, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_res_numContext::Integer_capital() {
  return getToken(CyanaMRParser::Integer_capital, 0);
}


size_t CyanaMRParser::Gen_res_numContext::getRuleIndex() const {
  return CyanaMRParser::RuleGen_res_num;
}


std::any CyanaMRParser::Gen_res_numContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitGen_res_num(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::gen_res_num() {
  Gen_res_numContext *_localctx = _tracker.createInstance<Gen_res_numContext>(_ctx, getState());
  enterRule(_localctx, 120, CyanaMRParser::RuleGen_res_num);
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
    setState(841);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 103079215108) != 0))) {
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

CyanaMRParser::Gen_simple_nameContext::Gen_simple_nameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Gen_simple_nameContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_simple_nameContext::Capital_integer() {
  return getToken(CyanaMRParser::Capital_integer, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_simple_nameContext::Integer_capital() {
  return getToken(CyanaMRParser::Integer_capital, 0);
}


size_t CyanaMRParser::Gen_simple_nameContext::getRuleIndex() const {
  return CyanaMRParser::RuleGen_simple_name;
}


std::any CyanaMRParser::Gen_simple_nameContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitGen_simple_name(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::gen_simple_name() {
  Gen_simple_nameContext *_localctx = _tracker.createInstance<Gen_simple_nameContext>(_ctx, getState());
  enterRule(_localctx, 122, CyanaMRParser::RuleGen_simple_name);
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
    setState(843);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 240518168576) != 0))) {
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

//----------------- Gen_atom_nameContext ------------------------------------------------------------------

CyanaMRParser::Gen_atom_nameContext::Gen_atom_nameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Gen_atom_nameContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_atom_nameContext::Capital_integer() {
  return getToken(CyanaMRParser::Capital_integer, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_atom_nameContext::Integer_capital() {
  return getToken(CyanaMRParser::Integer_capital, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_atom_nameContext::Ambig_code() {
  return getToken(CyanaMRParser::Ambig_code, 0);
}


size_t CyanaMRParser::Gen_atom_nameContext::getRuleIndex() const {
  return CyanaMRParser::RuleGen_atom_name;
}


std::any CyanaMRParser::Gen_atom_nameContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitGen_atom_name(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Gen_atom_nameContext* CyanaMRParser::gen_atom_name() {
  Gen_atom_nameContext *_localctx = _tracker.createInstance<Gen_atom_nameContext>(_ctx, getState());
  enterRule(_localctx, 124, CyanaMRParser::RuleGen_atom_name);
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
    setState(845);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 240518168578) != 0))) {
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

void CyanaMRParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  cyanamrparserParserInitialize();
#else
  ::antlr4::internal::call_once(cyanamrparserParserOnceFlag, cyanamrparserParserInitialize);
#endif
}
