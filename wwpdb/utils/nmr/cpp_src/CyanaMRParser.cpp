
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaMRParser.g4 by ANTLR 4.13.0


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
CyanaMRParserStaticData *cyanamrparserParserStaticData = nullptr;

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
      "fixatmw2_distance_restraint", "qconvr_distance_restraints", "qconvr_distance_restraint", 
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
      "", "", "", "", "", "", "", "", "", "'NOEUPP'", "'NOELOW'", "'TYPE'", 
      "", "'OR'", "'SSBOND'", "", "'HBOND'", "'LINK'", "", "'VAR'", "'UNSET'", 
      "", "'PRINT'", "'RESIDUE'", "'MAPPING'", "'AMBIG'", "", "", "", "", 
      "", "", "", "", "", "", "'ATOM1'", "'ATOM2'", "'RESIDUE1'", "'RESIDUE2'"
    },
    std::vector<std::string>{
      "", "Ambig_code", "Integer", "Float", "Float_DecimalComma", "Orientation_header", 
      "Tensor_header", "SMCLN_COMMENT", "COMMENT", "NoeUpp", "NoeLow", "Type", 
      "Equ_op", "Or", "Ssbond", "Ssbond_resids", "Hbond", "Link", "Atom_stereo", 
      "Var", "Unset", "SetVar", "Print", "Residue", "Mapping", "Ambig", 
      "Capital_integer", "Integer_capital", "Simple_name", "SPACE", "ENCLOSE_COMMENT", 
      "SECTION_COMMENT", "LINE_COMMENT", "Any_name", "SPACE_CM", "RETURN_CM", 
      "Atom1", "Atom2", "Residue1", "Residue2", "Equ_op_HB", "Integer_HB", 
      "Simple_name_HB", "SPACE_HB", "RETURN_HB", "LINE_COMMENT_HB", "Double_quote_string", 
      "SPACE_PR", "RETURN_PR", "LINE_COMMENT_PR", "Simple_name_VA", "SPACE_VA", 
      "RETURN_VA", "LINE_COMMENT_VA", "Ambig_code_MP", "Integer_MP", "Simple_name_MP", 
      "Equ_op_MP", "SPACE_MP", "RETURN_MP", "LINE_COMMENT_MP"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,60,648,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,
  	35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,
  	42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,
  	49,2,50,7,50,2,51,7,51,1,0,1,0,4,0,107,8,0,11,0,12,0,108,1,0,1,0,1,0,
  	1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
  	0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,138,8,0,10,0,12,0,141,9,0,1,0,1,0,1,1,1,
  	1,5,1,147,8,1,10,1,12,1,150,9,1,1,1,1,1,1,2,4,2,155,8,2,11,2,12,2,156,
  	1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,167,8,3,1,3,3,3,170,8,3,1,3,3,3,173,
  	8,3,1,3,3,3,176,8,3,1,3,3,3,179,8,3,1,4,4,4,182,8,4,11,4,12,4,183,1,5,
  	1,5,1,5,1,5,1,5,1,5,3,5,192,8,5,1,5,1,5,1,5,3,5,197,8,5,1,5,3,5,200,8,
  	5,1,6,4,6,203,8,6,11,6,12,6,204,1,6,1,6,1,6,4,6,210,8,6,11,6,12,6,211,
  	1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,230,
  	8,8,1,9,4,9,233,8,9,11,9,12,9,234,1,9,1,9,1,9,4,9,240,8,9,11,9,12,9,241,
  	1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,
  	4,12,258,8,12,11,12,12,12,259,1,13,1,13,1,13,3,13,265,8,13,1,13,1,13,
  	1,13,1,13,1,13,1,13,1,13,4,13,274,8,13,11,13,12,13,275,1,14,4,14,279,
  	8,14,11,14,12,14,280,1,15,1,15,1,15,3,15,286,8,15,1,15,1,15,1,15,1,15,
  	1,15,1,15,1,15,1,15,4,15,296,8,15,11,15,12,15,297,1,16,4,16,301,8,16,
  	11,16,12,16,302,1,17,1,17,1,17,3,17,308,8,17,1,17,1,17,1,17,1,17,1,17,
  	1,17,1,17,1,17,1,17,4,17,319,8,17,11,17,12,17,320,1,18,4,18,324,8,18,
  	11,18,12,18,325,1,19,1,19,1,19,1,19,3,19,332,8,19,1,19,1,19,1,19,1,19,
  	1,19,1,19,4,19,340,8,19,11,19,12,19,341,1,20,4,20,345,8,20,11,20,12,20,
  	346,1,21,1,21,1,21,1,21,3,21,353,8,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
  	21,4,21,362,8,21,11,21,12,21,363,1,22,4,22,367,8,22,11,22,12,22,368,1,
  	23,1,23,1,23,1,23,3,23,375,8,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
  	23,4,23,385,8,23,11,23,12,23,386,1,24,4,24,390,8,24,11,24,12,24,391,1,
  	25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,4,26,404,8,26,11,26,12,
  	26,405,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,418,8,27,
  	1,27,3,27,421,8,27,1,27,3,27,424,8,27,1,27,3,27,427,8,27,1,27,3,27,430,
  	8,27,1,28,4,28,433,8,28,11,28,12,28,434,1,29,1,29,1,29,1,29,1,29,1,29,
  	1,29,1,29,1,29,1,29,3,29,447,8,29,1,29,3,29,450,8,29,1,29,3,29,453,8,
  	29,1,29,3,29,456,8,29,1,29,3,29,459,8,29,1,30,4,30,462,8,30,11,30,12,
  	30,463,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,476,8,31,
  	1,31,3,31,479,8,31,1,31,3,31,482,8,31,1,31,3,31,485,8,31,1,31,3,31,488,
  	8,31,1,32,4,32,491,8,32,11,32,12,32,492,1,33,1,33,1,33,1,33,1,33,1,33,
  	1,33,3,33,502,8,33,1,33,1,33,1,33,3,33,507,8,33,1,33,3,33,510,8,33,1,
  	34,4,34,513,8,34,11,34,12,34,514,1,35,1,35,1,35,1,35,1,35,1,35,3,35,523,
  	8,35,1,35,3,35,526,8,35,1,35,3,35,529,8,35,1,35,3,35,532,8,35,1,35,3,
  	35,535,8,35,1,36,1,36,1,36,1,37,1,37,1,37,3,37,543,8,37,1,37,1,37,1,37,
  	3,37,548,8,37,1,37,1,37,1,37,3,37,553,8,37,1,37,1,37,1,37,3,37,558,8,
  	37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,
  	40,1,40,5,40,575,8,40,10,40,12,40,578,9,40,1,40,1,40,1,41,1,41,1,42,1,
  	42,5,42,586,8,42,10,42,12,42,589,9,42,1,42,1,42,1,43,1,43,1,43,1,43,1,
  	44,1,44,1,44,3,44,600,8,44,1,44,1,44,4,44,604,8,44,11,44,12,44,605,1,
  	45,1,45,1,45,1,45,4,45,612,8,45,11,45,12,45,613,1,45,1,45,1,46,1,46,1,
  	46,3,46,621,8,46,1,46,1,46,4,46,625,8,46,11,46,12,46,626,1,47,1,47,1,
  	47,1,47,1,47,4,47,634,8,47,11,47,12,47,635,1,47,1,47,1,48,1,48,1,49,1,
  	49,1,50,1,50,1,51,1,51,1,51,0,0,52,0,2,4,6,8,10,12,14,16,18,20,22,24,
  	26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
  	72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,0,8,1,1,35,35,2,0,2,
  	2,26,28,1,0,9,10,2,0,54,54,56,56,1,0,2,4,2,0,2,2,26,27,1,0,26,28,2,0,
  	1,1,26,28,712,0,139,1,0,0,0,2,144,1,0,0,0,4,154,1,0,0,0,6,158,1,0,0,0,
  	8,181,1,0,0,0,10,185,1,0,0,0,12,202,1,0,0,0,14,213,1,0,0,0,16,218,1,0,
  	0,0,18,232,1,0,0,0,20,243,1,0,0,0,22,248,1,0,0,0,24,257,1,0,0,0,26,261,
  	1,0,0,0,28,278,1,0,0,0,30,282,1,0,0,0,32,300,1,0,0,0,34,304,1,0,0,0,36,
  	323,1,0,0,0,38,327,1,0,0,0,40,344,1,0,0,0,42,348,1,0,0,0,44,366,1,0,0,
  	0,46,370,1,0,0,0,48,389,1,0,0,0,50,393,1,0,0,0,52,403,1,0,0,0,54,407,
  	1,0,0,0,56,432,1,0,0,0,58,436,1,0,0,0,60,461,1,0,0,0,62,465,1,0,0,0,64,
  	490,1,0,0,0,66,494,1,0,0,0,68,512,1,0,0,0,70,516,1,0,0,0,72,536,1,0,0,
  	0,74,539,1,0,0,0,76,562,1,0,0,0,78,568,1,0,0,0,80,572,1,0,0,0,82,581,
  	1,0,0,0,84,583,1,0,0,0,86,592,1,0,0,0,88,596,1,0,0,0,90,607,1,0,0,0,92,
  	617,1,0,0,0,94,628,1,0,0,0,96,639,1,0,0,0,98,641,1,0,0,0,100,643,1,0,
  	0,0,102,645,1,0,0,0,104,138,5,5,0,0,105,107,5,6,0,0,106,105,1,0,0,0,107,
  	108,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,138,1,0,0,0,110,138,3,
  	2,1,0,111,138,3,4,2,0,112,138,3,24,12,0,113,138,3,28,14,0,114,138,3,32,
  	16,0,115,138,3,36,18,0,116,138,3,40,20,0,117,138,3,44,22,0,118,138,3,
  	48,24,0,119,138,3,52,26,0,120,138,3,56,28,0,121,138,3,60,30,0,122,138,
  	3,8,4,0,123,138,3,64,32,0,124,138,3,12,6,0,125,138,3,18,9,0,126,138,3,
  	68,34,0,127,138,3,72,36,0,128,138,3,74,37,0,129,138,3,76,38,0,130,138,
  	3,78,39,0,131,138,3,80,40,0,132,138,3,82,41,0,133,138,3,84,42,0,134,138,
  	3,86,43,0,135,138,3,88,44,0,136,138,3,92,46,0,137,104,1,0,0,0,137,106,
  	1,0,0,0,137,110,1,0,0,0,137,111,1,0,0,0,137,112,1,0,0,0,137,113,1,0,0,
  	0,137,114,1,0,0,0,137,115,1,0,0,0,137,116,1,0,0,0,137,117,1,0,0,0,137,
  	118,1,0,0,0,137,119,1,0,0,0,137,120,1,0,0,0,137,121,1,0,0,0,137,122,1,
  	0,0,0,137,123,1,0,0,0,137,124,1,0,0,0,137,125,1,0,0,0,137,126,1,0,0,0,
  	137,127,1,0,0,0,137,128,1,0,0,0,137,129,1,0,0,0,137,130,1,0,0,0,137,131,
  	1,0,0,0,137,132,1,0,0,0,137,133,1,0,0,0,137,134,1,0,0,0,137,135,1,0,0,
  	0,137,136,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,
  	142,1,0,0,0,141,139,1,0,0,0,142,143,5,0,0,1,143,1,1,0,0,0,144,148,5,8,
  	0,0,145,147,5,33,0,0,146,145,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,
  	148,149,1,0,0,0,149,151,1,0,0,0,150,148,1,0,0,0,151,152,7,0,0,0,152,3,
  	1,0,0,0,153,155,3,6,3,0,154,153,1,0,0,0,155,156,1,0,0,0,156,154,1,0,0,
  	0,156,157,1,0,0,0,157,5,1,0,0,0,158,159,3,98,49,0,159,160,3,100,50,0,
  	160,161,3,102,51,0,161,162,3,98,49,0,162,163,3,100,50,0,163,164,3,102,
  	51,0,164,166,3,96,48,0,165,167,3,96,48,0,166,165,1,0,0,0,166,167,1,0,
  	0,0,167,169,1,0,0,0,168,170,3,96,48,0,169,168,1,0,0,0,169,170,1,0,0,0,
  	170,172,1,0,0,0,171,173,3,96,48,0,172,171,1,0,0,0,172,173,1,0,0,0,173,
  	175,1,0,0,0,174,176,3,96,48,0,175,174,1,0,0,0,175,176,1,0,0,0,176,178,
  	1,0,0,0,177,179,3,96,48,0,178,177,1,0,0,0,178,179,1,0,0,0,179,7,1,0,0,
  	0,180,182,3,10,5,0,181,180,1,0,0,0,182,183,1,0,0,0,183,181,1,0,0,0,183,
  	184,1,0,0,0,184,9,1,0,0,0,185,186,3,98,49,0,186,187,3,100,50,0,187,188,
  	3,100,50,0,188,189,3,96,48,0,189,191,3,96,48,0,190,192,3,96,48,0,191,
  	190,1,0,0,0,191,192,1,0,0,0,192,196,1,0,0,0,193,194,5,11,0,0,194,195,
  	5,12,0,0,195,197,5,2,0,0,196,193,1,0,0,0,196,197,1,0,0,0,197,199,1,0,
  	0,0,198,200,5,13,0,0,199,198,1,0,0,0,199,200,1,0,0,0,200,11,1,0,0,0,201,
  	203,3,14,7,0,202,201,1,0,0,0,203,204,1,0,0,0,204,202,1,0,0,0,204,205,
  	1,0,0,0,205,209,1,0,0,0,206,210,5,5,0,0,207,210,3,2,1,0,208,210,3,16,
  	8,0,209,206,1,0,0,0,209,207,1,0,0,0,209,208,1,0,0,0,210,211,1,0,0,0,211,
  	209,1,0,0,0,211,212,1,0,0,0,212,13,1,0,0,0,213,214,5,2,0,0,214,215,3,
  	96,48,0,215,216,3,96,48,0,216,217,7,1,0,0,217,15,1,0,0,0,218,219,3,98,
  	49,0,219,220,3,100,50,0,220,221,3,100,50,0,221,222,3,98,49,0,222,223,
  	3,100,50,0,223,224,3,100,50,0,224,225,3,96,48,0,225,226,3,96,48,0,226,
  	227,3,96,48,0,227,229,5,2,0,0,228,230,3,96,48,0,229,228,1,0,0,0,229,230,
  	1,0,0,0,230,17,1,0,0,0,231,233,3,20,10,0,232,231,1,0,0,0,233,234,1,0,
  	0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,239,1,0,0,0,236,240,5,5,0,0,237,
  	240,3,2,1,0,238,240,3,22,11,0,239,236,1,0,0,0,239,237,1,0,0,0,239,238,
  	1,0,0,0,240,241,1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,19,1,0,0,
  	0,243,244,5,2,0,0,244,245,3,96,48,0,245,246,3,96,48,0,246,247,7,1,0,0,
  	247,21,1,0,0,0,248,249,3,98,49,0,249,250,3,100,50,0,250,251,3,100,50,
  	0,251,252,3,96,48,0,252,253,3,96,48,0,253,254,3,96,48,0,254,255,5,2,0,
  	0,255,23,1,0,0,0,256,258,3,26,13,0,257,256,1,0,0,0,258,259,1,0,0,0,259,
  	257,1,0,0,0,259,260,1,0,0,0,260,25,1,0,0,0,261,262,3,98,49,0,262,264,
  	3,100,50,0,263,265,3,2,1,0,264,263,1,0,0,0,264,265,1,0,0,0,265,273,1,
  	0,0,0,266,267,3,100,50,0,267,268,3,98,49,0,268,269,3,100,50,0,269,270,
  	3,100,50,0,270,271,3,96,48,0,271,274,1,0,0,0,272,274,3,2,1,0,273,266,
  	1,0,0,0,273,272,1,0,0,0,274,275,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,
  	0,276,27,1,0,0,0,277,279,3,30,15,0,278,277,1,0,0,0,279,280,1,0,0,0,280,
  	278,1,0,0,0,280,281,1,0,0,0,281,29,1,0,0,0,282,283,3,98,49,0,283,285,
  	3,100,50,0,284,286,3,2,1,0,285,284,1,0,0,0,285,286,1,0,0,0,286,295,1,
  	0,0,0,287,288,3,100,50,0,288,289,3,98,49,0,289,290,3,100,50,0,290,291,
  	3,100,50,0,291,292,3,96,48,0,292,293,3,96,48,0,293,296,1,0,0,0,294,296,
  	3,2,1,0,295,287,1,0,0,0,295,294,1,0,0,0,296,297,1,0,0,0,297,295,1,0,0,
  	0,297,298,1,0,0,0,298,31,1,0,0,0,299,301,3,34,17,0,300,299,1,0,0,0,301,
  	302,1,0,0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,33,1,0,0,0,304,305,3,
  	98,49,0,305,307,3,100,50,0,306,308,3,2,1,0,307,306,1,0,0,0,307,308,1,
  	0,0,0,308,318,1,0,0,0,309,310,3,100,50,0,310,311,3,98,49,0,311,312,3,
  	100,50,0,312,313,3,100,50,0,313,314,3,96,48,0,314,315,3,96,48,0,315,316,
  	3,96,48,0,316,319,1,0,0,0,317,319,3,2,1,0,318,309,1,0,0,0,318,317,1,0,
  	0,0,319,320,1,0,0,0,320,318,1,0,0,0,320,321,1,0,0,0,321,35,1,0,0,0,322,
  	324,3,38,19,0,323,322,1,0,0,0,324,325,1,0,0,0,325,323,1,0,0,0,325,326,
  	1,0,0,0,326,37,1,0,0,0,327,328,3,98,49,0,328,329,3,100,50,0,329,331,3,
  	100,50,0,330,332,3,2,1,0,331,330,1,0,0,0,331,332,1,0,0,0,332,339,1,0,
  	0,0,333,334,3,98,49,0,334,335,3,100,50,0,335,336,3,100,50,0,336,337,3,
  	96,48,0,337,340,1,0,0,0,338,340,3,2,1,0,339,333,1,0,0,0,339,338,1,0,0,
  	0,340,341,1,0,0,0,341,339,1,0,0,0,341,342,1,0,0,0,342,39,1,0,0,0,343,
  	345,3,42,21,0,344,343,1,0,0,0,345,346,1,0,0,0,346,344,1,0,0,0,346,347,
  	1,0,0,0,347,41,1,0,0,0,348,349,3,98,49,0,349,350,3,100,50,0,350,352,3,
  	100,50,0,351,353,3,2,1,0,352,351,1,0,0,0,352,353,1,0,0,0,353,361,1,0,
  	0,0,354,355,3,98,49,0,355,356,3,100,50,0,356,357,3,100,50,0,357,358,3,
  	96,48,0,358,359,3,96,48,0,359,362,1,0,0,0,360,362,3,2,1,0,361,354,1,0,
  	0,0,361,360,1,0,0,0,362,363,1,0,0,0,363,361,1,0,0,0,363,364,1,0,0,0,364,
  	43,1,0,0,0,365,367,3,46,23,0,366,365,1,0,0,0,367,368,1,0,0,0,368,366,
  	1,0,0,0,368,369,1,0,0,0,369,45,1,0,0,0,370,371,3,98,49,0,371,372,3,100,
  	50,0,372,374,3,100,50,0,373,375,3,2,1,0,374,373,1,0,0,0,374,375,1,0,0,
  	0,375,384,1,0,0,0,376,377,3,98,49,0,377,378,3,100,50,0,378,379,3,100,
  	50,0,379,380,3,96,48,0,380,381,3,96,48,0,381,382,3,96,48,0,382,385,1,
  	0,0,0,383,385,3,2,1,0,384,376,1,0,0,0,384,383,1,0,0,0,385,386,1,0,0,0,
  	386,384,1,0,0,0,386,387,1,0,0,0,387,47,1,0,0,0,388,390,3,50,25,0,389,
  	388,1,0,0,0,390,391,1,0,0,0,391,389,1,0,0,0,391,392,1,0,0,0,392,49,1,
  	0,0,0,393,394,7,2,0,0,394,395,3,100,50,0,395,396,3,98,49,0,396,397,3,
  	100,50,0,397,398,3,100,50,0,398,399,3,98,49,0,399,400,3,100,50,0,400,
  	401,3,96,48,0,401,51,1,0,0,0,402,404,3,54,27,0,403,402,1,0,0,0,404,405,
  	1,0,0,0,405,403,1,0,0,0,405,406,1,0,0,0,406,53,1,0,0,0,407,408,5,2,0,
  	0,408,409,3,100,50,0,409,410,3,100,50,0,410,411,3,100,50,0,411,412,5,
  	2,0,0,412,413,3,100,50,0,413,414,3,100,50,0,414,415,3,100,50,0,415,417,
  	3,96,48,0,416,418,3,96,48,0,417,416,1,0,0,0,417,418,1,0,0,0,418,420,1,
  	0,0,0,419,421,3,96,48,0,420,419,1,0,0,0,420,421,1,0,0,0,421,423,1,0,0,
  	0,422,424,3,96,48,0,423,422,1,0,0,0,423,424,1,0,0,0,424,426,1,0,0,0,425,
  	427,3,96,48,0,426,425,1,0,0,0,426,427,1,0,0,0,427,429,1,0,0,0,428,430,
  	3,96,48,0,429,428,1,0,0,0,429,430,1,0,0,0,430,55,1,0,0,0,431,433,3,58,
  	29,0,432,431,1,0,0,0,433,434,1,0,0,0,434,432,1,0,0,0,434,435,1,0,0,0,
  	435,57,1,0,0,0,436,437,3,100,50,0,437,438,5,2,0,0,438,439,3,100,50,0,
  	439,440,3,100,50,0,440,441,3,100,50,0,441,442,5,2,0,0,442,443,3,100,50,
  	0,443,444,3,100,50,0,444,446,3,96,48,0,445,447,3,96,48,0,446,445,1,0,
  	0,0,446,447,1,0,0,0,447,449,1,0,0,0,448,450,3,96,48,0,449,448,1,0,0,0,
  	449,450,1,0,0,0,450,452,1,0,0,0,451,453,3,96,48,0,452,451,1,0,0,0,452,
  	453,1,0,0,0,453,455,1,0,0,0,454,456,3,96,48,0,455,454,1,0,0,0,455,456,
  	1,0,0,0,456,458,1,0,0,0,457,459,3,96,48,0,458,457,1,0,0,0,458,459,1,0,
  	0,0,459,59,1,0,0,0,460,462,3,62,31,0,461,460,1,0,0,0,462,463,1,0,0,0,
  	463,461,1,0,0,0,463,464,1,0,0,0,464,61,1,0,0,0,465,466,3,100,50,0,466,
  	467,3,100,50,0,467,468,5,2,0,0,468,469,3,100,50,0,469,470,3,100,50,0,
  	470,471,3,100,50,0,471,472,5,2,0,0,472,473,3,100,50,0,473,475,3,96,48,
  	0,474,476,3,96,48,0,475,474,1,0,0,0,475,476,1,0,0,0,476,478,1,0,0,0,477,
  	479,3,96,48,0,478,477,1,0,0,0,478,479,1,0,0,0,479,481,1,0,0,0,480,482,
  	3,96,48,0,481,480,1,0,0,0,481,482,1,0,0,0,482,484,1,0,0,0,483,485,3,96,
  	48,0,484,483,1,0,0,0,484,485,1,0,0,0,485,487,1,0,0,0,486,488,3,96,48,
  	0,487,486,1,0,0,0,487,488,1,0,0,0,488,63,1,0,0,0,489,491,3,66,33,0,490,
  	489,1,0,0,0,491,492,1,0,0,0,492,490,1,0,0,0,492,493,1,0,0,0,493,65,1,
  	0,0,0,494,495,3,100,50,0,495,496,5,2,0,0,496,497,3,100,50,0,497,498,3,
  	100,50,0,498,499,3,96,48,0,499,501,3,96,48,0,500,502,3,96,48,0,501,500,
  	1,0,0,0,501,502,1,0,0,0,502,506,1,0,0,0,503,504,5,11,0,0,504,505,5,12,
  	0,0,505,507,5,2,0,0,506,503,1,0,0,0,506,507,1,0,0,0,507,509,1,0,0,0,508,
  	510,5,13,0,0,509,508,1,0,0,0,509,510,1,0,0,0,510,67,1,0,0,0,511,513,3,
  	70,35,0,512,511,1,0,0,0,513,514,1,0,0,0,514,512,1,0,0,0,514,515,1,0,0,
  	0,515,69,1,0,0,0,516,517,3,98,49,0,517,518,3,100,50,0,518,519,3,100,50,
  	0,519,520,3,100,50,0,520,522,3,96,48,0,521,523,3,96,48,0,522,521,1,0,
  	0,0,522,523,1,0,0,0,523,525,1,0,0,0,524,526,3,96,48,0,525,524,1,0,0,0,
  	525,526,1,0,0,0,526,528,1,0,0,0,527,529,3,96,48,0,528,527,1,0,0,0,528,
  	529,1,0,0,0,529,531,1,0,0,0,530,532,3,96,48,0,531,530,1,0,0,0,531,532,
  	1,0,0,0,532,534,1,0,0,0,533,535,3,96,48,0,534,533,1,0,0,0,534,535,1,0,
  	0,0,535,71,1,0,0,0,536,537,5,14,0,0,537,538,5,15,0,0,538,73,1,0,0,0,539,
  	542,5,16,0,0,540,541,5,36,0,0,541,543,5,40,0,0,542,540,1,0,0,0,542,543,
  	1,0,0,0,543,544,1,0,0,0,544,547,5,42,0,0,545,546,5,38,0,0,546,548,5,40,
  	0,0,547,545,1,0,0,0,547,548,1,0,0,0,548,549,1,0,0,0,549,552,5,41,0,0,
  	550,551,5,37,0,0,551,553,5,40,0,0,552,550,1,0,0,0,552,553,1,0,0,0,553,
  	554,1,0,0,0,554,557,5,42,0,0,555,556,5,39,0,0,556,558,5,40,0,0,557,555,
  	1,0,0,0,557,558,1,0,0,0,558,559,1,0,0,0,559,560,5,41,0,0,560,561,5,44,
  	0,0,561,75,1,0,0,0,562,563,5,17,0,0,563,564,3,100,50,0,564,565,3,98,49,
  	0,565,566,3,100,50,0,566,567,3,98,49,0,567,77,1,0,0,0,568,569,5,18,0,
  	0,569,570,5,46,0,0,570,571,5,48,0,0,571,79,1,0,0,0,572,576,5,19,0,0,573,
  	575,5,50,0,0,574,573,1,0,0,0,575,578,1,0,0,0,576,574,1,0,0,0,576,577,
  	1,0,0,0,577,579,1,0,0,0,578,576,1,0,0,0,579,580,5,52,0,0,580,81,1,0,0,
  	0,581,582,5,21,0,0,582,83,1,0,0,0,583,587,5,20,0,0,584,586,5,50,0,0,585,
  	584,1,0,0,0,586,589,1,0,0,0,587,585,1,0,0,0,587,588,1,0,0,0,588,590,1,
  	0,0,0,589,587,1,0,0,0,590,591,5,52,0,0,591,85,1,0,0,0,592,593,5,22,0,
  	0,593,594,5,46,0,0,594,595,5,48,0,0,595,87,1,0,0,0,596,597,5,23,0,0,597,
  	599,3,100,50,0,598,600,3,2,1,0,599,598,1,0,0,0,599,600,1,0,0,0,600,603,
  	1,0,0,0,601,604,3,90,45,0,602,604,3,2,1,0,603,601,1,0,0,0,603,602,1,0,
  	0,0,604,605,1,0,0,0,605,603,1,0,0,0,605,606,1,0,0,0,606,89,1,0,0,0,607,
  	608,5,24,0,0,608,609,5,56,0,0,609,611,5,57,0,0,610,612,5,56,0,0,611,610,
  	1,0,0,0,612,613,1,0,0,0,613,611,1,0,0,0,613,614,1,0,0,0,614,615,1,0,0,
  	0,615,616,5,59,0,0,616,91,1,0,0,0,617,618,5,23,0,0,618,620,3,100,50,0,
  	619,621,3,2,1,0,620,619,1,0,0,0,620,621,1,0,0,0,621,624,1,0,0,0,622,625,
  	3,94,47,0,623,625,3,2,1,0,624,622,1,0,0,0,624,623,1,0,0,0,625,626,1,0,
  	0,0,626,624,1,0,0,0,626,627,1,0,0,0,627,93,1,0,0,0,628,629,5,25,0,0,629,
  	630,7,3,0,0,630,633,5,57,0,0,631,632,5,56,0,0,632,634,5,55,0,0,633,631,
  	1,0,0,0,634,635,1,0,0,0,635,633,1,0,0,0,635,636,1,0,0,0,636,637,1,0,0,
  	0,637,638,5,59,0,0,638,95,1,0,0,0,639,640,7,4,0,0,640,97,1,0,0,0,641,
  	642,7,5,0,0,642,99,1,0,0,0,643,644,7,6,0,0,644,101,1,0,0,0,645,646,7,
  	7,0,0,646,103,1,0,0,0,88,108,137,139,148,156,166,169,172,175,178,183,
  	191,196,199,204,209,211,229,234,239,241,259,264,273,275,280,285,295,297,
  	302,307,318,320,325,331,339,341,346,352,361,363,368,374,384,386,391,405,
  	417,420,423,426,429,434,446,449,452,455,458,463,475,478,481,484,487,492,
  	501,506,509,514,522,525,528,531,534,542,547,552,557,576,587,599,603,605,
  	613,620,624,626,635
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  cyanamrparserParserStaticData = staticData.release();
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

std::vector<CyanaMRParser::Qconvr_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::qconvr_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Qconvr_distance_restraintsContext>();
}

