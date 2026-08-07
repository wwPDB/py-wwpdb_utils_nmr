
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BarePKParser.g4 by ANTLR 4.13.0


#include "BarePKParserVisitor.h"

#include "BarePKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct BarePKParserStaticData final {
  BarePKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  BarePKParserStaticData(const BarePKParserStaticData&) = delete;
  BarePKParserStaticData(BarePKParserStaticData&&) = delete;
  BarePKParserStaticData& operator=(const BarePKParserStaticData&) = delete;
  BarePKParserStaticData& operator=(BarePKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag barepkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
BarePKParserStaticData *barepkparserParserStaticData = nullptr;

void barepkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (barepkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(barepkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<BarePKParserStaticData>(
    std::vector<std::string>{
      "bare_pk", "peak_list_2d", "peak_2d", "peak_list_3d", "peak_3d", "peak_list_4d", 
      "peak_4d", "peak_list_wo_chain_2d", "peak_wo_chain_2d", "peak_list_wo_chain_3d", 
      "peak_wo_chain_3d", "peak_list_wo_chain_4d", "peak_wo_chain_4d", "row_format_2d", 
      "row_format_3d", "row_format_4d", "rev_row_format_2d", "rev_row_format_3d", 
      "rev_row_format_4d", "row_format_wo_label_2d", "row_format_wo_label_3d", 
      "row_format_wo_label_4d", "peak_list_row_2d", "peak_list_row_3d", 
      "peak_list_row_4d", "position", "number"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "", "", "", "", "", "", "", "", "", "'Volume'"
    },
    std::vector<std::string>{
      "", "Peak", "X_PPM", "Y_PPM", "Z_PPM", "A_PPM", "Integer", "Float", 
      "Real", "Ambig_float", "SHARP_COMMENT", "EXCLM_COMMENT", "Simple_name", 
      "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT", "X_ppm", "Y_ppm", 
      "Z_ppm", "A_ppm", "X_width", "Y_width", "Z_width", "A_width", "Amplitude", 
      "Volume", "Label", "Comment", "SPACE_FO", "RETURN_FO"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,30,494,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,1,0,3,0,56,8,0,1,
  	0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,
  	75,8,0,10,0,12,0,78,9,0,1,0,1,0,1,1,4,1,83,8,1,11,1,12,1,84,1,2,1,2,1,
  	2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,98,8,2,10,2,12,2,101,9,2,1,2,1,
  	2,1,3,4,3,106,8,3,11,3,12,3,107,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
  	4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,126,8,4,10,4,12,4,129,9,4,1,4,1,4,1,5,4,
  	5,134,8,5,11,5,12,5,135,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
  	6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,159,8,6,10,6,12,6,162,9,6,1,
  	6,1,6,1,7,4,7,167,8,7,11,7,12,7,168,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
  	8,5,8,180,8,8,10,8,12,8,183,9,8,1,8,1,8,1,9,4,9,188,8,9,11,9,12,9,189,
  	1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,
  	205,8,10,10,10,12,10,208,9,10,1,10,1,10,1,11,4,11,213,8,11,11,11,12,11,
  	214,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
  	1,12,1,12,1,12,1,12,5,12,234,8,12,10,12,12,12,237,9,12,1,12,1,12,1,13,
  	1,13,1,13,3,13,244,8,13,1,13,1,13,1,13,3,13,249,8,13,1,13,3,13,252,8,
  	13,1,13,3,13,255,8,13,1,13,3,13,258,8,13,1,13,3,13,261,8,13,1,13,1,13,
  	4,13,265,8,13,11,13,12,13,266,1,14,1,14,1,14,3,14,272,8,14,1,14,1,14,
  	1,14,1,14,1,14,3,14,279,8,14,1,14,3,14,282,8,14,1,14,3,14,285,8,14,1,
  	14,3,14,288,8,14,1,14,3,14,291,8,14,1,14,1,14,4,14,295,8,14,11,14,12,
  	14,296,1,15,1,15,1,15,3,15,302,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
  	3,15,311,8,15,1,15,3,15,314,8,15,1,15,3,15,317,8,15,1,15,3,15,320,8,15,
  	1,15,3,15,323,8,15,1,15,1,15,4,15,327,8,15,11,15,12,15,328,1,16,1,16,
  	1,16,3,16,334,8,16,1,16,1,16,1,16,3,16,339,8,16,1,16,3,16,342,8,16,1,
  	16,3,16,345,8,16,1,16,3,16,348,8,16,1,16,3,16,351,8,16,1,16,1,16,4,16,
  	355,8,16,11,16,12,16,356,1,17,1,17,1,17,3,17,362,8,17,1,17,1,17,1,17,
  	1,17,1,17,3,17,369,8,17,1,17,3,17,372,8,17,1,17,3,17,375,8,17,1,17,3,
  	17,378,8,17,1,17,3,17,381,8,17,1,17,1,17,4,17,385,8,17,11,17,12,17,386,
  	1,18,1,18,1,18,3,18,392,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,
  	401,8,18,1,18,3,18,404,8,18,1,18,3,18,407,8,18,1,18,3,18,410,8,18,1,18,
  	3,18,413,8,18,1,18,1,18,4,18,417,8,18,11,18,12,18,418,1,19,4,19,422,8,
  	19,11,19,12,19,423,1,20,4,20,427,8,20,11,20,12,20,428,1,21,4,21,432,8,
  	21,11,21,12,21,433,1,22,1,22,1,22,1,22,5,22,440,8,22,10,22,12,22,443,
  	9,22,1,22,5,22,446,8,22,10,22,12,22,449,9,22,1,22,1,22,1,23,1,23,1,23,
  	1,23,1,23,5,23,458,8,23,10,23,12,23,461,9,23,1,23,5,23,464,8,23,10,23,
  	12,23,467,9,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,5,24,477,8,24,
  	10,24,12,24,480,9,24,1,24,5,24,483,8,24,10,24,12,24,486,9,24,1,24,1,24,
  	1,25,1,25,1,26,1,26,1,26,0,0,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
  	28,30,32,34,36,38,40,42,44,46,48,50,52,0,3,1,1,14,14,2,0,6,7,9,9,1,0,
  	6,8,545,0,55,1,0,0,0,2,82,1,0,0,0,4,86,1,0,0,0,6,105,1,0,0,0,8,109,1,
  	0,0,0,10,133,1,0,0,0,12,137,1,0,0,0,14,166,1,0,0,0,16,170,1,0,0,0,18,
  	187,1,0,0,0,20,191,1,0,0,0,22,212,1,0,0,0,24,216,1,0,0,0,26,243,1,0,0,
  	0,28,271,1,0,0,0,30,301,1,0,0,0,32,333,1,0,0,0,34,361,1,0,0,0,36,391,
  	1,0,0,0,38,421,1,0,0,0,40,426,1,0,0,0,42,431,1,0,0,0,44,435,1,0,0,0,46,
  	452,1,0,0,0,48,470,1,0,0,0,50,489,1,0,0,0,52,491,1,0,0,0,54,56,5,14,0,
  	0,55,54,1,0,0,0,55,56,1,0,0,0,56,76,1,0,0,0,57,75,3,2,1,0,58,75,3,6,3,
  	0,59,75,3,10,5,0,60,75,3,14,7,0,61,75,3,18,9,0,62,75,3,22,11,0,63,75,
  	3,26,13,0,64,75,3,28,14,0,65,75,3,30,15,0,66,75,3,32,16,0,67,75,3,34,
  	17,0,68,75,3,36,18,0,69,75,3,38,19,0,70,75,3,40,20,0,71,72,3,42,21,0,
  	72,73,5,14,0,0,73,75,1,0,0,0,74,57,1,0,0,0,74,58,1,0,0,0,74,59,1,0,0,
  	0,74,60,1,0,0,0,74,61,1,0,0,0,74,62,1,0,0,0,74,63,1,0,0,0,74,64,1,0,0,
  	0,74,65,1,0,0,0,74,66,1,0,0,0,74,67,1,0,0,0,74,68,1,0,0,0,74,69,1,0,0,
  	0,74,70,1,0,0,0,74,71,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,
  	0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,0,0,1,80,1,1,0,0,0,81,83,3,4,2,
  	0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,3,1,0,0,
  	0,86,87,5,12,0,0,87,88,5,6,0,0,88,89,5,12,0,0,89,90,5,12,0,0,90,91,3,
  	50,25,0,91,92,5,12,0,0,92,93,5,6,0,0,93,94,5,12,0,0,94,95,5,12,0,0,95,
  	99,3,50,25,0,96,98,3,52,26,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,
  	0,99,100,1,0,0,0,100,102,1,0,0,0,101,99,1,0,0,0,102,103,7,0,0,0,103,5,
  	1,0,0,0,104,106,3,8,4,0,105,104,1,0,0,0,106,107,1,0,0,0,107,105,1,0,0,
  	0,107,108,1,0,0,0,108,7,1,0,0,0,109,110,5,12,0,0,110,111,5,6,0,0,111,
  	112,5,12,0,0,112,113,5,12,0,0,113,114,3,50,25,0,114,115,5,12,0,0,115,
  	116,5,6,0,0,116,117,5,12,0,0,117,118,5,12,0,0,118,119,3,50,25,0,119,120,
  	5,12,0,0,120,121,5,6,0,0,121,122,5,12,0,0,122,123,5,12,0,0,123,127,3,
  	50,25,0,124,126,3,52,26,0,125,124,1,0,0,0,126,129,1,0,0,0,127,125,1,0,
  	0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,127,1,0,0,0,130,131,7,0,0,0,131,
  	9,1,0,0,0,132,134,3,12,6,0,133,132,1,0,0,0,134,135,1,0,0,0,135,133,1,
  	0,0,0,135,136,1,0,0,0,136,11,1,0,0,0,137,138,5,12,0,0,138,139,5,6,0,0,
  	139,140,5,12,0,0,140,141,5,12,0,0,141,142,3,50,25,0,142,143,5,12,0,0,
  	143,144,5,6,0,0,144,145,5,12,0,0,145,146,5,12,0,0,146,147,3,50,25,0,147,
  	148,5,12,0,0,148,149,5,6,0,0,149,150,5,12,0,0,150,151,5,12,0,0,151,152,
  	3,50,25,0,152,153,5,12,0,0,153,154,5,6,0,0,154,155,5,12,0,0,155,156,5,
  	12,0,0,156,160,3,50,25,0,157,159,3,52,26,0,158,157,1,0,0,0,159,162,1,
  	0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,163,1,0,0,0,162,160,1,0,0,0,
  	163,164,7,0,0,0,164,13,1,0,0,0,165,167,3,16,8,0,166,165,1,0,0,0,167,168,
  	1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,15,1,0,0,0,170,171,5,6,0,
  	0,171,172,5,12,0,0,172,173,5,12,0,0,173,174,3,50,25,0,174,175,5,6,0,0,
  	175,176,5,12,0,0,176,177,5,12,0,0,177,181,3,50,25,0,178,180,3,52,26,0,
  	179,178,1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,184,
  	1,0,0,0,183,181,1,0,0,0,184,185,7,0,0,0,185,17,1,0,0,0,186,188,3,20,10,
  	0,187,186,1,0,0,0,188,189,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,
  	19,1,0,0,0,191,192,5,6,0,0,192,193,5,12,0,0,193,194,5,12,0,0,194,195,
  	3,50,25,0,195,196,5,6,0,0,196,197,5,12,0,0,197,198,5,12,0,0,198,199,3,
  	50,25,0,199,200,5,6,0,0,200,201,5,12,0,0,201,202,5,12,0,0,202,206,3,50,
  	25,0,203,205,3,52,26,0,204,203,1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,
  	0,206,207,1,0,0,0,207,209,1,0,0,0,208,206,1,0,0,0,209,210,7,0,0,0,210,
  	21,1,0,0,0,211,213,3,24,12,0,212,211,1,0,0,0,213,214,1,0,0,0,214,212,
  	1,0,0,0,214,215,1,0,0,0,215,23,1,0,0,0,216,217,5,6,0,0,217,218,5,12,0,
  	0,218,219,5,12,0,0,219,220,3,50,25,0,220,221,5,6,0,0,221,222,5,12,0,0,
  	222,223,5,12,0,0,223,224,3,50,25,0,224,225,5,6,0,0,225,226,5,12,0,0,226,
  	227,5,12,0,0,227,228,3,50,25,0,228,229,5,6,0,0,229,230,5,12,0,0,230,231,
  	5,12,0,0,231,235,3,50,25,0,232,234,3,52,26,0,233,232,1,0,0,0,234,237,
  	1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,238,1,0,0,0,237,235,1,0,0,
  	0,238,239,7,0,0,0,239,25,1,0,0,0,240,241,5,1,0,0,241,244,5,17,0,0,242,
  	244,5,2,0,0,243,240,1,0,0,0,243,242,1,0,0,0,244,245,1,0,0,0,245,248,5,
  	18,0,0,246,247,5,21,0,0,247,249,5,22,0,0,248,246,1,0,0,0,248,249,1,0,
  	0,0,249,251,1,0,0,0,250,252,5,25,0,0,251,250,1,0,0,0,251,252,1,0,0,0,
  	252,254,1,0,0,0,253,255,5,26,0,0,254,253,1,0,0,0,254,255,1,0,0,0,255,
  	257,1,0,0,0,256,258,5,27,0,0,257,256,1,0,0,0,257,258,1,0,0,0,258,260,
  	1,0,0,0,259,261,5,28,0,0,260,259,1,0,0,0,260,261,1,0,0,0,261,262,1,0,
  	0,0,262,264,5,30,0,0,263,265,3,44,22,0,264,263,1,0,0,0,265,266,1,0,0,
  	0,266,264,1,0,0,0,266,267,1,0,0,0,267,27,1,0,0,0,268,269,5,1,0,0,269,
  	272,5,17,0,0,270,272,5,2,0,0,271,268,1,0,0,0,271,270,1,0,0,0,272,273,
  	1,0,0,0,273,274,5,18,0,0,274,278,5,19,0,0,275,276,5,21,0,0,276,277,5,
  	22,0,0,277,279,5,23,0,0,278,275,1,0,0,0,278,279,1,0,0,0,279,281,1,0,0,
  	0,280,282,5,25,0,0,281,280,1,0,0,0,281,282,1,0,0,0,282,284,1,0,0,0,283,
  	285,5,26,0,0,284,283,1,0,0,0,284,285,1,0,0,0,285,287,1,0,0,0,286,288,
  	5,27,0,0,287,286,1,0,0,0,287,288,1,0,0,0,288,290,1,0,0,0,289,291,5,28,
  	0,0,290,289,1,0,0,0,290,291,1,0,0,0,291,292,1,0,0,0,292,294,5,30,0,0,
  	293,295,3,46,23,0,294,293,1,0,0,0,295,296,1,0,0,0,296,294,1,0,0,0,296,
  	297,1,0,0,0,297,29,1,0,0,0,298,299,5,1,0,0,299,302,5,17,0,0,300,302,5,
  	2,0,0,301,298,1,0,0,0,301,300,1,0,0,0,302,303,1,0,0,0,303,304,5,18,0,
  	0,304,305,5,19,0,0,305,310,5,20,0,0,306,307,5,21,0,0,307,308,5,22,0,0,
  	308,309,5,23,0,0,309,311,5,24,0,0,310,306,1,0,0,0,310,311,1,0,0,0,311,
  	313,1,0,0,0,312,314,5,25,0,0,313,312,1,0,0,0,313,314,1,0,0,0,314,316,
  	1,0,0,0,315,317,5,26,0,0,316,315,1,0,0,0,316,317,1,0,0,0,317,319,1,0,
  	0,0,318,320,5,27,0,0,319,318,1,0,0,0,319,320,1,0,0,0,320,322,1,0,0,0,
  	321,323,5,28,0,0,322,321,1,0,0,0,322,323,1,0,0,0,323,324,1,0,0,0,324,
  	326,5,30,0,0,325,327,3,48,24,0,326,325,1,0,0,0,327,328,1,0,0,0,328,326,
  	1,0,0,0,328,329,1,0,0,0,329,31,1,0,0,0,330,331,5,1,0,0,331,334,5,18,0,
  	0,332,334,5,3,0,0,333,330,1,0,0,0,333,332,1,0,0,0,334,335,1,0,0,0,335,
  	338,5,17,0,0,336,337,5,22,0,0,337,339,5,21,0,0,338,336,1,0,0,0,338,339,
  	1,0,0,0,339,341,1,0,0,0,340,342,5,25,0,0,341,340,1,0,0,0,341,342,1,0,
  	0,0,342,344,1,0,0,0,343,345,5,26,0,0,344,343,1,0,0,0,344,345,1,0,0,0,
  	345,347,1,0,0,0,346,348,5,27,0,0,347,346,1,0,0,0,347,348,1,0,0,0,348,
  	350,1,0,0,0,349,351,5,28,0,0,350,349,1,0,0,0,350,351,1,0,0,0,351,352,
  	1,0,0,0,352,354,5,30,0,0,353,355,3,44,22,0,354,353,1,0,0,0,355,356,1,
  	0,0,0,356,354,1,0,0,0,356,357,1,0,0,0,357,33,1,0,0,0,358,359,5,1,0,0,
  	359,362,5,19,0,0,360,362,5,4,0,0,361,358,1,0,0,0,361,360,1,0,0,0,362,
  	363,1,0,0,0,363,364,5,18,0,0,364,368,5,17,0,0,365,366,5,23,0,0,366,367,
  	5,22,0,0,367,369,5,21,0,0,368,365,1,0,0,0,368,369,1,0,0,0,369,371,1,0,
  	0,0,370,372,5,25,0,0,371,370,1,0,0,0,371,372,1,0,0,0,372,374,1,0,0,0,
  	373,375,5,26,0,0,374,373,1,0,0,0,374,375,1,0,0,0,375,377,1,0,0,0,376,
  	378,5,27,0,0,377,376,1,0,0,0,377,378,1,0,0,0,378,380,1,0,0,0,379,381,
  	5,28,0,0,380,379,1,0,0,0,380,381,1,0,0,0,381,382,1,0,0,0,382,384,5,30,
  	0,0,383,385,3,46,23,0,384,383,1,0,0,0,385,386,1,0,0,0,386,384,1,0,0,0,
  	386,387,1,0,0,0,387,35,1,0,0,0,388,389,5,1,0,0,389,392,5,20,0,0,390,392,
  	5,5,0,0,391,388,1,0,0,0,391,390,1,0,0,0,392,393,1,0,0,0,393,394,5,19,
  	0,0,394,395,5,18,0,0,395,400,5,17,0,0,396,397,5,24,0,0,397,398,5,23,0,
  	0,398,399,5,22,0,0,399,401,5,21,0,0,400,396,1,0,0,0,400,401,1,0,0,0,401,
  	403,1,0,0,0,402,404,5,25,0,0,403,402,1,0,0,0,403,404,1,0,0,0,404,406,
  	1,0,0,0,405,407,5,26,0,0,406,405,1,0,0,0,406,407,1,0,0,0,407,409,1,0,
  	0,0,408,410,5,27,0,0,409,408,1,0,0,0,409,410,1,0,0,0,410,412,1,0,0,0,
  	411,413,5,28,0,0,412,411,1,0,0,0,412,413,1,0,0,0,413,414,1,0,0,0,414,
  	416,5,30,0,0,415,417,3,48,24,0,416,415,1,0,0,0,417,418,1,0,0,0,418,416,
  	1,0,0,0,418,419,1,0,0,0,419,37,1,0,0,0,420,422,3,44,22,0,421,420,1,0,
  	0,0,422,423,1,0,0,0,423,421,1,0,0,0,423,424,1,0,0,0,424,39,1,0,0,0,425,
  	427,3,46,23,0,426,425,1,0,0,0,427,428,1,0,0,0,428,426,1,0,0,0,428,429,
  	1,0,0,0,429,41,1,0,0,0,430,432,3,48,24,0,431,430,1,0,0,0,432,433,1,0,
  	0,0,433,431,1,0,0,0,433,434,1,0,0,0,434,43,1,0,0,0,435,436,5,6,0,0,436,
  	437,3,50,25,0,437,441,3,50,25,0,438,440,3,52,26,0,439,438,1,0,0,0,440,
  	443,1,0,0,0,441,439,1,0,0,0,441,442,1,0,0,0,442,447,1,0,0,0,443,441,1,
  	0,0,0,444,446,5,12,0,0,445,444,1,0,0,0,446,449,1,0,0,0,447,445,1,0,0,
  	0,447,448,1,0,0,0,448,450,1,0,0,0,449,447,1,0,0,0,450,451,7,0,0,0,451,
  	45,1,0,0,0,452,453,5,6,0,0,453,454,3,50,25,0,454,455,3,50,25,0,455,459,
  	3,50,25,0,456,458,3,52,26,0,457,456,1,0,0,0,458,461,1,0,0,0,459,457,1,
  	0,0,0,459,460,1,0,0,0,460,465,1,0,0,0,461,459,1,0,0,0,462,464,5,12,0,
  	0,463,462,1,0,0,0,464,467,1,0,0,0,465,463,1,0,0,0,465,466,1,0,0,0,466,
  	468,1,0,0,0,467,465,1,0,0,0,468,469,7,0,0,0,469,47,1,0,0,0,470,471,5,
  	6,0,0,471,472,3,50,25,0,472,473,3,50,25,0,473,474,3,50,25,0,474,478,3,
  	50,25,0,475,477,3,52,26,0,476,475,1,0,0,0,477,480,1,0,0,0,478,476,1,0,
  	0,0,478,479,1,0,0,0,479,484,1,0,0,0,480,478,1,0,0,0,481,483,5,12,0,0,
  	482,481,1,0,0,0,483,486,1,0,0,0,484,482,1,0,0,0,484,485,1,0,0,0,485,487,
  	1,0,0,0,486,484,1,0,0,0,487,488,7,0,0,0,488,49,1,0,0,0,489,490,7,1,0,
  	0,490,51,1,0,0,0,491,492,7,2,0,0,492,53,1,0,0,0,66,55,74,76,84,99,107,
  	127,135,160,168,181,189,206,214,235,243,248,251,254,257,260,266,271,278,
  	281,284,287,290,296,301,310,313,316,319,322,328,333,338,341,344,347,350,
  	356,361,368,371,374,377,380,386,391,400,403,406,409,412,418,423,428,433,
  	441,447,459,465,478,484
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  barepkparserParserStaticData = staticData.release();
}

}

BarePKParser::BarePKParser(TokenStream *input) : BarePKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

BarePKParser::BarePKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  BarePKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *barepkparserParserStaticData->atn, barepkparserParserStaticData->decisionToDFA, barepkparserParserStaticData->sharedContextCache, options);
}

BarePKParser::~BarePKParser() {
  delete _interpreter;
}

const atn::ATN& BarePKParser::getATN() const {
  return *barepkparserParserStaticData->atn;
}

std::string BarePKParser::getGrammarFileName() const {
  return "BarePKParser.g4";
}

const std::vector<std::string>& BarePKParser::getRuleNames() const {
  return barepkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& BarePKParser::getVocabulary() const {
  return barepkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView BarePKParser::getSerializedATN() const {
  return barepkparserParserStaticData->serializedATN;
}


//----------------- Bare_pkContext ------------------------------------------------------------------

BarePKParser::Bare_pkContext::Bare_pkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePKParser::Bare_pkContext::EOF() {
  return getToken(BarePKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> BarePKParser::Bare_pkContext::RETURN() {
  return getTokens(BarePKParser::RETURN);
}

tree::TerminalNode* BarePKParser::Bare_pkContext::RETURN(size_t i) {
  return getToken(BarePKParser::RETURN, i);
}

std::vector<BarePKParser::Peak_list_2dContext *> BarePKParser::Bare_pkContext::peak_list_2d() {
  return getRuleContexts<BarePKParser::Peak_list_2dContext>();
}

BarePKParser::Peak_list_2dContext* BarePKParser::Bare_pkContext::peak_list_2d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_2dContext>(i);
}

std::vector<BarePKParser::Peak_list_3dContext *> BarePKParser::Bare_pkContext::peak_list_3d() {
  return getRuleContexts<BarePKParser::Peak_list_3dContext>();
}

BarePKParser::Peak_list_3dContext* BarePKParser::Bare_pkContext::peak_list_3d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_3dContext>(i);
}

std::vector<BarePKParser::Peak_list_4dContext *> BarePKParser::Bare_pkContext::peak_list_4d() {
  return getRuleContexts<BarePKParser::Peak_list_4dContext>();
}

BarePKParser::Peak_list_4dContext* BarePKParser::Bare_pkContext::peak_list_4d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_4dContext>(i);
}

std::vector<BarePKParser::Peak_list_wo_chain_2dContext *> BarePKParser::Bare_pkContext::peak_list_wo_chain_2d() {
  return getRuleContexts<BarePKParser::Peak_list_wo_chain_2dContext>();
}

BarePKParser::Peak_list_wo_chain_2dContext* BarePKParser::Bare_pkContext::peak_list_wo_chain_2d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_wo_chain_2dContext>(i);
}

std::vector<BarePKParser::Peak_list_wo_chain_3dContext *> BarePKParser::Bare_pkContext::peak_list_wo_chain_3d() {
  return getRuleContexts<BarePKParser::Peak_list_wo_chain_3dContext>();
}

BarePKParser::Peak_list_wo_chain_3dContext* BarePKParser::Bare_pkContext::peak_list_wo_chain_3d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_wo_chain_3dContext>(i);
}

