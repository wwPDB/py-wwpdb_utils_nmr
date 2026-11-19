
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
      "diana_stereoassign_macro", "distance_w_chain_restraints", "distance_w_chain_restraint", 
      "distance_w_chain2_restraints", "distance_w_chain2_restraint", "distance_w_chain3_restraints", 
      "distance_w_chain3_restraint", "torsion_angle_w_chain_restraints", 
      "torsion_angle_w_chain_restraint", "cco_restraints", "cco_restraint", 
      "ssbond_macro", "hbond_macro", "link_statement", "stereoassign_macro", 
      "declare_variable", "set_variable", "unset_variable", "print_macro", 
      "unambig_atom_name_mapping", "mapping_list", "ambig_atom_name_mapping", 
      "ambig_list", "number", "gen_res_num", "gen_simple_name", "gen_atom_name", 
      "number_qc", "gen_res_num_qc", "gen_simple_name_qc", "gen_atom_name_qc"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "", "'NOEUPP'", "'NOELOW'", "'NOEUPLO'", 
      "'HBUPP'", "'HBLOW'", "'HBUPLO'", "'SSUPP'", "'SSLOW'", "'SSUPLO'", 
      "'JCOUPL'", "'ANGLE'", "'STEREO'", "'TYPE'", "", "'OR'", "'SSBOND'", 
      "", "'HBOND'", "'LINK'", "", "'VAR'", "'UNSET'", "", "'PRINT'", "'RESIDUE'", 
      "'MAPPING'", "'AMBIG'", "", "", "", "", "", "", "", "", "", "", "'ATOM1'", 
      "'ATOM2'", "'RESIDUE1'", "'RESIDUE2'", "", "'ATOM1='", "'ATOM2='", 
      "'RESIDUE1='", "'RESIDUE2='"
    },
    std::vector<std::string>{
      "", "Ambig_code", "Integer", "Float", "Float_DecimalComma", "Orientation_header", 
      "Tensor_header", "SMCLN_COMMENT", "COMMENT", "NoeUpp", "NoeLow", "NoeUpLo", 
      "HBUpp", "HBLow", "HBUpLo", "SSUpp", "SSLow", "SSUpLo", "Jcoupl", 
      "Angle", "Stereo", "Type", "Equ_op", "Or", "Ssbond", "Ssbond_resids", 
      "Hbond", "Link", "Atom_stereo", "Var", "Unset", "SetVar", "Print", 
      "Residue", "Mapping", "Ambig", "Capital_integer", "Integer_capital", 
      "Simple_name", "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT", 
      "Any_name", "SPACE_CM", "RETURN_CM", "Atom1", "Atom2", "Residue1", 
      "Residue2", "Equ_op_HB", "Atom1_equ", "Atom2_equ", "Residue1_equ", 
      "Residue2_equ", "Concat_atom_1", "Concat_atom_2", "Concat_res_1", 
      "Concat_res_2", "Integer_HB", "Simple_name_HB", "SPACE_HB", "RETURN_HB", 
      "LINE_COMMENT_HB", "Double_quote_string", "Integer_PR", "Simple_name_PR", 
      "SPACE_PR", "RETURN_PR", "LINE_COMMENT_PR", "Simple_name_VA", "SPACE_VA", 
      "RETURN_VA", "LINE_COMMENT_VA", "Ambig_code_MP", "Integer_MP", "Simple_name_MP", 
      "Equ_op_MP", "SPACE_MP", "RETURN_MP", "LINE_COMMENT_MP", "Integer_QC", 
      "Float_QC", "Float_DecimalComma_QC", "Simple_name_QC", "Capital_integer_QC", 
      "Integer_capital_QC", "SPACE_QC", "RETURN_QC"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,88,879,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,
  	35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,
  	42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,
  	49,2,50,7,50,2,51,7,51,2,52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,
  	56,2,57,7,57,2,58,7,58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,
  	63,2,64,7,64,1,0,1,0,4,0,133,8,0,11,0,12,0,134,1,0,1,0,1,0,1,0,1,0,1,
  	0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
  	1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,170,8,0,10,0,12,0,173,9,0,
  	1,0,1,0,1,1,1,1,5,1,179,8,1,10,1,12,1,182,9,1,1,1,1,1,1,2,4,2,187,8,2,
  	11,2,12,2,188,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,199,8,3,1,3,3,3,202,
  	8,3,1,3,3,3,205,8,3,1,3,3,3,208,8,3,1,3,3,3,211,8,3,1,4,4,4,214,8,4,11,
  	4,12,4,215,1,5,1,5,1,5,1,5,1,5,1,5,3,5,224,8,5,1,5,1,5,1,5,3,5,229,8,
  	5,1,5,3,5,232,8,5,1,6,4,6,235,8,6,11,6,12,6,236,1,6,1,6,1,6,4,6,242,8,
  	6,11,6,12,6,243,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
  	8,1,8,1,8,3,8,262,8,8,1,9,4,9,265,8,9,11,9,12,9,266,1,9,1,9,1,9,4,9,272,
  	8,9,11,9,12,9,273,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,
  	11,1,11,1,11,1,12,4,12,290,8,12,11,12,12,12,291,1,13,1,13,1,13,3,13,297,
  	8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,307,8,13,4,13,309,8,
  	13,11,13,12,13,310,1,14,4,14,314,8,14,11,14,12,14,315,1,15,1,15,1,15,
  	3,15,321,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,332,8,
  	15,4,15,334,8,15,11,15,12,15,335,1,16,4,16,339,8,16,11,16,12,16,340,1,
  	17,1,17,1,17,3,17,346,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
  	17,1,17,3,17,358,8,17,4,17,360,8,17,11,17,12,17,361,1,18,4,18,365,8,18,
  	11,18,12,18,366,1,19,1,19,1,19,1,19,3,19,373,8,19,1,19,1,19,1,19,1,19,
  	1,19,1,19,4,19,381,8,19,11,19,12,19,382,1,20,4,20,386,8,20,11,20,12,20,
  	387,1,21,1,21,1,21,1,21,3,21,394,8,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
  	21,4,21,403,8,21,11,21,12,21,404,1,22,4,22,408,8,22,11,22,12,22,409,1,
  	23,1,23,1,23,1,23,3,23,416,8,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
  	23,4,23,426,8,23,11,23,12,23,427,1,24,4,24,431,8,24,11,24,12,24,432,1,
  	25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,444,8,25,1,25,1,25,1,
  	25,1,25,1,25,1,25,3,25,452,8,25,1,25,3,25,455,8,25,1,25,3,25,458,8,25,
  	1,25,1,25,1,26,4,26,463,8,26,11,26,12,26,464,1,27,1,27,1,27,1,27,1,27,
  	1,27,1,27,1,27,1,27,3,27,476,8,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,
  	484,8,27,1,27,3,27,487,8,27,1,27,3,27,490,8,27,1,27,1,27,1,28,4,28,495,
  	8,28,11,28,12,28,496,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,
  	508,8,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,516,8,29,1,29,3,29,519,8,
  	29,1,29,3,29,522,8,29,1,29,1,29,1,30,4,30,527,8,30,11,30,12,30,528,1,
  	31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,541,8,31,1,31,3,
  	31,544,8,31,1,31,3,31,547,8,31,1,31,1,31,1,32,4,32,552,8,32,11,32,12,
  	32,553,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,563,8,33,1,33,1,33,1,33,
  	1,33,3,33,569,8,33,3,33,571,8,33,1,33,1,33,1,33,1,33,3,33,577,8,33,3,
  	33,579,8,33,1,33,3,33,582,8,33,1,33,3,33,585,8,33,1,33,1,33,1,34,1,34,
  	1,34,1,34,5,34,593,8,34,10,34,12,34,596,9,34,1,34,3,34,599,8,34,1,34,
  	1,34,1,35,4,35,604,8,35,11,35,12,35,605,1,36,1,36,1,36,1,36,1,36,1,36,
  	1,36,1,36,1,36,1,36,3,36,618,8,36,1,36,3,36,621,8,36,1,36,3,36,624,8,
  	36,1,36,3,36,627,8,36,1,36,3,36,630,8,36,1,37,4,37,633,8,37,11,37,12,
  	37,634,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,647,8,38,
  	1,38,3,38,650,8,38,1,38,3,38,653,8,38,1,38,3,38,656,8,38,1,38,3,38,659,
  	8,38,1,39,4,39,662,8,39,11,39,12,39,663,1,40,1,40,1,40,1,40,1,40,1,40,
  	1,40,1,40,1,40,1,40,3,40,676,8,40,1,40,3,40,679,8,40,1,40,3,40,682,8,
  	40,1,40,3,40,685,8,40,1,40,3,40,688,8,40,1,41,4,41,691,8,41,11,41,12,
  	41,692,1,42,1,42,1,42,1,42,1,42,1,42,1,42,3,42,702,8,42,1,42,1,42,1,42,
  	3,42,707,8,42,1,42,3,42,710,8,42,1,43,4,43,713,8,43,11,43,12,43,714,1,
  	44,1,44,1,44,1,44,1,44,1,44,3,44,723,8,44,1,44,3,44,726,8,44,1,44,3,44,
  	729,8,44,1,44,3,44,732,8,44,1,44,3,44,735,8,44,1,45,1,45,1,45,1,46,1,
  	46,1,46,1,46,3,46,744,8,46,1,46,1,46,3,46,748,8,46,1,46,1,46,1,46,3,46,
  	753,8,46,1,46,1,46,3,46,757,8,46,1,46,1,46,1,46,3,46,762,8,46,1,46,1,
  	46,3,46,766,8,46,1,46,1,46,1,46,3,46,771,8,46,1,46,1,46,3,46,775,8,46,
  	1,46,1,46,1,47,1,47,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,3,48,789,
  	8,48,1,48,3,48,792,8,48,1,48,1,48,1,49,1,49,5,49,798,8,49,10,49,12,49,
  	801,9,49,1,49,1,49,1,50,1,50,1,51,1,51,5,51,809,8,51,10,51,12,51,812,
  	9,51,1,51,1,51,1,52,1,52,1,52,1,52,1,53,1,53,1,53,3,53,823,8,53,1,53,
  	1,53,4,53,827,8,53,11,53,12,53,828,1,54,1,54,1,54,1,54,4,54,835,8,54,
  	11,54,12,54,836,1,54,1,54,1,55,1,55,1,55,3,55,844,8,55,1,55,1,55,4,55,
  	848,8,55,11,55,12,55,849,1,56,1,56,1,56,1,56,1,56,4,56,857,8,56,11,56,
  	12,56,858,1,56,1,56,1,57,1,57,1,58,1,58,1,59,1,59,1,60,1,60,1,61,1,61,
  	1,62,1,62,1,63,1,63,1,64,1,64,1,64,0,0,65,0,2,4,6,8,10,12,14,16,18,20,
  	22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
  	68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,
  	112,114,116,118,120,122,124,126,128,0,13,1,1,45,45,2,0,2,2,36,38,1,0,
  	9,11,1,0,15,17,1,0,12,14,2,0,74,74,76,76,1,0,2,4,2,0,2,2,36,37,1,0,36,
  	38,2,0,1,1,36,38,1,0,81,83,2,0,81,81,85,86,1,0,84,86,977,0,171,1,0,0,
  	0,2,176,1,0,0,0,4,186,1,0,0,0,6,190,1,0,0,0,8,213,1,0,0,0,10,217,1,0,
  	0,0,12,234,1,0,0,0,14,245,1,0,0,0,16,250,1,0,0,0,18,264,1,0,0,0,20,275,
  	1,0,0,0,22,280,1,0,0,0,24,289,1,0,0,0,26,293,1,0,0,0,28,313,1,0,0,0,30,
  	317,1,0,0,0,32,338,1,0,0,0,34,342,1,0,0,0,36,364,1,0,0,0,38,368,1,0,0,
  	0,40,385,1,0,0,0,42,389,1,0,0,0,44,407,1,0,0,0,46,411,1,0,0,0,48,430,
  	1,0,0,0,50,434,1,0,0,0,52,462,1,0,0,0,54,466,1,0,0,0,56,494,1,0,0,0,58,
  	498,1,0,0,0,60,526,1,0,0,0,62,530,1,0,0,0,64,551,1,0,0,0,66,555,1,0,0,
  	0,68,588,1,0,0,0,70,603,1,0,0,0,72,607,1,0,0,0,74,632,1,0,0,0,76,636,
  	1,0,0,0,78,661,1,0,0,0,80,665,1,0,0,0,82,690,1,0,0,0,84,694,1,0,0,0,86,
  	712,1,0,0,0,88,716,1,0,0,0,90,736,1,0,0,0,92,739,1,0,0,0,94,778,1,0,0,
  	0,96,784,1,0,0,0,98,795,1,0,0,0,100,804,1,0,0,0,102,806,1,0,0,0,104,815,
  	1,0,0,0,106,819,1,0,0,0,108,830,1,0,0,0,110,840,1,0,0,0,112,851,1,0,0,
  	0,114,862,1,0,0,0,116,864,1,0,0,0,118,866,1,0,0,0,120,868,1,0,0,0,122,
  	870,1,0,0,0,124,872,1,0,0,0,126,874,1,0,0,0,128,876,1,0,0,0,130,170,5,
  	5,0,0,131,133,5,6,0,0,132,131,1,0,0,0,133,134,1,0,0,0,134,132,1,0,0,0,
  	134,135,1,0,0,0,135,170,1,0,0,0,136,170,3,2,1,0,137,170,3,4,2,0,138,170,
  	3,24,12,0,139,170,3,28,14,0,140,170,3,32,16,0,141,170,3,36,18,0,142,170,
  	3,40,20,0,143,170,3,44,22,0,144,170,3,48,24,0,145,170,3,52,26,0,146,170,
  	3,56,28,0,147,170,3,60,30,0,148,170,3,64,32,0,149,170,3,68,34,0,150,170,
  	3,70,35,0,151,170,3,74,37,0,152,170,3,78,39,0,153,170,3,8,4,0,154,170,
  	3,82,41,0,155,170,3,12,6,0,156,170,3,18,9,0,157,170,3,86,43,0,158,170,
  	3,90,45,0,159,170,3,92,46,0,160,170,3,94,47,0,161,170,3,96,48,0,162,170,
  	3,98,49,0,163,170,3,100,50,0,164,170,3,102,51,0,165,170,3,104,52,0,166,
  	170,3,106,53,0,167,170,3,110,55,0,168,170,3,112,56,0,169,130,1,0,0,0,
  	169,132,1,0,0,0,169,136,1,0,0,0,169,137,1,0,0,0,169,138,1,0,0,0,169,139,
  	1,0,0,0,169,140,1,0,0,0,169,141,1,0,0,0,169,142,1,0,0,0,169,143,1,0,0,
  	0,169,144,1,0,0,0,169,145,1,0,0,0,169,146,1,0,0,0,169,147,1,0,0,0,169,
  	148,1,0,0,0,169,149,1,0,0,0,169,150,1,0,0,0,169,151,1,0,0,0,169,152,1,
  	0,0,0,169,153,1,0,0,0,169,154,1,0,0,0,169,155,1,0,0,0,169,156,1,0,0,0,
  	169,157,1,0,0,0,169,158,1,0,0,0,169,159,1,0,0,0,169,160,1,0,0,0,169,161,
  	1,0,0,0,169,162,1,0,0,0,169,163,1,0,0,0,169,164,1,0,0,0,169,165,1,0,0,
  	0,169,166,1,0,0,0,169,167,1,0,0,0,169,168,1,0,0,0,170,173,1,0,0,0,171,
  	169,1,0,0,0,171,172,1,0,0,0,172,174,1,0,0,0,173,171,1,0,0,0,174,175,5,
  	0,0,1,175,1,1,0,0,0,176,180,5,8,0,0,177,179,5,43,0,0,178,177,1,0,0,0,
  	179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,183,1,0,0,0,182,180,
  	1,0,0,0,183,184,7,0,0,0,184,3,1,0,0,0,185,187,3,6,3,0,186,185,1,0,0,0,
  	187,188,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,5,1,0,0,0,190,191,
  	3,116,58,0,191,192,3,118,59,0,192,193,3,120,60,0,193,194,3,116,58,0,194,
  	195,3,118,59,0,195,196,3,120,60,0,196,198,3,114,57,0,197,199,3,114,57,
  	0,198,197,1,0,0,0,198,199,1,0,0,0,199,201,1,0,0,0,200,202,3,114,57,0,
  	201,200,1,0,0,0,201,202,1,0,0,0,202,204,1,0,0,0,203,205,3,114,57,0,204,
  	203,1,0,0,0,204,205,1,0,0,0,205,207,1,0,0,0,206,208,3,114,57,0,207,206,
  	1,0,0,0,207,208,1,0,0,0,208,210,1,0,0,0,209,211,3,114,57,0,210,209,1,
  	0,0,0,210,211,1,0,0,0,211,7,1,0,0,0,212,214,3,10,5,0,213,212,1,0,0,0,
  	214,215,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,9,1,0,0,0,217,218,
  	3,116,58,0,218,219,3,118,59,0,219,220,3,118,59,0,220,221,3,114,57,0,221,
  	223,3,114,57,0,222,224,3,114,57,0,223,222,1,0,0,0,223,224,1,0,0,0,224,
  	228,1,0,0,0,225,226,5,21,0,0,226,227,5,22,0,0,227,229,5,2,0,0,228,225,
  	1,0,0,0,228,229,1,0,0,0,229,231,1,0,0,0,230,232,5,23,0,0,231,230,1,0,
  	0,0,231,232,1,0,0,0,232,11,1,0,0,0,233,235,3,14,7,0,234,233,1,0,0,0,235,
  	236,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,241,1,0,0,0,238,242,5,
  	5,0,0,239,242,3,2,1,0,240,242,3,16,8,0,241,238,1,0,0,0,241,239,1,0,0,
  	0,241,240,1,0,0,0,242,243,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,
  	13,1,0,0,0,245,246,5,2,0,0,246,247,3,114,57,0,247,248,3,114,57,0,248,
  	249,7,1,0,0,249,15,1,0,0,0,250,251,3,116,58,0,251,252,3,118,59,0,252,
  	253,3,118,59,0,253,254,3,116,58,0,254,255,3,118,59,0,255,256,3,118,59,
  	0,256,257,3,114,57,0,257,258,3,114,57,0,258,259,3,114,57,0,259,261,5,
  	2,0,0,260,262,3,114,57,0,261,260,1,0,0,0,261,262,1,0,0,0,262,17,1,0,0,
  	0,263,265,3,20,10,0,264,263,1,0,0,0,265,266,1,0,0,0,266,264,1,0,0,0,266,
  	267,1,0,0,0,267,271,1,0,0,0,268,272,5,5,0,0,269,272,3,2,1,0,270,272,3,
  	22,11,0,271,268,1,0,0,0,271,269,1,0,0,0,271,270,1,0,0,0,272,273,1,0,0,
  	0,273,271,1,0,0,0,273,274,1,0,0,0,274,19,1,0,0,0,275,276,5,2,0,0,276,
  	277,3,114,57,0,277,278,3,114,57,0,278,279,7,1,0,0,279,21,1,0,0,0,280,
  	281,3,116,58,0,281,282,3,118,59,0,282,283,3,118,59,0,283,284,3,114,57,
  	0,284,285,3,114,57,0,285,286,3,114,57,0,286,287,5,2,0,0,287,23,1,0,0,
  	0,288,290,3,26,13,0,289,288,1,0,0,0,290,291,1,0,0,0,291,289,1,0,0,0,291,
  	292,1,0,0,0,292,25,1,0,0,0,293,294,3,116,58,0,294,296,3,118,59,0,295,
  	297,3,2,1,0,296,295,1,0,0,0,296,297,1,0,0,0,297,308,1,0,0,0,298,299,3,
  	118,59,0,299,300,3,116,58,0,300,301,3,118,59,0,301,302,3,118,59,0,302,
  	303,3,114,57,0,303,309,1,0,0,0,304,307,3,2,1,0,305,307,5,3,0,0,306,304,
  	1,0,0,0,306,305,1,0,0,0,307,309,1,0,0,0,308,298,1,0,0,0,308,306,1,0,0,
  	0,309,310,1,0,0,0,310,308,1,0,0,0,310,311,1,0,0,0,311,27,1,0,0,0,312,
  	314,3,30,15,0,313,312,1,0,0,0,314,315,1,0,0,0,315,313,1,0,0,0,315,316,
  	1,0,0,0,316,29,1,0,0,0,317,318,3,116,58,0,318,320,3,118,59,0,319,321,
  	3,2,1,0,320,319,1,0,0,0,320,321,1,0,0,0,321,333,1,0,0,0,322,323,3,118,
  	59,0,323,324,3,116,58,0,324,325,3,118,59,0,325,326,3,118,59,0,326,327,
  	3,114,57,0,327,328,3,114,57,0,328,334,1,0,0,0,329,332,3,2,1,0,330,332,
  	5,3,0,0,331,329,1,0,0,0,331,330,1,0,0,0,332,334,1,0,0,0,333,322,1,0,0,
  	0,333,331,1,0,0,0,334,335,1,0,0,0,335,333,1,0,0,0,335,336,1,0,0,0,336,
  	31,1,0,0,0,337,339,3,34,17,0,338,337,1,0,0,0,339,340,1,0,0,0,340,338,
  	1,0,0,0,340,341,1,0,0,0,341,33,1,0,0,0,342,343,3,116,58,0,343,345,3,118,
  	59,0,344,346,3,2,1,0,345,344,1,0,0,0,345,346,1,0,0,0,346,359,1,0,0,0,
  	347,348,3,118,59,0,348,349,3,116,58,0,349,350,3,118,59,0,350,351,3,118,
  	59,0,351,352,3,114,57,0,352,353,3,114,57,0,353,354,3,114,57,0,354,360,
  	1,0,0,0,355,358,3,2,1,0,356,358,5,3,0,0,357,355,1,0,0,0,357,356,1,0,0,
  	0,358,360,1,0,0,0,359,347,1,0,0,0,359,357,1,0,0,0,360,361,1,0,0,0,361,
  	359,1,0,0,0,361,362,1,0,0,0,362,35,1,0,0,0,363,365,3,38,19,0,364,363,
  	1,0,0,0,365,366,1,0,0,0,366,364,1,0,0,0,366,367,1,0,0,0,367,37,1,0,0,
  	0,368,369,3,116,58,0,369,370,3,118,59,0,370,372,3,118,59,0,371,373,3,
  	2,1,0,372,371,1,0,0,0,372,373,1,0,0,0,373,380,1,0,0,0,374,375,3,116,58,
  	0,375,376,3,118,59,0,376,377,3,118,59,0,377,378,3,114,57,0,378,381,1,
  	0,0,0,379,381,3,2,1,0,380,374,1,0,0,0,380,379,1,0,0,0,381,382,1,0,0,0,
  	382,380,1,0,0,0,382,383,1,0,0,0,383,39,1,0,0,0,384,386,3,42,21,0,385,
  	384,1,0,0,0,386,387,1,0,0,0,387,385,1,0,0,0,387,388,1,0,0,0,388,41,1,
  	0,0,0,389,390,3,116,58,0,390,391,3,118,59,0,391,393,3,118,59,0,392,394,
  	3,2,1,0,393,392,1,0,0,0,393,394,1,0,0,0,394,402,1,0,0,0,395,396,3,116,
  	58,0,396,397,3,118,59,0,397,398,3,118,59,0,398,399,3,114,57,0,399,400,
  	3,114,57,0,400,403,1,0,0,0,401,403,3,2,1,0,402,395,1,0,0,0,402,401,1,
  	0,0,0,403,404,1,0,0,0,404,402,1,0,0,0,404,405,1,0,0,0,405,43,1,0,0,0,
  	406,408,3,46,23,0,407,406,1,0,0,0,408,409,1,0,0,0,409,407,1,0,0,0,409,
  	410,1,0,0,0,410,45,1,0,0,0,411,412,3,116,58,0,412,413,3,118,59,0,413,
  	415,3,118,59,0,414,416,3,2,1,0,415,414,1,0,0,0,415,416,1,0,0,0,416,425,
  	1,0,0,0,417,418,3,116,58,0,418,419,3,118,59,0,419,420,3,118,59,0,420,
  	421,3,114,57,0,421,422,3,114,57,0,422,423,3,114,57,0,423,426,1,0,0,0,
  	424,426,3,2,1,0,425,417,1,0,0,0,425,424,1,0,0,0,426,427,1,0,0,0,427,425,
  	1,0,0,0,427,428,1,0,0,0,428,47,1,0,0,0,429,431,3,50,25,0,430,429,1,0,
  	0,0,431,432,1,0,0,0,432,430,1,0,0,0,432,433,1,0,0,0,433,49,1,0,0,0,434,
  	435,7,2,0,0,435,436,3,126,63,0,436,437,3,124,62,0,437,438,3,126,63,0,
  	438,439,3,126,63,0,439,440,3,124,62,0,440,441,3,126,63,0,441,443,3,122,
  	61,0,442,444,3,122,61,0,443,442,1,0,0,0,443,444,1,0,0,0,444,451,1,0,0,
  	0,445,446,3,126,63,0,446,447,3,126,63,0,447,448,3,124,62,0,448,449,3,
  	126,63,0,449,450,3,122,61,0,450,452,1,0,0,0,451,445,1,0,0,0,451,452,1,
  	0,0,0,452,454,1,0,0,0,453,455,5,84,0,0,454,453,1,0,0,0,454,455,1,0,0,
  	0,455,457,1,0,0,0,456,458,5,81,0,0,457,456,1,0,0,0,457,458,1,0,0,0,458,
  	459,1,0,0,0,459,460,5,88,0,0,460,51,1,0,0,0,461,463,3,54,27,0,462,461,
  	1,0,0,0,463,464,1,0,0,0,464,462,1,0,0,0,464,465,1,0,0,0,465,53,1,0,0,
  	0,466,467,7,3,0,0,467,468,3,126,63,0,468,469,3,124,62,0,469,470,3,126,
  	63,0,470,471,3,126,63,0,471,472,3,124,62,0,472,473,3,126,63,0,473,475,
  	3,122,61,0,474,476,3,122,61,0,475,474,1,0,0,0,475,476,1,0,0,0,476,483,
  	1,0,0,0,477,478,3,126,63,0,478,479,3,126,63,0,479,480,3,124,62,0,480,
  	481,3,126,63,0,481,482,3,122,61,0,482,484,1,0,0,0,483,477,1,0,0,0,483,
  	484,1,0,0,0,484,486,1,0,0,0,485,487,5,84,0,0,486,485,1,0,0,0,486,487,
  	1,0,0,0,487,489,1,0,0,0,488,490,5,81,0,0,489,488,1,0,0,0,489,490,1,0,
  	0,0,490,491,1,0,0,0,491,492,5,88,0,0,492,55,1,0,0,0,493,495,3,58,29,0,
  	494,493,1,0,0,0,495,496,1,0,0,0,496,494,1,0,0,0,496,497,1,0,0,0,497,57,
  	1,0,0,0,498,499,7,4,0,0,499,500,3,126,63,0,500,501,3,124,62,0,501,502,
  	3,126,63,0,502,503,3,126,63,0,503,504,3,124,62,0,504,505,3,126,63,0,505,
  	507,3,122,61,0,506,508,3,122,61,0,507,506,1,0,0,0,507,508,1,0,0,0,508,
  	515,1,0,0,0,509,510,3,126,63,0,510,511,3,126,63,0,511,512,3,124,62,0,
  	512,513,3,126,63,0,513,514,3,122,61,0,514,516,1,0,0,0,515,509,1,0,0,0,
  	515,516,1,0,0,0,516,518,1,0,0,0,517,519,5,84,0,0,518,517,1,0,0,0,518,
  	519,1,0,0,0,519,521,1,0,0,0,520,522,5,81,0,0,521,520,1,0,0,0,521,522,
  	1,0,0,0,522,523,1,0,0,0,523,524,5,88,0,0,524,59,1,0,0,0,525,527,3,62,
  	31,0,526,525,1,0,0,0,527,528,1,0,0,0,528,526,1,0,0,0,528,529,1,0,0,0,
  	529,61,1,0,0,0,530,531,5,19,0,0,531,532,3,126,63,0,532,533,3,124,62,0,
  	533,534,3,126,63,0,534,535,3,122,61,0,535,540,3,122,61,0,536,537,3,126,
  	63,0,537,538,3,122,61,0,538,539,3,122,61,0,539,541,1,0,0,0,540,536,1,
  	0,0,0,540,541,1,0,0,0,541,543,1,0,0,0,542,544,5,84,0,0,543,542,1,0,0,
  	0,543,544,1,0,0,0,544,546,1,0,0,0,545,547,5,81,0,0,546,545,1,0,0,0,546,
  	547,1,0,0,0,547,548,1,0,0,0,548,549,5,88,0,0,549,63,1,0,0,0,550,552,3,
  	66,33,0,551,550,1,0,0,0,552,553,1,0,0,0,553,551,1,0,0,0,553,554,1,0,0,
  	0,554,65,1,0,0,0,555,556,5,18,0,0,556,557,3,126,63,0,557,558,3,124,62,
  	0,558,559,3,126,63,0,559,560,3,126,63,0,560,562,3,122,61,0,561,563,3,
  	122,61,0,562,561,1,0,0,0,562,563,1,0,0,0,563,570,1,0,0,0,564,565,3,126,
  	63,0,565,566,3,126,63,0,566,568,3,122,61,0,567,569,3,122,61,0,568,567,
  	1,0,0,0,568,569,1,0,0,0,569,571,1,0,0,0,570,564,1,0,0,0,570,571,1,0,0,
  	0,571,578,1,0,0,0,572,573,3,126,63,0,573,574,3,126,63,0,574,576,3,122,
  	61,0,575,577,3,122,61,0,576,575,1,0,0,0,576,577,1,0,0,0,577,579,1,0,0,
  	0,578,572,1,0,0,0,578,579,1,0,0,0,579,581,1,0,0,0,580,582,5,84,0,0,581,
  	580,1,0,0,0,581,582,1,0,0,0,582,584,1,0,0,0,583,585,5,81,0,0,584,583,
  	1,0,0,0,584,585,1,0,0,0,585,586,1,0,0,0,586,587,5,88,0,0,587,67,1,0,0,
  	0,588,589,5,20,0,0,589,590,3,126,63,0,590,594,3,124,62,0,591,593,3,126,
  	63,0,592,591,1,0,0,0,593,596,1,0,0,0,594,592,1,0,0,0,594,595,1,0,0,0,
  	595,598,1,0,0,0,596,594,1,0,0,0,597,599,5,81,0,0,598,597,1,0,0,0,598,
  	599,1,0,0,0,599,600,1,0,0,0,600,601,5,88,0,0,601,69,1,0,0,0,602,604,3,
  	72,36,0,603,602,1,0,0,0,604,605,1,0,0,0,605,603,1,0,0,0,605,606,1,0,0,
  	0,606,71,1,0,0,0,607,608,5,2,0,0,608,609,3,118,59,0,609,610,3,118,59,
  	0,610,611,3,118,59,0,611,612,5,2,0,0,612,613,3,118,59,0,613,614,3,118,
  	59,0,614,615,3,118,59,0,615,617,3,114,57,0,616,618,3,114,57,0,617,616,
  	1,0,0,0,617,618,1,0,0,0,618,620,1,0,0,0,619,621,3,114,57,0,620,619,1,
  	0,0,0,620,621,1,0,0,0,621,623,1,0,0,0,622,624,3,114,57,0,623,622,1,0,
  	0,0,623,624,1,0,0,0,624,626,1,0,0,0,625,627,3,114,57,0,626,625,1,0,0,
  	0,626,627,1,0,0,0,627,629,1,0,0,0,628,630,3,114,57,0,629,628,1,0,0,0,
  	629,630,1,0,0,0,630,73,1,0,0,0,631,633,3,76,38,0,632,631,1,0,0,0,633,
  	634,1,0,0,0,634,632,1,0,0,0,634,635,1,0,0,0,635,75,1,0,0,0,636,637,3,
  	118,59,0,637,638,5,2,0,0,638,639,3,118,59,0,639,640,3,118,59,0,640,641,
  	3,118,59,0,641,642,5,2,0,0,642,643,3,118,59,0,643,644,3,118,59,0,644,
  	646,3,114,57,0,645,647,3,114,57,0,646,645,1,0,0,0,646,647,1,0,0,0,647,
  	649,1,0,0,0,648,650,3,114,57,0,649,648,1,0,0,0,649,650,1,0,0,0,650,652,
  	1,0,0,0,651,653,3,114,57,0,652,651,1,0,0,0,652,653,1,0,0,0,653,655,1,
  	0,0,0,654,656,3,114,57,0,655,654,1,0,0,0,655,656,1,0,0,0,656,658,1,0,
  	0,0,657,659,3,114,57,0,658,657,1,0,0,0,658,659,1,0,0,0,659,77,1,0,0,0,
  	660,662,3,80,40,0,661,660,1,0,0,0,662,663,1,0,0,0,663,661,1,0,0,0,663,
  	664,1,0,0,0,664,79,1,0,0,0,665,666,3,118,59,0,666,667,3,118,59,0,667,
  	668,5,2,0,0,668,669,3,118,59,0,669,670,3,118,59,0,670,671,3,118,59,0,
  	671,672,5,2,0,0,672,673,3,118,59,0,673,675,3,114,57,0,674,676,3,114,57,
  	0,675,674,1,0,0,0,675,676,1,0,0,0,676,678,1,0,0,0,677,679,3,114,57,0,
  	678,677,1,0,0,0,678,679,1,0,0,0,679,681,1,0,0,0,680,682,3,114,57,0,681,
  	680,1,0,0,0,681,682,1,0,0,0,682,684,1,0,0,0,683,685,3,114,57,0,684,683,
  	1,0,0,0,684,685,1,0,0,0,685,687,1,0,0,0,686,688,3,114,57,0,687,686,1,
  	0,0,0,687,688,1,0,0,0,688,81,1,0,0,0,689,691,3,84,42,0,690,689,1,0,0,
  	0,691,692,1,0,0,0,692,690,1,0,0,0,692,693,1,0,0,0,693,83,1,0,0,0,694,
  	695,3,118,59,0,695,696,5,2,0,0,696,697,3,118,59,0,697,698,3,118,59,0,
  	698,699,3,114,57,0,699,701,3,114,57,0,700,702,3,114,57,0,701,700,1,0,
  	0,0,701,702,1,0,0,0,702,706,1,0,0,0,703,704,5,21,0,0,704,705,5,22,0,0,
  	705,707,5,2,0,0,706,703,1,0,0,0,706,707,1,0,0,0,707,709,1,0,0,0,708,710,
  	5,23,0,0,709,708,1,0,0,0,709,710,1,0,0,0,710,85,1,0,0,0,711,713,3,88,
  	44,0,712,711,1,0,0,0,713,714,1,0,0,0,714,712,1,0,0,0,714,715,1,0,0,0,
  	715,87,1,0,0,0,716,717,3,116,58,0,717,718,3,118,59,0,718,719,3,118,59,
  	0,719,720,3,118,59,0,720,722,3,114,57,0,721,723,3,114,57,0,722,721,1,
  	0,0,0,722,723,1,0,0,0,723,725,1,0,0,0,724,726,3,114,57,0,725,724,1,0,
  	0,0,725,726,1,0,0,0,726,728,1,0,0,0,727,729,3,114,57,0,728,727,1,0,0,
  	0,728,729,1,0,0,0,729,731,1,0,0,0,730,732,3,114,57,0,731,730,1,0,0,0,
  	731,732,1,0,0,0,732,734,1,0,0,0,733,735,3,114,57,0,734,733,1,0,0,0,734,
  	735,1,0,0,0,735,89,1,0,0,0,736,737,5,24,0,0,737,738,5,25,0,0,738,91,1,
  	0,0,0,739,747,5,26,0,0,740,741,5,46,0,0,741,744,5,50,0,0,742,744,5,51,
  	0,0,743,740,1,0,0,0,743,742,1,0,0,0,743,744,1,0,0,0,744,745,1,0,0,0,745,
  	748,5,60,0,0,746,748,5,55,0,0,747,743,1,0,0,0,747,746,1,0,0,0,748,756,
  	1,0,0,0,749,750,5,48,0,0,750,753,5,50,0,0,751,753,5,53,0,0,752,749,1,
  	0,0,0,752,751,1,0,0,0,752,753,1,0,0,0,753,754,1,0,0,0,754,757,5,59,0,
  	0,755,757,5,57,0,0,756,752,1,0,0,0,756,755,1,0,0,0,757,765,1,0,0,0,758,
  	759,5,47,0,0,759,762,5,50,0,0,760,762,5,52,0,0,761,758,1,0,0,0,761,760,
  	1,0,0,0,761,762,1,0,0,0,762,763,1,0,0,0,763,766,5,60,0,0,764,766,5,56,
  	0,0,765,761,1,0,0,0,765,764,1,0,0,0,766,774,1,0,0,0,767,768,5,49,0,0,
  	768,771,5,50,0,0,769,771,5,54,0,0,770,767,1,0,0,0,770,769,1,0,0,0,770,
  	771,1,0,0,0,771,772,1,0,0,0,772,775,5,59,0,0,773,775,5,58,0,0,774,770,
  	1,0,0,0,774,773,1,0,0,0,775,776,1,0,0,0,776,777,5,62,0,0,777,93,1,0,0,
  	0,778,779,5,27,0,0,779,780,3,118,59,0,780,781,3,116,58,0,781,782,3,118,
  	59,0,782,783,3,116,58,0,783,95,1,0,0,0,784,791,5,28,0,0,785,792,5,64,
  	0,0,786,788,5,66,0,0,787,789,5,66,0,0,788,787,1,0,0,0,788,789,1,0,0,0,
  	789,790,1,0,0,0,790,792,5,65,0,0,791,785,1,0,0,0,791,786,1,0,0,0,792,
  	793,1,0,0,0,793,794,5,68,0,0,794,97,1,0,0,0,795,799,5,29,0,0,796,798,
  	5,70,0,0,797,796,1,0,0,0,798,801,1,0,0,0,799,797,1,0,0,0,799,800,1,0,
  	0,0,800,802,1,0,0,0,801,799,1,0,0,0,802,803,5,72,0,0,803,99,1,0,0,0,804,
  	805,5,31,0,0,805,101,1,0,0,0,806,810,5,30,0,0,807,809,5,70,0,0,808,807,
  	1,0,0,0,809,812,1,0,0,0,810,808,1,0,0,0,810,811,1,0,0,0,811,813,1,0,0,
  	0,812,810,1,0,0,0,813,814,5,72,0,0,814,103,1,0,0,0,815,816,5,32,0,0,816,
  	817,5,64,0,0,817,818,5,68,0,0,818,105,1,0,0,0,819,820,5,33,0,0,820,822,
  	3,118,59,0,821,823,3,2,1,0,822,821,1,0,0,0,822,823,1,0,0,0,823,826,1,
  	0,0,0,824,827,3,108,54,0,825,827,3,2,1,0,826,824,1,0,0,0,826,825,1,0,
  	0,0,827,828,1,0,0,0,828,826,1,0,0,0,828,829,1,0,0,0,829,107,1,0,0,0,830,
  	831,5,34,0,0,831,832,5,76,0,0,832,834,5,77,0,0,833,835,5,76,0,0,834,833,
  	1,0,0,0,835,836,1,0,0,0,836,834,1,0,0,0,836,837,1,0,0,0,837,838,1,0,0,
  	0,838,839,5,79,0,0,839,109,1,0,0,0,840,841,5,33,0,0,841,843,3,118,59,
  	0,842,844,3,2,1,0,843,842,1,0,0,0,843,844,1,0,0,0,844,847,1,0,0,0,845,
  	848,3,112,56,0,846,848,3,2,1,0,847,845,1,0,0,0,847,846,1,0,0,0,848,849,
  	1,0,0,0,849,847,1,0,0,0,849,850,1,0,0,0,850,111,1,0,0,0,851,852,5,35,
  	0,0,852,853,7,5,0,0,853,856,5,77,0,0,854,855,5,76,0,0,855,857,5,75,0,
  	0,856,854,1,0,0,0,857,858,1,0,0,0,858,856,1,0,0,0,858,859,1,0,0,0,859,
  	860,1,0,0,0,860,861,5,79,0,0,861,113,1,0,0,0,862,863,7,6,0,0,863,115,
  	1,0,0,0,864,865,7,7,0,0,865,117,1,0,0,0,866,867,7,8,0,0,867,119,1,0,0,
  	0,868,869,7,9,0,0,869,121,1,0,0,0,870,871,7,10,0,0,871,123,1,0,0,0,872,
  	873,7,11,0,0,873,125,1,0,0,0,874,875,7,12,0,0,875,127,1,0,0,0,876,877,
  	7,12,0,0,877,129,1,0,0,0,125,134,169,171,180,188,198,201,204,207,210,
  	215,223,228,231,236,241,243,261,266,271,273,291,296,306,308,310,315,320,
  	331,333,335,340,345,357,359,361,366,372,380,382,387,393,402,404,409,415,
  	425,427,432,443,451,454,457,464,475,483,486,489,496,507,515,518,521,528,
  	540,543,546,553,562,568,570,576,578,581,584,594,598,605,617,620,623,626,
  	629,634,646,649,652,655,658,663,675,678,681,684,687,692,701,706,709,714,
  	722,725,728,731,734,743,747,752,756,761,765,770,774,788,791,799,810,822,
  	826,828,836,843,847,849,858
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

std::vector<CyanaMRParser::Ambig_listContext *> CyanaMRParser::Cyana_mrContext::ambig_list() {
  return getRuleContexts<CyanaMRParser::Ambig_listContext>();
}

CyanaMRParser::Ambig_listContext* CyanaMRParser::Cyana_mrContext::ambig_list(size_t i) {
  return getRuleContext<CyanaMRParser::Ambig_listContext>(i);
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
    setState(171);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 532527710052) != 0)) {
      setState(169);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(130);
        match(CyanaMRParser::Orientation_header);
        break;
      }

      case 2: {
        setState(132); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(131);
                  match(CyanaMRParser::Tensor_header);
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(134); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 3: {
        setState(136);
        comment();
        break;
      }

      case 4: {
        setState(137);
        distance_restraints();
        break;
      }

      case 5: {
        setState(138);
        fixres_distance_restraints();
        break;
      }

      case 6: {
        setState(139);
        fixresw_distance_restraints();
        break;
      }

      case 7: {
        setState(140);
        fixresw2_distance_restraints();
        break;
      }

      case 8: {
        setState(141);
        fixatm_distance_restraints();
        break;
      }

      case 9: {
        setState(142);
        fixatmw_distance_restraints();
        break;
      }

      case 10: {
        setState(143);
        fixatmw2_distance_restraints();
        break;
      }

      case 11: {
        setState(144);
        diana_distance_restraints();
        break;
      }

      case 12: {
        setState(145);
        diana_ssbond_restraints();
        break;
      }

      case 13: {
        setState(146);
        diana_hbond_restraints();
        break;
      }

      case 14: {
        setState(147);
        diana_torsion_angle_restraints();
        break;
      }

      case 15: {
        setState(148);
        diana_coupling_constant_restraints();
        break;
      }

      case 16: {
        setState(149);
        diana_stereoassign_macro();
        break;
      }

      case 17: {
        setState(150);
        distance_w_chain_restraints();
        break;
      }

      case 18: {
        setState(151);
        distance_w_chain2_restraints();
        break;
      }

      case 19: {
        setState(152);
        distance_w_chain3_restraints();
        break;
      }

      case 20: {
        setState(153);
        torsion_angle_restraints();
        break;
      }

      case 21: {
        setState(154);
        torsion_angle_w_chain_restraints();
        break;
      }

      case 22: {
        setState(155);
        rdc_restraints();
        break;
      }

      case 23: {
        setState(156);
        pcs_restraints();
        break;
      }

      case 24: {
        setState(157);
        cco_restraints();
        break;
      }

      case 25: {
        setState(158);
        ssbond_macro();
        break;
      }

      case 26: {
        setState(159);
        hbond_macro();
        break;
      }

      case 27: {
        setState(160);
        link_statement();
        break;
      }

      case 28: {
        setState(161);
        stereoassign_macro();
        break;
      }

      case 29: {
        setState(162);
        declare_variable();
        break;
      }

      case 30: {
        setState(163);
        set_variable();
        break;
      }

      case 31: {
        setState(164);
        unset_variable();
        break;
      }

      case 32: {
        setState(165);
        print_macro();
        break;
      }

      case 33: {
        setState(166);
        unambig_atom_name_mapping();
        break;
      }

      case 34: {
        setState(167);
        ambig_atom_name_mapping();
        break;
      }

      case 35: {
        setState(168);
        ambig_list();
        break;
      }

      default:
        break;
      }
      setState(173);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(174);
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
    setState(176);
    match(CyanaMRParser::COMMENT);
    setState(180);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Any_name) {
      setState(177);
      match(CyanaMRParser::Any_name);
      setState(182);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(183);
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
    setState(186); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(185);
              distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(188); 
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
    setState(190);
    gen_res_num();
    setState(191);
    gen_simple_name();
    setState(192);
    gen_atom_name();
    setState(193);
    gen_res_num();
    setState(194);
    gen_simple_name();
    setState(195);
    gen_atom_name();
    setState(196);
    number();
    setState(198);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx)) {
    case 1: {
      setState(197);
      number();
      break;
    }

    default:
      break;
    }
    setState(201);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 6, _ctx)) {
    case 1: {
      setState(200);
      number();
      break;
    }

    default:
      break;
    }
    setState(204);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx)) {
    case 1: {
      setState(203);
      number();
      break;
    }

    default:
      break;
    }
    setState(207);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx)) {
    case 1: {
      setState(206);
      number();
      break;
    }

    default:
      break;
    }
    setState(210);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx)) {
    case 1: {
      setState(209);
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
    setState(213); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(212);
              torsion_angle_restraint();
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
    setState(217);
    gen_res_num();
    setState(218);
    gen_simple_name();
    setState(219);
    gen_simple_name();
    setState(220);
    number();
    setState(221);
    number();
    setState(223);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx)) {
    case 1: {
      setState(222);
      number();
      break;
    }

    default:
      break;
    }
    setState(228);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Type) {
      setState(225);
      match(CyanaMRParser::Type);
      setState(226);
      match(CyanaMRParser::Equ_op);
      setState(227);
      match(CyanaMRParser::Integer);
    }
    setState(231);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Or) {
      setState(230);
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
    setState(234); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(233);
              rdc_parameter();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(236); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(241); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(241);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Orientation_header: {
                  setState(238);
                  match(CyanaMRParser::Orientation_header);
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(239);
                  comment();
                  break;
                }

                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(240);
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
      setState(243); 
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
    setState(245);
    match(CyanaMRParser::Integer);
    setState(246);
    number();
    setState(247);
    number();
    setState(248);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 481036337156) != 0))) {
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
    setState(250);
    gen_res_num();
    setState(251);
    gen_simple_name();
    setState(252);
    gen_simple_name();
    setState(253);
    gen_res_num();
    setState(254);
    gen_simple_name();
    setState(255);
    gen_simple_name();
    setState(256);
    number();
    setState(257);
    number();
    setState(258);
    number();
    setState(259);
    match(CyanaMRParser::Integer);
    setState(261);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx)) {
    case 1: {
      setState(260);
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
    setState(264); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(263);
              pcs_parameter();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(266); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(271); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(271);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Orientation_header: {
                  setState(268);
                  match(CyanaMRParser::Orientation_header);
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(269);
                  comment();
                  break;
                }

                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(270);
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
      setState(273); 
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
    setState(275);
    match(CyanaMRParser::Integer);
    setState(276);
    number();
    setState(277);
    number();
    setState(278);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 481036337156) != 0))) {
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
    setState(280);
    gen_res_num();
    setState(281);
    gen_simple_name();
    setState(282);
    gen_simple_name();
    setState(283);
    number();
    setState(284);
    number();
    setState(285);
    number();
    setState(286);
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
    setState(289); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(288);
              fixres_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(291); 
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

std::vector<tree::TerminalNode *> CyanaMRParser::Fixres_distance_restraintContext::Float() {
  return getTokens(CyanaMRParser::Float);
}

tree::TerminalNode* CyanaMRParser::Fixres_distance_restraintContext::Float(size_t i) {
  return getToken(CyanaMRParser::Float, i);
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
    setState(293);
    gen_res_num();
    setState(294);
    gen_simple_name();
    setState(296);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 22, _ctx)) {
    case 1: {
      setState(295);
      comment();
      break;
    }

    default:
      break;
    }
    setState(308); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(308);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(298);
                  gen_simple_name();
                  setState(299);
                  gen_res_num();
                  setState(300);
                  gen_simple_name();
                  setState(301);
                  gen_simple_name();
                  setState(302);
                  number();
                  break;
                }

                case CyanaMRParser::Float:
                case CyanaMRParser::COMMENT: {
                  setState(306);
                  _errHandler->sync(this);
                  switch (_input->LA(1)) {
                    case CyanaMRParser::COMMENT: {
                      setState(304);
                      comment();
                      break;
                    }

                    case CyanaMRParser::Float: {
                      setState(305);
                      match(CyanaMRParser::Float);
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
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(310); 
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
    setState(313); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(312);
              fixresw_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(315); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 26, _ctx);
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

std::vector<tree::TerminalNode *> CyanaMRParser::Fixresw_distance_restraintContext::Float() {
  return getTokens(CyanaMRParser::Float);
}

tree::TerminalNode* CyanaMRParser::Fixresw_distance_restraintContext::Float(size_t i) {
  return getToken(CyanaMRParser::Float, i);
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
    setState(317);
    gen_res_num();
    setState(318);
    gen_simple_name();
    setState(320);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 27, _ctx)) {
    case 1: {
      setState(319);
      comment();
      break;
    }

    default:
      break;
    }
    setState(333); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(333);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(322);
                  gen_simple_name();
                  setState(323);
                  gen_res_num();
                  setState(324);
                  gen_simple_name();
                  setState(325);
                  gen_simple_name();
                  setState(326);
                  number();
                  setState(327);
                  number();
                  break;
                }

                case CyanaMRParser::Float:
                case CyanaMRParser::COMMENT: {
                  setState(331);
                  _errHandler->sync(this);
                  switch (_input->LA(1)) {
                    case CyanaMRParser::COMMENT: {
                      setState(329);
                      comment();
                      break;
                    }

                    case CyanaMRParser::Float: {
                      setState(330);
                      match(CyanaMRParser::Float);
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
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(335); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 30, _ctx);
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
    setState(338); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(337);
              fixresw2_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(340); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 31, _ctx);
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

std::vector<tree::TerminalNode *> CyanaMRParser::Fixresw2_distance_restraintContext::Float() {
  return getTokens(CyanaMRParser::Float);
}

tree::TerminalNode* CyanaMRParser::Fixresw2_distance_restraintContext::Float(size_t i) {
  return getToken(CyanaMRParser::Float, i);
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
    setState(342);
    gen_res_num();
    setState(343);
    gen_simple_name();
    setState(345);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 32, _ctx)) {
    case 1: {
      setState(344);
      comment();
      break;
    }

    default:
      break;
    }
    setState(359); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(359);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(347);
                  gen_simple_name();
                  setState(348);
                  gen_res_num();
                  setState(349);
                  gen_simple_name();
                  setState(350);
                  gen_simple_name();
                  setState(351);
                  number();
                  setState(352);
                  number();
                  setState(353);
                  number();
                  break;
                }

                case CyanaMRParser::Float:
                case CyanaMRParser::COMMENT: {
                  setState(357);
                  _errHandler->sync(this);
                  switch (_input->LA(1)) {
                    case CyanaMRParser::COMMENT: {
                      setState(355);
                      comment();
                      break;
                    }

                    case CyanaMRParser::Float: {
                      setState(356);
                      match(CyanaMRParser::Float);
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
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(361); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 35, _ctx);
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
    setState(364); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(363);
              fixatm_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(366); 
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
    setState(368);
    gen_res_num();
    setState(369);
    gen_simple_name();
    setState(370);
    gen_simple_name();
    setState(372);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 37, _ctx)) {
    case 1: {
      setState(371);
      comment();
      break;
    }

    default:
      break;
    }
    setState(380); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(380);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(374);
                  gen_res_num();
                  setState(375);
                  gen_simple_name();
                  setState(376);
                  gen_simple_name();
                  setState(377);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(379);
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
      setState(382); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 39, _ctx);
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
    setState(385); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(384);
              fixatmw_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(387); 
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
    setState(389);
    gen_res_num();
    setState(390);
    gen_simple_name();
    setState(391);
    gen_simple_name();
    setState(393);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 41, _ctx)) {
    case 1: {
      setState(392);
      comment();
      break;
    }

    default:
      break;
    }
    setState(402); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(402);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(395);
                  gen_res_num();
                  setState(396);
                  gen_simple_name();
                  setState(397);
                  gen_simple_name();
                  setState(398);
                  number();
                  setState(399);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(401);
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
      setState(404); 
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
    setState(407); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(406);
              fixatmw2_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(409); 
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
    setState(411);
    gen_res_num();
    setState(412);
    gen_simple_name();
    setState(413);
    gen_simple_name();
    setState(415);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 45, _ctx)) {
    case 1: {
      setState(414);
      comment();
      break;
    }

    default:
      break;
    }
    setState(425); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(425);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(417);
                  gen_res_num();
                  setState(418);
                  gen_simple_name();
                  setState(419);
                  gen_simple_name();
                  setState(420);
                  number();
                  setState(421);
                  number();
                  setState(422);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(424);
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
      setState(427); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 47, _ctx);
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
    setState(430); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(429);
              diana_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(432); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 48, _ctx);
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

