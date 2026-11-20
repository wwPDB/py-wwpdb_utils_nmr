
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
      "pcs_no_param_restraints", "pcs_no_param_restraint", "ssbond_macro", 
      "hbond_macro", "link_statement", "stereoassign_macro", "declare_variable", 
      "set_variable", "unset_variable", "print_macro", "unambig_atom_name_mapping", 
      "mapping_list", "ambig_atom_name_mapping", "ambig_list", "number", 
      "gen_res_num", "gen_simple_name", "gen_atom_name", "number_qc", "gen_res_num_qc", 
      "gen_simple_name_qc", "gen_atom_name_qc"
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
  	4,1,88,898,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,
  	35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,
  	42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,
  	49,2,50,7,50,2,51,7,51,2,52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,
  	56,2,57,7,57,2,58,7,58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,
  	63,2,64,7,64,2,65,7,65,2,66,7,66,1,0,1,0,4,0,137,8,0,11,0,12,0,138,1,
  	0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
  	1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,175,
  	8,0,10,0,12,0,178,9,0,1,0,1,0,1,1,1,1,5,1,184,8,1,10,1,12,1,187,9,1,1,
  	1,1,1,1,2,4,2,192,8,2,11,2,12,2,193,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,
  	3,204,8,3,1,3,3,3,207,8,3,1,3,3,3,210,8,3,1,3,3,3,213,8,3,1,3,3,3,216,
  	8,3,1,4,4,4,219,8,4,11,4,12,4,220,1,5,1,5,1,5,1,5,1,5,1,5,3,5,229,8,5,
  	1,5,1,5,1,5,3,5,234,8,5,1,5,3,5,237,8,5,1,6,4,6,240,8,6,11,6,12,6,241,
  	1,6,1,6,1,6,4,6,247,8,6,11,6,12,6,248,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,
  	1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,267,8,8,1,9,4,9,270,8,9,11,9,12,9,
  	271,1,9,1,9,1,9,4,9,277,8,9,11,9,12,9,278,1,10,1,10,1,10,1,10,1,10,1,
  	11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,4,12,295,8,12,11,12,12,12,
  	296,1,13,1,13,1,13,3,13,302,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
  	13,3,13,312,8,13,4,13,314,8,13,11,13,12,13,315,1,14,4,14,319,8,14,11,
  	14,12,14,320,1,15,1,15,1,15,3,15,326,8,15,1,15,1,15,1,15,1,15,1,15,1,
  	15,1,15,1,15,1,15,3,15,337,8,15,4,15,339,8,15,11,15,12,15,340,1,16,4,
  	16,344,8,16,11,16,12,16,345,1,17,1,17,1,17,3,17,351,8,17,1,17,1,17,1,
  	17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,363,8,17,4,17,365,8,17,11,
  	17,12,17,366,1,18,4,18,370,8,18,11,18,12,18,371,1,19,1,19,1,19,1,19,3,
  	19,378,8,19,1,19,1,19,1,19,1,19,1,19,1,19,4,19,386,8,19,11,19,12,19,387,
  	1,20,4,20,391,8,20,11,20,12,20,392,1,21,1,21,1,21,1,21,3,21,399,8,21,
  	1,21,1,21,1,21,1,21,1,21,1,21,1,21,4,21,408,8,21,11,21,12,21,409,1,22,
  	4,22,413,8,22,11,22,12,22,414,1,23,1,23,1,23,1,23,3,23,421,8,23,1,23,
  	1,23,1,23,1,23,1,23,1,23,1,23,1,23,4,23,431,8,23,11,23,12,23,432,1,24,
  	4,24,436,8,24,11,24,12,24,437,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
  	1,25,3,25,449,8,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,457,8,25,1,25,3,
  	25,460,8,25,1,25,3,25,463,8,25,1,25,1,25,1,26,4,26,468,8,26,11,26,12,
  	26,469,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,481,8,27,1,27,
  	1,27,1,27,1,27,1,27,1,27,3,27,489,8,27,1,27,3,27,492,8,27,1,27,3,27,495,
  	8,27,1,27,1,27,1,28,4,28,500,8,28,11,28,12,28,501,1,29,1,29,1,29,1,29,
  	1,29,1,29,1,29,1,29,1,29,3,29,513,8,29,1,29,1,29,1,29,1,29,1,29,1,29,
  	3,29,521,8,29,1,29,3,29,524,8,29,1,29,3,29,527,8,29,1,29,1,29,1,30,4,
  	30,532,8,30,11,30,12,30,533,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,
  	31,1,31,3,31,546,8,31,1,31,3,31,549,8,31,1,31,3,31,552,8,31,1,31,1,31,
  	1,32,4,32,557,8,32,11,32,12,32,558,1,33,1,33,1,33,1,33,1,33,1,33,1,33,
  	3,33,568,8,33,1,33,1,33,1,33,1,33,3,33,574,8,33,3,33,576,8,33,1,33,1,
  	33,1,33,1,33,3,33,582,8,33,3,33,584,8,33,1,33,3,33,587,8,33,1,33,3,33,
  	590,8,33,1,33,1,33,1,34,1,34,1,34,1,34,5,34,598,8,34,10,34,12,34,601,
  	9,34,1,34,3,34,604,8,34,1,34,1,34,1,35,4,35,609,8,35,11,35,12,35,610,
  	1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,623,8,36,1,36,
  	3,36,626,8,36,1,36,3,36,629,8,36,1,36,3,36,632,8,36,1,36,3,36,635,8,36,
  	1,37,4,37,638,8,37,11,37,12,37,639,1,38,1,38,1,38,1,38,1,38,1,38,1,38,
  	1,38,1,38,1,38,3,38,652,8,38,1,38,3,38,655,8,38,1,38,3,38,658,8,38,1,
  	38,3,38,661,8,38,1,38,3,38,664,8,38,1,39,4,39,667,8,39,11,39,12,39,668,
  	1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,681,8,40,1,40,
  	3,40,684,8,40,1,40,3,40,687,8,40,1,40,3,40,690,8,40,1,40,3,40,693,8,40,
  	1,41,4,41,696,8,41,11,41,12,41,697,1,42,1,42,1,42,1,42,1,42,1,42,1,42,
  	3,42,707,8,42,1,42,1,42,1,42,3,42,712,8,42,1,42,3,42,715,8,42,1,43,4,
  	43,718,8,43,11,43,12,43,719,1,44,1,44,1,44,1,44,1,44,1,44,3,44,728,8,
  	44,1,44,3,44,731,8,44,1,44,3,44,734,8,44,1,44,3,44,737,8,44,1,44,3,44,
  	740,8,44,1,45,4,45,743,8,45,11,45,12,45,744,1,46,1,46,1,46,1,46,1,46,
  	1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,48,1,48,1,48,1,48,3,48,763,8,48,
  	1,48,1,48,3,48,767,8,48,1,48,1,48,1,48,3,48,772,8,48,1,48,1,48,3,48,776,
  	8,48,1,48,1,48,1,48,3,48,781,8,48,1,48,1,48,3,48,785,8,48,1,48,1,48,1,
  	48,3,48,790,8,48,1,48,1,48,3,48,794,8,48,1,48,1,48,1,49,1,49,1,49,1,49,
  	1,49,1,49,1,50,1,50,1,50,1,50,3,50,808,8,50,1,50,3,50,811,8,50,1,50,1,
  	50,1,51,1,51,5,51,817,8,51,10,51,12,51,820,9,51,1,51,1,51,1,52,1,52,1,
  	53,1,53,5,53,828,8,53,10,53,12,53,831,9,53,1,53,1,53,1,54,1,54,1,54,1,
  	54,1,55,1,55,1,55,3,55,842,8,55,1,55,1,55,4,55,846,8,55,11,55,12,55,847,
  	1,56,1,56,1,56,1,56,4,56,854,8,56,11,56,12,56,855,1,56,1,56,1,57,1,57,
  	1,57,3,57,863,8,57,1,57,1,57,4,57,867,8,57,11,57,12,57,868,1,58,1,58,
  	1,58,1,58,1,58,4,58,876,8,58,11,58,12,58,877,1,58,1,58,1,59,1,59,1,60,
  	1,60,1,61,1,61,1,62,1,62,1,63,1,63,1,64,1,64,1,65,1,65,1,66,1,66,1,66,
  	0,0,67,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
  	46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,
  	92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,
  	130,132,0,13,1,1,45,45,2,0,2,2,36,38,1,0,9,11,1,0,15,17,1,0,12,14,2,0,
  	74,74,76,76,1,0,2,4,2,0,2,2,36,37,1,0,36,38,2,0,1,1,36,38,1,0,81,83,2,
  	0,81,81,85,86,1,0,84,86,996,0,176,1,0,0,0,2,181,1,0,0,0,4,191,1,0,0,0,
  	6,195,1,0,0,0,8,218,1,0,0,0,10,222,1,0,0,0,12,239,1,0,0,0,14,250,1,0,
  	0,0,16,255,1,0,0,0,18,269,1,0,0,0,20,280,1,0,0,0,22,285,1,0,0,0,24,294,
  	1,0,0,0,26,298,1,0,0,0,28,318,1,0,0,0,30,322,1,0,0,0,32,343,1,0,0,0,34,
  	347,1,0,0,0,36,369,1,0,0,0,38,373,1,0,0,0,40,390,1,0,0,0,42,394,1,0,0,
  	0,44,412,1,0,0,0,46,416,1,0,0,0,48,435,1,0,0,0,50,439,1,0,0,0,52,467,
  	1,0,0,0,54,471,1,0,0,0,56,499,1,0,0,0,58,503,1,0,0,0,60,531,1,0,0,0,62,
  	535,1,0,0,0,64,556,1,0,0,0,66,560,1,0,0,0,68,593,1,0,0,0,70,608,1,0,0,
  	0,72,612,1,0,0,0,74,637,1,0,0,0,76,641,1,0,0,0,78,666,1,0,0,0,80,670,
  	1,0,0,0,82,695,1,0,0,0,84,699,1,0,0,0,86,717,1,0,0,0,88,721,1,0,0,0,90,
  	742,1,0,0,0,92,746,1,0,0,0,94,755,1,0,0,0,96,758,1,0,0,0,98,797,1,0,0,
  	0,100,803,1,0,0,0,102,814,1,0,0,0,104,823,1,0,0,0,106,825,1,0,0,0,108,
  	834,1,0,0,0,110,838,1,0,0,0,112,849,1,0,0,0,114,859,1,0,0,0,116,870,1,
  	0,0,0,118,881,1,0,0,0,120,883,1,0,0,0,122,885,1,0,0,0,124,887,1,0,0,0,
  	126,889,1,0,0,0,128,891,1,0,0,0,130,893,1,0,0,0,132,895,1,0,0,0,134,175,
  	5,5,0,0,135,137,5,6,0,0,136,135,1,0,0,0,137,138,1,0,0,0,138,136,1,0,0,
  	0,138,139,1,0,0,0,139,175,1,0,0,0,140,175,3,2,1,0,141,175,3,4,2,0,142,
  	175,3,24,12,0,143,175,3,28,14,0,144,175,3,32,16,0,145,175,3,36,18,0,146,
  	175,3,40,20,0,147,175,3,44,22,0,148,175,3,48,24,0,149,175,3,52,26,0,150,
  	175,3,56,28,0,151,175,3,60,30,0,152,175,3,64,32,0,153,175,3,68,34,0,154,
  	175,3,70,35,0,155,175,3,74,37,0,156,175,3,78,39,0,157,175,3,8,4,0,158,
  	175,3,82,41,0,159,175,3,12,6,0,160,175,3,18,9,0,161,175,3,86,43,0,162,
  	175,3,90,45,0,163,175,3,94,47,0,164,175,3,96,48,0,165,175,3,98,49,0,166,
  	175,3,100,50,0,167,175,3,102,51,0,168,175,3,104,52,0,169,175,3,106,53,
  	0,170,175,3,108,54,0,171,175,3,110,55,0,172,175,3,114,57,0,173,175,3,
  	116,58,0,174,134,1,0,0,0,174,136,1,0,0,0,174,140,1,0,0,0,174,141,1,0,
  	0,0,174,142,1,0,0,0,174,143,1,0,0,0,174,144,1,0,0,0,174,145,1,0,0,0,174,
  	146,1,0,0,0,174,147,1,0,0,0,174,148,1,0,0,0,174,149,1,0,0,0,174,150,1,
  	0,0,0,174,151,1,0,0,0,174,152,1,0,0,0,174,153,1,0,0,0,174,154,1,0,0,0,
  	174,155,1,0,0,0,174,156,1,0,0,0,174,157,1,0,0,0,174,158,1,0,0,0,174,159,
  	1,0,0,0,174,160,1,0,0,0,174,161,1,0,0,0,174,162,1,0,0,0,174,163,1,0,0,
  	0,174,164,1,0,0,0,174,165,1,0,0,0,174,166,1,0,0,0,174,167,1,0,0,0,174,
  	168,1,0,0,0,174,169,1,0,0,0,174,170,1,0,0,0,174,171,1,0,0,0,174,172,1,
  	0,0,0,174,173,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,
  	177,179,1,0,0,0,178,176,1,0,0,0,179,180,5,0,0,1,180,1,1,0,0,0,181,185,
  	5,8,0,0,182,184,5,43,0,0,183,182,1,0,0,0,184,187,1,0,0,0,185,183,1,0,
  	0,0,185,186,1,0,0,0,186,188,1,0,0,0,187,185,1,0,0,0,188,189,7,0,0,0,189,
  	3,1,0,0,0,190,192,3,6,3,0,191,190,1,0,0,0,192,193,1,0,0,0,193,191,1,0,
  	0,0,193,194,1,0,0,0,194,5,1,0,0,0,195,196,3,120,60,0,196,197,3,122,61,
  	0,197,198,3,124,62,0,198,199,3,120,60,0,199,200,3,122,61,0,200,201,3,
  	124,62,0,201,203,3,118,59,0,202,204,3,118,59,0,203,202,1,0,0,0,203,204,
  	1,0,0,0,204,206,1,0,0,0,205,207,3,118,59,0,206,205,1,0,0,0,206,207,1,
  	0,0,0,207,209,1,0,0,0,208,210,3,118,59,0,209,208,1,0,0,0,209,210,1,0,
  	0,0,210,212,1,0,0,0,211,213,3,118,59,0,212,211,1,0,0,0,212,213,1,0,0,
  	0,213,215,1,0,0,0,214,216,3,118,59,0,215,214,1,0,0,0,215,216,1,0,0,0,
  	216,7,1,0,0,0,217,219,3,10,5,0,218,217,1,0,0,0,219,220,1,0,0,0,220,218,
  	1,0,0,0,220,221,1,0,0,0,221,9,1,0,0,0,222,223,3,120,60,0,223,224,3,122,
  	61,0,224,225,3,122,61,0,225,226,3,118,59,0,226,228,3,118,59,0,227,229,
  	3,118,59,0,228,227,1,0,0,0,228,229,1,0,0,0,229,233,1,0,0,0,230,231,5,
  	21,0,0,231,232,5,22,0,0,232,234,5,2,0,0,233,230,1,0,0,0,233,234,1,0,0,
  	0,234,236,1,0,0,0,235,237,5,23,0,0,236,235,1,0,0,0,236,237,1,0,0,0,237,
  	11,1,0,0,0,238,240,3,14,7,0,239,238,1,0,0,0,240,241,1,0,0,0,241,239,1,
  	0,0,0,241,242,1,0,0,0,242,246,1,0,0,0,243,247,5,5,0,0,244,247,3,2,1,0,
  	245,247,3,16,8,0,246,243,1,0,0,0,246,244,1,0,0,0,246,245,1,0,0,0,247,
  	248,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,13,1,0,0,0,250,251,5,
  	2,0,0,251,252,3,118,59,0,252,253,3,118,59,0,253,254,7,1,0,0,254,15,1,
  	0,0,0,255,256,3,120,60,0,256,257,3,122,61,0,257,258,3,122,61,0,258,259,
  	3,120,60,0,259,260,3,122,61,0,260,261,3,122,61,0,261,262,3,118,59,0,262,
  	263,3,118,59,0,263,264,3,118,59,0,264,266,5,2,0,0,265,267,3,118,59,0,
  	266,265,1,0,0,0,266,267,1,0,0,0,267,17,1,0,0,0,268,270,3,20,10,0,269,
  	268,1,0,0,0,270,271,1,0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,276,1,
  	0,0,0,273,277,5,5,0,0,274,277,3,2,1,0,275,277,3,22,11,0,276,273,1,0,0,
  	0,276,274,1,0,0,0,276,275,1,0,0,0,277,278,1,0,0,0,278,276,1,0,0,0,278,
  	279,1,0,0,0,279,19,1,0,0,0,280,281,5,2,0,0,281,282,3,118,59,0,282,283,
  	3,118,59,0,283,284,7,1,0,0,284,21,1,0,0,0,285,286,3,120,60,0,286,287,
  	3,122,61,0,287,288,3,122,61,0,288,289,3,118,59,0,289,290,3,118,59,0,290,
  	291,3,118,59,0,291,292,5,2,0,0,292,23,1,0,0,0,293,295,3,26,13,0,294,293,
  	1,0,0,0,295,296,1,0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,25,1,0,0,
  	0,298,299,3,120,60,0,299,301,3,122,61,0,300,302,3,2,1,0,301,300,1,0,0,
  	0,301,302,1,0,0,0,302,313,1,0,0,0,303,304,3,122,61,0,304,305,3,120,60,
  	0,305,306,3,122,61,0,306,307,3,122,61,0,307,308,3,118,59,0,308,314,1,
  	0,0,0,309,312,3,2,1,0,310,312,5,3,0,0,311,309,1,0,0,0,311,310,1,0,0,0,
  	312,314,1,0,0,0,313,303,1,0,0,0,313,311,1,0,0,0,314,315,1,0,0,0,315,313,
  	1,0,0,0,315,316,1,0,0,0,316,27,1,0,0,0,317,319,3,30,15,0,318,317,1,0,
  	0,0,319,320,1,0,0,0,320,318,1,0,0,0,320,321,1,0,0,0,321,29,1,0,0,0,322,
  	323,3,120,60,0,323,325,3,122,61,0,324,326,3,2,1,0,325,324,1,0,0,0,325,
  	326,1,0,0,0,326,338,1,0,0,0,327,328,3,122,61,0,328,329,3,120,60,0,329,
  	330,3,122,61,0,330,331,3,122,61,0,331,332,3,118,59,0,332,333,3,118,59,
  	0,333,339,1,0,0,0,334,337,3,2,1,0,335,337,5,3,0,0,336,334,1,0,0,0,336,
  	335,1,0,0,0,337,339,1,0,0,0,338,327,1,0,0,0,338,336,1,0,0,0,339,340,1,
  	0,0,0,340,338,1,0,0,0,340,341,1,0,0,0,341,31,1,0,0,0,342,344,3,34,17,
  	0,343,342,1,0,0,0,344,345,1,0,0,0,345,343,1,0,0,0,345,346,1,0,0,0,346,
  	33,1,0,0,0,347,348,3,120,60,0,348,350,3,122,61,0,349,351,3,2,1,0,350,
  	349,1,0,0,0,350,351,1,0,0,0,351,364,1,0,0,0,352,353,3,122,61,0,353,354,
  	3,120,60,0,354,355,3,122,61,0,355,356,3,122,61,0,356,357,3,118,59,0,357,
  	358,3,118,59,0,358,359,3,118,59,0,359,365,1,0,0,0,360,363,3,2,1,0,361,
  	363,5,3,0,0,362,360,1,0,0,0,362,361,1,0,0,0,363,365,1,0,0,0,364,352,1,
  	0,0,0,364,362,1,0,0,0,365,366,1,0,0,0,366,364,1,0,0,0,366,367,1,0,0,0,
  	367,35,1,0,0,0,368,370,3,38,19,0,369,368,1,0,0,0,370,371,1,0,0,0,371,
  	369,1,0,0,0,371,372,1,0,0,0,372,37,1,0,0,0,373,374,3,120,60,0,374,375,
  	3,122,61,0,375,377,3,122,61,0,376,378,3,2,1,0,377,376,1,0,0,0,377,378,
  	1,0,0,0,378,385,1,0,0,0,379,380,3,120,60,0,380,381,3,122,61,0,381,382,
  	3,122,61,0,382,383,3,118,59,0,383,386,1,0,0,0,384,386,3,2,1,0,385,379,
  	1,0,0,0,385,384,1,0,0,0,386,387,1,0,0,0,387,385,1,0,0,0,387,388,1,0,0,
  	0,388,39,1,0,0,0,389,391,3,42,21,0,390,389,1,0,0,0,391,392,1,0,0,0,392,
  	390,1,0,0,0,392,393,1,0,0,0,393,41,1,0,0,0,394,395,3,120,60,0,395,396,
  	3,122,61,0,396,398,3,122,61,0,397,399,3,2,1,0,398,397,1,0,0,0,398,399,
  	1,0,0,0,399,407,1,0,0,0,400,401,3,120,60,0,401,402,3,122,61,0,402,403,
  	3,122,61,0,403,404,3,118,59,0,404,405,3,118,59,0,405,408,1,0,0,0,406,
  	408,3,2,1,0,407,400,1,0,0,0,407,406,1,0,0,0,408,409,1,0,0,0,409,407,1,
  	0,0,0,409,410,1,0,0,0,410,43,1,0,0,0,411,413,3,46,23,0,412,411,1,0,0,
  	0,413,414,1,0,0,0,414,412,1,0,0,0,414,415,1,0,0,0,415,45,1,0,0,0,416,
  	417,3,120,60,0,417,418,3,122,61,0,418,420,3,122,61,0,419,421,3,2,1,0,
  	420,419,1,0,0,0,420,421,1,0,0,0,421,430,1,0,0,0,422,423,3,120,60,0,423,
  	424,3,122,61,0,424,425,3,122,61,0,425,426,3,118,59,0,426,427,3,118,59,
  	0,427,428,3,118,59,0,428,431,1,0,0,0,429,431,3,2,1,0,430,422,1,0,0,0,
  	430,429,1,0,0,0,431,432,1,0,0,0,432,430,1,0,0,0,432,433,1,0,0,0,433,47,
  	1,0,0,0,434,436,3,50,25,0,435,434,1,0,0,0,436,437,1,0,0,0,437,435,1,0,
  	0,0,437,438,1,0,0,0,438,49,1,0,0,0,439,440,7,2,0,0,440,441,3,130,65,0,
  	441,442,3,128,64,0,442,443,3,130,65,0,443,444,3,130,65,0,444,445,3,128,
  	64,0,445,446,3,130,65,0,446,448,3,126,63,0,447,449,3,126,63,0,448,447,
  	1,0,0,0,448,449,1,0,0,0,449,456,1,0,0,0,450,451,3,130,65,0,451,452,3,
  	130,65,0,452,453,3,128,64,0,453,454,3,130,65,0,454,455,3,126,63,0,455,
  	457,1,0,0,0,456,450,1,0,0,0,456,457,1,0,0,0,457,459,1,0,0,0,458,460,5,
  	84,0,0,459,458,1,0,0,0,459,460,1,0,0,0,460,462,1,0,0,0,461,463,5,81,0,
  	0,462,461,1,0,0,0,462,463,1,0,0,0,463,464,1,0,0,0,464,465,5,88,0,0,465,
  	51,1,0,0,0,466,468,3,54,27,0,467,466,1,0,0,0,468,469,1,0,0,0,469,467,
  	1,0,0,0,469,470,1,0,0,0,470,53,1,0,0,0,471,472,7,3,0,0,472,473,3,130,
  	65,0,473,474,3,128,64,0,474,475,3,130,65,0,475,476,3,130,65,0,476,477,
  	3,128,64,0,477,478,3,130,65,0,478,480,3,126,63,0,479,481,3,126,63,0,480,
  	479,1,0,0,0,480,481,1,0,0,0,481,488,1,0,0,0,482,483,3,130,65,0,483,484,
  	3,130,65,0,484,485,3,128,64,0,485,486,3,130,65,0,486,487,3,126,63,0,487,
  	489,1,0,0,0,488,482,1,0,0,0,488,489,1,0,0,0,489,491,1,0,0,0,490,492,5,
  	84,0,0,491,490,1,0,0,0,491,492,1,0,0,0,492,494,1,0,0,0,493,495,5,81,0,
  	0,494,493,1,0,0,0,494,495,1,0,0,0,495,496,1,0,0,0,496,497,5,88,0,0,497,
  	55,1,0,0,0,498,500,3,58,29,0,499,498,1,0,0,0,500,501,1,0,0,0,501,499,
  	1,0,0,0,501,502,1,0,0,0,502,57,1,0,0,0,503,504,7,4,0,0,504,505,3,130,
  	65,0,505,506,3,128,64,0,506,507,3,130,65,0,507,508,3,130,65,0,508,509,
  	3,128,64,0,509,510,3,130,65,0,510,512,3,126,63,0,511,513,3,126,63,0,512,
  	511,1,0,0,0,512,513,1,0,0,0,513,520,1,0,0,0,514,515,3,130,65,0,515,516,
  	3,130,65,0,516,517,3,128,64,0,517,518,3,130,65,0,518,519,3,126,63,0,519,
  	521,1,0,0,0,520,514,1,0,0,0,520,521,1,0,0,0,521,523,1,0,0,0,522,524,5,
  	84,0,0,523,522,1,0,0,0,523,524,1,0,0,0,524,526,1,0,0,0,525,527,5,81,0,
  	0,526,525,1,0,0,0,526,527,1,0,0,0,527,528,1,0,0,0,528,529,5,88,0,0,529,
  	59,1,0,0,0,530,532,3,62,31,0,531,530,1,0,0,0,532,533,1,0,0,0,533,531,
  	1,0,0,0,533,534,1,0,0,0,534,61,1,0,0,0,535,536,5,19,0,0,536,537,3,130,
  	65,0,537,538,3,128,64,0,538,539,3,130,65,0,539,540,3,126,63,0,540,545,
  	3,126,63,0,541,542,3,130,65,0,542,543,3,126,63,0,543,544,3,126,63,0,544,
  	546,1,0,0,0,545,541,1,0,0,0,545,546,1,0,0,0,546,548,1,0,0,0,547,549,5,
  	84,0,0,548,547,1,0,0,0,548,549,1,0,0,0,549,551,1,0,0,0,550,552,5,81,0,
  	0,551,550,1,0,0,0,551,552,1,0,0,0,552,553,1,0,0,0,553,554,5,88,0,0,554,
  	63,1,0,0,0,555,557,3,66,33,0,556,555,1,0,0,0,557,558,1,0,0,0,558,556,
  	1,0,0,0,558,559,1,0,0,0,559,65,1,0,0,0,560,561,5,18,0,0,561,562,3,130,
  	65,0,562,563,3,128,64,0,563,564,3,130,65,0,564,565,3,130,65,0,565,567,
  	3,126,63,0,566,568,3,126,63,0,567,566,1,0,0,0,567,568,1,0,0,0,568,575,
  	1,0,0,0,569,570,3,130,65,0,570,571,3,130,65,0,571,573,3,126,63,0,572,
  	574,3,126,63,0,573,572,1,0,0,0,573,574,1,0,0,0,574,576,1,0,0,0,575,569,
  	1,0,0,0,575,576,1,0,0,0,576,583,1,0,0,0,577,578,3,130,65,0,578,579,3,
  	130,65,0,579,581,3,126,63,0,580,582,3,126,63,0,581,580,1,0,0,0,581,582,
  	1,0,0,0,582,584,1,0,0,0,583,577,1,0,0,0,583,584,1,0,0,0,584,586,1,0,0,
  	0,585,587,5,84,0,0,586,585,1,0,0,0,586,587,1,0,0,0,587,589,1,0,0,0,588,
  	590,5,81,0,0,589,588,1,0,0,0,589,590,1,0,0,0,590,591,1,0,0,0,591,592,
  	5,88,0,0,592,67,1,0,0,0,593,594,5,20,0,0,594,595,3,130,65,0,595,599,3,
  	128,64,0,596,598,3,130,65,0,597,596,1,0,0,0,598,601,1,0,0,0,599,597,1,
  	0,0,0,599,600,1,0,0,0,600,603,1,0,0,0,601,599,1,0,0,0,602,604,5,81,0,
  	0,603,602,1,0,0,0,603,604,1,0,0,0,604,605,1,0,0,0,605,606,5,88,0,0,606,
  	69,1,0,0,0,607,609,3,72,36,0,608,607,1,0,0,0,609,610,1,0,0,0,610,608,
  	1,0,0,0,610,611,1,0,0,0,611,71,1,0,0,0,612,613,5,2,0,0,613,614,3,122,
  	61,0,614,615,3,122,61,0,615,616,3,122,61,0,616,617,5,2,0,0,617,618,3,
  	122,61,0,618,619,3,122,61,0,619,620,3,122,61,0,620,622,3,118,59,0,621,
  	623,3,118,59,0,622,621,1,0,0,0,622,623,1,0,0,0,623,625,1,0,0,0,624,626,
  	3,118,59,0,625,624,1,0,0,0,625,626,1,0,0,0,626,628,1,0,0,0,627,629,3,
  	118,59,0,628,627,1,0,0,0,628,629,1,0,0,0,629,631,1,0,0,0,630,632,3,118,
  	59,0,631,630,1,0,0,0,631,632,1,0,0,0,632,634,1,0,0,0,633,635,3,118,59,
  	0,634,633,1,0,0,0,634,635,1,0,0,0,635,73,1,0,0,0,636,638,3,76,38,0,637,
  	636,1,0,0,0,638,639,1,0,0,0,639,637,1,0,0,0,639,640,1,0,0,0,640,75,1,
  	0,0,0,641,642,3,122,61,0,642,643,5,2,0,0,643,644,3,122,61,0,644,645,3,
  	122,61,0,645,646,3,122,61,0,646,647,5,2,0,0,647,648,3,122,61,0,648,649,
  	3,122,61,0,649,651,3,118,59,0,650,652,3,118,59,0,651,650,1,0,0,0,651,
  	652,1,0,0,0,652,654,1,0,0,0,653,655,3,118,59,0,654,653,1,0,0,0,654,655,
  	1,0,0,0,655,657,1,0,0,0,656,658,3,118,59,0,657,656,1,0,0,0,657,658,1,
  	0,0,0,658,660,1,0,0,0,659,661,3,118,59,0,660,659,1,0,0,0,660,661,1,0,
  	0,0,661,663,1,0,0,0,662,664,3,118,59,0,663,662,1,0,0,0,663,664,1,0,0,
  	0,664,77,1,0,0,0,665,667,3,80,40,0,666,665,1,0,0,0,667,668,1,0,0,0,668,
  	666,1,0,0,0,668,669,1,0,0,0,669,79,1,0,0,0,670,671,3,122,61,0,671,672,
  	3,122,61,0,672,673,5,2,0,0,673,674,3,122,61,0,674,675,3,122,61,0,675,
  	676,3,122,61,0,676,677,5,2,0,0,677,678,3,122,61,0,678,680,3,118,59,0,
  	679,681,3,118,59,0,680,679,1,0,0,0,680,681,1,0,0,0,681,683,1,0,0,0,682,
  	684,3,118,59,0,683,682,1,0,0,0,683,684,1,0,0,0,684,686,1,0,0,0,685,687,
  	3,118,59,0,686,685,1,0,0,0,686,687,1,0,0,0,687,689,1,0,0,0,688,690,3,
  	118,59,0,689,688,1,0,0,0,689,690,1,0,0,0,690,692,1,0,0,0,691,693,3,118,
  	59,0,692,691,1,0,0,0,692,693,1,0,0,0,693,81,1,0,0,0,694,696,3,84,42,0,
  	695,694,1,0,0,0,696,697,1,0,0,0,697,695,1,0,0,0,697,698,1,0,0,0,698,83,
  	1,0,0,0,699,700,3,122,61,0,700,701,5,2,0,0,701,702,3,122,61,0,702,703,
  	3,122,61,0,703,704,3,118,59,0,704,706,3,118,59,0,705,707,3,118,59,0,706,
  	705,1,0,0,0,706,707,1,0,0,0,707,711,1,0,0,0,708,709,5,21,0,0,709,710,
  	5,22,0,0,710,712,5,2,0,0,711,708,1,0,0,0,711,712,1,0,0,0,712,714,1,0,
  	0,0,713,715,5,23,0,0,714,713,1,0,0,0,714,715,1,0,0,0,715,85,1,0,0,0,716,
  	718,3,88,44,0,717,716,1,0,0,0,718,719,1,0,0,0,719,717,1,0,0,0,719,720,
  	1,0,0,0,720,87,1,0,0,0,721,722,3,120,60,0,722,723,3,122,61,0,723,724,
  	3,122,61,0,724,725,3,122,61,0,725,727,3,118,59,0,726,728,3,118,59,0,727,
  	726,1,0,0,0,727,728,1,0,0,0,728,730,1,0,0,0,729,731,3,118,59,0,730,729,
  	1,0,0,0,730,731,1,0,0,0,731,733,1,0,0,0,732,734,3,118,59,0,733,732,1,
  	0,0,0,733,734,1,0,0,0,734,736,1,0,0,0,735,737,3,118,59,0,736,735,1,0,
  	0,0,736,737,1,0,0,0,737,739,1,0,0,0,738,740,3,118,59,0,739,738,1,0,0,
  	0,739,740,1,0,0,0,740,89,1,0,0,0,741,743,3,92,46,0,742,741,1,0,0,0,743,
  	744,1,0,0,0,744,742,1,0,0,0,744,745,1,0,0,0,745,91,1,0,0,0,746,747,3,
  	120,60,0,747,748,3,122,61,0,748,749,3,122,61,0,749,750,3,118,59,0,750,
  	751,5,2,0,0,751,752,3,118,59,0,752,753,3,118,59,0,753,754,5,2,0,0,754,
  	93,1,0,0,0,755,756,5,24,0,0,756,757,5,25,0,0,757,95,1,0,0,0,758,766,5,
  	26,0,0,759,760,5,46,0,0,760,763,5,50,0,0,761,763,5,51,0,0,762,759,1,0,
  	0,0,762,761,1,0,0,0,762,763,1,0,0,0,763,764,1,0,0,0,764,767,5,60,0,0,
  	765,767,5,55,0,0,766,762,1,0,0,0,766,765,1,0,0,0,767,775,1,0,0,0,768,
  	769,5,48,0,0,769,772,5,50,0,0,770,772,5,53,0,0,771,768,1,0,0,0,771,770,
  	1,0,0,0,771,772,1,0,0,0,772,773,1,0,0,0,773,776,5,59,0,0,774,776,5,57,
  	0,0,775,771,1,0,0,0,775,774,1,0,0,0,776,784,1,0,0,0,777,778,5,47,0,0,
  	778,781,5,50,0,0,779,781,5,52,0,0,780,777,1,0,0,0,780,779,1,0,0,0,780,
  	781,1,0,0,0,781,782,1,0,0,0,782,785,5,60,0,0,783,785,5,56,0,0,784,780,
  	1,0,0,0,784,783,1,0,0,0,785,793,1,0,0,0,786,787,5,49,0,0,787,790,5,50,
  	0,0,788,790,5,54,0,0,789,786,1,0,0,0,789,788,1,0,0,0,789,790,1,0,0,0,
  	790,791,1,0,0,0,791,794,5,59,0,0,792,794,5,58,0,0,793,789,1,0,0,0,793,
  	792,1,0,0,0,794,795,1,0,0,0,795,796,5,62,0,0,796,97,1,0,0,0,797,798,5,
  	27,0,0,798,799,3,122,61,0,799,800,3,120,60,0,800,801,3,122,61,0,801,802,
  	3,120,60,0,802,99,1,0,0,0,803,810,5,28,0,0,804,811,5,64,0,0,805,807,5,
  	66,0,0,806,808,5,66,0,0,807,806,1,0,0,0,807,808,1,0,0,0,808,809,1,0,0,
  	0,809,811,5,65,0,0,810,804,1,0,0,0,810,805,1,0,0,0,811,812,1,0,0,0,812,
  	813,5,68,0,0,813,101,1,0,0,0,814,818,5,29,0,0,815,817,5,70,0,0,816,815,
  	1,0,0,0,817,820,1,0,0,0,818,816,1,0,0,0,818,819,1,0,0,0,819,821,1,0,0,
  	0,820,818,1,0,0,0,821,822,5,72,0,0,822,103,1,0,0,0,823,824,5,31,0,0,824,
  	105,1,0,0,0,825,829,5,30,0,0,826,828,5,70,0,0,827,826,1,0,0,0,828,831,
  	1,0,0,0,829,827,1,0,0,0,829,830,1,0,0,0,830,832,1,0,0,0,831,829,1,0,0,
  	0,832,833,5,72,0,0,833,107,1,0,0,0,834,835,5,32,0,0,835,836,5,64,0,0,
  	836,837,5,68,0,0,837,109,1,0,0,0,838,839,5,33,0,0,839,841,3,122,61,0,
  	840,842,3,2,1,0,841,840,1,0,0,0,841,842,1,0,0,0,842,845,1,0,0,0,843,846,
  	3,112,56,0,844,846,3,2,1,0,845,843,1,0,0,0,845,844,1,0,0,0,846,847,1,
  	0,0,0,847,845,1,0,0,0,847,848,1,0,0,0,848,111,1,0,0,0,849,850,5,34,0,
  	0,850,851,5,76,0,0,851,853,5,77,0,0,852,854,5,76,0,0,853,852,1,0,0,0,
  	854,855,1,0,0,0,855,853,1,0,0,0,855,856,1,0,0,0,856,857,1,0,0,0,857,858,
  	5,79,0,0,858,113,1,0,0,0,859,860,5,33,0,0,860,862,3,122,61,0,861,863,
  	3,2,1,0,862,861,1,0,0,0,862,863,1,0,0,0,863,866,1,0,0,0,864,867,3,116,
  	58,0,865,867,3,2,1,0,866,864,1,0,0,0,866,865,1,0,0,0,867,868,1,0,0,0,
  	868,866,1,0,0,0,868,869,1,0,0,0,869,115,1,0,0,0,870,871,5,35,0,0,871,
  	872,7,5,0,0,872,875,5,77,0,0,873,874,5,76,0,0,874,876,5,75,0,0,875,873,
  	1,0,0,0,876,877,1,0,0,0,877,875,1,0,0,0,877,878,1,0,0,0,878,879,1,0,0,
  	0,879,880,5,79,0,0,880,117,1,0,0,0,881,882,7,6,0,0,882,119,1,0,0,0,883,
  	884,7,7,0,0,884,121,1,0,0,0,885,886,7,8,0,0,886,123,1,0,0,0,887,888,7,
  	9,0,0,888,125,1,0,0,0,889,890,7,10,0,0,890,127,1,0,0,0,891,892,7,11,0,
  	0,892,129,1,0,0,0,893,894,7,12,0,0,894,131,1,0,0,0,895,896,7,12,0,0,896,
  	133,1,0,0,0,126,138,174,176,185,193,203,206,209,212,215,220,228,233,236,
  	241,246,248,266,271,276,278,296,301,311,313,315,320,325,336,338,340,345,
  	350,362,364,366,371,377,385,387,392,398,407,409,414,420,430,432,437,448,
  	456,459,462,469,480,488,491,494,501,512,520,523,526,533,545,548,551,558,
  	567,573,575,581,583,586,589,599,603,610,622,625,628,631,634,639,651,654,
  	657,660,663,668,680,683,686,689,692,697,706,711,714,719,727,730,733,736,
  	739,744,762,766,771,775,780,784,789,793,807,810,818,829,841,845,847,855,
  	862,866,868,877
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