std::vector<BarePKParser::Peak_list_wo_chain_4dContext *> BarePKParser::Bare_pkContext::peak_list_wo_chain_4d() {
  return getRuleContexts<BarePKParser::Peak_list_wo_chain_4dContext>();
}

BarePKParser::Peak_list_wo_chain_4dContext* BarePKParser::Bare_pkContext::peak_list_wo_chain_4d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_wo_chain_4dContext>(i);
}

std::vector<BarePKParser::Row_format_2dContext *> BarePKParser::Bare_pkContext::row_format_2d() {
  return getRuleContexts<BarePKParser::Row_format_2dContext>();
}

BarePKParser::Row_format_2dContext* BarePKParser::Bare_pkContext::row_format_2d(size_t i) {
  return getRuleContext<BarePKParser::Row_format_2dContext>(i);
}

std::vector<BarePKParser::Row_format_3dContext *> BarePKParser::Bare_pkContext::row_format_3d() {
  return getRuleContexts<BarePKParser::Row_format_3dContext>();
}

BarePKParser::Row_format_3dContext* BarePKParser::Bare_pkContext::row_format_3d(size_t i) {
  return getRuleContext<BarePKParser::Row_format_3dContext>(i);
}

std::vector<BarePKParser::Row_format_4dContext *> BarePKParser::Bare_pkContext::row_format_4d() {
  return getRuleContexts<BarePKParser::Row_format_4dContext>();
}