std::vector<CyanaMRParser::Gen_simple_name_qcContext *> CyanaMRParser::Diana_distance_restraintContext::gen_simple_name_qc() {
  return getRuleContexts<CyanaMRParser::Gen_simple_name_qcContext>();
}

CyanaMRParser::Gen_simple_name_qcContext* CyanaMRParser::Diana_distance_restraintContext::gen_simple_name_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_name_qcContext>(i);
}

std::vector<CyanaMRParser::Gen_res_num_qcContext *> CyanaMRParser::Diana_distance_restraintContext::gen_res_num_qc() {
  return getRuleContexts<CyanaMRParser::Gen_res_num_qcContext>();
}

CyanaMRParser::Gen_res_num_qcContext* CyanaMRParser::Diana_distance_restraintContext::gen_res_num_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_num_qcContext>(i);
}

std::vector<CyanaMRParser::Number_qcContext *> CyanaMRParser::Diana_distance_restraintContext::number_qc() {
  return getRuleContexts<CyanaMRParser::Number_qcContext>();
}

CyanaMRParser::Number_qcContext* CyanaMRParser::Diana_distance_restraintContext::number_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Number_qcContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_distance_restraintContext::RETURN_QC() {
  return getToken(CyanaMRParser::RETURN_QC, 0);
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

tree::TerminalNode* CyanaMRParser::Diana_distance_restraintContext::Simple_name_QC() {
  return getToken(CyanaMRParser::Simple_name_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_distance_restraintContext::Integer_QC() {
  return getToken(CyanaMRParser::Integer_QC, 0);
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
    setState(434);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 3584) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(435);
    gen_simple_name_qc();
    setState(436);
    gen_res_num_qc();
    setState(437);
    gen_simple_name_qc();
    setState(438);
    gen_simple_name_qc();
    setState(439);
    gen_res_num_qc();
    setState(440);
    gen_simple_name_qc();
    setState(441);
    number_qc();
    setState(443);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 49, _ctx)) {
    case 1: {
      setState(442);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(451);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 50, _ctx)) {
    case 1: {
      setState(445);
      gen_simple_name_qc();
      setState(446);
      gen_simple_name_qc();
      setState(447);
      gen_res_num_qc();
      setState(448);
      gen_simple_name_qc();
      setState(449);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(454);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Simple_name_QC) {
      setState(453);
      match(CyanaMRParser::Simple_name_QC);
    }
    setState(457);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Integer_QC) {
      setState(456);
      match(CyanaMRParser::Integer_QC);
    }
    setState(459);
    match(CyanaMRParser::RETURN_QC);
   
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
    setState(462); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(461);
              diana_ssbond_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(464); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 53, _ctx);
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