CyanaMRParser::Qconvr_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::qconvr_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Qconvr_distance_restraintsContext>(i);
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
    setState(139);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 486492004) != 0)) {
      setState(137);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(104);
        match(CyanaMRParser::Orientation_header);
        break;
      }

      case 2: {
        setState(106); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(105);
                  match(CyanaMRParser::Tensor_header);
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(108); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 3: {
        setState(110);
        comment();
        break;
      }

      case 4: {
        setState(111);
        distance_restraints();
        break;
      }

      case 5: {
        setState(112);
        fixres_distance_restraints();
        break;
      }

      case 6: {
        setState(113);
        fixresw_distance_restraints();
        break;
      }

      case 7: {
        setState(114);
        fixresw2_distance_restraints();
        break;
      }

      case 8: {
        setState(115);
        fixatm_distance_restraints();
        break;
      }

      case 9: {
        setState(116);
        fixatmw_distance_restraints();
        break;
      }

      case 10: {
        setState(117);
        fixatmw2_distance_restraints();
        break;
      }

      case 11: {
        setState(118);
        qconvr_distance_restraints();
        break;
      }

      case 12: {
        setState(119);
        distance_w_chain_restraints();
        break;
      }

      case 13: {
        setState(120);
        distance_w_chain2_restraints();
        break;
      }

      case 14: {
        setState(121);
        distance_w_chain3_restraints();
        break;
      }

      case 15: {
        setState(122);
        torsion_angle_restraints();
        break;
      }

      case 16: {
        setState(123);
        torsion_angle_w_chain_restraints();
        break;
      }

      case 17: {
        setState(124);
        rdc_restraints();
        break;
      }

      case 18: {
        setState(125);
        pcs_restraints();
        break;
      }

      case 19: {
        setState(126);
        cco_restraints();
        break;
      }

      case 20: {
        setState(127);
        ssbond_macro();
        break;
      }

      case 21: {
        setState(128);
        hbond_macro();
        break;
      }

      case 22: {
        setState(129);
        link_statement();
        break;
      }

      case 23: {
        setState(130);
        stereoassign_macro();
        break;
      }

      case 24: {
        setState(131);
        declare_variable();
        break;
      }

      case 25: {
        setState(132);
        set_variable();
        break;
      }

      case 26: {
        setState(133);
        unset_variable();
        break;
      }

      case 27: {
        setState(134);
        print_macro();
        break;
      }

      case 28: {
        setState(135);
        unambig_atom_name_mapping();
        break;
      }

      case 29: {
        setState(136);
        ambig_atom_name_mapping();
        break;
      }

      default:
        break;
      }
      setState(141);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(142);
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
    setState(144);
    match(CyanaMRParser::COMMENT);
    setState(148);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Any_name) {
      setState(145);
      match(CyanaMRParser::Any_name);
      setState(150);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(151);
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
    setState(154); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(153);
              distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(156); 
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
    setState(158);
    gen_res_num();
    setState(159);
    gen_simple_name();
    setState(160);
    gen_atom_name();
    setState(161);
    gen_res_num();
    setState(162);
    gen_simple_name();
    setState(163);
    gen_atom_name();
    setState(164);
    number();
    setState(166);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx)) {
    case 1: {
      setState(165);
      number();
      break;
    }

    default:
      break;
    }
    setState(169);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 6, _ctx)) {
    case 1: {
      setState(168);
      number();
      break;
    }

    default:
      break;
    }
    setState(172);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx)) {
    case 1: {
      setState(171);
      number();
      break;
    }

    default:
      break;
    }
    setState(175);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx)) {
    case 1: {
      setState(174);
      number();
      break;
    }

    default:
      break;
    }
    setState(178);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx)) {
    case 1: {
      setState(177);
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
    setState(181); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(180);
              torsion_angle_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(183); 
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
    setState(185);
    gen_res_num();
    setState(186);
    gen_simple_name();
    setState(187);
    gen_simple_name();
    setState(188);
    number();
    setState(189);
    number();
    setState(191);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx)) {
    case 1: {
      setState(190);
      number();
      break;
    }

    default:
      break;
    }
    setState(196);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Type) {
      setState(193);
      match(CyanaMRParser::Type);
      setState(194);
      match(CyanaMRParser::Equ_op);
      setState(195);
      match(CyanaMRParser::Integer);
    }
    setState(199);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Or) {
      setState(198);
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
    setState(202); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(201);
              rdc_parameter();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(204); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(209); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(209);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Orientation_header: {
                  setState(206);
                  match(CyanaMRParser::Orientation_header);
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(207);
                  comment();
                  break;
                }

                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(208);
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
      setState(211); 
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
    setState(213);
    match(CyanaMRParser::Integer);
    setState(214);
    number();
    setState(215);
    number();
    setState(216);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 469762052) != 0))) {
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
    setState(218);
    gen_res_num();
    setState(219);
    gen_simple_name();
    setState(220);
    gen_simple_name();
    setState(221);
    gen_res_num();
    setState(222);
    gen_simple_name();
    setState(223);
    gen_simple_name();
    setState(224);
    number();
    setState(225);
    number();
    setState(226);
    number();
    setState(227);
    match(CyanaMRParser::Integer);
    setState(229);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx)) {
    case 1: {
      setState(228);
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
    setState(232); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(231);
              pcs_parameter();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(234); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(239); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(239);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Orientation_header: {
                  setState(236);
                  match(CyanaMRParser::Orientation_header);
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(237);
                  comment();
                  break;
                }

                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(238);
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
      setState(241); 
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
    setState(243);
    match(CyanaMRParser::Integer);
    setState(244);
    number();
    setState(245);
    number();
    setState(246);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 469762052) != 0))) {
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
    setState(248);
    gen_res_num();
    setState(249);
    gen_simple_name();
    setState(250);
    gen_simple_name();
    setState(251);
    number();
    setState(252);
    number();
    setState(253);
    number();
    setState(254);
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
    setState(257); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(256);
              fixres_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(259); 
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
    setState(261);
    gen_res_num();
    setState(262);
    gen_simple_name();
    setState(264);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 22, _ctx)) {
    case 1: {
      setState(263);
      comment();
      break;
    }

    default:
      break;
    }
    setState(273); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(273);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(266);
                  gen_simple_name();
                  setState(267);
                  gen_res_num();
                  setState(268);
                  gen_simple_name();
                  setState(269);
                  gen_simple_name();
                  setState(270);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(272);
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
      setState(275); 
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
    setState(278); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(277);
              fixresw_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(280); 
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
    setState(282);
    gen_res_num();
    setState(283);
    gen_simple_name();
    setState(285);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 26, _ctx)) {
    case 1: {
      setState(284);
      comment();
      break;
    }

    default:
      break;
    }
    setState(295); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(295);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(287);
                  gen_simple_name();
                  setState(288);
                  gen_res_num();
                  setState(289);
                  gen_simple_name();
                  setState(290);
                  gen_simple_name();
                  setState(291);
                  number();
                  setState(292);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(294);
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
      setState(297); 
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
    setState(300); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(299);
              fixresw2_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(302); 
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
    setState(304);
    gen_res_num();
    setState(305);
    gen_simple_name();
    setState(307);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 30, _ctx)) {
    case 1: {
      setState(306);
      comment();
      break;
    }

    default:
      break;
    }
    setState(318); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(318);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(309);
                  gen_simple_name();
                  setState(310);
                  gen_res_num();
                  setState(311);
                  gen_simple_name();
                  setState(312);
                  gen_simple_name();
                  setState(313);
                  number();
                  setState(314);
                  number();
                  setState(315);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(317);
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
      setState(320); 
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
    setState(323); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(322);
              fixatm_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(325); 
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
    setState(327);
    gen_res_num();
    setState(328);
    gen_simple_name();
    setState(329);
    gen_simple_name();
    setState(331);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 34, _ctx)) {
    case 1: {
      setState(330);
      comment();
      break;
    }

    default:
      break;
    }
    setState(339); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(339);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(333);
                  gen_res_num();
                  setState(334);
                  gen_simple_name();
                  setState(335);
                  gen_simple_name();
                  setState(336);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(338);
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
      setState(341); 
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
    setState(344); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(343);
              fixatmw_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(346); 
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
    setState(348);
    gen_res_num();
    setState(349);
    gen_simple_name();
    setState(350);
    gen_simple_name();
    setState(352);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 38, _ctx)) {
    case 1: {
      setState(351);
      comment();
      break;
    }

    default:
      break;
    }
    setState(361); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(361);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(354);
                  gen_res_num();
                  setState(355);
                  gen_simple_name();
                  setState(356);
                  gen_simple_name();
                  setState(357);
                  number();
                  setState(358);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(360);
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
      setState(363); 
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
    setState(366); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(365);
              fixatmw2_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(368); 
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
    setState(370);
    gen_res_num();
    setState(371);
    gen_simple_name();
    setState(372);
    gen_simple_name();
    setState(374);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 42, _ctx)) {
    case 1: {
      setState(373);
      comment();
      break;
    }

    default:
      break;
    }
    setState(384); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(384);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(376);
                  gen_res_num();
                  setState(377);
                  gen_simple_name();
                  setState(378);
                  gen_simple_name();
                  setState(379);
                  number();
                  setState(380);
                  number();
                  setState(381);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(383);
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
      setState(386); 
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