BarePKParser::Row_format_4dContext* BarePKParser::Bare_pkContext::row_format_4d(size_t i) {
  return getRuleContext<BarePKParser::Row_format_4dContext>(i);
}

std::vector<BarePKParser::Rev_row_format_2dContext *> BarePKParser::Bare_pkContext::rev_row_format_2d() {
  return getRuleContexts<BarePKParser::Rev_row_format_2dContext>();
}

BarePKParser::Rev_row_format_2dContext* BarePKParser::Bare_pkContext::rev_row_format_2d(size_t i) {
  return getRuleContext<BarePKParser::Rev_row_format_2dContext>(i);
}

std::vector<BarePKParser::Rev_row_format_3dContext *> BarePKParser::Bare_pkContext::rev_row_format_3d() {
  return getRuleContexts<BarePKParser::Rev_row_format_3dContext>();
}

BarePKParser::Rev_row_format_3dContext* BarePKParser::Bare_pkContext::rev_row_format_3d(size_t i) {
  return getRuleContext<BarePKParser::Rev_row_format_3dContext>(i);
}

std::vector<BarePKParser::Rev_row_format_4dContext *> BarePKParser::Bare_pkContext::rev_row_format_4d() {
  return getRuleContexts<BarePKParser::Rev_row_format_4dContext>();
}

BarePKParser::Rev_row_format_4dContext* BarePKParser::Bare_pkContext::rev_row_format_4d(size_t i) {
  return getRuleContext<BarePKParser::Rev_row_format_4dContext>(i);
}

std::vector<BarePKParser::Row_format_wo_label_2dContext *> BarePKParser::Bare_pkContext::row_format_wo_label_2d() {
  return getRuleContexts<BarePKParser::Row_format_wo_label_2dContext>();
}

BarePKParser::Row_format_wo_label_2dContext* BarePKParser::Bare_pkContext::row_format_wo_label_2d(size_t i) {
  return getRuleContext<BarePKParser::Row_format_wo_label_2dContext>(i);
}

std::vector<BarePKParser::Row_format_wo_label_3dContext *> BarePKParser::Bare_pkContext::row_format_wo_label_3d() {
  return getRuleContexts<BarePKParser::Row_format_wo_label_3dContext>();
}

BarePKParser::Row_format_wo_label_3dContext* BarePKParser::Bare_pkContext::row_format_wo_label_3d(size_t i) {
  return getRuleContext<BarePKParser::Row_format_wo_label_3dContext>(i);
}

std::vector<BarePKParser::Row_format_wo_label_4dContext *> BarePKParser::Bare_pkContext::row_format_wo_label_4d() {
  return getRuleContexts<BarePKParser::Row_format_wo_label_4dContext>();
}

BarePKParser::Row_format_wo_label_4dContext* BarePKParser::Bare_pkContext::row_format_wo_label_4d(size_t i) {
  return getRuleContext<BarePKParser::Row_format_wo_label_4dContext>(i);
}


size_t BarePKParser::Bare_pkContext::getRuleIndex() const {
  return BarePKParser::RuleBare_pk;
}