std::vector<CyanaMRParser::Pcs_no_param_restraintsContext *> CyanaMRParser::Cyana_mrContext::pcs_no_param_restraints() {
  return getRuleContexts<CyanaMRParser::Pcs_no_param_restraintsContext>();
}

CyanaMRParser::Pcs_no_param_restraintsContext* CyanaMRParser::Cyana_mrContext::pcs_no_param_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Pcs_no_param_restraintsContext>(i);
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
    setState(176);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 532527710052) != 0)) {
      setState(174);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(134);
        match(CyanaMRParser::Orientation_header);
        break;
      }

      case 2: {
        setState(136); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(135);
                  match(CyanaMRParser::Tensor_header);
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(138); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 3: {
        setState(140);
        comment();
        break;
      }

      case 4: {
        setState(141);
        distance_restraints();
        break;
      }

      case 5: {
        setState(142);
        fixres_distance_restraints();
        break;
      }

      case 6: {
        setState(143);
        fixresw_distance_restraints();
        break;
      }

      case 7: {
        setState(144);
        fixresw2_distance_restraints();
        break;
      }

      case 8: {
        setState(145);
        fixatm_distance_restraints();
        break;
      }

      case 9: {
        setState(146);
        fixatmw_distance_restraints();
        break;
      }

      case 10: {
        setState(147);
        fixatmw2_distance_restraints();
        break;
      }

      case 11: {
        setState(148);
        diana_distance_restraints();
        break;
      }

      case 12: {
        setState(149);
        diana_ssbond_restraints();
        break;
      }

      case 13: {
        setState(150);
        diana_hbond_restraints();
        break;
      }

      case 14: {
        setState(151);
        diana_torsion_angle_restraints();
        break;
      }

      case 15: {
        setState(152);
        diana_coupling_constant_restraints();
        break;
      }

      case 16: {
        setState(153);
        diana_stereoassign_macro();
        break;
      }

      case 17: {
        setState(154);
        distance_w_chain_restraints();
        break;
      }

      case 18: {
        setState(155);
        distance_w_chain2_restraints();
        break;
      }

      case 19: {
        setState(156);
        distance_w_chain3_restraints();
        break;
      }

      case 20: {
        setState(157);
        torsion_angle_restraints();
        break;
      }

      case 21: {
        setState(158);
        torsion_angle_w_chain_restraints();
        break;
      }

      case 22: {
        setState(159);
        rdc_restraints();
        break;
      }

      case 23: {
        setState(160);
        pcs_restraints();
        break;
      }

      case 24: {
        setState(161);
        cco_restraints();
        break;
      }

      case 25: {
        setState(162);
        pcs_no_param_restraints();
        break;
      }

      case 26: {
        setState(163);
        ssbond_macro();
        break;
      }

      case 27: {
        setState(164);
        hbond_macro();
        break;
      }

      case 28: {
        setState(165);
        link_statement();
        break;
      }

      case 29: {
        setState(166);
        stereoassign_macro();
        break;
      }

      case 30: {
        setState(167);
        declare_variable();
        break;
      }

      case 31: {
        setState(168);
        set_variable();
        break;
      }

      case 32: {
        setState(169);
        unset_variable();
        break;
      }

      case 33: {
        setState(170);
        print_macro();
        break;
      }

      case 34: {
        setState(171);
        unambig_atom_name_mapping();
        break;
      }

      case 35: {
        setState(172);
        ambig_atom_name_mapping();
        break;
      }

      case 36: {
        setState(173);
        ambig_list();
        break;
      }

      default:
        break;
      }
      setState(178);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(179);
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
    setState(181);
    match(CyanaMRParser::COMMENT);
    setState(185);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Any_name) {
      setState(182);
      match(CyanaMRParser::Any_name);
      setState(187);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(188);
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
    setState(191); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(190);
              distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(193); 
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
    setState(195);
    gen_res_num();
    setState(196);
    gen_simple_name();
    setState(197);
    gen_atom_name();
    setState(198);
    gen_res_num();
    setState(199);
    gen_simple_name();
    setState(200);
    gen_atom_name();
    setState(201);
    number();
    setState(203);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx)) {
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

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 6, _ctx)) {
    case 1: {
      setState(205);
      number();
      break;
    }

    default:
      break;
    }
    setState(209);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx)) {
    case 1: {
      setState(208);
      number();
      break;
    }

    default:
      break;
    }
    setState(212);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx)) {
    case 1: {
      setState(211);
      number();
      break;
    }

    default:
      break;
    }
    setState(215);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx)) {
    case 1: {
      setState(214);
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
    setState(218); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(217);
              torsion_angle_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(220); 
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
    setState(222);
    gen_res_num();
    setState(223);
    gen_simple_name();
    setState(224);
    gen_simple_name();
    setState(225);
    number();
    setState(226);
    number();
    setState(228);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx)) {
    case 1: {
      setState(227);
      number();
      break;
    }

    default:
      break;
    }
    setState(233);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Type) {
      setState(230);
      match(CyanaMRParser::Type);
      setState(231);
      match(CyanaMRParser::Equ_op);
      setState(232);
      match(CyanaMRParser::Integer);
    }
    setState(236);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Or) {
      setState(235);
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
    setState(239); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(238);
              rdc_parameter();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(241); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(246); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(246);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Orientation_header: {
                  setState(243);
                  match(CyanaMRParser::Orientation_header);
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(244);
                  comment();
                  break;
                }

                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(245);
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
      setState(248); 
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
    setState(250);
    match(CyanaMRParser::Integer);
    setState(251);
    number();
    setState(252);
    number();
    setState(253);
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
    setState(255);
    gen_res_num();
    setState(256);
    gen_simple_name();
    setState(257);
    gen_simple_name();
    setState(258);
    gen_res_num();
    setState(259);
    gen_simple_name();
    setState(260);
    gen_simple_name();
    setState(261);
    number();
    setState(262);
    number();
    setState(263);
    number();
    setState(264);
    match(CyanaMRParser::Integer);
    setState(266);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx)) {
    case 1: {
      setState(265);
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
    setState(269); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(268);
              pcs_parameter();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(271); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(276); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(276);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Orientation_header: {
                  setState(273);
                  match(CyanaMRParser::Orientation_header);
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(274);
                  comment();
                  break;
                }

                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(275);
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
      setState(278); 
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
    setState(280);
    match(CyanaMRParser::Integer);
    setState(281);
    number();
    setState(282);
    number();
    setState(283);
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
    setState(285);
    gen_res_num();
    setState(286);
    gen_simple_name();
    setState(287);
    gen_simple_name();
    setState(288);
    number();
    setState(289);
    number();
    setState(290);
    number();
    setState(291);
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
    setState(294); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(293);
              fixres_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(296); 
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
    setState(298);
    gen_res_num();
    setState(299);
    gen_simple_name();
    setState(301);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 22, _ctx)) {
    case 1: {
      setState(300);
      comment();
      break;
    }

    default:
      break;
    }
    setState(313); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(313);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(303);
                  gen_simple_name();
                  setState(304);
                  gen_res_num();
                  setState(305);
                  gen_simple_name();
                  setState(306);
                  gen_simple_name();
                  setState(307);
                  number();
                  break;
                }

                case CyanaMRParser::Float:
                case CyanaMRParser::COMMENT: {
                  setState(311);
                  _errHandler->sync(this);
                  switch (_input->LA(1)) {
                    case CyanaMRParser::COMMENT: {
                      setState(309);
                      comment();
                      break;
                    }

                    case CyanaMRParser::Float: {
                      setState(310);
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
      setState(315); 
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
    setState(318); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(317);
              fixresw_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(320); 
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
    setState(322);
    gen_res_num();
    setState(323);
    gen_simple_name();
    setState(325);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 27, _ctx)) {
    case 1: {
      setState(324);
      comment();
      break;
    }

    default:
      break;
    }
    setState(338); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(338);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(327);
                  gen_simple_name();
                  setState(328);
                  gen_res_num();
                  setState(329);
                  gen_simple_name();
                  setState(330);
                  gen_simple_name();
                  setState(331);
                  number();
                  setState(332);
                  number();
                  break;
                }

                case CyanaMRParser::Float:
                case CyanaMRParser::COMMENT: {
                  setState(336);
                  _errHandler->sync(this);
                  switch (_input->LA(1)) {
                    case CyanaMRParser::COMMENT: {
                      setState(334);
                      comment();
                      break;
                    }

                    case CyanaMRParser::Float: {
                      setState(335);
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
      setState(340); 
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
    setState(343); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(342);
              fixresw2_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(345); 
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
    setState(347);
    gen_res_num();
    setState(348);
    gen_simple_name();
    setState(350);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 32, _ctx)) {
    case 1: {
      setState(349);
      comment();
      break;
    }

    default:
      break;
    }
    setState(364); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(364);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(352);
                  gen_simple_name();
                  setState(353);
                  gen_res_num();
                  setState(354);
                  gen_simple_name();
                  setState(355);
                  gen_simple_name();
                  setState(356);
                  number();
                  setState(357);
                  number();
                  setState(358);
                  number();
                  break;
                }

                case CyanaMRParser::Float:
                case CyanaMRParser::COMMENT: {
                  setState(362);
                  _errHandler->sync(this);
                  switch (_input->LA(1)) {
                    case CyanaMRParser::COMMENT: {
                      setState(360);
                      comment();
                      break;
                    }

                    case CyanaMRParser::Float: {
                      setState(361);
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
      setState(366); 
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
    setState(369); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(368);
              fixatm_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(371); 
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
    setState(373);
    gen_res_num();
    setState(374);
    gen_simple_name();
    setState(375);
    gen_simple_name();
    setState(377);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 37, _ctx)) {
    case 1: {
      setState(376);
      comment();
      break;
    }

    default:
      break;
    }
    setState(385); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(385);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(379);
                  gen_res_num();
                  setState(380);
                  gen_simple_name();
                  setState(381);
                  gen_simple_name();
                  setState(382);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(384);
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
      setState(387); 
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
    setState(390); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(389);
              fixatmw_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(392); 
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
    setState(394);
    gen_res_num();
    setState(395);
    gen_simple_name();
    setState(396);
    gen_simple_name();
    setState(398);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 41, _ctx)) {
    case 1: {
      setState(397);
      comment();
      break;
    }

    default:
      break;
    }
    setState(407); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(407);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(400);
                  gen_res_num();
                  setState(401);
                  gen_simple_name();
                  setState(402);
                  gen_simple_name();
                  setState(403);
                  number();
                  setState(404);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(406);
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
      setState(409); 
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
    setState(412); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(411);
              fixatmw2_distance_restraint();
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
    setState(416);
    gen_res_num();
    setState(417);
    gen_simple_name();
    setState(418);
    gen_simple_name();
    setState(420);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 45, _ctx)) {
    case 1: {
      setState(419);
      comment();
      break;
    }

    default:
      break;
    }
    setState(430); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(430);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(422);
                  gen_res_num();
                  setState(423);
                  gen_simple_name();
                  setState(424);
                  gen_simple_name();
                  setState(425);
                  number();
                  setState(426);
                  number();
                  setState(427);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(429);
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
      setState(432); 
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
    setState(435); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(434);
              diana_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(437); 
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
    setState(439);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 3584) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(440);
    gen_simple_name_qc();
    setState(441);
    gen_res_num_qc();
    setState(442);
    gen_simple_name_qc();
    setState(443);
    gen_simple_name_qc();
    setState(444);
    gen_res_num_qc();
    setState(445);
    gen_simple_name_qc();
    setState(446);
    number_qc();
    setState(448);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 49, _ctx)) {
    case 1: {
      setState(447);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(456);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 50, _ctx)) {
    case 1: {
      setState(450);
      gen_simple_name_qc();
      setState(451);
      gen_simple_name_qc();
      setState(452);
      gen_res_num_qc();
      setState(453);
      gen_simple_name_qc();
      setState(454);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(459);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Simple_name_QC) {
      setState(458);
      match(CyanaMRParser::Simple_name_QC);
    }
    setState(462);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Integer_QC) {
      setState(461);
      match(CyanaMRParser::Integer_QC);
    }
    setState(464);
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
    setState(467); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(466);
              diana_ssbond_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(469); 
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
    setState(471);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 229376) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(472);
    gen_simple_name_qc();
    setState(473);
    gen_res_num_qc();
    setState(474);
    gen_simple_name_qc();
    setState(475);
    gen_simple_name_qc();
    setState(476);
    gen_res_num_qc();
    setState(477);
    gen_simple_name_qc();
    setState(478);
    number_qc();
    setState(480);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 54, _ctx)) {
    case 1: {
      setState(479);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(488);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 55, _ctx)) {
    case 1: {
      setState(482);
      gen_simple_name_qc();
      setState(483);
      gen_simple_name_qc();
      setState(484);
      gen_res_num_qc();
      setState(485);
      gen_simple_name_qc();
      setState(486);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(491);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Simple_name_QC) {
      setState(490);
      match(CyanaMRParser::Simple_name_QC);
    }
    setState(494);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Integer_QC) {
      setState(493);
      match(CyanaMRParser::Integer_QC);
    }
    setState(496);
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
    setState(499); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(498);
              diana_hbond_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(501); 
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
    setState(503);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 28672) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(504);
    gen_simple_name_qc();
    setState(505);
    gen_res_num_qc();
    setState(506);
    gen_simple_name_qc();
    setState(507);
    gen_simple_name_qc();
    setState(508);
    gen_res_num_qc();
    setState(509);
    gen_simple_name_qc();
    setState(510);
    number_qc();
    setState(512);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 59, _ctx)) {
    case 1: {
      setState(511);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(520);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 60, _ctx)) {
    case 1: {
      setState(514);
      gen_simple_name_qc();
      setState(515);
      gen_simple_name_qc();
      setState(516);
      gen_res_num_qc();
      setState(517);
      gen_simple_name_qc();
      setState(518);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(523);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Simple_name_QC) {
      setState(522);
      match(CyanaMRParser::Simple_name_QC);
    }
    setState(526);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Integer_QC) {
      setState(525);
      match(CyanaMRParser::Integer_QC);
    }
    setState(528);
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
    setState(531); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(530);
              diana_torsion_angle_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(533); 
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
    setState(535);
    match(CyanaMRParser::Angle);
    setState(536);
    gen_simple_name_qc();
    setState(537);
    gen_res_num_qc();
    setState(538);
    gen_simple_name_qc();
    setState(539);
    number_qc();
    setState(540);
    number_qc();
    setState(545);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 64, _ctx)) {
    case 1: {
      setState(541);
      gen_simple_name_qc();
      setState(542);
      number_qc();
      setState(543);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(548);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Simple_name_QC) {
      setState(547);
      match(CyanaMRParser::Simple_name_QC);
    }
    setState(551);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Integer_QC) {
      setState(550);
      match(CyanaMRParser::Integer_QC);
    }
    setState(553);
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
    setState(556); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(555);
              diana_coupling_constant_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(558); 
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
    setState(560);
    match(CyanaMRParser::Jcoupl);
    setState(561);
    gen_simple_name_qc();
    setState(562);
    gen_res_num_qc();
    setState(563);
    gen_simple_name_qc();
    setState(564);
    gen_simple_name_qc();
    setState(565);
    number_qc();
    setState(567);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 68, _ctx)) {
    case 1: {
      setState(566);
      number_qc();
      break;
    }

    default:
      break;
    }
    setState(575);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 70, _ctx)) {
    case 1: {
      setState(569);
      gen_simple_name_qc();
      setState(570);
      gen_simple_name_qc();
      setState(571);
      number_qc();
      setState(573);
      _errHandler->sync(this);

      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 69, _ctx)) {
      case 1: {
        setState(572);
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
    setState(583);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 72, _ctx)) {
    case 1: {
      setState(577);
      gen_simple_name_qc();
      setState(578);
      gen_simple_name_qc();
      setState(579);
      number_qc();
      setState(581);
      _errHandler->sync(this);

      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 71, _ctx)) {
      case 1: {
        setState(580);
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
    setState(586);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Simple_name_QC) {
      setState(585);
      match(CyanaMRParser::Simple_name_QC);
    }
    setState(589);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Integer_QC) {
      setState(588);
      match(CyanaMRParser::Integer_QC);
    }
    setState(591);
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
    setState(593);
    match(CyanaMRParser::Stereo);
    setState(594);
    gen_simple_name_qc();
    setState(595);
    gen_res_num_qc();
    setState(599);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((((_la - 84) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 84)) & 7) != 0)) {
      setState(596);
      gen_simple_name_qc();
      setState(601);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(603);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Integer_QC) {
      setState(602);
      match(CyanaMRParser::Integer_QC);
    }
    setState(605);
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
    setState(608); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(607);
              distance_w_chain_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(610); 
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
    setState(612);
    match(CyanaMRParser::Integer);
    setState(613);
    gen_simple_name();
    setState(614);
    gen_simple_name();
    setState(615);
    gen_simple_name();
    setState(616);
    match(CyanaMRParser::Integer);
    setState(617);
    gen_simple_name();
    setState(618);
    gen_simple_name();
    setState(619);
    gen_simple_name();
    setState(620);
    number();
    setState(622);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 78, _ctx)) {
    case 1: {
      setState(621);
      number();
      break;
    }

    default:
      break;
    }
    setState(625);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 79, _ctx)) {
    case 1: {
      setState(624);
      number();
      break;
    }

    default:
      break;
    }
    setState(628);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 80, _ctx)) {
    case 1: {
      setState(627);
      number();
      break;
    }

    default:
      break;
    }
    setState(631);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 81, _ctx)) {
    case 1: {
      setState(630);
      number();
      break;
    }

    default:
      break;
    }
    setState(634);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 82, _ctx)) {
    case 1: {
      setState(633);
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
    setState(637); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(636);
              distance_w_chain2_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(639); 
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
    setState(641);
    gen_simple_name();
    setState(642);
    match(CyanaMRParser::Integer);
    setState(643);
    gen_simple_name();
    setState(644);
    gen_simple_name();
    setState(645);
    gen_simple_name();
    setState(646);
    match(CyanaMRParser::Integer);
    setState(647);
    gen_simple_name();
    setState(648);
    gen_simple_name();
    setState(649);
    number();
    setState(651);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 84, _ctx)) {
    case 1: {
      setState(650);
      number();
      break;
    }

    default:
      break;
    }
    setState(654);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 85, _ctx)) {
    case 1: {
      setState(653);
      number();
      break;
    }

    default:
      break;
    }
    setState(657);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 86, _ctx)) {
    case 1: {
      setState(656);
      number();
      break;
    }

    default:
      break;
    }
    setState(660);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 87, _ctx)) {
    case 1: {
      setState(659);
      number();
      break;
    }

    default:
      break;
    }
    setState(663);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 88, _ctx)) {
    case 1: {
      setState(662);
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
    setState(666); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(665);
              distance_w_chain3_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(668); 
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
    setState(670);
    gen_simple_name();
    setState(671);
    gen_simple_name();
    setState(672);
    match(CyanaMRParser::Integer);
    setState(673);
    gen_simple_name();
    setState(674);
    gen_simple_name();
    setState(675);
    gen_simple_name();
    setState(676);
    match(CyanaMRParser::Integer);
    setState(677);
    gen_simple_name();
    setState(678);
    number();
    setState(680);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 90, _ctx)) {
    case 1: {
      setState(679);
      number();
      break;
    }

    default:
      break;
    }
    setState(683);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 91, _ctx)) {
    case 1: {
      setState(682);
      number();
      break;
    }

    default:
      break;
    }
    setState(686);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 92, _ctx)) {
    case 1: {
      setState(685);
      number();
      break;
    }

    default:
      break;
    }
    setState(689);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 93, _ctx)) {
    case 1: {
      setState(688);
      number();
      break;
    }

    default:
      break;
    }
    setState(692);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 94, _ctx)) {
    case 1: {
      setState(691);
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
    setState(695); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(694);
              torsion_angle_w_chain_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(697); 
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
    setState(699);
    gen_simple_name();
    setState(700);
    match(CyanaMRParser::Integer);
    setState(701);
    gen_simple_name();
    setState(702);
    gen_simple_name();
    setState(703);
    number();
    setState(704);
    number();
    setState(706);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 96, _ctx)) {
    case 1: {
      setState(705);
      number();
      break;
    }

    default:
      break;
    }
    setState(711);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Type) {
      setState(708);
      match(CyanaMRParser::Type);
      setState(709);
      match(CyanaMRParser::Equ_op);
      setState(710);
      match(CyanaMRParser::Integer);
    }
    setState(714);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Or) {
      setState(713);
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
    setState(717); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(716);
              cco_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(719); 
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
    setState(721);
    gen_res_num();
    setState(722);
    gen_simple_name();
    setState(723);
    gen_simple_name();
    setState(724);
    gen_simple_name();
    setState(725);
    number();
    setState(727);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 100, _ctx)) {
    case 1: {
      setState(726);
      number();
      break;
    }

    default:
      break;
    }
    setState(730);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 101, _ctx)) {
    case 1: {
      setState(729);
      number();
      break;
    }

    default:
      break;
    }
    setState(733);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 102, _ctx)) {
    case 1: {
      setState(732);
      number();
      break;
    }

    default:
      break;
    }
    setState(736);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 103, _ctx)) {
    case 1: {
      setState(735);
      number();
      break;
    }

    default:
      break;
    }
    setState(739);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 104, _ctx)) {
    case 1: {
      setState(738);
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

//----------------- Pcs_no_param_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Pcs_no_param_restraintsContext::Pcs_no_param_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Pcs_no_param_restraintContext *> CyanaMRParser::Pcs_no_param_restraintsContext::pcs_no_param_restraint() {
  return getRuleContexts<CyanaMRParser::Pcs_no_param_restraintContext>();
}

CyanaMRParser::Pcs_no_param_restraintContext* CyanaMRParser::Pcs_no_param_restraintsContext::pcs_no_param_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Pcs_no_param_restraintContext>(i);
}


