
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/OliviaPKParser.g4 by ANTLR 4.13.2


#include "OliviaPKParserVisitor.h"

#include "OliviaPKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct OliviaPKParserStaticData final {
  OliviaPKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  OliviaPKParserStaticData(const OliviaPKParserStaticData&) = delete;
  OliviaPKParserStaticData(OliviaPKParserStaticData&&) = delete;
  OliviaPKParserStaticData& operator=(const OliviaPKParserStaticData&) = delete;
  OliviaPKParserStaticData& operator=(OliviaPKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag oliviapkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<OliviaPKParserStaticData> oliviapkparserParserStaticData = nullptr;

void oliviapkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (oliviapkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(oliviapkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<OliviaPKParserStaticData>(
    std::vector<std::string>{
      "olivia_pk", "comment", "idx_peak_list_2d", "idx_peak_2d", "idx_peak_list_3d", 
      "idx_peak_3d", "idx_peak_list_4d", "idx_peak_4d", "ass_peak_list_2d", 
      "ass_peak_2d", "ass_peak_list_3d", "ass_peak_3d", "ass_peak_list_4d", 
      "ass_peak_4d", "def_2d_axis_order_ppm", "tp_2d_axis_order_ppm", "def_2d_axis_order_hz", 
      "tp_2d_axis_order_hz", "def_3d_axis_order_ppm", "tp_3d_axis_order_ppm", 
      "def_3d_axis_order_hz", "tp_3d_axis_order_hz", "def_4d_axis_order_ppm", 
      "tp_4d_axis_order_ppm", "def_4d_axis_order_hz", "tp_4d_axis_order_hz", 
      "string", "integer", "number", "memo"
    },
    std::vector<std::string>{
      "", "'TYPEDEF'", "'SEPARATOR'", "'FORMAT\\n'", "'UNFORMAT'", "'EOF'", 
      "", "", "", "", "'REMARK'", "", "", "", "", "", "", "", "", "", "'IDX_TBL_2D'", 
      "'IDX_TBL_3D'", "'IDX_TBL_4D'", "'ASS_TBL_2D'", "'ASS_TBL_3D'", "'ASS_TBL_4D'", 
      "", "", "'TAB'", "'COMMA'", "'SPACE'", "", "", "'INDEX'", "'X_PPM'", 
      "'Y_PPM'", "'Z_PPM'", "'A_PPM'", "'X_HZ'", "'Y_HZ'", "'Z_HZ'", "'A_HZ'", 
      "'AMPLITUDE'", "'VOLUME'", "'VOL_ERR'", "'X_CHAIN'", "'Y_CHAIN'", 
      "'Z_CHAIN'", "'A_CHAIN'", "'X_RESNAME'", "'Y_RESNAME'", "'Z_RESNAME'", 
      "'A_RESNAME'", "'X_SEQNUM'", "'Y_SEQNUM'", "'Z_SEQNUM'", "'A_SEQNUM'", 
      "'X_ASSIGN'", "'Y_ASSIGN'", "'Z_ASSIGN'", "'A_ASSIGN'", "'EVAL'", 
      "'STATUS'", "'USER_MEMO'", "'UPDATE_TIME'"
    },
    std::vector<std::string>{
      "", "Typedef", "Separator", "Format", "Unformat", "Eof", "Null_string", 
      "Integer", "Float", "Real", "COMMENT", "SHARP_COMMENT", "EXCLM_COMMENT", 
      "Double_quote_string", "Single_quote_string", "Simple_name", "SPACE", 
      "RETURN", "SECTION_COMMENT", "LINE_COMMENT", "Idx_tbl_2d", "Idx_tbl_3d", 
      "Idx_tbl_4d", "Ass_tbl_2d", "Ass_tbl_3d", "Ass_tbl_4d", "SPACE_TD", 
      "RETURN_TD", "Tab", "Comma", "Space", "SPACE_SE", "RETURN_SE", "Index", 
      "X_ppm", "Y_ppm", "Z_ppm", "A_ppm", "X_hz", "Y_hz", "Z_hz", "A_hz", 
      "Amplitude", "Volume", "Vol_err", "X_chain", "Y_chain", "Z_chain", 
      "A_chain", "X_resname", "Y_resname", "Z_resname", "A_resname", "X_seqnum", 
      "Y_seqnum", "Z_seqnum", "A_seqnum", "X_assign", "Y_assign", "Z_assign", 
      "A_assign", "Eval", "Status", "User_memo", "Update_time", "SPACE_FO", 
      "RETURN_FO", "Printf_string", "SPACE_PF", "RETURN_PF", "Any_name", 
      "SPACE_CM", "RETURN_CM"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,72,684,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,1,0,3,0,62,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,72,8,
  	0,10,0,12,0,75,9,0,1,0,1,0,1,1,1,1,5,1,81,8,1,10,1,12,1,84,9,1,1,1,1,
  	1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,100,8,2,1,2,1,2,
  	1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
  	2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,
  	138,8,2,11,2,12,2,139,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
  	1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
  	4,1,4,1,4,1,4,1,4,3,4,176,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
  	1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
  	4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
  	4,4,223,8,4,11,4,12,4,224,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
  	1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,
  	6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,266,8,6,1,6,1,6,1,6,1,6,
  	1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
  	6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
  	1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,322,8,
  	6,11,6,12,6,323,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
  	7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
  	1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
  	8,1,8,1,8,1,8,3,8,378,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
  	1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,4,
  	8,408,8,8,11,8,12,8,409,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
  	9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,
  	10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
  	10,1,10,1,10,1,10,1,10,3,10,458,8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
  	10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
  	10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,4,10,493,
  	8,10,11,10,12,10,494,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
  	1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
  	1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
  	1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
  	1,12,1,12,1,12,3,12,552,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
  	1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
  	1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
  	1,12,1,12,4,12,592,8,12,11,12,12,12,593,1,12,1,12,1,13,1,13,1,13,1,13,
  	1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
  	1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
  	1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,
  	1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,
  	1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,
  	1,25,1,25,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,29,0,0,
  	30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
  	48,50,52,54,56,58,0,6,1,1,72,72,1,0,28,30,2,0,6,6,15,15,1,0,6,7,1,0,7,
  	9,1,0,13,15,687,0,61,1,0,0,0,2,78,1,0,0,0,4,87,1,0,0,0,6,143,1,0,0,0,
  	8,163,1,0,0,0,10,228,1,0,0,0,12,253,1,0,0,0,14,327,1,0,0,0,16,357,1,0,
  	0,0,18,413,1,0,0,0,20,433,1,0,0,0,22,498,1,0,0,0,24,523,1,0,0,0,26,597,
  	1,0,0,0,28,627,1,0,0,0,30,630,1,0,0,0,32,633,1,0,0,0,34,636,1,0,0,0,36,
  	639,1,0,0,0,38,643,1,0,0,0,40,647,1,0,0,0,42,651,1,0,0,0,44,655,1,0,0,
  	0,46,660,1,0,0,0,48,665,1,0,0,0,50,670,1,0,0,0,52,675,1,0,0,0,54,677,
  	1,0,0,0,56,679,1,0,0,0,58,681,1,0,0,0,60,62,5,17,0,0,61,60,1,0,0,0,61,
  	62,1,0,0,0,62,73,1,0,0,0,63,72,3,2,1,0,64,72,3,4,2,0,65,72,3,8,4,0,66,
  	72,3,12,6,0,67,72,3,16,8,0,68,72,3,20,10,0,69,72,3,24,12,0,70,72,5,17,
  	0,0,71,63,1,0,0,0,71,64,1,0,0,0,71,65,1,0,0,0,71,66,1,0,0,0,71,67,1,0,
  	0,0,71,68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,
  	0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,77,5,0,0,1,77,1,1,0,
  	0,0,78,82,5,10,0,0,79,81,5,70,0,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,
  	0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,7,0,0,0,86,3,1,
  	0,0,0,87,88,5,1,0,0,88,89,5,20,0,0,89,90,5,27,0,0,90,91,5,2,0,0,91,92,
  	7,1,0,0,92,93,5,32,0,0,93,94,5,3,0,0,94,99,5,33,0,0,95,100,3,28,14,0,
  	96,100,3,30,15,0,97,100,3,32,16,0,98,100,3,34,17,0,99,95,1,0,0,0,99,96,
  	1,0,0,0,99,97,1,0,0,0,99,98,1,0,0,0,100,101,1,0,0,0,101,102,5,42,0,0,
  	102,103,5,43,0,0,103,104,5,44,0,0,104,105,5,45,0,0,105,106,5,49,0,0,106,
  	107,5,53,0,0,107,108,5,57,0,0,108,109,5,46,0,0,109,110,5,50,0,0,110,111,
  	5,54,0,0,111,112,5,58,0,0,112,113,5,61,0,0,113,114,5,62,0,0,114,115,5,
  	63,0,0,115,116,5,64,0,0,116,117,5,66,0,0,117,118,5,67,0,0,118,119,5,67,
  	0,0,119,120,5,67,0,0,120,121,5,67,0,0,121,122,5,67,0,0,122,123,5,67,0,
  	0,123,124,5,67,0,0,124,125,5,67,0,0,125,126,5,67,0,0,126,127,5,67,0,0,
  	127,128,5,67,0,0,128,129,5,67,0,0,129,130,5,67,0,0,130,131,5,67,0,0,131,
  	132,5,67,0,0,132,133,5,67,0,0,133,134,5,67,0,0,134,135,5,67,0,0,135,137,
  	5,69,0,0,136,138,3,6,3,0,137,136,1,0,0,0,138,139,1,0,0,0,139,137,1,0,
  	0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,142,5,4,0,0,142,5,1,0,0,0,143,
  	144,5,7,0,0,144,145,3,56,28,0,145,146,3,56,28,0,146,147,3,56,28,0,147,
  	148,3,56,28,0,148,149,3,56,28,0,149,150,3,52,26,0,150,151,3,52,26,0,151,
  	152,3,54,27,0,152,153,3,52,26,0,153,154,3,52,26,0,154,155,3,52,26,0,155,
  	156,3,54,27,0,156,157,3,52,26,0,157,158,5,7,0,0,158,159,5,7,0,0,159,160,
  	3,58,29,0,160,161,5,7,0,0,161,162,5,17,0,0,162,7,1,0,0,0,163,164,5,1,
  	0,0,164,165,5,21,0,0,165,166,5,27,0,0,166,167,5,2,0,0,167,168,7,1,0,0,
  	168,169,5,32,0,0,169,170,5,3,0,0,170,175,5,33,0,0,171,176,3,36,18,0,172,
  	176,3,38,19,0,173,176,3,40,20,0,174,176,3,42,21,0,175,171,1,0,0,0,175,
  	172,1,0,0,0,175,173,1,0,0,0,175,174,1,0,0,0,176,177,1,0,0,0,177,178,5,
  	42,0,0,178,179,5,43,0,0,179,180,5,44,0,0,180,181,5,45,0,0,181,182,5,49,
  	0,0,182,183,5,53,0,0,183,184,5,57,0,0,184,185,5,46,0,0,185,186,5,50,0,
  	0,186,187,5,54,0,0,187,188,5,58,0,0,188,189,5,47,0,0,189,190,5,51,0,0,
  	190,191,5,55,0,0,191,192,5,59,0,0,192,193,5,61,0,0,193,194,5,62,0,0,194,
  	195,5,63,0,0,195,196,5,64,0,0,196,197,5,66,0,0,197,198,5,67,0,0,198,199,
  	5,67,0,0,199,200,5,67,0,0,200,201,5,67,0,0,201,202,5,67,0,0,202,203,5,
  	67,0,0,203,204,5,67,0,0,204,205,5,67,0,0,205,206,5,67,0,0,206,207,5,67,
  	0,0,207,208,5,67,0,0,208,209,5,67,0,0,209,210,5,67,0,0,210,211,5,67,0,
  	0,211,212,5,67,0,0,212,213,5,67,0,0,213,214,5,67,0,0,214,215,5,67,0,0,
  	215,216,5,67,0,0,216,217,5,67,0,0,217,218,5,67,0,0,218,219,5,67,0,0,219,
  	220,5,67,0,0,220,222,5,69,0,0,221,223,3,10,5,0,222,221,1,0,0,0,223,224,
  	1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,226,1,0,0,0,226,227,5,4,0,
  	0,227,9,1,0,0,0,228,229,5,7,0,0,229,230,3,56,28,0,230,231,3,56,28,0,231,
  	232,3,56,28,0,232,233,3,56,28,0,233,234,3,56,28,0,234,235,3,56,28,0,235,
  	236,3,52,26,0,236,237,3,52,26,0,237,238,3,54,27,0,238,239,3,52,26,0,239,
  	240,3,52,26,0,240,241,3,52,26,0,241,242,3,54,27,0,242,243,3,52,26,0,243,
  	244,3,52,26,0,244,245,3,52,26,0,245,246,3,54,27,0,246,247,3,52,26,0,247,
  	248,5,7,0,0,248,249,5,7,0,0,249,250,3,58,29,0,250,251,5,7,0,0,251,252,
  	5,17,0,0,252,11,1,0,0,0,253,254,5,1,0,0,254,255,5,22,0,0,255,256,5,27,
  	0,0,256,257,5,2,0,0,257,258,7,1,0,0,258,259,5,32,0,0,259,260,5,3,0,0,
  	260,265,5,33,0,0,261,266,3,44,22,0,262,266,3,46,23,0,263,266,3,48,24,
  	0,264,266,3,50,25,0,265,261,1,0,0,0,265,262,1,0,0,0,265,263,1,0,0,0,265,
  	264,1,0,0,0,266,267,1,0,0,0,267,268,5,42,0,0,268,269,5,43,0,0,269,270,
  	5,44,0,0,270,271,5,45,0,0,271,272,5,49,0,0,272,273,5,53,0,0,273,274,5,
  	57,0,0,274,275,5,46,0,0,275,276,5,50,0,0,276,277,5,54,0,0,277,278,5,58,
  	0,0,278,279,5,47,0,0,279,280,5,51,0,0,280,281,5,55,0,0,281,282,5,59,0,
  	0,282,283,5,48,0,0,283,284,5,52,0,0,284,285,5,56,0,0,285,286,5,60,0,0,
  	286,287,5,61,0,0,287,288,5,62,0,0,288,289,5,63,0,0,289,290,5,64,0,0,290,
  	291,5,66,0,0,291,292,5,67,0,0,292,293,5,67,0,0,293,294,5,67,0,0,294,295,
  	5,67,0,0,295,296,5,67,0,0,296,297,5,67,0,0,297,298,5,67,0,0,298,299,5,
  	67,0,0,299,300,5,67,0,0,300,301,5,67,0,0,301,302,5,67,0,0,302,303,5,67,
  	0,0,303,304,5,67,0,0,304,305,5,67,0,0,305,306,5,67,0,0,306,307,5,67,0,
  	0,307,308,5,67,0,0,308,309,5,67,0,0,309,310,5,67,0,0,310,311,5,67,0,0,
  	311,312,5,67,0,0,312,313,5,67,0,0,313,314,5,67,0,0,314,315,5,67,0,0,315,
  	316,5,67,0,0,316,317,5,67,0,0,317,318,5,67,0,0,318,319,5,67,0,0,319,321,
  	5,69,0,0,320,322,3,14,7,0,321,320,1,0,0,0,322,323,1,0,0,0,323,321,1,0,
  	0,0,323,324,1,0,0,0,324,325,1,0,0,0,325,326,5,4,0,0,326,13,1,0,0,0,327,
  	328,5,7,0,0,328,329,3,56,28,0,329,330,3,56,28,0,330,331,3,56,28,0,331,
  	332,3,56,28,0,332,333,3,56,28,0,333,334,3,56,28,0,334,335,3,56,28,0,335,
  	336,3,52,26,0,336,337,3,52,26,0,337,338,3,54,27,0,338,339,3,52,26,0,339,
  	340,3,52,26,0,340,341,3,52,26,0,341,342,3,54,27,0,342,343,3,52,26,0,343,
  	344,3,52,26,0,344,345,3,52,26,0,345,346,3,54,27,0,346,347,3,52,26,0,347,
  	348,3,52,26,0,348,349,3,52,26,0,349,350,3,54,27,0,350,351,3,52,26,0,351,
  	352,5,7,0,0,352,353,5,7,0,0,353,354,3,58,29,0,354,355,5,7,0,0,355,356,
  	5,17,0,0,356,15,1,0,0,0,357,358,5,1,0,0,358,359,5,23,0,0,359,360,5,27,
  	0,0,360,361,5,2,0,0,361,362,7,1,0,0,362,363,5,32,0,0,363,364,5,3,0,0,
  	364,365,5,45,0,0,365,366,5,49,0,0,366,367,5,53,0,0,367,368,5,57,0,0,368,
  	369,5,46,0,0,369,370,5,50,0,0,370,371,5,54,0,0,371,372,5,58,0,0,372,377,
  	5,33,0,0,373,378,3,28,14,0,374,378,3,30,15,0,375,378,3,32,16,0,376,378,
  	3,34,17,0,377,373,1,0,0,0,377,374,1,0,0,0,377,375,1,0,0,0,377,376,1,0,
  	0,0,378,379,1,0,0,0,379,380,5,42,0,0,380,381,5,43,0,0,381,382,5,44,0,
  	0,382,383,5,61,0,0,383,384,5,62,0,0,384,385,5,63,0,0,385,386,5,64,0,0,
  	386,387,5,66,0,0,387,388,5,67,0,0,388,389,5,67,0,0,389,390,5,67,0,0,390,
  	391,5,67,0,0,391,392,5,67,0,0,392,393,5,67,0,0,393,394,5,67,0,0,394,395,
  	5,67,0,0,395,396,5,67,0,0,396,397,5,67,0,0,397,398,5,67,0,0,398,399,5,
  	67,0,0,399,400,5,67,0,0,400,401,5,67,0,0,401,402,5,67,0,0,402,403,5,67,
  	0,0,403,404,5,67,0,0,404,405,5,67,0,0,405,407,5,69,0,0,406,408,3,18,9,
  	0,407,406,1,0,0,0,408,409,1,0,0,0,409,407,1,0,0,0,409,410,1,0,0,0,410,
  	411,1,0,0,0,411,412,5,4,0,0,412,17,1,0,0,0,413,414,3,52,26,0,414,415,
  	3,52,26,0,415,416,3,54,27,0,416,417,3,52,26,0,417,418,3,52,26,0,418,419,
  	3,52,26,0,419,420,3,54,27,0,420,421,3,52,26,0,421,422,5,7,0,0,422,423,
  	3,56,28,0,423,424,3,56,28,0,424,425,3,56,28,0,425,426,3,56,28,0,426,427,
  	3,56,28,0,427,428,5,7,0,0,428,429,5,7,0,0,429,430,3,58,29,0,430,431,5,
  	7,0,0,431,432,5,17,0,0,432,19,1,0,0,0,433,434,5,1,0,0,434,435,5,24,0,
  	0,435,436,5,27,0,0,436,437,5,2,0,0,437,438,7,1,0,0,438,439,5,32,0,0,439,
  	440,5,3,0,0,440,441,5,45,0,0,441,442,5,49,0,0,442,443,5,53,0,0,443,444,
  	5,57,0,0,444,445,5,46,0,0,445,446,5,50,0,0,446,447,5,54,0,0,447,448,5,
  	58,0,0,448,449,5,47,0,0,449,450,5,51,0,0,450,451,5,55,0,0,451,452,5,59,
  	0,0,452,457,5,33,0,0,453,458,3,36,18,0,454,458,3,38,19,0,455,458,3,40,
  	20,0,456,458,3,42,21,0,457,453,1,0,0,0,457,454,1,0,0,0,457,455,1,0,0,
  	0,457,456,1,0,0,0,458,459,1,0,0,0,459,460,5,42,0,0,460,461,5,43,0,0,461,
  	462,5,44,0,0,462,463,5,61,0,0,463,464,5,62,0,0,464,465,5,63,0,0,465,466,
  	5,64,0,0,466,467,5,66,0,0,467,468,5,67,0,0,468,469,5,67,0,0,469,470,5,
  	67,0,0,470,471,5,67,0,0,471,472,5,67,0,0,472,473,5,67,0,0,473,474,5,67,
  	0,0,474,475,5,67,0,0,475,476,5,67,0,0,476,477,5,67,0,0,477,478,5,67,0,
  	0,478,479,5,67,0,0,479,480,5,67,0,0,480,481,5,67,0,0,481,482,5,67,0,0,
  	482,483,5,67,0,0,483,484,5,67,0,0,484,485,5,67,0,0,485,486,5,67,0,0,486,
  	487,5,67,0,0,487,488,5,67,0,0,488,489,5,67,0,0,489,490,5,67,0,0,490,492,
  	5,69,0,0,491,493,3,22,11,0,492,491,1,0,0,0,493,494,1,0,0,0,494,492,1,
  	0,0,0,494,495,1,0,0,0,495,496,1,0,0,0,496,497,5,4,0,0,497,21,1,0,0,0,
  	498,499,3,52,26,0,499,500,3,52,26,0,500,501,3,54,27,0,501,502,3,52,26,
  	0,502,503,3,52,26,0,503,504,3,52,26,0,504,505,3,54,27,0,505,506,3,52,
  	26,0,506,507,3,52,26,0,507,508,3,52,26,0,508,509,3,54,27,0,509,510,3,
  	52,26,0,510,511,5,7,0,0,511,512,3,56,28,0,512,513,3,56,28,0,513,514,3,
  	56,28,0,514,515,3,56,28,0,515,516,3,56,28,0,516,517,3,56,28,0,517,518,
  	5,7,0,0,518,519,5,7,0,0,519,520,3,58,29,0,520,521,5,7,0,0,521,522,5,17,
  	0,0,522,23,1,0,0,0,523,524,5,1,0,0,524,525,5,25,0,0,525,526,5,27,0,0,
  	526,527,5,2,0,0,527,528,7,1,0,0,528,529,5,32,0,0,529,530,5,3,0,0,530,
  	531,5,45,0,0,531,532,5,49,0,0,532,533,5,53,0,0,533,534,5,57,0,0,534,535,
  	5,46,0,0,535,536,5,50,0,0,536,537,5,54,0,0,537,538,5,58,0,0,538,539,5,
  	47,0,0,539,540,5,51,0,0,540,541,5,55,0,0,541,542,5,59,0,0,542,543,5,48,
  	0,0,543,544,5,52,0,0,544,545,5,56,0,0,545,546,5,60,0,0,546,551,5,33,0,
  	0,547,552,3,44,22,0,548,552,3,46,23,0,549,552,3,48,24,0,550,552,3,50,
  	25,0,551,547,1,0,0,0,551,548,1,0,0,0,551,549,1,0,0,0,551,550,1,0,0,0,
  	552,553,1,0,0,0,553,554,5,42,0,0,554,555,5,43,0,0,555,556,5,44,0,0,556,
  	557,5,61,0,0,557,558,5,62,0,0,558,559,5,63,0,0,559,560,5,64,0,0,560,561,
  	5,66,0,0,561,562,5,67,0,0,562,563,5,67,0,0,563,564,5,67,0,0,564,565,5,
  	67,0,0,565,566,5,67,0,0,566,567,5,67,0,0,567,568,5,67,0,0,568,569,5,67,
  	0,0,569,570,5,67,0,0,570,571,5,67,0,0,571,572,5,67,0,0,572,573,5,67,0,
  	0,573,574,5,67,0,0,574,575,5,67,0,0,575,576,5,67,0,0,576,577,5,67,0,0,
  	577,578,5,67,0,0,578,579,5,67,0,0,579,580,5,67,0,0,580,581,5,67,0,0,581,
  	582,5,67,0,0,582,583,5,67,0,0,583,584,5,67,0,0,584,585,5,67,0,0,585,586,
  	5,67,0,0,586,587,5,67,0,0,587,588,5,67,0,0,588,589,5,67,0,0,589,591,5,
  	69,0,0,590,592,3,26,13,0,591,590,1,0,0,0,592,593,1,0,0,0,593,591,1,0,
  	0,0,593,594,1,0,0,0,594,595,1,0,0,0,595,596,5,4,0,0,596,25,1,0,0,0,597,
  	598,3,52,26,0,598,599,3,52,26,0,599,600,3,54,27,0,600,601,3,52,26,0,601,
  	602,3,52,26,0,602,603,3,52,26,0,603,604,3,54,27,0,604,605,3,52,26,0,605,
  	606,3,52,26,0,606,607,3,52,26,0,607,608,3,54,27,0,608,609,3,52,26,0,609,
  	610,3,52,26,0,610,611,3,52,26,0,611,612,3,54,27,0,612,613,3,52,26,0,613,
  	614,5,7,0,0,614,615,3,56,28,0,615,616,3,56,28,0,616,617,3,56,28,0,617,
  	618,3,56,28,0,618,619,3,56,28,0,619,620,3,56,28,0,620,621,3,56,28,0,621,
  	622,5,7,0,0,622,623,5,7,0,0,623,624,3,58,29,0,624,625,5,7,0,0,625,626,
  	5,17,0,0,626,27,1,0,0,0,627,628,5,34,0,0,628,629,5,35,0,0,629,29,1,0,
  	0,0,630,631,5,35,0,0,631,632,5,34,0,0,632,31,1,0,0,0,633,634,5,38,0,0,
  	634,635,5,39,0,0,635,33,1,0,0,0,636,637,5,39,0,0,637,638,5,38,0,0,638,
  	35,1,0,0,0,639,640,5,34,0,0,640,641,5,35,0,0,641,642,5,36,0,0,642,37,
  	1,0,0,0,643,644,5,36,0,0,644,645,5,35,0,0,645,646,5,34,0,0,646,39,1,0,
  	0,0,647,648,5,38,0,0,648,649,5,39,0,0,649,650,5,40,0,0,650,41,1,0,0,0,
  	651,652,5,40,0,0,652,653,5,39,0,0,653,654,5,38,0,0,654,43,1,0,0,0,655,
  	656,5,34,0,0,656,657,5,35,0,0,657,658,5,36,0,0,658,659,5,37,0,0,659,45,
  	1,0,0,0,660,661,5,37,0,0,661,662,5,36,0,0,662,663,5,35,0,0,663,664,5,
  	34,0,0,664,47,1,0,0,0,665,666,5,38,0,0,666,667,5,39,0,0,667,668,5,40,
  	0,0,668,669,5,41,0,0,669,49,1,0,0,0,670,671,5,41,0,0,671,672,5,40,0,0,
  	672,673,5,39,0,0,673,674,5,38,0,0,674,51,1,0,0,0,675,676,7,2,0,0,676,
  	53,1,0,0,0,677,678,7,3,0,0,678,55,1,0,0,0,679,680,7,4,0,0,680,57,1,0,
  	0,0,681,682,7,5,0,0,682,59,1,0,0,0,16,61,71,73,82,99,139,175,224,265,
  	323,377,409,457,494,551,593
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  oliviapkparserParserStaticData = std::move(staticData);
}

}

OliviaPKParser::OliviaPKParser(TokenStream *input) : OliviaPKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

OliviaPKParser::OliviaPKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  OliviaPKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *oliviapkparserParserStaticData->atn, oliviapkparserParserStaticData->decisionToDFA, oliviapkparserParserStaticData->sharedContextCache, options);
}

OliviaPKParser::~OliviaPKParser() {
  delete _interpreter;
}

const atn::ATN& OliviaPKParser::getATN() const {
  return *oliviapkparserParserStaticData->atn;
}

std::string OliviaPKParser::getGrammarFileName() const {
  return "OliviaPKParser.g4";
}

const std::vector<std::string>& OliviaPKParser::getRuleNames() const {
  return oliviapkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& OliviaPKParser::getVocabulary() const {
  return oliviapkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView OliviaPKParser::getSerializedATN() const {
  return oliviapkparserParserStaticData->serializedATN;
}


//----------------- Olivia_pkContext ------------------------------------------------------------------

OliviaPKParser::Olivia_pkContext::Olivia_pkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Olivia_pkContext::EOF() {
  return getToken(OliviaPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> OliviaPKParser::Olivia_pkContext::RETURN() {
  return getTokens(OliviaPKParser::RETURN);
}

tree::TerminalNode* OliviaPKParser::Olivia_pkContext::RETURN(size_t i) {
  return getToken(OliviaPKParser::RETURN, i);
}

std::vector<OliviaPKParser::CommentContext *> OliviaPKParser::Olivia_pkContext::comment() {
  return getRuleContexts<OliviaPKParser::CommentContext>();
}

OliviaPKParser::CommentContext* OliviaPKParser::Olivia_pkContext::comment(size_t i) {
  return getRuleContext<OliviaPKParser::CommentContext>(i);
}

std::vector<OliviaPKParser::Idx_peak_list_2dContext *> OliviaPKParser::Olivia_pkContext::idx_peak_list_2d() {
  return getRuleContexts<OliviaPKParser::Idx_peak_list_2dContext>();
}

OliviaPKParser::Idx_peak_list_2dContext* OliviaPKParser::Olivia_pkContext::idx_peak_list_2d(size_t i) {
  return getRuleContext<OliviaPKParser::Idx_peak_list_2dContext>(i);
}

std::vector<OliviaPKParser::Idx_peak_list_3dContext *> OliviaPKParser::Olivia_pkContext::idx_peak_list_3d() {
  return getRuleContexts<OliviaPKParser::Idx_peak_list_3dContext>();
}

OliviaPKParser::Idx_peak_list_3dContext* OliviaPKParser::Olivia_pkContext::idx_peak_list_3d(size_t i) {
  return getRuleContext<OliviaPKParser::Idx_peak_list_3dContext>(i);
}

std::vector<OliviaPKParser::Idx_peak_list_4dContext *> OliviaPKParser::Olivia_pkContext::idx_peak_list_4d() {
  return getRuleContexts<OliviaPKParser::Idx_peak_list_4dContext>();
}

OliviaPKParser::Idx_peak_list_4dContext* OliviaPKParser::Olivia_pkContext::idx_peak_list_4d(size_t i) {
  return getRuleContext<OliviaPKParser::Idx_peak_list_4dContext>(i);
}

std::vector<OliviaPKParser::Ass_peak_list_2dContext *> OliviaPKParser::Olivia_pkContext::ass_peak_list_2d() {
  return getRuleContexts<OliviaPKParser::Ass_peak_list_2dContext>();
}

OliviaPKParser::Ass_peak_list_2dContext* OliviaPKParser::Olivia_pkContext::ass_peak_list_2d(size_t i) {
  return getRuleContext<OliviaPKParser::Ass_peak_list_2dContext>(i);
}

std::vector<OliviaPKParser::Ass_peak_list_3dContext *> OliviaPKParser::Olivia_pkContext::ass_peak_list_3d() {
  return getRuleContexts<OliviaPKParser::Ass_peak_list_3dContext>();
}

OliviaPKParser::Ass_peak_list_3dContext* OliviaPKParser::Olivia_pkContext::ass_peak_list_3d(size_t i) {
  return getRuleContext<OliviaPKParser::Ass_peak_list_3dContext>(i);
}

std::vector<OliviaPKParser::Ass_peak_list_4dContext *> OliviaPKParser::Olivia_pkContext::ass_peak_list_4d() {
  return getRuleContexts<OliviaPKParser::Ass_peak_list_4dContext>();
}

OliviaPKParser::Ass_peak_list_4dContext* OliviaPKParser::Olivia_pkContext::ass_peak_list_4d(size_t i) {
  return getRuleContext<OliviaPKParser::Ass_peak_list_4dContext>(i);
}


size_t OliviaPKParser::Olivia_pkContext::getRuleIndex() const {
  return OliviaPKParser::RuleOlivia_pk;
}


std::any OliviaPKParser::Olivia_pkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitOlivia_pk(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Olivia_pkContext* OliviaPKParser::olivia_pk() {
  Olivia_pkContext *_localctx = _tracker.createInstance<Olivia_pkContext>(_ctx, getState());
  enterRule(_localctx, 0, OliviaPKParser::RuleOlivia_pk);
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
    setState(61);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(60);
      match(OliviaPKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(73);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 132098) != 0)) {
      setState(71);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(63);
        comment();
        break;
      }

      case 2: {
        setState(64);
        idx_peak_list_2d();
        break;
      }

      case 3: {
        setState(65);
        idx_peak_list_3d();
        break;
      }

      case 4: {
        setState(66);
        idx_peak_list_4d();
        break;
      }

      case 5: {
        setState(67);
        ass_peak_list_2d();
        break;
      }

      case 6: {
        setState(68);
        ass_peak_list_3d();
        break;
      }

      case 7: {
        setState(69);
        ass_peak_list_4d();
        break;
      }

      case 8: {
        setState(70);
        match(OliviaPKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(75);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(76);
    match(OliviaPKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CommentContext ------------------------------------------------------------------

OliviaPKParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::CommentContext::COMMENT() {
  return getToken(OliviaPKParser::COMMENT, 0);
}

tree::TerminalNode* OliviaPKParser::CommentContext::RETURN_CM() {
  return getToken(OliviaPKParser::RETURN_CM, 0);
}

tree::TerminalNode* OliviaPKParser::CommentContext::EOF() {
  return getToken(OliviaPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> OliviaPKParser::CommentContext::Any_name() {
  return getTokens(OliviaPKParser::Any_name);
}

tree::TerminalNode* OliviaPKParser::CommentContext::Any_name(size_t i) {
  return getToken(OliviaPKParser::Any_name, i);
}


size_t OliviaPKParser::CommentContext::getRuleIndex() const {
  return OliviaPKParser::RuleComment;
}


std::any OliviaPKParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::CommentContext* OliviaPKParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 2, OliviaPKParser::RuleComment);
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
    setState(78);
    match(OliviaPKParser::COMMENT);
    setState(82);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == OliviaPKParser::Any_name) {
      setState(79);
      match(OliviaPKParser::Any_name);
      setState(84);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(85);
    _la = _input->LA(1);
    if (!(_la == OliviaPKParser::EOF || _la == OliviaPKParser::RETURN_CM)) {
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

//----------------- Idx_peak_list_2dContext ------------------------------------------------------------------

OliviaPKParser::Idx_peak_list_2dContext::Idx_peak_list_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Typedef() {
  return getToken(OliviaPKParser::Typedef, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Idx_tbl_2d() {
  return getToken(OliviaPKParser::Idx_tbl_2d, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::RETURN_TD() {
  return getToken(OliviaPKParser::RETURN_TD, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Separator() {
  return getToken(OliviaPKParser::Separator, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::RETURN_SE() {
  return getToken(OliviaPKParser::RETURN_SE, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Format() {
  return getToken(OliviaPKParser::Format, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Index() {
  return getToken(OliviaPKParser::Index, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Amplitude() {
  return getToken(OliviaPKParser::Amplitude, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Volume() {
  return getToken(OliviaPKParser::Volume, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Vol_err() {
  return getToken(OliviaPKParser::Vol_err, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::X_chain() {
  return getToken(OliviaPKParser::X_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::X_resname() {
  return getToken(OliviaPKParser::X_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::X_seqnum() {
  return getToken(OliviaPKParser::X_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::X_assign() {
  return getToken(OliviaPKParser::X_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Y_chain() {
  return getToken(OliviaPKParser::Y_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Y_resname() {
  return getToken(OliviaPKParser::Y_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Y_seqnum() {
  return getToken(OliviaPKParser::Y_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Y_assign() {
  return getToken(OliviaPKParser::Y_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Eval() {
  return getToken(OliviaPKParser::Eval, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Status() {
  return getToken(OliviaPKParser::Status, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::User_memo() {
  return getToken(OliviaPKParser::User_memo, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Update_time() {
  return getToken(OliviaPKParser::Update_time, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::RETURN_FO() {
  return getToken(OliviaPKParser::RETURN_FO, 0);
}

std::vector<tree::TerminalNode *> OliviaPKParser::Idx_peak_list_2dContext::Printf_string() {
  return getTokens(OliviaPKParser::Printf_string);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Printf_string(size_t i) {
  return getToken(OliviaPKParser::Printf_string, i);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::RETURN_PF() {
  return getToken(OliviaPKParser::RETURN_PF, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Unformat() {
  return getToken(OliviaPKParser::Unformat, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Tab() {
  return getToken(OliviaPKParser::Tab, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Comma() {
  return getToken(OliviaPKParser::Comma, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_2dContext::Space() {
  return getToken(OliviaPKParser::Space, 0);
}

OliviaPKParser::Def_2d_axis_order_ppmContext* OliviaPKParser::Idx_peak_list_2dContext::def_2d_axis_order_ppm() {
  return getRuleContext<OliviaPKParser::Def_2d_axis_order_ppmContext>(0);
}

OliviaPKParser::Tp_2d_axis_order_ppmContext* OliviaPKParser::Idx_peak_list_2dContext::tp_2d_axis_order_ppm() {
  return getRuleContext<OliviaPKParser::Tp_2d_axis_order_ppmContext>(0);
}

OliviaPKParser::Def_2d_axis_order_hzContext* OliviaPKParser::Idx_peak_list_2dContext::def_2d_axis_order_hz() {
  return getRuleContext<OliviaPKParser::Def_2d_axis_order_hzContext>(0);
}

OliviaPKParser::Tp_2d_axis_order_hzContext* OliviaPKParser::Idx_peak_list_2dContext::tp_2d_axis_order_hz() {
  return getRuleContext<OliviaPKParser::Tp_2d_axis_order_hzContext>(0);
}

std::vector<OliviaPKParser::Idx_peak_2dContext *> OliviaPKParser::Idx_peak_list_2dContext::idx_peak_2d() {
  return getRuleContexts<OliviaPKParser::Idx_peak_2dContext>();
}

OliviaPKParser::Idx_peak_2dContext* OliviaPKParser::Idx_peak_list_2dContext::idx_peak_2d(size_t i) {
  return getRuleContext<OliviaPKParser::Idx_peak_2dContext>(i);
}


size_t OliviaPKParser::Idx_peak_list_2dContext::getRuleIndex() const {
  return OliviaPKParser::RuleIdx_peak_list_2d;
}


std::any OliviaPKParser::Idx_peak_list_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitIdx_peak_list_2d(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Idx_peak_list_2dContext* OliviaPKParser::idx_peak_list_2d() {
  Idx_peak_list_2dContext *_localctx = _tracker.createInstance<Idx_peak_list_2dContext>(_ctx, getState());
  enterRule(_localctx, 4, OliviaPKParser::RuleIdx_peak_list_2d);
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
    match(OliviaPKParser::Typedef);
    setState(88);
    match(OliviaPKParser::Idx_tbl_2d);
    setState(89);
    match(OliviaPKParser::RETURN_TD);
    setState(90);
    match(OliviaPKParser::Separator);
    setState(91);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1879048192) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(92);
    match(OliviaPKParser::RETURN_SE);
    setState(93);
    match(OliviaPKParser::Format);
    setState(94);
    match(OliviaPKParser::Index);
    setState(99);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case OliviaPKParser::X_ppm: {
        setState(95);
        def_2d_axis_order_ppm();
        break;
      }

      case OliviaPKParser::Y_ppm: {
        setState(96);
        tp_2d_axis_order_ppm();
        break;
      }

      case OliviaPKParser::X_hz: {
        setState(97);
        def_2d_axis_order_hz();
        break;
      }

      case OliviaPKParser::Y_hz: {
        setState(98);
        tp_2d_axis_order_hz();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(101);
    match(OliviaPKParser::Amplitude);
    setState(102);
    match(OliviaPKParser::Volume);
    setState(103);
    match(OliviaPKParser::Vol_err);
    setState(104);
    match(OliviaPKParser::X_chain);
    setState(105);
    match(OliviaPKParser::X_resname);
    setState(106);
    match(OliviaPKParser::X_seqnum);
    setState(107);
    match(OliviaPKParser::X_assign);
    setState(108);
    match(OliviaPKParser::Y_chain);
    setState(109);
    match(OliviaPKParser::Y_resname);
    setState(110);
    match(OliviaPKParser::Y_seqnum);
    setState(111);
    match(OliviaPKParser::Y_assign);
    setState(112);
    match(OliviaPKParser::Eval);
    setState(113);
    match(OliviaPKParser::Status);
    setState(114);
    match(OliviaPKParser::User_memo);
    setState(115);
    match(OliviaPKParser::Update_time);
    setState(116);
    match(OliviaPKParser::RETURN_FO);
    setState(117);
    match(OliviaPKParser::Printf_string);
    setState(118);
    match(OliviaPKParser::Printf_string);
    setState(119);
    match(OliviaPKParser::Printf_string);
    setState(120);
    match(OliviaPKParser::Printf_string);
    setState(121);
    match(OliviaPKParser::Printf_string);
    setState(122);
    match(OliviaPKParser::Printf_string);
    setState(123);
    match(OliviaPKParser::Printf_string);
    setState(124);
    match(OliviaPKParser::Printf_string);
    setState(125);
    match(OliviaPKParser::Printf_string);
    setState(126);
    match(OliviaPKParser::Printf_string);
    setState(127);
    match(OliviaPKParser::Printf_string);
    setState(128);
    match(OliviaPKParser::Printf_string);
    setState(129);
    match(OliviaPKParser::Printf_string);
    setState(130);
    match(OliviaPKParser::Printf_string);
    setState(131);
    match(OliviaPKParser::Printf_string);
    setState(132);
    match(OliviaPKParser::Printf_string);
    setState(133);
    match(OliviaPKParser::Printf_string);
    setState(134);
    match(OliviaPKParser::Printf_string);
    setState(135);
    match(OliviaPKParser::RETURN_PF);
    setState(137); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(136);
      idx_peak_2d();
      setState(139); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == OliviaPKParser::Integer);
    setState(141);
    match(OliviaPKParser::Unformat);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Idx_peak_2dContext ------------------------------------------------------------------

OliviaPKParser::Idx_peak_2dContext::Idx_peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> OliviaPKParser::Idx_peak_2dContext::Integer() {
  return getTokens(OliviaPKParser::Integer);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_2dContext::Integer(size_t i) {
  return getToken(OliviaPKParser::Integer, i);
}

std::vector<OliviaPKParser::NumberContext *> OliviaPKParser::Idx_peak_2dContext::number() {
  return getRuleContexts<OliviaPKParser::NumberContext>();
}

OliviaPKParser::NumberContext* OliviaPKParser::Idx_peak_2dContext::number(size_t i) {
  return getRuleContext<OliviaPKParser::NumberContext>(i);
}

std::vector<OliviaPKParser::StringContext *> OliviaPKParser::Idx_peak_2dContext::string() {
  return getRuleContexts<OliviaPKParser::StringContext>();
}

OliviaPKParser::StringContext* OliviaPKParser::Idx_peak_2dContext::string(size_t i) {
  return getRuleContext<OliviaPKParser::StringContext>(i);
}

std::vector<OliviaPKParser::IntegerContext *> OliviaPKParser::Idx_peak_2dContext::integer() {
  return getRuleContexts<OliviaPKParser::IntegerContext>();
}

OliviaPKParser::IntegerContext* OliviaPKParser::Idx_peak_2dContext::integer(size_t i) {
  return getRuleContext<OliviaPKParser::IntegerContext>(i);
}

OliviaPKParser::MemoContext* OliviaPKParser::Idx_peak_2dContext::memo() {
  return getRuleContext<OliviaPKParser::MemoContext>(0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_2dContext::RETURN() {
  return getToken(OliviaPKParser::RETURN, 0);
}


size_t OliviaPKParser::Idx_peak_2dContext::getRuleIndex() const {
  return OliviaPKParser::RuleIdx_peak_2d;
}


std::any OliviaPKParser::Idx_peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitIdx_peak_2d(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Idx_peak_2dContext* OliviaPKParser::idx_peak_2d() {
  Idx_peak_2dContext *_localctx = _tracker.createInstance<Idx_peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 6, OliviaPKParser::RuleIdx_peak_2d);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(143);
    match(OliviaPKParser::Integer);
    setState(144);
    number();
    setState(145);
    number();
    setState(146);
    number();
    setState(147);
    number();
    setState(148);
    number();
    setState(149);
    string();
    setState(150);
    string();
    setState(151);
    integer();
    setState(152);
    string();
    setState(153);
    string();
    setState(154);
    string();
    setState(155);
    integer();
    setState(156);
    string();
    setState(157);
    match(OliviaPKParser::Integer);
    setState(158);
    match(OliviaPKParser::Integer);
    setState(159);
    memo();
    setState(160);
    match(OliviaPKParser::Integer);
    setState(161);
    match(OliviaPKParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Idx_peak_list_3dContext ------------------------------------------------------------------

OliviaPKParser::Idx_peak_list_3dContext::Idx_peak_list_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Typedef() {
  return getToken(OliviaPKParser::Typedef, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Idx_tbl_3d() {
  return getToken(OliviaPKParser::Idx_tbl_3d, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::RETURN_TD() {
  return getToken(OliviaPKParser::RETURN_TD, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Separator() {
  return getToken(OliviaPKParser::Separator, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::RETURN_SE() {
  return getToken(OliviaPKParser::RETURN_SE, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Format() {
  return getToken(OliviaPKParser::Format, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Index() {
  return getToken(OliviaPKParser::Index, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Amplitude() {
  return getToken(OliviaPKParser::Amplitude, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Volume() {
  return getToken(OliviaPKParser::Volume, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Vol_err() {
  return getToken(OliviaPKParser::Vol_err, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::X_chain() {
  return getToken(OliviaPKParser::X_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::X_resname() {
  return getToken(OliviaPKParser::X_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::X_seqnum() {
  return getToken(OliviaPKParser::X_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::X_assign() {
  return getToken(OliviaPKParser::X_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Y_chain() {
  return getToken(OliviaPKParser::Y_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Y_resname() {
  return getToken(OliviaPKParser::Y_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Y_seqnum() {
  return getToken(OliviaPKParser::Y_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Y_assign() {
  return getToken(OliviaPKParser::Y_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Z_chain() {
  return getToken(OliviaPKParser::Z_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Z_resname() {
  return getToken(OliviaPKParser::Z_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Z_seqnum() {
  return getToken(OliviaPKParser::Z_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Z_assign() {
  return getToken(OliviaPKParser::Z_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Eval() {
  return getToken(OliviaPKParser::Eval, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Status() {
  return getToken(OliviaPKParser::Status, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::User_memo() {
  return getToken(OliviaPKParser::User_memo, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Update_time() {
  return getToken(OliviaPKParser::Update_time, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::RETURN_FO() {
  return getToken(OliviaPKParser::RETURN_FO, 0);
}

std::vector<tree::TerminalNode *> OliviaPKParser::Idx_peak_list_3dContext::Printf_string() {
  return getTokens(OliviaPKParser::Printf_string);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Printf_string(size_t i) {
  return getToken(OliviaPKParser::Printf_string, i);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::RETURN_PF() {
  return getToken(OliviaPKParser::RETURN_PF, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Unformat() {
  return getToken(OliviaPKParser::Unformat, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Tab() {
  return getToken(OliviaPKParser::Tab, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Comma() {
  return getToken(OliviaPKParser::Comma, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_3dContext::Space() {
  return getToken(OliviaPKParser::Space, 0);
}

OliviaPKParser::Def_3d_axis_order_ppmContext* OliviaPKParser::Idx_peak_list_3dContext::def_3d_axis_order_ppm() {
  return getRuleContext<OliviaPKParser::Def_3d_axis_order_ppmContext>(0);
}

OliviaPKParser::Tp_3d_axis_order_ppmContext* OliviaPKParser::Idx_peak_list_3dContext::tp_3d_axis_order_ppm() {
  return getRuleContext<OliviaPKParser::Tp_3d_axis_order_ppmContext>(0);
}

OliviaPKParser::Def_3d_axis_order_hzContext* OliviaPKParser::Idx_peak_list_3dContext::def_3d_axis_order_hz() {
  return getRuleContext<OliviaPKParser::Def_3d_axis_order_hzContext>(0);
}

OliviaPKParser::Tp_3d_axis_order_hzContext* OliviaPKParser::Idx_peak_list_3dContext::tp_3d_axis_order_hz() {
  return getRuleContext<OliviaPKParser::Tp_3d_axis_order_hzContext>(0);
}

std::vector<OliviaPKParser::Idx_peak_3dContext *> OliviaPKParser::Idx_peak_list_3dContext::idx_peak_3d() {
  return getRuleContexts<OliviaPKParser::Idx_peak_3dContext>();
}

OliviaPKParser::Idx_peak_3dContext* OliviaPKParser::Idx_peak_list_3dContext::idx_peak_3d(size_t i) {
  return getRuleContext<OliviaPKParser::Idx_peak_3dContext>(i);
}


size_t OliviaPKParser::Idx_peak_list_3dContext::getRuleIndex() const {
  return OliviaPKParser::RuleIdx_peak_list_3d;
}


std::any OliviaPKParser::Idx_peak_list_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitIdx_peak_list_3d(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Idx_peak_list_3dContext* OliviaPKParser::idx_peak_list_3d() {
  Idx_peak_list_3dContext *_localctx = _tracker.createInstance<Idx_peak_list_3dContext>(_ctx, getState());
  enterRule(_localctx, 8, OliviaPKParser::RuleIdx_peak_list_3d);
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
    setState(163);
    match(OliviaPKParser::Typedef);
    setState(164);
    match(OliviaPKParser::Idx_tbl_3d);
    setState(165);
    match(OliviaPKParser::RETURN_TD);
    setState(166);
    match(OliviaPKParser::Separator);
    setState(167);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1879048192) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(168);
    match(OliviaPKParser::RETURN_SE);
    setState(169);
    match(OliviaPKParser::Format);
    setState(170);
    match(OliviaPKParser::Index);
    setState(175);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case OliviaPKParser::X_ppm: {
        setState(171);
        def_3d_axis_order_ppm();
        break;
      }

      case OliviaPKParser::Z_ppm: {
        setState(172);
        tp_3d_axis_order_ppm();
        break;
      }

      case OliviaPKParser::X_hz: {
        setState(173);
        def_3d_axis_order_hz();
        break;
      }

      case OliviaPKParser::Z_hz: {
        setState(174);
        tp_3d_axis_order_hz();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(177);
    match(OliviaPKParser::Amplitude);
    setState(178);
    match(OliviaPKParser::Volume);
    setState(179);
    match(OliviaPKParser::Vol_err);
    setState(180);
    match(OliviaPKParser::X_chain);
    setState(181);
    match(OliviaPKParser::X_resname);
    setState(182);
    match(OliviaPKParser::X_seqnum);
    setState(183);
    match(OliviaPKParser::X_assign);
    setState(184);
    match(OliviaPKParser::Y_chain);
    setState(185);
    match(OliviaPKParser::Y_resname);
    setState(186);
    match(OliviaPKParser::Y_seqnum);
    setState(187);
    match(OliviaPKParser::Y_assign);
    setState(188);
    match(OliviaPKParser::Z_chain);
    setState(189);
    match(OliviaPKParser::Z_resname);
    setState(190);
    match(OliviaPKParser::Z_seqnum);
    setState(191);
    match(OliviaPKParser::Z_assign);
    setState(192);
    match(OliviaPKParser::Eval);
    setState(193);
    match(OliviaPKParser::Status);
    setState(194);
    match(OliviaPKParser::User_memo);
    setState(195);
    match(OliviaPKParser::Update_time);
    setState(196);
    match(OliviaPKParser::RETURN_FO);
    setState(197);
    match(OliviaPKParser::Printf_string);
    setState(198);
    match(OliviaPKParser::Printf_string);
    setState(199);
    match(OliviaPKParser::Printf_string);
    setState(200);
    match(OliviaPKParser::Printf_string);
    setState(201);
    match(OliviaPKParser::Printf_string);
    setState(202);
    match(OliviaPKParser::Printf_string);
    setState(203);
    match(OliviaPKParser::Printf_string);
    setState(204);
    match(OliviaPKParser::Printf_string);
    setState(205);
    match(OliviaPKParser::Printf_string);
    setState(206);
    match(OliviaPKParser::Printf_string);
    setState(207);
    match(OliviaPKParser::Printf_string);
    setState(208);
    match(OliviaPKParser::Printf_string);
    setState(209);
    match(OliviaPKParser::Printf_string);
    setState(210);
    match(OliviaPKParser::Printf_string);
    setState(211);
    match(OliviaPKParser::Printf_string);
    setState(212);
    match(OliviaPKParser::Printf_string);
    setState(213);
    match(OliviaPKParser::Printf_string);
    setState(214);
    match(OliviaPKParser::Printf_string);
    setState(215);
    match(OliviaPKParser::Printf_string);
    setState(216);
    match(OliviaPKParser::Printf_string);
    setState(217);
    match(OliviaPKParser::Printf_string);
    setState(218);
    match(OliviaPKParser::Printf_string);
    setState(219);
    match(OliviaPKParser::Printf_string);
    setState(220);
    match(OliviaPKParser::RETURN_PF);
    setState(222); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(221);
      idx_peak_3d();
      setState(224); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == OliviaPKParser::Integer);
    setState(226);
    match(OliviaPKParser::Unformat);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Idx_peak_3dContext ------------------------------------------------------------------

OliviaPKParser::Idx_peak_3dContext::Idx_peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> OliviaPKParser::Idx_peak_3dContext::Integer() {
  return getTokens(OliviaPKParser::Integer);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_3dContext::Integer(size_t i) {
  return getToken(OliviaPKParser::Integer, i);
}

std::vector<OliviaPKParser::NumberContext *> OliviaPKParser::Idx_peak_3dContext::number() {
  return getRuleContexts<OliviaPKParser::NumberContext>();
}

OliviaPKParser::NumberContext* OliviaPKParser::Idx_peak_3dContext::number(size_t i) {
  return getRuleContext<OliviaPKParser::NumberContext>(i);
}

std::vector<OliviaPKParser::StringContext *> OliviaPKParser::Idx_peak_3dContext::string() {
  return getRuleContexts<OliviaPKParser::StringContext>();
}

OliviaPKParser::StringContext* OliviaPKParser::Idx_peak_3dContext::string(size_t i) {
  return getRuleContext<OliviaPKParser::StringContext>(i);
}

std::vector<OliviaPKParser::IntegerContext *> OliviaPKParser::Idx_peak_3dContext::integer() {
  return getRuleContexts<OliviaPKParser::IntegerContext>();
}

OliviaPKParser::IntegerContext* OliviaPKParser::Idx_peak_3dContext::integer(size_t i) {
  return getRuleContext<OliviaPKParser::IntegerContext>(i);
}

OliviaPKParser::MemoContext* OliviaPKParser::Idx_peak_3dContext::memo() {
  return getRuleContext<OliviaPKParser::MemoContext>(0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_3dContext::RETURN() {
  return getToken(OliviaPKParser::RETURN, 0);
}


size_t OliviaPKParser::Idx_peak_3dContext::getRuleIndex() const {
  return OliviaPKParser::RuleIdx_peak_3d;
}


std::any OliviaPKParser::Idx_peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitIdx_peak_3d(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Idx_peak_3dContext* OliviaPKParser::idx_peak_3d() {
  Idx_peak_3dContext *_localctx = _tracker.createInstance<Idx_peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 10, OliviaPKParser::RuleIdx_peak_3d);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(228);
    match(OliviaPKParser::Integer);
    setState(229);
    number();
    setState(230);
    number();
    setState(231);
    number();
    setState(232);
    number();
    setState(233);
    number();
    setState(234);
    number();
    setState(235);
    string();
    setState(236);
    string();
    setState(237);
    integer();
    setState(238);
    string();
    setState(239);
    string();
    setState(240);
    string();
    setState(241);
    integer();
    setState(242);
    string();
    setState(243);
    string();
    setState(244);
    string();
    setState(245);
    integer();
    setState(246);
    string();
    setState(247);
    match(OliviaPKParser::Integer);
    setState(248);
    match(OliviaPKParser::Integer);
    setState(249);
    memo();
    setState(250);
    match(OliviaPKParser::Integer);
    setState(251);
    match(OliviaPKParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Idx_peak_list_4dContext ------------------------------------------------------------------

OliviaPKParser::Idx_peak_list_4dContext::Idx_peak_list_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Typedef() {
  return getToken(OliviaPKParser::Typedef, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Idx_tbl_4d() {
  return getToken(OliviaPKParser::Idx_tbl_4d, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::RETURN_TD() {
  return getToken(OliviaPKParser::RETURN_TD, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Separator() {
  return getToken(OliviaPKParser::Separator, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::RETURN_SE() {
  return getToken(OliviaPKParser::RETURN_SE, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Format() {
  return getToken(OliviaPKParser::Format, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Index() {
  return getToken(OliviaPKParser::Index, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Amplitude() {
  return getToken(OliviaPKParser::Amplitude, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Volume() {
  return getToken(OliviaPKParser::Volume, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Vol_err() {
  return getToken(OliviaPKParser::Vol_err, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::X_chain() {
  return getToken(OliviaPKParser::X_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::X_resname() {
  return getToken(OliviaPKParser::X_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::X_seqnum() {
  return getToken(OliviaPKParser::X_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::X_assign() {
  return getToken(OliviaPKParser::X_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Y_chain() {
  return getToken(OliviaPKParser::Y_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Y_resname() {
  return getToken(OliviaPKParser::Y_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Y_seqnum() {
  return getToken(OliviaPKParser::Y_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Y_assign() {
  return getToken(OliviaPKParser::Y_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Z_chain() {
  return getToken(OliviaPKParser::Z_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Z_resname() {
  return getToken(OliviaPKParser::Z_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Z_seqnum() {
  return getToken(OliviaPKParser::Z_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Z_assign() {
  return getToken(OliviaPKParser::Z_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::A_chain() {
  return getToken(OliviaPKParser::A_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::A_resname() {
  return getToken(OliviaPKParser::A_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::A_seqnum() {
  return getToken(OliviaPKParser::A_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::A_assign() {
  return getToken(OliviaPKParser::A_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Eval() {
  return getToken(OliviaPKParser::Eval, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Status() {
  return getToken(OliviaPKParser::Status, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::User_memo() {
  return getToken(OliviaPKParser::User_memo, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Update_time() {
  return getToken(OliviaPKParser::Update_time, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::RETURN_FO() {
  return getToken(OliviaPKParser::RETURN_FO, 0);
}

std::vector<tree::TerminalNode *> OliviaPKParser::Idx_peak_list_4dContext::Printf_string() {
  return getTokens(OliviaPKParser::Printf_string);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Printf_string(size_t i) {
  return getToken(OliviaPKParser::Printf_string, i);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::RETURN_PF() {
  return getToken(OliviaPKParser::RETURN_PF, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Unformat() {
  return getToken(OliviaPKParser::Unformat, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Tab() {
  return getToken(OliviaPKParser::Tab, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Comma() {
  return getToken(OliviaPKParser::Comma, 0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_list_4dContext::Space() {
  return getToken(OliviaPKParser::Space, 0);
}

OliviaPKParser::Def_4d_axis_order_ppmContext* OliviaPKParser::Idx_peak_list_4dContext::def_4d_axis_order_ppm() {
  return getRuleContext<OliviaPKParser::Def_4d_axis_order_ppmContext>(0);
}

OliviaPKParser::Tp_4d_axis_order_ppmContext* OliviaPKParser::Idx_peak_list_4dContext::tp_4d_axis_order_ppm() {
  return getRuleContext<OliviaPKParser::Tp_4d_axis_order_ppmContext>(0);
}

OliviaPKParser::Def_4d_axis_order_hzContext* OliviaPKParser::Idx_peak_list_4dContext::def_4d_axis_order_hz() {
  return getRuleContext<OliviaPKParser::Def_4d_axis_order_hzContext>(0);
}

OliviaPKParser::Tp_4d_axis_order_hzContext* OliviaPKParser::Idx_peak_list_4dContext::tp_4d_axis_order_hz() {
  return getRuleContext<OliviaPKParser::Tp_4d_axis_order_hzContext>(0);
}

std::vector<OliviaPKParser::Idx_peak_4dContext *> OliviaPKParser::Idx_peak_list_4dContext::idx_peak_4d() {
  return getRuleContexts<OliviaPKParser::Idx_peak_4dContext>();
}

OliviaPKParser::Idx_peak_4dContext* OliviaPKParser::Idx_peak_list_4dContext::idx_peak_4d(size_t i) {
  return getRuleContext<OliviaPKParser::Idx_peak_4dContext>(i);
}


size_t OliviaPKParser::Idx_peak_list_4dContext::getRuleIndex() const {
  return OliviaPKParser::RuleIdx_peak_list_4d;
}


std::any OliviaPKParser::Idx_peak_list_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitIdx_peak_list_4d(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Idx_peak_list_4dContext* OliviaPKParser::idx_peak_list_4d() {
  Idx_peak_list_4dContext *_localctx = _tracker.createInstance<Idx_peak_list_4dContext>(_ctx, getState());
  enterRule(_localctx, 12, OliviaPKParser::RuleIdx_peak_list_4d);
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
    match(OliviaPKParser::Typedef);
    setState(254);
    match(OliviaPKParser::Idx_tbl_4d);
    setState(255);
    match(OliviaPKParser::RETURN_TD);
    setState(256);
    match(OliviaPKParser::Separator);
    setState(257);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1879048192) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(258);
    match(OliviaPKParser::RETURN_SE);
    setState(259);
    match(OliviaPKParser::Format);
    setState(260);
    match(OliviaPKParser::Index);
    setState(265);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case OliviaPKParser::X_ppm: {
        setState(261);
        def_4d_axis_order_ppm();
        break;
      }

      case OliviaPKParser::A_ppm: {
        setState(262);
        tp_4d_axis_order_ppm();
        break;
      }

      case OliviaPKParser::X_hz: {
        setState(263);
        def_4d_axis_order_hz();
        break;
      }

      case OliviaPKParser::A_hz: {
        setState(264);
        tp_4d_axis_order_hz();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(267);
    match(OliviaPKParser::Amplitude);
    setState(268);
    match(OliviaPKParser::Volume);
    setState(269);
    match(OliviaPKParser::Vol_err);
    setState(270);
    match(OliviaPKParser::X_chain);
    setState(271);
    match(OliviaPKParser::X_resname);
    setState(272);
    match(OliviaPKParser::X_seqnum);
    setState(273);
    match(OliviaPKParser::X_assign);
    setState(274);
    match(OliviaPKParser::Y_chain);
    setState(275);
    match(OliviaPKParser::Y_resname);
    setState(276);
    match(OliviaPKParser::Y_seqnum);
    setState(277);
    match(OliviaPKParser::Y_assign);
    setState(278);
    match(OliviaPKParser::Z_chain);
    setState(279);
    match(OliviaPKParser::Z_resname);
    setState(280);
    match(OliviaPKParser::Z_seqnum);
    setState(281);
    match(OliviaPKParser::Z_assign);
    setState(282);
    match(OliviaPKParser::A_chain);
    setState(283);
    match(OliviaPKParser::A_resname);
    setState(284);
    match(OliviaPKParser::A_seqnum);
    setState(285);
    match(OliviaPKParser::A_assign);
    setState(286);
    match(OliviaPKParser::Eval);
    setState(287);
    match(OliviaPKParser::Status);
    setState(288);
    match(OliviaPKParser::User_memo);
    setState(289);
    match(OliviaPKParser::Update_time);
    setState(290);
    match(OliviaPKParser::RETURN_FO);
    setState(291);
    match(OliviaPKParser::Printf_string);
    setState(292);
    match(OliviaPKParser::Printf_string);
    setState(293);
    match(OliviaPKParser::Printf_string);
    setState(294);
    match(OliviaPKParser::Printf_string);
    setState(295);
    match(OliviaPKParser::Printf_string);
    setState(296);
    match(OliviaPKParser::Printf_string);
    setState(297);
    match(OliviaPKParser::Printf_string);
    setState(298);
    match(OliviaPKParser::Printf_string);
    setState(299);
    match(OliviaPKParser::Printf_string);
    setState(300);
    match(OliviaPKParser::Printf_string);
    setState(301);
    match(OliviaPKParser::Printf_string);
    setState(302);
    match(OliviaPKParser::Printf_string);
    setState(303);
    match(OliviaPKParser::Printf_string);
    setState(304);
    match(OliviaPKParser::Printf_string);
    setState(305);
    match(OliviaPKParser::Printf_string);
    setState(306);
    match(OliviaPKParser::Printf_string);
    setState(307);
    match(OliviaPKParser::Printf_string);
    setState(308);
    match(OliviaPKParser::Printf_string);
    setState(309);
    match(OliviaPKParser::Printf_string);
    setState(310);
    match(OliviaPKParser::Printf_string);
    setState(311);
    match(OliviaPKParser::Printf_string);
    setState(312);
    match(OliviaPKParser::Printf_string);
    setState(313);
    match(OliviaPKParser::Printf_string);
    setState(314);
    match(OliviaPKParser::Printf_string);
    setState(315);
    match(OliviaPKParser::Printf_string);
    setState(316);
    match(OliviaPKParser::Printf_string);
    setState(317);
    match(OliviaPKParser::Printf_string);
    setState(318);
    match(OliviaPKParser::Printf_string);
    setState(319);
    match(OliviaPKParser::RETURN_PF);
    setState(321); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(320);
      idx_peak_4d();
      setState(323); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == OliviaPKParser::Integer);
    setState(325);
    match(OliviaPKParser::Unformat);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Idx_peak_4dContext ------------------------------------------------------------------

OliviaPKParser::Idx_peak_4dContext::Idx_peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> OliviaPKParser::Idx_peak_4dContext::Integer() {
  return getTokens(OliviaPKParser::Integer);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_4dContext::Integer(size_t i) {
  return getToken(OliviaPKParser::Integer, i);
}

std::vector<OliviaPKParser::NumberContext *> OliviaPKParser::Idx_peak_4dContext::number() {
  return getRuleContexts<OliviaPKParser::NumberContext>();
}

OliviaPKParser::NumberContext* OliviaPKParser::Idx_peak_4dContext::number(size_t i) {
  return getRuleContext<OliviaPKParser::NumberContext>(i);
}

std::vector<OliviaPKParser::StringContext *> OliviaPKParser::Idx_peak_4dContext::string() {
  return getRuleContexts<OliviaPKParser::StringContext>();
}

OliviaPKParser::StringContext* OliviaPKParser::Idx_peak_4dContext::string(size_t i) {
  return getRuleContext<OliviaPKParser::StringContext>(i);
}

std::vector<OliviaPKParser::IntegerContext *> OliviaPKParser::Idx_peak_4dContext::integer() {
  return getRuleContexts<OliviaPKParser::IntegerContext>();
}

OliviaPKParser::IntegerContext* OliviaPKParser::Idx_peak_4dContext::integer(size_t i) {
  return getRuleContext<OliviaPKParser::IntegerContext>(i);
}

OliviaPKParser::MemoContext* OliviaPKParser::Idx_peak_4dContext::memo() {
  return getRuleContext<OliviaPKParser::MemoContext>(0);
}

tree::TerminalNode* OliviaPKParser::Idx_peak_4dContext::RETURN() {
  return getToken(OliviaPKParser::RETURN, 0);
}


size_t OliviaPKParser::Idx_peak_4dContext::getRuleIndex() const {
  return OliviaPKParser::RuleIdx_peak_4d;
}


std::any OliviaPKParser::Idx_peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitIdx_peak_4d(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Idx_peak_4dContext* OliviaPKParser::idx_peak_4d() {
  Idx_peak_4dContext *_localctx = _tracker.createInstance<Idx_peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 14, OliviaPKParser::RuleIdx_peak_4d);

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
    match(OliviaPKParser::Integer);
    setState(328);
    number();
    setState(329);
    number();
    setState(330);
    number();
    setState(331);
    number();
    setState(332);
    number();
    setState(333);
    number();
    setState(334);
    number();
    setState(335);
    string();
    setState(336);
    string();
    setState(337);
    integer();
    setState(338);
    string();
    setState(339);
    string();
    setState(340);
    string();
    setState(341);
    integer();
    setState(342);
    string();
    setState(343);
    string();
    setState(344);
    string();
    setState(345);
    integer();
    setState(346);
    string();
    setState(347);
    string();
    setState(348);
    string();
    setState(349);
    integer();
    setState(350);
    string();
    setState(351);
    match(OliviaPKParser::Integer);
    setState(352);
    match(OliviaPKParser::Integer);
    setState(353);
    memo();
    setState(354);
    match(OliviaPKParser::Integer);
    setState(355);
    match(OliviaPKParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ass_peak_list_2dContext ------------------------------------------------------------------

OliviaPKParser::Ass_peak_list_2dContext::Ass_peak_list_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Typedef() {
  return getToken(OliviaPKParser::Typedef, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Ass_tbl_2d() {
  return getToken(OliviaPKParser::Ass_tbl_2d, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::RETURN_TD() {
  return getToken(OliviaPKParser::RETURN_TD, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Separator() {
  return getToken(OliviaPKParser::Separator, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::RETURN_SE() {
  return getToken(OliviaPKParser::RETURN_SE, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Format() {
  return getToken(OliviaPKParser::Format, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::X_chain() {
  return getToken(OliviaPKParser::X_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::X_resname() {
  return getToken(OliviaPKParser::X_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::X_seqnum() {
  return getToken(OliviaPKParser::X_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::X_assign() {
  return getToken(OliviaPKParser::X_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Y_chain() {
  return getToken(OliviaPKParser::Y_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Y_resname() {
  return getToken(OliviaPKParser::Y_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Y_seqnum() {
  return getToken(OliviaPKParser::Y_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Y_assign() {
  return getToken(OliviaPKParser::Y_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Index() {
  return getToken(OliviaPKParser::Index, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Amplitude() {
  return getToken(OliviaPKParser::Amplitude, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Volume() {
  return getToken(OliviaPKParser::Volume, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Vol_err() {
  return getToken(OliviaPKParser::Vol_err, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Eval() {
  return getToken(OliviaPKParser::Eval, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Status() {
  return getToken(OliviaPKParser::Status, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::User_memo() {
  return getToken(OliviaPKParser::User_memo, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Update_time() {
  return getToken(OliviaPKParser::Update_time, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::RETURN_FO() {
  return getToken(OliviaPKParser::RETURN_FO, 0);
}

std::vector<tree::TerminalNode *> OliviaPKParser::Ass_peak_list_2dContext::Printf_string() {
  return getTokens(OliviaPKParser::Printf_string);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Printf_string(size_t i) {
  return getToken(OliviaPKParser::Printf_string, i);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::RETURN_PF() {
  return getToken(OliviaPKParser::RETURN_PF, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Unformat() {
  return getToken(OliviaPKParser::Unformat, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Tab() {
  return getToken(OliviaPKParser::Tab, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Comma() {
  return getToken(OliviaPKParser::Comma, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_2dContext::Space() {
  return getToken(OliviaPKParser::Space, 0);
}

OliviaPKParser::Def_2d_axis_order_ppmContext* OliviaPKParser::Ass_peak_list_2dContext::def_2d_axis_order_ppm() {
  return getRuleContext<OliviaPKParser::Def_2d_axis_order_ppmContext>(0);
}

OliviaPKParser::Tp_2d_axis_order_ppmContext* OliviaPKParser::Ass_peak_list_2dContext::tp_2d_axis_order_ppm() {
  return getRuleContext<OliviaPKParser::Tp_2d_axis_order_ppmContext>(0);
}

OliviaPKParser::Def_2d_axis_order_hzContext* OliviaPKParser::Ass_peak_list_2dContext::def_2d_axis_order_hz() {
  return getRuleContext<OliviaPKParser::Def_2d_axis_order_hzContext>(0);
}

OliviaPKParser::Tp_2d_axis_order_hzContext* OliviaPKParser::Ass_peak_list_2dContext::tp_2d_axis_order_hz() {
  return getRuleContext<OliviaPKParser::Tp_2d_axis_order_hzContext>(0);
}

std::vector<OliviaPKParser::Ass_peak_2dContext *> OliviaPKParser::Ass_peak_list_2dContext::ass_peak_2d() {
  return getRuleContexts<OliviaPKParser::Ass_peak_2dContext>();
}

OliviaPKParser::Ass_peak_2dContext* OliviaPKParser::Ass_peak_list_2dContext::ass_peak_2d(size_t i) {
  return getRuleContext<OliviaPKParser::Ass_peak_2dContext>(i);
}


size_t OliviaPKParser::Ass_peak_list_2dContext::getRuleIndex() const {
  return OliviaPKParser::RuleAss_peak_list_2d;
}


std::any OliviaPKParser::Ass_peak_list_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitAss_peak_list_2d(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Ass_peak_list_2dContext* OliviaPKParser::ass_peak_list_2d() {
  Ass_peak_list_2dContext *_localctx = _tracker.createInstance<Ass_peak_list_2dContext>(_ctx, getState());
  enterRule(_localctx, 16, OliviaPKParser::RuleAss_peak_list_2d);
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
    setState(357);
    match(OliviaPKParser::Typedef);
    setState(358);
    match(OliviaPKParser::Ass_tbl_2d);
    setState(359);
    match(OliviaPKParser::RETURN_TD);
    setState(360);
    match(OliviaPKParser::Separator);
    setState(361);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1879048192) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(362);
    match(OliviaPKParser::RETURN_SE);
    setState(363);
    match(OliviaPKParser::Format);
    setState(364);
    match(OliviaPKParser::X_chain);
    setState(365);
    match(OliviaPKParser::X_resname);
    setState(366);
    match(OliviaPKParser::X_seqnum);
    setState(367);
    match(OliviaPKParser::X_assign);
    setState(368);
    match(OliviaPKParser::Y_chain);
    setState(369);
    match(OliviaPKParser::Y_resname);
    setState(370);
    match(OliviaPKParser::Y_seqnum);
    setState(371);
    match(OliviaPKParser::Y_assign);
    setState(372);
    match(OliviaPKParser::Index);
    setState(377);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case OliviaPKParser::X_ppm: {
        setState(373);
        def_2d_axis_order_ppm();
        break;
      }

      case OliviaPKParser::Y_ppm: {
        setState(374);
        tp_2d_axis_order_ppm();
        break;
      }

      case OliviaPKParser::X_hz: {
        setState(375);
        def_2d_axis_order_hz();
        break;
      }

      case OliviaPKParser::Y_hz: {
        setState(376);
        tp_2d_axis_order_hz();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(379);
    match(OliviaPKParser::Amplitude);
    setState(380);
    match(OliviaPKParser::Volume);
    setState(381);
    match(OliviaPKParser::Vol_err);
    setState(382);
    match(OliviaPKParser::Eval);
    setState(383);
    match(OliviaPKParser::Status);
    setState(384);
    match(OliviaPKParser::User_memo);
    setState(385);
    match(OliviaPKParser::Update_time);
    setState(386);
    match(OliviaPKParser::RETURN_FO);
    setState(387);
    match(OliviaPKParser::Printf_string);
    setState(388);
    match(OliviaPKParser::Printf_string);
    setState(389);
    match(OliviaPKParser::Printf_string);
    setState(390);
    match(OliviaPKParser::Printf_string);
    setState(391);
    match(OliviaPKParser::Printf_string);
    setState(392);
    match(OliviaPKParser::Printf_string);
    setState(393);
    match(OliviaPKParser::Printf_string);
    setState(394);
    match(OliviaPKParser::Printf_string);
    setState(395);
    match(OliviaPKParser::Printf_string);
    setState(396);
    match(OliviaPKParser::Printf_string);
    setState(397);
    match(OliviaPKParser::Printf_string);
    setState(398);
    match(OliviaPKParser::Printf_string);
    setState(399);
    match(OliviaPKParser::Printf_string);
    setState(400);
    match(OliviaPKParser::Printf_string);
    setState(401);
    match(OliviaPKParser::Printf_string);
    setState(402);
    match(OliviaPKParser::Printf_string);
    setState(403);
    match(OliviaPKParser::Printf_string);
    setState(404);
    match(OliviaPKParser::Printf_string);
    setState(405);
    match(OliviaPKParser::RETURN_PF);
    setState(407); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(406);
      ass_peak_2d();
      setState(409); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == OliviaPKParser::Null_string

    || _la == OliviaPKParser::Simple_name);
    setState(411);
    match(OliviaPKParser::Unformat);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ass_peak_2dContext ------------------------------------------------------------------

OliviaPKParser::Ass_peak_2dContext::Ass_peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<OliviaPKParser::StringContext *> OliviaPKParser::Ass_peak_2dContext::string() {
  return getRuleContexts<OliviaPKParser::StringContext>();
}

OliviaPKParser::StringContext* OliviaPKParser::Ass_peak_2dContext::string(size_t i) {
  return getRuleContext<OliviaPKParser::StringContext>(i);
}

std::vector<OliviaPKParser::IntegerContext *> OliviaPKParser::Ass_peak_2dContext::integer() {
  return getRuleContexts<OliviaPKParser::IntegerContext>();
}

OliviaPKParser::IntegerContext* OliviaPKParser::Ass_peak_2dContext::integer(size_t i) {
  return getRuleContext<OliviaPKParser::IntegerContext>(i);
}

std::vector<tree::TerminalNode *> OliviaPKParser::Ass_peak_2dContext::Integer() {
  return getTokens(OliviaPKParser::Integer);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_2dContext::Integer(size_t i) {
  return getToken(OliviaPKParser::Integer, i);
}

std::vector<OliviaPKParser::NumberContext *> OliviaPKParser::Ass_peak_2dContext::number() {
  return getRuleContexts<OliviaPKParser::NumberContext>();
}

OliviaPKParser::NumberContext* OliviaPKParser::Ass_peak_2dContext::number(size_t i) {
  return getRuleContext<OliviaPKParser::NumberContext>(i);
}

OliviaPKParser::MemoContext* OliviaPKParser::Ass_peak_2dContext::memo() {
  return getRuleContext<OliviaPKParser::MemoContext>(0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_2dContext::RETURN() {
  return getToken(OliviaPKParser::RETURN, 0);
}


size_t OliviaPKParser::Ass_peak_2dContext::getRuleIndex() const {
  return OliviaPKParser::RuleAss_peak_2d;
}


std::any OliviaPKParser::Ass_peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitAss_peak_2d(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Ass_peak_2dContext* OliviaPKParser::ass_peak_2d() {
  Ass_peak_2dContext *_localctx = _tracker.createInstance<Ass_peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 18, OliviaPKParser::RuleAss_peak_2d);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(413);
    string();
    setState(414);
    string();
    setState(415);
    integer();
    setState(416);
    string();
    setState(417);
    string();
    setState(418);
    string();
    setState(419);
    integer();
    setState(420);
    string();
    setState(421);
    match(OliviaPKParser::Integer);
    setState(422);
    number();
    setState(423);
    number();
    setState(424);
    number();
    setState(425);
    number();
    setState(426);
    number();
    setState(427);
    match(OliviaPKParser::Integer);
    setState(428);
    match(OliviaPKParser::Integer);
    setState(429);
    memo();
    setState(430);
    match(OliviaPKParser::Integer);
    setState(431);
    match(OliviaPKParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ass_peak_list_3dContext ------------------------------------------------------------------

OliviaPKParser::Ass_peak_list_3dContext::Ass_peak_list_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Typedef() {
  return getToken(OliviaPKParser::Typedef, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Ass_tbl_3d() {
  return getToken(OliviaPKParser::Ass_tbl_3d, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::RETURN_TD() {
  return getToken(OliviaPKParser::RETURN_TD, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Separator() {
  return getToken(OliviaPKParser::Separator, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::RETURN_SE() {
  return getToken(OliviaPKParser::RETURN_SE, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Format() {
  return getToken(OliviaPKParser::Format, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::X_chain() {
  return getToken(OliviaPKParser::X_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::X_resname() {
  return getToken(OliviaPKParser::X_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::X_seqnum() {
  return getToken(OliviaPKParser::X_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::X_assign() {
  return getToken(OliviaPKParser::X_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Y_chain() {
  return getToken(OliviaPKParser::Y_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Y_resname() {
  return getToken(OliviaPKParser::Y_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Y_seqnum() {
  return getToken(OliviaPKParser::Y_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Y_assign() {
  return getToken(OliviaPKParser::Y_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Z_chain() {
  return getToken(OliviaPKParser::Z_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Z_resname() {
  return getToken(OliviaPKParser::Z_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Z_seqnum() {
  return getToken(OliviaPKParser::Z_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Z_assign() {
  return getToken(OliviaPKParser::Z_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Index() {
  return getToken(OliviaPKParser::Index, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Amplitude() {
  return getToken(OliviaPKParser::Amplitude, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Volume() {
  return getToken(OliviaPKParser::Volume, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Vol_err() {
  return getToken(OliviaPKParser::Vol_err, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Eval() {
  return getToken(OliviaPKParser::Eval, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Status() {
  return getToken(OliviaPKParser::Status, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::User_memo() {
  return getToken(OliviaPKParser::User_memo, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Update_time() {
  return getToken(OliviaPKParser::Update_time, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::RETURN_FO() {
  return getToken(OliviaPKParser::RETURN_FO, 0);
}

std::vector<tree::TerminalNode *> OliviaPKParser::Ass_peak_list_3dContext::Printf_string() {
  return getTokens(OliviaPKParser::Printf_string);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Printf_string(size_t i) {
  return getToken(OliviaPKParser::Printf_string, i);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::RETURN_PF() {
  return getToken(OliviaPKParser::RETURN_PF, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Unformat() {
  return getToken(OliviaPKParser::Unformat, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Tab() {
  return getToken(OliviaPKParser::Tab, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Comma() {
  return getToken(OliviaPKParser::Comma, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_3dContext::Space() {
  return getToken(OliviaPKParser::Space, 0);
}

OliviaPKParser::Def_3d_axis_order_ppmContext* OliviaPKParser::Ass_peak_list_3dContext::def_3d_axis_order_ppm() {
  return getRuleContext<OliviaPKParser::Def_3d_axis_order_ppmContext>(0);
}

OliviaPKParser::Tp_3d_axis_order_ppmContext* OliviaPKParser::Ass_peak_list_3dContext::tp_3d_axis_order_ppm() {
  return getRuleContext<OliviaPKParser::Tp_3d_axis_order_ppmContext>(0);
}

OliviaPKParser::Def_3d_axis_order_hzContext* OliviaPKParser::Ass_peak_list_3dContext::def_3d_axis_order_hz() {
  return getRuleContext<OliviaPKParser::Def_3d_axis_order_hzContext>(0);
}

OliviaPKParser::Tp_3d_axis_order_hzContext* OliviaPKParser::Ass_peak_list_3dContext::tp_3d_axis_order_hz() {
  return getRuleContext<OliviaPKParser::Tp_3d_axis_order_hzContext>(0);
}

std::vector<OliviaPKParser::Ass_peak_3dContext *> OliviaPKParser::Ass_peak_list_3dContext::ass_peak_3d() {
  return getRuleContexts<OliviaPKParser::Ass_peak_3dContext>();
}

OliviaPKParser::Ass_peak_3dContext* OliviaPKParser::Ass_peak_list_3dContext::ass_peak_3d(size_t i) {
  return getRuleContext<OliviaPKParser::Ass_peak_3dContext>(i);
}


size_t OliviaPKParser::Ass_peak_list_3dContext::getRuleIndex() const {
  return OliviaPKParser::RuleAss_peak_list_3d;
}


std::any OliviaPKParser::Ass_peak_list_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitAss_peak_list_3d(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Ass_peak_list_3dContext* OliviaPKParser::ass_peak_list_3d() {
  Ass_peak_list_3dContext *_localctx = _tracker.createInstance<Ass_peak_list_3dContext>(_ctx, getState());
  enterRule(_localctx, 20, OliviaPKParser::RuleAss_peak_list_3d);
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
    setState(433);
    match(OliviaPKParser::Typedef);
    setState(434);
    match(OliviaPKParser::Ass_tbl_3d);
    setState(435);
    match(OliviaPKParser::RETURN_TD);
    setState(436);
    match(OliviaPKParser::Separator);
    setState(437);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1879048192) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(438);
    match(OliviaPKParser::RETURN_SE);
    setState(439);
    match(OliviaPKParser::Format);
    setState(440);
    match(OliviaPKParser::X_chain);
    setState(441);
    match(OliviaPKParser::X_resname);
    setState(442);
    match(OliviaPKParser::X_seqnum);
    setState(443);
    match(OliviaPKParser::X_assign);
    setState(444);
    match(OliviaPKParser::Y_chain);
    setState(445);
    match(OliviaPKParser::Y_resname);
    setState(446);
    match(OliviaPKParser::Y_seqnum);
    setState(447);
    match(OliviaPKParser::Y_assign);
    setState(448);
    match(OliviaPKParser::Z_chain);
    setState(449);
    match(OliviaPKParser::Z_resname);
    setState(450);
    match(OliviaPKParser::Z_seqnum);
    setState(451);
    match(OliviaPKParser::Z_assign);
    setState(452);
    match(OliviaPKParser::Index);
    setState(457);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case OliviaPKParser::X_ppm: {
        setState(453);
        def_3d_axis_order_ppm();
        break;
      }

      case OliviaPKParser::Z_ppm: {
        setState(454);
        tp_3d_axis_order_ppm();
        break;
      }

      case OliviaPKParser::X_hz: {
        setState(455);
        def_3d_axis_order_hz();
        break;
      }

      case OliviaPKParser::Z_hz: {
        setState(456);
        tp_3d_axis_order_hz();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(459);
    match(OliviaPKParser::Amplitude);
    setState(460);
    match(OliviaPKParser::Volume);
    setState(461);
    match(OliviaPKParser::Vol_err);
    setState(462);
    match(OliviaPKParser::Eval);
    setState(463);
    match(OliviaPKParser::Status);
    setState(464);
    match(OliviaPKParser::User_memo);
    setState(465);
    match(OliviaPKParser::Update_time);
    setState(466);
    match(OliviaPKParser::RETURN_FO);
    setState(467);
    match(OliviaPKParser::Printf_string);
    setState(468);
    match(OliviaPKParser::Printf_string);
    setState(469);
    match(OliviaPKParser::Printf_string);
    setState(470);
    match(OliviaPKParser::Printf_string);
    setState(471);
    match(OliviaPKParser::Printf_string);
    setState(472);
    match(OliviaPKParser::Printf_string);
    setState(473);
    match(OliviaPKParser::Printf_string);
    setState(474);
    match(OliviaPKParser::Printf_string);
    setState(475);
    match(OliviaPKParser::Printf_string);
    setState(476);
    match(OliviaPKParser::Printf_string);
    setState(477);
    match(OliviaPKParser::Printf_string);
    setState(478);
    match(OliviaPKParser::Printf_string);
    setState(479);
    match(OliviaPKParser::Printf_string);
    setState(480);
    match(OliviaPKParser::Printf_string);
    setState(481);
    match(OliviaPKParser::Printf_string);
    setState(482);
    match(OliviaPKParser::Printf_string);
    setState(483);
    match(OliviaPKParser::Printf_string);
    setState(484);
    match(OliviaPKParser::Printf_string);
    setState(485);
    match(OliviaPKParser::Printf_string);
    setState(486);
    match(OliviaPKParser::Printf_string);
    setState(487);
    match(OliviaPKParser::Printf_string);
    setState(488);
    match(OliviaPKParser::Printf_string);
    setState(489);
    match(OliviaPKParser::Printf_string);
    setState(490);
    match(OliviaPKParser::RETURN_PF);
    setState(492); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(491);
      ass_peak_3d();
      setState(494); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == OliviaPKParser::Null_string

    || _la == OliviaPKParser::Simple_name);
    setState(496);
    match(OliviaPKParser::Unformat);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ass_peak_3dContext ------------------------------------------------------------------

OliviaPKParser::Ass_peak_3dContext::Ass_peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<OliviaPKParser::StringContext *> OliviaPKParser::Ass_peak_3dContext::string() {
  return getRuleContexts<OliviaPKParser::StringContext>();
}

OliviaPKParser::StringContext* OliviaPKParser::Ass_peak_3dContext::string(size_t i) {
  return getRuleContext<OliviaPKParser::StringContext>(i);
}

std::vector<OliviaPKParser::IntegerContext *> OliviaPKParser::Ass_peak_3dContext::integer() {
  return getRuleContexts<OliviaPKParser::IntegerContext>();
}

OliviaPKParser::IntegerContext* OliviaPKParser::Ass_peak_3dContext::integer(size_t i) {
  return getRuleContext<OliviaPKParser::IntegerContext>(i);
}

std::vector<tree::TerminalNode *> OliviaPKParser::Ass_peak_3dContext::Integer() {
  return getTokens(OliviaPKParser::Integer);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_3dContext::Integer(size_t i) {
  return getToken(OliviaPKParser::Integer, i);
}

std::vector<OliviaPKParser::NumberContext *> OliviaPKParser::Ass_peak_3dContext::number() {
  return getRuleContexts<OliviaPKParser::NumberContext>();
}

OliviaPKParser::NumberContext* OliviaPKParser::Ass_peak_3dContext::number(size_t i) {
  return getRuleContext<OliviaPKParser::NumberContext>(i);
}

OliviaPKParser::MemoContext* OliviaPKParser::Ass_peak_3dContext::memo() {
  return getRuleContext<OliviaPKParser::MemoContext>(0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_3dContext::RETURN() {
  return getToken(OliviaPKParser::RETURN, 0);
}


size_t OliviaPKParser::Ass_peak_3dContext::getRuleIndex() const {
  return OliviaPKParser::RuleAss_peak_3d;
}


std::any OliviaPKParser::Ass_peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitAss_peak_3d(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Ass_peak_3dContext* OliviaPKParser::ass_peak_3d() {
  Ass_peak_3dContext *_localctx = _tracker.createInstance<Ass_peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 22, OliviaPKParser::RuleAss_peak_3d);

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
    string();
    setState(499);
    string();
    setState(500);
    integer();
    setState(501);
    string();
    setState(502);
    string();
    setState(503);
    string();
    setState(504);
    integer();
    setState(505);
    string();
    setState(506);
    string();
    setState(507);
    string();
    setState(508);
    integer();
    setState(509);
    string();
    setState(510);
    match(OliviaPKParser::Integer);
    setState(511);
    number();
    setState(512);
    number();
    setState(513);
    number();
    setState(514);
    number();
    setState(515);
    number();
    setState(516);
    number();
    setState(517);
    match(OliviaPKParser::Integer);
    setState(518);
    match(OliviaPKParser::Integer);
    setState(519);
    memo();
    setState(520);
    match(OliviaPKParser::Integer);
    setState(521);
    match(OliviaPKParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ass_peak_list_4dContext ------------------------------------------------------------------

OliviaPKParser::Ass_peak_list_4dContext::Ass_peak_list_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Typedef() {
  return getToken(OliviaPKParser::Typedef, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Ass_tbl_4d() {
  return getToken(OliviaPKParser::Ass_tbl_4d, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::RETURN_TD() {
  return getToken(OliviaPKParser::RETURN_TD, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Separator() {
  return getToken(OliviaPKParser::Separator, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::RETURN_SE() {
  return getToken(OliviaPKParser::RETURN_SE, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Format() {
  return getToken(OliviaPKParser::Format, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::X_chain() {
  return getToken(OliviaPKParser::X_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::X_resname() {
  return getToken(OliviaPKParser::X_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::X_seqnum() {
  return getToken(OliviaPKParser::X_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::X_assign() {
  return getToken(OliviaPKParser::X_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Y_chain() {
  return getToken(OliviaPKParser::Y_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Y_resname() {
  return getToken(OliviaPKParser::Y_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Y_seqnum() {
  return getToken(OliviaPKParser::Y_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Y_assign() {
  return getToken(OliviaPKParser::Y_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Z_chain() {
  return getToken(OliviaPKParser::Z_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Z_resname() {
  return getToken(OliviaPKParser::Z_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Z_seqnum() {
  return getToken(OliviaPKParser::Z_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Z_assign() {
  return getToken(OliviaPKParser::Z_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::A_chain() {
  return getToken(OliviaPKParser::A_chain, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::A_resname() {
  return getToken(OliviaPKParser::A_resname, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::A_seqnum() {
  return getToken(OliviaPKParser::A_seqnum, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::A_assign() {
  return getToken(OliviaPKParser::A_assign, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Index() {
  return getToken(OliviaPKParser::Index, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Amplitude() {
  return getToken(OliviaPKParser::Amplitude, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Volume() {
  return getToken(OliviaPKParser::Volume, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Vol_err() {
  return getToken(OliviaPKParser::Vol_err, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Eval() {
  return getToken(OliviaPKParser::Eval, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Status() {
  return getToken(OliviaPKParser::Status, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::User_memo() {
  return getToken(OliviaPKParser::User_memo, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Update_time() {
  return getToken(OliviaPKParser::Update_time, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::RETURN_FO() {
  return getToken(OliviaPKParser::RETURN_FO, 0);
}

std::vector<tree::TerminalNode *> OliviaPKParser::Ass_peak_list_4dContext::Printf_string() {
  return getTokens(OliviaPKParser::Printf_string);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Printf_string(size_t i) {
  return getToken(OliviaPKParser::Printf_string, i);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::RETURN_PF() {
  return getToken(OliviaPKParser::RETURN_PF, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Unformat() {
  return getToken(OliviaPKParser::Unformat, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Tab() {
  return getToken(OliviaPKParser::Tab, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Comma() {
  return getToken(OliviaPKParser::Comma, 0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_list_4dContext::Space() {
  return getToken(OliviaPKParser::Space, 0);
}

OliviaPKParser::Def_4d_axis_order_ppmContext* OliviaPKParser::Ass_peak_list_4dContext::def_4d_axis_order_ppm() {
  return getRuleContext<OliviaPKParser::Def_4d_axis_order_ppmContext>(0);
}

OliviaPKParser::Tp_4d_axis_order_ppmContext* OliviaPKParser::Ass_peak_list_4dContext::tp_4d_axis_order_ppm() {
  return getRuleContext<OliviaPKParser::Tp_4d_axis_order_ppmContext>(0);
}

OliviaPKParser::Def_4d_axis_order_hzContext* OliviaPKParser::Ass_peak_list_4dContext::def_4d_axis_order_hz() {
  return getRuleContext<OliviaPKParser::Def_4d_axis_order_hzContext>(0);
}

OliviaPKParser::Tp_4d_axis_order_hzContext* OliviaPKParser::Ass_peak_list_4dContext::tp_4d_axis_order_hz() {
  return getRuleContext<OliviaPKParser::Tp_4d_axis_order_hzContext>(0);
}

std::vector<OliviaPKParser::Ass_peak_4dContext *> OliviaPKParser::Ass_peak_list_4dContext::ass_peak_4d() {
  return getRuleContexts<OliviaPKParser::Ass_peak_4dContext>();
}

OliviaPKParser::Ass_peak_4dContext* OliviaPKParser::Ass_peak_list_4dContext::ass_peak_4d(size_t i) {
  return getRuleContext<OliviaPKParser::Ass_peak_4dContext>(i);
}


size_t OliviaPKParser::Ass_peak_list_4dContext::getRuleIndex() const {
  return OliviaPKParser::RuleAss_peak_list_4d;
}


std::any OliviaPKParser::Ass_peak_list_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitAss_peak_list_4d(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Ass_peak_list_4dContext* OliviaPKParser::ass_peak_list_4d() {
  Ass_peak_list_4dContext *_localctx = _tracker.createInstance<Ass_peak_list_4dContext>(_ctx, getState());
  enterRule(_localctx, 24, OliviaPKParser::RuleAss_peak_list_4d);
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
    setState(523);
    match(OliviaPKParser::Typedef);
    setState(524);
    match(OliviaPKParser::Ass_tbl_4d);
    setState(525);
    match(OliviaPKParser::RETURN_TD);
    setState(526);
    match(OliviaPKParser::Separator);
    setState(527);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1879048192) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(528);
    match(OliviaPKParser::RETURN_SE);
    setState(529);
    match(OliviaPKParser::Format);
    setState(530);
    match(OliviaPKParser::X_chain);
    setState(531);
    match(OliviaPKParser::X_resname);
    setState(532);
    match(OliviaPKParser::X_seqnum);
    setState(533);
    match(OliviaPKParser::X_assign);
    setState(534);
    match(OliviaPKParser::Y_chain);
    setState(535);
    match(OliviaPKParser::Y_resname);
    setState(536);
    match(OliviaPKParser::Y_seqnum);
    setState(537);
    match(OliviaPKParser::Y_assign);
    setState(538);
    match(OliviaPKParser::Z_chain);
    setState(539);
    match(OliviaPKParser::Z_resname);
    setState(540);
    match(OliviaPKParser::Z_seqnum);
    setState(541);
    match(OliviaPKParser::Z_assign);
    setState(542);
    match(OliviaPKParser::A_chain);
    setState(543);
    match(OliviaPKParser::A_resname);
    setState(544);
    match(OliviaPKParser::A_seqnum);
    setState(545);
    match(OliviaPKParser::A_assign);
    setState(546);
    match(OliviaPKParser::Index);
    setState(551);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case OliviaPKParser::X_ppm: {
        setState(547);
        def_4d_axis_order_ppm();
        break;
      }

      case OliviaPKParser::A_ppm: {
        setState(548);
        tp_4d_axis_order_ppm();
        break;
      }

      case OliviaPKParser::X_hz: {
        setState(549);
        def_4d_axis_order_hz();
        break;
      }

      case OliviaPKParser::A_hz: {
        setState(550);
        tp_4d_axis_order_hz();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(553);
    match(OliviaPKParser::Amplitude);
    setState(554);
    match(OliviaPKParser::Volume);
    setState(555);
    match(OliviaPKParser::Vol_err);
    setState(556);
    match(OliviaPKParser::Eval);
    setState(557);
    match(OliviaPKParser::Status);
    setState(558);
    match(OliviaPKParser::User_memo);
    setState(559);
    match(OliviaPKParser::Update_time);
    setState(560);
    match(OliviaPKParser::RETURN_FO);
    setState(561);
    match(OliviaPKParser::Printf_string);
    setState(562);
    match(OliviaPKParser::Printf_string);
    setState(563);
    match(OliviaPKParser::Printf_string);
    setState(564);
    match(OliviaPKParser::Printf_string);
    setState(565);
    match(OliviaPKParser::Printf_string);
    setState(566);
    match(OliviaPKParser::Printf_string);
    setState(567);
    match(OliviaPKParser::Printf_string);
    setState(568);
    match(OliviaPKParser::Printf_string);
    setState(569);
    match(OliviaPKParser::Printf_string);
    setState(570);
    match(OliviaPKParser::Printf_string);
    setState(571);
    match(OliviaPKParser::Printf_string);
    setState(572);
    match(OliviaPKParser::Printf_string);
    setState(573);
    match(OliviaPKParser::Printf_string);
    setState(574);
    match(OliviaPKParser::Printf_string);
    setState(575);
    match(OliviaPKParser::Printf_string);
    setState(576);
    match(OliviaPKParser::Printf_string);
    setState(577);
    match(OliviaPKParser::Printf_string);
    setState(578);
    match(OliviaPKParser::Printf_string);
    setState(579);
    match(OliviaPKParser::Printf_string);
    setState(580);
    match(OliviaPKParser::Printf_string);
    setState(581);
    match(OliviaPKParser::Printf_string);
    setState(582);
    match(OliviaPKParser::Printf_string);
    setState(583);
    match(OliviaPKParser::Printf_string);
    setState(584);
    match(OliviaPKParser::Printf_string);
    setState(585);
    match(OliviaPKParser::Printf_string);
    setState(586);
    match(OliviaPKParser::Printf_string);
    setState(587);
    match(OliviaPKParser::Printf_string);
    setState(588);
    match(OliviaPKParser::Printf_string);
    setState(589);
    match(OliviaPKParser::RETURN_PF);
    setState(591); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(590);
      ass_peak_4d();
      setState(593); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == OliviaPKParser::Null_string

    || _la == OliviaPKParser::Simple_name);
    setState(595);
    match(OliviaPKParser::Unformat);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ass_peak_4dContext ------------------------------------------------------------------

OliviaPKParser::Ass_peak_4dContext::Ass_peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<OliviaPKParser::StringContext *> OliviaPKParser::Ass_peak_4dContext::string() {
  return getRuleContexts<OliviaPKParser::StringContext>();
}

OliviaPKParser::StringContext* OliviaPKParser::Ass_peak_4dContext::string(size_t i) {
  return getRuleContext<OliviaPKParser::StringContext>(i);
}

std::vector<OliviaPKParser::IntegerContext *> OliviaPKParser::Ass_peak_4dContext::integer() {
  return getRuleContexts<OliviaPKParser::IntegerContext>();
}

OliviaPKParser::IntegerContext* OliviaPKParser::Ass_peak_4dContext::integer(size_t i) {
  return getRuleContext<OliviaPKParser::IntegerContext>(i);
}

std::vector<tree::TerminalNode *> OliviaPKParser::Ass_peak_4dContext::Integer() {
  return getTokens(OliviaPKParser::Integer);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_4dContext::Integer(size_t i) {
  return getToken(OliviaPKParser::Integer, i);
}

std::vector<OliviaPKParser::NumberContext *> OliviaPKParser::Ass_peak_4dContext::number() {
  return getRuleContexts<OliviaPKParser::NumberContext>();
}

OliviaPKParser::NumberContext* OliviaPKParser::Ass_peak_4dContext::number(size_t i) {
  return getRuleContext<OliviaPKParser::NumberContext>(i);
}

OliviaPKParser::MemoContext* OliviaPKParser::Ass_peak_4dContext::memo() {
  return getRuleContext<OliviaPKParser::MemoContext>(0);
}

tree::TerminalNode* OliviaPKParser::Ass_peak_4dContext::RETURN() {
  return getToken(OliviaPKParser::RETURN, 0);
}


size_t OliviaPKParser::Ass_peak_4dContext::getRuleIndex() const {
  return OliviaPKParser::RuleAss_peak_4d;
}


std::any OliviaPKParser::Ass_peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitAss_peak_4d(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Ass_peak_4dContext* OliviaPKParser::ass_peak_4d() {
  Ass_peak_4dContext *_localctx = _tracker.createInstance<Ass_peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 26, OliviaPKParser::RuleAss_peak_4d);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(597);
    string();
    setState(598);
    string();
    setState(599);
    integer();
    setState(600);
    string();
    setState(601);
    string();
    setState(602);
    string();
    setState(603);
    integer();
    setState(604);
    string();
    setState(605);
    string();
    setState(606);
    string();
    setState(607);
    integer();
    setState(608);
    string();
    setState(609);
    string();
    setState(610);
    string();
    setState(611);
    integer();
    setState(612);
    string();
    setState(613);
    match(OliviaPKParser::Integer);
    setState(614);
    number();
    setState(615);
    number();
    setState(616);
    number();
    setState(617);
    number();
    setState(618);
    number();
    setState(619);
    number();
    setState(620);
    number();
    setState(621);
    match(OliviaPKParser::Integer);
    setState(622);
    match(OliviaPKParser::Integer);
    setState(623);
    memo();
    setState(624);
    match(OliviaPKParser::Integer);
    setState(625);
    match(OliviaPKParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Def_2d_axis_order_ppmContext ------------------------------------------------------------------

OliviaPKParser::Def_2d_axis_order_ppmContext::Def_2d_axis_order_ppmContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Def_2d_axis_order_ppmContext::X_ppm() {
  return getToken(OliviaPKParser::X_ppm, 0);
}

tree::TerminalNode* OliviaPKParser::Def_2d_axis_order_ppmContext::Y_ppm() {
  return getToken(OliviaPKParser::Y_ppm, 0);
}


size_t OliviaPKParser::Def_2d_axis_order_ppmContext::getRuleIndex() const {
  return OliviaPKParser::RuleDef_2d_axis_order_ppm;
}


std::any OliviaPKParser::Def_2d_axis_order_ppmContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitDef_2d_axis_order_ppm(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Def_2d_axis_order_ppmContext* OliviaPKParser::def_2d_axis_order_ppm() {
  Def_2d_axis_order_ppmContext *_localctx = _tracker.createInstance<Def_2d_axis_order_ppmContext>(_ctx, getState());
  enterRule(_localctx, 28, OliviaPKParser::RuleDef_2d_axis_order_ppm);

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
    match(OliviaPKParser::X_ppm);
    setState(628);
    match(OliviaPKParser::Y_ppm);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Tp_2d_axis_order_ppmContext ------------------------------------------------------------------

OliviaPKParser::Tp_2d_axis_order_ppmContext::Tp_2d_axis_order_ppmContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Tp_2d_axis_order_ppmContext::Y_ppm() {
  return getToken(OliviaPKParser::Y_ppm, 0);
}

tree::TerminalNode* OliviaPKParser::Tp_2d_axis_order_ppmContext::X_ppm() {
  return getToken(OliviaPKParser::X_ppm, 0);
}


size_t OliviaPKParser::Tp_2d_axis_order_ppmContext::getRuleIndex() const {
  return OliviaPKParser::RuleTp_2d_axis_order_ppm;
}


std::any OliviaPKParser::Tp_2d_axis_order_ppmContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitTp_2d_axis_order_ppm(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Tp_2d_axis_order_ppmContext* OliviaPKParser::tp_2d_axis_order_ppm() {
  Tp_2d_axis_order_ppmContext *_localctx = _tracker.createInstance<Tp_2d_axis_order_ppmContext>(_ctx, getState());
  enterRule(_localctx, 30, OliviaPKParser::RuleTp_2d_axis_order_ppm);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(630);
    match(OliviaPKParser::Y_ppm);
    setState(631);
    match(OliviaPKParser::X_ppm);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Def_2d_axis_order_hzContext ------------------------------------------------------------------

OliviaPKParser::Def_2d_axis_order_hzContext::Def_2d_axis_order_hzContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Def_2d_axis_order_hzContext::X_hz() {
  return getToken(OliviaPKParser::X_hz, 0);
}

tree::TerminalNode* OliviaPKParser::Def_2d_axis_order_hzContext::Y_hz() {
  return getToken(OliviaPKParser::Y_hz, 0);
}


size_t OliviaPKParser::Def_2d_axis_order_hzContext::getRuleIndex() const {
  return OliviaPKParser::RuleDef_2d_axis_order_hz;
}


std::any OliviaPKParser::Def_2d_axis_order_hzContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitDef_2d_axis_order_hz(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Def_2d_axis_order_hzContext* OliviaPKParser::def_2d_axis_order_hz() {
  Def_2d_axis_order_hzContext *_localctx = _tracker.createInstance<Def_2d_axis_order_hzContext>(_ctx, getState());
  enterRule(_localctx, 32, OliviaPKParser::RuleDef_2d_axis_order_hz);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(633);
    match(OliviaPKParser::X_hz);
    setState(634);
    match(OliviaPKParser::Y_hz);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Tp_2d_axis_order_hzContext ------------------------------------------------------------------

OliviaPKParser::Tp_2d_axis_order_hzContext::Tp_2d_axis_order_hzContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Tp_2d_axis_order_hzContext::Y_hz() {
  return getToken(OliviaPKParser::Y_hz, 0);
}

tree::TerminalNode* OliviaPKParser::Tp_2d_axis_order_hzContext::X_hz() {
  return getToken(OliviaPKParser::X_hz, 0);
}


size_t OliviaPKParser::Tp_2d_axis_order_hzContext::getRuleIndex() const {
  return OliviaPKParser::RuleTp_2d_axis_order_hz;
}


std::any OliviaPKParser::Tp_2d_axis_order_hzContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitTp_2d_axis_order_hz(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Tp_2d_axis_order_hzContext* OliviaPKParser::tp_2d_axis_order_hz() {
  Tp_2d_axis_order_hzContext *_localctx = _tracker.createInstance<Tp_2d_axis_order_hzContext>(_ctx, getState());
  enterRule(_localctx, 34, OliviaPKParser::RuleTp_2d_axis_order_hz);

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
    match(OliviaPKParser::Y_hz);
    setState(637);
    match(OliviaPKParser::X_hz);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Def_3d_axis_order_ppmContext ------------------------------------------------------------------

OliviaPKParser::Def_3d_axis_order_ppmContext::Def_3d_axis_order_ppmContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Def_3d_axis_order_ppmContext::X_ppm() {
  return getToken(OliviaPKParser::X_ppm, 0);
}

tree::TerminalNode* OliviaPKParser::Def_3d_axis_order_ppmContext::Y_ppm() {
  return getToken(OliviaPKParser::Y_ppm, 0);
}

tree::TerminalNode* OliviaPKParser::Def_3d_axis_order_ppmContext::Z_ppm() {
  return getToken(OliviaPKParser::Z_ppm, 0);
}


size_t OliviaPKParser::Def_3d_axis_order_ppmContext::getRuleIndex() const {
  return OliviaPKParser::RuleDef_3d_axis_order_ppm;
}


std::any OliviaPKParser::Def_3d_axis_order_ppmContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitDef_3d_axis_order_ppm(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Def_3d_axis_order_ppmContext* OliviaPKParser::def_3d_axis_order_ppm() {
  Def_3d_axis_order_ppmContext *_localctx = _tracker.createInstance<Def_3d_axis_order_ppmContext>(_ctx, getState());
  enterRule(_localctx, 36, OliviaPKParser::RuleDef_3d_axis_order_ppm);

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
    match(OliviaPKParser::X_ppm);
    setState(640);
    match(OliviaPKParser::Y_ppm);
    setState(641);
    match(OliviaPKParser::Z_ppm);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Tp_3d_axis_order_ppmContext ------------------------------------------------------------------

OliviaPKParser::Tp_3d_axis_order_ppmContext::Tp_3d_axis_order_ppmContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Tp_3d_axis_order_ppmContext::Z_ppm() {
  return getToken(OliviaPKParser::Z_ppm, 0);
}

tree::TerminalNode* OliviaPKParser::Tp_3d_axis_order_ppmContext::Y_ppm() {
  return getToken(OliviaPKParser::Y_ppm, 0);
}

tree::TerminalNode* OliviaPKParser::Tp_3d_axis_order_ppmContext::X_ppm() {
  return getToken(OliviaPKParser::X_ppm, 0);
}


size_t OliviaPKParser::Tp_3d_axis_order_ppmContext::getRuleIndex() const {
  return OliviaPKParser::RuleTp_3d_axis_order_ppm;
}


std::any OliviaPKParser::Tp_3d_axis_order_ppmContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitTp_3d_axis_order_ppm(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Tp_3d_axis_order_ppmContext* OliviaPKParser::tp_3d_axis_order_ppm() {
  Tp_3d_axis_order_ppmContext *_localctx = _tracker.createInstance<Tp_3d_axis_order_ppmContext>(_ctx, getState());
  enterRule(_localctx, 38, OliviaPKParser::RuleTp_3d_axis_order_ppm);

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
    match(OliviaPKParser::Z_ppm);
    setState(644);
    match(OliviaPKParser::Y_ppm);
    setState(645);
    match(OliviaPKParser::X_ppm);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Def_3d_axis_order_hzContext ------------------------------------------------------------------

OliviaPKParser::Def_3d_axis_order_hzContext::Def_3d_axis_order_hzContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Def_3d_axis_order_hzContext::X_hz() {
  return getToken(OliviaPKParser::X_hz, 0);
}

tree::TerminalNode* OliviaPKParser::Def_3d_axis_order_hzContext::Y_hz() {
  return getToken(OliviaPKParser::Y_hz, 0);
}

tree::TerminalNode* OliviaPKParser::Def_3d_axis_order_hzContext::Z_hz() {
  return getToken(OliviaPKParser::Z_hz, 0);
}


size_t OliviaPKParser::Def_3d_axis_order_hzContext::getRuleIndex() const {
  return OliviaPKParser::RuleDef_3d_axis_order_hz;
}


std::any OliviaPKParser::Def_3d_axis_order_hzContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitDef_3d_axis_order_hz(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Def_3d_axis_order_hzContext* OliviaPKParser::def_3d_axis_order_hz() {
  Def_3d_axis_order_hzContext *_localctx = _tracker.createInstance<Def_3d_axis_order_hzContext>(_ctx, getState());
  enterRule(_localctx, 40, OliviaPKParser::RuleDef_3d_axis_order_hz);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(647);
    match(OliviaPKParser::X_hz);
    setState(648);
    match(OliviaPKParser::Y_hz);
    setState(649);
    match(OliviaPKParser::Z_hz);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Tp_3d_axis_order_hzContext ------------------------------------------------------------------

OliviaPKParser::Tp_3d_axis_order_hzContext::Tp_3d_axis_order_hzContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Tp_3d_axis_order_hzContext::Z_hz() {
  return getToken(OliviaPKParser::Z_hz, 0);
}

tree::TerminalNode* OliviaPKParser::Tp_3d_axis_order_hzContext::Y_hz() {
  return getToken(OliviaPKParser::Y_hz, 0);
}

tree::TerminalNode* OliviaPKParser::Tp_3d_axis_order_hzContext::X_hz() {
  return getToken(OliviaPKParser::X_hz, 0);
}


size_t OliviaPKParser::Tp_3d_axis_order_hzContext::getRuleIndex() const {
  return OliviaPKParser::RuleTp_3d_axis_order_hz;
}


std::any OliviaPKParser::Tp_3d_axis_order_hzContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitTp_3d_axis_order_hz(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Tp_3d_axis_order_hzContext* OliviaPKParser::tp_3d_axis_order_hz() {
  Tp_3d_axis_order_hzContext *_localctx = _tracker.createInstance<Tp_3d_axis_order_hzContext>(_ctx, getState());
  enterRule(_localctx, 42, OliviaPKParser::RuleTp_3d_axis_order_hz);

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
    match(OliviaPKParser::Z_hz);
    setState(652);
    match(OliviaPKParser::Y_hz);
    setState(653);
    match(OliviaPKParser::X_hz);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Def_4d_axis_order_ppmContext ------------------------------------------------------------------

OliviaPKParser::Def_4d_axis_order_ppmContext::Def_4d_axis_order_ppmContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Def_4d_axis_order_ppmContext::X_ppm() {
  return getToken(OliviaPKParser::X_ppm, 0);
}

tree::TerminalNode* OliviaPKParser::Def_4d_axis_order_ppmContext::Y_ppm() {
  return getToken(OliviaPKParser::Y_ppm, 0);
}

tree::TerminalNode* OliviaPKParser::Def_4d_axis_order_ppmContext::Z_ppm() {
  return getToken(OliviaPKParser::Z_ppm, 0);
}

tree::TerminalNode* OliviaPKParser::Def_4d_axis_order_ppmContext::A_ppm() {
  return getToken(OliviaPKParser::A_ppm, 0);
}


size_t OliviaPKParser::Def_4d_axis_order_ppmContext::getRuleIndex() const {
  return OliviaPKParser::RuleDef_4d_axis_order_ppm;
}


std::any OliviaPKParser::Def_4d_axis_order_ppmContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitDef_4d_axis_order_ppm(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Def_4d_axis_order_ppmContext* OliviaPKParser::def_4d_axis_order_ppm() {
  Def_4d_axis_order_ppmContext *_localctx = _tracker.createInstance<Def_4d_axis_order_ppmContext>(_ctx, getState());
  enterRule(_localctx, 44, OliviaPKParser::RuleDef_4d_axis_order_ppm);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(655);
    match(OliviaPKParser::X_ppm);
    setState(656);
    match(OliviaPKParser::Y_ppm);
    setState(657);
    match(OliviaPKParser::Z_ppm);
    setState(658);
    match(OliviaPKParser::A_ppm);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Tp_4d_axis_order_ppmContext ------------------------------------------------------------------

OliviaPKParser::Tp_4d_axis_order_ppmContext::Tp_4d_axis_order_ppmContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Tp_4d_axis_order_ppmContext::A_ppm() {
  return getToken(OliviaPKParser::A_ppm, 0);
}

tree::TerminalNode* OliviaPKParser::Tp_4d_axis_order_ppmContext::Z_ppm() {
  return getToken(OliviaPKParser::Z_ppm, 0);
}

tree::TerminalNode* OliviaPKParser::Tp_4d_axis_order_ppmContext::Y_ppm() {
  return getToken(OliviaPKParser::Y_ppm, 0);
}

tree::TerminalNode* OliviaPKParser::Tp_4d_axis_order_ppmContext::X_ppm() {
  return getToken(OliviaPKParser::X_ppm, 0);
}


size_t OliviaPKParser::Tp_4d_axis_order_ppmContext::getRuleIndex() const {
  return OliviaPKParser::RuleTp_4d_axis_order_ppm;
}


std::any OliviaPKParser::Tp_4d_axis_order_ppmContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitTp_4d_axis_order_ppm(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Tp_4d_axis_order_ppmContext* OliviaPKParser::tp_4d_axis_order_ppm() {
  Tp_4d_axis_order_ppmContext *_localctx = _tracker.createInstance<Tp_4d_axis_order_ppmContext>(_ctx, getState());
  enterRule(_localctx, 46, OliviaPKParser::RuleTp_4d_axis_order_ppm);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(660);
    match(OliviaPKParser::A_ppm);
    setState(661);
    match(OliviaPKParser::Z_ppm);
    setState(662);
    match(OliviaPKParser::Y_ppm);
    setState(663);
    match(OliviaPKParser::X_ppm);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Def_4d_axis_order_hzContext ------------------------------------------------------------------

OliviaPKParser::Def_4d_axis_order_hzContext::Def_4d_axis_order_hzContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Def_4d_axis_order_hzContext::X_hz() {
  return getToken(OliviaPKParser::X_hz, 0);
}

tree::TerminalNode* OliviaPKParser::Def_4d_axis_order_hzContext::Y_hz() {
  return getToken(OliviaPKParser::Y_hz, 0);
}

tree::TerminalNode* OliviaPKParser::Def_4d_axis_order_hzContext::Z_hz() {
  return getToken(OliviaPKParser::Z_hz, 0);
}

tree::TerminalNode* OliviaPKParser::Def_4d_axis_order_hzContext::A_hz() {
  return getToken(OliviaPKParser::A_hz, 0);
}


size_t OliviaPKParser::Def_4d_axis_order_hzContext::getRuleIndex() const {
  return OliviaPKParser::RuleDef_4d_axis_order_hz;
}


std::any OliviaPKParser::Def_4d_axis_order_hzContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitDef_4d_axis_order_hz(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Def_4d_axis_order_hzContext* OliviaPKParser::def_4d_axis_order_hz() {
  Def_4d_axis_order_hzContext *_localctx = _tracker.createInstance<Def_4d_axis_order_hzContext>(_ctx, getState());
  enterRule(_localctx, 48, OliviaPKParser::RuleDef_4d_axis_order_hz);

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
    match(OliviaPKParser::X_hz);
    setState(666);
    match(OliviaPKParser::Y_hz);
    setState(667);
    match(OliviaPKParser::Z_hz);
    setState(668);
    match(OliviaPKParser::A_hz);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Tp_4d_axis_order_hzContext ------------------------------------------------------------------

OliviaPKParser::Tp_4d_axis_order_hzContext::Tp_4d_axis_order_hzContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::Tp_4d_axis_order_hzContext::A_hz() {
  return getToken(OliviaPKParser::A_hz, 0);
}

tree::TerminalNode* OliviaPKParser::Tp_4d_axis_order_hzContext::Z_hz() {
  return getToken(OliviaPKParser::Z_hz, 0);
}

tree::TerminalNode* OliviaPKParser::Tp_4d_axis_order_hzContext::Y_hz() {
  return getToken(OliviaPKParser::Y_hz, 0);
}

tree::TerminalNode* OliviaPKParser::Tp_4d_axis_order_hzContext::X_hz() {
  return getToken(OliviaPKParser::X_hz, 0);
}


size_t OliviaPKParser::Tp_4d_axis_order_hzContext::getRuleIndex() const {
  return OliviaPKParser::RuleTp_4d_axis_order_hz;
}


std::any OliviaPKParser::Tp_4d_axis_order_hzContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitTp_4d_axis_order_hz(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::Tp_4d_axis_order_hzContext* OliviaPKParser::tp_4d_axis_order_hz() {
  Tp_4d_axis_order_hzContext *_localctx = _tracker.createInstance<Tp_4d_axis_order_hzContext>(_ctx, getState());
  enterRule(_localctx, 50, OliviaPKParser::RuleTp_4d_axis_order_hz);

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
    match(OliviaPKParser::A_hz);
    setState(671);
    match(OliviaPKParser::Z_hz);
    setState(672);
    match(OliviaPKParser::Y_hz);
    setState(673);
    match(OliviaPKParser::X_hz);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StringContext ------------------------------------------------------------------

OliviaPKParser::StringContext::StringContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::StringContext::Simple_name() {
  return getToken(OliviaPKParser::Simple_name, 0);
}

tree::TerminalNode* OliviaPKParser::StringContext::Null_string() {
  return getToken(OliviaPKParser::Null_string, 0);
}


size_t OliviaPKParser::StringContext::getRuleIndex() const {
  return OliviaPKParser::RuleString;
}


std::any OliviaPKParser::StringContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitString(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::StringContext* OliviaPKParser::string() {
  StringContext *_localctx = _tracker.createInstance<StringContext>(_ctx, getState());
  enterRule(_localctx, 52, OliviaPKParser::RuleString);
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
    setState(675);
    _la = _input->LA(1);
    if (!(_la == OliviaPKParser::Null_string

    || _la == OliviaPKParser::Simple_name)) {
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

//----------------- IntegerContext ------------------------------------------------------------------

OliviaPKParser::IntegerContext::IntegerContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::IntegerContext::Integer() {
  return getToken(OliviaPKParser::Integer, 0);
}

tree::TerminalNode* OliviaPKParser::IntegerContext::Null_string() {
  return getToken(OliviaPKParser::Null_string, 0);
}


size_t OliviaPKParser::IntegerContext::getRuleIndex() const {
  return OliviaPKParser::RuleInteger;
}


std::any OliviaPKParser::IntegerContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitInteger(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::IntegerContext* OliviaPKParser::integer() {
  IntegerContext *_localctx = _tracker.createInstance<IntegerContext>(_ctx, getState());
  enterRule(_localctx, 54, OliviaPKParser::RuleInteger);
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
    setState(677);
    _la = _input->LA(1);
    if (!(_la == OliviaPKParser::Null_string

    || _la == OliviaPKParser::Integer)) {
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

OliviaPKParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::NumberContext::Integer() {
  return getToken(OliviaPKParser::Integer, 0);
}

tree::TerminalNode* OliviaPKParser::NumberContext::Float() {
  return getToken(OliviaPKParser::Float, 0);
}

tree::TerminalNode* OliviaPKParser::NumberContext::Real() {
  return getToken(OliviaPKParser::Real, 0);
}


size_t OliviaPKParser::NumberContext::getRuleIndex() const {
  return OliviaPKParser::RuleNumber;
}


std::any OliviaPKParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::NumberContext* OliviaPKParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 56, OliviaPKParser::RuleNumber);
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
    setState(679);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 896) != 0))) {
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

//----------------- MemoContext ------------------------------------------------------------------

OliviaPKParser::MemoContext::MemoContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaPKParser::MemoContext::Double_quote_string() {
  return getToken(OliviaPKParser::Double_quote_string, 0);
}

tree::TerminalNode* OliviaPKParser::MemoContext::Single_quote_string() {
  return getToken(OliviaPKParser::Single_quote_string, 0);
}

tree::TerminalNode* OliviaPKParser::MemoContext::Simple_name() {
  return getToken(OliviaPKParser::Simple_name, 0);
}


size_t OliviaPKParser::MemoContext::getRuleIndex() const {
  return OliviaPKParser::RuleMemo;
}


std::any OliviaPKParser::MemoContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaPKParserVisitor*>(visitor))
    return parserVisitor->visitMemo(this);
  else
    return visitor->visitChildren(this);
}

OliviaPKParser::MemoContext* OliviaPKParser::memo() {
  MemoContext *_localctx = _tracker.createInstance<MemoContext>(_ctx, getState());
  enterRule(_localctx, 58, OliviaPKParser::RuleMemo);
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
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 57344) != 0))) {
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

void OliviaPKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  oliviapkparserParserInitialize();
#else
  ::antlr4::internal::call_once(oliviapkparserParserOnceFlag, oliviapkparserParserInitialize);
#endif
}