//----------------- Qconvr_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Qconvr_distance_restraintsContext::Qconvr_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Qconvr_distance_restraintContext *> CyanaMRParser::Qconvr_distance_restraintsContext::qconvr_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Qconvr_distance_restraintContext>();
}

CyanaMRParser::Qconvr_distance_restraintContext* CyanaMRParser::Qconvr_distance_restraintsContext::qconvr_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Qconvr_distance_restraintContext>(i);
}


size_t CyanaMRParser::Qconvr_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleQconvr_distance_restraints;
}


std::any CyanaMRParser::Qconvr_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitQconvr_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Qconvr_distance_restraintsContext* CyanaMRParser::qconvr_distance_restraints() {
  Qconvr_distance_restraintsContext *_localctx = _tracker.createInstance<Qconvr_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 48, CyanaMRParser::RuleQconvr_distance_restraints);

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
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(388);
              qconvr_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(391); 
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

//----------------- Qconvr_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Qconvr_distance_restraintContext::Qconvr_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Qconvr_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Qconvr_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Qconvr_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Qconvr_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

CyanaMRParser::NumberContext* CyanaMRParser::Qconvr_distance_restraintContext::number() {
  return getRuleContext<CyanaMRParser::NumberContext>(0);
}

tree::TerminalNode* CyanaMRParser::Qconvr_distance_restraintContext::NoeUpp() {
  return getToken(CyanaMRParser::NoeUpp, 0);
}

