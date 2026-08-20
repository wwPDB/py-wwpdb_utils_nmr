
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrPipePKParser.g4 by ANTLR 4.13.2


#include "NmrPipePKParserVisitor.h"

#include "NmrPipePKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct NmrPipePKParserStaticData final {
  NmrPipePKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  NmrPipePKParserStaticData(const NmrPipePKParserStaticData&) = delete;
  NmrPipePKParserStaticData(NmrPipePKParserStaticData&&) = delete;
  NmrPipePKParserStaticData& operator=(const NmrPipePKParserStaticData&) = delete;
  NmrPipePKParserStaticData& operator=(NmrPipePKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag nmrpipepkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<NmrPipePKParserStaticData> nmrpipepkparserParserStaticData = nullptr;

void nmrpipepkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (nmrpipepkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(nmrpipepkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<NmrPipePKParserStaticData>(
    std::vector<std::string>{
      "nmrpipe_pk", "data_label", "peak_list_2d", "peak_2d", "peak_list_3d", 
      "peak_3d", "peak_list_4d", "peak_4d", "pipp_label", "pipp_axis", "pipp_peak_list_2d", 
      "pipp_peak_2d", "pipp_peak_list_3d", "pipp_peak_3d", "pipp_peak_list_4d", 
      "pipp_peak_4d", "pipp_row_peak_list_2d", "pipp_row_peak_2d", "pipp_row_peak_list_3d", 
      "pipp_row_peak_3d", "pipp_row_peak_list_4d", "pipp_row_peak_4d", "number"
    },
    std::vector<std::string>{
      "", "'DATA'", "'VARS'", "'FORMAT'", "'NULLVALUE'", "'NULLSTRING'", 
      "'('", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "'DIMCOUNT'", "'PPM'", "'HZ'", "", "", "", "", "", "", "", "'INDEX'", 
      "", "", "", "", "'DX'", "'DY'", "'DZ'", "'DA'", "'X_PPM'", "'Y_PPM'", 
      "'Z_PPM'", "'A_PPM'", "'X_HZ'", "'Y_HZ'", "'Z_HZ'", "'A_HZ'", "'XW'", 
      "'YW'", "'ZW'", "'AW'", "'XW_HZ'", "'YW_HZ'", "'ZW_HZ'", "'AW_HZ'", 
      "'X1'", "'X3'", "'Y1'", "'Y3'", "'Z1'", "'Z3'", "'A1'", "'A3'", "'HEIGHT'", 
      "'DHEIGHT'", "'VOL'", "'PCHI2'", "'TYPE'", "'ASS'", "'CLUSTID'", "'MEMCNT'", 
      "'TROUBLE'", "'PkID'", "'Sl.Z'", "'Sl.A'", "'X'", "'Y'", "'Z'", "'A'", 
      "'Intensity'", "'Assign'", "'Assign1'", "'Assign2'", "", "", "", "", 
      "", "", "", "", "", "", "", "", "", "", "", "", "", "')'", "'['", 
      "']'", "','", "';'", "'#'", "'%'", "'^'"
    },
    std::vector<std::string>{
      "", "Data", "Vars", "Format", "Null_value", "Null_string", "L_paren", 
      "Integer", "Float", "Real", "SHARP_COMMENT", "EXCLM_COMMENT", "Any_name", 
      "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT", "X_axis_DA", 
      "Y_axis_DA", "Z_axis_DA", "A_axis_DA", "Ppm_value_DA", "Dim_count_DA", 
      "Ppm_DA", "Hz_DA", "Integer_DA", "Float_DA", "Real_DA", "Simple_name_DA", 
      "SPACE_DA", "RETURN_DA", "LINE_COMMENT_DA", "Index", "X_axis", "Y_axis", 
      "Z_axis", "A_axis", "Dx", "Dy", "Dz", "Da", "X_ppm", "Y_ppm", "Z_ppm", 
      "A_ppm", "X_hz", "Y_hz", "Z_hz", "A_hz", "Xw", "Yw", "Zw", "Aw", "Xw_hz", 
      "Yw_hz", "Zw_hz", "Aw_hz", "X1", "X3", "Y1", "Y3", "Z1", "Z3", "A1", 
      "A3", "Height", "DHeight", "Vol", "Pchi2", "Type", "Ass", "ClustId", 
      "Memcnt", "Trouble", "PkID", "Sl_Z", "Sl_A", "X", "Y", "Z", "A", "Intensity", 
      "Assign", "Assign1", "Assign2", "Integer_VA", "Float_VA", "Real_VA", 
      "Simple_name_VA", "SPACE_VA", "RETURN_VA", "LINE_COMMENT_VA", "Format_code", 
      "SPACE_FO", "RETURN_FO", "LINE_COMMENT_FO", "Any_name_NV", "SPACE_NV", 
      "RETURN_NV", "Any_name_NS", "SPACE_NS", "RETURN_NS", "R_paren", "L_brkt", 
      "R_brkt", "Comma", "Semicolon", "Number_sign", "Percent_sign", "Caret", 
      "Integer_PR", "Float_PR", "Real_PR", "Assignments_PR", "SPACE_PR", 
      "RETURN_PR"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,115,729,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,1,0,3,0,48,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
  	0,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
  	1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
  	2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,102,8,2,1,2,1,2,1,2,3,2,107,8,2,
  	1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
  	2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,134,8,2,1,2,1,2,1,2,3,2,139,8,2,1,2,
  	1,2,1,2,1,2,3,2,145,8,2,1,2,1,2,1,2,3,2,150,8,2,1,2,4,2,153,8,2,11,2,
  	12,2,154,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
  	1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,180,8,3,1,3,1,3,1,3,3,3,185,8,3,1,
  	3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
  	1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,221,
  	8,4,1,4,1,4,1,4,3,4,226,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
  	4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
  	1,4,1,4,1,4,1,4,1,4,3,4,261,8,4,1,4,1,4,1,4,3,4,266,8,4,1,4,1,4,1,4,1,
  	4,3,4,272,8,4,1,4,1,4,1,4,3,4,277,8,4,1,4,4,4,280,8,4,11,4,12,4,281,1,
  	5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
  	1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,315,8,5,1,5,1,
  	5,1,5,3,5,320,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
  	1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
  	6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,364,8,6,1,6,1,6,1,6,
  	3,6,369,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
  	6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
  	1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,412,8,6,1,6,1,6,1,6,3,6,417,8,
  	6,1,6,1,6,1,6,1,6,3,6,423,8,6,1,6,1,6,1,6,3,6,428,8,6,1,6,4,6,431,8,6,
  	11,6,12,6,432,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
  	1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
  	7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,474,8,7,1,7,1,7,1,7,3,7,479,8,7,1,7,
  	1,7,1,8,1,8,1,8,1,8,1,8,4,8,488,8,8,11,8,12,8,489,1,9,1,9,1,9,1,9,1,9,
  	1,9,1,9,1,9,1,9,1,9,1,10,1,10,4,10,504,8,10,11,10,12,10,505,1,10,1,10,
  	1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,517,8,10,1,10,1,10,4,10,521,8,
  	10,11,10,12,10,522,1,11,1,11,1,11,1,11,4,11,529,8,11,11,11,12,11,530,
  	1,11,1,11,1,12,1,12,4,12,537,8,12,11,12,12,12,538,1,12,1,12,1,12,1,12,
  	3,12,545,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,554,8,12,1,12,1,
  	12,4,12,558,8,12,11,12,12,12,559,1,13,1,13,3,13,564,8,13,1,13,1,13,1,
  	13,1,13,4,13,570,8,13,11,13,12,13,571,1,13,1,13,1,14,1,14,4,14,578,8,
  	14,11,14,12,14,579,1,14,1,14,1,14,1,14,3,14,586,8,14,1,14,3,14,589,8,
  	14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,599,8,14,1,14,1,14,4,
  	14,603,8,14,11,14,12,14,604,1,15,1,15,3,15,609,8,15,1,15,3,15,612,8,15,
  	1,15,1,15,1,15,1,15,1,15,4,15,619,8,15,11,15,12,15,620,1,15,1,15,1,16,
  	4,16,626,8,16,11,16,12,16,627,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
  	1,17,1,17,1,17,1,17,1,17,1,17,3,17,644,8,17,1,17,1,17,1,17,1,17,1,17,
  	1,17,1,17,1,17,1,17,1,18,4,18,656,8,18,11,18,12,18,657,1,19,1,19,1,19,
  	1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
  	1,19,3,19,678,8,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,
  	4,20,690,8,20,11,20,12,20,691,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
  	1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
  	3,21,716,8,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,
  	1,22,0,0,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
  	42,44,0,5,1,0,17,20,1,1,14,14,1,0,23,24,1,1,115,115,2,0,7,9,12,12,773,
  	0,47,1,0,0,0,2,68,1,0,0,0,4,77,1,0,0,0,6,156,1,0,0,0,8,188,1,0,0,0,10,
  	283,1,0,0,0,12,323,1,0,0,0,14,434,1,0,0,0,16,482,1,0,0,0,18,491,1,0,0,
  	0,20,501,1,0,0,0,22,524,1,0,0,0,24,534,1,0,0,0,26,561,1,0,0,0,28,575,
  	1,0,0,0,30,606,1,0,0,0,32,625,1,0,0,0,34,629,1,0,0,0,36,655,1,0,0,0,38,
  	659,1,0,0,0,40,689,1,0,0,0,42,693,1,0,0,0,44,726,1,0,0,0,46,48,5,14,0,
  	0,47,46,1,0,0,0,47,48,1,0,0,0,48,63,1,0,0,0,49,62,3,2,1,0,50,62,3,4,2,
  	0,51,62,3,8,4,0,52,62,3,12,6,0,53,62,3,16,8,0,54,62,3,20,10,0,55,62,3,
  	24,12,0,56,62,3,28,14,0,57,62,3,32,16,0,58,62,3,36,18,0,59,62,3,40,20,
  	0,60,62,5,14,0,0,61,49,1,0,0,0,61,50,1,0,0,0,61,51,1,0,0,0,61,52,1,0,
  	0,0,61,53,1,0,0,0,61,54,1,0,0,0,61,55,1,0,0,0,61,56,1,0,0,0,61,57,1,0,
  	0,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,
  	0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,0,0,1,67,1,1,0,
  	0,0,68,69,5,1,0,0,69,70,7,0,0,0,70,71,5,28,0,0,71,72,5,25,0,0,72,73,5,
  	25,0,0,73,74,5,21,0,0,74,75,5,21,0,0,75,76,5,30,0,0,76,3,1,0,0,0,77,78,
  	5,2,0,0,78,79,5,32,0,0,79,80,5,33,0,0,80,81,5,34,0,0,81,82,5,37,0,0,82,
  	83,5,38,0,0,83,84,5,41,0,0,84,85,5,42,0,0,85,86,5,45,0,0,86,87,5,46,0,
  	0,87,88,5,49,0,0,88,89,5,50,0,0,89,90,5,53,0,0,90,91,5,54,0,0,91,92,5,
  	57,0,0,92,93,5,58,0,0,93,94,5,59,0,0,94,95,5,60,0,0,95,96,5,65,0,0,96,
  	97,5,66,0,0,97,98,5,67,0,0,98,99,5,68,0,0,99,101,5,69,0,0,100,102,5,70,
  	0,0,101,100,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,5,71,0,0,
  	104,106,5,72,0,0,105,107,5,73,0,0,106,105,1,0,0,0,106,107,1,0,0,0,107,
  	108,1,0,0,0,108,109,5,90,0,0,109,110,5,3,0,0,110,111,5,92,0,0,111,112,
  	5,92,0,0,112,113,5,92,0,0,113,114,5,92,0,0,114,115,5,92,0,0,115,116,5,
  	92,0,0,116,117,5,92,0,0,117,118,5,92,0,0,118,119,5,92,0,0,119,120,5,92,
  	0,0,120,121,5,92,0,0,121,122,5,92,0,0,122,123,5,92,0,0,123,124,5,92,0,
  	0,124,125,5,92,0,0,125,126,5,92,0,0,126,127,5,92,0,0,127,128,5,92,0,0,
  	128,129,5,92,0,0,129,130,5,92,0,0,130,131,5,92,0,0,131,133,5,92,0,0,132,
  	134,5,92,0,0,133,132,1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,136,
  	5,92,0,0,136,138,5,92,0,0,137,139,5,92,0,0,138,137,1,0,0,0,138,139,1,
  	0,0,0,139,140,1,0,0,0,140,144,5,94,0,0,141,142,5,4,0,0,142,143,5,96,0,
  	0,143,145,5,98,0,0,144,141,1,0,0,0,144,145,1,0,0,0,145,149,1,0,0,0,146,
  	147,5,5,0,0,147,148,5,99,0,0,148,150,5,101,0,0,149,146,1,0,0,0,149,150,
  	1,0,0,0,150,152,1,0,0,0,151,153,3,6,3,0,152,151,1,0,0,0,153,154,1,0,0,
  	0,154,152,1,0,0,0,154,155,1,0,0,0,155,5,1,0,0,0,156,157,5,7,0,0,157,158,
  	3,44,22,0,158,159,3,44,22,0,159,160,3,44,22,0,160,161,3,44,22,0,161,162,
  	3,44,22,0,162,163,3,44,22,0,163,164,3,44,22,0,164,165,3,44,22,0,165,166,
  	3,44,22,0,166,167,3,44,22,0,167,168,3,44,22,0,168,169,3,44,22,0,169,170,
  	5,7,0,0,170,171,5,7,0,0,171,172,5,7,0,0,172,173,5,7,0,0,173,174,3,44,
  	22,0,174,175,3,44,22,0,175,176,3,44,22,0,176,177,3,44,22,0,177,179,5,
  	7,0,0,178,180,5,12,0,0,179,178,1,0,0,0,179,180,1,0,0,0,180,181,1,0,0,
  	0,181,182,5,7,0,0,182,184,5,7,0,0,183,185,5,7,0,0,184,183,1,0,0,0,184,
  	185,1,0,0,0,185,186,1,0,0,0,186,187,7,1,0,0,187,7,1,0,0,0,188,189,5,2,
  	0,0,189,190,5,32,0,0,190,191,5,33,0,0,191,192,5,34,0,0,192,193,5,35,0,
  	0,193,194,5,37,0,0,194,195,5,38,0,0,195,196,5,39,0,0,196,197,5,41,0,0,
  	197,198,5,42,0,0,198,199,5,43,0,0,199,200,5,45,0,0,200,201,5,46,0,0,201,
  	202,5,47,0,0,202,203,5,49,0,0,203,204,5,50,0,0,204,205,5,51,0,0,205,206,
  	5,53,0,0,206,207,5,54,0,0,207,208,5,55,0,0,208,209,5,57,0,0,209,210,5,
  	58,0,0,210,211,5,59,0,0,211,212,5,60,0,0,212,213,5,61,0,0,213,214,5,62,
  	0,0,214,215,5,65,0,0,215,216,5,66,0,0,216,217,5,67,0,0,217,218,5,68,0,
  	0,218,220,5,69,0,0,219,221,5,70,0,0,220,219,1,0,0,0,220,221,1,0,0,0,221,
  	222,1,0,0,0,222,223,5,71,0,0,223,225,5,72,0,0,224,226,5,73,0,0,225,224,
  	1,0,0,0,225,226,1,0,0,0,226,227,1,0,0,0,227,228,5,90,0,0,228,229,5,3,
  	0,0,229,230,5,92,0,0,230,231,5,92,0,0,231,232,5,92,0,0,232,233,5,92,0,
  	0,233,234,5,92,0,0,234,235,5,92,0,0,235,236,5,92,0,0,236,237,5,92,0,0,
  	237,238,5,92,0,0,238,239,5,92,0,0,239,240,5,92,0,0,240,241,5,92,0,0,241,
  	242,5,92,0,0,242,243,5,92,0,0,243,244,5,92,0,0,244,245,5,92,0,0,245,246,
  	5,92,0,0,246,247,5,92,0,0,247,248,5,92,0,0,248,249,5,92,0,0,249,250,5,
  	92,0,0,250,251,5,92,0,0,251,252,5,92,0,0,252,253,5,92,0,0,253,254,5,92,
  	0,0,254,255,5,92,0,0,255,256,5,92,0,0,256,257,5,92,0,0,257,258,5,92,0,
  	0,258,260,5,92,0,0,259,261,5,92,0,0,260,259,1,0,0,0,260,261,1,0,0,0,261,
  	262,1,0,0,0,262,263,5,92,0,0,263,265,5,92,0,0,264,266,5,92,0,0,265,264,
  	1,0,0,0,265,266,1,0,0,0,266,267,1,0,0,0,267,271,5,94,0,0,268,269,5,4,
  	0,0,269,270,5,96,0,0,270,272,5,98,0,0,271,268,1,0,0,0,271,272,1,0,0,0,
  	272,276,1,0,0,0,273,274,5,5,0,0,274,275,5,99,0,0,275,277,5,101,0,0,276,
  	273,1,0,0,0,276,277,1,0,0,0,277,279,1,0,0,0,278,280,3,10,5,0,279,278,
  	1,0,0,0,280,281,1,0,0,0,281,279,1,0,0,0,281,282,1,0,0,0,282,9,1,0,0,0,
  	283,284,5,7,0,0,284,285,3,44,22,0,285,286,3,44,22,0,286,287,3,44,22,0,
  	287,288,3,44,22,0,288,289,3,44,22,0,289,290,3,44,22,0,290,291,3,44,22,
  	0,291,292,3,44,22,0,292,293,3,44,22,0,293,294,3,44,22,0,294,295,3,44,
  	22,0,295,296,3,44,22,0,296,297,3,44,22,0,297,298,3,44,22,0,298,299,3,
  	44,22,0,299,300,3,44,22,0,300,301,3,44,22,0,301,302,3,44,22,0,302,303,
  	5,7,0,0,303,304,5,7,0,0,304,305,5,7,0,0,305,306,5,7,0,0,306,307,5,7,0,
  	0,307,308,5,7,0,0,308,309,3,44,22,0,309,310,3,44,22,0,310,311,3,44,22,
  	0,311,312,3,44,22,0,312,314,5,7,0,0,313,315,5,12,0,0,314,313,1,0,0,0,
  	314,315,1,0,0,0,315,316,1,0,0,0,316,317,5,7,0,0,317,319,5,7,0,0,318,320,
  	5,7,0,0,319,318,1,0,0,0,319,320,1,0,0,0,320,321,1,0,0,0,321,322,7,1,0,
  	0,322,11,1,0,0,0,323,324,5,2,0,0,324,325,5,32,0,0,325,326,5,33,0,0,326,
  	327,5,34,0,0,327,328,5,35,0,0,328,329,5,36,0,0,329,330,5,37,0,0,330,331,
  	5,38,0,0,331,332,5,39,0,0,332,333,5,39,0,0,333,334,5,41,0,0,334,335,5,
  	42,0,0,335,336,5,43,0,0,336,337,5,44,0,0,337,338,5,45,0,0,338,339,5,46,
  	0,0,339,340,5,47,0,0,340,341,5,48,0,0,341,342,5,49,0,0,342,343,5,50,0,
  	0,343,344,5,51,0,0,344,345,5,52,0,0,345,346,5,53,0,0,346,347,5,54,0,0,
  	347,348,5,55,0,0,348,349,5,56,0,0,349,350,5,57,0,0,350,351,5,58,0,0,351,
  	352,5,59,0,0,352,353,5,60,0,0,353,354,5,61,0,0,354,355,5,62,0,0,355,356,
  	5,63,0,0,356,357,5,64,0,0,357,358,5,65,0,0,358,359,5,66,0,0,359,360,5,
  	67,0,0,360,361,5,68,0,0,361,363,5,69,0,0,362,364,5,70,0,0,363,362,1,0,
  	0,0,363,364,1,0,0,0,364,365,1,0,0,0,365,366,5,71,0,0,366,368,5,72,0,0,
  	367,369,5,73,0,0,368,367,1,0,0,0,368,369,1,0,0,0,369,370,1,0,0,0,370,
  	371,5,90,0,0,371,372,5,3,0,0,372,373,5,92,0,0,373,374,5,92,0,0,374,375,
  	5,92,0,0,375,376,5,92,0,0,376,377,5,92,0,0,377,378,5,92,0,0,378,379,5,
  	92,0,0,379,380,5,92,0,0,380,381,5,92,0,0,381,382,5,92,0,0,382,383,5,92,
  	0,0,383,384,5,92,0,0,384,385,5,92,0,0,385,386,5,92,0,0,386,387,5,92,0,
  	0,387,388,5,92,0,0,388,389,5,92,0,0,389,390,5,92,0,0,390,391,5,92,0,0,
  	391,392,5,92,0,0,392,393,5,92,0,0,393,394,5,92,0,0,394,395,5,92,0,0,395,
  	396,5,92,0,0,396,397,5,92,0,0,397,398,5,92,0,0,398,399,5,92,0,0,399,400,
  	5,92,0,0,400,401,5,92,0,0,401,402,5,92,0,0,402,403,5,92,0,0,403,404,5,
  	92,0,0,404,405,5,92,0,0,405,406,5,92,0,0,406,407,5,92,0,0,407,408,5,92,
  	0,0,408,409,5,92,0,0,409,411,5,92,0,0,410,412,5,92,0,0,411,410,1,0,0,
  	0,411,412,1,0,0,0,412,413,1,0,0,0,413,414,5,92,0,0,414,416,5,92,0,0,415,
  	417,5,92,0,0,416,415,1,0,0,0,416,417,1,0,0,0,417,418,1,0,0,0,418,422,
  	5,94,0,0,419,420,5,4,0,0,420,421,5,96,0,0,421,423,5,98,0,0,422,419,1,
  	0,0,0,422,423,1,0,0,0,423,427,1,0,0,0,424,425,5,5,0,0,425,426,5,99,0,
  	0,426,428,5,101,0,0,427,424,1,0,0,0,427,428,1,0,0,0,428,430,1,0,0,0,429,
  	431,3,14,7,0,430,429,1,0,0,0,431,432,1,0,0,0,432,430,1,0,0,0,432,433,
  	1,0,0,0,433,13,1,0,0,0,434,435,5,7,0,0,435,436,3,44,22,0,436,437,3,44,
  	22,0,437,438,3,44,22,0,438,439,3,44,22,0,439,440,3,44,22,0,440,441,3,
  	44,22,0,441,442,3,44,22,0,442,443,3,44,22,0,443,444,3,44,22,0,444,445,
  	3,44,22,0,445,446,3,44,22,0,446,447,3,44,22,0,447,448,3,44,22,0,448,449,
  	3,44,22,0,449,450,3,44,22,0,450,451,3,44,22,0,451,452,3,44,22,0,452,453,
  	3,44,22,0,453,454,3,44,22,0,454,455,3,44,22,0,455,456,3,44,22,0,456,457,
  	3,44,22,0,457,458,3,44,22,0,458,459,3,44,22,0,459,460,5,7,0,0,460,461,
  	5,7,0,0,461,462,5,7,0,0,462,463,5,7,0,0,463,464,5,7,0,0,464,465,5,7,0,
  	0,465,466,5,7,0,0,466,467,5,7,0,0,467,468,3,44,22,0,468,469,3,44,22,0,
  	469,470,3,44,22,0,470,471,3,44,22,0,471,473,5,7,0,0,472,474,5,12,0,0,
  	473,472,1,0,0,0,473,474,1,0,0,0,474,475,1,0,0,0,475,476,5,7,0,0,476,478,
  	5,7,0,0,477,479,5,7,0,0,478,477,1,0,0,0,478,479,1,0,0,0,479,480,1,0,0,
  	0,480,481,7,1,0,0,481,15,1,0,0,0,482,483,5,1,0,0,483,484,5,22,0,0,484,
  	485,5,25,0,0,485,487,5,30,0,0,486,488,3,18,9,0,487,486,1,0,0,0,488,489,
  	1,0,0,0,489,487,1,0,0,0,489,490,1,0,0,0,490,17,1,0,0,0,491,492,5,1,0,
  	0,492,493,7,0,0,0,493,494,5,25,0,0,494,495,5,26,0,0,495,496,5,26,0,0,
  	496,497,5,26,0,0,497,498,7,2,0,0,498,499,5,26,0,0,499,500,5,30,0,0,500,
  	19,1,0,0,0,501,503,5,3,0,0,502,504,5,92,0,0,503,502,1,0,0,0,504,505,1,
  	0,0,0,505,503,1,0,0,0,505,506,1,0,0,0,506,507,1,0,0,0,507,508,5,94,0,
  	0,508,509,5,2,0,0,509,510,5,74,0,0,510,511,5,77,0,0,511,512,5,78,0,0,
  	512,516,5,81,0,0,513,517,5,82,0,0,514,515,5,83,0,0,515,517,5,84,0,0,516,
  	513,1,0,0,0,516,514,1,0,0,0,516,517,1,0,0,0,517,518,1,0,0,0,518,520,5,
  	90,0,0,519,521,3,22,11,0,520,519,1,0,0,0,521,522,1,0,0,0,522,520,1,0,
  	0,0,522,523,1,0,0,0,523,21,1,0,0,0,524,525,5,7,0,0,525,526,3,44,22,0,
  	526,528,3,44,22,0,527,529,3,44,22,0,528,527,1,0,0,0,529,530,1,0,0,0,530,
  	528,1,0,0,0,530,531,1,0,0,0,531,532,1,0,0,0,532,533,7,1,0,0,533,23,1,
  	0,0,0,534,536,5,3,0,0,535,537,5,92,0,0,536,535,1,0,0,0,537,538,1,0,0,
  	0,538,536,1,0,0,0,538,539,1,0,0,0,539,540,1,0,0,0,540,541,5,94,0,0,541,
  	542,5,2,0,0,542,544,5,74,0,0,543,545,5,75,0,0,544,543,1,0,0,0,544,545,
  	1,0,0,0,545,546,1,0,0,0,546,547,5,77,0,0,547,548,5,78,0,0,548,549,5,79,
  	0,0,549,553,5,81,0,0,550,554,5,82,0,0,551,552,5,83,0,0,552,554,5,84,0,
  	0,553,550,1,0,0,0,553,551,1,0,0,0,553,554,1,0,0,0,554,555,1,0,0,0,555,
  	557,5,90,0,0,556,558,3,26,13,0,557,556,1,0,0,0,558,559,1,0,0,0,559,557,
  	1,0,0,0,559,560,1,0,0,0,560,25,1,0,0,0,561,563,5,7,0,0,562,564,5,7,0,
  	0,563,562,1,0,0,0,563,564,1,0,0,0,564,565,1,0,0,0,565,566,3,44,22,0,566,
  	567,3,44,22,0,567,569,3,44,22,0,568,570,3,44,22,0,569,568,1,0,0,0,570,
  	571,1,0,0,0,571,569,1,0,0,0,571,572,1,0,0,0,572,573,1,0,0,0,573,574,7,
  	1,0,0,574,27,1,0,0,0,575,577,5,3,0,0,576,578,5,92,0,0,577,576,1,0,0,0,
  	578,579,1,0,0,0,579,577,1,0,0,0,579,580,1,0,0,0,580,581,1,0,0,0,581,582,
  	5,94,0,0,582,583,5,2,0,0,583,585,5,74,0,0,584,586,5,76,0,0,585,584,1,
  	0,0,0,585,586,1,0,0,0,586,588,1,0,0,0,587,589,5,75,0,0,588,587,1,0,0,
  	0,588,589,1,0,0,0,589,590,1,0,0,0,590,591,5,77,0,0,591,592,5,78,0,0,592,
  	593,5,79,0,0,593,594,5,80,0,0,594,598,5,81,0,0,595,599,5,82,0,0,596,597,
  	5,83,0,0,597,599,5,84,0,0,598,595,1,0,0,0,598,596,1,0,0,0,598,599,1,0,
  	0,0,599,600,1,0,0,0,600,602,5,90,0,0,601,603,3,30,15,0,602,601,1,0,0,
  	0,603,604,1,0,0,0,604,602,1,0,0,0,604,605,1,0,0,0,605,29,1,0,0,0,606,
  	608,5,7,0,0,607,609,5,7,0,0,608,607,1,0,0,0,608,609,1,0,0,0,609,611,1,
  	0,0,0,610,612,5,7,0,0,611,610,1,0,0,0,611,612,1,0,0,0,612,613,1,0,0,0,
  	613,614,3,44,22,0,614,615,3,44,22,0,615,616,3,44,22,0,616,618,3,44,22,
  	0,617,619,3,44,22,0,618,617,1,0,0,0,619,620,1,0,0,0,620,618,1,0,0,0,620,
  	621,1,0,0,0,621,622,1,0,0,0,622,623,7,1,0,0,623,31,1,0,0,0,624,626,3,
  	34,17,0,625,624,1,0,0,0,626,627,1,0,0,0,627,625,1,0,0,0,627,628,1,0,0,
  	0,628,33,1,0,0,0,629,630,5,6,0,0,630,631,5,111,0,0,631,632,5,105,0,0,
  	632,633,5,111,0,0,633,634,5,106,0,0,634,635,5,107,0,0,635,636,5,110,0,
  	0,636,643,5,106,0,0,637,644,5,113,0,0,638,639,5,103,0,0,639,640,5,111,
  	0,0,640,641,5,105,0,0,641,642,5,111,0,0,642,644,5,104,0,0,643,637,1,0,
  	0,0,643,638,1,0,0,0,644,645,1,0,0,0,645,646,5,109,0,0,646,647,5,112,0,
  	0,647,648,5,106,0,0,648,649,5,108,0,0,649,650,5,110,0,0,650,651,5,106,
  	0,0,651,652,5,102,0,0,652,653,7,3,0,0,653,35,1,0,0,0,654,656,3,38,19,
  	0,655,654,1,0,0,0,656,657,1,0,0,0,657,655,1,0,0,0,657,658,1,0,0,0,658,
  	37,1,0,0,0,659,660,5,6,0,0,660,661,5,111,0,0,661,662,5,105,0,0,662,663,
  	5,111,0,0,663,664,5,105,0,0,664,665,5,111,0,0,665,666,5,106,0,0,666,667,
  	5,107,0,0,667,668,5,110,0,0,668,677,5,106,0,0,669,678,5,113,0,0,670,671,
  	5,103,0,0,671,672,5,111,0,0,672,673,5,105,0,0,673,674,5,111,0,0,674,675,
  	5,105,0,0,675,676,5,111,0,0,676,678,5,104,0,0,677,669,1,0,0,0,677,670,
  	1,0,0,0,678,679,1,0,0,0,679,680,5,109,0,0,680,681,5,112,0,0,681,682,5,
  	106,0,0,682,683,5,108,0,0,683,684,5,110,0,0,684,685,5,106,0,0,685,686,
  	5,102,0,0,686,687,7,3,0,0,687,39,1,0,0,0,688,690,3,42,21,0,689,688,1,
  	0,0,0,690,691,1,0,0,0,691,689,1,0,0,0,691,692,1,0,0,0,692,41,1,0,0,0,
  	693,694,5,6,0,0,694,695,5,111,0,0,695,696,5,105,0,0,696,697,5,111,0,0,
  	697,698,5,105,0,0,698,699,5,111,0,0,699,700,5,105,0,0,700,701,5,111,0,
  	0,701,702,5,106,0,0,702,703,5,107,0,0,703,704,5,110,0,0,704,715,5,106,
  	0,0,705,716,5,113,0,0,706,707,5,103,0,0,707,708,5,111,0,0,708,709,5,105,
  	0,0,709,710,5,111,0,0,710,711,5,105,0,0,711,712,5,111,0,0,712,713,5,105,
  	0,0,713,714,5,111,0,0,714,716,5,104,0,0,715,705,1,0,0,0,715,706,1,0,0,
  	0,716,717,1,0,0,0,717,718,5,109,0,0,718,719,5,112,0,0,719,720,5,106,0,
  	0,720,721,5,108,0,0,721,722,5,110,0,0,722,723,5,106,0,0,723,724,5,102,
  	0,0,724,725,7,3,0,0,725,43,1,0,0,0,726,727,7,4,0,0,727,45,1,0,0,0,55,
  	47,61,63,101,106,133,138,144,149,154,179,184,220,225,260,265,271,276,
  	281,314,319,363,368,411,416,422,427,432,473,478,489,505,516,522,530,538,
  	544,553,559,563,571,579,585,588,598,604,608,611,620,627,643,657,677,691,
  	715
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  nmrpipepkparserParserStaticData = std::move(staticData);
}

}

NmrPipePKParser::NmrPipePKParser(TokenStream *input) : NmrPipePKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

NmrPipePKParser::NmrPipePKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  NmrPipePKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *nmrpipepkparserParserStaticData->atn, nmrpipepkparserParserStaticData->decisionToDFA, nmrpipepkparserParserStaticData->sharedContextCache, options);
}

NmrPipePKParser::~NmrPipePKParser() {
  delete _interpreter;
}

const atn::ATN& NmrPipePKParser::getATN() const {
  return *nmrpipepkparserParserStaticData->atn;
}

std::string NmrPipePKParser::getGrammarFileName() const {
  return "NmrPipePKParser.g4";
}

const std::vector<std::string>& NmrPipePKParser::getRuleNames() const {
  return nmrpipepkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& NmrPipePKParser::getVocabulary() const {
  return nmrpipepkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView NmrPipePKParser::getSerializedATN() const {
  return nmrpipepkparserParserStaticData->serializedATN;
}


//----------------- Nmrpipe_pkContext ------------------------------------------------------------------

NmrPipePKParser::Nmrpipe_pkContext::Nmrpipe_pkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Nmrpipe_pkContext::EOF() {
  return getToken(NmrPipePKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Nmrpipe_pkContext::RETURN() {
  return getTokens(NmrPipePKParser::RETURN);
}

tree::TerminalNode* NmrPipePKParser::Nmrpipe_pkContext::RETURN(size_t i) {
  return getToken(NmrPipePKParser::RETURN, i);
}

std::vector<NmrPipePKParser::Data_labelContext *> NmrPipePKParser::Nmrpipe_pkContext::data_label() {
  return getRuleContexts<NmrPipePKParser::Data_labelContext>();
}

NmrPipePKParser::Data_labelContext* NmrPipePKParser::Nmrpipe_pkContext::data_label(size_t i) {
  return getRuleContext<NmrPipePKParser::Data_labelContext>(i);
}

std::vector<NmrPipePKParser::Peak_list_2dContext *> NmrPipePKParser::Nmrpipe_pkContext::peak_list_2d() {
  return getRuleContexts<NmrPipePKParser::Peak_list_2dContext>();
}

NmrPipePKParser::Peak_list_2dContext* NmrPipePKParser::Nmrpipe_pkContext::peak_list_2d(size_t i) {
  return getRuleContext<NmrPipePKParser::Peak_list_2dContext>(i);
}

std::vector<NmrPipePKParser::Peak_list_3dContext *> NmrPipePKParser::Nmrpipe_pkContext::peak_list_3d() {
  return getRuleContexts<NmrPipePKParser::Peak_list_3dContext>();
}

NmrPipePKParser::Peak_list_3dContext* NmrPipePKParser::Nmrpipe_pkContext::peak_list_3d(size_t i) {
  return getRuleContext<NmrPipePKParser::Peak_list_3dContext>(i);
}

std::vector<NmrPipePKParser::Peak_list_4dContext *> NmrPipePKParser::Nmrpipe_pkContext::peak_list_4d() {
  return getRuleContexts<NmrPipePKParser::Peak_list_4dContext>();
}

NmrPipePKParser::Peak_list_4dContext* NmrPipePKParser::Nmrpipe_pkContext::peak_list_4d(size_t i) {
  return getRuleContext<NmrPipePKParser::Peak_list_4dContext>(i);
}

std::vector<NmrPipePKParser::Pipp_labelContext *> NmrPipePKParser::Nmrpipe_pkContext::pipp_label() {
  return getRuleContexts<NmrPipePKParser::Pipp_labelContext>();
}

NmrPipePKParser::Pipp_labelContext* NmrPipePKParser::Nmrpipe_pkContext::pipp_label(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_labelContext>(i);
}

std::vector<NmrPipePKParser::Pipp_peak_list_2dContext *> NmrPipePKParser::Nmrpipe_pkContext::pipp_peak_list_2d() {
  return getRuleContexts<NmrPipePKParser::Pipp_peak_list_2dContext>();
}

NmrPipePKParser::Pipp_peak_list_2dContext* NmrPipePKParser::Nmrpipe_pkContext::pipp_peak_list_2d(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_peak_list_2dContext>(i);
}

std::vector<NmrPipePKParser::Pipp_peak_list_3dContext *> NmrPipePKParser::Nmrpipe_pkContext::pipp_peak_list_3d() {
  return getRuleContexts<NmrPipePKParser::Pipp_peak_list_3dContext>();
}

NmrPipePKParser::Pipp_peak_list_3dContext* NmrPipePKParser::Nmrpipe_pkContext::pipp_peak_list_3d(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_peak_list_3dContext>(i);
}

std::vector<NmrPipePKParser::Pipp_peak_list_4dContext *> NmrPipePKParser::Nmrpipe_pkContext::pipp_peak_list_4d() {
  return getRuleContexts<NmrPipePKParser::Pipp_peak_list_4dContext>();
}

NmrPipePKParser::Pipp_peak_list_4dContext* NmrPipePKParser::Nmrpipe_pkContext::pipp_peak_list_4d(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_peak_list_4dContext>(i);
}

std::vector<NmrPipePKParser::Pipp_row_peak_list_2dContext *> NmrPipePKParser::Nmrpipe_pkContext::pipp_row_peak_list_2d() {
  return getRuleContexts<NmrPipePKParser::Pipp_row_peak_list_2dContext>();
}

NmrPipePKParser::Pipp_row_peak_list_2dContext* NmrPipePKParser::Nmrpipe_pkContext::pipp_row_peak_list_2d(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_row_peak_list_2dContext>(i);
}

std::vector<NmrPipePKParser::Pipp_row_peak_list_3dContext *> NmrPipePKParser::Nmrpipe_pkContext::pipp_row_peak_list_3d() {
  return getRuleContexts<NmrPipePKParser::Pipp_row_peak_list_3dContext>();
}

NmrPipePKParser::Pipp_row_peak_list_3dContext* NmrPipePKParser::Nmrpipe_pkContext::pipp_row_peak_list_3d(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_row_peak_list_3dContext>(i);
}

std::vector<NmrPipePKParser::Pipp_row_peak_list_4dContext *> NmrPipePKParser::Nmrpipe_pkContext::pipp_row_peak_list_4d() {
  return getRuleContexts<NmrPipePKParser::Pipp_row_peak_list_4dContext>();
}

NmrPipePKParser::Pipp_row_peak_list_4dContext* NmrPipePKParser::Nmrpipe_pkContext::pipp_row_peak_list_4d(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_row_peak_list_4dContext>(i);
}


size_t NmrPipePKParser::Nmrpipe_pkContext::getRuleIndex() const {
  return NmrPipePKParser::RuleNmrpipe_pk;
}


std::any NmrPipePKParser::Nmrpipe_pkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitNmrpipe_pk(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Nmrpipe_pkContext* NmrPipePKParser::nmrpipe_pk() {
  Nmrpipe_pkContext *_localctx = _tracker.createInstance<Nmrpipe_pkContext>(_ctx, getState());
  enterRule(_localctx, 0, NmrPipePKParser::RuleNmrpipe_pk);
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
    setState(47);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(46);
      match(NmrPipePKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(63);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 16462) != 0)) {
      setState(61);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(49);
        data_label();
        break;
      }

      case 2: {
        setState(50);
        peak_list_2d();
        break;
      }

      case 3: {
        setState(51);
        peak_list_3d();
        break;
      }

      case 4: {
        setState(52);
        peak_list_4d();
        break;
      }

      case 5: {
        setState(53);
        pipp_label();
        break;
      }

      case 6: {
        setState(54);
        pipp_peak_list_2d();
        break;
      }

      case 7: {
        setState(55);
        pipp_peak_list_3d();
        break;
      }

      case 8: {
        setState(56);
        pipp_peak_list_4d();
        break;
      }

      case 9: {
        setState(57);
        pipp_row_peak_list_2d();
        break;
      }

      case 10: {
        setState(58);
        pipp_row_peak_list_3d();
        break;
      }

      case 11: {
        setState(59);
        pipp_row_peak_list_4d();
        break;
      }

      case 12: {
        setState(60);
        match(NmrPipePKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(65);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(66);
    match(NmrPipePKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Data_labelContext ------------------------------------------------------------------

NmrPipePKParser::Data_labelContext::Data_labelContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Data_labelContext::Data() {
  return getToken(NmrPipePKParser::Data, 0);
}

tree::TerminalNode* NmrPipePKParser::Data_labelContext::Simple_name_DA() {
  return getToken(NmrPipePKParser::Simple_name_DA, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Data_labelContext::Integer_DA() {
  return getTokens(NmrPipePKParser::Integer_DA);
}

tree::TerminalNode* NmrPipePKParser::Data_labelContext::Integer_DA(size_t i) {
  return getToken(NmrPipePKParser::Integer_DA, i);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Data_labelContext::Ppm_value_DA() {
  return getTokens(NmrPipePKParser::Ppm_value_DA);
}

tree::TerminalNode* NmrPipePKParser::Data_labelContext::Ppm_value_DA(size_t i) {
  return getToken(NmrPipePKParser::Ppm_value_DA, i);
}

tree::TerminalNode* NmrPipePKParser::Data_labelContext::RETURN_DA() {
  return getToken(NmrPipePKParser::RETURN_DA, 0);
}

tree::TerminalNode* NmrPipePKParser::Data_labelContext::X_axis_DA() {
  return getToken(NmrPipePKParser::X_axis_DA, 0);
}

tree::TerminalNode* NmrPipePKParser::Data_labelContext::Y_axis_DA() {
  return getToken(NmrPipePKParser::Y_axis_DA, 0);
}

tree::TerminalNode* NmrPipePKParser::Data_labelContext::Z_axis_DA() {
  return getToken(NmrPipePKParser::Z_axis_DA, 0);
}

tree::TerminalNode* NmrPipePKParser::Data_labelContext::A_axis_DA() {
  return getToken(NmrPipePKParser::A_axis_DA, 0);
}


size_t NmrPipePKParser::Data_labelContext::getRuleIndex() const {
  return NmrPipePKParser::RuleData_label;
}


std::any NmrPipePKParser::Data_labelContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitData_label(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Data_labelContext* NmrPipePKParser::data_label() {
  Data_labelContext *_localctx = _tracker.createInstance<Data_labelContext>(_ctx, getState());
  enterRule(_localctx, 2, NmrPipePKParser::RuleData_label);
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
    setState(68);
    match(NmrPipePKParser::Data);
    setState(69);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1966080) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(70);
    match(NmrPipePKParser::Simple_name_DA);
    setState(71);
    match(NmrPipePKParser::Integer_DA);
    setState(72);
    match(NmrPipePKParser::Integer_DA);
    setState(73);
    match(NmrPipePKParser::Ppm_value_DA);
    setState(74);
    match(NmrPipePKParser::Ppm_value_DA);
    setState(75);
    match(NmrPipePKParser::RETURN_DA);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_list_2dContext ------------------------------------------------------------------

NmrPipePKParser::Peak_list_2dContext::Peak_list_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Vars() {
  return getToken(NmrPipePKParser::Vars, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Index() {
  return getToken(NmrPipePKParser::Index, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::X_axis() {
  return getToken(NmrPipePKParser::X_axis, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Y_axis() {
  return getToken(NmrPipePKParser::Y_axis, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Dx() {
  return getToken(NmrPipePKParser::Dx, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Dy() {
  return getToken(NmrPipePKParser::Dy, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::X_ppm() {
  return getToken(NmrPipePKParser::X_ppm, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Y_ppm() {
  return getToken(NmrPipePKParser::Y_ppm, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::X_hz() {
  return getToken(NmrPipePKParser::X_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Y_hz() {
  return getToken(NmrPipePKParser::Y_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Xw() {
  return getToken(NmrPipePKParser::Xw, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Yw() {
  return getToken(NmrPipePKParser::Yw, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Xw_hz() {
  return getToken(NmrPipePKParser::Xw_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Yw_hz() {
  return getToken(NmrPipePKParser::Yw_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::X1() {
  return getToken(NmrPipePKParser::X1, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::X3() {
  return getToken(NmrPipePKParser::X3, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Y1() {
  return getToken(NmrPipePKParser::Y1, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Y3() {
  return getToken(NmrPipePKParser::Y3, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Height() {
  return getToken(NmrPipePKParser::Height, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::DHeight() {
  return getToken(NmrPipePKParser::DHeight, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Vol() {
  return getToken(NmrPipePKParser::Vol, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Pchi2() {
  return getToken(NmrPipePKParser::Pchi2, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Type() {
  return getToken(NmrPipePKParser::Type, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::ClustId() {
  return getToken(NmrPipePKParser::ClustId, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Memcnt() {
  return getToken(NmrPipePKParser::Memcnt, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::RETURN_VA() {
  return getToken(NmrPipePKParser::RETURN_VA, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Format() {
  return getToken(NmrPipePKParser::Format, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Peak_list_2dContext::Format_code() {
  return getTokens(NmrPipePKParser::Format_code);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Format_code(size_t i) {
  return getToken(NmrPipePKParser::Format_code, i);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::RETURN_FO() {
  return getToken(NmrPipePKParser::RETURN_FO, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Ass() {
  return getToken(NmrPipePKParser::Ass, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Trouble() {
  return getToken(NmrPipePKParser::Trouble, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Null_value() {
  return getToken(NmrPipePKParser::Null_value, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Any_name_NV() {
  return getToken(NmrPipePKParser::Any_name_NV, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::RETURN_NV() {
  return getToken(NmrPipePKParser::RETURN_NV, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Null_string() {
  return getToken(NmrPipePKParser::Null_string, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::Any_name_NS() {
  return getToken(NmrPipePKParser::Any_name_NS, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_2dContext::RETURN_NS() {
  return getToken(NmrPipePKParser::RETURN_NS, 0);
}

std::vector<NmrPipePKParser::Peak_2dContext *> NmrPipePKParser::Peak_list_2dContext::peak_2d() {
  return getRuleContexts<NmrPipePKParser::Peak_2dContext>();
}

NmrPipePKParser::Peak_2dContext* NmrPipePKParser::Peak_list_2dContext::peak_2d(size_t i) {
  return getRuleContext<NmrPipePKParser::Peak_2dContext>(i);
}


size_t NmrPipePKParser::Peak_list_2dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePeak_list_2d;
}


std::any NmrPipePKParser::Peak_list_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Peak_list_2dContext* NmrPipePKParser::peak_list_2d() {
  Peak_list_2dContext *_localctx = _tracker.createInstance<Peak_list_2dContext>(_ctx, getState());
  enterRule(_localctx, 4, NmrPipePKParser::RulePeak_list_2d);
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
    setState(77);
    match(NmrPipePKParser::Vars);
    setState(78);
    match(NmrPipePKParser::Index);
    setState(79);
    match(NmrPipePKParser::X_axis);
    setState(80);
    match(NmrPipePKParser::Y_axis);
    setState(81);
    match(NmrPipePKParser::Dx);
    setState(82);
    match(NmrPipePKParser::Dy);
    setState(83);
    match(NmrPipePKParser::X_ppm);
    setState(84);
    match(NmrPipePKParser::Y_ppm);
    setState(85);
    match(NmrPipePKParser::X_hz);
    setState(86);
    match(NmrPipePKParser::Y_hz);
    setState(87);
    match(NmrPipePKParser::Xw);
    setState(88);
    match(NmrPipePKParser::Yw);
    setState(89);
    match(NmrPipePKParser::Xw_hz);
    setState(90);
    match(NmrPipePKParser::Yw_hz);
    setState(91);
    match(NmrPipePKParser::X1);
    setState(92);
    match(NmrPipePKParser::X3);
    setState(93);
    match(NmrPipePKParser::Y1);
    setState(94);
    match(NmrPipePKParser::Y3);
    setState(95);
    match(NmrPipePKParser::Height);
    setState(96);
    match(NmrPipePKParser::DHeight);
    setState(97);
    match(NmrPipePKParser::Vol);
    setState(98);
    match(NmrPipePKParser::Pchi2);
    setState(99);
    match(NmrPipePKParser::Type);
    setState(101);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Ass) {
      setState(100);
      match(NmrPipePKParser::Ass);
    }
    setState(103);
    match(NmrPipePKParser::ClustId);
    setState(104);
    match(NmrPipePKParser::Memcnt);
    setState(106);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Trouble) {
      setState(105);
      match(NmrPipePKParser::Trouble);
    }
    setState(108);
    match(NmrPipePKParser::RETURN_VA);
    setState(109);
    match(NmrPipePKParser::Format);
    setState(110);
    match(NmrPipePKParser::Format_code);
    setState(111);
    match(NmrPipePKParser::Format_code);
    setState(112);
    match(NmrPipePKParser::Format_code);
    setState(113);
    match(NmrPipePKParser::Format_code);
    setState(114);
    match(NmrPipePKParser::Format_code);
    setState(115);
    match(NmrPipePKParser::Format_code);
    setState(116);
    match(NmrPipePKParser::Format_code);
    setState(117);
    match(NmrPipePKParser::Format_code);
    setState(118);
    match(NmrPipePKParser::Format_code);
    setState(119);
    match(NmrPipePKParser::Format_code);
    setState(120);
    match(NmrPipePKParser::Format_code);
    setState(121);
    match(NmrPipePKParser::Format_code);
    setState(122);
    match(NmrPipePKParser::Format_code);
    setState(123);
    match(NmrPipePKParser::Format_code);
    setState(124);
    match(NmrPipePKParser::Format_code);
    setState(125);
    match(NmrPipePKParser::Format_code);
    setState(126);
    match(NmrPipePKParser::Format_code);
    setState(127);
    match(NmrPipePKParser::Format_code);
    setState(128);
    match(NmrPipePKParser::Format_code);
    setState(129);
    match(NmrPipePKParser::Format_code);
    setState(130);
    match(NmrPipePKParser::Format_code);
    setState(131);
    match(NmrPipePKParser::Format_code);
    setState(133);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx)) {
    case 1: {
      setState(132);
      match(NmrPipePKParser::Format_code);
      break;
    }

    default:
      break;
    }
    setState(135);
    match(NmrPipePKParser::Format_code);
    setState(136);
    match(NmrPipePKParser::Format_code);
    setState(138);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Format_code) {
      setState(137);
      match(NmrPipePKParser::Format_code);
    }
    setState(140);
    match(NmrPipePKParser::RETURN_FO);
    setState(144);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Null_value) {
      setState(141);
      match(NmrPipePKParser::Null_value);
      setState(142);
      match(NmrPipePKParser::Any_name_NV);
      setState(143);
      match(NmrPipePKParser::RETURN_NV);
    }
    setState(149);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Null_string) {
      setState(146);
      match(NmrPipePKParser::Null_string);
      setState(147);
      match(NmrPipePKParser::Any_name_NS);
      setState(148);
      match(NmrPipePKParser::RETURN_NS);
    }
    setState(152); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(151);
      peak_2d();
      setState(154); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrPipePKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_2dContext ------------------------------------------------------------------

NmrPipePKParser::Peak_2dContext::Peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Peak_2dContext::Integer() {
  return getTokens(NmrPipePKParser::Integer);
}

tree::TerminalNode* NmrPipePKParser::Peak_2dContext::Integer(size_t i) {
  return getToken(NmrPipePKParser::Integer, i);
}

std::vector<NmrPipePKParser::NumberContext *> NmrPipePKParser::Peak_2dContext::number() {
  return getRuleContexts<NmrPipePKParser::NumberContext>();
}

NmrPipePKParser::NumberContext* NmrPipePKParser::Peak_2dContext::number(size_t i) {
  return getRuleContext<NmrPipePKParser::NumberContext>(i);
}

tree::TerminalNode* NmrPipePKParser::Peak_2dContext::RETURN() {
  return getToken(NmrPipePKParser::RETURN, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_2dContext::EOF() {
  return getToken(NmrPipePKParser::EOF, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_2dContext::Any_name() {
  return getToken(NmrPipePKParser::Any_name, 0);
}


size_t NmrPipePKParser::Peak_2dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePeak_2d;
}


std::any NmrPipePKParser::Peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Peak_2dContext* NmrPipePKParser::peak_2d() {
  Peak_2dContext *_localctx = _tracker.createInstance<Peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 6, NmrPipePKParser::RulePeak_2d);
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
    setState(156);
    match(NmrPipePKParser::Integer);
    setState(157);
    number();
    setState(158);
    number();
    setState(159);
    number();
    setState(160);
    number();
    setState(161);
    number();
    setState(162);
    number();
    setState(163);
    number();
    setState(164);
    number();
    setState(165);
    number();
    setState(166);
    number();
    setState(167);
    number();
    setState(168);
    number();
    setState(169);
    match(NmrPipePKParser::Integer);
    setState(170);
    match(NmrPipePKParser::Integer);
    setState(171);
    match(NmrPipePKParser::Integer);
    setState(172);
    match(NmrPipePKParser::Integer);
    setState(173);
    number();
    setState(174);
    number();
    setState(175);
    number();
    setState(176);
    number();
    setState(177);
    match(NmrPipePKParser::Integer);
    setState(179);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Any_name) {
      setState(178);
      match(NmrPipePKParser::Any_name);
    }
    setState(181);
    match(NmrPipePKParser::Integer);
    setState(182);
    match(NmrPipePKParser::Integer);
    setState(184);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Integer) {
      setState(183);
      match(NmrPipePKParser::Integer);
    }
    setState(186);
    _la = _input->LA(1);
    if (!(_la == NmrPipePKParser::EOF

    || _la == NmrPipePKParser::RETURN)) {
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

//----------------- Peak_list_3dContext ------------------------------------------------------------------

NmrPipePKParser::Peak_list_3dContext::Peak_list_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Vars() {
  return getToken(NmrPipePKParser::Vars, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Index() {
  return getToken(NmrPipePKParser::Index, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::X_axis() {
  return getToken(NmrPipePKParser::X_axis, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Y_axis() {
  return getToken(NmrPipePKParser::Y_axis, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Z_axis() {
  return getToken(NmrPipePKParser::Z_axis, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Dx() {
  return getToken(NmrPipePKParser::Dx, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Dy() {
  return getToken(NmrPipePKParser::Dy, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Dz() {
  return getToken(NmrPipePKParser::Dz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::X_ppm() {
  return getToken(NmrPipePKParser::X_ppm, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Y_ppm() {
  return getToken(NmrPipePKParser::Y_ppm, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Z_ppm() {
  return getToken(NmrPipePKParser::Z_ppm, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::X_hz() {
  return getToken(NmrPipePKParser::X_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Y_hz() {
  return getToken(NmrPipePKParser::Y_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Z_hz() {
  return getToken(NmrPipePKParser::Z_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Xw() {
  return getToken(NmrPipePKParser::Xw, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Yw() {
  return getToken(NmrPipePKParser::Yw, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Zw() {
  return getToken(NmrPipePKParser::Zw, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Xw_hz() {
  return getToken(NmrPipePKParser::Xw_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Yw_hz() {
  return getToken(NmrPipePKParser::Yw_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Zw_hz() {
  return getToken(NmrPipePKParser::Zw_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::X1() {
  return getToken(NmrPipePKParser::X1, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::X3() {
  return getToken(NmrPipePKParser::X3, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Y1() {
  return getToken(NmrPipePKParser::Y1, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Y3() {
  return getToken(NmrPipePKParser::Y3, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Z1() {
  return getToken(NmrPipePKParser::Z1, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Z3() {
  return getToken(NmrPipePKParser::Z3, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Height() {
  return getToken(NmrPipePKParser::Height, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::DHeight() {
  return getToken(NmrPipePKParser::DHeight, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Vol() {
  return getToken(NmrPipePKParser::Vol, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Pchi2() {
  return getToken(NmrPipePKParser::Pchi2, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Type() {
  return getToken(NmrPipePKParser::Type, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::ClustId() {
  return getToken(NmrPipePKParser::ClustId, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Memcnt() {
  return getToken(NmrPipePKParser::Memcnt, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::RETURN_VA() {
  return getToken(NmrPipePKParser::RETURN_VA, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Format() {
  return getToken(NmrPipePKParser::Format, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Peak_list_3dContext::Format_code() {
  return getTokens(NmrPipePKParser::Format_code);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Format_code(size_t i) {
  return getToken(NmrPipePKParser::Format_code, i);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::RETURN_FO() {
  return getToken(NmrPipePKParser::RETURN_FO, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Ass() {
  return getToken(NmrPipePKParser::Ass, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Trouble() {
  return getToken(NmrPipePKParser::Trouble, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Null_value() {
  return getToken(NmrPipePKParser::Null_value, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Any_name_NV() {
  return getToken(NmrPipePKParser::Any_name_NV, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::RETURN_NV() {
  return getToken(NmrPipePKParser::RETURN_NV, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Null_string() {
  return getToken(NmrPipePKParser::Null_string, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::Any_name_NS() {
  return getToken(NmrPipePKParser::Any_name_NS, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_3dContext::RETURN_NS() {
  return getToken(NmrPipePKParser::RETURN_NS, 0);
}

std::vector<NmrPipePKParser::Peak_3dContext *> NmrPipePKParser::Peak_list_3dContext::peak_3d() {
  return getRuleContexts<NmrPipePKParser::Peak_3dContext>();
}

NmrPipePKParser::Peak_3dContext* NmrPipePKParser::Peak_list_3dContext::peak_3d(size_t i) {
  return getRuleContext<NmrPipePKParser::Peak_3dContext>(i);
}


size_t NmrPipePKParser::Peak_list_3dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePeak_list_3d;
}


std::any NmrPipePKParser::Peak_list_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Peak_list_3dContext* NmrPipePKParser::peak_list_3d() {
  Peak_list_3dContext *_localctx = _tracker.createInstance<Peak_list_3dContext>(_ctx, getState());
  enterRule(_localctx, 8, NmrPipePKParser::RulePeak_list_3d);
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
    setState(188);
    match(NmrPipePKParser::Vars);
    setState(189);
    match(NmrPipePKParser::Index);
    setState(190);
    match(NmrPipePKParser::X_axis);
    setState(191);
    match(NmrPipePKParser::Y_axis);
    setState(192);
    match(NmrPipePKParser::Z_axis);
    setState(193);
    match(NmrPipePKParser::Dx);
    setState(194);
    match(NmrPipePKParser::Dy);
    setState(195);
    match(NmrPipePKParser::Dz);
    setState(196);
    match(NmrPipePKParser::X_ppm);
    setState(197);
    match(NmrPipePKParser::Y_ppm);
    setState(198);
    match(NmrPipePKParser::Z_ppm);
    setState(199);
    match(NmrPipePKParser::X_hz);
    setState(200);
    match(NmrPipePKParser::Y_hz);
    setState(201);
    match(NmrPipePKParser::Z_hz);
    setState(202);
    match(NmrPipePKParser::Xw);
    setState(203);
    match(NmrPipePKParser::Yw);
    setState(204);
    match(NmrPipePKParser::Zw);
    setState(205);
    match(NmrPipePKParser::Xw_hz);
    setState(206);
    match(NmrPipePKParser::Yw_hz);
    setState(207);
    match(NmrPipePKParser::Zw_hz);
    setState(208);
    match(NmrPipePKParser::X1);
    setState(209);
    match(NmrPipePKParser::X3);
    setState(210);
    match(NmrPipePKParser::Y1);
    setState(211);
    match(NmrPipePKParser::Y3);
    setState(212);
    match(NmrPipePKParser::Z1);
    setState(213);
    match(NmrPipePKParser::Z3);
    setState(214);
    match(NmrPipePKParser::Height);
    setState(215);
    match(NmrPipePKParser::DHeight);
    setState(216);
    match(NmrPipePKParser::Vol);
    setState(217);
    match(NmrPipePKParser::Pchi2);
    setState(218);
    match(NmrPipePKParser::Type);
    setState(220);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Ass) {
      setState(219);
      match(NmrPipePKParser::Ass);
    }
    setState(222);
    match(NmrPipePKParser::ClustId);
    setState(223);
    match(NmrPipePKParser::Memcnt);
    setState(225);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Trouble) {
      setState(224);
      match(NmrPipePKParser::Trouble);
    }
    setState(227);
    match(NmrPipePKParser::RETURN_VA);
    setState(228);
    match(NmrPipePKParser::Format);
    setState(229);
    match(NmrPipePKParser::Format_code);
    setState(230);
    match(NmrPipePKParser::Format_code);
    setState(231);
    match(NmrPipePKParser::Format_code);
    setState(232);
    match(NmrPipePKParser::Format_code);
    setState(233);
    match(NmrPipePKParser::Format_code);
    setState(234);
    match(NmrPipePKParser::Format_code);
    setState(235);
    match(NmrPipePKParser::Format_code);
    setState(236);
    match(NmrPipePKParser::Format_code);
    setState(237);
    match(NmrPipePKParser::Format_code);
    setState(238);
    match(NmrPipePKParser::Format_code);
    setState(239);
    match(NmrPipePKParser::Format_code);
    setState(240);
    match(NmrPipePKParser::Format_code);
    setState(241);
    match(NmrPipePKParser::Format_code);
    setState(242);
    match(NmrPipePKParser::Format_code);
    setState(243);
    match(NmrPipePKParser::Format_code);
    setState(244);
    match(NmrPipePKParser::Format_code);
    setState(245);
    match(NmrPipePKParser::Format_code);
    setState(246);
    match(NmrPipePKParser::Format_code);
    setState(247);
    match(NmrPipePKParser::Format_code);
    setState(248);
    match(NmrPipePKParser::Format_code);
    setState(249);
    match(NmrPipePKParser::Format_code);
    setState(250);
    match(NmrPipePKParser::Format_code);
    setState(251);
    match(NmrPipePKParser::Format_code);
    setState(252);
    match(NmrPipePKParser::Format_code);
    setState(253);
    match(NmrPipePKParser::Format_code);
    setState(254);
    match(NmrPipePKParser::Format_code);
    setState(255);
    match(NmrPipePKParser::Format_code);
    setState(256);
    match(NmrPipePKParser::Format_code);
    setState(257);
    match(NmrPipePKParser::Format_code);
    setState(258);
    match(NmrPipePKParser::Format_code);
    setState(260);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx)) {
    case 1: {
      setState(259);
      match(NmrPipePKParser::Format_code);
      break;
    }

    default:
      break;
    }
    setState(262);
    match(NmrPipePKParser::Format_code);
    setState(263);
    match(NmrPipePKParser::Format_code);
    setState(265);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Format_code) {
      setState(264);
      match(NmrPipePKParser::Format_code);
    }
    setState(267);
    match(NmrPipePKParser::RETURN_FO);
    setState(271);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Null_value) {
      setState(268);
      match(NmrPipePKParser::Null_value);
      setState(269);
      match(NmrPipePKParser::Any_name_NV);
      setState(270);
      match(NmrPipePKParser::RETURN_NV);
    }
    setState(276);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Null_string) {
      setState(273);
      match(NmrPipePKParser::Null_string);
      setState(274);
      match(NmrPipePKParser::Any_name_NS);
      setState(275);
      match(NmrPipePKParser::RETURN_NS);
    }
    setState(279); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(278);
      peak_3d();
      setState(281); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrPipePKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_3dContext ------------------------------------------------------------------

NmrPipePKParser::Peak_3dContext::Peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Peak_3dContext::Integer() {
  return getTokens(NmrPipePKParser::Integer);
}

tree::TerminalNode* NmrPipePKParser::Peak_3dContext::Integer(size_t i) {
  return getToken(NmrPipePKParser::Integer, i);
}

std::vector<NmrPipePKParser::NumberContext *> NmrPipePKParser::Peak_3dContext::number() {
  return getRuleContexts<NmrPipePKParser::NumberContext>();
}

NmrPipePKParser::NumberContext* NmrPipePKParser::Peak_3dContext::number(size_t i) {
  return getRuleContext<NmrPipePKParser::NumberContext>(i);
}

tree::TerminalNode* NmrPipePKParser::Peak_3dContext::RETURN() {
  return getToken(NmrPipePKParser::RETURN, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_3dContext::EOF() {
  return getToken(NmrPipePKParser::EOF, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_3dContext::Any_name() {
  return getToken(NmrPipePKParser::Any_name, 0);
}


size_t NmrPipePKParser::Peak_3dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePeak_3d;
}


std::any NmrPipePKParser::Peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Peak_3dContext* NmrPipePKParser::peak_3d() {
  Peak_3dContext *_localctx = _tracker.createInstance<Peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 10, NmrPipePKParser::RulePeak_3d);
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
    setState(283);
    match(NmrPipePKParser::Integer);
    setState(284);
    number();
    setState(285);
    number();
    setState(286);
    number();
    setState(287);
    number();
    setState(288);
    number();
    setState(289);
    number();
    setState(290);
    number();
    setState(291);
    number();
    setState(292);
    number();
    setState(293);
    number();
    setState(294);
    number();
    setState(295);
    number();
    setState(296);
    number();
    setState(297);
    number();
    setState(298);
    number();
    setState(299);
    number();
    setState(300);
    number();
    setState(301);
    number();
    setState(302);
    match(NmrPipePKParser::Integer);
    setState(303);
    match(NmrPipePKParser::Integer);
    setState(304);
    match(NmrPipePKParser::Integer);
    setState(305);
    match(NmrPipePKParser::Integer);
    setState(306);
    match(NmrPipePKParser::Integer);
    setState(307);
    match(NmrPipePKParser::Integer);
    setState(308);
    number();
    setState(309);
    number();
    setState(310);
    number();
    setState(311);
    number();
    setState(312);
    match(NmrPipePKParser::Integer);
    setState(314);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Any_name) {
      setState(313);
      match(NmrPipePKParser::Any_name);
    }
    setState(316);
    match(NmrPipePKParser::Integer);
    setState(317);
    match(NmrPipePKParser::Integer);
    setState(319);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Integer) {
      setState(318);
      match(NmrPipePKParser::Integer);
    }
    setState(321);
    _la = _input->LA(1);
    if (!(_la == NmrPipePKParser::EOF

    || _la == NmrPipePKParser::RETURN)) {
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

//----------------- Peak_list_4dContext ------------------------------------------------------------------

NmrPipePKParser::Peak_list_4dContext::Peak_list_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Vars() {
  return getToken(NmrPipePKParser::Vars, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Index() {
  return getToken(NmrPipePKParser::Index, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::X_axis() {
  return getToken(NmrPipePKParser::X_axis, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Y_axis() {
  return getToken(NmrPipePKParser::Y_axis, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Z_axis() {
  return getToken(NmrPipePKParser::Z_axis, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::A_axis() {
  return getToken(NmrPipePKParser::A_axis, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Dx() {
  return getToken(NmrPipePKParser::Dx, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Dy() {
  return getToken(NmrPipePKParser::Dy, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Peak_list_4dContext::Dz() {
  return getTokens(NmrPipePKParser::Dz);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Dz(size_t i) {
  return getToken(NmrPipePKParser::Dz, i);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::X_ppm() {
  return getToken(NmrPipePKParser::X_ppm, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Y_ppm() {
  return getToken(NmrPipePKParser::Y_ppm, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Z_ppm() {
  return getToken(NmrPipePKParser::Z_ppm, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::A_ppm() {
  return getToken(NmrPipePKParser::A_ppm, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::X_hz() {
  return getToken(NmrPipePKParser::X_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Y_hz() {
  return getToken(NmrPipePKParser::Y_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Z_hz() {
  return getToken(NmrPipePKParser::Z_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::A_hz() {
  return getToken(NmrPipePKParser::A_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Xw() {
  return getToken(NmrPipePKParser::Xw, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Yw() {
  return getToken(NmrPipePKParser::Yw, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Zw() {
  return getToken(NmrPipePKParser::Zw, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Aw() {
  return getToken(NmrPipePKParser::Aw, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Xw_hz() {
  return getToken(NmrPipePKParser::Xw_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Yw_hz() {
  return getToken(NmrPipePKParser::Yw_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Zw_hz() {
  return getToken(NmrPipePKParser::Zw_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Aw_hz() {
  return getToken(NmrPipePKParser::Aw_hz, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::X1() {
  return getToken(NmrPipePKParser::X1, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::X3() {
  return getToken(NmrPipePKParser::X3, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Y1() {
  return getToken(NmrPipePKParser::Y1, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Y3() {
  return getToken(NmrPipePKParser::Y3, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Z1() {
  return getToken(NmrPipePKParser::Z1, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Z3() {
  return getToken(NmrPipePKParser::Z3, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::A1() {
  return getToken(NmrPipePKParser::A1, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::A3() {
  return getToken(NmrPipePKParser::A3, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Height() {
  return getToken(NmrPipePKParser::Height, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::DHeight() {
  return getToken(NmrPipePKParser::DHeight, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Vol() {
  return getToken(NmrPipePKParser::Vol, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Pchi2() {
  return getToken(NmrPipePKParser::Pchi2, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Type() {
  return getToken(NmrPipePKParser::Type, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::ClustId() {
  return getToken(NmrPipePKParser::ClustId, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Memcnt() {
  return getToken(NmrPipePKParser::Memcnt, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::RETURN_VA() {
  return getToken(NmrPipePKParser::RETURN_VA, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Format() {
  return getToken(NmrPipePKParser::Format, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Peak_list_4dContext::Format_code() {
  return getTokens(NmrPipePKParser::Format_code);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Format_code(size_t i) {
  return getToken(NmrPipePKParser::Format_code, i);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::RETURN_FO() {
  return getToken(NmrPipePKParser::RETURN_FO, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Ass() {
  return getToken(NmrPipePKParser::Ass, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Trouble() {
  return getToken(NmrPipePKParser::Trouble, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Null_value() {
  return getToken(NmrPipePKParser::Null_value, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Any_name_NV() {
  return getToken(NmrPipePKParser::Any_name_NV, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::RETURN_NV() {
  return getToken(NmrPipePKParser::RETURN_NV, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Null_string() {
  return getToken(NmrPipePKParser::Null_string, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::Any_name_NS() {
  return getToken(NmrPipePKParser::Any_name_NS, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_list_4dContext::RETURN_NS() {
  return getToken(NmrPipePKParser::RETURN_NS, 0);
}

std::vector<NmrPipePKParser::Peak_4dContext *> NmrPipePKParser::Peak_list_4dContext::peak_4d() {
  return getRuleContexts<NmrPipePKParser::Peak_4dContext>();
}

NmrPipePKParser::Peak_4dContext* NmrPipePKParser::Peak_list_4dContext::peak_4d(size_t i) {
  return getRuleContext<NmrPipePKParser::Peak_4dContext>(i);
}


size_t NmrPipePKParser::Peak_list_4dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePeak_list_4d;
}


std::any NmrPipePKParser::Peak_list_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Peak_list_4dContext* NmrPipePKParser::peak_list_4d() {
  Peak_list_4dContext *_localctx = _tracker.createInstance<Peak_list_4dContext>(_ctx, getState());
  enterRule(_localctx, 12, NmrPipePKParser::RulePeak_list_4d);
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
    setState(323);
    match(NmrPipePKParser::Vars);
    setState(324);
    match(NmrPipePKParser::Index);
    setState(325);
    match(NmrPipePKParser::X_axis);
    setState(326);
    match(NmrPipePKParser::Y_axis);
    setState(327);
    match(NmrPipePKParser::Z_axis);
    setState(328);
    match(NmrPipePKParser::A_axis);
    setState(329);
    match(NmrPipePKParser::Dx);
    setState(330);
    match(NmrPipePKParser::Dy);
    setState(331);
    match(NmrPipePKParser::Dz);
    setState(332);
    match(NmrPipePKParser::Dz);
    setState(333);
    match(NmrPipePKParser::X_ppm);
    setState(334);
    match(NmrPipePKParser::Y_ppm);
    setState(335);
    match(NmrPipePKParser::Z_ppm);
    setState(336);
    match(NmrPipePKParser::A_ppm);
    setState(337);
    match(NmrPipePKParser::X_hz);
    setState(338);
    match(NmrPipePKParser::Y_hz);
    setState(339);
    match(NmrPipePKParser::Z_hz);
    setState(340);
    match(NmrPipePKParser::A_hz);
    setState(341);
    match(NmrPipePKParser::Xw);
    setState(342);
    match(NmrPipePKParser::Yw);
    setState(343);
    match(NmrPipePKParser::Zw);
    setState(344);
    match(NmrPipePKParser::Aw);
    setState(345);
    match(NmrPipePKParser::Xw_hz);
    setState(346);
    match(NmrPipePKParser::Yw_hz);
    setState(347);
    match(NmrPipePKParser::Zw_hz);
    setState(348);
    match(NmrPipePKParser::Aw_hz);
    setState(349);
    match(NmrPipePKParser::X1);
    setState(350);
    match(NmrPipePKParser::X3);
    setState(351);
    match(NmrPipePKParser::Y1);
    setState(352);
    match(NmrPipePKParser::Y3);
    setState(353);
    match(NmrPipePKParser::Z1);
    setState(354);
    match(NmrPipePKParser::Z3);
    setState(355);
    match(NmrPipePKParser::A1);
    setState(356);
    match(NmrPipePKParser::A3);
    setState(357);
    match(NmrPipePKParser::Height);
    setState(358);
    match(NmrPipePKParser::DHeight);
    setState(359);
    match(NmrPipePKParser::Vol);
    setState(360);
    match(NmrPipePKParser::Pchi2);
    setState(361);
    match(NmrPipePKParser::Type);
    setState(363);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Ass) {
      setState(362);
      match(NmrPipePKParser::Ass);
    }
    setState(365);
    match(NmrPipePKParser::ClustId);
    setState(366);
    match(NmrPipePKParser::Memcnt);
    setState(368);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Trouble) {
      setState(367);
      match(NmrPipePKParser::Trouble);
    }
    setState(370);
    match(NmrPipePKParser::RETURN_VA);
    setState(371);
    match(NmrPipePKParser::Format);
    setState(372);
    match(NmrPipePKParser::Format_code);
    setState(373);
    match(NmrPipePKParser::Format_code);
    setState(374);
    match(NmrPipePKParser::Format_code);
    setState(375);
    match(NmrPipePKParser::Format_code);
    setState(376);
    match(NmrPipePKParser::Format_code);
    setState(377);
    match(NmrPipePKParser::Format_code);
    setState(378);
    match(NmrPipePKParser::Format_code);
    setState(379);
    match(NmrPipePKParser::Format_code);
    setState(380);
    match(NmrPipePKParser::Format_code);
    setState(381);
    match(NmrPipePKParser::Format_code);
    setState(382);
    match(NmrPipePKParser::Format_code);
    setState(383);
    match(NmrPipePKParser::Format_code);
    setState(384);
    match(NmrPipePKParser::Format_code);
    setState(385);
    match(NmrPipePKParser::Format_code);
    setState(386);
    match(NmrPipePKParser::Format_code);
    setState(387);
    match(NmrPipePKParser::Format_code);
    setState(388);
    match(NmrPipePKParser::Format_code);
    setState(389);
    match(NmrPipePKParser::Format_code);
    setState(390);
    match(NmrPipePKParser::Format_code);
    setState(391);
    match(NmrPipePKParser::Format_code);
    setState(392);
    match(NmrPipePKParser::Format_code);
    setState(393);
    match(NmrPipePKParser::Format_code);
    setState(394);
    match(NmrPipePKParser::Format_code);
    setState(395);
    match(NmrPipePKParser::Format_code);
    setState(396);
    match(NmrPipePKParser::Format_code);
    setState(397);
    match(NmrPipePKParser::Format_code);
    setState(398);
    match(NmrPipePKParser::Format_code);
    setState(399);
    match(NmrPipePKParser::Format_code);
    setState(400);
    match(NmrPipePKParser::Format_code);
    setState(401);
    match(NmrPipePKParser::Format_code);
    setState(402);
    match(NmrPipePKParser::Format_code);
    setState(403);
    match(NmrPipePKParser::Format_code);
    setState(404);
    match(NmrPipePKParser::Format_code);
    setState(405);
    match(NmrPipePKParser::Format_code);
    setState(406);
    match(NmrPipePKParser::Format_code);
    setState(407);
    match(NmrPipePKParser::Format_code);
    setState(408);
    match(NmrPipePKParser::Format_code);
    setState(409);
    match(NmrPipePKParser::Format_code);
    setState(411);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx)) {
    case 1: {
      setState(410);
      match(NmrPipePKParser::Format_code);
      break;
    }

    default:
      break;
    }
    setState(413);
    match(NmrPipePKParser::Format_code);
    setState(414);
    match(NmrPipePKParser::Format_code);
    setState(416);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Format_code) {
      setState(415);
      match(NmrPipePKParser::Format_code);
    }
    setState(418);
    match(NmrPipePKParser::RETURN_FO);
    setState(422);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Null_value) {
      setState(419);
      match(NmrPipePKParser::Null_value);
      setState(420);
      match(NmrPipePKParser::Any_name_NV);
      setState(421);
      match(NmrPipePKParser::RETURN_NV);
    }
    setState(427);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Null_string) {
      setState(424);
      match(NmrPipePKParser::Null_string);
      setState(425);
      match(NmrPipePKParser::Any_name_NS);
      setState(426);
      match(NmrPipePKParser::RETURN_NS);
    }
    setState(430); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(429);
      peak_4d();
      setState(432); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrPipePKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_4dContext ------------------------------------------------------------------

NmrPipePKParser::Peak_4dContext::Peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Peak_4dContext::Integer() {
  return getTokens(NmrPipePKParser::Integer);
}

tree::TerminalNode* NmrPipePKParser::Peak_4dContext::Integer(size_t i) {
  return getToken(NmrPipePKParser::Integer, i);
}

std::vector<NmrPipePKParser::NumberContext *> NmrPipePKParser::Peak_4dContext::number() {
  return getRuleContexts<NmrPipePKParser::NumberContext>();
}

NmrPipePKParser::NumberContext* NmrPipePKParser::Peak_4dContext::number(size_t i) {
  return getRuleContext<NmrPipePKParser::NumberContext>(i);
}

tree::TerminalNode* NmrPipePKParser::Peak_4dContext::RETURN() {
  return getToken(NmrPipePKParser::RETURN, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_4dContext::EOF() {
  return getToken(NmrPipePKParser::EOF, 0);
}

tree::TerminalNode* NmrPipePKParser::Peak_4dContext::Any_name() {
  return getToken(NmrPipePKParser::Any_name, 0);
}


size_t NmrPipePKParser::Peak_4dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePeak_4d;
}


std::any NmrPipePKParser::Peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Peak_4dContext* NmrPipePKParser::peak_4d() {
  Peak_4dContext *_localctx = _tracker.createInstance<Peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 14, NmrPipePKParser::RulePeak_4d);
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
    match(NmrPipePKParser::Integer);
    setState(435);
    number();
    setState(436);
    number();
    setState(437);
    number();
    setState(438);
    number();
    setState(439);
    number();
    setState(440);
    number();
    setState(441);
    number();
    setState(442);
    number();
    setState(443);
    number();
    setState(444);
    number();
    setState(445);
    number();
    setState(446);
    number();
    setState(447);
    number();
    setState(448);
    number();
    setState(449);
    number();
    setState(450);
    number();
    setState(451);
    number();
    setState(452);
    number();
    setState(453);
    number();
    setState(454);
    number();
    setState(455);
    number();
    setState(456);
    number();
    setState(457);
    number();
    setState(458);
    number();
    setState(459);
    match(NmrPipePKParser::Integer);
    setState(460);
    match(NmrPipePKParser::Integer);
    setState(461);
    match(NmrPipePKParser::Integer);
    setState(462);
    match(NmrPipePKParser::Integer);
    setState(463);
    match(NmrPipePKParser::Integer);
    setState(464);
    match(NmrPipePKParser::Integer);
    setState(465);
    match(NmrPipePKParser::Integer);
    setState(466);
    match(NmrPipePKParser::Integer);
    setState(467);
    number();
    setState(468);
    number();
    setState(469);
    number();
    setState(470);
    number();
    setState(471);
    match(NmrPipePKParser::Integer);
    setState(473);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Any_name) {
      setState(472);
      match(NmrPipePKParser::Any_name);
    }
    setState(475);
    match(NmrPipePKParser::Integer);
    setState(476);
    match(NmrPipePKParser::Integer);
    setState(478);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Integer) {
      setState(477);
      match(NmrPipePKParser::Integer);
    }
    setState(480);
    _la = _input->LA(1);
    if (!(_la == NmrPipePKParser::EOF

    || _la == NmrPipePKParser::RETURN)) {
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

//----------------- Pipp_labelContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_labelContext::Pipp_labelContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Pipp_labelContext::Data() {
  return getToken(NmrPipePKParser::Data, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_labelContext::Dim_count_DA() {
  return getToken(NmrPipePKParser::Dim_count_DA, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_labelContext::Integer_DA() {
  return getToken(NmrPipePKParser::Integer_DA, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_labelContext::RETURN_DA() {
  return getToken(NmrPipePKParser::RETURN_DA, 0);
}

std::vector<NmrPipePKParser::Pipp_axisContext *> NmrPipePKParser::Pipp_labelContext::pipp_axis() {
  return getRuleContexts<NmrPipePKParser::Pipp_axisContext>();
}

NmrPipePKParser::Pipp_axisContext* NmrPipePKParser::Pipp_labelContext::pipp_axis(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_axisContext>(i);
}


size_t NmrPipePKParser::Pipp_labelContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_label;
}


std::any NmrPipePKParser::Pipp_labelContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_label(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_labelContext* NmrPipePKParser::pipp_label() {
  Pipp_labelContext *_localctx = _tracker.createInstance<Pipp_labelContext>(_ctx, getState());
  enterRule(_localctx, 16, NmrPipePKParser::RulePipp_label);

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
    setState(482);
    match(NmrPipePKParser::Data);
    setState(483);
    match(NmrPipePKParser::Dim_count_DA);
    setState(484);
    match(NmrPipePKParser::Integer_DA);
    setState(485);
    match(NmrPipePKParser::RETURN_DA);
    setState(487); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(486);
              pipp_axis();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(489); 
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

//----------------- Pipp_axisContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_axisContext::Pipp_axisContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Pipp_axisContext::Data() {
  return getToken(NmrPipePKParser::Data, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_axisContext::Integer_DA() {
  return getToken(NmrPipePKParser::Integer_DA, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_axisContext::Float_DA() {
  return getTokens(NmrPipePKParser::Float_DA);
}

tree::TerminalNode* NmrPipePKParser::Pipp_axisContext::Float_DA(size_t i) {
  return getToken(NmrPipePKParser::Float_DA, i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_axisContext::RETURN_DA() {
  return getToken(NmrPipePKParser::RETURN_DA, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_axisContext::X_axis_DA() {
  return getToken(NmrPipePKParser::X_axis_DA, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_axisContext::Y_axis_DA() {
  return getToken(NmrPipePKParser::Y_axis_DA, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_axisContext::Z_axis_DA() {
  return getToken(NmrPipePKParser::Z_axis_DA, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_axisContext::A_axis_DA() {
  return getToken(NmrPipePKParser::A_axis_DA, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_axisContext::Ppm_DA() {
  return getToken(NmrPipePKParser::Ppm_DA, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_axisContext::Hz_DA() {
  return getToken(NmrPipePKParser::Hz_DA, 0);
}


size_t NmrPipePKParser::Pipp_axisContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_axis;
}


std::any NmrPipePKParser::Pipp_axisContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_axis(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_axisContext* NmrPipePKParser::pipp_axis() {
  Pipp_axisContext *_localctx = _tracker.createInstance<Pipp_axisContext>(_ctx, getState());
  enterRule(_localctx, 18, NmrPipePKParser::RulePipp_axis);
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
    match(NmrPipePKParser::Data);
    setState(492);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1966080) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(493);
    match(NmrPipePKParser::Integer_DA);
    setState(494);
    match(NmrPipePKParser::Float_DA);
    setState(495);
    match(NmrPipePKParser::Float_DA);
    setState(496);
    match(NmrPipePKParser::Float_DA);
    setState(497);
    _la = _input->LA(1);
    if (!(_la == NmrPipePKParser::Ppm_DA

    || _la == NmrPipePKParser::Hz_DA)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(498);
    match(NmrPipePKParser::Float_DA);
    setState(499);
    match(NmrPipePKParser::RETURN_DA);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pipp_peak_list_2dContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_peak_list_2dContext::Pipp_peak_list_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_2dContext::Format() {
  return getToken(NmrPipePKParser::Format, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_2dContext::RETURN_FO() {
  return getToken(NmrPipePKParser::RETURN_FO, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_2dContext::Vars() {
  return getToken(NmrPipePKParser::Vars, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_2dContext::PkID() {
  return getToken(NmrPipePKParser::PkID, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_2dContext::X() {
  return getToken(NmrPipePKParser::X, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_2dContext::Y() {
  return getToken(NmrPipePKParser::Y, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_2dContext::Intensity() {
  return getToken(NmrPipePKParser::Intensity, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_2dContext::RETURN_VA() {
  return getToken(NmrPipePKParser::RETURN_VA, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_peak_list_2dContext::Format_code() {
  return getTokens(NmrPipePKParser::Format_code);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_2dContext::Format_code(size_t i) {
  return getToken(NmrPipePKParser::Format_code, i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_2dContext::Assign() {
  return getToken(NmrPipePKParser::Assign, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_2dContext::Assign1() {
  return getToken(NmrPipePKParser::Assign1, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_2dContext::Assign2() {
  return getToken(NmrPipePKParser::Assign2, 0);
}

std::vector<NmrPipePKParser::Pipp_peak_2dContext *> NmrPipePKParser::Pipp_peak_list_2dContext::pipp_peak_2d() {
  return getRuleContexts<NmrPipePKParser::Pipp_peak_2dContext>();
}

NmrPipePKParser::Pipp_peak_2dContext* NmrPipePKParser::Pipp_peak_list_2dContext::pipp_peak_2d(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_peak_2dContext>(i);
}


size_t NmrPipePKParser::Pipp_peak_list_2dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_peak_list_2d;
}


std::any NmrPipePKParser::Pipp_peak_list_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_peak_list_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_peak_list_2dContext* NmrPipePKParser::pipp_peak_list_2d() {
  Pipp_peak_list_2dContext *_localctx = _tracker.createInstance<Pipp_peak_list_2dContext>(_ctx, getState());
  enterRule(_localctx, 20, NmrPipePKParser::RulePipp_peak_list_2d);
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
    setState(501);
    match(NmrPipePKParser::Format);
    setState(503); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(502);
      match(NmrPipePKParser::Format_code);
      setState(505); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrPipePKParser::Format_code);
    setState(507);
    match(NmrPipePKParser::RETURN_FO);
    setState(508);
    match(NmrPipePKParser::Vars);
    setState(509);
    match(NmrPipePKParser::PkID);
    setState(510);
    match(NmrPipePKParser::X);
    setState(511);
    match(NmrPipePKParser::Y);
    setState(512);
    match(NmrPipePKParser::Intensity);
    setState(516);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case NmrPipePKParser::Assign: {
        setState(513);
        match(NmrPipePKParser::Assign);
        break;
      }

      case NmrPipePKParser::Assign1: {
        setState(514);
        match(NmrPipePKParser::Assign1);
        setState(515);
        match(NmrPipePKParser::Assign2);
        break;
      }

      case NmrPipePKParser::RETURN_VA: {
        break;
      }

    default:
      break;
    }
    setState(518);
    match(NmrPipePKParser::RETURN_VA);
    setState(520); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(519);
      pipp_peak_2d();
      setState(522); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrPipePKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pipp_peak_2dContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_peak_2dContext::Pipp_peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_2dContext::Integer() {
  return getToken(NmrPipePKParser::Integer, 0);
}

std::vector<NmrPipePKParser::NumberContext *> NmrPipePKParser::Pipp_peak_2dContext::number() {
  return getRuleContexts<NmrPipePKParser::NumberContext>();
}

NmrPipePKParser::NumberContext* NmrPipePKParser::Pipp_peak_2dContext::number(size_t i) {
  return getRuleContext<NmrPipePKParser::NumberContext>(i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_2dContext::RETURN() {
  return getToken(NmrPipePKParser::RETURN, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_2dContext::EOF() {
  return getToken(NmrPipePKParser::EOF, 0);
}


size_t NmrPipePKParser::Pipp_peak_2dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_peak_2d;
}


std::any NmrPipePKParser::Pipp_peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_peak_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_peak_2dContext* NmrPipePKParser::pipp_peak_2d() {
  Pipp_peak_2dContext *_localctx = _tracker.createInstance<Pipp_peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 22, NmrPipePKParser::RulePipp_peak_2d);
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
    setState(524);
    match(NmrPipePKParser::Integer);
    setState(525);
    number();
    setState(526);
    number();
    setState(528); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(527);
      number();
      setState(530); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 4992) != 0));
    setState(532);
    _la = _input->LA(1);
    if (!(_la == NmrPipePKParser::EOF

    || _la == NmrPipePKParser::RETURN)) {
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

//----------------- Pipp_peak_list_3dContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_peak_list_3dContext::Pipp_peak_list_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::Format() {
  return getToken(NmrPipePKParser::Format, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::RETURN_FO() {
  return getToken(NmrPipePKParser::RETURN_FO, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::Vars() {
  return getToken(NmrPipePKParser::Vars, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::PkID() {
  return getToken(NmrPipePKParser::PkID, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::X() {
  return getToken(NmrPipePKParser::X, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::Y() {
  return getToken(NmrPipePKParser::Y, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::Z() {
  return getToken(NmrPipePKParser::Z, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::Intensity() {
  return getToken(NmrPipePKParser::Intensity, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::RETURN_VA() {
  return getToken(NmrPipePKParser::RETURN_VA, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_peak_list_3dContext::Format_code() {
  return getTokens(NmrPipePKParser::Format_code);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::Format_code(size_t i) {
  return getToken(NmrPipePKParser::Format_code, i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::Sl_Z() {
  return getToken(NmrPipePKParser::Sl_Z, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::Assign() {
  return getToken(NmrPipePKParser::Assign, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::Assign1() {
  return getToken(NmrPipePKParser::Assign1, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_3dContext::Assign2() {
  return getToken(NmrPipePKParser::Assign2, 0);
}

std::vector<NmrPipePKParser::Pipp_peak_3dContext *> NmrPipePKParser::Pipp_peak_list_3dContext::pipp_peak_3d() {
  return getRuleContexts<NmrPipePKParser::Pipp_peak_3dContext>();
}

NmrPipePKParser::Pipp_peak_3dContext* NmrPipePKParser::Pipp_peak_list_3dContext::pipp_peak_3d(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_peak_3dContext>(i);
}


size_t NmrPipePKParser::Pipp_peak_list_3dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_peak_list_3d;
}


std::any NmrPipePKParser::Pipp_peak_list_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_peak_list_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_peak_list_3dContext* NmrPipePKParser::pipp_peak_list_3d() {
  Pipp_peak_list_3dContext *_localctx = _tracker.createInstance<Pipp_peak_list_3dContext>(_ctx, getState());
  enterRule(_localctx, 24, NmrPipePKParser::RulePipp_peak_list_3d);
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
    match(NmrPipePKParser::Format);
    setState(536); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(535);
      match(NmrPipePKParser::Format_code);
      setState(538); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrPipePKParser::Format_code);
    setState(540);
    match(NmrPipePKParser::RETURN_FO);
    setState(541);
    match(NmrPipePKParser::Vars);
    setState(542);
    match(NmrPipePKParser::PkID);
    setState(544);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Sl_Z) {
      setState(543);
      match(NmrPipePKParser::Sl_Z);
    }
    setState(546);
    match(NmrPipePKParser::X);
    setState(547);
    match(NmrPipePKParser::Y);
    setState(548);
    match(NmrPipePKParser::Z);
    setState(549);
    match(NmrPipePKParser::Intensity);
    setState(553);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case NmrPipePKParser::Assign: {
        setState(550);
        match(NmrPipePKParser::Assign);
        break;
      }

      case NmrPipePKParser::Assign1: {
        setState(551);
        match(NmrPipePKParser::Assign1);
        setState(552);
        match(NmrPipePKParser::Assign2);
        break;
      }

      case NmrPipePKParser::RETURN_VA: {
        break;
      }

    default:
      break;
    }
    setState(555);
    match(NmrPipePKParser::RETURN_VA);
    setState(557); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(556);
      pipp_peak_3d();
      setState(559); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrPipePKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pipp_peak_3dContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_peak_3dContext::Pipp_peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_peak_3dContext::Integer() {
  return getTokens(NmrPipePKParser::Integer);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_3dContext::Integer(size_t i) {
  return getToken(NmrPipePKParser::Integer, i);
}

std::vector<NmrPipePKParser::NumberContext *> NmrPipePKParser::Pipp_peak_3dContext::number() {
  return getRuleContexts<NmrPipePKParser::NumberContext>();
}

NmrPipePKParser::NumberContext* NmrPipePKParser::Pipp_peak_3dContext::number(size_t i) {
  return getRuleContext<NmrPipePKParser::NumberContext>(i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_3dContext::RETURN() {
  return getToken(NmrPipePKParser::RETURN, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_3dContext::EOF() {
  return getToken(NmrPipePKParser::EOF, 0);
}


size_t NmrPipePKParser::Pipp_peak_3dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_peak_3d;
}


std::any NmrPipePKParser::Pipp_peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_peak_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_peak_3dContext* NmrPipePKParser::pipp_peak_3d() {
  Pipp_peak_3dContext *_localctx = _tracker.createInstance<Pipp_peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 26, NmrPipePKParser::RulePipp_peak_3d);
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
    setState(561);
    match(NmrPipePKParser::Integer);
    setState(563);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 39, _ctx)) {
    case 1: {
      setState(562);
      match(NmrPipePKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(565);
    number();
    setState(566);
    number();
    setState(567);
    number();
    setState(569); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(568);
      number();
      setState(571); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 4992) != 0));
    setState(573);
    _la = _input->LA(1);
    if (!(_la == NmrPipePKParser::EOF

    || _la == NmrPipePKParser::RETURN)) {
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

//----------------- Pipp_peak_list_4dContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_peak_list_4dContext::Pipp_peak_list_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::Format() {
  return getToken(NmrPipePKParser::Format, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::RETURN_FO() {
  return getToken(NmrPipePKParser::RETURN_FO, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::Vars() {
  return getToken(NmrPipePKParser::Vars, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::PkID() {
  return getToken(NmrPipePKParser::PkID, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::X() {
  return getToken(NmrPipePKParser::X, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::Y() {
  return getToken(NmrPipePKParser::Y, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::Z() {
  return getToken(NmrPipePKParser::Z, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::A() {
  return getToken(NmrPipePKParser::A, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::Intensity() {
  return getToken(NmrPipePKParser::Intensity, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::RETURN_VA() {
  return getToken(NmrPipePKParser::RETURN_VA, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_peak_list_4dContext::Format_code() {
  return getTokens(NmrPipePKParser::Format_code);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::Format_code(size_t i) {
  return getToken(NmrPipePKParser::Format_code, i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::Sl_A() {
  return getToken(NmrPipePKParser::Sl_A, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::Sl_Z() {
  return getToken(NmrPipePKParser::Sl_Z, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::Assign() {
  return getToken(NmrPipePKParser::Assign, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::Assign1() {
  return getToken(NmrPipePKParser::Assign1, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_list_4dContext::Assign2() {
  return getToken(NmrPipePKParser::Assign2, 0);
}

std::vector<NmrPipePKParser::Pipp_peak_4dContext *> NmrPipePKParser::Pipp_peak_list_4dContext::pipp_peak_4d() {
  return getRuleContexts<NmrPipePKParser::Pipp_peak_4dContext>();
}

NmrPipePKParser::Pipp_peak_4dContext* NmrPipePKParser::Pipp_peak_list_4dContext::pipp_peak_4d(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_peak_4dContext>(i);
}


size_t NmrPipePKParser::Pipp_peak_list_4dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_peak_list_4d;
}


std::any NmrPipePKParser::Pipp_peak_list_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_peak_list_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_peak_list_4dContext* NmrPipePKParser::pipp_peak_list_4d() {
  Pipp_peak_list_4dContext *_localctx = _tracker.createInstance<Pipp_peak_list_4dContext>(_ctx, getState());
  enterRule(_localctx, 28, NmrPipePKParser::RulePipp_peak_list_4d);
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
    setState(575);
    match(NmrPipePKParser::Format);
    setState(577); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(576);
      match(NmrPipePKParser::Format_code);
      setState(579); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrPipePKParser::Format_code);
    setState(581);
    match(NmrPipePKParser::RETURN_FO);
    setState(582);
    match(NmrPipePKParser::Vars);
    setState(583);
    match(NmrPipePKParser::PkID);
    setState(585);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Sl_A) {
      setState(584);
      match(NmrPipePKParser::Sl_A);
    }
    setState(588);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrPipePKParser::Sl_Z) {
      setState(587);
      match(NmrPipePKParser::Sl_Z);
    }
    setState(590);
    match(NmrPipePKParser::X);
    setState(591);
    match(NmrPipePKParser::Y);
    setState(592);
    match(NmrPipePKParser::Z);
    setState(593);
    match(NmrPipePKParser::A);
    setState(594);
    match(NmrPipePKParser::Intensity);
    setState(598);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case NmrPipePKParser::Assign: {
        setState(595);
        match(NmrPipePKParser::Assign);
        break;
      }

      case NmrPipePKParser::Assign1: {
        setState(596);
        match(NmrPipePKParser::Assign1);
        setState(597);
        match(NmrPipePKParser::Assign2);
        break;
      }

      case NmrPipePKParser::RETURN_VA: {
        break;
      }

    default:
      break;
    }
    setState(600);
    match(NmrPipePKParser::RETURN_VA);
    setState(602); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(601);
      pipp_peak_4d();
      setState(604); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrPipePKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pipp_peak_4dContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_peak_4dContext::Pipp_peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_peak_4dContext::Integer() {
  return getTokens(NmrPipePKParser::Integer);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_4dContext::Integer(size_t i) {
  return getToken(NmrPipePKParser::Integer, i);
}

std::vector<NmrPipePKParser::NumberContext *> NmrPipePKParser::Pipp_peak_4dContext::number() {
  return getRuleContexts<NmrPipePKParser::NumberContext>();
}

NmrPipePKParser::NumberContext* NmrPipePKParser::Pipp_peak_4dContext::number(size_t i) {
  return getRuleContext<NmrPipePKParser::NumberContext>(i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_4dContext::RETURN() {
  return getToken(NmrPipePKParser::RETURN, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_peak_4dContext::EOF() {
  return getToken(NmrPipePKParser::EOF, 0);
}


size_t NmrPipePKParser::Pipp_peak_4dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_peak_4d;
}


std::any NmrPipePKParser::Pipp_peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_peak_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_peak_4dContext* NmrPipePKParser::pipp_peak_4d() {
  Pipp_peak_4dContext *_localctx = _tracker.createInstance<Pipp_peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 30, NmrPipePKParser::RulePipp_peak_4d);
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
    match(NmrPipePKParser::Integer);
    setState(608);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 46, _ctx)) {
    case 1: {
      setState(607);
      match(NmrPipePKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(611);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 47, _ctx)) {
    case 1: {
      setState(610);
      match(NmrPipePKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(613);
    number();
    setState(614);
    number();
    setState(615);
    number();
    setState(616);
    number();
    setState(618); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(617);
      number();
      setState(620); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 4992) != 0));
    setState(622);
    _la = _input->LA(1);
    if (!(_la == NmrPipePKParser::EOF

    || _la == NmrPipePKParser::RETURN)) {
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

//----------------- Pipp_row_peak_list_2dContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_row_peak_list_2dContext::Pipp_row_peak_list_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<NmrPipePKParser::Pipp_row_peak_2dContext *> NmrPipePKParser::Pipp_row_peak_list_2dContext::pipp_row_peak_2d() {
  return getRuleContexts<NmrPipePKParser::Pipp_row_peak_2dContext>();
}

NmrPipePKParser::Pipp_row_peak_2dContext* NmrPipePKParser::Pipp_row_peak_list_2dContext::pipp_row_peak_2d(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_row_peak_2dContext>(i);
}


size_t NmrPipePKParser::Pipp_row_peak_list_2dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_row_peak_list_2d;
}


std::any NmrPipePKParser::Pipp_row_peak_list_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_row_peak_list_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_row_peak_list_2dContext* NmrPipePKParser::pipp_row_peak_list_2d() {
  Pipp_row_peak_list_2dContext *_localctx = _tracker.createInstance<Pipp_row_peak_list_2dContext>(_ctx, getState());
  enterRule(_localctx, 32, NmrPipePKParser::RulePipp_row_peak_list_2d);

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
    setState(625); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(624);
              pipp_row_peak_2d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(627); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 49, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pipp_row_peak_2dContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_row_peak_2dContext::Pipp_row_peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::L_paren() {
  return getToken(NmrPipePKParser::L_paren, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_row_peak_2dContext::Float_PR() {
  return getTokens(NmrPipePKParser::Float_PR);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::Float_PR(size_t i) {
  return getToken(NmrPipePKParser::Float_PR, i);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_row_peak_2dContext::Comma() {
  return getTokens(NmrPipePKParser::Comma);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::Comma(size_t i) {
  return getToken(NmrPipePKParser::Comma, i);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_row_peak_2dContext::Semicolon() {
  return getTokens(NmrPipePKParser::Semicolon);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::Semicolon(size_t i) {
  return getToken(NmrPipePKParser::Semicolon, i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::Number_sign() {
  return getToken(NmrPipePKParser::Number_sign, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_row_peak_2dContext::Integer_PR() {
  return getTokens(NmrPipePKParser::Integer_PR);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::Integer_PR(size_t i) {
  return getToken(NmrPipePKParser::Integer_PR, i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::Caret() {
  return getToken(NmrPipePKParser::Caret, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::Real_PR() {
  return getToken(NmrPipePKParser::Real_PR, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::Percent_sign() {
  return getToken(NmrPipePKParser::Percent_sign, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::R_paren() {
  return getToken(NmrPipePKParser::R_paren, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::RETURN_PR() {
  return getToken(NmrPipePKParser::RETURN_PR, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::EOF() {
  return getToken(NmrPipePKParser::EOF, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::Assignments_PR() {
  return getToken(NmrPipePKParser::Assignments_PR, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::L_brkt() {
  return getToken(NmrPipePKParser::L_brkt, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_2dContext::R_brkt() {
  return getToken(NmrPipePKParser::R_brkt, 0);
}


size_t NmrPipePKParser::Pipp_row_peak_2dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_row_peak_2d;
}


std::any NmrPipePKParser::Pipp_row_peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_row_peak_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_row_peak_2dContext* NmrPipePKParser::pipp_row_peak_2d() {
  Pipp_row_peak_2dContext *_localctx = _tracker.createInstance<Pipp_row_peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 34, NmrPipePKParser::RulePipp_row_peak_2d);
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
    setState(629);
    match(NmrPipePKParser::L_paren);
    setState(630);
    match(NmrPipePKParser::Float_PR);
    setState(631);
    match(NmrPipePKParser::Comma);
    setState(632);
    match(NmrPipePKParser::Float_PR);
    setState(633);
    match(NmrPipePKParser::Semicolon);
    setState(634);
    match(NmrPipePKParser::Number_sign);
    setState(635);
    match(NmrPipePKParser::Integer_PR);
    setState(636);
    match(NmrPipePKParser::Semicolon);
    setState(643);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case NmrPipePKParser::Assignments_PR: {
        setState(637);
        match(NmrPipePKParser::Assignments_PR);
        break;
      }

      case NmrPipePKParser::L_brkt: {
        setState(638);
        match(NmrPipePKParser::L_brkt);
        setState(639);
        match(NmrPipePKParser::Float_PR);
        setState(640);
        match(NmrPipePKParser::Comma);
        setState(641);
        match(NmrPipePKParser::Float_PR);
        setState(642);
        match(NmrPipePKParser::R_brkt);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(645);
    match(NmrPipePKParser::Caret);
    setState(646);
    match(NmrPipePKParser::Real_PR);
    setState(647);
    match(NmrPipePKParser::Semicolon);
    setState(648);
    match(NmrPipePKParser::Percent_sign);
    setState(649);
    match(NmrPipePKParser::Integer_PR);
    setState(650);
    match(NmrPipePKParser::Semicolon);
    setState(651);
    match(NmrPipePKParser::R_paren);
    setState(652);
    _la = _input->LA(1);
    if (!(_la == NmrPipePKParser::EOF || _la == NmrPipePKParser::RETURN_PR)) {
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

//----------------- Pipp_row_peak_list_3dContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_row_peak_list_3dContext::Pipp_row_peak_list_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<NmrPipePKParser::Pipp_row_peak_3dContext *> NmrPipePKParser::Pipp_row_peak_list_3dContext::pipp_row_peak_3d() {
  return getRuleContexts<NmrPipePKParser::Pipp_row_peak_3dContext>();
}

NmrPipePKParser::Pipp_row_peak_3dContext* NmrPipePKParser::Pipp_row_peak_list_3dContext::pipp_row_peak_3d(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_row_peak_3dContext>(i);
}


size_t NmrPipePKParser::Pipp_row_peak_list_3dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_row_peak_list_3d;
}


std::any NmrPipePKParser::Pipp_row_peak_list_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_row_peak_list_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_row_peak_list_3dContext* NmrPipePKParser::pipp_row_peak_list_3d() {
  Pipp_row_peak_list_3dContext *_localctx = _tracker.createInstance<Pipp_row_peak_list_3dContext>(_ctx, getState());
  enterRule(_localctx, 36, NmrPipePKParser::RulePipp_row_peak_list_3d);

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
    setState(655); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(654);
              pipp_row_peak_3d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(657); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 51, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pipp_row_peak_3dContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_row_peak_3dContext::Pipp_row_peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::L_paren() {
  return getToken(NmrPipePKParser::L_paren, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_row_peak_3dContext::Float_PR() {
  return getTokens(NmrPipePKParser::Float_PR);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::Float_PR(size_t i) {
  return getToken(NmrPipePKParser::Float_PR, i);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_row_peak_3dContext::Comma() {
  return getTokens(NmrPipePKParser::Comma);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::Comma(size_t i) {
  return getToken(NmrPipePKParser::Comma, i);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_row_peak_3dContext::Semicolon() {
  return getTokens(NmrPipePKParser::Semicolon);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::Semicolon(size_t i) {
  return getToken(NmrPipePKParser::Semicolon, i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::Number_sign() {
  return getToken(NmrPipePKParser::Number_sign, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_row_peak_3dContext::Integer_PR() {
  return getTokens(NmrPipePKParser::Integer_PR);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::Integer_PR(size_t i) {
  return getToken(NmrPipePKParser::Integer_PR, i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::Caret() {
  return getToken(NmrPipePKParser::Caret, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::Real_PR() {
  return getToken(NmrPipePKParser::Real_PR, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::Percent_sign() {
  return getToken(NmrPipePKParser::Percent_sign, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::R_paren() {
  return getToken(NmrPipePKParser::R_paren, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::RETURN_PR() {
  return getToken(NmrPipePKParser::RETURN_PR, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::EOF() {
  return getToken(NmrPipePKParser::EOF, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::Assignments_PR() {
  return getToken(NmrPipePKParser::Assignments_PR, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::L_brkt() {
  return getToken(NmrPipePKParser::L_brkt, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_3dContext::R_brkt() {
  return getToken(NmrPipePKParser::R_brkt, 0);
}


size_t NmrPipePKParser::Pipp_row_peak_3dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_row_peak_3d;
}


std::any NmrPipePKParser::Pipp_row_peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_row_peak_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_row_peak_3dContext* NmrPipePKParser::pipp_row_peak_3d() {
  Pipp_row_peak_3dContext *_localctx = _tracker.createInstance<Pipp_row_peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 38, NmrPipePKParser::RulePipp_row_peak_3d);
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
    setState(659);
    match(NmrPipePKParser::L_paren);
    setState(660);
    match(NmrPipePKParser::Float_PR);
    setState(661);
    match(NmrPipePKParser::Comma);
    setState(662);
    match(NmrPipePKParser::Float_PR);
    setState(663);
    match(NmrPipePKParser::Comma);
    setState(664);
    match(NmrPipePKParser::Float_PR);
    setState(665);
    match(NmrPipePKParser::Semicolon);
    setState(666);
    match(NmrPipePKParser::Number_sign);
    setState(667);
    match(NmrPipePKParser::Integer_PR);
    setState(668);
    match(NmrPipePKParser::Semicolon);
    setState(677);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case NmrPipePKParser::Assignments_PR: {
        setState(669);
        match(NmrPipePKParser::Assignments_PR);
        break;
      }

      case NmrPipePKParser::L_brkt: {
        setState(670);
        match(NmrPipePKParser::L_brkt);
        setState(671);
        match(NmrPipePKParser::Float_PR);
        setState(672);
        match(NmrPipePKParser::Comma);
        setState(673);
        match(NmrPipePKParser::Float_PR);
        setState(674);
        match(NmrPipePKParser::Comma);
        setState(675);
        match(NmrPipePKParser::Float_PR);
        setState(676);
        match(NmrPipePKParser::R_brkt);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(679);
    match(NmrPipePKParser::Caret);
    setState(680);
    match(NmrPipePKParser::Real_PR);
    setState(681);
    match(NmrPipePKParser::Semicolon);
    setState(682);
    match(NmrPipePKParser::Percent_sign);
    setState(683);
    match(NmrPipePKParser::Integer_PR);
    setState(684);
    match(NmrPipePKParser::Semicolon);
    setState(685);
    match(NmrPipePKParser::R_paren);
    setState(686);
    _la = _input->LA(1);
    if (!(_la == NmrPipePKParser::EOF || _la == NmrPipePKParser::RETURN_PR)) {
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

//----------------- Pipp_row_peak_list_4dContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_row_peak_list_4dContext::Pipp_row_peak_list_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<NmrPipePKParser::Pipp_row_peak_4dContext *> NmrPipePKParser::Pipp_row_peak_list_4dContext::pipp_row_peak_4d() {
  return getRuleContexts<NmrPipePKParser::Pipp_row_peak_4dContext>();
}

NmrPipePKParser::Pipp_row_peak_4dContext* NmrPipePKParser::Pipp_row_peak_list_4dContext::pipp_row_peak_4d(size_t i) {
  return getRuleContext<NmrPipePKParser::Pipp_row_peak_4dContext>(i);
}


size_t NmrPipePKParser::Pipp_row_peak_list_4dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_row_peak_list_4d;
}


std::any NmrPipePKParser::Pipp_row_peak_list_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_row_peak_list_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_row_peak_list_4dContext* NmrPipePKParser::pipp_row_peak_list_4d() {
  Pipp_row_peak_list_4dContext *_localctx = _tracker.createInstance<Pipp_row_peak_list_4dContext>(_ctx, getState());
  enterRule(_localctx, 40, NmrPipePKParser::RulePipp_row_peak_list_4d);

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
    setState(689); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(688);
              pipp_row_peak_4d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(691); 
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

//----------------- Pipp_row_peak_4dContext ------------------------------------------------------------------

NmrPipePKParser::Pipp_row_peak_4dContext::Pipp_row_peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::L_paren() {
  return getToken(NmrPipePKParser::L_paren, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_row_peak_4dContext::Float_PR() {
  return getTokens(NmrPipePKParser::Float_PR);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::Float_PR(size_t i) {
  return getToken(NmrPipePKParser::Float_PR, i);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_row_peak_4dContext::Comma() {
  return getTokens(NmrPipePKParser::Comma);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::Comma(size_t i) {
  return getToken(NmrPipePKParser::Comma, i);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_row_peak_4dContext::Semicolon() {
  return getTokens(NmrPipePKParser::Semicolon);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::Semicolon(size_t i) {
  return getToken(NmrPipePKParser::Semicolon, i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::Number_sign() {
  return getToken(NmrPipePKParser::Number_sign, 0);
}

std::vector<tree::TerminalNode *> NmrPipePKParser::Pipp_row_peak_4dContext::Integer_PR() {
  return getTokens(NmrPipePKParser::Integer_PR);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::Integer_PR(size_t i) {
  return getToken(NmrPipePKParser::Integer_PR, i);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::Caret() {
  return getToken(NmrPipePKParser::Caret, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::Real_PR() {
  return getToken(NmrPipePKParser::Real_PR, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::Percent_sign() {
  return getToken(NmrPipePKParser::Percent_sign, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::R_paren() {
  return getToken(NmrPipePKParser::R_paren, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::RETURN_PR() {
  return getToken(NmrPipePKParser::RETURN_PR, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::EOF() {
  return getToken(NmrPipePKParser::EOF, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::Assignments_PR() {
  return getToken(NmrPipePKParser::Assignments_PR, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::L_brkt() {
  return getToken(NmrPipePKParser::L_brkt, 0);
}

tree::TerminalNode* NmrPipePKParser::Pipp_row_peak_4dContext::R_brkt() {
  return getToken(NmrPipePKParser::R_brkt, 0);
}


size_t NmrPipePKParser::Pipp_row_peak_4dContext::getRuleIndex() const {
  return NmrPipePKParser::RulePipp_row_peak_4d;
}


std::any NmrPipePKParser::Pipp_row_peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitPipp_row_peak_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::Pipp_row_peak_4dContext* NmrPipePKParser::pipp_row_peak_4d() {
  Pipp_row_peak_4dContext *_localctx = _tracker.createInstance<Pipp_row_peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 42, NmrPipePKParser::RulePipp_row_peak_4d);
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
    setState(693);
    match(NmrPipePKParser::L_paren);
    setState(694);
    match(NmrPipePKParser::Float_PR);
    setState(695);
    match(NmrPipePKParser::Comma);
    setState(696);
    match(NmrPipePKParser::Float_PR);
    setState(697);
    match(NmrPipePKParser::Comma);
    setState(698);
    match(NmrPipePKParser::Float_PR);
    setState(699);
    match(NmrPipePKParser::Comma);
    setState(700);
    match(NmrPipePKParser::Float_PR);
    setState(701);
    match(NmrPipePKParser::Semicolon);
    setState(702);
    match(NmrPipePKParser::Number_sign);
    setState(703);
    match(NmrPipePKParser::Integer_PR);
    setState(704);
    match(NmrPipePKParser::Semicolon);
    setState(715);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case NmrPipePKParser::Assignments_PR: {
        setState(705);
        match(NmrPipePKParser::Assignments_PR);
        break;
      }

      case NmrPipePKParser::L_brkt: {
        setState(706);
        match(NmrPipePKParser::L_brkt);
        setState(707);
        match(NmrPipePKParser::Float_PR);
        setState(708);
        match(NmrPipePKParser::Comma);
        setState(709);
        match(NmrPipePKParser::Float_PR);
        setState(710);
        match(NmrPipePKParser::Comma);
        setState(711);
        match(NmrPipePKParser::Float_PR);
        setState(712);
        match(NmrPipePKParser::Comma);
        setState(713);
        match(NmrPipePKParser::Float_PR);
        setState(714);
        match(NmrPipePKParser::R_brkt);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(717);
    match(NmrPipePKParser::Caret);
    setState(718);
    match(NmrPipePKParser::Real_PR);
    setState(719);
    match(NmrPipePKParser::Semicolon);
    setState(720);
    match(NmrPipePKParser::Percent_sign);
    setState(721);
    match(NmrPipePKParser::Integer_PR);
    setState(722);
    match(NmrPipePKParser::Semicolon);
    setState(723);
    match(NmrPipePKParser::R_paren);
    setState(724);
    _la = _input->LA(1);
    if (!(_la == NmrPipePKParser::EOF || _la == NmrPipePKParser::RETURN_PR)) {
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

//----------------- NumberContext ------------------------------------------------------------------

NmrPipePKParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipePKParser::NumberContext::Integer() {
  return getToken(NmrPipePKParser::Integer, 0);
}

tree::TerminalNode* NmrPipePKParser::NumberContext::Float() {
  return getToken(NmrPipePKParser::Float, 0);
}

tree::TerminalNode* NmrPipePKParser::NumberContext::Real() {
  return getToken(NmrPipePKParser::Real, 0);
}

tree::TerminalNode* NmrPipePKParser::NumberContext::Any_name() {
  return getToken(NmrPipePKParser::Any_name, 0);
}


size_t NmrPipePKParser::NumberContext::getRuleIndex() const {
  return NmrPipePKParser::RuleNumber;
}


std::any NmrPipePKParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipePKParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

NmrPipePKParser::NumberContext* NmrPipePKParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 44, NmrPipePKParser::RuleNumber);
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
    setState(726);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 4992) != 0))) {
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

void NmrPipePKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  nmrpipepkparserParserInitialize();
#else
  ::antlr4::internal::call_once(nmrpipepkparserParserOnceFlag, nmrpipepkparserParserInitialize);
#endif
}