std::any BarePKParser::Bare_pkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitBare_pk(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Bare_pkContext* BarePKParser::bare_pk() {
  Bare_pkContext *_localctx = _tracker.createInstance<Bare_pkContext>(_ctx, getState());
  enterRule(_localctx, 0, BarePKParser::RuleBare_pk);
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
    setState(55);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::RETURN) {
      setState(54);
      match(BarePKParser::RETURN);
    }
    setState(76);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 4222) != 0)) {
      setState(74);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(57);
        peak_list_2d();
        break;
      }

      case 2: {
        setState(58);
        peak_list_3d();
        break;
      }

      case 3: {
        setState(59);
        peak_list_4d();
        break;
      }

      case 4: {
        setState(60);
        peak_list_wo_chain_2d();
        break;
      }

      case 5: {
        setState(61);
        peak_list_wo_chain_3d();
        break;
      }

      case 6: {
        setState(62);
        peak_list_wo_chain_4d();
        break;
      }

      case 7: {
        setState(63);
        row_format_2d();
        break;
      }

      case 8: {
        setState(64);
        row_format_3d();
        break;
      }

      case 9: {
        setState(65);
        row_format_4d();
        break;
      }

      case 10: {
        setState(66);
        rev_row_format_2d();
        break;
      }

      case 11: {
        setState(67);
        rev_row_format_3d();
        break;
      }

      case 12: {
        setState(68);
        rev_row_format_4d();
        break;
      }

      case 13: {
        setState(69);
        row_format_wo_label_2d();
        break;
      }

      case 14: {
        setState(70);
        row_format_wo_label_3d();
        break;
      }

      case 15: {
        setState(71);
        row_format_wo_label_4d();
        setState(72);
        match(BarePKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(78);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(79);
    match(BarePKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_list_2dContext ------------------------------------------------------------------

BarePKParser::Peak_list_2dContext::Peak_list_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BarePKParser::Peak_2dContext *> BarePKParser::Peak_list_2dContext::peak_2d() {
  return getRuleContexts<BarePKParser::Peak_2dContext>();
}

BarePKParser::Peak_2dContext* BarePKParser::Peak_list_2dContext::peak_2d(size_t i) {
  return getRuleContext<BarePKParser::Peak_2dContext>(i);
}


size_t BarePKParser::Peak_list_2dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_list_2d;
}


std::any BarePKParser::Peak_list_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_2d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_list_2dContext* BarePKParser::peak_list_2d() {
  Peak_list_2dContext *_localctx = _tracker.createInstance<Peak_list_2dContext>(_ctx, getState());
  enterRule(_localctx, 2, BarePKParser::RulePeak_list_2d);

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
    setState(82); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(81);
              peak_2d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(84); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_2dContext ------------------------------------------------------------------

BarePKParser::Peak_2dContext::Peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_2dContext::Simple_name() {
  return getTokens(BarePKParser::Simple_name);
}

tree::TerminalNode* BarePKParser::Peak_2dContext::Simple_name(size_t i) {
  return getToken(BarePKParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_2dContext::Integer() {
  return getTokens(BarePKParser::Integer);
}

tree::TerminalNode* BarePKParser::Peak_2dContext::Integer(size_t i) {
  return getToken(BarePKParser::Integer, i);
}

std::vector<BarePKParser::PositionContext *> BarePKParser::Peak_2dContext::position() {
  return getRuleContexts<BarePKParser::PositionContext>();
}

BarePKParser::PositionContext* BarePKParser::Peak_2dContext::position(size_t i) {
  return getRuleContext<BarePKParser::PositionContext>(i);
}

tree::TerminalNode* BarePKParser::Peak_2dContext::RETURN() {
  return getToken(BarePKParser::RETURN, 0);
}

tree::TerminalNode* BarePKParser::Peak_2dContext::EOF() {
  return getToken(BarePKParser::EOF, 0);
}

std::vector<BarePKParser::NumberContext *> BarePKParser::Peak_2dContext::number() {
  return getRuleContexts<BarePKParser::NumberContext>();
}

BarePKParser::NumberContext* BarePKParser::Peak_2dContext::number(size_t i) {
  return getRuleContext<BarePKParser::NumberContext>(i);
}


size_t BarePKParser::Peak_2dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_2d;
}


std::any BarePKParser::Peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_2dContext* BarePKParser::peak_2d() {
  Peak_2dContext *_localctx = _tracker.createInstance<Peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 4, BarePKParser::RulePeak_2d);
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
    setState(86);
    match(BarePKParser::Simple_name);
    setState(87);
    match(BarePKParser::Integer);
    setState(88);
    match(BarePKParser::Simple_name);
    setState(89);
    match(BarePKParser::Simple_name);
    setState(90);
    position();
    setState(91);
    match(BarePKParser::Simple_name);
    setState(92);
    match(BarePKParser::Integer);
    setState(93);
    match(BarePKParser::Simple_name);
    setState(94);
    match(BarePKParser::Simple_name);
    setState(95);
    position();
    setState(99);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 448) != 0)) {
      setState(96);
      number();
      setState(101);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(102);
    _la = _input->LA(1);
    if (!(_la == BarePKParser::EOF

    || _la == BarePKParser::RETURN)) {
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

BarePKParser::Peak_list_3dContext::Peak_list_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BarePKParser::Peak_3dContext *> BarePKParser::Peak_list_3dContext::peak_3d() {
  return getRuleContexts<BarePKParser::Peak_3dContext>();
}

BarePKParser::Peak_3dContext* BarePKParser::Peak_list_3dContext::peak_3d(size_t i) {
  return getRuleContext<BarePKParser::Peak_3dContext>(i);
}


size_t BarePKParser::Peak_list_3dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_list_3d;
}


std::any BarePKParser::Peak_list_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_3d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_list_3dContext* BarePKParser::peak_list_3d() {
  Peak_list_3dContext *_localctx = _tracker.createInstance<Peak_list_3dContext>(_ctx, getState());
  enterRule(_localctx, 6, BarePKParser::RulePeak_list_3d);

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
    setState(105); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(104);
              peak_3d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(107); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_3dContext ------------------------------------------------------------------

BarePKParser::Peak_3dContext::Peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_3dContext::Simple_name() {
  return getTokens(BarePKParser::Simple_name);
}

tree::TerminalNode* BarePKParser::Peak_3dContext::Simple_name(size_t i) {
  return getToken(BarePKParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_3dContext::Integer() {
  return getTokens(BarePKParser::Integer);
}

tree::TerminalNode* BarePKParser::Peak_3dContext::Integer(size_t i) {
  return getToken(BarePKParser::Integer, i);
}

std::vector<BarePKParser::PositionContext *> BarePKParser::Peak_3dContext::position() {
  return getRuleContexts<BarePKParser::PositionContext>();
}

BarePKParser::PositionContext* BarePKParser::Peak_3dContext::position(size_t i) {
  return getRuleContext<BarePKParser::PositionContext>(i);
}

tree::TerminalNode* BarePKParser::Peak_3dContext::RETURN() {
  return getToken(BarePKParser::RETURN, 0);
}

tree::TerminalNode* BarePKParser::Peak_3dContext::EOF() {
  return getToken(BarePKParser::EOF, 0);
}

std::vector<BarePKParser::NumberContext *> BarePKParser::Peak_3dContext::number() {
  return getRuleContexts<BarePKParser::NumberContext>();
}

BarePKParser::NumberContext* BarePKParser::Peak_3dContext::number(size_t i) {
  return getRuleContext<BarePKParser::NumberContext>(i);
}


size_t BarePKParser::Peak_3dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_3d;
}


std::any BarePKParser::Peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_3dContext* BarePKParser::peak_3d() {
  Peak_3dContext *_localctx = _tracker.createInstance<Peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 8, BarePKParser::RulePeak_3d);
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
    setState(109);
    match(BarePKParser::Simple_name);
    setState(110);
    match(BarePKParser::Integer);
    setState(111);
    match(BarePKParser::Simple_name);
    setState(112);
    match(BarePKParser::Simple_name);
    setState(113);
    position();
    setState(114);
    match(BarePKParser::Simple_name);
    setState(115);
    match(BarePKParser::Integer);
    setState(116);
    match(BarePKParser::Simple_name);
    setState(117);
    match(BarePKParser::Simple_name);
    setState(118);
    position();
    setState(119);
    match(BarePKParser::Simple_name);
    setState(120);
    match(BarePKParser::Integer);
    setState(121);
    match(BarePKParser::Simple_name);
    setState(122);
    match(BarePKParser::Simple_name);
    setState(123);
    position();
    setState(127);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 448) != 0)) {
      setState(124);
      number();
      setState(129);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(130);
    _la = _input->LA(1);
    if (!(_la == BarePKParser::EOF

    || _la == BarePKParser::RETURN)) {
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

BarePKParser::Peak_list_4dContext::Peak_list_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BarePKParser::Peak_4dContext *> BarePKParser::Peak_list_4dContext::peak_4d() {
  return getRuleContexts<BarePKParser::Peak_4dContext>();
}

BarePKParser::Peak_4dContext* BarePKParser::Peak_list_4dContext::peak_4d(size_t i) {
  return getRuleContext<BarePKParser::Peak_4dContext>(i);
}


size_t BarePKParser::Peak_list_4dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_list_4d;
}


std::any BarePKParser::Peak_list_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_4d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_list_4dContext* BarePKParser::peak_list_4d() {
  Peak_list_4dContext *_localctx = _tracker.createInstance<Peak_list_4dContext>(_ctx, getState());
  enterRule(_localctx, 10, BarePKParser::RulePeak_list_4d);

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
    setState(133); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(132);
              peak_4d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(135); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_4dContext ------------------------------------------------------------------

BarePKParser::Peak_4dContext::Peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_4dContext::Simple_name() {
  return getTokens(BarePKParser::Simple_name);
}

tree::TerminalNode* BarePKParser::Peak_4dContext::Simple_name(size_t i) {
  return getToken(BarePKParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_4dContext::Integer() {
  return getTokens(BarePKParser::Integer);
}

tree::TerminalNode* BarePKParser::Peak_4dContext::Integer(size_t i) {
  return getToken(BarePKParser::Integer, i);
}

std::vector<BarePKParser::PositionContext *> BarePKParser::Peak_4dContext::position() {
  return getRuleContexts<BarePKParser::PositionContext>();
}

BarePKParser::PositionContext* BarePKParser::Peak_4dContext::position(size_t i) {
  return getRuleContext<BarePKParser::PositionContext>(i);
}

tree::TerminalNode* BarePKParser::Peak_4dContext::RETURN() {
  return getToken(BarePKParser::RETURN, 0);
}

tree::TerminalNode* BarePKParser::Peak_4dContext::EOF() {
  return getToken(BarePKParser::EOF, 0);
}

std::vector<BarePKParser::NumberContext *> BarePKParser::Peak_4dContext::number() {
  return getRuleContexts<BarePKParser::NumberContext>();
}

BarePKParser::NumberContext* BarePKParser::Peak_4dContext::number(size_t i) {
  return getRuleContext<BarePKParser::NumberContext>(i);
}


size_t BarePKParser::Peak_4dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_4d;
}


std::any BarePKParser::Peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_4dContext* BarePKParser::peak_4d() {
  Peak_4dContext *_localctx = _tracker.createInstance<Peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 12, BarePKParser::RulePeak_4d);
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
    match(BarePKParser::Simple_name);
    setState(138);
    match(BarePKParser::Integer);
    setState(139);
    match(BarePKParser::Simple_name);
    setState(140);
    match(BarePKParser::Simple_name);
    setState(141);
    position();
    setState(142);
    match(BarePKParser::Simple_name);
    setState(143);
    match(BarePKParser::Integer);
    setState(144);
    match(BarePKParser::Simple_name);
    setState(145);
    match(BarePKParser::Simple_name);
    setState(146);
    position();
    setState(147);
    match(BarePKParser::Simple_name);
    setState(148);
    match(BarePKParser::Integer);
    setState(149);
    match(BarePKParser::Simple_name);
    setState(150);
    match(BarePKParser::Simple_name);
    setState(151);
    position();
    setState(152);
    match(BarePKParser::Simple_name);
    setState(153);
    match(BarePKParser::Integer);
    setState(154);
    match(BarePKParser::Simple_name);
    setState(155);
    match(BarePKParser::Simple_name);
    setState(156);
    position();
    setState(160);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 448) != 0)) {
      setState(157);
      number();
      setState(162);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(163);
    _la = _input->LA(1);
    if (!(_la == BarePKParser::EOF

    || _la == BarePKParser::RETURN)) {
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

//----------------- Peak_list_wo_chain_2dContext ------------------------------------------------------------------

BarePKParser::Peak_list_wo_chain_2dContext::Peak_list_wo_chain_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BarePKParser::Peak_wo_chain_2dContext *> BarePKParser::Peak_list_wo_chain_2dContext::peak_wo_chain_2d() {
  return getRuleContexts<BarePKParser::Peak_wo_chain_2dContext>();
}

BarePKParser::Peak_wo_chain_2dContext* BarePKParser::Peak_list_wo_chain_2dContext::peak_wo_chain_2d(size_t i) {
  return getRuleContext<BarePKParser::Peak_wo_chain_2dContext>(i);
}


size_t BarePKParser::Peak_list_wo_chain_2dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_list_wo_chain_2d;
}


std::any BarePKParser::Peak_list_wo_chain_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_wo_chain_2d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_list_wo_chain_2dContext* BarePKParser::peak_list_wo_chain_2d() {
  Peak_list_wo_chain_2dContext *_localctx = _tracker.createInstance<Peak_list_wo_chain_2dContext>(_ctx, getState());
  enterRule(_localctx, 14, BarePKParser::RulePeak_list_wo_chain_2d);

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
    setState(166); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(165);
              peak_wo_chain_2d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(168); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_wo_chain_2dContext ------------------------------------------------------------------

BarePKParser::Peak_wo_chain_2dContext::Peak_wo_chain_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_wo_chain_2dContext::Integer() {
  return getTokens(BarePKParser::Integer);
}

tree::TerminalNode* BarePKParser::Peak_wo_chain_2dContext::Integer(size_t i) {
  return getToken(BarePKParser::Integer, i);
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_wo_chain_2dContext::Simple_name() {
  return getTokens(BarePKParser::Simple_name);
}

tree::TerminalNode* BarePKParser::Peak_wo_chain_2dContext::Simple_name(size_t i) {
  return getToken(BarePKParser::Simple_name, i);
}

std::vector<BarePKParser::PositionContext *> BarePKParser::Peak_wo_chain_2dContext::position() {
  return getRuleContexts<BarePKParser::PositionContext>();
}

BarePKParser::PositionContext* BarePKParser::Peak_wo_chain_2dContext::position(size_t i) {
  return getRuleContext<BarePKParser::PositionContext>(i);
}

tree::TerminalNode* BarePKParser::Peak_wo_chain_2dContext::RETURN() {
  return getToken(BarePKParser::RETURN, 0);
}

tree::TerminalNode* BarePKParser::Peak_wo_chain_2dContext::EOF() {
  return getToken(BarePKParser::EOF, 0);
}

std::vector<BarePKParser::NumberContext *> BarePKParser::Peak_wo_chain_2dContext::number() {
  return getRuleContexts<BarePKParser::NumberContext>();
}

BarePKParser::NumberContext* BarePKParser::Peak_wo_chain_2dContext::number(size_t i) {
  return getRuleContext<BarePKParser::NumberContext>(i);
}


size_t BarePKParser::Peak_wo_chain_2dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_wo_chain_2d;
}


std::any BarePKParser::Peak_wo_chain_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_chain_2d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_wo_chain_2dContext* BarePKParser::peak_wo_chain_2d() {
  Peak_wo_chain_2dContext *_localctx = _tracker.createInstance<Peak_wo_chain_2dContext>(_ctx, getState());
  enterRule(_localctx, 16, BarePKParser::RulePeak_wo_chain_2d);
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
    match(BarePKParser::Integer);
    setState(171);
    match(BarePKParser::Simple_name);
    setState(172);
    match(BarePKParser::Simple_name);
    setState(173);
    position();
    setState(174);
    match(BarePKParser::Integer);
    setState(175);
    match(BarePKParser::Simple_name);
    setState(176);
    match(BarePKParser::Simple_name);
    setState(177);
    position();
    setState(181);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 448) != 0)) {
      setState(178);
      number();
      setState(183);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(184);
    _la = _input->LA(1);
    if (!(_la == BarePKParser::EOF

    || _la == BarePKParser::RETURN)) {
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

//----------------- Peak_list_wo_chain_3dContext ------------------------------------------------------------------

BarePKParser::Peak_list_wo_chain_3dContext::Peak_list_wo_chain_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BarePKParser::Peak_wo_chain_3dContext *> BarePKParser::Peak_list_wo_chain_3dContext::peak_wo_chain_3d() {
  return getRuleContexts<BarePKParser::Peak_wo_chain_3dContext>();
}

BarePKParser::Peak_wo_chain_3dContext* BarePKParser::Peak_list_wo_chain_3dContext::peak_wo_chain_3d(size_t i) {
  return getRuleContext<BarePKParser::Peak_wo_chain_3dContext>(i);
}


size_t BarePKParser::Peak_list_wo_chain_3dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_list_wo_chain_3d;
}


std::any BarePKParser::Peak_list_wo_chain_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_wo_chain_3d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_list_wo_chain_3dContext* BarePKParser::peak_list_wo_chain_3d() {
  Peak_list_wo_chain_3dContext *_localctx = _tracker.createInstance<Peak_list_wo_chain_3dContext>(_ctx, getState());
  enterRule(_localctx, 18, BarePKParser::RulePeak_list_wo_chain_3d);

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
    setState(187); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(186);
              peak_wo_chain_3d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(189); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_wo_chain_3dContext ------------------------------------------------------------------

BarePKParser::Peak_wo_chain_3dContext::Peak_wo_chain_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_wo_chain_3dContext::Integer() {
  return getTokens(BarePKParser::Integer);
}

tree::TerminalNode* BarePKParser::Peak_wo_chain_3dContext::Integer(size_t i) {
  return getToken(BarePKParser::Integer, i);
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_wo_chain_3dContext::Simple_name() {
  return getTokens(BarePKParser::Simple_name);
}

tree::TerminalNode* BarePKParser::Peak_wo_chain_3dContext::Simple_name(size_t i) {
  return getToken(BarePKParser::Simple_name, i);
}

std::vector<BarePKParser::PositionContext *> BarePKParser::Peak_wo_chain_3dContext::position() {
  return getRuleContexts<BarePKParser::PositionContext>();
}

BarePKParser::PositionContext* BarePKParser::Peak_wo_chain_3dContext::position(size_t i) {
  return getRuleContext<BarePKParser::PositionContext>(i);
}

tree::TerminalNode* BarePKParser::Peak_wo_chain_3dContext::RETURN() {
  return getToken(BarePKParser::RETURN, 0);
}

tree::TerminalNode* BarePKParser::Peak_wo_chain_3dContext::EOF() {
  return getToken(BarePKParser::EOF, 0);
}

std::vector<BarePKParser::NumberContext *> BarePKParser::Peak_wo_chain_3dContext::number() {
  return getRuleContexts<BarePKParser::NumberContext>();
}

BarePKParser::NumberContext* BarePKParser::Peak_wo_chain_3dContext::number(size_t i) {
  return getRuleContext<BarePKParser::NumberContext>(i);
}


size_t BarePKParser::Peak_wo_chain_3dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_wo_chain_3d;
}


std::any BarePKParser::Peak_wo_chain_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_chain_3d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_wo_chain_3dContext* BarePKParser::peak_wo_chain_3d() {
  Peak_wo_chain_3dContext *_localctx = _tracker.createInstance<Peak_wo_chain_3dContext>(_ctx, getState());
  enterRule(_localctx, 20, BarePKParser::RulePeak_wo_chain_3d);
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
    setState(191);
    match(BarePKParser::Integer);
    setState(192);
    match(BarePKParser::Simple_name);
    setState(193);
    match(BarePKParser::Simple_name);
    setState(194);
    position();
    setState(195);
    match(BarePKParser::Integer);
    setState(196);
    match(BarePKParser::Simple_name);
    setState(197);
    match(BarePKParser::Simple_name);
    setState(198);
    position();
    setState(199);
    match(BarePKParser::Integer);
    setState(200);
    match(BarePKParser::Simple_name);
    setState(201);
    match(BarePKParser::Simple_name);
    setState(202);
    position();
    setState(206);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 448) != 0)) {
      setState(203);
      number();
      setState(208);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(209);
    _la = _input->LA(1);
    if (!(_la == BarePKParser::EOF

    || _la == BarePKParser::RETURN)) {
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

//----------------- Peak_list_wo_chain_4dContext ------------------------------------------------------------------

BarePKParser::Peak_list_wo_chain_4dContext::Peak_list_wo_chain_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BarePKParser::Peak_wo_chain_4dContext *> BarePKParser::Peak_list_wo_chain_4dContext::peak_wo_chain_4d() {
  return getRuleContexts<BarePKParser::Peak_wo_chain_4dContext>();
}

BarePKParser::Peak_wo_chain_4dContext* BarePKParser::Peak_list_wo_chain_4dContext::peak_wo_chain_4d(size_t i) {
  return getRuleContext<BarePKParser::Peak_wo_chain_4dContext>(i);
}


size_t BarePKParser::Peak_list_wo_chain_4dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_list_wo_chain_4d;
}


std::any BarePKParser::Peak_list_wo_chain_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_wo_chain_4d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_list_wo_chain_4dContext* BarePKParser::peak_list_wo_chain_4d() {
  Peak_list_wo_chain_4dContext *_localctx = _tracker.createInstance<Peak_list_wo_chain_4dContext>(_ctx, getState());
  enterRule(_localctx, 22, BarePKParser::RulePeak_list_wo_chain_4d);

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
    setState(212); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(211);
              peak_wo_chain_4d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(214); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 13, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_wo_chain_4dContext ------------------------------------------------------------------

BarePKParser::Peak_wo_chain_4dContext::Peak_wo_chain_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_wo_chain_4dContext::Integer() {
  return getTokens(BarePKParser::Integer);
}

tree::TerminalNode* BarePKParser::Peak_wo_chain_4dContext::Integer(size_t i) {
  return getToken(BarePKParser::Integer, i);
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_wo_chain_4dContext::Simple_name() {
  return getTokens(BarePKParser::Simple_name);
}

tree::TerminalNode* BarePKParser::Peak_wo_chain_4dContext::Simple_name(size_t i) {
  return getToken(BarePKParser::Simple_name, i);
}

std::vector<BarePKParser::PositionContext *> BarePKParser::Peak_wo_chain_4dContext::position() {
  return getRuleContexts<BarePKParser::PositionContext>();
}

BarePKParser::PositionContext* BarePKParser::Peak_wo_chain_4dContext::position(size_t i) {
  return getRuleContext<BarePKParser::PositionContext>(i);
}

tree::TerminalNode* BarePKParser::Peak_wo_chain_4dContext::RETURN() {
  return getToken(BarePKParser::RETURN, 0);
}

tree::TerminalNode* BarePKParser::Peak_wo_chain_4dContext::EOF() {
  return getToken(BarePKParser::EOF, 0);
}

std::vector<BarePKParser::NumberContext *> BarePKParser::Peak_wo_chain_4dContext::number() {
  return getRuleContexts<BarePKParser::NumberContext>();
}

BarePKParser::NumberContext* BarePKParser::Peak_wo_chain_4dContext::number(size_t i) {
  return getRuleContext<BarePKParser::NumberContext>(i);
}


size_t BarePKParser::Peak_wo_chain_4dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_wo_chain_4d;
}


std::any BarePKParser::Peak_wo_chain_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_chain_4d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_wo_chain_4dContext* BarePKParser::peak_wo_chain_4d() {
  Peak_wo_chain_4dContext *_localctx = _tracker.createInstance<Peak_wo_chain_4dContext>(_ctx, getState());
  enterRule(_localctx, 24, BarePKParser::RulePeak_wo_chain_4d);
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
    setState(216);
    match(BarePKParser::Integer);
    setState(217);
    match(BarePKParser::Simple_name);
    setState(218);
    match(BarePKParser::Simple_name);
    setState(219);
    position();
    setState(220);
    match(BarePKParser::Integer);
    setState(221);
    match(BarePKParser::Simple_name);
    setState(222);
    match(BarePKParser::Simple_name);
    setState(223);
    position();
    setState(224);
    match(BarePKParser::Integer);
    setState(225);
    match(BarePKParser::Simple_name);
    setState(226);
    match(BarePKParser::Simple_name);
    setState(227);
    position();
    setState(228);
    match(BarePKParser::Integer);
    setState(229);
    match(BarePKParser::Simple_name);
    setState(230);
    match(BarePKParser::Simple_name);
    setState(231);
    position();
    setState(235);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 448) != 0)) {
      setState(232);
      number();
      setState(237);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(238);
    _la = _input->LA(1);
    if (!(_la == BarePKParser::EOF

    || _la == BarePKParser::RETURN)) {
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

//----------------- Row_format_2dContext ------------------------------------------------------------------

BarePKParser::Row_format_2dContext::Row_format_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePKParser::Row_format_2dContext::Y_ppm() {
  return getToken(BarePKParser::Y_ppm, 0);
}

tree::TerminalNode* BarePKParser::Row_format_2dContext::RETURN_FO() {
  return getToken(BarePKParser::RETURN_FO, 0);
}

tree::TerminalNode* BarePKParser::Row_format_2dContext::Peak() {
  return getToken(BarePKParser::Peak, 0);
}

tree::TerminalNode* BarePKParser::Row_format_2dContext::X_ppm() {
  return getToken(BarePKParser::X_ppm, 0);
}

tree::TerminalNode* BarePKParser::Row_format_2dContext::X_PPM() {
  return getToken(BarePKParser::X_PPM, 0);
}

tree::TerminalNode* BarePKParser::Row_format_2dContext::X_width() {
  return getToken(BarePKParser::X_width, 0);
}

tree::TerminalNode* BarePKParser::Row_format_2dContext::Y_width() {
  return getToken(BarePKParser::Y_width, 0);
}

tree::TerminalNode* BarePKParser::Row_format_2dContext::Amplitude() {
  return getToken(BarePKParser::Amplitude, 0);
}

tree::TerminalNode* BarePKParser::Row_format_2dContext::Volume() {
  return getToken(BarePKParser::Volume, 0);
}

tree::TerminalNode* BarePKParser::Row_format_2dContext::Label() {
  return getToken(BarePKParser::Label, 0);
}

tree::TerminalNode* BarePKParser::Row_format_2dContext::Comment() {
  return getToken(BarePKParser::Comment, 0);
}

std::vector<BarePKParser::Peak_list_row_2dContext *> BarePKParser::Row_format_2dContext::peak_list_row_2d() {
  return getRuleContexts<BarePKParser::Peak_list_row_2dContext>();
}

BarePKParser::Peak_list_row_2dContext* BarePKParser::Row_format_2dContext::peak_list_row_2d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_row_2dContext>(i);
}


size_t BarePKParser::Row_format_2dContext::getRuleIndex() const {
  return BarePKParser::RuleRow_format_2d;
}


std::any BarePKParser::Row_format_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitRow_format_2d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Row_format_2dContext* BarePKParser::row_format_2d() {
  Row_format_2dContext *_localctx = _tracker.createInstance<Row_format_2dContext>(_ctx, getState());
  enterRule(_localctx, 26, BarePKParser::RuleRow_format_2d);
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
    setState(243);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BarePKParser::Peak: {
        setState(240);
        match(BarePKParser::Peak);
        setState(241);
        match(BarePKParser::X_ppm);
        break;
      }

      case BarePKParser::X_PPM: {
        setState(242);
        match(BarePKParser::X_PPM);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(245);
    match(BarePKParser::Y_ppm);
    setState(248);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::X_width) {
      setState(246);
      match(BarePKParser::X_width);
      setState(247);
      match(BarePKParser::Y_width);
    }
    setState(251);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Amplitude) {
      setState(250);
      match(BarePKParser::Amplitude);
    }
    setState(254);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Volume) {
      setState(253);
      match(BarePKParser::Volume);
    }
    setState(257);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Label) {
      setState(256);
      match(BarePKParser::Label);
    }
    setState(260);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Comment) {
      setState(259);
      match(BarePKParser::Comment);
    }
    setState(262);
    match(BarePKParser::RETURN_FO);
    setState(264); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(263);
              peak_list_row_2d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(266); 
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