tree::TerminalNode* CyanaMRParser::Qconvr_distance_restraintContext::NoeLow() {
  return getToken(CyanaMRParser::NoeLow, 0);
}


size_t CyanaMRParser::Qconvr_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleQconvr_distance_restraint;
}


std::any CyanaMRParser::Qconvr_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitQconvr_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Qconvr_distance_restraintContext* CyanaMRParser::qconvr_distance_restraint() {
  Qconvr_distance_restraintContext *_localctx = _tracker.createInstance<Qconvr_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 50, CyanaMRParser::RuleQconvr_distance_restraint);
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
    setState(393);
    _la = _input->LA(1);
    if (!(_la == CyanaMRParser::NoeUpp

    || _la == CyanaMRParser::NoeLow)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(394);
    gen_simple_name();
    setState(395);
    gen_res_num();
    setState(396);
    gen_simple_name();
    setState(397);
    gen_simple_name();
    setState(398);
    gen_res_num();
    setState(399);
    gen_simple_name();
    setState(400);
    number();
   
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
  enterRule(_localctx, 52, CyanaMRParser::RuleDistance_w_chain_restraints);

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
    setState(403); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(402);
              distance_w_chain_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(405); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 46, _ctx);
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
  enterRule(_localctx, 54, CyanaMRParser::RuleDistance_w_chain_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(407);
    match(CyanaMRParser::Integer);
    setState(408);
    gen_simple_name();
    setState(409);
    gen_simple_name();
    setState(410);
    gen_simple_name();
    setState(411);
    match(CyanaMRParser::Integer);
    setState(412);
    gen_simple_name();
    setState(413);
    gen_simple_name();
    setState(414);
    gen_simple_name();
    setState(415);
    number();
    setState(417);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 47, _ctx)) {
    case 1: {
      setState(416);
      number();
      break;
    }

    default:
      break;
    }
    setState(420);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 48, _ctx)) {
    case 1: {
      setState(419);
      number();
      break;
    }

    default:
      break;
    }
    setState(423);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 49, _ctx)) {
    case 1: {
      setState(422);
      number();
      break;
    }

    default:
      break;
    }
    setState(426);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 50, _ctx)) {
    case 1: {
      setState(425);
      number();
      break;
    }

    default:
      break;
    }
    setState(429);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 51, _ctx)) {
    case 1: {
      setState(428);
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
  enterRule(_localctx, 56, CyanaMRParser::RuleDistance_w_chain2_restraints);

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
    setState(432); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(431);
              distance_w_chain2_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(434); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 52, _ctx);
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
  enterRule(_localctx, 58, CyanaMRParser::RuleDistance_w_chain2_restraint);

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
    gen_simple_name();
    setState(437);
    match(CyanaMRParser::Integer);
    setState(438);
    gen_simple_name();
    setState(439);
    gen_simple_name();
    setState(440);
    gen_simple_name();
    setState(441);
    match(CyanaMRParser::Integer);
    setState(442);
    gen_simple_name();
    setState(443);
    gen_simple_name();
    setState(444);
    number();
    setState(446);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 53, _ctx)) {
    case 1: {
      setState(445);
      number();
      break;
    }

    default:
      break;
    }
    setState(449);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 54, _ctx)) {
    case 1: {
      setState(448);
      number();
      break;
    }

    default:
      break;
    }
    setState(452);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 55, _ctx)) {
    case 1: {
      setState(451);
      number();
      break;
    }

    default:
      break;
    }
    setState(455);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 56, _ctx)) {
    case 1: {
      setState(454);
      number();
      break;
    }

    default:
      break;
    }
    setState(458);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 57, _ctx)) {
    case 1: {
      setState(457);
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
  enterRule(_localctx, 60, CyanaMRParser::RuleDistance_w_chain3_restraints);

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
    setState(461); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(460);
              distance_w_chain3_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(463); 
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
  enterRule(_localctx, 62, CyanaMRParser::RuleDistance_w_chain3_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(465);
    gen_simple_name();
    setState(466);
    gen_simple_name();
    setState(467);
    match(CyanaMRParser::Integer);
    setState(468);
    gen_simple_name();
    setState(469);
    gen_simple_name();
    setState(470);
    gen_simple_name();
    setState(471);
    match(CyanaMRParser::Integer);
    setState(472);
    gen_simple_name();
    setState(473);
    number();
    setState(475);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 59, _ctx)) {
    case 1: {
      setState(474);
      number();
      break;
    }

    default:
      break;
    }
    setState(478);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 60, _ctx)) {
    case 1: {
      setState(477);
      number();
      break;
    }

    default:
      break;
    }
    setState(481);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 61, _ctx)) {
    case 1: {
      setState(480);
      number();
      break;
    }

    default:
      break;
    }
    setState(484);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 62, _ctx)) {
    case 1: {
      setState(483);
      number();
      break;
    }

    default:
      break;
    }
    setState(487);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 63, _ctx)) {
    case 1: {
      setState(486);
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
  enterRule(_localctx, 64, CyanaMRParser::RuleTorsion_angle_w_chain_restraints);

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
    setState(490); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(489);
              torsion_angle_w_chain_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(492); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 64, _ctx);
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
  enterRule(_localctx, 66, CyanaMRParser::RuleTorsion_angle_w_chain_restraint);
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
    gen_simple_name();
    setState(495);
    match(CyanaMRParser::Integer);
    setState(496);
    gen_simple_name();
    setState(497);
    gen_simple_name();
    setState(498);
    number();
    setState(499);
    number();
    setState(501);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 65, _ctx)) {
    case 1: {
      setState(500);
      number();
      break;
    }

    default:
      break;
    }
    setState(506);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Type) {
      setState(503);
      match(CyanaMRParser::Type);
      setState(504);
      match(CyanaMRParser::Equ_op);
      setState(505);
      match(CyanaMRParser::Integer);
    }
    setState(509);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Or) {
      setState(508);
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
  enterRule(_localctx, 68, CyanaMRParser::RuleCco_restraints);

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
    setState(512); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(511);
              cco_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(514); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 68, _ctx);
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
  enterRule(_localctx, 70, CyanaMRParser::RuleCco_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(516);
    gen_res_num();
    setState(517);
    gen_simple_name();
    setState(518);
    gen_simple_name();
    setState(519);
    gen_simple_name();
    setState(520);
    number();
    setState(522);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 69, _ctx)) {
    case 1: {
      setState(521);
      number();
      break;
    }

    default:
      break;
    }
    setState(525);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 70, _ctx)) {
    case 1: {
      setState(524);
      number();
      break;
    }

    default:
      break;
    }
    setState(528);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 71, _ctx)) {
    case 1: {
      setState(527);
      number();
      break;
    }

    default:
      break;
    }
    setState(531);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 72, _ctx)) {
    case 1: {
      setState(530);
      number();
      break;
    }

    default:
      break;
    }
    setState(534);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 73, _ctx)) {
    case 1: {
      setState(533);
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
  enterRule(_localctx, 72, CyanaMRParser::RuleSsbond_macro);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(536);
    match(CyanaMRParser::Ssbond);
    setState(537);
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

std::vector<tree::TerminalNode *> CyanaMRParser::Hbond_macroContext::Simple_name_HB() {
  return getTokens(CyanaMRParser::Simple_name_HB);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Simple_name_HB(size_t i) {
  return getToken(CyanaMRParser::Simple_name_HB, i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Hbond_macroContext::Integer_HB() {
  return getTokens(CyanaMRParser::Integer_HB);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Integer_HB(size_t i) {
  return getToken(CyanaMRParser::Integer_HB, i);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::RETURN_HB() {
  return getToken(CyanaMRParser::RETURN_HB, 0);
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

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Residue1() {
  return getToken(CyanaMRParser::Residue1, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Atom2() {
  return getToken(CyanaMRParser::Atom2, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Residue2() {
  return getToken(CyanaMRParser::Residue2, 0);
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
  enterRule(_localctx, 74, CyanaMRParser::RuleHbond_macro);
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
    setState(539);
    match(CyanaMRParser::Hbond);
    setState(542);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Atom1) {
      setState(540);
      match(CyanaMRParser::Atom1);
      setState(541);
      match(CyanaMRParser::Equ_op_HB);
    }
    setState(544);
    match(CyanaMRParser::Simple_name_HB);
    setState(547);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Residue1) {
      setState(545);
      match(CyanaMRParser::Residue1);
      setState(546);
      match(CyanaMRParser::Equ_op_HB);
    }
    setState(549);
    match(CyanaMRParser::Integer_HB);
    setState(552);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Atom2) {
      setState(550);
      match(CyanaMRParser::Atom2);
      setState(551);
      match(CyanaMRParser::Equ_op_HB);
    }
    setState(554);
    match(CyanaMRParser::Simple_name_HB);
    setState(557);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Residue2) {
      setState(555);
      match(CyanaMRParser::Residue2);
      setState(556);
      match(CyanaMRParser::Equ_op_HB);
    }
    setState(559);
    match(CyanaMRParser::Integer_HB);
    setState(560);
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
  enterRule(_localctx, 76, CyanaMRParser::RuleLink_statement);

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
    match(CyanaMRParser::Link);
    setState(563);
    gen_simple_name();
    setState(564);
    gen_res_num();
    setState(565);
    gen_simple_name();
    setState(566);
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
  enterRule(_localctx, 78, CyanaMRParser::RuleStereoassign_macro);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(568);
    match(CyanaMRParser::Atom_stereo);
    setState(569);
    match(CyanaMRParser::Double_quote_string);
    setState(570);
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
  enterRule(_localctx, 80, CyanaMRParser::RuleDeclare_variable);
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
    match(CyanaMRParser::Var);
    setState(576);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Simple_name_VA) {
      setState(573);
      match(CyanaMRParser::Simple_name_VA);
      setState(578);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(579);
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
  enterRule(_localctx, 82, CyanaMRParser::RuleSet_variable);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(581);
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
  enterRule(_localctx, 84, CyanaMRParser::RuleUnset_variable);
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
    setState(583);
    match(CyanaMRParser::Unset);
    setState(587);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Simple_name_VA) {
      setState(584);
      match(CyanaMRParser::Simple_name_VA);
      setState(589);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(590);
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
  enterRule(_localctx, 86, CyanaMRParser::RulePrint_macro);

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
    match(CyanaMRParser::Print);
    setState(593);
    match(CyanaMRParser::Double_quote_string);
    setState(594);
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
  enterRule(_localctx, 88, CyanaMRParser::RuleUnambig_atom_name_mapping);

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
    setState(596);
    match(CyanaMRParser::Residue);
    setState(597);
    gen_simple_name();
    setState(599);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 80, _ctx)) {
    case 1: {
      setState(598);
      comment();
      break;
    }

    default:
      break;
    }
    setState(603); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(603);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Mapping: {
                  setState(601);
                  mapping_list();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(602);
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
      setState(605); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 82, _ctx);
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
  enterRule(_localctx, 90, CyanaMRParser::RuleMapping_list);
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
    setState(607);
    match(CyanaMRParser::Mapping);
    setState(608);
    match(CyanaMRParser::Simple_name_MP);
    setState(609);
    match(CyanaMRParser::Equ_op_MP);
    setState(611); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(610);
      match(CyanaMRParser::Simple_name_MP);
      setState(613); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == CyanaMRParser::Simple_name_MP);
    setState(615);
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
  enterRule(_localctx, 92, CyanaMRParser::RuleAmbig_atom_name_mapping);

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
    setState(617);
    match(CyanaMRParser::Residue);
    setState(618);
    gen_simple_name();
    setState(620);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 84, _ctx)) {
    case 1: {
      setState(619);
      comment();
      break;
    }

    default:
      break;
    }
    setState(624); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(624);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Ambig: {
                  setState(622);
                  ambig_list();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(623);
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
      setState(626); 
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
  enterRule(_localctx, 94, CyanaMRParser::RuleAmbig_list);
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
    setState(628);
    match(CyanaMRParser::Ambig);
    setState(629);
    _la = _input->LA(1);
    if (!(_la == CyanaMRParser::Ambig_code_MP

    || _la == CyanaMRParser::Simple_name_MP)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(630);
    match(CyanaMRParser::Equ_op_MP);
    setState(633); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(631);
      match(CyanaMRParser::Simple_name_MP);
      setState(632);
      match(CyanaMRParser::Integer_MP);
      setState(635); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == CyanaMRParser::Simple_name_MP);
    setState(637);
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
  enterRule(_localctx, 96, CyanaMRParser::RuleNumber);
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
    setState(639);
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
  enterRule(_localctx, 98, CyanaMRParser::RuleGen_res_num);
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
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 201326596) != 0))) {
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
  enterRule(_localctx, 100, CyanaMRParser::RuleGen_simple_name);
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
    setState(643);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 469762048) != 0))) {
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
  enterRule(_localctx, 102, CyanaMRParser::RuleGen_atom_name);
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
    setState(645);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 469762050) != 0))) {
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