std::vector<CyanaMRParser::Gen_simple_name_qcContext *> CyanaMRParser::Diana_ssbond_restraintContext::gen_simple_name_qc() {
  return getRuleContexts<CyanaMRParser::Gen_simple_name_qcContext>();
}

CyanaMRParser::Gen_simple_name_qcContext* CyanaMRParser::Diana_ssbond_restraintContext::gen_simple_name_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_name_qcContext>(i);
}

std::vector<CyanaMRParser::Gen_res_num_qcContext *> CyanaMRParser::Diana_ssbond_restraintContext::gen_res_num_qc() {
  return getRuleContexts<CyanaMRParser::Gen_res_num_qcContext>();
}

CyanaMRParser::Gen_res_num_qcContext* CyanaMRParser::Diana_ssbond_restraintContext::gen_res_num_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_num_qcContext>(i);
}

std::vector<CyanaMRParser::Number_qcContext *> CyanaMRParser::Diana_ssbond_restraintContext::number_qc() {
  return getRuleContexts<CyanaMRParser::Number_qcContext>();
}

CyanaMRParser::Number_qcContext* CyanaMRParser::Diana_ssbond_restraintContext::number_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Number_qcContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::RETURN_QC() {
  return getToken(CyanaMRParser::RETURN_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::SSUpp() {
  return getToken(CyanaMRParser::SSUpp, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::SSLow() {
  return getToken(CyanaMRParser::SSLow, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::SSUpLo() {
  return getToken(CyanaMRParser::SSUpLo, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::Simple_name_QC() {
  return getToken(CyanaMRParser::Simple_name_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::Integer_QC() {
  return getToken(CyanaMRParser::Integer_QC, 0);
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
    setState(466);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 229376) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(467);
    gen_simple_name_qc();
    setState(468);
    gen_res_num_qc();
    setState(469);
    gen_simple_name_qc();
    setState(470);
    gen_simple_name_qc();
    setState(471);
    gen_res_num_qc();
    setState(472);
    gen_simple_name_qc();
    setState(473);
    number_qc();
    setState(475);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 54, _ctx)) {
    case 1: {
      setState(474);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(483);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 55, _ctx)) {
    case 1: {
      setState(477);
      gen_simple_name_qc();
      setState(478);
      gen_simple_name_qc();
      setState(479);
      gen_res_num_qc();
      setState(480);
      gen_simple_name_qc();
      setState(481);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(486);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Simple_name_QC) {
      setState(485);
      match(CyanaMRParser::Simple_name_QC);
    }
    setState(489);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Integer_QC) {
      setState(488);
      match(CyanaMRParser::Integer_QC);
    }
    setState(491);
    match(CyanaMRParser::RETURN_QC);
   
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
    setState(494); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(493);
              diana_hbond_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(496); 
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

//----------------- Diana_hbond_restraintContext ------------------------------------------------------------------

CyanaMRParser::Diana_hbond_restraintContext::Diana_hbond_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_name_qcContext *> CyanaMRParser::Diana_hbond_restraintContext::gen_simple_name_qc() {
  return getRuleContexts<CyanaMRParser::Gen_simple_name_qcContext>();
}

CyanaMRParser::Gen_simple_name_qcContext* CyanaMRParser::Diana_hbond_restraintContext::gen_simple_name_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_name_qcContext>(i);
}

std::vector<CyanaMRParser::Gen_res_num_qcContext *> CyanaMRParser::Diana_hbond_restraintContext::gen_res_num_qc() {
  return getRuleContexts<CyanaMRParser::Gen_res_num_qcContext>();
}

CyanaMRParser::Gen_res_num_qcContext* CyanaMRParser::Diana_hbond_restraintContext::gen_res_num_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_num_qcContext>(i);
}

std::vector<CyanaMRParser::Number_qcContext *> CyanaMRParser::Diana_hbond_restraintContext::number_qc() {
  return getRuleContexts<CyanaMRParser::Number_qcContext>();
}

CyanaMRParser::Number_qcContext* CyanaMRParser::Diana_hbond_restraintContext::number_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Number_qcContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_hbond_restraintContext::RETURN_QC() {
  return getToken(CyanaMRParser::RETURN_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_hbond_restraintContext::HBUpp() {
  return getToken(CyanaMRParser::HBUpp, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_hbond_restraintContext::HBLow() {
  return getToken(CyanaMRParser::HBLow, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_hbond_restraintContext::HBUpLo() {
  return getToken(CyanaMRParser::HBUpLo, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_hbond_restraintContext::Simple_name_QC() {
  return getToken(CyanaMRParser::Simple_name_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_hbond_restraintContext::Integer_QC() {
  return getToken(CyanaMRParser::Integer_QC, 0);
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
    setState(498);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 28672) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(499);
    gen_simple_name_qc();
    setState(500);
    gen_res_num_qc();
    setState(501);
    gen_simple_name_qc();
    setState(502);
    gen_simple_name_qc();
    setState(503);
    gen_res_num_qc();
    setState(504);
    gen_simple_name_qc();
    setState(505);
    number_qc();
    setState(507);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 59, _ctx)) {
    case 1: {
      setState(506);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(515);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 60, _ctx)) {
    case 1: {
      setState(509);
      gen_simple_name_qc();
      setState(510);
      gen_simple_name_qc();
      setState(511);
      gen_res_num_qc();
      setState(512);
      gen_simple_name_qc();
      setState(513);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(518);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Simple_name_QC) {
      setState(517);
      match(CyanaMRParser::Simple_name_QC);
    }
    setState(521);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Integer_QC) {
      setState(520);
      match(CyanaMRParser::Integer_QC);
    }
    setState(523);
    match(CyanaMRParser::RETURN_QC);
   
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
    setState(526); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(525);
              diana_torsion_angle_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(528); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 63, _ctx);
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

std::vector<CyanaMRParser::Gen_simple_name_qcContext *> CyanaMRParser::Diana_torsion_angle_restraintContext::gen_simple_name_qc() {
  return getRuleContexts<CyanaMRParser::Gen_simple_name_qcContext>();
}

CyanaMRParser::Gen_simple_name_qcContext* CyanaMRParser::Diana_torsion_angle_restraintContext::gen_simple_name_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_name_qcContext>(i);
}

CyanaMRParser::Gen_res_num_qcContext* CyanaMRParser::Diana_torsion_angle_restraintContext::gen_res_num_qc() {
  return getRuleContext<CyanaMRParser::Gen_res_num_qcContext>(0);
}

std::vector<CyanaMRParser::Number_qcContext *> CyanaMRParser::Diana_torsion_angle_restraintContext::number_qc() {
  return getRuleContexts<CyanaMRParser::Number_qcContext>();
}

CyanaMRParser::Number_qcContext* CyanaMRParser::Diana_torsion_angle_restraintContext::number_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Number_qcContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_torsion_angle_restraintContext::RETURN_QC() {
  return getToken(CyanaMRParser::RETURN_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_torsion_angle_restraintContext::Simple_name_QC() {
  return getToken(CyanaMRParser::Simple_name_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_torsion_angle_restraintContext::Integer_QC() {
  return getToken(CyanaMRParser::Integer_QC, 0);
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
    setState(530);
    match(CyanaMRParser::Angle);
    setState(531);
    gen_simple_name_qc();
    setState(532);
    gen_res_num_qc();
    setState(533);
    gen_simple_name_qc();
    setState(534);
    number_qc();
    setState(535);
    number_qc();
    setState(540);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 64, _ctx)) {
    case 1: {
      setState(536);
      gen_simple_name_qc();
      setState(537);
      number_qc();
      setState(538);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(543);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Simple_name_QC) {
      setState(542);
      match(CyanaMRParser::Simple_name_QC);
    }
    setState(546);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Integer_QC) {
      setState(545);
      match(CyanaMRParser::Integer_QC);
    }
    setState(548);
    match(CyanaMRParser::RETURN_QC);
   
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
    setState(551); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(550);
              diana_coupling_constant_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(553); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 67, _ctx);
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

std::vector<CyanaMRParser::Gen_simple_name_qcContext *> CyanaMRParser::Diana_coupling_constant_restraintContext::gen_simple_name_qc() {
  return getRuleContexts<CyanaMRParser::Gen_simple_name_qcContext>();
}

CyanaMRParser::Gen_simple_name_qcContext* CyanaMRParser::Diana_coupling_constant_restraintContext::gen_simple_name_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_name_qcContext>(i);
}

CyanaMRParser::Gen_res_num_qcContext* CyanaMRParser::Diana_coupling_constant_restraintContext::gen_res_num_qc() {
  return getRuleContext<CyanaMRParser::Gen_res_num_qcContext>(0);
}

std::vector<CyanaMRParser::Number_qcContext *> CyanaMRParser::Diana_coupling_constant_restraintContext::number_qc() {
  return getRuleContexts<CyanaMRParser::Number_qcContext>();
}

CyanaMRParser::Number_qcContext* CyanaMRParser::Diana_coupling_constant_restraintContext::number_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Number_qcContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_coupling_constant_restraintContext::RETURN_QC() {
  return getToken(CyanaMRParser::RETURN_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_coupling_constant_restraintContext::Simple_name_QC() {
  return getToken(CyanaMRParser::Simple_name_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_coupling_constant_restraintContext::Integer_QC() {
  return getToken(CyanaMRParser::Integer_QC, 0);
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
    setState(555);
    match(CyanaMRParser::Jcoupl);
    setState(556);
    gen_simple_name_qc();
    setState(557);
    gen_res_num_qc();
    setState(558);
    gen_simple_name_qc();
    setState(559);
    gen_simple_name_qc();
    setState(560);
    number_qc();
    setState(562);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 68, _ctx)) {
    case 1: {
      setState(561);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(570);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 70, _ctx)) {
    case 1: {
      setState(564);
      gen_simple_name_qc();
      setState(565);
      gen_simple_name_qc();
      setState(566);
      number_qc();
      setState(568);
      _errHandler->sync(this);

      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 69, _ctx)) {
      case 1: {
        setState(567);
        number_qc();
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
    setState(578);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 72, _ctx)) {
    case 1: {
      setState(572);
      gen_simple_name_qc();
      setState(573);
      gen_simple_name_qc();
      setState(574);
      number_qc();
      setState(576);
      _errHandler->sync(this);

      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 71, _ctx)) {
      case 1: {
        setState(575);
        number_qc();
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
    setState(581);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Simple_name_QC) {
      setState(580);
      match(CyanaMRParser::Simple_name_QC);
    }
    setState(584);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Integer_QC) {
      setState(583);
      match(CyanaMRParser::Integer_QC);
    }
    setState(586);
    match(CyanaMRParser::RETURN_QC);
   
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

std::vector<CyanaMRParser::Gen_simple_name_qcContext *> CyanaMRParser::Diana_stereoassign_macroContext::gen_simple_name_qc() {
  return getRuleContexts<CyanaMRParser::Gen_simple_name_qcContext>();
}

CyanaMRParser::Gen_simple_name_qcContext* CyanaMRParser::Diana_stereoassign_macroContext::gen_simple_name_qc(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_name_qcContext>(i);
}

CyanaMRParser::Gen_res_num_qcContext* CyanaMRParser::Diana_stereoassign_macroContext::gen_res_num_qc() {
  return getRuleContext<CyanaMRParser::Gen_res_num_qcContext>(0);
}

tree::TerminalNode* CyanaMRParser::Diana_stereoassign_macroContext::RETURN_QC() {
  return getToken(CyanaMRParser::RETURN_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_stereoassign_macroContext::Integer_QC() {
  return getToken(CyanaMRParser::Integer_QC, 0);
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
    setState(588);
    match(CyanaMRParser::Stereo);
    setState(589);
    gen_simple_name_qc();
    setState(590);
    gen_res_num_qc();
    setState(594);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((((_la - 84) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 84)) & 7) != 0)) {
      setState(591);
      gen_simple_name_qc();
      setState(596);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(598);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Integer_QC) {
      setState(597);
      match(CyanaMRParser::Integer_QC);
    }
    setState(600);
    match(CyanaMRParser::RETURN_QC);
   
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
  enterRule(_localctx, 70, CyanaMRParser::RuleDistance_w_chain_restraints);

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
    setState(603); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(602);
              distance_w_chain_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(605); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 77, _ctx);
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
  enterRule(_localctx, 72, CyanaMRParser::RuleDistance_w_chain_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(607);
    match(CyanaMRParser::Integer);
    setState(608);
    gen_simple_name();
    setState(609);
    gen_simple_name();
    setState(610);
    gen_simple_name();
    setState(611);
    match(CyanaMRParser::Integer);
    setState(612);
    gen_simple_name();
    setState(613);
    gen_simple_name();
    setState(614);
    gen_simple_name();
    setState(615);
    number();
    setState(617);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 78, _ctx)) {
    case 1: {
      setState(616);
      number();
      break;
    }

    default:
      break;
    }
    setState(620);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 79, _ctx)) {
    case 1: {
      setState(619);
      number();
      break;
    }

    default:
      break;
    }
    setState(623);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 80, _ctx)) {
    case 1: {
      setState(622);
      number();
      break;
    }

    default:
      break;
    }
    setState(626);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 81, _ctx)) {
    case 1: {
      setState(625);
      number();
      break;
    }

    default:
      break;
    }
    setState(629);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 82, _ctx)) {
    case 1: {
      setState(628);
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
  enterRule(_localctx, 74, CyanaMRParser::RuleDistance_w_chain2_restraints);

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
    setState(632); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(631);
              distance_w_chain2_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(634); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 83, _ctx);
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
  enterRule(_localctx, 76, CyanaMRParser::RuleDistance_w_chain2_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(636);
    gen_simple_name();
    setState(637);
    match(CyanaMRParser::Integer);
    setState(638);
    gen_simple_name();
    setState(639);
    gen_simple_name();
    setState(640);
    gen_simple_name();
    setState(641);
    match(CyanaMRParser::Integer);
    setState(642);
    gen_simple_name();
    setState(643);
    gen_simple_name();
    setState(644);
    number();
    setState(646);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 84, _ctx)) {
    case 1: {
      setState(645);
      number();
      break;
    }

    default:
      break;
    }
    setState(649);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 85, _ctx)) {
    case 1: {
      setState(648);
      number();
      break;
    }

    default:
      break;
    }
    setState(652);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 86, _ctx)) {
    case 1: {
      setState(651);
      number();
      break;
    }

    default:
      break;
    }
    setState(655);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 87, _ctx)) {
    case 1: {
      setState(654);
      number();
      break;
    }

    default:
      break;
    }
    setState(658);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 88, _ctx)) {
    case 1: {
      setState(657);
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
  enterRule(_localctx, 78, CyanaMRParser::RuleDistance_w_chain3_restraints);

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
    setState(661); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(660);
              distance_w_chain3_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(663); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 89, _ctx);
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
  enterRule(_localctx, 80, CyanaMRParser::RuleDistance_w_chain3_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(665);
    gen_simple_name();
    setState(666);
    gen_simple_name();
    setState(667);
    match(CyanaMRParser::Integer);
    setState(668);
    gen_simple_name();
    setState(669);
    gen_simple_name();
    setState(670);
    gen_simple_name();
    setState(671);
    match(CyanaMRParser::Integer);
    setState(672);
    gen_simple_name();
    setState(673);
    number();
    setState(675);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 90, _ctx)) {
    case 1: {
      setState(674);
      number();
      break;
    }

    default:
      break;
    }
    setState(678);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 91, _ctx)) {
    case 1: {
      setState(677);
      number();
      break;
    }

    default:
      break;
    }
    setState(681);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 92, _ctx)) {
    case 1: {
      setState(680);
      number();
      break;
    }

    default:
      break;
    }
    setState(684);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 93, _ctx)) {
    case 1: {
      setState(683);
      number();
      break;
    }

    default:
      break;
    }
    setState(687);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 94, _ctx)) {
    case 1: {
      setState(686);
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
  enterRule(_localctx, 82, CyanaMRParser::RuleTorsion_angle_w_chain_restraints);

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
    setState(690); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(689);
              torsion_angle_w_chain_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(692); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 95, _ctx);
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
  enterRule(_localctx, 84, CyanaMRParser::RuleTorsion_angle_w_chain_restraint);
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
    setState(694);
    gen_simple_name();
    setState(695);
    match(CyanaMRParser::Integer);
    setState(696);
    gen_simple_name();
    setState(697);
    gen_simple_name();
    setState(698);
    number();
    setState(699);
    number();
    setState(701);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 96, _ctx)) {
    case 1: {
      setState(700);
      number();
      break;
    }

    default:
      break;
    }
    setState(706);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Type) {
      setState(703);
      match(CyanaMRParser::Type);
      setState(704);
      match(CyanaMRParser::Equ_op);
      setState(705);
      match(CyanaMRParser::Integer);
    }
    setState(709);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Or) {
      setState(708);
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
  enterRule(_localctx, 86, CyanaMRParser::RuleCco_restraints);

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
    setState(712); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(711);
              cco_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(714); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 99, _ctx);
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
  enterRule(_localctx, 88, CyanaMRParser::RuleCco_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(716);
    gen_res_num();
    setState(717);
    gen_simple_name();
    setState(718);
    gen_simple_name();
    setState(719);
    gen_simple_name();
    setState(720);
    number();
    setState(722);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 100, _ctx)) {
    case 1: {
      setState(721);
      number();
      break;
    }

    default:
      break;
    }
    setState(725);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 101, _ctx)) {
    case 1: {
      setState(724);
      number();
      break;
    }

    default:
      break;
    }
    setState(728);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 102, _ctx)) {
    case 1: {
      setState(727);
      number();
      break;
    }

    default:
      break;
    }
    setState(731);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 103, _ctx)) {
    case 1: {
      setState(730);
      number();
      break;
    }

    default:
      break;
    }
    setState(734);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 104, _ctx)) {
    case 1: {
      setState(733);
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
  enterRule(_localctx, 90, CyanaMRParser::RuleSsbond_macro);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(736);
    match(CyanaMRParser::Ssbond);
    setState(737);
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
  enterRule(_localctx, 92, CyanaMRParser::RuleHbond_macro);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(739);
    match(CyanaMRParser::Hbond);
    setState(747);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Atom1:
      case CyanaMRParser::Atom1_equ:
      case CyanaMRParser::Simple_name_HB: {
        setState(743);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CyanaMRParser::Atom1: {
            setState(740);
            match(CyanaMRParser::Atom1);
            setState(741);
            match(CyanaMRParser::Equ_op_HB);
            break;
          }

          case CyanaMRParser::Atom1_equ: {
            setState(742);
            match(CyanaMRParser::Atom1_equ);
            break;
          }

          case CyanaMRParser::Simple_name_HB: {
            break;
          }

        default:
          break;
        }
        setState(745);
        match(CyanaMRParser::Simple_name_HB);
        break;
      }

      case CyanaMRParser::Concat_atom_1: {
        setState(746);
        match(CyanaMRParser::Concat_atom_1);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(756);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Residue1:
      case CyanaMRParser::Residue1_equ:
      case CyanaMRParser::Integer_HB: {
        setState(752);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CyanaMRParser::Residue1: {
            setState(749);
            match(CyanaMRParser::Residue1);
            setState(750);
            match(CyanaMRParser::Equ_op_HB);
            break;
          }

          case CyanaMRParser::Residue1_equ: {
            setState(751);
            match(CyanaMRParser::Residue1_equ);
            break;
          }

          case CyanaMRParser::Integer_HB: {
            break;
          }

        default:
          break;
        }
        setState(754);
        match(CyanaMRParser::Integer_HB);
        break;
      }

      case CyanaMRParser::Concat_res_1: {
        setState(755);
        match(CyanaMRParser::Concat_res_1);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(765);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Atom2:
      case CyanaMRParser::Atom2_equ:
      case CyanaMRParser::Simple_name_HB: {
        setState(761);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CyanaMRParser::Atom2: {
            setState(758);
            match(CyanaMRParser::Atom2);
            setState(759);
            match(CyanaMRParser::Equ_op_HB);
            break;
          }

          case CyanaMRParser::Atom2_equ: {
            setState(760);
            match(CyanaMRParser::Atom2_equ);
            break;
          }

          case CyanaMRParser::Simple_name_HB: {
            break;
          }

        default:
          break;
        }
        setState(763);
        match(CyanaMRParser::Simple_name_HB);
        break;
      }

      case CyanaMRParser::Concat_atom_2: {
        setState(764);
        match(CyanaMRParser::Concat_atom_2);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(774);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Residue2:
      case CyanaMRParser::Residue2_equ:
      case CyanaMRParser::Integer_HB: {
        setState(770);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CyanaMRParser::Residue2: {
            setState(767);
            match(CyanaMRParser::Residue2);
            setState(768);
            match(CyanaMRParser::Equ_op_HB);
            break;
          }

          case CyanaMRParser::Residue2_equ: {
            setState(769);
            match(CyanaMRParser::Residue2_equ);
            break;
          }

          case CyanaMRParser::Integer_HB: {
            break;
          }

        default:
          break;
        }
        setState(772);
        match(CyanaMRParser::Integer_HB);
        break;
      }

      case CyanaMRParser::Concat_res_2: {
        setState(773);
        match(CyanaMRParser::Concat_res_2);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(776);
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
  enterRule(_localctx, 94, CyanaMRParser::RuleLink_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(778);
    match(CyanaMRParser::Link);
    setState(779);
    gen_simple_name();
    setState(780);
    gen_res_num();
    setState(781);
    gen_simple_name();
    setState(782);
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

tree::TerminalNode* CyanaMRParser::Stereoassign_macroContext::RETURN_PR() {
  return getToken(CyanaMRParser::RETURN_PR, 0);
}

tree::TerminalNode* CyanaMRParser::Stereoassign_macroContext::Double_quote_string() {
  return getToken(CyanaMRParser::Double_quote_string, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Stereoassign_macroContext::Simple_name_PR() {
  return getTokens(CyanaMRParser::Simple_name_PR);
}

tree::TerminalNode* CyanaMRParser::Stereoassign_macroContext::Simple_name_PR(size_t i) {
  return getToken(CyanaMRParser::Simple_name_PR, i);
}

tree::TerminalNode* CyanaMRParser::Stereoassign_macroContext::Integer_PR() {
  return getToken(CyanaMRParser::Integer_PR, 0);
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
  enterRule(_localctx, 96, CyanaMRParser::RuleStereoassign_macro);
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
    setState(784);
    match(CyanaMRParser::Atom_stereo);
    setState(791);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Double_quote_string: {
        setState(785);
        match(CyanaMRParser::Double_quote_string);
        break;
      }

      case CyanaMRParser::Simple_name_PR: {
        setState(786);
        match(CyanaMRParser::Simple_name_PR);
        setState(788);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CyanaMRParser::Simple_name_PR) {
          setState(787);
          match(CyanaMRParser::Simple_name_PR);
        }
        setState(790);
        match(CyanaMRParser::Integer_PR);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(793);
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
  enterRule(_localctx, 98, CyanaMRParser::RuleDeclare_variable);
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
    setState(795);
    match(CyanaMRParser::Var);
    setState(799);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Simple_name_VA) {
      setState(796);
      match(CyanaMRParser::Simple_name_VA);
      setState(801);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(802);
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
  enterRule(_localctx, 100, CyanaMRParser::RuleSet_variable);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(804);
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
  enterRule(_localctx, 102, CyanaMRParser::RuleUnset_variable);
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
    setState(806);
    match(CyanaMRParser::Unset);
    setState(810);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Simple_name_VA) {
      setState(807);
      match(CyanaMRParser::Simple_name_VA);
      setState(812);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(813);
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
  enterRule(_localctx, 104, CyanaMRParser::RulePrint_macro);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(815);
    match(CyanaMRParser::Print);
    setState(816);
    match(CyanaMRParser::Double_quote_string);
    setState(817);
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
  enterRule(_localctx, 106, CyanaMRParser::RuleUnambig_atom_name_mapping);

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
    setState(819);
    match(CyanaMRParser::Residue);
    setState(820);
    gen_simple_name();
    setState(822);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 117, _ctx)) {
    case 1: {
      setState(821);
      comment();
      break;
    }

    default:
      break;
    }
    setState(826); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(826);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Mapping: {
                  setState(824);
                  mapping_list();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(825);
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
      setState(828); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 119, _ctx);
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
  enterRule(_localctx, 108, CyanaMRParser::RuleMapping_list);
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
    setState(830);
    match(CyanaMRParser::Mapping);
    setState(831);
    match(CyanaMRParser::Simple_name_MP);
    setState(832);
    match(CyanaMRParser::Equ_op_MP);
    setState(834); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(833);
      match(CyanaMRParser::Simple_name_MP);
      setState(836); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == CyanaMRParser::Simple_name_MP);
    setState(838);
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
  enterRule(_localctx, 110, CyanaMRParser::RuleAmbig_atom_name_mapping);

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
    setState(840);
    match(CyanaMRParser::Residue);
    setState(841);
    gen_simple_name();
    setState(843);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 121, _ctx)) {
    case 1: {
      setState(842);
      comment();
      break;
    }

    default:
      break;
    }
    setState(847); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(847);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Ambig: {
                  setState(845);
                  ambig_list();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(846);
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
      setState(849); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 123, _ctx);
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
  enterRule(_localctx, 112, CyanaMRParser::RuleAmbig_list);
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
    setState(851);
    match(CyanaMRParser::Ambig);
    setState(852);
    _la = _input->LA(1);
    if (!(_la == CyanaMRParser::Ambig_code_MP

    || _la == CyanaMRParser::Simple_name_MP)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(853);
    match(CyanaMRParser::Equ_op_MP);
    setState(856); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(854);
      match(CyanaMRParser::Simple_name_MP);
      setState(855);
      match(CyanaMRParser::Integer_MP);
      setState(858); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == CyanaMRParser::Simple_name_MP);
    setState(860);
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
  enterRule(_localctx, 114, CyanaMRParser::RuleNumber);
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
    setState(862);
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
  enterRule(_localctx, 116, CyanaMRParser::RuleGen_res_num);
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
    setState(864);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 206158430212) != 0))) {
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
  enterRule(_localctx, 118, CyanaMRParser::RuleGen_simple_name);
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
    setState(866);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 481036337152) != 0))) {
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
  enterRule(_localctx, 120, CyanaMRParser::RuleGen_atom_name);
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
    setState(868);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 481036337154) != 0))) {
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

//----------------- Number_qcContext ------------------------------------------------------------------

CyanaMRParser::Number_qcContext::Number_qcContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Number_qcContext::Float_QC() {
  return getToken(CyanaMRParser::Float_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Number_qcContext::Float_DecimalComma_QC() {
  return getToken(CyanaMRParser::Float_DecimalComma_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Number_qcContext::Integer_QC() {
  return getToken(CyanaMRParser::Integer_QC, 0);
}


size_t CyanaMRParser::Number_qcContext::getRuleIndex() const {
  return CyanaMRParser::RuleNumber_qc;
}


std::any CyanaMRParser::Number_qcContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber_qc(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Number_qcContext* CyanaMRParser::number_qc() {
  Number_qcContext *_localctx = _tracker.createInstance<Number_qcContext>(_ctx, getState());
  enterRule(_localctx, 122, CyanaMRParser::RuleNumber_qc);
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
    setState(870);
    _la = _input->LA(1);
    if (!(((((_la - 81) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 81)) & 7) != 0))) {
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

//----------------- Gen_res_num_qcContext ------------------------------------------------------------------

CyanaMRParser::Gen_res_num_qcContext::Gen_res_num_qcContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Gen_res_num_qcContext::Integer_QC() {
  return getToken(CyanaMRParser::Integer_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_res_num_qcContext::Capital_integer_QC() {
  return getToken(CyanaMRParser::Capital_integer_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_res_num_qcContext::Integer_capital_QC() {
  return getToken(CyanaMRParser::Integer_capital_QC, 0);
}


size_t CyanaMRParser::Gen_res_num_qcContext::getRuleIndex() const {
  return CyanaMRParser::RuleGen_res_num_qc;
}


std::any CyanaMRParser::Gen_res_num_qcContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitGen_res_num_qc(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Gen_res_num_qcContext* CyanaMRParser::gen_res_num_qc() {
  Gen_res_num_qcContext *_localctx = _tracker.createInstance<Gen_res_num_qcContext>(_ctx, getState());
  enterRule(_localctx, 124, CyanaMRParser::RuleGen_res_num_qc);
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
    setState(872);
    _la = _input->LA(1);
    if (!(((((_la - 81) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 81)) & 49) != 0))) {
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

//----------------- Gen_simple_name_qcContext ------------------------------------------------------------------

CyanaMRParser::Gen_simple_name_qcContext::Gen_simple_name_qcContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Gen_simple_name_qcContext::Simple_name_QC() {
  return getToken(CyanaMRParser::Simple_name_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_simple_name_qcContext::Capital_integer_QC() {
  return getToken(CyanaMRParser::Capital_integer_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_simple_name_qcContext::Integer_capital_QC() {
  return getToken(CyanaMRParser::Integer_capital_QC, 0);
}


size_t CyanaMRParser::Gen_simple_name_qcContext::getRuleIndex() const {
  return CyanaMRParser::RuleGen_simple_name_qc;
}


std::any CyanaMRParser::Gen_simple_name_qcContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitGen_simple_name_qc(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Gen_simple_name_qcContext* CyanaMRParser::gen_simple_name_qc() {
  Gen_simple_name_qcContext *_localctx = _tracker.createInstance<Gen_simple_name_qcContext>(_ctx, getState());
  enterRule(_localctx, 126, CyanaMRParser::RuleGen_simple_name_qc);
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
    setState(874);
    _la = _input->LA(1);
    if (!(((((_la - 84) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 84)) & 7) != 0))) {
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

//----------------- Gen_atom_name_qcContext ------------------------------------------------------------------

CyanaMRParser::Gen_atom_name_qcContext::Gen_atom_name_qcContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Gen_atom_name_qcContext::Simple_name_QC() {
  return getToken(CyanaMRParser::Simple_name_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_atom_name_qcContext::Capital_integer_QC() {
  return getToken(CyanaMRParser::Capital_integer_QC, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_atom_name_qcContext::Integer_capital_QC() {
  return getToken(CyanaMRParser::Integer_capital_QC, 0);
}


size_t CyanaMRParser::Gen_atom_name_qcContext::getRuleIndex() const {
  return CyanaMRParser::RuleGen_atom_name_qc;
}


std::any CyanaMRParser::Gen_atom_name_qcContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitGen_atom_name_qc(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Gen_atom_name_qcContext* CyanaMRParser::gen_atom_name_qc() {
  Gen_atom_name_qcContext *_localctx = _tracker.createInstance<Gen_atom_name_qcContext>(_ctx, getState());
  enterRule(_localctx, 128, CyanaMRParser::RuleGen_atom_name_qc);
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
    setState(876);
    _la = _input->LA(1);
    if (!(((((_la - 84) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 84)) & 7) != 0))) {
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