size_t CyanaMRParser::Pcs_no_param_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RulePcs_no_param_restraints;
}


std::any CyanaMRParser::Pcs_no_param_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitPcs_no_param_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Pcs_no_param_restraintsContext* CyanaMRParser::pcs_no_param_restraints() {
  Pcs_no_param_restraintsContext *_localctx = _tracker.createInstance<Pcs_no_param_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 90, CyanaMRParser::RulePcs_no_param_restraints);

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
    setState(742); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(741);
              pcs_no_param_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(744); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 105, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pcs_no_param_restraintContext ------------------------------------------------------------------

CyanaMRParser::Pcs_no_param_restraintContext::Pcs_no_param_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Pcs_no_param_restraintContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Pcs_no_param_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Pcs_no_param_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Pcs_no_param_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Pcs_no_param_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Pcs_no_param_restraintContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Pcs_no_param_restraintContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}


size_t CyanaMRParser::Pcs_no_param_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RulePcs_no_param_restraint;
}


std::any CyanaMRParser::Pcs_no_param_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitPcs_no_param_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Pcs_no_param_restraintContext* CyanaMRParser::pcs_no_param_restraint() {
  Pcs_no_param_restraintContext *_localctx = _tracker.createInstance<Pcs_no_param_restraintContext>(_ctx, getState());
  enterRule(_localctx, 92, CyanaMRParser::RulePcs_no_param_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(746);
    gen_res_num();
    setState(747);
    gen_simple_name();
    setState(748);
    gen_simple_name();
    setState(749);
    number();
    setState(750);
    match(CyanaMRParser::Integer);
    setState(751);
    number();
    setState(752);
    number();
    setState(753);
    match(CyanaMRParser::Integer);
   
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
    setState(755);
    match(CyanaMRParser::Ssbond);
    setState(756);
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
    setState(758);
    match(CyanaMRParser::Hbond);
    setState(766);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Atom1:
      case CyanaMRParser::Atom1_equ:
      case CyanaMRParser::Simple_name_HB: {
        setState(762);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CyanaMRParser::Atom1: {
            setState(759);
            match(CyanaMRParser::Atom1);
            setState(760);
            match(CyanaMRParser::Equ_op_HB);
            break;
          }

          case CyanaMRParser::Atom1_equ: {
            setState(761);
            match(CyanaMRParser::Atom1_equ);
            break;
          }

          case CyanaMRParser::Simple_name_HB: {
            break;
          }

        default:
          break;
        }
        setState(764);
        match(CyanaMRParser::Simple_name_HB);
        break;
      }

      case CyanaMRParser::Concat_atom_1: {
        setState(765);
        match(CyanaMRParser::Concat_atom_1);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(775);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Residue1:
      case CyanaMRParser::Residue1_equ:
      case CyanaMRParser::Integer_HB: {
        setState(771);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CyanaMRParser::Residue1: {
            setState(768);
            match(CyanaMRParser::Residue1);
            setState(769);
            match(CyanaMRParser::Equ_op_HB);
            break;
          }

          case CyanaMRParser::Residue1_equ: {
            setState(770);
            match(CyanaMRParser::Residue1_equ);
            break;
          }

          case CyanaMRParser::Integer_HB: {
            break;
          }

        default:
          break;
        }
        setState(773);
        match(CyanaMRParser::Integer_HB);
        break;
      }

      case CyanaMRParser::Concat_res_1: {
        setState(774);
        match(CyanaMRParser::Concat_res_1);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(784);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Atom2:
      case CyanaMRParser::Atom2_equ:
      case CyanaMRParser::Simple_name_HB: {
        setState(780);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CyanaMRParser::Atom2: {
            setState(777);
            match(CyanaMRParser::Atom2);
            setState(778);
            match(CyanaMRParser::Equ_op_HB);
            break;
          }

          case CyanaMRParser::Atom2_equ: {
            setState(779);
            match(CyanaMRParser::Atom2_equ);
            break;
          }

          case CyanaMRParser::Simple_name_HB: {
            break;
          }

        default:
          break;
        }
        setState(782);
        match(CyanaMRParser::Simple_name_HB);
        break;
      }

      case CyanaMRParser::Concat_atom_2: {
        setState(783);
        match(CyanaMRParser::Concat_atom_2);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(793);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Residue2:
      case CyanaMRParser::Residue2_equ:
      case CyanaMRParser::Integer_HB: {
        setState(789);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CyanaMRParser::Residue2: {
            setState(786);
            match(CyanaMRParser::Residue2);
            setState(787);
            match(CyanaMRParser::Equ_op_HB);
            break;
          }

          case CyanaMRParser::Residue2_equ: {
            setState(788);
            match(CyanaMRParser::Residue2_equ);
            break;
          }

          case CyanaMRParser::Integer_HB: {
            break;
          }

        default:
          break;
        }
        setState(791);
        match(CyanaMRParser::Integer_HB);
        break;
      }

      case CyanaMRParser::Concat_res_2: {
        setState(792);
        match(CyanaMRParser::Concat_res_2);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(795);
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
    setState(797);
    match(CyanaMRParser::Link);
    setState(798);
    gen_simple_name();
    setState(799);
    gen_res_num();
    setState(800);
    gen_simple_name();
    setState(801);
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
  enterRule(_localctx, 100, CyanaMRParser::RuleStereoassign_macro);
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
    setState(803);
    match(CyanaMRParser::Atom_stereo);
    setState(810);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CyanaMRParser::Double_quote_string: {
        setState(804);
        match(CyanaMRParser::Double_quote_string);
        break;
      }

      case CyanaMRParser::Simple_name_PR: {
        setState(805);
        match(CyanaMRParser::Simple_name_PR);
        setState(807);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CyanaMRParser::Simple_name_PR) {
          setState(806);
          match(CyanaMRParser::Simple_name_PR);
        }
        setState(809);
        match(CyanaMRParser::Integer_PR);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(812);
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
    setState(814);
    match(CyanaMRParser::Var);
    setState(818);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Simple_name_VA) {
      setState(815);
      match(CyanaMRParser::Simple_name_VA);
      setState(820);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(821);
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
    setState(823);
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
    setState(825);
    match(CyanaMRParser::Unset);
    setState(829);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Simple_name_VA) {
      setState(826);
      match(CyanaMRParser::Simple_name_VA);
      setState(831);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(832);
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
    setState(834);
    match(CyanaMRParser::Print);
    setState(835);
    match(CyanaMRParser::Double_quote_string);
    setState(836);
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
    setState(838);
    match(CyanaMRParser::Residue);
    setState(839);
    gen_simple_name();
    setState(841);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 118, _ctx)) {
    case 1: {
      setState(840);
      comment();
      break;
    }

    default:
      break;
    }
    setState(845); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(845);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Mapping: {
                  setState(843);
                  mapping_list();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(844);
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
      setState(847); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 120, _ctx);
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
    setState(849);
    match(CyanaMRParser::Mapping);
    setState(850);
    match(CyanaMRParser::Simple_name_MP);
    setState(851);
    match(CyanaMRParser::Equ_op_MP);
    setState(853); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(852);
      match(CyanaMRParser::Simple_name_MP);
      setState(855); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == CyanaMRParser::Simple_name_MP);
    setState(857);
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
    setState(859);
    match(CyanaMRParser::Residue);
    setState(860);
    gen_simple_name();
    setState(862);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 122, _ctx)) {
    case 1: {
      setState(861);
      comment();
      break;
    }

    default:
      break;
    }
    setState(866); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(866);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Ambig: {
                  setState(864);
                  ambig_list();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(865);
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
      setState(868); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 124, _ctx);
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
    setState(870);
    match(CyanaMRParser::Ambig);
    setState(871);
    _la = _input->LA(1);
    if (!(_la == CyanaMRParser::Ambig_code_MP

    || _la == CyanaMRParser::Simple_name_MP)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(872);
    match(CyanaMRParser::Equ_op_MP);
    setState(875); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(873);
      match(CyanaMRParser::Simple_name_MP);
      setState(874);
      match(CyanaMRParser::Integer_MP);
      setState(877); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == CyanaMRParser::Simple_name_MP);
    setState(879);
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
    setState(881);
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
    setState(883);
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
    setState(885);
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
    setState(887);
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
  enterRule(_localctx, 126, CyanaMRParser::RuleNumber_qc);
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
    setState(889);
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
  enterRule(_localctx, 128, CyanaMRParser::RuleGen_res_num_qc);
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
    setState(891);
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
  enterRule(_localctx, 130, CyanaMRParser::RuleGen_simple_name_qc);
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
    setState(893);
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
  enterRule(_localctx, 132, CyanaMRParser::RuleGen_atom_name_qc);
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
    setState(895);
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