//----------------- Row_format_3dContext ------------------------------------------------------------------

BarePKParser::Row_format_3dContext::Row_format_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::Y_ppm() {
  return getToken(BarePKParser::Y_ppm, 0);
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::Z_ppm() {
  return getToken(BarePKParser::Z_ppm, 0);
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::RETURN_FO() {
  return getToken(BarePKParser::RETURN_FO, 0);
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::Peak() {
  return getToken(BarePKParser::Peak, 0);
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::X_ppm() {
  return getToken(BarePKParser::X_ppm, 0);
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::X_PPM() {
  return getToken(BarePKParser::X_PPM, 0);
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::X_width() {
  return getToken(BarePKParser::X_width, 0);
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::Y_width() {
  return getToken(BarePKParser::Y_width, 0);
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::Z_width() {
  return getToken(BarePKParser::Z_width, 0);
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::Amplitude() {
  return getToken(BarePKParser::Amplitude, 0);
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::Volume() {
  return getToken(BarePKParser::Volume, 0);
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::Label() {
  return getToken(BarePKParser::Label, 0);
}

tree::TerminalNode* BarePKParser::Row_format_3dContext::Comment() {
  return getToken(BarePKParser::Comment, 0);
}

std::vector<BarePKParser::Peak_list_row_3dContext *> BarePKParser::Row_format_3dContext::peak_list_row_3d() {
  return getRuleContexts<BarePKParser::Peak_list_row_3dContext>();
}

BarePKParser::Peak_list_row_3dContext* BarePKParser::Row_format_3dContext::peak_list_row_3d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_row_3dContext>(i);
}


size_t BarePKParser::Row_format_3dContext::getRuleIndex() const {
  return BarePKParser::RuleRow_format_3d;
}


std::any BarePKParser::Row_format_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitRow_format_3d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Row_format_3dContext* BarePKParser::row_format_3d() {
  Row_format_3dContext *_localctx = _tracker.createInstance<Row_format_3dContext>(_ctx, getState());
  enterRule(_localctx, 28, BarePKParser::RuleRow_format_3d);
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
    setState(271);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BarePKParser::Peak: {
        setState(268);
        match(BarePKParser::Peak);
        setState(269);
        match(BarePKParser::X_ppm);
        break;
      }

      case BarePKParser::X_PPM: {
        setState(270);
        match(BarePKParser::X_PPM);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(273);
    match(BarePKParser::Y_ppm);
    setState(274);
    match(BarePKParser::Z_ppm);
    setState(278);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::X_width) {
      setState(275);
      match(BarePKParser::X_width);
      setState(276);
      match(BarePKParser::Y_width);
      setState(277);
      match(BarePKParser::Z_width);
    }
    setState(281);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Amplitude) {
      setState(280);
      match(BarePKParser::Amplitude);
    }
    setState(284);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Volume) {
      setState(283);
      match(BarePKParser::Volume);
    }
    setState(287);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Label) {
      setState(286);
      match(BarePKParser::Label);
    }
    setState(290);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Comment) {
      setState(289);
      match(BarePKParser::Comment);
    }
    setState(292);
    match(BarePKParser::RETURN_FO);
    setState(294); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(293);
              peak_list_row_3d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(296); 
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

//----------------- Row_format_4dContext ------------------------------------------------------------------

BarePKParser::Row_format_4dContext::Row_format_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::Y_ppm() {
  return getToken(BarePKParser::Y_ppm, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::Z_ppm() {
  return getToken(BarePKParser::Z_ppm, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::A_ppm() {
  return getToken(BarePKParser::A_ppm, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::RETURN_FO() {
  return getToken(BarePKParser::RETURN_FO, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::Peak() {
  return getToken(BarePKParser::Peak, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::X_ppm() {
  return getToken(BarePKParser::X_ppm, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::X_PPM() {
  return getToken(BarePKParser::X_PPM, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::X_width() {
  return getToken(BarePKParser::X_width, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::Y_width() {
  return getToken(BarePKParser::Y_width, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::Z_width() {
  return getToken(BarePKParser::Z_width, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::A_width() {
  return getToken(BarePKParser::A_width, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::Amplitude() {
  return getToken(BarePKParser::Amplitude, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::Volume() {
  return getToken(BarePKParser::Volume, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::Label() {
  return getToken(BarePKParser::Label, 0);
}

tree::TerminalNode* BarePKParser::Row_format_4dContext::Comment() {
  return getToken(BarePKParser::Comment, 0);
}

std::vector<BarePKParser::Peak_list_row_4dContext *> BarePKParser::Row_format_4dContext::peak_list_row_4d() {
  return getRuleContexts<BarePKParser::Peak_list_row_4dContext>();
}

BarePKParser::Peak_list_row_4dContext* BarePKParser::Row_format_4dContext::peak_list_row_4d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_row_4dContext>(i);
}


size_t BarePKParser::Row_format_4dContext::getRuleIndex() const {
  return BarePKParser::RuleRow_format_4d;
}


std::any BarePKParser::Row_format_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitRow_format_4d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Row_format_4dContext* BarePKParser::row_format_4d() {
  Row_format_4dContext *_localctx = _tracker.createInstance<Row_format_4dContext>(_ctx, getState());
  enterRule(_localctx, 30, BarePKParser::RuleRow_format_4d);
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
    setState(301);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BarePKParser::Peak: {
        setState(298);
        match(BarePKParser::Peak);
        setState(299);
        match(BarePKParser::X_ppm);
        break;
      }

      case BarePKParser::X_PPM: {
        setState(300);
        match(BarePKParser::X_PPM);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(303);
    match(BarePKParser::Y_ppm);
    setState(304);
    match(BarePKParser::Z_ppm);
    setState(305);
    match(BarePKParser::A_ppm);
    setState(310);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::X_width) {
      setState(306);
      match(BarePKParser::X_width);
      setState(307);
      match(BarePKParser::Y_width);
      setState(308);
      match(BarePKParser::Z_width);
      setState(309);
      match(BarePKParser::A_width);
    }
    setState(313);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Amplitude) {
      setState(312);
      match(BarePKParser::Amplitude);
    }
    setState(316);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Volume) {
      setState(315);
      match(BarePKParser::Volume);
    }
    setState(319);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Label) {
      setState(318);
      match(BarePKParser::Label);
    }
    setState(322);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Comment) {
      setState(321);
      match(BarePKParser::Comment);
    }
    setState(324);
    match(BarePKParser::RETURN_FO);
    setState(326); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(325);
              peak_list_row_4d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(328); 
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

//----------------- Rev_row_format_2dContext ------------------------------------------------------------------

BarePKParser::Rev_row_format_2dContext::Rev_row_format_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePKParser::Rev_row_format_2dContext::X_ppm() {
  return getToken(BarePKParser::X_ppm, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_2dContext::RETURN_FO() {
  return getToken(BarePKParser::RETURN_FO, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_2dContext::Peak() {
  return getToken(BarePKParser::Peak, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_2dContext::Y_ppm() {
  return getToken(BarePKParser::Y_ppm, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_2dContext::Y_PPM() {
  return getToken(BarePKParser::Y_PPM, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_2dContext::Y_width() {
  return getToken(BarePKParser::Y_width, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_2dContext::X_width() {
  return getToken(BarePKParser::X_width, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_2dContext::Amplitude() {
  return getToken(BarePKParser::Amplitude, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_2dContext::Volume() {
  return getToken(BarePKParser::Volume, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_2dContext::Label() {
  return getToken(BarePKParser::Label, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_2dContext::Comment() {
  return getToken(BarePKParser::Comment, 0);
}

std::vector<BarePKParser::Peak_list_row_2dContext *> BarePKParser::Rev_row_format_2dContext::peak_list_row_2d() {
  return getRuleContexts<BarePKParser::Peak_list_row_2dContext>();
}

BarePKParser::Peak_list_row_2dContext* BarePKParser::Rev_row_format_2dContext::peak_list_row_2d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_row_2dContext>(i);
}


size_t BarePKParser::Rev_row_format_2dContext::getRuleIndex() const {
  return BarePKParser::RuleRev_row_format_2d;
}


std::any BarePKParser::Rev_row_format_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitRev_row_format_2d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Rev_row_format_2dContext* BarePKParser::rev_row_format_2d() {
  Rev_row_format_2dContext *_localctx = _tracker.createInstance<Rev_row_format_2dContext>(_ctx, getState());
  enterRule(_localctx, 32, BarePKParser::RuleRev_row_format_2d);
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
    setState(333);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BarePKParser::Peak: {
        setState(330);
        match(BarePKParser::Peak);
        setState(331);
        match(BarePKParser::Y_ppm);
        break;
      }

      case BarePKParser::Y_PPM: {
        setState(332);
        match(BarePKParser::Y_PPM);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(335);
    match(BarePKParser::X_ppm);
    setState(338);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Y_width) {
      setState(336);
      match(BarePKParser::Y_width);
      setState(337);
      match(BarePKParser::X_width);
    }
    setState(341);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Amplitude) {
      setState(340);
      match(BarePKParser::Amplitude);
    }
    setState(344);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Volume) {
      setState(343);
      match(BarePKParser::Volume);
    }
    setState(347);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Label) {
      setState(346);
      match(BarePKParser::Label);
    }
    setState(350);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Comment) {
      setState(349);
      match(BarePKParser::Comment);
    }
    setState(352);
    match(BarePKParser::RETURN_FO);
    setState(354); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(353);
              peak_list_row_2d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(356); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 42, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Rev_row_format_3dContext ------------------------------------------------------------------

BarePKParser::Rev_row_format_3dContext::Rev_row_format_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::Y_ppm() {
  return getToken(BarePKParser::Y_ppm, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::X_ppm() {
  return getToken(BarePKParser::X_ppm, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::RETURN_FO() {
  return getToken(BarePKParser::RETURN_FO, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::Peak() {
  return getToken(BarePKParser::Peak, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::Z_ppm() {
  return getToken(BarePKParser::Z_ppm, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::Z_PPM() {
  return getToken(BarePKParser::Z_PPM, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::Z_width() {
  return getToken(BarePKParser::Z_width, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::Y_width() {
  return getToken(BarePKParser::Y_width, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::X_width() {
  return getToken(BarePKParser::X_width, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::Amplitude() {
  return getToken(BarePKParser::Amplitude, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::Volume() {
  return getToken(BarePKParser::Volume, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::Label() {
  return getToken(BarePKParser::Label, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_3dContext::Comment() {
  return getToken(BarePKParser::Comment, 0);
}

std::vector<BarePKParser::Peak_list_row_3dContext *> BarePKParser::Rev_row_format_3dContext::peak_list_row_3d() {
  return getRuleContexts<BarePKParser::Peak_list_row_3dContext>();
}

BarePKParser::Peak_list_row_3dContext* BarePKParser::Rev_row_format_3dContext::peak_list_row_3d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_row_3dContext>(i);
}


size_t BarePKParser::Rev_row_format_3dContext::getRuleIndex() const {
  return BarePKParser::RuleRev_row_format_3d;
}


std::any BarePKParser::Rev_row_format_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitRev_row_format_3d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Rev_row_format_3dContext* BarePKParser::rev_row_format_3d() {
  Rev_row_format_3dContext *_localctx = _tracker.createInstance<Rev_row_format_3dContext>(_ctx, getState());
  enterRule(_localctx, 34, BarePKParser::RuleRev_row_format_3d);
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
    setState(361);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BarePKParser::Peak: {
        setState(358);
        match(BarePKParser::Peak);
        setState(359);
        match(BarePKParser::Z_ppm);
        break;
      }

      case BarePKParser::Z_PPM: {
        setState(360);
        match(BarePKParser::Z_PPM);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(363);
    match(BarePKParser::Y_ppm);
    setState(364);
    match(BarePKParser::X_ppm);
    setState(368);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Z_width) {
      setState(365);
      match(BarePKParser::Z_width);
      setState(366);
      match(BarePKParser::Y_width);
      setState(367);
      match(BarePKParser::X_width);
    }
    setState(371);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Amplitude) {
      setState(370);
      match(BarePKParser::Amplitude);
    }
    setState(374);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Volume) {
      setState(373);
      match(BarePKParser::Volume);
    }
    setState(377);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Label) {
      setState(376);
      match(BarePKParser::Label);
    }
    setState(380);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Comment) {
      setState(379);
      match(BarePKParser::Comment);
    }
    setState(382);
    match(BarePKParser::RETURN_FO);
    setState(384); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(383);
              peak_list_row_3d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(386); 
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

//----------------- Rev_row_format_4dContext ------------------------------------------------------------------

BarePKParser::Rev_row_format_4dContext::Rev_row_format_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::Z_ppm() {
  return getToken(BarePKParser::Z_ppm, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::Y_ppm() {
  return getToken(BarePKParser::Y_ppm, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::X_ppm() {
  return getToken(BarePKParser::X_ppm, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::RETURN_FO() {
  return getToken(BarePKParser::RETURN_FO, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::Peak() {
  return getToken(BarePKParser::Peak, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::A_ppm() {
  return getToken(BarePKParser::A_ppm, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::A_PPM() {
  return getToken(BarePKParser::A_PPM, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::A_width() {
  return getToken(BarePKParser::A_width, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::Z_width() {
  return getToken(BarePKParser::Z_width, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::Y_width() {
  return getToken(BarePKParser::Y_width, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::X_width() {
  return getToken(BarePKParser::X_width, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::Amplitude() {
  return getToken(BarePKParser::Amplitude, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::Volume() {
  return getToken(BarePKParser::Volume, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::Label() {
  return getToken(BarePKParser::Label, 0);
}

tree::TerminalNode* BarePKParser::Rev_row_format_4dContext::Comment() {
  return getToken(BarePKParser::Comment, 0);
}

std::vector<BarePKParser::Peak_list_row_4dContext *> BarePKParser::Rev_row_format_4dContext::peak_list_row_4d() {
  return getRuleContexts<BarePKParser::Peak_list_row_4dContext>();
}

BarePKParser::Peak_list_row_4dContext* BarePKParser::Rev_row_format_4dContext::peak_list_row_4d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_row_4dContext>(i);
}


size_t BarePKParser::Rev_row_format_4dContext::getRuleIndex() const {
  return BarePKParser::RuleRev_row_format_4d;
}


std::any BarePKParser::Rev_row_format_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitRev_row_format_4d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Rev_row_format_4dContext* BarePKParser::rev_row_format_4d() {
  Rev_row_format_4dContext *_localctx = _tracker.createInstance<Rev_row_format_4dContext>(_ctx, getState());
  enterRule(_localctx, 36, BarePKParser::RuleRev_row_format_4d);
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
    setState(391);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BarePKParser::Peak: {
        setState(388);
        match(BarePKParser::Peak);
        setState(389);
        match(BarePKParser::A_ppm);
        break;
      }

      case BarePKParser::A_PPM: {
        setState(390);
        match(BarePKParser::A_PPM);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(393);
    match(BarePKParser::Z_ppm);
    setState(394);
    match(BarePKParser::Y_ppm);
    setState(395);
    match(BarePKParser::X_ppm);
    setState(400);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::A_width) {
      setState(396);
      match(BarePKParser::A_width);
      setState(397);
      match(BarePKParser::Z_width);
      setState(398);
      match(BarePKParser::Y_width);
      setState(399);
      match(BarePKParser::X_width);
    }
    setState(403);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Amplitude) {
      setState(402);
      match(BarePKParser::Amplitude);
    }
    setState(406);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Volume) {
      setState(405);
      match(BarePKParser::Volume);
    }
    setState(409);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Label) {
      setState(408);
      match(BarePKParser::Label);
    }
    setState(412);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePKParser::Comment) {
      setState(411);
      match(BarePKParser::Comment);
    }
    setState(414);
    match(BarePKParser::RETURN_FO);
    setState(416); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(415);
              peak_list_row_4d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(418); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 56, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Row_format_wo_label_2dContext ------------------------------------------------------------------

BarePKParser::Row_format_wo_label_2dContext::Row_format_wo_label_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BarePKParser::Peak_list_row_2dContext *> BarePKParser::Row_format_wo_label_2dContext::peak_list_row_2d() {
  return getRuleContexts<BarePKParser::Peak_list_row_2dContext>();
}

BarePKParser::Peak_list_row_2dContext* BarePKParser::Row_format_wo_label_2dContext::peak_list_row_2d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_row_2dContext>(i);
}


size_t BarePKParser::Row_format_wo_label_2dContext::getRuleIndex() const {
  return BarePKParser::RuleRow_format_wo_label_2d;
}


std::any BarePKParser::Row_format_wo_label_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitRow_format_wo_label_2d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Row_format_wo_label_2dContext* BarePKParser::row_format_wo_label_2d() {
  Row_format_wo_label_2dContext *_localctx = _tracker.createInstance<Row_format_wo_label_2dContext>(_ctx, getState());
  enterRule(_localctx, 38, BarePKParser::RuleRow_format_wo_label_2d);

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
    setState(421); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(420);
              peak_list_row_2d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(423); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 57, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Row_format_wo_label_3dContext ------------------------------------------------------------------

BarePKParser::Row_format_wo_label_3dContext::Row_format_wo_label_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BarePKParser::Peak_list_row_3dContext *> BarePKParser::Row_format_wo_label_3dContext::peak_list_row_3d() {
  return getRuleContexts<BarePKParser::Peak_list_row_3dContext>();
}

BarePKParser::Peak_list_row_3dContext* BarePKParser::Row_format_wo_label_3dContext::peak_list_row_3d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_row_3dContext>(i);
}


size_t BarePKParser::Row_format_wo_label_3dContext::getRuleIndex() const {
  return BarePKParser::RuleRow_format_wo_label_3d;
}


std::any BarePKParser::Row_format_wo_label_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitRow_format_wo_label_3d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Row_format_wo_label_3dContext* BarePKParser::row_format_wo_label_3d() {
  Row_format_wo_label_3dContext *_localctx = _tracker.createInstance<Row_format_wo_label_3dContext>(_ctx, getState());
  enterRule(_localctx, 40, BarePKParser::RuleRow_format_wo_label_3d);

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
    setState(426); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(425);
              peak_list_row_3d();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(428); 
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

//----------------- Row_format_wo_label_4dContext ------------------------------------------------------------------

BarePKParser::Row_format_wo_label_4dContext::Row_format_wo_label_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BarePKParser::Peak_list_row_4dContext *> BarePKParser::Row_format_wo_label_4dContext::peak_list_row_4d() {
  return getRuleContexts<BarePKParser::Peak_list_row_4dContext>();
}

BarePKParser::Peak_list_row_4dContext* BarePKParser::Row_format_wo_label_4dContext::peak_list_row_4d(size_t i) {
  return getRuleContext<BarePKParser::Peak_list_row_4dContext>(i);
}


size_t BarePKParser::Row_format_wo_label_4dContext::getRuleIndex() const {
  return BarePKParser::RuleRow_format_wo_label_4d;
}


std::any BarePKParser::Row_format_wo_label_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitRow_format_wo_label_4d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Row_format_wo_label_4dContext* BarePKParser::row_format_wo_label_4d() {
  Row_format_wo_label_4dContext *_localctx = _tracker.createInstance<Row_format_wo_label_4dContext>(_ctx, getState());
  enterRule(_localctx, 42, BarePKParser::RuleRow_format_wo_label_4d);
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
    setState(431); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(430);
      peak_list_row_4d();
      setState(433); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == BarePKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_list_row_2dContext ------------------------------------------------------------------

BarePKParser::Peak_list_row_2dContext::Peak_list_row_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePKParser::Peak_list_row_2dContext::Integer() {
  return getToken(BarePKParser::Integer, 0);
}

std::vector<BarePKParser::PositionContext *> BarePKParser::Peak_list_row_2dContext::position() {
  return getRuleContexts<BarePKParser::PositionContext>();
}

BarePKParser::PositionContext* BarePKParser::Peak_list_row_2dContext::position(size_t i) {
  return getRuleContext<BarePKParser::PositionContext>(i);
}

tree::TerminalNode* BarePKParser::Peak_list_row_2dContext::RETURN() {
  return getToken(BarePKParser::RETURN, 0);
}

tree::TerminalNode* BarePKParser::Peak_list_row_2dContext::EOF() {
  return getToken(BarePKParser::EOF, 0);
}

std::vector<BarePKParser::NumberContext *> BarePKParser::Peak_list_row_2dContext::number() {
  return getRuleContexts<BarePKParser::NumberContext>();
}

BarePKParser::NumberContext* BarePKParser::Peak_list_row_2dContext::number(size_t i) {
  return getRuleContext<BarePKParser::NumberContext>(i);
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_list_row_2dContext::Simple_name() {
  return getTokens(BarePKParser::Simple_name);
}

tree::TerminalNode* BarePKParser::Peak_list_row_2dContext::Simple_name(size_t i) {
  return getToken(BarePKParser::Simple_name, i);
}


size_t BarePKParser::Peak_list_row_2dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_list_row_2d;
}


std::any BarePKParser::Peak_list_row_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_row_2d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_list_row_2dContext* BarePKParser::peak_list_row_2d() {
  Peak_list_row_2dContext *_localctx = _tracker.createInstance<Peak_list_row_2dContext>(_ctx, getState());
  enterRule(_localctx, 44, BarePKParser::RulePeak_list_row_2d);
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
    setState(435);
    match(BarePKParser::Integer);
    setState(436);
    position();
    setState(437);
    position();
    setState(441);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 448) != 0)) {
      setState(438);
      number();
      setState(443);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(447);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BarePKParser::Simple_name) {
      setState(444);
      match(BarePKParser::Simple_name);
      setState(449);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(450);
    _la = _input->LA(1);
    if (!(_la == BarePKParser::EOF

    || _la == BarePKParser::RETURN)) {
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

//----------------- Peak_list_row_3dContext ------------------------------------------------------------------

BarePKParser::Peak_list_row_3dContext::Peak_list_row_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePKParser::Peak_list_row_3dContext::Integer() {
  return getToken(BarePKParser::Integer, 0);
}

std::vector<BarePKParser::PositionContext *> BarePKParser::Peak_list_row_3dContext::position() {
  return getRuleContexts<BarePKParser::PositionContext>();
}

BarePKParser::PositionContext* BarePKParser::Peak_list_row_3dContext::position(size_t i) {
  return getRuleContext<BarePKParser::PositionContext>(i);
}

tree::TerminalNode* BarePKParser::Peak_list_row_3dContext::RETURN() {
  return getToken(BarePKParser::RETURN, 0);
}

tree::TerminalNode* BarePKParser::Peak_list_row_3dContext::EOF() {
  return getToken(BarePKParser::EOF, 0);
}

std::vector<BarePKParser::NumberContext *> BarePKParser::Peak_list_row_3dContext::number() {
  return getRuleContexts<BarePKParser::NumberContext>();
}

BarePKParser::NumberContext* BarePKParser::Peak_list_row_3dContext::number(size_t i) {
  return getRuleContext<BarePKParser::NumberContext>(i);
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_list_row_3dContext::Simple_name() {
  return getTokens(BarePKParser::Simple_name);
}

tree::TerminalNode* BarePKParser::Peak_list_row_3dContext::Simple_name(size_t i) {
  return getToken(BarePKParser::Simple_name, i);
}


size_t BarePKParser::Peak_list_row_3dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_list_row_3d;
}


std::any BarePKParser::Peak_list_row_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_row_3d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_list_row_3dContext* BarePKParser::peak_list_row_3d() {
  Peak_list_row_3dContext *_localctx = _tracker.createInstance<Peak_list_row_3dContext>(_ctx, getState());
  enterRule(_localctx, 46, BarePKParser::RulePeak_list_row_3d);
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
    match(BarePKParser::Integer);
    setState(453);
    position();
    setState(454);
    position();
    setState(455);
    position();
    setState(459);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 448) != 0)) {
      setState(456);
      number();
      setState(461);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(465);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BarePKParser::Simple_name) {
      setState(462);
      match(BarePKParser::Simple_name);
      setState(467);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(468);
    _la = _input->LA(1);
    if (!(_la == BarePKParser::EOF

    || _la == BarePKParser::RETURN)) {
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

//----------------- Peak_list_row_4dContext ------------------------------------------------------------------

BarePKParser::Peak_list_row_4dContext::Peak_list_row_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePKParser::Peak_list_row_4dContext::Integer() {
  return getToken(BarePKParser::Integer, 0);
}

std::vector<BarePKParser::PositionContext *> BarePKParser::Peak_list_row_4dContext::position() {
  return getRuleContexts<BarePKParser::PositionContext>();
}

BarePKParser::PositionContext* BarePKParser::Peak_list_row_4dContext::position(size_t i) {
  return getRuleContext<BarePKParser::PositionContext>(i);
}

tree::TerminalNode* BarePKParser::Peak_list_row_4dContext::RETURN() {
  return getToken(BarePKParser::RETURN, 0);
}

tree::TerminalNode* BarePKParser::Peak_list_row_4dContext::EOF() {
  return getToken(BarePKParser::EOF, 0);
}

std::vector<BarePKParser::NumberContext *> BarePKParser::Peak_list_row_4dContext::number() {
  return getRuleContexts<BarePKParser::NumberContext>();
}

BarePKParser::NumberContext* BarePKParser::Peak_list_row_4dContext::number(size_t i) {
  return getRuleContext<BarePKParser::NumberContext>(i);
}

std::vector<tree::TerminalNode *> BarePKParser::Peak_list_row_4dContext::Simple_name() {
  return getTokens(BarePKParser::Simple_name);
}

tree::TerminalNode* BarePKParser::Peak_list_row_4dContext::Simple_name(size_t i) {
  return getToken(BarePKParser::Simple_name, i);
}


size_t BarePKParser::Peak_list_row_4dContext::getRuleIndex() const {
  return BarePKParser::RulePeak_list_row_4d;
}


std::any BarePKParser::Peak_list_row_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_row_4d(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::Peak_list_row_4dContext* BarePKParser::peak_list_row_4d() {
  Peak_list_row_4dContext *_localctx = _tracker.createInstance<Peak_list_row_4dContext>(_ctx, getState());
  enterRule(_localctx, 48, BarePKParser::RulePeak_list_row_4d);
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
    setState(470);
    match(BarePKParser::Integer);
    setState(471);
    position();
    setState(472);
    position();
    setState(473);
    position();
    setState(474);
    position();
    setState(478);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 448) != 0)) {
      setState(475);
      number();
      setState(480);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(484);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BarePKParser::Simple_name) {
      setState(481);
      match(BarePKParser::Simple_name);
      setState(486);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(487);
    _la = _input->LA(1);
    if (!(_la == BarePKParser::EOF

    || _la == BarePKParser::RETURN)) {
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

BarePKParser::PositionContext::PositionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePKParser::PositionContext::Float() {
  return getToken(BarePKParser::Float, 0);
}

tree::TerminalNode* BarePKParser::PositionContext::Integer() {
  return getToken(BarePKParser::Integer, 0);
}

tree::TerminalNode* BarePKParser::PositionContext::Ambig_float() {
  return getToken(BarePKParser::Ambig_float, 0);
}


size_t BarePKParser::PositionContext::getRuleIndex() const {
  return BarePKParser::RulePosition;
}


std::any BarePKParser::PositionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitPosition(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::PositionContext* BarePKParser::position() {
  PositionContext *_localctx = _tracker.createInstance<PositionContext>(_ctx, getState());
  enterRule(_localctx, 50, BarePKParser::RulePosition);
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
    setState(489);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 704) != 0))) {
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

BarePKParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePKParser::NumberContext::Float() {
  return getToken(BarePKParser::Float, 0);
}

tree::TerminalNode* BarePKParser::NumberContext::Real() {
  return getToken(BarePKParser::Real, 0);
}

tree::TerminalNode* BarePKParser::NumberContext::Integer() {
  return getToken(BarePKParser::Integer, 0);
}


size_t BarePKParser::NumberContext::getRuleIndex() const {
  return BarePKParser::RuleNumber;
}


std::any BarePKParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePKParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

BarePKParser::NumberContext* BarePKParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 52, BarePKParser::RuleNumber);
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
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 448) != 0))) {
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

void BarePKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  barepkparserParserInitialize();
#else
  ::antlr4::internal::call_once(barepkparserParserOnceFlag, barepkparserParserInitialize);
#endif
}
