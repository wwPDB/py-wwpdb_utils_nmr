
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CcpnPKParser.g4 by ANTLR 4.13.2


#include "CcpnPKParserVisitor.h"

#include "CcpnPKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct CcpnPKParserStaticData final {
  CcpnPKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  CcpnPKParserStaticData(const CcpnPKParserStaticData&) = delete;
  CcpnPKParserStaticData(CcpnPKParserStaticData&&) = delete;
  CcpnPKParserStaticData& operator=(const CcpnPKParserStaticData&) = delete;
  CcpnPKParserStaticData& operator=(CcpnPKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag ccpnpkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<CcpnPKParserStaticData> ccpnpkparserParserStaticData = nullptr;

void ccpnpkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (ccpnpkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(ccpnpkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<CcpnPKParserStaticData>(
    std::vector<std::string>{
      "ccpn_pk", "peak_list_2d", "peak_2d", "peak_list_3d", "peak_3d", "peak_list_4d", 
      "peak_4d", "peak_list_wo_assign_2d", "peak_wo_assign_2d", "peak_list_wo_assign_3d", 
      "peak_wo_assign_3d", "peak_list_wo_assign_4d", "peak_wo_assign_4d", 
      "position", "number", "note"
    },
    std::vector<std::string>{
      "", "'Number'", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "", "", "", "", "'Position F2'", "'Position F3'", "'Position F4'", 
      "", "'Shift F2'", "'Shift F3'", "'Shift F4'", "", "'Assign F2'", "'Assign F3'", 
      "'Assign F4'", "'Height'", "'Volume'", "'Line Width F1 (Hz)'", "'Line Width F2 (Hz)'", 
      "'Line Width F3 (Hz)'", "'Line Width F4 (Hz)'", "'Merit'", "'Details'", 
      "'Fit Method'", "'Vol. Method'"
    },
    std::vector<std::string>{
      "", "Num", "Id", "Assign_F1", "Position_F1", "Shift_F1", "Integer", 
      "Float", "Real", "EXCLM_COMMENT", "SMCLN_COMMENT", "Simple_name", 
      "Any_name", "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT", 
      "Id_", "Position_F1_", "Position_F2", "Position_F3", "Position_F4", 
      "Shift_F1_", "Shift_F2", "Shift_F3", "Shift_F4", "Assign_F1_", "Assign_F2", 
      "Assign_F3", "Assign_F4", "Height", "Volume", "Line_width_F1", "Line_width_F2", 
      "Line_width_F3", "Line_width_F4", "Merit", "Details", "Fit_method", 
      "Vol_method", "SPACE_VARS", "RETURN_VARS"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,41,590,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,1,0,3,0,34,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,43,8,0,10,
  	0,12,0,46,9,0,1,0,1,0,1,1,3,1,51,8,1,1,1,3,1,54,8,1,1,1,1,1,1,1,1,1,1,
  	1,1,1,1,1,1,1,3,1,64,8,1,1,1,3,1,67,8,1,1,1,3,1,70,8,1,1,1,3,1,73,8,1,
  	1,1,3,1,76,8,1,1,1,3,1,79,8,1,1,1,3,1,82,8,1,1,1,3,1,85,8,1,1,1,3,1,88,
  	8,1,1,1,1,1,4,1,92,8,1,11,1,12,1,93,1,2,3,2,97,8,2,1,2,3,2,100,8,2,1,
  	2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,112,8,2,1,2,3,2,115,8,2,1,2,
  	3,2,118,8,2,1,2,3,2,121,8,2,1,2,3,2,124,8,2,1,2,3,2,127,8,2,1,2,5,2,130,
  	8,2,10,2,12,2,133,9,2,1,2,1,2,1,3,3,3,138,8,3,1,3,3,3,141,8,3,1,3,1,3,
  	1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,155,8,3,1,3,3,3,158,8,3,1,
  	3,3,3,161,8,3,1,3,3,3,164,8,3,1,3,3,3,167,8,3,1,3,3,3,170,8,3,1,3,3,3,
  	173,8,3,1,3,3,3,176,8,3,1,3,3,3,179,8,3,1,3,3,3,182,8,3,1,3,1,3,4,3,186,
  	8,3,11,3,12,3,187,1,4,3,4,191,8,4,1,4,3,4,194,8,4,1,4,1,4,1,4,1,4,1,4,
  	1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,210,8,4,1,4,3,4,213,8,4,1,4,3,
  	4,216,8,4,1,4,3,4,219,8,4,1,4,3,4,222,8,4,1,4,3,4,225,8,4,1,4,3,4,228,
  	8,4,1,4,5,4,231,8,4,10,4,12,4,234,9,4,1,4,1,4,1,5,3,5,239,8,5,1,5,3,5,
  	242,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
  	5,3,5,260,8,5,1,5,3,5,263,8,5,1,5,3,5,266,8,5,1,5,3,5,269,8,5,1,5,3,5,
  	272,8,5,1,5,3,5,275,8,5,1,5,3,5,278,8,5,1,5,3,5,281,8,5,1,5,3,5,284,8,
  	5,1,5,3,5,287,8,5,1,5,3,5,290,8,5,1,5,1,5,4,5,294,8,5,11,5,12,5,295,1,
  	6,3,6,299,8,6,1,6,3,6,302,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
  	1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,322,8,6,1,6,3,6,325,8,6,1,6,3,6,328,
  	8,6,1,6,3,6,331,8,6,1,6,3,6,334,8,6,1,6,3,6,337,8,6,1,6,3,6,340,8,6,1,
  	6,3,6,343,8,6,1,6,5,6,346,8,6,10,6,12,6,349,9,6,1,6,1,6,1,7,3,7,354,8,
  	7,1,7,3,7,357,8,7,1,7,1,7,1,7,3,7,362,8,7,1,7,3,7,365,8,7,1,7,3,7,368,
  	8,7,1,7,3,7,371,8,7,1,7,3,7,374,8,7,1,7,3,7,377,8,7,1,7,3,7,380,8,7,1,
  	7,3,7,383,8,7,1,7,1,7,4,7,387,8,7,11,7,12,7,388,1,8,3,8,392,8,8,1,8,3,
  	8,395,8,8,1,8,1,8,1,8,3,8,400,8,8,1,8,3,8,403,8,8,1,8,3,8,406,8,8,1,8,
  	3,8,409,8,8,1,8,3,8,412,8,8,1,8,5,8,415,8,8,10,8,12,8,418,9,8,1,8,1,8,
  	1,9,3,9,423,8,9,1,9,3,9,426,8,9,1,9,1,9,1,9,1,9,3,9,432,8,9,1,9,3,9,435,
  	8,9,1,9,3,9,438,8,9,1,9,3,9,441,8,9,1,9,3,9,444,8,9,1,9,3,9,447,8,9,1,
  	9,3,9,450,8,9,1,9,3,9,453,8,9,1,9,3,9,456,8,9,1,9,1,9,4,9,460,8,9,11,
  	9,12,9,461,1,10,3,10,465,8,10,1,10,3,10,468,8,10,1,10,1,10,1,10,1,10,
  	3,10,474,8,10,1,10,3,10,477,8,10,1,10,3,10,480,8,10,1,10,3,10,483,8,10,
  	1,10,3,10,486,8,10,1,10,3,10,489,8,10,1,10,5,10,492,8,10,10,10,12,10,
  	495,9,10,1,10,1,10,1,11,3,11,500,8,11,1,11,3,11,503,8,11,1,11,1,11,1,
  	11,1,11,1,11,3,11,510,8,11,1,11,3,11,513,8,11,1,11,3,11,516,8,11,1,11,
  	3,11,519,8,11,1,11,3,11,522,8,11,1,11,3,11,525,8,11,1,11,3,11,528,8,11,
  	1,11,3,11,531,8,11,1,11,3,11,534,8,11,1,11,3,11,537,8,11,1,11,1,11,4,
  	11,541,8,11,11,11,12,11,542,1,12,3,12,546,8,12,1,12,3,12,549,8,12,1,12,
  	1,12,1,12,1,12,1,12,3,12,556,8,12,1,12,3,12,559,8,12,1,12,3,12,562,8,
  	12,1,12,3,12,565,8,12,1,12,3,12,568,8,12,1,12,3,12,571,8,12,1,12,3,12,
  	574,8,12,1,12,5,12,577,8,12,10,12,12,12,580,9,12,1,12,1,12,1,13,1,13,
  	1,14,1,14,1,15,1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
  	28,30,0,11,2,0,2,2,17,17,3,0,4,5,18,18,22,22,2,0,19,19,23,23,2,0,3,3,
  	26,26,2,0,18,18,22,22,1,1,14,14,2,0,20,20,24,24,2,0,5,5,18,18,2,0,21,
  	21,25,25,2,0,6,8,11,11,2,0,6,8,11,12,713,0,33,1,0,0,0,2,50,1,0,0,0,4,
  	96,1,0,0,0,6,137,1,0,0,0,8,190,1,0,0,0,10,238,1,0,0,0,12,298,1,0,0,0,
  	14,353,1,0,0,0,16,391,1,0,0,0,18,422,1,0,0,0,20,464,1,0,0,0,22,499,1,
  	0,0,0,24,545,1,0,0,0,26,583,1,0,0,0,28,585,1,0,0,0,30,587,1,0,0,0,32,
  	34,5,14,0,0,33,32,1,0,0,0,33,34,1,0,0,0,34,44,1,0,0,0,35,43,3,2,1,0,36,
  	43,3,6,3,0,37,43,3,10,5,0,38,43,3,14,7,0,39,43,3,18,9,0,40,43,3,22,11,
  	0,41,43,5,14,0,0,42,35,1,0,0,0,42,36,1,0,0,0,42,37,1,0,0,0,42,38,1,0,
  	0,0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,
  	0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,47,48,5,0,0,1,48,1,1,0,
  	0,0,49,51,5,1,0,0,50,49,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,54,7,0,
  	0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,63,1,0,0,0,55,56,7,1,0,0,56,57,7,2,
  	0,0,57,58,5,26,0,0,58,64,5,27,0,0,59,60,7,3,0,0,60,61,5,27,0,0,61,62,
  	7,4,0,0,62,64,7,2,0,0,63,55,1,0,0,0,63,59,1,0,0,0,64,66,1,0,0,0,65,67,
  	5,30,0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,70,5,31,0,0,69,
  	68,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,73,5,32,0,0,72,71,1,0,0,0,72,
  	73,1,0,0,0,73,75,1,0,0,0,74,76,5,33,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,
  	78,1,0,0,0,77,79,5,36,0,0,78,77,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,
  	82,5,37,0,0,81,80,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,85,5,38,0,0,
  	84,83,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,88,5,39,0,0,87,86,1,0,0,
  	0,87,88,1,0,0,0,88,89,1,0,0,0,89,91,5,41,0,0,90,92,3,4,2,0,91,90,1,0,
  	0,0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,3,1,0,0,0,95,97,5,6,
  	0,0,96,95,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,100,5,6,0,0,99,98,1,
  	0,0,0,99,100,1,0,0,0,100,111,1,0,0,0,101,102,3,26,13,0,102,103,3,26,13,
  	0,103,104,5,11,0,0,104,105,5,11,0,0,105,112,1,0,0,0,106,107,5,11,0,0,
  	107,108,5,11,0,0,108,109,3,26,13,0,109,110,3,26,13,0,110,112,1,0,0,0,
  	111,101,1,0,0,0,111,106,1,0,0,0,112,114,1,0,0,0,113,115,3,28,14,0,114,
  	113,1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,0,116,118,3,28,14,0,117,116,
  	1,0,0,0,117,118,1,0,0,0,118,120,1,0,0,0,119,121,3,26,13,0,120,119,1,0,
  	0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,124,3,26,13,0,123,122,1,0,0,0,
  	123,124,1,0,0,0,124,126,1,0,0,0,125,127,3,26,13,0,126,125,1,0,0,0,126,
  	127,1,0,0,0,127,131,1,0,0,0,128,130,3,30,15,0,129,128,1,0,0,0,130,133,
  	1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,
  	0,134,135,7,5,0,0,135,5,1,0,0,0,136,138,5,1,0,0,137,136,1,0,0,0,137,138,
  	1,0,0,0,138,140,1,0,0,0,139,141,7,0,0,0,140,139,1,0,0,0,140,141,1,0,0,
  	0,141,154,1,0,0,0,142,143,7,1,0,0,143,144,7,2,0,0,144,145,7,6,0,0,145,
  	146,5,26,0,0,146,147,5,27,0,0,147,155,5,28,0,0,148,149,7,3,0,0,149,150,
  	5,27,0,0,150,151,5,28,0,0,151,152,7,7,0,0,152,153,7,2,0,0,153,155,7,6,
  	0,0,154,142,1,0,0,0,154,148,1,0,0,0,155,157,1,0,0,0,156,158,5,30,0,0,
  	157,156,1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,161,5,31,0,0,160,
  	159,1,0,0,0,160,161,1,0,0,0,161,163,1,0,0,0,162,164,5,32,0,0,163,162,
  	1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,165,167,5,33,0,0,166,165,1,0,
  	0,0,166,167,1,0,0,0,167,169,1,0,0,0,168,170,5,34,0,0,169,168,1,0,0,0,
  	169,170,1,0,0,0,170,172,1,0,0,0,171,173,5,36,0,0,172,171,1,0,0,0,172,
  	173,1,0,0,0,173,175,1,0,0,0,174,176,5,37,0,0,175,174,1,0,0,0,175,176,
  	1,0,0,0,176,178,1,0,0,0,177,179,5,38,0,0,178,177,1,0,0,0,178,179,1,0,
  	0,0,179,181,1,0,0,0,180,182,5,39,0,0,181,180,1,0,0,0,181,182,1,0,0,0,
  	182,183,1,0,0,0,183,185,5,41,0,0,184,186,3,8,4,0,185,184,1,0,0,0,186,
  	187,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,7,1,0,0,0,189,191,5,6,
  	0,0,190,189,1,0,0,0,190,191,1,0,0,0,191,193,1,0,0,0,192,194,5,6,0,0,193,
  	192,1,0,0,0,193,194,1,0,0,0,194,209,1,0,0,0,195,196,3,26,13,0,196,197,
  	3,26,13,0,197,198,3,26,13,0,198,199,5,11,0,0,199,200,5,11,0,0,200,201,
  	5,11,0,0,201,210,1,0,0,0,202,203,5,11,0,0,203,204,5,11,0,0,204,205,5,
  	11,0,0,205,206,3,26,13,0,206,207,3,26,13,0,207,208,3,26,13,0,208,210,
  	1,0,0,0,209,195,1,0,0,0,209,202,1,0,0,0,210,212,1,0,0,0,211,213,3,28,
  	14,0,212,211,1,0,0,0,212,213,1,0,0,0,213,215,1,0,0,0,214,216,3,28,14,
  	0,215,214,1,0,0,0,215,216,1,0,0,0,216,218,1,0,0,0,217,219,3,26,13,0,218,
  	217,1,0,0,0,218,219,1,0,0,0,219,221,1,0,0,0,220,222,3,26,13,0,221,220,
  	1,0,0,0,221,222,1,0,0,0,222,224,1,0,0,0,223,225,3,26,13,0,224,223,1,0,
  	0,0,224,225,1,0,0,0,225,227,1,0,0,0,226,228,3,26,13,0,227,226,1,0,0,0,
  	227,228,1,0,0,0,228,232,1,0,0,0,229,231,3,30,15,0,230,229,1,0,0,0,231,
  	234,1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,235,1,0,0,0,234,232,1,
  	0,0,0,235,236,7,5,0,0,236,9,1,0,0,0,237,239,5,1,0,0,238,237,1,0,0,0,238,
  	239,1,0,0,0,239,241,1,0,0,0,240,242,7,0,0,0,241,240,1,0,0,0,241,242,1,
  	0,0,0,242,259,1,0,0,0,243,244,7,1,0,0,244,245,7,2,0,0,245,246,7,6,0,0,
  	246,247,7,8,0,0,247,248,5,26,0,0,248,249,5,27,0,0,249,250,5,28,0,0,250,
  	260,5,29,0,0,251,252,7,3,0,0,252,253,5,27,0,0,253,254,5,28,0,0,254,255,
  	5,29,0,0,255,256,7,7,0,0,256,257,7,2,0,0,257,258,7,6,0,0,258,260,7,8,
  	0,0,259,243,1,0,0,0,259,251,1,0,0,0,260,262,1,0,0,0,261,263,5,30,0,0,
  	262,261,1,0,0,0,262,263,1,0,0,0,263,265,1,0,0,0,264,266,5,31,0,0,265,
  	264,1,0,0,0,265,266,1,0,0,0,266,268,1,0,0,0,267,269,5,32,0,0,268,267,
  	1,0,0,0,268,269,1,0,0,0,269,271,1,0,0,0,270,272,5,33,0,0,271,270,1,0,
  	0,0,271,272,1,0,0,0,272,274,1,0,0,0,273,275,5,34,0,0,274,273,1,0,0,0,
  	274,275,1,0,0,0,275,277,1,0,0,0,276,278,5,35,0,0,277,276,1,0,0,0,277,
  	278,1,0,0,0,278,280,1,0,0,0,279,281,5,36,0,0,280,279,1,0,0,0,280,281,
  	1,0,0,0,281,283,1,0,0,0,282,284,5,37,0,0,283,282,1,0,0,0,283,284,1,0,
  	0,0,284,286,1,0,0,0,285,287,5,38,0,0,286,285,1,0,0,0,286,287,1,0,0,0,
  	287,289,1,0,0,0,288,290,5,39,0,0,289,288,1,0,0,0,289,290,1,0,0,0,290,
  	291,1,0,0,0,291,293,5,41,0,0,292,294,3,12,6,0,293,292,1,0,0,0,294,295,
  	1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,11,1,0,0,0,297,299,5,6,0,
  	0,298,297,1,0,0,0,298,299,1,0,0,0,299,301,1,0,0,0,300,302,5,6,0,0,301,
  	300,1,0,0,0,301,302,1,0,0,0,302,321,1,0,0,0,303,304,3,26,13,0,304,305,
  	3,26,13,0,305,306,3,26,13,0,306,307,3,26,13,0,307,308,5,11,0,0,308,309,
  	5,11,0,0,309,310,5,11,0,0,310,311,5,11,0,0,311,322,1,0,0,0,312,313,5,
  	11,0,0,313,314,5,11,0,0,314,315,5,11,0,0,315,316,5,11,0,0,316,317,3,26,
  	13,0,317,318,3,26,13,0,318,319,3,26,13,0,319,320,3,26,13,0,320,322,1,
  	0,0,0,321,303,1,0,0,0,321,312,1,0,0,0,322,324,1,0,0,0,323,325,3,28,14,
  	0,324,323,1,0,0,0,324,325,1,0,0,0,325,327,1,0,0,0,326,328,3,28,14,0,327,
  	326,1,0,0,0,327,328,1,0,0,0,328,330,1,0,0,0,329,331,3,26,13,0,330,329,
  	1,0,0,0,330,331,1,0,0,0,331,333,1,0,0,0,332,334,3,26,13,0,333,332,1,0,
  	0,0,333,334,1,0,0,0,334,336,1,0,0,0,335,337,3,26,13,0,336,335,1,0,0,0,
  	336,337,1,0,0,0,337,339,1,0,0,0,338,340,3,26,13,0,339,338,1,0,0,0,339,
  	340,1,0,0,0,340,342,1,0,0,0,341,343,3,26,13,0,342,341,1,0,0,0,342,343,
  	1,0,0,0,343,347,1,0,0,0,344,346,3,30,15,0,345,344,1,0,0,0,346,349,1,0,
  	0,0,347,345,1,0,0,0,347,348,1,0,0,0,348,350,1,0,0,0,349,347,1,0,0,0,350,
  	351,7,5,0,0,351,13,1,0,0,0,352,354,5,1,0,0,353,352,1,0,0,0,353,354,1,
  	0,0,0,354,356,1,0,0,0,355,357,7,0,0,0,356,355,1,0,0,0,356,357,1,0,0,0,
  	357,358,1,0,0,0,358,359,7,1,0,0,359,361,7,2,0,0,360,362,5,30,0,0,361,
  	360,1,0,0,0,361,362,1,0,0,0,362,364,1,0,0,0,363,365,5,31,0,0,364,363,
  	1,0,0,0,364,365,1,0,0,0,365,367,1,0,0,0,366,368,5,32,0,0,367,366,1,0,
  	0,0,367,368,1,0,0,0,368,370,1,0,0,0,369,371,5,33,0,0,370,369,1,0,0,0,
  	370,371,1,0,0,0,371,373,1,0,0,0,372,374,5,36,0,0,373,372,1,0,0,0,373,
  	374,1,0,0,0,374,376,1,0,0,0,375,377,5,37,0,0,376,375,1,0,0,0,376,377,
  	1,0,0,0,377,379,1,0,0,0,378,380,5,38,0,0,379,378,1,0,0,0,379,380,1,0,
  	0,0,380,382,1,0,0,0,381,383,5,39,0,0,382,381,1,0,0,0,382,383,1,0,0,0,
  	383,384,1,0,0,0,384,386,5,41,0,0,385,387,3,16,8,0,386,385,1,0,0,0,387,
  	388,1,0,0,0,388,386,1,0,0,0,388,389,1,0,0,0,389,15,1,0,0,0,390,392,5,
  	6,0,0,391,390,1,0,0,0,391,392,1,0,0,0,392,394,1,0,0,0,393,395,5,6,0,0,
  	394,393,1,0,0,0,394,395,1,0,0,0,395,396,1,0,0,0,396,397,3,26,13,0,397,
  	399,3,26,13,0,398,400,3,28,14,0,399,398,1,0,0,0,399,400,1,0,0,0,400,402,
  	1,0,0,0,401,403,3,28,14,0,402,401,1,0,0,0,402,403,1,0,0,0,403,405,1,0,
  	0,0,404,406,3,26,13,0,405,404,1,0,0,0,405,406,1,0,0,0,406,408,1,0,0,0,
  	407,409,3,26,13,0,408,407,1,0,0,0,408,409,1,0,0,0,409,411,1,0,0,0,410,
  	412,3,26,13,0,411,410,1,0,0,0,411,412,1,0,0,0,412,416,1,0,0,0,413,415,
  	3,30,15,0,414,413,1,0,0,0,415,418,1,0,0,0,416,414,1,0,0,0,416,417,1,0,
  	0,0,417,419,1,0,0,0,418,416,1,0,0,0,419,420,7,5,0,0,420,17,1,0,0,0,421,
  	423,5,1,0,0,422,421,1,0,0,0,422,423,1,0,0,0,423,425,1,0,0,0,424,426,7,
  	0,0,0,425,424,1,0,0,0,425,426,1,0,0,0,426,427,1,0,0,0,427,428,7,1,0,0,
  	428,429,7,2,0,0,429,431,7,6,0,0,430,432,5,30,0,0,431,430,1,0,0,0,431,
  	432,1,0,0,0,432,434,1,0,0,0,433,435,5,31,0,0,434,433,1,0,0,0,434,435,
  	1,0,0,0,435,437,1,0,0,0,436,438,5,32,0,0,437,436,1,0,0,0,437,438,1,0,
  	0,0,438,440,1,0,0,0,439,441,5,33,0,0,440,439,1,0,0,0,440,441,1,0,0,0,
  	441,443,1,0,0,0,442,444,5,34,0,0,443,442,1,0,0,0,443,444,1,0,0,0,444,
  	446,1,0,0,0,445,447,5,36,0,0,446,445,1,0,0,0,446,447,1,0,0,0,447,449,
  	1,0,0,0,448,450,5,37,0,0,449,448,1,0,0,0,449,450,1,0,0,0,450,452,1,0,
  	0,0,451,453,5,38,0,0,452,451,1,0,0,0,452,453,1,0,0,0,453,455,1,0,0,0,
  	454,456,5,39,0,0,455,454,1,0,0,0,455,456,1,0,0,0,456,457,1,0,0,0,457,
  	459,5,41,0,0,458,460,3,20,10,0,459,458,1,0,0,0,460,461,1,0,0,0,461,459,
  	1,0,0,0,461,462,1,0,0,0,462,19,1,0,0,0,463,465,5,6,0,0,464,463,1,0,0,
  	0,464,465,1,0,0,0,465,467,1,0,0,0,466,468,5,6,0,0,467,466,1,0,0,0,467,
  	468,1,0,0,0,468,469,1,0,0,0,469,470,3,26,13,0,470,471,3,26,13,0,471,473,
  	3,26,13,0,472,474,3,28,14,0,473,472,1,0,0,0,473,474,1,0,0,0,474,476,1,
  	0,0,0,475,477,3,28,14,0,476,475,1,0,0,0,476,477,1,0,0,0,477,479,1,0,0,
  	0,478,480,3,26,13,0,479,478,1,0,0,0,479,480,1,0,0,0,480,482,1,0,0,0,481,
  	483,3,26,13,0,482,481,1,0,0,0,482,483,1,0,0,0,483,485,1,0,0,0,484,486,
  	3,26,13,0,485,484,1,0,0,0,485,486,1,0,0,0,486,488,1,0,0,0,487,489,3,26,
  	13,0,488,487,1,0,0,0,488,489,1,0,0,0,489,493,1,0,0,0,490,492,3,30,15,
  	0,491,490,1,0,0,0,492,495,1,0,0,0,493,491,1,0,0,0,493,494,1,0,0,0,494,
  	496,1,0,0,0,495,493,1,0,0,0,496,497,7,5,0,0,497,21,1,0,0,0,498,500,5,
  	1,0,0,499,498,1,0,0,0,499,500,1,0,0,0,500,502,1,0,0,0,501,503,7,0,0,0,
  	502,501,1,0,0,0,502,503,1,0,0,0,503,504,1,0,0,0,504,505,7,1,0,0,505,506,
  	7,2,0,0,506,507,7,6,0,0,507,509,7,8,0,0,508,510,5,30,0,0,509,508,1,0,
  	0,0,509,510,1,0,0,0,510,512,1,0,0,0,511,513,5,31,0,0,512,511,1,0,0,0,
  	512,513,1,0,0,0,513,515,1,0,0,0,514,516,5,32,0,0,515,514,1,0,0,0,515,
  	516,1,0,0,0,516,518,1,0,0,0,517,519,5,33,0,0,518,517,1,0,0,0,518,519,
  	1,0,0,0,519,521,1,0,0,0,520,522,5,34,0,0,521,520,1,0,0,0,521,522,1,0,
  	0,0,522,524,1,0,0,0,523,525,5,35,0,0,524,523,1,0,0,0,524,525,1,0,0,0,
  	525,527,1,0,0,0,526,528,5,36,0,0,527,526,1,0,0,0,527,528,1,0,0,0,528,
  	530,1,0,0,0,529,531,5,37,0,0,530,529,1,0,0,0,530,531,1,0,0,0,531,533,
  	1,0,0,0,532,534,5,38,0,0,533,532,1,0,0,0,533,534,1,0,0,0,534,536,1,0,
  	0,0,535,537,5,39,0,0,536,535,1,0,0,0,536,537,1,0,0,0,537,538,1,0,0,0,
  	538,540,5,41,0,0,539,541,3,24,12,0,540,539,1,0,0,0,541,542,1,0,0,0,542,
  	540,1,0,0,0,542,543,1,0,0,0,543,23,1,0,0,0,544,546,5,6,0,0,545,544,1,
  	0,0,0,545,546,1,0,0,0,546,548,1,0,0,0,547,549,5,6,0,0,548,547,1,0,0,0,
  	548,549,1,0,0,0,549,550,1,0,0,0,550,551,3,26,13,0,551,552,3,26,13,0,552,
  	553,3,26,13,0,553,555,3,26,13,0,554,556,3,28,14,0,555,554,1,0,0,0,555,
  	556,1,0,0,0,556,558,1,0,0,0,557,559,3,28,14,0,558,557,1,0,0,0,558,559,
  	1,0,0,0,559,561,1,0,0,0,560,562,3,26,13,0,561,560,1,0,0,0,561,562,1,0,
  	0,0,562,564,1,0,0,0,563,565,3,26,13,0,564,563,1,0,0,0,564,565,1,0,0,0,
  	565,567,1,0,0,0,566,568,3,26,13,0,567,566,1,0,0,0,567,568,1,0,0,0,568,
  	570,1,0,0,0,569,571,3,26,13,0,570,569,1,0,0,0,570,571,1,0,0,0,571,573,
  	1,0,0,0,572,574,3,26,13,0,573,572,1,0,0,0,573,574,1,0,0,0,574,578,1,0,
  	0,0,575,577,3,30,15,0,576,575,1,0,0,0,577,580,1,0,0,0,578,576,1,0,0,0,
  	578,579,1,0,0,0,579,581,1,0,0,0,580,578,1,0,0,0,581,582,7,5,0,0,582,25,
  	1,0,0,0,583,584,7,9,0,0,584,27,1,0,0,0,585,586,7,9,0,0,586,29,1,0,0,0,
  	587,588,7,10,0,0,588,31,1,0,0,0,135,33,42,44,50,53,63,66,69,72,75,78,
  	81,84,87,93,96,99,111,114,117,120,123,126,131,137,140,154,157,160,163,
  	166,169,172,175,178,181,187,190,193,209,212,215,218,221,224,227,232,238,
  	241,259,262,265,268,271,274,277,280,283,286,289,295,298,301,321,324,327,
  	330,333,336,339,342,347,353,356,361,364,367,370,373,376,379,382,388,391,
  	394,399,402,405,408,411,416,422,425,431,434,437,440,443,446,449,452,455,
  	461,464,467,473,476,479,482,485,488,493,499,502,509,512,515,518,521,524,
  	527,530,533,536,542,545,548,555,558,561,564,567,570,573,578
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  ccpnpkparserParserStaticData = std::move(staticData);
}

}

CcpnPKParser::CcpnPKParser(TokenStream *input) : CcpnPKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

CcpnPKParser::CcpnPKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  CcpnPKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *ccpnpkparserParserStaticData->atn, ccpnpkparserParserStaticData->decisionToDFA, ccpnpkparserParserStaticData->sharedContextCache, options);
}

CcpnPKParser::~CcpnPKParser() {
  delete _interpreter;
}

const atn::ATN& CcpnPKParser::getATN() const {
  return *ccpnpkparserParserStaticData->atn;
}

std::string CcpnPKParser::getGrammarFileName() const {
  return "CcpnPKParser.g4";
}

const std::vector<std::string>& CcpnPKParser::getRuleNames() const {
  return ccpnpkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& CcpnPKParser::getVocabulary() const {
  return ccpnpkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView CcpnPKParser::getSerializedATN() const {
  return ccpnpkparserParserStaticData->serializedATN;
}


//----------------- Ccpn_pkContext ------------------------------------------------------------------

CcpnPKParser::Ccpn_pkContext::Ccpn_pkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::Ccpn_pkContext::EOF() {
  return getToken(CcpnPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CcpnPKParser::Ccpn_pkContext::RETURN() {
  return getTokens(CcpnPKParser::RETURN);
}

tree::TerminalNode* CcpnPKParser::Ccpn_pkContext::RETURN(size_t i) {
  return getToken(CcpnPKParser::RETURN, i);
}

std::vector<CcpnPKParser::Peak_list_2dContext *> CcpnPKParser::Ccpn_pkContext::peak_list_2d() {
  return getRuleContexts<CcpnPKParser::Peak_list_2dContext>();
}

CcpnPKParser::Peak_list_2dContext* CcpnPKParser::Ccpn_pkContext::peak_list_2d(size_t i) {
  return getRuleContext<CcpnPKParser::Peak_list_2dContext>(i);
}

std::vector<CcpnPKParser::Peak_list_3dContext *> CcpnPKParser::Ccpn_pkContext::peak_list_3d() {
  return getRuleContexts<CcpnPKParser::Peak_list_3dContext>();
}

CcpnPKParser::Peak_list_3dContext* CcpnPKParser::Ccpn_pkContext::peak_list_3d(size_t i) {
  return getRuleContext<CcpnPKParser::Peak_list_3dContext>(i);
}

std::vector<CcpnPKParser::Peak_list_4dContext *> CcpnPKParser::Ccpn_pkContext::peak_list_4d() {
  return getRuleContexts<CcpnPKParser::Peak_list_4dContext>();
}

CcpnPKParser::Peak_list_4dContext* CcpnPKParser::Ccpn_pkContext::peak_list_4d(size_t i) {
  return getRuleContext<CcpnPKParser::Peak_list_4dContext>(i);
}

std::vector<CcpnPKParser::Peak_list_wo_assign_2dContext *> CcpnPKParser::Ccpn_pkContext::peak_list_wo_assign_2d() {
  return getRuleContexts<CcpnPKParser::Peak_list_wo_assign_2dContext>();
}

CcpnPKParser::Peak_list_wo_assign_2dContext* CcpnPKParser::Ccpn_pkContext::peak_list_wo_assign_2d(size_t i) {
  return getRuleContext<CcpnPKParser::Peak_list_wo_assign_2dContext>(i);
}

std::vector<CcpnPKParser::Peak_list_wo_assign_3dContext *> CcpnPKParser::Ccpn_pkContext::peak_list_wo_assign_3d() {
  return getRuleContexts<CcpnPKParser::Peak_list_wo_assign_3dContext>();
}

CcpnPKParser::Peak_list_wo_assign_3dContext* CcpnPKParser::Ccpn_pkContext::peak_list_wo_assign_3d(size_t i) {
  return getRuleContext<CcpnPKParser::Peak_list_wo_assign_3dContext>(i);
}

std::vector<CcpnPKParser::Peak_list_wo_assign_4dContext *> CcpnPKParser::Ccpn_pkContext::peak_list_wo_assign_4d() {
  return getRuleContexts<CcpnPKParser::Peak_list_wo_assign_4dContext>();
}

CcpnPKParser::Peak_list_wo_assign_4dContext* CcpnPKParser::Ccpn_pkContext::peak_list_wo_assign_4d(size_t i) {
  return getRuleContext<CcpnPKParser::Peak_list_wo_assign_4dContext>(i);
}


size_t CcpnPKParser::Ccpn_pkContext::getRuleIndex() const {
  return CcpnPKParser::RuleCcpn_pk;
}


std::any CcpnPKParser::Ccpn_pkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitCcpn_pk(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Ccpn_pkContext* CcpnPKParser::ccpn_pk() {
  Ccpn_pkContext *_localctx = _tracker.createInstance<Ccpn_pkContext>(_ctx, getState());
  enterRule(_localctx, 0, CcpnPKParser::RuleCcpn_pk);
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
    setState(33);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(32);
      match(CcpnPKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(44);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 71712830) != 0)) {
      setState(42);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(35);
        peak_list_2d();
        break;
      }

      case 2: {
        setState(36);
        peak_list_3d();
        break;
      }

      case 3: {
        setState(37);
        peak_list_4d();
        break;
      }

      case 4: {
        setState(38);
        peak_list_wo_assign_2d();
        break;
      }

      case 5: {
        setState(39);
        peak_list_wo_assign_3d();
        break;
      }

      case 6: {
        setState(40);
        peak_list_wo_assign_4d();
        break;
      }

      case 7: {
        setState(41);
        match(CcpnPKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(46);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(47);
    match(CcpnPKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_list_2dContext ------------------------------------------------------------------

CcpnPKParser::Peak_list_2dContext::Peak_list_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::RETURN_VARS() {
  return getToken(CcpnPKParser::RETURN_VARS, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Num() {
  return getToken(CcpnPKParser::Num, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Height() {
  return getToken(CcpnPKParser::Height, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Volume() {
  return getToken(CcpnPKParser::Volume, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Line_width_F1() {
  return getToken(CcpnPKParser::Line_width_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Line_width_F2() {
  return getToken(CcpnPKParser::Line_width_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Merit() {
  return getToken(CcpnPKParser::Merit, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Details() {
  return getToken(CcpnPKParser::Details, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Fit_method() {
  return getToken(CcpnPKParser::Fit_method, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Vol_method() {
  return getToken(CcpnPKParser::Vol_method, 0);
}

std::vector<CcpnPKParser::Peak_2dContext *> CcpnPKParser::Peak_list_2dContext::peak_2d() {
  return getRuleContexts<CcpnPKParser::Peak_2dContext>();
}

CcpnPKParser::Peak_2dContext* CcpnPKParser::Peak_list_2dContext::peak_2d(size_t i) {
  return getRuleContext<CcpnPKParser::Peak_2dContext>(i);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Id() {
  return getToken(CcpnPKParser::Id, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Id_() {
  return getToken(CcpnPKParser::Id_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Assign_F1_() {
  return getToken(CcpnPKParser::Assign_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Assign_F2() {
  return getToken(CcpnPKParser::Assign_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Position_F1() {
  return getToken(CcpnPKParser::Position_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Shift_F1() {
  return getToken(CcpnPKParser::Shift_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Position_F1_() {
  return getToken(CcpnPKParser::Position_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Shift_F1_() {
  return getToken(CcpnPKParser::Shift_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Position_F2() {
  return getToken(CcpnPKParser::Position_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Shift_F2() {
  return getToken(CcpnPKParser::Shift_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_2dContext::Assign_F1() {
  return getToken(CcpnPKParser::Assign_F1, 0);
}


size_t CcpnPKParser::Peak_list_2dContext::getRuleIndex() const {
  return CcpnPKParser::RulePeak_list_2d;
}


std::any CcpnPKParser::Peak_list_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_2d(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Peak_list_2dContext* CcpnPKParser::peak_list_2d() {
  Peak_list_2dContext *_localctx = _tracker.createInstance<Peak_list_2dContext>(_ctx, getState());
  enterRule(_localctx, 2, CcpnPKParser::RulePeak_list_2d);
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
    setState(50);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Num) {
      setState(49);
      match(CcpnPKParser::Num);
    }
    setState(53);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Id

    || _la == CcpnPKParser::Id_) {
      setState(52);
      _la = _input->LA(1);
      if (!(_la == CcpnPKParser::Id

      || _la == CcpnPKParser::Id_)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
    }
    setState(63);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CcpnPKParser::Position_F1:
      case CcpnPKParser::Shift_F1:
      case CcpnPKParser::Position_F1_:
      case CcpnPKParser::Shift_F1_: {
        setState(55);
        _la = _input->LA(1);
        if (!((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 4456496) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(56);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F2

        || _la == CcpnPKParser::Shift_F2)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(57);
        match(CcpnPKParser::Assign_F1_);
        setState(58);
        match(CcpnPKParser::Assign_F2);
        break;
      }

      case CcpnPKParser::Assign_F1:
      case CcpnPKParser::Assign_F1_: {
        setState(59);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Assign_F1

        || _la == CcpnPKParser::Assign_F1_)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(60);
        match(CcpnPKParser::Assign_F2);
        setState(61);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F1_

        || _la == CcpnPKParser::Shift_F1_)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(62);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F2

        || _la == CcpnPKParser::Shift_F2)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(66);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Height) {
      setState(65);
      match(CcpnPKParser::Height);
    }
    setState(69);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Volume) {
      setState(68);
      match(CcpnPKParser::Volume);
    }
    setState(72);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F1) {
      setState(71);
      match(CcpnPKParser::Line_width_F1);
    }
    setState(75);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F2) {
      setState(74);
      match(CcpnPKParser::Line_width_F2);
    }
    setState(78);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Merit) {
      setState(77);
      match(CcpnPKParser::Merit);
    }
    setState(81);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Details) {
      setState(80);
      match(CcpnPKParser::Details);
    }
    setState(84);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Fit_method) {
      setState(83);
      match(CcpnPKParser::Fit_method);
    }
    setState(87);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Vol_method) {
      setState(86);
      match(CcpnPKParser::Vol_method);
    }
    setState(89);
    match(CcpnPKParser::RETURN_VARS);
    setState(91); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(90);
      peak_2d();
      setState(93); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2496) != 0));
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_2dContext ------------------------------------------------------------------

CcpnPKParser::Peak_2dContext::Peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::Peak_2dContext::RETURN() {
  return getToken(CcpnPKParser::RETURN, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_2dContext::EOF() {
  return getToken(CcpnPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CcpnPKParser::Peak_2dContext::Integer() {
  return getTokens(CcpnPKParser::Integer);
}

tree::TerminalNode* CcpnPKParser::Peak_2dContext::Integer(size_t i) {
  return getToken(CcpnPKParser::Integer, i);
}

std::vector<CcpnPKParser::NumberContext *> CcpnPKParser::Peak_2dContext::number() {
  return getRuleContexts<CcpnPKParser::NumberContext>();
}

CcpnPKParser::NumberContext* CcpnPKParser::Peak_2dContext::number(size_t i) {
  return getRuleContext<CcpnPKParser::NumberContext>(i);
}

std::vector<CcpnPKParser::PositionContext *> CcpnPKParser::Peak_2dContext::position() {
  return getRuleContexts<CcpnPKParser::PositionContext>();
}

CcpnPKParser::PositionContext* CcpnPKParser::Peak_2dContext::position(size_t i) {
  return getRuleContext<CcpnPKParser::PositionContext>(i);
}

std::vector<CcpnPKParser::NoteContext *> CcpnPKParser::Peak_2dContext::note() {
  return getRuleContexts<CcpnPKParser::NoteContext>();
}

CcpnPKParser::NoteContext* CcpnPKParser::Peak_2dContext::note(size_t i) {
  return getRuleContext<CcpnPKParser::NoteContext>(i);
}

std::vector<tree::TerminalNode *> CcpnPKParser::Peak_2dContext::Simple_name() {
  return getTokens(CcpnPKParser::Simple_name);
}

tree::TerminalNode* CcpnPKParser::Peak_2dContext::Simple_name(size_t i) {
  return getToken(CcpnPKParser::Simple_name, i);
}


size_t CcpnPKParser::Peak_2dContext::getRuleIndex() const {
  return CcpnPKParser::RulePeak_2d;
}


std::any CcpnPKParser::Peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Peak_2dContext* CcpnPKParser::peak_2d() {
  Peak_2dContext *_localctx = _tracker.createInstance<Peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 4, CcpnPKParser::RulePeak_2d);
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
    setState(96);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 15, _ctx)) {
    case 1: {
      setState(95);
      match(CcpnPKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(99);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 16, _ctx)) {
    case 1: {
      setState(98);
      match(CcpnPKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(111);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx)) {
    case 1: {
      setState(101);
      position();
      setState(102);
      position();
      setState(103);
      match(CcpnPKParser::Simple_name);
      setState(104);
      match(CcpnPKParser::Simple_name);
      break;
    }

    case 2: {
      setState(106);
      match(CcpnPKParser::Simple_name);
      setState(107);
      match(CcpnPKParser::Simple_name);
      setState(108);
      position();
      setState(109);
      position();
      break;
    }

    default:
      break;
    }
    setState(114);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx)) {
    case 1: {
      setState(113);
      number();
      break;
    }

    default:
      break;
    }
    setState(117);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 19, _ctx)) {
    case 1: {
      setState(116);
      number();
      break;
    }

    default:
      break;
    }
    setState(120);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 20, _ctx)) {
    case 1: {
      setState(119);
      position();
      break;
    }

    default:
      break;
    }
    setState(123);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 21, _ctx)) {
    case 1: {
      setState(122);
      position();
      break;
    }

    default:
      break;
    }
    setState(126);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 22, _ctx)) {
    case 1: {
      setState(125);
      position();
      break;
    }

    default:
      break;
    }
    setState(131);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 6592) != 0)) {
      setState(128);
      note();
      setState(133);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(134);
    _la = _input->LA(1);
    if (!(_la == CcpnPKParser::EOF

    || _la == CcpnPKParser::RETURN)) {
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

CcpnPKParser::Peak_list_3dContext::Peak_list_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::RETURN_VARS() {
  return getToken(CcpnPKParser::RETURN_VARS, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Num() {
  return getToken(CcpnPKParser::Num, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Height() {
  return getToken(CcpnPKParser::Height, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Volume() {
  return getToken(CcpnPKParser::Volume, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Line_width_F1() {
  return getToken(CcpnPKParser::Line_width_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Line_width_F2() {
  return getToken(CcpnPKParser::Line_width_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Line_width_F3() {
  return getToken(CcpnPKParser::Line_width_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Merit() {
  return getToken(CcpnPKParser::Merit, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Details() {
  return getToken(CcpnPKParser::Details, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Fit_method() {
  return getToken(CcpnPKParser::Fit_method, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Vol_method() {
  return getToken(CcpnPKParser::Vol_method, 0);
}

std::vector<CcpnPKParser::Peak_3dContext *> CcpnPKParser::Peak_list_3dContext::peak_3d() {
  return getRuleContexts<CcpnPKParser::Peak_3dContext>();
}

CcpnPKParser::Peak_3dContext* CcpnPKParser::Peak_list_3dContext::peak_3d(size_t i) {
  return getRuleContext<CcpnPKParser::Peak_3dContext>(i);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Id() {
  return getToken(CcpnPKParser::Id, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Id_() {
  return getToken(CcpnPKParser::Id_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Assign_F1_() {
  return getToken(CcpnPKParser::Assign_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Assign_F2() {
  return getToken(CcpnPKParser::Assign_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Assign_F3() {
  return getToken(CcpnPKParser::Assign_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Position_F1() {
  return getToken(CcpnPKParser::Position_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Shift_F1() {
  return getToken(CcpnPKParser::Shift_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Position_F1_() {
  return getToken(CcpnPKParser::Position_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Shift_F1_() {
  return getToken(CcpnPKParser::Shift_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Position_F2() {
  return getToken(CcpnPKParser::Position_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Shift_F2() {
  return getToken(CcpnPKParser::Shift_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Position_F3() {
  return getToken(CcpnPKParser::Position_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Shift_F3() {
  return getToken(CcpnPKParser::Shift_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_3dContext::Assign_F1() {
  return getToken(CcpnPKParser::Assign_F1, 0);
}


size_t CcpnPKParser::Peak_list_3dContext::getRuleIndex() const {
  return CcpnPKParser::RulePeak_list_3d;
}


std::any CcpnPKParser::Peak_list_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_3d(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Peak_list_3dContext* CcpnPKParser::peak_list_3d() {
  Peak_list_3dContext *_localctx = _tracker.createInstance<Peak_list_3dContext>(_ctx, getState());
  enterRule(_localctx, 6, CcpnPKParser::RulePeak_list_3d);
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
    setState(137);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Num) {
      setState(136);
      match(CcpnPKParser::Num);
    }
    setState(140);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Id

    || _la == CcpnPKParser::Id_) {
      setState(139);
      _la = _input->LA(1);
      if (!(_la == CcpnPKParser::Id

      || _la == CcpnPKParser::Id_)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
    }
    setState(154);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CcpnPKParser::Position_F1:
      case CcpnPKParser::Shift_F1:
      case CcpnPKParser::Position_F1_:
      case CcpnPKParser::Shift_F1_: {
        setState(142);
        _la = _input->LA(1);
        if (!((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 4456496) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(143);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F2

        || _la == CcpnPKParser::Shift_F2)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(144);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F3

        || _la == CcpnPKParser::Shift_F3)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(145);
        match(CcpnPKParser::Assign_F1_);
        setState(146);
        match(CcpnPKParser::Assign_F2);
        setState(147);
        match(CcpnPKParser::Assign_F3);
        break;
      }

      case CcpnPKParser::Assign_F1:
      case CcpnPKParser::Assign_F1_: {
        setState(148);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Assign_F1

        || _la == CcpnPKParser::Assign_F1_)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(149);
        match(CcpnPKParser::Assign_F2);
        setState(150);
        match(CcpnPKParser::Assign_F3);
        setState(151);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Shift_F1

        || _la == CcpnPKParser::Position_F1_)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(152);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F2

        || _la == CcpnPKParser::Shift_F2)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(153);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F3

        || _la == CcpnPKParser::Shift_F3)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(157);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Height) {
      setState(156);
      match(CcpnPKParser::Height);
    }
    setState(160);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Volume) {
      setState(159);
      match(CcpnPKParser::Volume);
    }
    setState(163);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F1) {
      setState(162);
      match(CcpnPKParser::Line_width_F1);
    }
    setState(166);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F2) {
      setState(165);
      match(CcpnPKParser::Line_width_F2);
    }
    setState(169);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F3) {
      setState(168);
      match(CcpnPKParser::Line_width_F3);
    }
    setState(172);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Merit) {
      setState(171);
      match(CcpnPKParser::Merit);
    }
    setState(175);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Details) {
      setState(174);
      match(CcpnPKParser::Details);
    }
    setState(178);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Fit_method) {
      setState(177);
      match(CcpnPKParser::Fit_method);
    }
    setState(181);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Vol_method) {
      setState(180);
      match(CcpnPKParser::Vol_method);
    }
    setState(183);
    match(CcpnPKParser::RETURN_VARS);
    setState(185); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(184);
      peak_3d();
      setState(187); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2496) != 0));
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_3dContext ------------------------------------------------------------------

CcpnPKParser::Peak_3dContext::Peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::Peak_3dContext::RETURN() {
  return getToken(CcpnPKParser::RETURN, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_3dContext::EOF() {
  return getToken(CcpnPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CcpnPKParser::Peak_3dContext::Integer() {
  return getTokens(CcpnPKParser::Integer);
}

tree::TerminalNode* CcpnPKParser::Peak_3dContext::Integer(size_t i) {
  return getToken(CcpnPKParser::Integer, i);
}

std::vector<CcpnPKParser::NumberContext *> CcpnPKParser::Peak_3dContext::number() {
  return getRuleContexts<CcpnPKParser::NumberContext>();
}

CcpnPKParser::NumberContext* CcpnPKParser::Peak_3dContext::number(size_t i) {
  return getRuleContext<CcpnPKParser::NumberContext>(i);
}

std::vector<CcpnPKParser::PositionContext *> CcpnPKParser::Peak_3dContext::position() {
  return getRuleContexts<CcpnPKParser::PositionContext>();
}

CcpnPKParser::PositionContext* CcpnPKParser::Peak_3dContext::position(size_t i) {
  return getRuleContext<CcpnPKParser::PositionContext>(i);
}

std::vector<CcpnPKParser::NoteContext *> CcpnPKParser::Peak_3dContext::note() {
  return getRuleContexts<CcpnPKParser::NoteContext>();
}

CcpnPKParser::NoteContext* CcpnPKParser::Peak_3dContext::note(size_t i) {
  return getRuleContext<CcpnPKParser::NoteContext>(i);
}

std::vector<tree::TerminalNode *> CcpnPKParser::Peak_3dContext::Simple_name() {
  return getTokens(CcpnPKParser::Simple_name);
}

tree::TerminalNode* CcpnPKParser::Peak_3dContext::Simple_name(size_t i) {
  return getToken(CcpnPKParser::Simple_name, i);
}


size_t CcpnPKParser::Peak_3dContext::getRuleIndex() const {
  return CcpnPKParser::RulePeak_3d;
}


std::any CcpnPKParser::Peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Peak_3dContext* CcpnPKParser::peak_3d() {
  Peak_3dContext *_localctx = _tracker.createInstance<Peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 8, CcpnPKParser::RulePeak_3d);
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
    setState(190);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 37, _ctx)) {
    case 1: {
      setState(189);
      match(CcpnPKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(193);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 38, _ctx)) {
    case 1: {
      setState(192);
      match(CcpnPKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(209);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 39, _ctx)) {
    case 1: {
      setState(195);
      position();
      setState(196);
      position();
      setState(197);
      position();
      setState(198);
      match(CcpnPKParser::Simple_name);
      setState(199);
      match(CcpnPKParser::Simple_name);
      setState(200);
      match(CcpnPKParser::Simple_name);
      break;
    }

    case 2: {
      setState(202);
      match(CcpnPKParser::Simple_name);
      setState(203);
      match(CcpnPKParser::Simple_name);
      setState(204);
      match(CcpnPKParser::Simple_name);
      setState(205);
      position();
      setState(206);
      position();
      setState(207);
      position();
      break;
    }

    default:
      break;
    }
    setState(212);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 40, _ctx)) {
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

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 41, _ctx)) {
    case 1: {
      setState(214);
      number();
      break;
    }

    default:
      break;
    }
    setState(218);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 42, _ctx)) {
    case 1: {
      setState(217);
      position();
      break;
    }

    default:
      break;
    }
    setState(221);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 43, _ctx)) {
    case 1: {
      setState(220);
      position();
      break;
    }

    default:
      break;
    }
    setState(224);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 44, _ctx)) {
    case 1: {
      setState(223);
      position();
      break;
    }

    default:
      break;
    }
    setState(227);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 45, _ctx)) {
    case 1: {
      setState(226);
      position();
      break;
    }

    default:
      break;
    }
    setState(232);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 6592) != 0)) {
      setState(229);
      note();
      setState(234);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(235);
    _la = _input->LA(1);
    if (!(_la == CcpnPKParser::EOF

    || _la == CcpnPKParser::RETURN)) {
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

CcpnPKParser::Peak_list_4dContext::Peak_list_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::RETURN_VARS() {
  return getToken(CcpnPKParser::RETURN_VARS, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Num() {
  return getToken(CcpnPKParser::Num, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Height() {
  return getToken(CcpnPKParser::Height, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Volume() {
  return getToken(CcpnPKParser::Volume, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Line_width_F1() {
  return getToken(CcpnPKParser::Line_width_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Line_width_F2() {
  return getToken(CcpnPKParser::Line_width_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Line_width_F3() {
  return getToken(CcpnPKParser::Line_width_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Line_width_F4() {
  return getToken(CcpnPKParser::Line_width_F4, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Merit() {
  return getToken(CcpnPKParser::Merit, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Details() {
  return getToken(CcpnPKParser::Details, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Fit_method() {
  return getToken(CcpnPKParser::Fit_method, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Vol_method() {
  return getToken(CcpnPKParser::Vol_method, 0);
}

std::vector<CcpnPKParser::Peak_4dContext *> CcpnPKParser::Peak_list_4dContext::peak_4d() {
  return getRuleContexts<CcpnPKParser::Peak_4dContext>();
}

CcpnPKParser::Peak_4dContext* CcpnPKParser::Peak_list_4dContext::peak_4d(size_t i) {
  return getRuleContext<CcpnPKParser::Peak_4dContext>(i);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Id() {
  return getToken(CcpnPKParser::Id, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Id_() {
  return getToken(CcpnPKParser::Id_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Assign_F1_() {
  return getToken(CcpnPKParser::Assign_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Assign_F2() {
  return getToken(CcpnPKParser::Assign_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Assign_F3() {
  return getToken(CcpnPKParser::Assign_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Assign_F4() {
  return getToken(CcpnPKParser::Assign_F4, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Position_F1() {
  return getToken(CcpnPKParser::Position_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Shift_F1() {
  return getToken(CcpnPKParser::Shift_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Position_F1_() {
  return getToken(CcpnPKParser::Position_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Shift_F1_() {
  return getToken(CcpnPKParser::Shift_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Position_F2() {
  return getToken(CcpnPKParser::Position_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Shift_F2() {
  return getToken(CcpnPKParser::Shift_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Position_F3() {
  return getToken(CcpnPKParser::Position_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Shift_F3() {
  return getToken(CcpnPKParser::Shift_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Position_F4() {
  return getToken(CcpnPKParser::Position_F4, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Shift_F4() {
  return getToken(CcpnPKParser::Shift_F4, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_4dContext::Assign_F1() {
  return getToken(CcpnPKParser::Assign_F1, 0);
}


size_t CcpnPKParser::Peak_list_4dContext::getRuleIndex() const {
  return CcpnPKParser::RulePeak_list_4d;
}


std::any CcpnPKParser::Peak_list_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_4d(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Peak_list_4dContext* CcpnPKParser::peak_list_4d() {
  Peak_list_4dContext *_localctx = _tracker.createInstance<Peak_list_4dContext>(_ctx, getState());
  enterRule(_localctx, 10, CcpnPKParser::RulePeak_list_4d);
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
    setState(238);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Num) {
      setState(237);
      match(CcpnPKParser::Num);
    }
    setState(241);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Id

    || _la == CcpnPKParser::Id_) {
      setState(240);
      _la = _input->LA(1);
      if (!(_la == CcpnPKParser::Id

      || _la == CcpnPKParser::Id_)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
    }
    setState(259);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CcpnPKParser::Position_F1:
      case CcpnPKParser::Shift_F1:
      case CcpnPKParser::Position_F1_:
      case CcpnPKParser::Shift_F1_: {
        setState(243);
        _la = _input->LA(1);
        if (!((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 4456496) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(244);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F2

        || _la == CcpnPKParser::Shift_F2)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(245);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F3

        || _la == CcpnPKParser::Shift_F3)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(246);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F4

        || _la == CcpnPKParser::Shift_F4)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(247);
        match(CcpnPKParser::Assign_F1_);
        setState(248);
        match(CcpnPKParser::Assign_F2);
        setState(249);
        match(CcpnPKParser::Assign_F3);
        setState(250);
        match(CcpnPKParser::Assign_F4);
        break;
      }

      case CcpnPKParser::Assign_F1:
      case CcpnPKParser::Assign_F1_: {
        setState(251);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Assign_F1

        || _la == CcpnPKParser::Assign_F1_)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(252);
        match(CcpnPKParser::Assign_F2);
        setState(253);
        match(CcpnPKParser::Assign_F3);
        setState(254);
        match(CcpnPKParser::Assign_F4);
        setState(255);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Shift_F1

        || _la == CcpnPKParser::Position_F1_)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(256);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F2

        || _la == CcpnPKParser::Shift_F2)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(257);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F3

        || _la == CcpnPKParser::Shift_F3)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(258);
        _la = _input->LA(1);
        if (!(_la == CcpnPKParser::Position_F4

        || _la == CcpnPKParser::Shift_F4)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(262);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Height) {
      setState(261);
      match(CcpnPKParser::Height);
    }
    setState(265);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Volume) {
      setState(264);
      match(CcpnPKParser::Volume);
    }
    setState(268);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F1) {
      setState(267);
      match(CcpnPKParser::Line_width_F1);
    }
    setState(271);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F2) {
      setState(270);
      match(CcpnPKParser::Line_width_F2);
    }
    setState(274);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F3) {
      setState(273);
      match(CcpnPKParser::Line_width_F3);
    }
    setState(277);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F4) {
      setState(276);
      match(CcpnPKParser::Line_width_F4);
    }
    setState(280);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Merit) {
      setState(279);
      match(CcpnPKParser::Merit);
    }
    setState(283);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Details) {
      setState(282);
      match(CcpnPKParser::Details);
    }
    setState(286);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Fit_method) {
      setState(285);
      match(CcpnPKParser::Fit_method);
    }
    setState(289);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Vol_method) {
      setState(288);
      match(CcpnPKParser::Vol_method);
    }
    setState(291);
    match(CcpnPKParser::RETURN_VARS);
    setState(293); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(292);
      peak_4d();
      setState(295); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2496) != 0));
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_4dContext ------------------------------------------------------------------

CcpnPKParser::Peak_4dContext::Peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::Peak_4dContext::RETURN() {
  return getToken(CcpnPKParser::RETURN, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_4dContext::EOF() {
  return getToken(CcpnPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CcpnPKParser::Peak_4dContext::Integer() {
  return getTokens(CcpnPKParser::Integer);
}

tree::TerminalNode* CcpnPKParser::Peak_4dContext::Integer(size_t i) {
  return getToken(CcpnPKParser::Integer, i);
}

std::vector<CcpnPKParser::NumberContext *> CcpnPKParser::Peak_4dContext::number() {
  return getRuleContexts<CcpnPKParser::NumberContext>();
}

CcpnPKParser::NumberContext* CcpnPKParser::Peak_4dContext::number(size_t i) {
  return getRuleContext<CcpnPKParser::NumberContext>(i);
}

std::vector<CcpnPKParser::PositionContext *> CcpnPKParser::Peak_4dContext::position() {
  return getRuleContexts<CcpnPKParser::PositionContext>();
}

CcpnPKParser::PositionContext* CcpnPKParser::Peak_4dContext::position(size_t i) {
  return getRuleContext<CcpnPKParser::PositionContext>(i);
}

std::vector<CcpnPKParser::NoteContext *> CcpnPKParser::Peak_4dContext::note() {
  return getRuleContexts<CcpnPKParser::NoteContext>();
}

CcpnPKParser::NoteContext* CcpnPKParser::Peak_4dContext::note(size_t i) {
  return getRuleContext<CcpnPKParser::NoteContext>(i);
}

std::vector<tree::TerminalNode *> CcpnPKParser::Peak_4dContext::Simple_name() {
  return getTokens(CcpnPKParser::Simple_name);
}

tree::TerminalNode* CcpnPKParser::Peak_4dContext::Simple_name(size_t i) {
  return getToken(CcpnPKParser::Simple_name, i);
}


size_t CcpnPKParser::Peak_4dContext::getRuleIndex() const {
  return CcpnPKParser::RulePeak_4d;
}


std::any CcpnPKParser::Peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Peak_4dContext* CcpnPKParser::peak_4d() {
  Peak_4dContext *_localctx = _tracker.createInstance<Peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 12, CcpnPKParser::RulePeak_4d);
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
    setState(298);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 61, _ctx)) {
    case 1: {
      setState(297);
      match(CcpnPKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(301);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 62, _ctx)) {
    case 1: {
      setState(300);
      match(CcpnPKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(321);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 63, _ctx)) {
    case 1: {
      setState(303);
      position();
      setState(304);
      position();
      setState(305);
      position();
      setState(306);
      position();
      setState(307);
      match(CcpnPKParser::Simple_name);
      setState(308);
      match(CcpnPKParser::Simple_name);
      setState(309);
      match(CcpnPKParser::Simple_name);
      setState(310);
      match(CcpnPKParser::Simple_name);
      break;
    }

    case 2: {
      setState(312);
      match(CcpnPKParser::Simple_name);
      setState(313);
      match(CcpnPKParser::Simple_name);
      setState(314);
      match(CcpnPKParser::Simple_name);
      setState(315);
      match(CcpnPKParser::Simple_name);
      setState(316);
      position();
      setState(317);
      position();
      setState(318);
      position();
      setState(319);
      position();
      break;
    }

    default:
      break;
    }
    setState(324);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 64, _ctx)) {
    case 1: {
      setState(323);
      number();
      break;
    }

    default:
      break;
    }
    setState(327);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 65, _ctx)) {
    case 1: {
      setState(326);
      number();
      break;
    }

    default:
      break;
    }
    setState(330);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 66, _ctx)) {
    case 1: {
      setState(329);
      position();
      break;
    }

    default:
      break;
    }
    setState(333);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 67, _ctx)) {
    case 1: {
      setState(332);
      position();
      break;
    }

    default:
      break;
    }
    setState(336);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 68, _ctx)) {
    case 1: {
      setState(335);
      position();
      break;
    }

    default:
      break;
    }
    setState(339);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 69, _ctx)) {
    case 1: {
      setState(338);
      position();
      break;
    }

    default:
      break;
    }
    setState(342);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 70, _ctx)) {
    case 1: {
      setState(341);
      position();
      break;
    }

    default:
      break;
    }
    setState(347);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 6592) != 0)) {
      setState(344);
      note();
      setState(349);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(350);
    _la = _input->LA(1);
    if (!(_la == CcpnPKParser::EOF

    || _la == CcpnPKParser::RETURN)) {
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

//----------------- Peak_list_wo_assign_2dContext ------------------------------------------------------------------

CcpnPKParser::Peak_list_wo_assign_2dContext::Peak_list_wo_assign_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::RETURN_VARS() {
  return getToken(CcpnPKParser::RETURN_VARS, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Position_F1() {
  return getToken(CcpnPKParser::Position_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Shift_F1() {
  return getToken(CcpnPKParser::Shift_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Position_F1_() {
  return getToken(CcpnPKParser::Position_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Shift_F1_() {
  return getToken(CcpnPKParser::Shift_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Position_F2() {
  return getToken(CcpnPKParser::Position_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Shift_F2() {
  return getToken(CcpnPKParser::Shift_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Num() {
  return getToken(CcpnPKParser::Num, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Height() {
  return getToken(CcpnPKParser::Height, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Volume() {
  return getToken(CcpnPKParser::Volume, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Line_width_F1() {
  return getToken(CcpnPKParser::Line_width_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Line_width_F2() {
  return getToken(CcpnPKParser::Line_width_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Merit() {
  return getToken(CcpnPKParser::Merit, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Details() {
  return getToken(CcpnPKParser::Details, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Fit_method() {
  return getToken(CcpnPKParser::Fit_method, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Vol_method() {
  return getToken(CcpnPKParser::Vol_method, 0);
}

std::vector<CcpnPKParser::Peak_wo_assign_2dContext *> CcpnPKParser::Peak_list_wo_assign_2dContext::peak_wo_assign_2d() {
  return getRuleContexts<CcpnPKParser::Peak_wo_assign_2dContext>();
}

CcpnPKParser::Peak_wo_assign_2dContext* CcpnPKParser::Peak_list_wo_assign_2dContext::peak_wo_assign_2d(size_t i) {
  return getRuleContext<CcpnPKParser::Peak_wo_assign_2dContext>(i);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Id() {
  return getToken(CcpnPKParser::Id, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_2dContext::Id_() {
  return getToken(CcpnPKParser::Id_, 0);
}


size_t CcpnPKParser::Peak_list_wo_assign_2dContext::getRuleIndex() const {
  return CcpnPKParser::RulePeak_list_wo_assign_2d;
}


std::any CcpnPKParser::Peak_list_wo_assign_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_wo_assign_2d(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Peak_list_wo_assign_2dContext* CcpnPKParser::peak_list_wo_assign_2d() {
  Peak_list_wo_assign_2dContext *_localctx = _tracker.createInstance<Peak_list_wo_assign_2dContext>(_ctx, getState());
  enterRule(_localctx, 14, CcpnPKParser::RulePeak_list_wo_assign_2d);
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
    setState(353);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Num) {
      setState(352);
      match(CcpnPKParser::Num);
    }
    setState(356);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Id

    || _la == CcpnPKParser::Id_) {
      setState(355);
      _la = _input->LA(1);
      if (!(_la == CcpnPKParser::Id

      || _la == CcpnPKParser::Id_)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
    }
    setState(358);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 4456496) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(359);
    _la = _input->LA(1);
    if (!(_la == CcpnPKParser::Position_F2

    || _la == CcpnPKParser::Shift_F2)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(361);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Height) {
      setState(360);
      match(CcpnPKParser::Height);
    }
    setState(364);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Volume) {
      setState(363);
      match(CcpnPKParser::Volume);
    }
    setState(367);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F1) {
      setState(366);
      match(CcpnPKParser::Line_width_F1);
    }
    setState(370);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F2) {
      setState(369);
      match(CcpnPKParser::Line_width_F2);
    }
    setState(373);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Merit) {
      setState(372);
      match(CcpnPKParser::Merit);
    }
    setState(376);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Details) {
      setState(375);
      match(CcpnPKParser::Details);
    }
    setState(379);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Fit_method) {
      setState(378);
      match(CcpnPKParser::Fit_method);
    }
    setState(382);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Vol_method) {
      setState(381);
      match(CcpnPKParser::Vol_method);
    }
    setState(384);
    match(CcpnPKParser::RETURN_VARS);
    setState(386); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(385);
      peak_wo_assign_2d();
      setState(388); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2496) != 0));
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_wo_assign_2dContext ------------------------------------------------------------------

CcpnPKParser::Peak_wo_assign_2dContext::Peak_wo_assign_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CcpnPKParser::PositionContext *> CcpnPKParser::Peak_wo_assign_2dContext::position() {
  return getRuleContexts<CcpnPKParser::PositionContext>();
}

CcpnPKParser::PositionContext* CcpnPKParser::Peak_wo_assign_2dContext::position(size_t i) {
  return getRuleContext<CcpnPKParser::PositionContext>(i);
}

tree::TerminalNode* CcpnPKParser::Peak_wo_assign_2dContext::RETURN() {
  return getToken(CcpnPKParser::RETURN, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_wo_assign_2dContext::EOF() {
  return getToken(CcpnPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CcpnPKParser::Peak_wo_assign_2dContext::Integer() {
  return getTokens(CcpnPKParser::Integer);
}

tree::TerminalNode* CcpnPKParser::Peak_wo_assign_2dContext::Integer(size_t i) {
  return getToken(CcpnPKParser::Integer, i);
}

std::vector<CcpnPKParser::NumberContext *> CcpnPKParser::Peak_wo_assign_2dContext::number() {
  return getRuleContexts<CcpnPKParser::NumberContext>();
}

CcpnPKParser::NumberContext* CcpnPKParser::Peak_wo_assign_2dContext::number(size_t i) {
  return getRuleContext<CcpnPKParser::NumberContext>(i);
}

std::vector<CcpnPKParser::NoteContext *> CcpnPKParser::Peak_wo_assign_2dContext::note() {
  return getRuleContexts<CcpnPKParser::NoteContext>();
}

CcpnPKParser::NoteContext* CcpnPKParser::Peak_wo_assign_2dContext::note(size_t i) {
  return getRuleContext<CcpnPKParser::NoteContext>(i);
}


size_t CcpnPKParser::Peak_wo_assign_2dContext::getRuleIndex() const {
  return CcpnPKParser::RulePeak_wo_assign_2d;
}


std::any CcpnPKParser::Peak_wo_assign_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_assign_2d(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Peak_wo_assign_2dContext* CcpnPKParser::peak_wo_assign_2d() {
  Peak_wo_assign_2dContext *_localctx = _tracker.createInstance<Peak_wo_assign_2dContext>(_ctx, getState());
  enterRule(_localctx, 16, CcpnPKParser::RulePeak_wo_assign_2d);
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
    setState(391);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 83, _ctx)) {
    case 1: {
      setState(390);
      match(CcpnPKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(394);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 84, _ctx)) {
    case 1: {
      setState(393);
      match(CcpnPKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(396);
    position();
    setState(397);
    position();
    setState(399);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 85, _ctx)) {
    case 1: {
      setState(398);
      number();
      break;
    }

    default:
      break;
    }
    setState(402);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 86, _ctx)) {
    case 1: {
      setState(401);
      number();
      break;
    }

    default:
      break;
    }
    setState(405);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 87, _ctx)) {
    case 1: {
      setState(404);
      position();
      break;
    }

    default:
      break;
    }
    setState(408);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 88, _ctx)) {
    case 1: {
      setState(407);
      position();
      break;
    }

    default:
      break;
    }
    setState(411);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 89, _ctx)) {
    case 1: {
      setState(410);
      position();
      break;
    }

    default:
      break;
    }
    setState(416);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 6592) != 0)) {
      setState(413);
      note();
      setState(418);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(419);
    _la = _input->LA(1);
    if (!(_la == CcpnPKParser::EOF

    || _la == CcpnPKParser::RETURN)) {
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

//----------------- Peak_list_wo_assign_3dContext ------------------------------------------------------------------

CcpnPKParser::Peak_list_wo_assign_3dContext::Peak_list_wo_assign_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::RETURN_VARS() {
  return getToken(CcpnPKParser::RETURN_VARS, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Position_F1() {
  return getToken(CcpnPKParser::Position_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Shift_F1() {
  return getToken(CcpnPKParser::Shift_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Position_F1_() {
  return getToken(CcpnPKParser::Position_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Shift_F1_() {
  return getToken(CcpnPKParser::Shift_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Position_F2() {
  return getToken(CcpnPKParser::Position_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Shift_F2() {
  return getToken(CcpnPKParser::Shift_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Position_F3() {
  return getToken(CcpnPKParser::Position_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Shift_F3() {
  return getToken(CcpnPKParser::Shift_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Num() {
  return getToken(CcpnPKParser::Num, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Height() {
  return getToken(CcpnPKParser::Height, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Volume() {
  return getToken(CcpnPKParser::Volume, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Line_width_F1() {
  return getToken(CcpnPKParser::Line_width_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Line_width_F2() {
  return getToken(CcpnPKParser::Line_width_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Line_width_F3() {
  return getToken(CcpnPKParser::Line_width_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Merit() {
  return getToken(CcpnPKParser::Merit, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Details() {
  return getToken(CcpnPKParser::Details, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Fit_method() {
  return getToken(CcpnPKParser::Fit_method, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Vol_method() {
  return getToken(CcpnPKParser::Vol_method, 0);
}

std::vector<CcpnPKParser::Peak_wo_assign_3dContext *> CcpnPKParser::Peak_list_wo_assign_3dContext::peak_wo_assign_3d() {
  return getRuleContexts<CcpnPKParser::Peak_wo_assign_3dContext>();
}

CcpnPKParser::Peak_wo_assign_3dContext* CcpnPKParser::Peak_list_wo_assign_3dContext::peak_wo_assign_3d(size_t i) {
  return getRuleContext<CcpnPKParser::Peak_wo_assign_3dContext>(i);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Id() {
  return getToken(CcpnPKParser::Id, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_3dContext::Id_() {
  return getToken(CcpnPKParser::Id_, 0);
}


size_t CcpnPKParser::Peak_list_wo_assign_3dContext::getRuleIndex() const {
  return CcpnPKParser::RulePeak_list_wo_assign_3d;
}


std::any CcpnPKParser::Peak_list_wo_assign_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_wo_assign_3d(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Peak_list_wo_assign_3dContext* CcpnPKParser::peak_list_wo_assign_3d() {
  Peak_list_wo_assign_3dContext *_localctx = _tracker.createInstance<Peak_list_wo_assign_3dContext>(_ctx, getState());
  enterRule(_localctx, 18, CcpnPKParser::RulePeak_list_wo_assign_3d);
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
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Num) {
      setState(421);
      match(CcpnPKParser::Num);
    }
    setState(425);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Id

    || _la == CcpnPKParser::Id_) {
      setState(424);
      _la = _input->LA(1);
      if (!(_la == CcpnPKParser::Id

      || _la == CcpnPKParser::Id_)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
    }
    setState(427);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 4456496) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(428);
    _la = _input->LA(1);
    if (!(_la == CcpnPKParser::Position_F2

    || _la == CcpnPKParser::Shift_F2)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(429);
    _la = _input->LA(1);
    if (!(_la == CcpnPKParser::Position_F3

    || _la == CcpnPKParser::Shift_F3)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(431);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Height) {
      setState(430);
      match(CcpnPKParser::Height);
    }
    setState(434);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Volume) {
      setState(433);
      match(CcpnPKParser::Volume);
    }
    setState(437);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F1) {
      setState(436);
      match(CcpnPKParser::Line_width_F1);
    }
    setState(440);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F2) {
      setState(439);
      match(CcpnPKParser::Line_width_F2);
    }
    setState(443);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F3) {
      setState(442);
      match(CcpnPKParser::Line_width_F3);
    }
    setState(446);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Merit) {
      setState(445);
      match(CcpnPKParser::Merit);
    }
    setState(449);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Details) {
      setState(448);
      match(CcpnPKParser::Details);
    }
    setState(452);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Fit_method) {
      setState(451);
      match(CcpnPKParser::Fit_method);
    }
    setState(455);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Vol_method) {
      setState(454);
      match(CcpnPKParser::Vol_method);
    }
    setState(457);
    match(CcpnPKParser::RETURN_VARS);
    setState(459); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(458);
      peak_wo_assign_3d();
      setState(461); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2496) != 0));
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_wo_assign_3dContext ------------------------------------------------------------------

CcpnPKParser::Peak_wo_assign_3dContext::Peak_wo_assign_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CcpnPKParser::PositionContext *> CcpnPKParser::Peak_wo_assign_3dContext::position() {
  return getRuleContexts<CcpnPKParser::PositionContext>();
}

CcpnPKParser::PositionContext* CcpnPKParser::Peak_wo_assign_3dContext::position(size_t i) {
  return getRuleContext<CcpnPKParser::PositionContext>(i);
}

tree::TerminalNode* CcpnPKParser::Peak_wo_assign_3dContext::RETURN() {
  return getToken(CcpnPKParser::RETURN, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_wo_assign_3dContext::EOF() {
  return getToken(CcpnPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CcpnPKParser::Peak_wo_assign_3dContext::Integer() {
  return getTokens(CcpnPKParser::Integer);
}

tree::TerminalNode* CcpnPKParser::Peak_wo_assign_3dContext::Integer(size_t i) {
  return getToken(CcpnPKParser::Integer, i);
}

std::vector<CcpnPKParser::NumberContext *> CcpnPKParser::Peak_wo_assign_3dContext::number() {
  return getRuleContexts<CcpnPKParser::NumberContext>();
}

CcpnPKParser::NumberContext* CcpnPKParser::Peak_wo_assign_3dContext::number(size_t i) {
  return getRuleContext<CcpnPKParser::NumberContext>(i);
}

std::vector<CcpnPKParser::NoteContext *> CcpnPKParser::Peak_wo_assign_3dContext::note() {
  return getRuleContexts<CcpnPKParser::NoteContext>();
}

CcpnPKParser::NoteContext* CcpnPKParser::Peak_wo_assign_3dContext::note(size_t i) {
  return getRuleContext<CcpnPKParser::NoteContext>(i);
}


size_t CcpnPKParser::Peak_wo_assign_3dContext::getRuleIndex() const {
  return CcpnPKParser::RulePeak_wo_assign_3d;
}


std::any CcpnPKParser::Peak_wo_assign_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_assign_3d(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Peak_wo_assign_3dContext* CcpnPKParser::peak_wo_assign_3d() {
  Peak_wo_assign_3dContext *_localctx = _tracker.createInstance<Peak_wo_assign_3dContext>(_ctx, getState());
  enterRule(_localctx, 20, CcpnPKParser::RulePeak_wo_assign_3d);
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
    setState(464);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 103, _ctx)) {
    case 1: {
      setState(463);
      match(CcpnPKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(467);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 104, _ctx)) {
    case 1: {
      setState(466);
      match(CcpnPKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(469);
    position();
    setState(470);
    position();
    setState(471);
    position();
    setState(473);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 105, _ctx)) {
    case 1: {
      setState(472);
      number();
      break;
    }

    default:
      break;
    }
    setState(476);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 106, _ctx)) {
    case 1: {
      setState(475);
      number();
      break;
    }

    default:
      break;
    }
    setState(479);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 107, _ctx)) {
    case 1: {
      setState(478);
      position();
      break;
    }

    default:
      break;
    }
    setState(482);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 108, _ctx)) {
    case 1: {
      setState(481);
      position();
      break;
    }

    default:
      break;
    }
    setState(485);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 109, _ctx)) {
    case 1: {
      setState(484);
      position();
      break;
    }

    default:
      break;
    }
    setState(488);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 110, _ctx)) {
    case 1: {
      setState(487);
      position();
      break;
    }

    default:
      break;
    }
    setState(493);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 6592) != 0)) {
      setState(490);
      note();
      setState(495);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(496);
    _la = _input->LA(1);
    if (!(_la == CcpnPKParser::EOF

    || _la == CcpnPKParser::RETURN)) {
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

//----------------- Peak_list_wo_assign_4dContext ------------------------------------------------------------------

CcpnPKParser::Peak_list_wo_assign_4dContext::Peak_list_wo_assign_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::RETURN_VARS() {
  return getToken(CcpnPKParser::RETURN_VARS, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Position_F1() {
  return getToken(CcpnPKParser::Position_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Shift_F1() {
  return getToken(CcpnPKParser::Shift_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Position_F1_() {
  return getToken(CcpnPKParser::Position_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Shift_F1_() {
  return getToken(CcpnPKParser::Shift_F1_, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Position_F2() {
  return getToken(CcpnPKParser::Position_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Shift_F2() {
  return getToken(CcpnPKParser::Shift_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Position_F3() {
  return getToken(CcpnPKParser::Position_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Shift_F3() {
  return getToken(CcpnPKParser::Shift_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Position_F4() {
  return getToken(CcpnPKParser::Position_F4, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Shift_F4() {
  return getToken(CcpnPKParser::Shift_F4, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Num() {
  return getToken(CcpnPKParser::Num, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Height() {
  return getToken(CcpnPKParser::Height, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Volume() {
  return getToken(CcpnPKParser::Volume, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Line_width_F1() {
  return getToken(CcpnPKParser::Line_width_F1, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Line_width_F2() {
  return getToken(CcpnPKParser::Line_width_F2, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Line_width_F3() {
  return getToken(CcpnPKParser::Line_width_F3, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Line_width_F4() {
  return getToken(CcpnPKParser::Line_width_F4, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Merit() {
  return getToken(CcpnPKParser::Merit, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Details() {
  return getToken(CcpnPKParser::Details, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Fit_method() {
  return getToken(CcpnPKParser::Fit_method, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Vol_method() {
  return getToken(CcpnPKParser::Vol_method, 0);
}

std::vector<CcpnPKParser::Peak_wo_assign_4dContext *> CcpnPKParser::Peak_list_wo_assign_4dContext::peak_wo_assign_4d() {
  return getRuleContexts<CcpnPKParser::Peak_wo_assign_4dContext>();
}

CcpnPKParser::Peak_wo_assign_4dContext* CcpnPKParser::Peak_list_wo_assign_4dContext::peak_wo_assign_4d(size_t i) {
  return getRuleContext<CcpnPKParser::Peak_wo_assign_4dContext>(i);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Id() {
  return getToken(CcpnPKParser::Id, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_list_wo_assign_4dContext::Id_() {
  return getToken(CcpnPKParser::Id_, 0);
}


size_t CcpnPKParser::Peak_list_wo_assign_4dContext::getRuleIndex() const {
  return CcpnPKParser::RulePeak_list_wo_assign_4d;
}


std::any CcpnPKParser::Peak_list_wo_assign_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_wo_assign_4d(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Peak_list_wo_assign_4dContext* CcpnPKParser::peak_list_wo_assign_4d() {
  Peak_list_wo_assign_4dContext *_localctx = _tracker.createInstance<Peak_list_wo_assign_4dContext>(_ctx, getState());
  enterRule(_localctx, 22, CcpnPKParser::RulePeak_list_wo_assign_4d);
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
    setState(499);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Num) {
      setState(498);
      match(CcpnPKParser::Num);
    }
    setState(502);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Id

    || _la == CcpnPKParser::Id_) {
      setState(501);
      _la = _input->LA(1);
      if (!(_la == CcpnPKParser::Id

      || _la == CcpnPKParser::Id_)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
    }
    setState(504);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 4456496) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(505);
    _la = _input->LA(1);
    if (!(_la == CcpnPKParser::Position_F2

    || _la == CcpnPKParser::Shift_F2)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(506);
    _la = _input->LA(1);
    if (!(_la == CcpnPKParser::Position_F3

    || _la == CcpnPKParser::Shift_F3)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(507);
    _la = _input->LA(1);
    if (!(_la == CcpnPKParser::Position_F4

    || _la == CcpnPKParser::Shift_F4)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(509);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Height) {
      setState(508);
      match(CcpnPKParser::Height);
    }
    setState(512);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Volume) {
      setState(511);
      match(CcpnPKParser::Volume);
    }
    setState(515);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F1) {
      setState(514);
      match(CcpnPKParser::Line_width_F1);
    }
    setState(518);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F2) {
      setState(517);
      match(CcpnPKParser::Line_width_F2);
    }
    setState(521);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F3) {
      setState(520);
      match(CcpnPKParser::Line_width_F3);
    }
    setState(524);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Line_width_F4) {
      setState(523);
      match(CcpnPKParser::Line_width_F4);
    }
    setState(527);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Merit) {
      setState(526);
      match(CcpnPKParser::Merit);
    }
    setState(530);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Details) {
      setState(529);
      match(CcpnPKParser::Details);
    }
    setState(533);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Fit_method) {
      setState(532);
      match(CcpnPKParser::Fit_method);
    }
    setState(536);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CcpnPKParser::Vol_method) {
      setState(535);
      match(CcpnPKParser::Vol_method);
    }
    setState(538);
    match(CcpnPKParser::RETURN_VARS);
    setState(540); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(539);
      peak_wo_assign_4d();
      setState(542); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2496) != 0));
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_wo_assign_4dContext ------------------------------------------------------------------

CcpnPKParser::Peak_wo_assign_4dContext::Peak_wo_assign_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CcpnPKParser::PositionContext *> CcpnPKParser::Peak_wo_assign_4dContext::position() {
  return getRuleContexts<CcpnPKParser::PositionContext>();
}

CcpnPKParser::PositionContext* CcpnPKParser::Peak_wo_assign_4dContext::position(size_t i) {
  return getRuleContext<CcpnPKParser::PositionContext>(i);
}

tree::TerminalNode* CcpnPKParser::Peak_wo_assign_4dContext::RETURN() {
  return getToken(CcpnPKParser::RETURN, 0);
}

tree::TerminalNode* CcpnPKParser::Peak_wo_assign_4dContext::EOF() {
  return getToken(CcpnPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CcpnPKParser::Peak_wo_assign_4dContext::Integer() {
  return getTokens(CcpnPKParser::Integer);
}

tree::TerminalNode* CcpnPKParser::Peak_wo_assign_4dContext::Integer(size_t i) {
  return getToken(CcpnPKParser::Integer, i);
}

std::vector<CcpnPKParser::NumberContext *> CcpnPKParser::Peak_wo_assign_4dContext::number() {
  return getRuleContexts<CcpnPKParser::NumberContext>();
}

CcpnPKParser::NumberContext* CcpnPKParser::Peak_wo_assign_4dContext::number(size_t i) {
  return getRuleContext<CcpnPKParser::NumberContext>(i);
}

std::vector<CcpnPKParser::NoteContext *> CcpnPKParser::Peak_wo_assign_4dContext::note() {
  return getRuleContexts<CcpnPKParser::NoteContext>();
}

CcpnPKParser::NoteContext* CcpnPKParser::Peak_wo_assign_4dContext::note(size_t i) {
  return getRuleContext<CcpnPKParser::NoteContext>(i);
}


size_t CcpnPKParser::Peak_wo_assign_4dContext::getRuleIndex() const {
  return CcpnPKParser::RulePeak_wo_assign_4d;
}


std::any CcpnPKParser::Peak_wo_assign_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_assign_4d(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::Peak_wo_assign_4dContext* CcpnPKParser::peak_wo_assign_4d() {
  Peak_wo_assign_4dContext *_localctx = _tracker.createInstance<Peak_wo_assign_4dContext>(_ctx, getState());
  enterRule(_localctx, 24, CcpnPKParser::RulePeak_wo_assign_4d);
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
    setState(545);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 125, _ctx)) {
    case 1: {
      setState(544);
      match(CcpnPKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(548);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 126, _ctx)) {
    case 1: {
      setState(547);
      match(CcpnPKParser::Integer);
      break;
    }

    default:
      break;
    }
    setState(550);
    position();
    setState(551);
    position();
    setState(552);
    position();
    setState(553);
    position();
    setState(555);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 127, _ctx)) {
    case 1: {
      setState(554);
      number();
      break;
    }

    default:
      break;
    }
    setState(558);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 128, _ctx)) {
    case 1: {
      setState(557);
      number();
      break;
    }

    default:
      break;
    }
    setState(561);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 129, _ctx)) {
    case 1: {
      setState(560);
      position();
      break;
    }

    default:
      break;
    }
    setState(564);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 130, _ctx)) {
    case 1: {
      setState(563);
      position();
      break;
    }

    default:
      break;
    }
    setState(567);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 131, _ctx)) {
    case 1: {
      setState(566);
      position();
      break;
    }

    default:
      break;
    }
    setState(570);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 132, _ctx)) {
    case 1: {
      setState(569);
      position();
      break;
    }

    default:
      break;
    }
    setState(573);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 133, _ctx)) {
    case 1: {
      setState(572);
      position();
      break;
    }

    default:
      break;
    }
    setState(578);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 6592) != 0)) {
      setState(575);
      note();
      setState(580);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(581);
    _la = _input->LA(1);
    if (!(_la == CcpnPKParser::EOF

    || _la == CcpnPKParser::RETURN)) {
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

//----------------- PositionContext ------------------------------------------------------------------

CcpnPKParser::PositionContext::PositionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::PositionContext::Float() {
  return getToken(CcpnPKParser::Float, 0);
}

tree::TerminalNode* CcpnPKParser::PositionContext::Real() {
  return getToken(CcpnPKParser::Real, 0);
}

tree::TerminalNode* CcpnPKParser::PositionContext::Integer() {
  return getToken(CcpnPKParser::Integer, 0);
}

tree::TerminalNode* CcpnPKParser::PositionContext::Simple_name() {
  return getToken(CcpnPKParser::Simple_name, 0);
}


size_t CcpnPKParser::PositionContext::getRuleIndex() const {
  return CcpnPKParser::RulePosition;
}


std::any CcpnPKParser::PositionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitPosition(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::PositionContext* CcpnPKParser::position() {
  PositionContext *_localctx = _tracker.createInstance<PositionContext>(_ctx, getState());
  enterRule(_localctx, 26, CcpnPKParser::RulePosition);
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
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2496) != 0))) {
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

CcpnPKParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::NumberContext::Float() {
  return getToken(CcpnPKParser::Float, 0);
}

tree::TerminalNode* CcpnPKParser::NumberContext::Real() {
  return getToken(CcpnPKParser::Real, 0);
}

tree::TerminalNode* CcpnPKParser::NumberContext::Integer() {
  return getToken(CcpnPKParser::Integer, 0);
}

tree::TerminalNode* CcpnPKParser::NumberContext::Simple_name() {
  return getToken(CcpnPKParser::Simple_name, 0);
}


size_t CcpnPKParser::NumberContext::getRuleIndex() const {
  return CcpnPKParser::RuleNumber;
}


std::any CcpnPKParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::NumberContext* CcpnPKParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 28, CcpnPKParser::RuleNumber);
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
    setState(585);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2496) != 0))) {
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

//----------------- NoteContext ------------------------------------------------------------------

CcpnPKParser::NoteContext::NoteContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CcpnPKParser::NoteContext::Float() {
  return getToken(CcpnPKParser::Float, 0);
}

tree::TerminalNode* CcpnPKParser::NoteContext::Real() {
  return getToken(CcpnPKParser::Real, 0);
}

tree::TerminalNode* CcpnPKParser::NoteContext::Integer() {
  return getToken(CcpnPKParser::Integer, 0);
}

tree::TerminalNode* CcpnPKParser::NoteContext::Simple_name() {
  return getToken(CcpnPKParser::Simple_name, 0);
}

tree::TerminalNode* CcpnPKParser::NoteContext::Any_name() {
  return getToken(CcpnPKParser::Any_name, 0);
}


size_t CcpnPKParser::NoteContext::getRuleIndex() const {
  return CcpnPKParser::RuleNote;
}


std::any CcpnPKParser::NoteContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CcpnPKParserVisitor*>(visitor))
    return parserVisitor->visitNote(this);
  else
    return visitor->visitChildren(this);
}

CcpnPKParser::NoteContext* CcpnPKParser::note() {
  NoteContext *_localctx = _tracker.createInstance<NoteContext>(_ctx, getState());
  enterRule(_localctx, 30, CcpnPKParser::RuleNote);
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
    setState(587);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 6592) != 0))) {
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

void CcpnPKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  ccpnpkparserParserInitialize();
#else
  ::antlr4::internal::call_once(ccpnpkparserParserOnceFlag, ccpnpkparserParserInitialize);
#endif
}
