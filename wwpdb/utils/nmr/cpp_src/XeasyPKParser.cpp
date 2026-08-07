
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XeasyPKParser.g4 by ANTLR 4.13.0


#include "XeasyPKParserVisitor.h"

#include "XeasyPKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct XeasyPKParserStaticData final {
  XeasyPKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  XeasyPKParserStaticData(const XeasyPKParserStaticData&) = delete;
  XeasyPKParserStaticData(XeasyPKParserStaticData&&) = delete;
  XeasyPKParserStaticData& operator=(const XeasyPKParserStaticData&) = delete;
  XeasyPKParserStaticData& operator=(XeasyPKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag xeasypkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
XeasyPKParserStaticData *xeasypkparserParserStaticData = nullptr;

void xeasypkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (xeasypkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(xeasypkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<XeasyPKParserStaticData>(
    std::vector<std::string>{
      "xeasy_pk", "dimension", "peak", "format", "iname", "cyana_format", 
      "spectrum", "tolerance", "peak_list_2d", "peak_2d", "peak_list_3d", 
      "peak_3d", "peak_list_4d", "peak_4d", "position", "number", "type_code", 
      "assign", "comment"
    },
    std::vector<std::string>{
      "", "", "", "'#FORMAT'", "", "'#INAME'", "'#CYANAFORMAT'", "'#SPECTRUM'", 
      "'#TOLERANCE'"
    },
    std::vector<std::string>{
      "", "Num_of_dim", "Num_of_peaks", "Format", "XEASY_WO_FORMAT", "Iname", 
      "Cyana_format", "Spectrum", "Tolerance", "Integer", "Float", "Real", 
      "COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", "Simple_name", "SPACE", 
      "RETURN", "SECTION_COMMENT", "LINE_COMMENT", "Integer_ND", "SPACE_ND", 
      "RETURN_ND", "Integer_NP", "SPACE_NP", "RETURN_NP", "Simple_name_FO", 
      "SPACE_FO", "RETURN_FO", "Integer_IN", "Simple_name_IN", "SPACE_IN", 
      "RETURN_IN", "Simple_name_CY", "SPACE_CY", "RETURN_CY", "Simple_name_SP", 
      "SPACE_SP", "RETURN_SP", "Float_TO", "TOACE_TO", "RETURN_TO", "Any_name", 
      "SPACE_CM", "RETURN_CM"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,44,311,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,3,0,40,8,0,1,0,1,0,1,0,
  	1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,54,8,0,10,0,12,0,57,9,0,1,0,1,
  	0,3,0,61,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,4,3,75,8,
  	3,11,3,12,3,76,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,4,
  	6,92,8,6,11,6,12,6,93,1,6,1,6,1,7,1,7,4,7,100,8,7,11,7,12,7,101,1,7,1,
  	7,1,8,1,8,5,8,108,8,8,10,8,12,8,111,9,8,4,8,113,8,8,11,8,12,8,114,1,9,
  	1,9,1,9,1,9,1,9,3,9,122,8,9,1,9,1,9,1,9,3,9,127,8,9,1,9,1,9,1,9,1,9,1,
  	9,3,9,134,8,9,1,9,3,9,137,8,9,1,9,1,9,1,9,3,9,142,8,9,3,9,144,8,9,1,9,
  	1,9,1,9,3,9,149,8,9,1,9,3,9,152,8,9,1,9,1,9,1,9,3,9,157,8,9,5,9,159,8,
  	9,10,9,12,9,162,9,9,1,10,1,10,5,10,166,8,10,10,10,12,10,169,9,10,4,10,
  	171,8,10,11,10,12,10,172,1,11,1,11,1,11,1,11,1,11,1,11,3,11,181,8,11,
  	1,11,1,11,1,11,3,11,186,8,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,194,8,
  	11,1,11,3,11,197,8,11,1,11,1,11,1,11,3,11,202,8,11,3,11,204,8,11,1,11,
  	1,11,1,11,1,11,3,11,210,8,11,1,11,3,11,213,8,11,1,11,1,11,1,11,3,11,218,
  	8,11,5,11,220,8,11,10,11,12,11,223,9,11,1,12,1,12,5,12,227,8,12,10,12,
  	12,12,230,9,12,4,12,232,8,12,11,12,12,12,233,1,13,1,13,1,13,1,13,1,13,
  	1,13,1,13,3,13,243,8,13,1,13,1,13,1,13,3,13,248,8,13,1,13,1,13,1,13,1,
  	13,1,13,1,13,1,13,3,13,257,8,13,1,13,3,13,260,8,13,1,13,1,13,1,13,3,13,
  	265,8,13,3,13,267,8,13,1,13,1,13,1,13,1,13,1,13,3,13,274,8,13,1,13,3,
  	13,277,8,13,1,13,1,13,1,13,3,13,282,8,13,5,13,284,8,13,10,13,12,13,287,
  	9,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,17,3,17,298,8,17,3,17,
  	300,8,17,1,18,1,18,5,18,304,8,18,10,18,12,18,307,9,18,1,18,1,18,1,18,
  	0,0,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,5,1,1,17,
  	17,1,0,9,10,2,0,9,11,15,15,2,0,9,9,15,15,1,1,44,44,354,0,39,1,0,0,0,2,
  	64,1,0,0,0,4,68,1,0,0,0,6,72,1,0,0,0,8,80,1,0,0,0,10,85,1,0,0,0,12,89,
  	1,0,0,0,14,97,1,0,0,0,16,112,1,0,0,0,18,116,1,0,0,0,20,170,1,0,0,0,22,
  	174,1,0,0,0,24,231,1,0,0,0,26,235,1,0,0,0,28,288,1,0,0,0,30,290,1,0,0,
  	0,32,292,1,0,0,0,34,299,1,0,0,0,36,301,1,0,0,0,38,40,5,17,0,0,39,38,1,
  	0,0,0,39,40,1,0,0,0,40,55,1,0,0,0,41,54,3,2,1,0,42,54,3,4,2,0,43,54,3,
  	6,3,0,44,54,3,8,4,0,45,54,3,10,5,0,46,54,3,12,6,0,47,54,3,14,7,0,48,54,
  	3,36,18,0,49,54,3,16,8,0,50,54,3,20,10,0,51,54,3,24,12,0,52,54,5,17,0,
  	0,53,41,1,0,0,0,53,42,1,0,0,0,53,43,1,0,0,0,53,44,1,0,0,0,53,45,1,0,0,
  	0,53,46,1,0,0,0,53,47,1,0,0,0,53,48,1,0,0,0,53,49,1,0,0,0,53,50,1,0,0,
  	0,53,51,1,0,0,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,
  	0,56,60,1,0,0,0,57,55,1,0,0,0,58,61,5,17,0,0,59,61,3,36,18,0,60,58,1,
  	0,0,0,60,59,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,5,0,0,1,63,1,1,
  	0,0,0,64,65,5,1,0,0,65,66,5,20,0,0,66,67,5,22,0,0,67,3,1,0,0,0,68,69,
  	5,2,0,0,69,70,5,23,0,0,70,71,5,25,0,0,71,5,1,0,0,0,72,74,5,3,0,0,73,75,
  	5,26,0,0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,78,
  	1,0,0,0,78,79,5,28,0,0,79,7,1,0,0,0,80,81,5,5,0,0,81,82,5,29,0,0,82,83,
  	5,30,0,0,83,84,5,32,0,0,84,9,1,0,0,0,85,86,5,6,0,0,86,87,5,33,0,0,87,
  	88,5,35,0,0,88,11,1,0,0,0,89,91,5,7,0,0,90,92,5,36,0,0,91,90,1,0,0,0,
  	92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,5,38,0,
  	0,96,13,1,0,0,0,97,99,5,8,0,0,98,100,5,39,0,0,99,98,1,0,0,0,100,101,1,
  	0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,5,41,0,0,
  	104,15,1,0,0,0,105,109,3,18,9,0,106,108,3,36,18,0,107,106,1,0,0,0,108,
  	111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,113,1,0,0,0,111,109,1,
  	0,0,0,112,105,1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,
  	115,17,1,0,0,0,116,117,5,9,0,0,117,118,3,28,14,0,118,119,3,28,14,0,119,
  	121,5,9,0,0,120,122,5,15,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,123,
  	1,0,0,0,123,124,3,30,15,0,124,126,3,30,15,0,125,127,5,15,0,0,126,125,
  	1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,143,3,32,16,0,129,144,7,0,
  	0,0,130,131,3,34,17,0,131,133,3,34,17,0,132,134,5,9,0,0,133,132,1,0,0,
  	0,133,134,1,0,0,0,134,136,1,0,0,0,135,137,5,9,0,0,136,135,1,0,0,0,136,
  	137,1,0,0,0,137,141,1,0,0,0,138,142,5,17,0,0,139,142,3,36,18,0,140,142,
  	5,0,0,1,141,138,1,0,0,0,141,139,1,0,0,0,141,140,1,0,0,0,142,144,1,0,0,
  	0,143,129,1,0,0,0,143,130,1,0,0,0,144,160,1,0,0,0,145,146,3,34,17,0,146,
  	148,3,34,17,0,147,149,5,9,0,0,148,147,1,0,0,0,148,149,1,0,0,0,149,151,
  	1,0,0,0,150,152,5,9,0,0,151,150,1,0,0,0,151,152,1,0,0,0,152,156,1,0,0,
  	0,153,157,5,17,0,0,154,157,3,36,18,0,155,157,5,0,0,1,156,153,1,0,0,0,
  	156,154,1,0,0,0,156,155,1,0,0,0,157,159,1,0,0,0,158,145,1,0,0,0,159,162,
  	1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,19,1,0,0,0,162,160,1,0,0,
  	0,163,167,3,22,11,0,164,166,3,36,18,0,165,164,1,0,0,0,166,169,1,0,0,0,
  	167,165,1,0,0,0,167,168,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,170,163,
  	1,0,0,0,171,172,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,21,1,0,0,
  	0,174,175,5,9,0,0,175,176,3,28,14,0,176,177,3,28,14,0,177,178,3,28,14,
  	0,178,180,5,9,0,0,179,181,5,15,0,0,180,179,1,0,0,0,180,181,1,0,0,0,181,
  	182,1,0,0,0,182,183,3,30,15,0,183,185,3,30,15,0,184,186,5,15,0,0,185,
  	184,1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,203,3,32,16,0,188,204,
  	7,0,0,0,189,190,3,34,17,0,190,191,3,34,17,0,191,193,3,34,17,0,192,194,
  	5,9,0,0,193,192,1,0,0,0,193,194,1,0,0,0,194,196,1,0,0,0,195,197,5,9,0,
  	0,196,195,1,0,0,0,196,197,1,0,0,0,197,201,1,0,0,0,198,202,5,17,0,0,199,
  	202,3,36,18,0,200,202,5,0,0,1,201,198,1,0,0,0,201,199,1,0,0,0,201,200,
  	1,0,0,0,202,204,1,0,0,0,203,188,1,0,0,0,203,189,1,0,0,0,204,221,1,0,0,
  	0,205,206,3,34,17,0,206,207,3,34,17,0,207,209,3,34,17,0,208,210,5,9,0,
  	0,209,208,1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,213,5,9,0,0,212,
  	211,1,0,0,0,212,213,1,0,0,0,213,217,1,0,0,0,214,218,5,17,0,0,215,218,
  	3,36,18,0,216,218,5,0,0,1,217,214,1,0,0,0,217,215,1,0,0,0,217,216,1,0,
  	0,0,218,220,1,0,0,0,219,205,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,
  	222,1,0,0,0,222,23,1,0,0,0,223,221,1,0,0,0,224,228,3,26,13,0,225,227,
  	3,36,18,0,226,225,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,1,0,
  	0,0,229,232,1,0,0,0,230,228,1,0,0,0,231,224,1,0,0,0,232,233,1,0,0,0,233,
  	231,1,0,0,0,233,234,1,0,0,0,234,25,1,0,0,0,235,236,5,9,0,0,236,237,3,
  	28,14,0,237,238,3,28,14,0,238,239,3,28,14,0,239,240,3,28,14,0,240,242,
  	5,9,0,0,241,243,5,15,0,0,242,241,1,0,0,0,242,243,1,0,0,0,243,244,1,0,
  	0,0,244,245,3,30,15,0,245,247,3,30,15,0,246,248,5,15,0,0,247,246,1,0,
  	0,0,247,248,1,0,0,0,248,249,1,0,0,0,249,266,3,32,16,0,250,267,7,0,0,0,
  	251,252,3,34,17,0,252,253,3,34,17,0,253,254,3,34,17,0,254,256,3,34,17,
  	0,255,257,5,9,0,0,256,255,1,0,0,0,256,257,1,0,0,0,257,259,1,0,0,0,258,
  	260,5,9,0,0,259,258,1,0,0,0,259,260,1,0,0,0,260,264,1,0,0,0,261,265,5,
  	17,0,0,262,265,3,36,18,0,263,265,5,0,0,1,264,261,1,0,0,0,264,262,1,0,
  	0,0,264,263,1,0,0,0,265,267,1,0,0,0,266,250,1,0,0,0,266,251,1,0,0,0,267,
  	285,1,0,0,0,268,269,3,34,17,0,269,270,3,34,17,0,270,271,3,34,17,0,271,
  	273,3,34,17,0,272,274,5,9,0,0,273,272,1,0,0,0,273,274,1,0,0,0,274,276,
  	1,0,0,0,275,277,5,9,0,0,276,275,1,0,0,0,276,277,1,0,0,0,277,281,1,0,0,
  	0,278,282,5,17,0,0,279,282,3,36,18,0,280,282,5,0,0,1,281,278,1,0,0,0,
  	281,279,1,0,0,0,281,280,1,0,0,0,282,284,1,0,0,0,283,268,1,0,0,0,284,287,
  	1,0,0,0,285,283,1,0,0,0,285,286,1,0,0,0,286,27,1,0,0,0,287,285,1,0,0,
  	0,288,289,7,1,0,0,289,29,1,0,0,0,290,291,7,2,0,0,291,31,1,0,0,0,292,293,
  	7,3,0,0,293,33,1,0,0,0,294,300,5,9,0,0,295,297,5,15,0,0,296,298,5,9,0,
  	0,297,296,1,0,0,0,297,298,1,0,0,0,298,300,1,0,0,0,299,294,1,0,0,0,299,
  	295,1,0,0,0,300,35,1,0,0,0,301,305,5,12,0,0,302,304,5,42,0,0,303,302,
  	1,0,0,0,304,307,1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,308,1,0,0,
  	0,307,305,1,0,0,0,308,309,7,4,0,0,309,37,1,0,0,0,46,39,53,55,60,76,93,
  	101,109,114,121,126,133,136,141,143,148,151,156,160,167,172,180,185,193,
  	196,201,203,209,212,217,221,228,233,242,247,256,259,264,266,273,276,281,
  	285,297,299,305
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  xeasypkparserParserStaticData = staticData.release();
}

}

XeasyPKParser::XeasyPKParser(TokenStream *input) : XeasyPKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

XeasyPKParser::XeasyPKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  XeasyPKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *xeasypkparserParserStaticData->atn, xeasypkparserParserStaticData->decisionToDFA, xeasypkparserParserStaticData->sharedContextCache, options);
}

XeasyPKParser::~XeasyPKParser() {
  delete _interpreter;
}

const atn::ATN& XeasyPKParser::getATN() const {
  return *xeasypkparserParserStaticData->atn;
}

std::string XeasyPKParser::getGrammarFileName() const {
  return "XeasyPKParser.g4";
}

const std::vector<std::string>& XeasyPKParser::getRuleNames() const {
  return xeasypkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& XeasyPKParser::getVocabulary() const {
  return xeasypkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView XeasyPKParser::getSerializedATN() const {
  return xeasypkparserParserStaticData->serializedATN;
}


//----------------- Xeasy_pkContext ------------------------------------------------------------------

XeasyPKParser::Xeasy_pkContext::Xeasy_pkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::Xeasy_pkContext::EOF() {
  return getToken(XeasyPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> XeasyPKParser::Xeasy_pkContext::RETURN() {
  return getTokens(XeasyPKParser::RETURN);
}

tree::TerminalNode* XeasyPKParser::Xeasy_pkContext::RETURN(size_t i) {
  return getToken(XeasyPKParser::RETURN, i);
}

std::vector<XeasyPKParser::DimensionContext *> XeasyPKParser::Xeasy_pkContext::dimension() {
  return getRuleContexts<XeasyPKParser::DimensionContext>();
}

XeasyPKParser::DimensionContext* XeasyPKParser::Xeasy_pkContext::dimension(size_t i) {
  return getRuleContext<XeasyPKParser::DimensionContext>(i);
}

std::vector<XeasyPKParser::PeakContext *> XeasyPKParser::Xeasy_pkContext::peak() {
  return getRuleContexts<XeasyPKParser::PeakContext>();
}

XeasyPKParser::PeakContext* XeasyPKParser::Xeasy_pkContext::peak(size_t i) {
  return getRuleContext<XeasyPKParser::PeakContext>(i);
}

std::vector<XeasyPKParser::FormatContext *> XeasyPKParser::Xeasy_pkContext::format() {
  return getRuleContexts<XeasyPKParser::FormatContext>();
}

XeasyPKParser::FormatContext* XeasyPKParser::Xeasy_pkContext::format(size_t i) {
  return getRuleContext<XeasyPKParser::FormatContext>(i);
}

std::vector<XeasyPKParser::InameContext *> XeasyPKParser::Xeasy_pkContext::iname() {
  return getRuleContexts<XeasyPKParser::InameContext>();
}

XeasyPKParser::InameContext* XeasyPKParser::Xeasy_pkContext::iname(size_t i) {
  return getRuleContext<XeasyPKParser::InameContext>(i);
}

std::vector<XeasyPKParser::Cyana_formatContext *> XeasyPKParser::Xeasy_pkContext::cyana_format() {
  return getRuleContexts<XeasyPKParser::Cyana_formatContext>();
}

XeasyPKParser::Cyana_formatContext* XeasyPKParser::Xeasy_pkContext::cyana_format(size_t i) {
  return getRuleContext<XeasyPKParser::Cyana_formatContext>(i);
}

std::vector<XeasyPKParser::SpectrumContext *> XeasyPKParser::Xeasy_pkContext::spectrum() {
  return getRuleContexts<XeasyPKParser::SpectrumContext>();
}

XeasyPKParser::SpectrumContext* XeasyPKParser::Xeasy_pkContext::spectrum(size_t i) {
  return getRuleContext<XeasyPKParser::SpectrumContext>(i);
}

std::vector<XeasyPKParser::ToleranceContext *> XeasyPKParser::Xeasy_pkContext::tolerance() {
  return getRuleContexts<XeasyPKParser::ToleranceContext>();
}

XeasyPKParser::ToleranceContext* XeasyPKParser::Xeasy_pkContext::tolerance(size_t i) {
  return getRuleContext<XeasyPKParser::ToleranceContext>(i);
}

std::vector<XeasyPKParser::CommentContext *> XeasyPKParser::Xeasy_pkContext::comment() {
  return getRuleContexts<XeasyPKParser::CommentContext>();
}

XeasyPKParser::CommentContext* XeasyPKParser::Xeasy_pkContext::comment(size_t i) {
  return getRuleContext<XeasyPKParser::CommentContext>(i);
}

std::vector<XeasyPKParser::Peak_list_2dContext *> XeasyPKParser::Xeasy_pkContext::peak_list_2d() {
  return getRuleContexts<XeasyPKParser::Peak_list_2dContext>();
}

XeasyPKParser::Peak_list_2dContext* XeasyPKParser::Xeasy_pkContext::peak_list_2d(size_t i) {
  return getRuleContext<XeasyPKParser::Peak_list_2dContext>(i);
}

std::vector<XeasyPKParser::Peak_list_3dContext *> XeasyPKParser::Xeasy_pkContext::peak_list_3d() {
  return getRuleContexts<XeasyPKParser::Peak_list_3dContext>();
}

XeasyPKParser::Peak_list_3dContext* XeasyPKParser::Xeasy_pkContext::peak_list_3d(size_t i) {
  return getRuleContext<XeasyPKParser::Peak_list_3dContext>(i);
}

std::vector<XeasyPKParser::Peak_list_4dContext *> XeasyPKParser::Xeasy_pkContext::peak_list_4d() {
  return getRuleContexts<XeasyPKParser::Peak_list_4dContext>();
}

XeasyPKParser::Peak_list_4dContext* XeasyPKParser::Xeasy_pkContext::peak_list_4d(size_t i) {
  return getRuleContext<XeasyPKParser::Peak_list_4dContext>(i);
}


size_t XeasyPKParser::Xeasy_pkContext::getRuleIndex() const {
  return XeasyPKParser::RuleXeasy_pk;
}


std::any XeasyPKParser::Xeasy_pkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitXeasy_pk(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::Xeasy_pkContext* XeasyPKParser::xeasy_pk() {
  Xeasy_pkContext *_localctx = _tracker.createInstance<Xeasy_pkContext>(_ctx, getState());
  enterRule(_localctx, 0, XeasyPKParser::RuleXeasy_pk);

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
    setState(39);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(38);
      match(XeasyPKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(55);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(53);
        _errHandler->sync(this);
        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
        case 1: {
          setState(41);
          dimension();
          break;
        }

        case 2: {
          setState(42);
          peak();
          break;
        }

        case 3: {
          setState(43);
          format();
          break;
        }

        case 4: {
          setState(44);
          iname();
          break;
        }

        case 5: {
          setState(45);
          cyana_format();
          break;
        }

        case 6: {
          setState(46);
          spectrum();
          break;
        }

        case 7: {
          setState(47);
          tolerance();
          break;
        }

        case 8: {
          setState(48);
          comment();
          break;
        }

        case 9: {
          setState(49);
          peak_list_2d();
          break;
        }

        case 10: {
          setState(50);
          peak_list_3d();
          break;
        }

        case 11: {
          setState(51);
          peak_list_4d();
          break;
        }

        case 12: {
          setState(52);
          match(XeasyPKParser::RETURN);
          break;
        }

        default:
          break;
        } 
      }
      setState(57);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
    }
    setState(60);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case XeasyPKParser::RETURN: {
        setState(58);
        match(XeasyPKParser::RETURN);
        break;
      }

      case XeasyPKParser::COMMENT: {
        setState(59);
        comment();
        break;
      }

      case XeasyPKParser::EOF: {
        break;
      }

    default:
      break;
    }
    setState(62);
    match(XeasyPKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DimensionContext ------------------------------------------------------------------

XeasyPKParser::DimensionContext::DimensionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::DimensionContext::Num_of_dim() {
  return getToken(XeasyPKParser::Num_of_dim, 0);
}

tree::TerminalNode* XeasyPKParser::DimensionContext::Integer_ND() {
  return getToken(XeasyPKParser::Integer_ND, 0);
}

tree::TerminalNode* XeasyPKParser::DimensionContext::RETURN_ND() {
  return getToken(XeasyPKParser::RETURN_ND, 0);
}


size_t XeasyPKParser::DimensionContext::getRuleIndex() const {
  return XeasyPKParser::RuleDimension;
}


std::any XeasyPKParser::DimensionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitDimension(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::DimensionContext* XeasyPKParser::dimension() {
  DimensionContext *_localctx = _tracker.createInstance<DimensionContext>(_ctx, getState());
  enterRule(_localctx, 2, XeasyPKParser::RuleDimension);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(64);
    match(XeasyPKParser::Num_of_dim);
    setState(65);
    match(XeasyPKParser::Integer_ND);
    setState(66);
    match(XeasyPKParser::RETURN_ND);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- PeakContext ------------------------------------------------------------------

XeasyPKParser::PeakContext::PeakContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::PeakContext::Num_of_peaks() {
  return getToken(XeasyPKParser::Num_of_peaks, 0);
}

tree::TerminalNode* XeasyPKParser::PeakContext::Integer_NP() {
  return getToken(XeasyPKParser::Integer_NP, 0);
}

tree::TerminalNode* XeasyPKParser::PeakContext::RETURN_NP() {
  return getToken(XeasyPKParser::RETURN_NP, 0);
}


size_t XeasyPKParser::PeakContext::getRuleIndex() const {
  return XeasyPKParser::RulePeak;
}


std::any XeasyPKParser::PeakContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::PeakContext* XeasyPKParser::peak() {
  PeakContext *_localctx = _tracker.createInstance<PeakContext>(_ctx, getState());
  enterRule(_localctx, 4, XeasyPKParser::RulePeak);

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
    match(XeasyPKParser::Num_of_peaks);
    setState(69);
    match(XeasyPKParser::Integer_NP);
    setState(70);
    match(XeasyPKParser::RETURN_NP);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- FormatContext ------------------------------------------------------------------

XeasyPKParser::FormatContext::FormatContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::FormatContext::Format() {
  return getToken(XeasyPKParser::Format, 0);
}

tree::TerminalNode* XeasyPKParser::FormatContext::RETURN_FO() {
  return getToken(XeasyPKParser::RETURN_FO, 0);
}

std::vector<tree::TerminalNode *> XeasyPKParser::FormatContext::Simple_name_FO() {
  return getTokens(XeasyPKParser::Simple_name_FO);
}

tree::TerminalNode* XeasyPKParser::FormatContext::Simple_name_FO(size_t i) {
  return getToken(XeasyPKParser::Simple_name_FO, i);
}


size_t XeasyPKParser::FormatContext::getRuleIndex() const {
  return XeasyPKParser::RuleFormat;
}


std::any XeasyPKParser::FormatContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitFormat(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::FormatContext* XeasyPKParser::format() {
  FormatContext *_localctx = _tracker.createInstance<FormatContext>(_ctx, getState());
  enterRule(_localctx, 6, XeasyPKParser::RuleFormat);
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
    setState(72);
    match(XeasyPKParser::Format);
    setState(74); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(73);
      match(XeasyPKParser::Simple_name_FO);
      setState(76); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == XeasyPKParser::Simple_name_FO);
    setState(78);
    match(XeasyPKParser::RETURN_FO);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- InameContext ------------------------------------------------------------------

XeasyPKParser::InameContext::InameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::InameContext::Iname() {
  return getToken(XeasyPKParser::Iname, 0);
}

tree::TerminalNode* XeasyPKParser::InameContext::Integer_IN() {
  return getToken(XeasyPKParser::Integer_IN, 0);
}

tree::TerminalNode* XeasyPKParser::InameContext::Simple_name_IN() {
  return getToken(XeasyPKParser::Simple_name_IN, 0);
}

tree::TerminalNode* XeasyPKParser::InameContext::RETURN_IN() {
  return getToken(XeasyPKParser::RETURN_IN, 0);
}


size_t XeasyPKParser::InameContext::getRuleIndex() const {
  return XeasyPKParser::RuleIname;
}


std::any XeasyPKParser::InameContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitIname(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::InameContext* XeasyPKParser::iname() {
  InameContext *_localctx = _tracker.createInstance<InameContext>(_ctx, getState());
  enterRule(_localctx, 8, XeasyPKParser::RuleIname);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(80);
    match(XeasyPKParser::Iname);
    setState(81);
    match(XeasyPKParser::Integer_IN);
    setState(82);
    match(XeasyPKParser::Simple_name_IN);
    setState(83);
    match(XeasyPKParser::RETURN_IN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Cyana_formatContext ------------------------------------------------------------------

XeasyPKParser::Cyana_formatContext::Cyana_formatContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::Cyana_formatContext::Cyana_format() {
  return getToken(XeasyPKParser::Cyana_format, 0);
}

tree::TerminalNode* XeasyPKParser::Cyana_formatContext::Simple_name_CY() {
  return getToken(XeasyPKParser::Simple_name_CY, 0);
}

tree::TerminalNode* XeasyPKParser::Cyana_formatContext::RETURN_CY() {
  return getToken(XeasyPKParser::RETURN_CY, 0);
}


size_t XeasyPKParser::Cyana_formatContext::getRuleIndex() const {
  return XeasyPKParser::RuleCyana_format;
}


std::any XeasyPKParser::Cyana_formatContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitCyana_format(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::Cyana_formatContext* XeasyPKParser::cyana_format() {
  Cyana_formatContext *_localctx = _tracker.createInstance<Cyana_formatContext>(_ctx, getState());
  enterRule(_localctx, 10, XeasyPKParser::RuleCyana_format);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(85);
    match(XeasyPKParser::Cyana_format);
    setState(86);
    match(XeasyPKParser::Simple_name_CY);
    setState(87);
    match(XeasyPKParser::RETURN_CY);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- SpectrumContext ------------------------------------------------------------------

XeasyPKParser::SpectrumContext::SpectrumContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::SpectrumContext::Spectrum() {
  return getToken(XeasyPKParser::Spectrum, 0);
}

tree::TerminalNode* XeasyPKParser::SpectrumContext::RETURN_SP() {
  return getToken(XeasyPKParser::RETURN_SP, 0);
}

std::vector<tree::TerminalNode *> XeasyPKParser::SpectrumContext::Simple_name_SP() {
  return getTokens(XeasyPKParser::Simple_name_SP);
}

tree::TerminalNode* XeasyPKParser::SpectrumContext::Simple_name_SP(size_t i) {
  return getToken(XeasyPKParser::Simple_name_SP, i);
}


size_t XeasyPKParser::SpectrumContext::getRuleIndex() const {
  return XeasyPKParser::RuleSpectrum;
}


std::any XeasyPKParser::SpectrumContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitSpectrum(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::SpectrumContext* XeasyPKParser::spectrum() {
  SpectrumContext *_localctx = _tracker.createInstance<SpectrumContext>(_ctx, getState());
  enterRule(_localctx, 12, XeasyPKParser::RuleSpectrum);
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
    setState(89);
    match(XeasyPKParser::Spectrum);
    setState(91); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(90);
      match(XeasyPKParser::Simple_name_SP);
      setState(93); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == XeasyPKParser::Simple_name_SP);
    setState(95);
    match(XeasyPKParser::RETURN_SP);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ToleranceContext ------------------------------------------------------------------

XeasyPKParser::ToleranceContext::ToleranceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::ToleranceContext::Tolerance() {
  return getToken(XeasyPKParser::Tolerance, 0);
}

tree::TerminalNode* XeasyPKParser::ToleranceContext::RETURN_TO() {
  return getToken(XeasyPKParser::RETURN_TO, 0);
}

std::vector<tree::TerminalNode *> XeasyPKParser::ToleranceContext::Float_TO() {
  return getTokens(XeasyPKParser::Float_TO);
}

tree::TerminalNode* XeasyPKParser::ToleranceContext::Float_TO(size_t i) {
  return getToken(XeasyPKParser::Float_TO, i);
}


size_t XeasyPKParser::ToleranceContext::getRuleIndex() const {
  return XeasyPKParser::RuleTolerance;
}


std::any XeasyPKParser::ToleranceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitTolerance(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::ToleranceContext* XeasyPKParser::tolerance() {
  ToleranceContext *_localctx = _tracker.createInstance<ToleranceContext>(_ctx, getState());
  enterRule(_localctx, 14, XeasyPKParser::RuleTolerance);
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
    setState(97);
    match(XeasyPKParser::Tolerance);
    setState(99); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(98);
      match(XeasyPKParser::Float_TO);
      setState(101); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == XeasyPKParser::Float_TO);
    setState(103);
    match(XeasyPKParser::RETURN_TO);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_list_2dContext ------------------------------------------------------------------

XeasyPKParser::Peak_list_2dContext::Peak_list_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<XeasyPKParser::Peak_2dContext *> XeasyPKParser::Peak_list_2dContext::peak_2d() {
  return getRuleContexts<XeasyPKParser::Peak_2dContext>();
}

XeasyPKParser::Peak_2dContext* XeasyPKParser::Peak_list_2dContext::peak_2d(size_t i) {
  return getRuleContext<XeasyPKParser::Peak_2dContext>(i);
}

std::vector<XeasyPKParser::CommentContext *> XeasyPKParser::Peak_list_2dContext::comment() {
  return getRuleContexts<XeasyPKParser::CommentContext>();
}

XeasyPKParser::CommentContext* XeasyPKParser::Peak_list_2dContext::comment(size_t i) {
  return getRuleContext<XeasyPKParser::CommentContext>(i);
}


size_t XeasyPKParser::Peak_list_2dContext::getRuleIndex() const {
  return XeasyPKParser::RulePeak_list_2d;
}


std::any XeasyPKParser::Peak_list_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_2d(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::Peak_list_2dContext* XeasyPKParser::peak_list_2d() {
  Peak_list_2dContext *_localctx = _tracker.createInstance<Peak_list_2dContext>(_ctx, getState());
  enterRule(_localctx, 16, XeasyPKParser::RulePeak_list_2d);

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
    setState(112); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(105);
              peak_2d();
              setState(109);
              _errHandler->sync(this);
              alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx);
              while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
                if (alt == 1) {
                  setState(106);
                  comment(); 
                }
                setState(111);
                _errHandler->sync(this);
                alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(114); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx);
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

XeasyPKParser::Peak_2dContext::Peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> XeasyPKParser::Peak_2dContext::Integer() {
  return getTokens(XeasyPKParser::Integer);
}

tree::TerminalNode* XeasyPKParser::Peak_2dContext::Integer(size_t i) {
  return getToken(XeasyPKParser::Integer, i);
}

std::vector<XeasyPKParser::PositionContext *> XeasyPKParser::Peak_2dContext::position() {
  return getRuleContexts<XeasyPKParser::PositionContext>();
}

XeasyPKParser::PositionContext* XeasyPKParser::Peak_2dContext::position(size_t i) {
  return getRuleContext<XeasyPKParser::PositionContext>(i);
}

std::vector<XeasyPKParser::NumberContext *> XeasyPKParser::Peak_2dContext::number() {
  return getRuleContexts<XeasyPKParser::NumberContext>();
}

XeasyPKParser::NumberContext* XeasyPKParser::Peak_2dContext::number(size_t i) {
  return getRuleContext<XeasyPKParser::NumberContext>(i);
}

XeasyPKParser::Type_codeContext* XeasyPKParser::Peak_2dContext::type_code() {
  return getRuleContext<XeasyPKParser::Type_codeContext>(0);
}

std::vector<XeasyPKParser::AssignContext *> XeasyPKParser::Peak_2dContext::assign() {
  return getRuleContexts<XeasyPKParser::AssignContext>();
}

XeasyPKParser::AssignContext* XeasyPKParser::Peak_2dContext::assign(size_t i) {
  return getRuleContext<XeasyPKParser::AssignContext>(i);
}

std::vector<tree::TerminalNode *> XeasyPKParser::Peak_2dContext::Simple_name() {
  return getTokens(XeasyPKParser::Simple_name);
}

tree::TerminalNode* XeasyPKParser::Peak_2dContext::Simple_name(size_t i) {
  return getToken(XeasyPKParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> XeasyPKParser::Peak_2dContext::RETURN() {
  return getTokens(XeasyPKParser::RETURN);
}

tree::TerminalNode* XeasyPKParser::Peak_2dContext::RETURN(size_t i) {
  return getToken(XeasyPKParser::RETURN, i);
}

std::vector<tree::TerminalNode *> XeasyPKParser::Peak_2dContext::EOF() {
  return getTokens(XeasyPKParser::EOF);
}

tree::TerminalNode* XeasyPKParser::Peak_2dContext::EOF(size_t i) {
  return getToken(XeasyPKParser::EOF, i);
}

std::vector<XeasyPKParser::CommentContext *> XeasyPKParser::Peak_2dContext::comment() {
  return getRuleContexts<XeasyPKParser::CommentContext>();
}

XeasyPKParser::CommentContext* XeasyPKParser::Peak_2dContext::comment(size_t i) {
  return getRuleContext<XeasyPKParser::CommentContext>(i);
}


size_t XeasyPKParser::Peak_2dContext::getRuleIndex() const {
  return XeasyPKParser::RulePeak_2d;
}


std::any XeasyPKParser::Peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::Peak_2dContext* XeasyPKParser::peak_2d() {
  Peak_2dContext *_localctx = _tracker.createInstance<Peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 18, XeasyPKParser::RulePeak_2d);
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
    setState(116);
    match(XeasyPKParser::Integer);
    setState(117);
    position();
    setState(118);
    position();
    setState(119);
    match(XeasyPKParser::Integer);
    setState(121);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx)) {
    case 1: {
      setState(120);
      match(XeasyPKParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(123);
    number();
    setState(124);
    number();
    setState(126);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 10, _ctx)) {
    case 1: {
      setState(125);
      match(XeasyPKParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(128);
    type_code();
    setState(143);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case XeasyPKParser::EOF:
      case XeasyPKParser::RETURN: {
        setState(129);
        _la = _input->LA(1);
        if (!(_la == XeasyPKParser::EOF

        || _la == XeasyPKParser::RETURN)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        break;
      }

      case XeasyPKParser::Integer:
      case XeasyPKParser::Simple_name: {
        setState(130);
        assign();
        setState(131);
        assign();
        setState(133);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx)) {
        case 1: {
          setState(132);
          match(XeasyPKParser::Integer);
          break;
        }

        default:
          break;
        }
        setState(136);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == XeasyPKParser::Integer) {
          setState(135);
          match(XeasyPKParser::Integer);
        }
        setState(141);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case XeasyPKParser::RETURN: {
            setState(138);
            match(XeasyPKParser::RETURN);
            break;
          }

          case XeasyPKParser::COMMENT: {
            setState(139);
            comment();
            break;
          }

          case XeasyPKParser::EOF: {
            setState(140);
            match(XeasyPKParser::EOF);
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
    setState(160);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(145);
        assign();
        setState(146);
        assign();
        setState(148);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 15, _ctx)) {
        case 1: {
          setState(147);
          match(XeasyPKParser::Integer);
          break;
        }

        default:
          break;
        }
        setState(151);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == XeasyPKParser::Integer) {
          setState(150);
          match(XeasyPKParser::Integer);
        }
        setState(156);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case XeasyPKParser::RETURN: {
            setState(153);
            match(XeasyPKParser::RETURN);
            break;
          }

          case XeasyPKParser::COMMENT: {
            setState(154);
            comment();
            break;
          }

          case XeasyPKParser::EOF: {
            setState(155);
            match(XeasyPKParser::EOF);
            break;
          }

        default:
          throw NoViableAltException(this);
        } 
      }
      setState(162);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx);
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

XeasyPKParser::Peak_list_3dContext::Peak_list_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<XeasyPKParser::Peak_3dContext *> XeasyPKParser::Peak_list_3dContext::peak_3d() {
  return getRuleContexts<XeasyPKParser::Peak_3dContext>();
}

XeasyPKParser::Peak_3dContext* XeasyPKParser::Peak_list_3dContext::peak_3d(size_t i) {
  return getRuleContext<XeasyPKParser::Peak_3dContext>(i);
}

std::vector<XeasyPKParser::CommentContext *> XeasyPKParser::Peak_list_3dContext::comment() {
  return getRuleContexts<XeasyPKParser::CommentContext>();
}

XeasyPKParser::CommentContext* XeasyPKParser::Peak_list_3dContext::comment(size_t i) {
  return getRuleContext<XeasyPKParser::CommentContext>(i);
}


size_t XeasyPKParser::Peak_list_3dContext::getRuleIndex() const {
  return XeasyPKParser::RulePeak_list_3d;
}


std::any XeasyPKParser::Peak_list_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_3d(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::Peak_list_3dContext* XeasyPKParser::peak_list_3d() {
  Peak_list_3dContext *_localctx = _tracker.createInstance<Peak_list_3dContext>(_ctx, getState());
  enterRule(_localctx, 20, XeasyPKParser::RulePeak_list_3d);

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
    setState(170); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(163);
              peak_3d();
              setState(167);
              _errHandler->sync(this);
              alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 19, _ctx);
              while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
                if (alt == 1) {
                  setState(164);
                  comment(); 
                }
                setState(169);
                _errHandler->sync(this);
                alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 19, _ctx);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(172); 
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

//----------------- Peak_3dContext ------------------------------------------------------------------

XeasyPKParser::Peak_3dContext::Peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> XeasyPKParser::Peak_3dContext::Integer() {
  return getTokens(XeasyPKParser::Integer);
}

tree::TerminalNode* XeasyPKParser::Peak_3dContext::Integer(size_t i) {
  return getToken(XeasyPKParser::Integer, i);
}

std::vector<XeasyPKParser::PositionContext *> XeasyPKParser::Peak_3dContext::position() {
  return getRuleContexts<XeasyPKParser::PositionContext>();
}

XeasyPKParser::PositionContext* XeasyPKParser::Peak_3dContext::position(size_t i) {
  return getRuleContext<XeasyPKParser::PositionContext>(i);
}

std::vector<XeasyPKParser::NumberContext *> XeasyPKParser::Peak_3dContext::number() {
  return getRuleContexts<XeasyPKParser::NumberContext>();
}

XeasyPKParser::NumberContext* XeasyPKParser::Peak_3dContext::number(size_t i) {
  return getRuleContext<XeasyPKParser::NumberContext>(i);
}

XeasyPKParser::Type_codeContext* XeasyPKParser::Peak_3dContext::type_code() {
  return getRuleContext<XeasyPKParser::Type_codeContext>(0);
}

std::vector<XeasyPKParser::AssignContext *> XeasyPKParser::Peak_3dContext::assign() {
  return getRuleContexts<XeasyPKParser::AssignContext>();
}

XeasyPKParser::AssignContext* XeasyPKParser::Peak_3dContext::assign(size_t i) {
  return getRuleContext<XeasyPKParser::AssignContext>(i);
}

std::vector<tree::TerminalNode *> XeasyPKParser::Peak_3dContext::Simple_name() {
  return getTokens(XeasyPKParser::Simple_name);
}

tree::TerminalNode* XeasyPKParser::Peak_3dContext::Simple_name(size_t i) {
  return getToken(XeasyPKParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> XeasyPKParser::Peak_3dContext::RETURN() {
  return getTokens(XeasyPKParser::RETURN);
}

tree::TerminalNode* XeasyPKParser::Peak_3dContext::RETURN(size_t i) {
  return getToken(XeasyPKParser::RETURN, i);
}

std::vector<tree::TerminalNode *> XeasyPKParser::Peak_3dContext::EOF() {
  return getTokens(XeasyPKParser::EOF);
}

tree::TerminalNode* XeasyPKParser::Peak_3dContext::EOF(size_t i) {
  return getToken(XeasyPKParser::EOF, i);
}

std::vector<XeasyPKParser::CommentContext *> XeasyPKParser::Peak_3dContext::comment() {
  return getRuleContexts<XeasyPKParser::CommentContext>();
}

XeasyPKParser::CommentContext* XeasyPKParser::Peak_3dContext::comment(size_t i) {
  return getRuleContext<XeasyPKParser::CommentContext>(i);
}


size_t XeasyPKParser::Peak_3dContext::getRuleIndex() const {
  return XeasyPKParser::RulePeak_3d;
}


std::any XeasyPKParser::Peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::Peak_3dContext* XeasyPKParser::peak_3d() {
  Peak_3dContext *_localctx = _tracker.createInstance<Peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 22, XeasyPKParser::RulePeak_3d);
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
    setState(174);
    match(XeasyPKParser::Integer);
    setState(175);
    position();
    setState(176);
    position();
    setState(177);
    position();
    setState(178);
    match(XeasyPKParser::Integer);
    setState(180);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 21, _ctx)) {
    case 1: {
      setState(179);
      match(XeasyPKParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(182);
    number();
    setState(183);
    number();
    setState(185);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 22, _ctx)) {
    case 1: {
      setState(184);
      match(XeasyPKParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(187);
    type_code();
    setState(203);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case XeasyPKParser::EOF:
      case XeasyPKParser::RETURN: {
        setState(188);
        _la = _input->LA(1);
        if (!(_la == XeasyPKParser::EOF

        || _la == XeasyPKParser::RETURN)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        break;
      }

      case XeasyPKParser::Integer:
      case XeasyPKParser::Simple_name: {
        setState(189);
        assign();
        setState(190);
        assign();
        setState(191);
        assign();
        setState(193);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx)) {
        case 1: {
          setState(192);
          match(XeasyPKParser::Integer);
          break;
        }

        default:
          break;
        }
        setState(196);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == XeasyPKParser::Integer) {
          setState(195);
          match(XeasyPKParser::Integer);
        }
        setState(201);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case XeasyPKParser::RETURN: {
            setState(198);
            match(XeasyPKParser::RETURN);
            break;
          }

          case XeasyPKParser::COMMENT: {
            setState(199);
            comment();
            break;
          }

          case XeasyPKParser::EOF: {
            setState(200);
            match(XeasyPKParser::EOF);
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
    setState(221);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 30, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(205);
        assign();
        setState(206);
        assign();
        setState(207);
        assign();
        setState(209);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 27, _ctx)) {
        case 1: {
          setState(208);
          match(XeasyPKParser::Integer);
          break;
        }

        default:
          break;
        }
        setState(212);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == XeasyPKParser::Integer) {
          setState(211);
          match(XeasyPKParser::Integer);
        }
        setState(217);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case XeasyPKParser::RETURN: {
            setState(214);
            match(XeasyPKParser::RETURN);
            break;
          }

          case XeasyPKParser::COMMENT: {
            setState(215);
            comment();
            break;
          }

          case XeasyPKParser::EOF: {
            setState(216);
            match(XeasyPKParser::EOF);
            break;
          }

        default:
          throw NoViableAltException(this);
        } 
      }
      setState(223);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 30, _ctx);
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

XeasyPKParser::Peak_list_4dContext::Peak_list_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<XeasyPKParser::Peak_4dContext *> XeasyPKParser::Peak_list_4dContext::peak_4d() {
  return getRuleContexts<XeasyPKParser::Peak_4dContext>();
}

XeasyPKParser::Peak_4dContext* XeasyPKParser::Peak_list_4dContext::peak_4d(size_t i) {
  return getRuleContext<XeasyPKParser::Peak_4dContext>(i);
}

std::vector<XeasyPKParser::CommentContext *> XeasyPKParser::Peak_list_4dContext::comment() {
  return getRuleContexts<XeasyPKParser::CommentContext>();
}

XeasyPKParser::CommentContext* XeasyPKParser::Peak_list_4dContext::comment(size_t i) {
  return getRuleContext<XeasyPKParser::CommentContext>(i);
}


size_t XeasyPKParser::Peak_list_4dContext::getRuleIndex() const {
  return XeasyPKParser::RulePeak_list_4d;
}


std::any XeasyPKParser::Peak_list_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_4d(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::Peak_list_4dContext* XeasyPKParser::peak_list_4d() {
  Peak_list_4dContext *_localctx = _tracker.createInstance<Peak_list_4dContext>(_ctx, getState());
  enterRule(_localctx, 24, XeasyPKParser::RulePeak_list_4d);

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
    setState(231); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(224);
              peak_4d();
              setState(228);
              _errHandler->sync(this);
              alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 31, _ctx);
              while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
                if (alt == 1) {
                  setState(225);
                  comment(); 
                }
                setState(230);
                _errHandler->sync(this);
                alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 31, _ctx);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(233); 
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

//----------------- Peak_4dContext ------------------------------------------------------------------

XeasyPKParser::Peak_4dContext::Peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> XeasyPKParser::Peak_4dContext::Integer() {
  return getTokens(XeasyPKParser::Integer);
}

tree::TerminalNode* XeasyPKParser::Peak_4dContext::Integer(size_t i) {
  return getToken(XeasyPKParser::Integer, i);
}

std::vector<XeasyPKParser::PositionContext *> XeasyPKParser::Peak_4dContext::position() {
  return getRuleContexts<XeasyPKParser::PositionContext>();
}

XeasyPKParser::PositionContext* XeasyPKParser::Peak_4dContext::position(size_t i) {
  return getRuleContext<XeasyPKParser::PositionContext>(i);
}

std::vector<XeasyPKParser::NumberContext *> XeasyPKParser::Peak_4dContext::number() {
  return getRuleContexts<XeasyPKParser::NumberContext>();
}

XeasyPKParser::NumberContext* XeasyPKParser::Peak_4dContext::number(size_t i) {
  return getRuleContext<XeasyPKParser::NumberContext>(i);
}

XeasyPKParser::Type_codeContext* XeasyPKParser::Peak_4dContext::type_code() {
  return getRuleContext<XeasyPKParser::Type_codeContext>(0);
}

std::vector<XeasyPKParser::AssignContext *> XeasyPKParser::Peak_4dContext::assign() {
  return getRuleContexts<XeasyPKParser::AssignContext>();
}

XeasyPKParser::AssignContext* XeasyPKParser::Peak_4dContext::assign(size_t i) {
  return getRuleContext<XeasyPKParser::AssignContext>(i);
}

std::vector<tree::TerminalNode *> XeasyPKParser::Peak_4dContext::Simple_name() {
  return getTokens(XeasyPKParser::Simple_name);
}

tree::TerminalNode* XeasyPKParser::Peak_4dContext::Simple_name(size_t i) {
  return getToken(XeasyPKParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> XeasyPKParser::Peak_4dContext::RETURN() {
  return getTokens(XeasyPKParser::RETURN);
}

tree::TerminalNode* XeasyPKParser::Peak_4dContext::RETURN(size_t i) {
  return getToken(XeasyPKParser::RETURN, i);
}

std::vector<tree::TerminalNode *> XeasyPKParser::Peak_4dContext::EOF() {
  return getTokens(XeasyPKParser::EOF);
}

tree::TerminalNode* XeasyPKParser::Peak_4dContext::EOF(size_t i) {
  return getToken(XeasyPKParser::EOF, i);
}

std::vector<XeasyPKParser::CommentContext *> XeasyPKParser::Peak_4dContext::comment() {
  return getRuleContexts<XeasyPKParser::CommentContext>();
}

XeasyPKParser::CommentContext* XeasyPKParser::Peak_4dContext::comment(size_t i) {
  return getRuleContext<XeasyPKParser::CommentContext>(i);
}


size_t XeasyPKParser::Peak_4dContext::getRuleIndex() const {
  return XeasyPKParser::RulePeak_4d;
}


std::any XeasyPKParser::Peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::Peak_4dContext* XeasyPKParser::peak_4d() {
  Peak_4dContext *_localctx = _tracker.createInstance<Peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 26, XeasyPKParser::RulePeak_4d);
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
    setState(235);
    match(XeasyPKParser::Integer);
    setState(236);
    position();
    setState(237);
    position();
    setState(238);
    position();
    setState(239);
    position();
    setState(240);
    match(XeasyPKParser::Integer);
    setState(242);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 33, _ctx)) {
    case 1: {
      setState(241);
      match(XeasyPKParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(244);
    number();
    setState(245);
    number();
    setState(247);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 34, _ctx)) {
    case 1: {
      setState(246);
      match(XeasyPKParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(249);
    type_code();
    setState(266);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case XeasyPKParser::EOF:
      case XeasyPKParser::RETURN: {
        setState(250);
        _la = _input->LA(1);
        if (!(_la == XeasyPKParser::EOF

        || _la == XeasyPKParser::RETURN)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        break;
      }

      case XeasyPKParser::Integer:
      case XeasyPKParser::Simple_name: {
        setState(251);
        assign();
        setState(252);
        assign();
        setState(253);
        assign();
        setState(254);
        assign();
        setState(256);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 35, _ctx)) {
        case 1: {
          setState(255);
          match(XeasyPKParser::Integer);
          break;
        }

        default:
          break;
        }
        setState(259);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == XeasyPKParser::Integer) {
          setState(258);
          match(XeasyPKParser::Integer);
        }
        setState(264);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case XeasyPKParser::RETURN: {
            setState(261);
            match(XeasyPKParser::RETURN);
            break;
          }

          case XeasyPKParser::COMMENT: {
            setState(262);
            comment();
            break;
          }

          case XeasyPKParser::EOF: {
            setState(263);
            match(XeasyPKParser::EOF);
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
    setState(285);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 42, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(268);
        assign();
        setState(269);
        assign();
        setState(270);
        assign();
        setState(271);
        assign();
        setState(273);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 39, _ctx)) {
        case 1: {
          setState(272);
          match(XeasyPKParser::Integer);
          break;
        }

        default:
          break;
        }
        setState(276);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == XeasyPKParser::Integer) {
          setState(275);
          match(XeasyPKParser::Integer);
        }
        setState(281);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case XeasyPKParser::RETURN: {
            setState(278);
            match(XeasyPKParser::RETURN);
            break;
          }

          case XeasyPKParser::COMMENT: {
            setState(279);
            comment();
            break;
          }

          case XeasyPKParser::EOF: {
            setState(280);
            match(XeasyPKParser::EOF);
            break;
          }

        default:
          throw NoViableAltException(this);
        } 
      }
      setState(287);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 42, _ctx);
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

XeasyPKParser::PositionContext::PositionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::PositionContext::Float() {
  return getToken(XeasyPKParser::Float, 0);
}

tree::TerminalNode* XeasyPKParser::PositionContext::Integer() {
  return getToken(XeasyPKParser::Integer, 0);
}


size_t XeasyPKParser::PositionContext::getRuleIndex() const {
  return XeasyPKParser::RulePosition;
}


std::any XeasyPKParser::PositionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitPosition(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::PositionContext* XeasyPKParser::position() {
  PositionContext *_localctx = _tracker.createInstance<PositionContext>(_ctx, getState());
  enterRule(_localctx, 28, XeasyPKParser::RulePosition);
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
    setState(288);
    _la = _input->LA(1);
    if (!(_la == XeasyPKParser::Integer

    || _la == XeasyPKParser::Float)) {
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

XeasyPKParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::NumberContext::Float() {
  return getToken(XeasyPKParser::Float, 0);
}

tree::TerminalNode* XeasyPKParser::NumberContext::Real() {
  return getToken(XeasyPKParser::Real, 0);
}

tree::TerminalNode* XeasyPKParser::NumberContext::Integer() {
  return getToken(XeasyPKParser::Integer, 0);
}

tree::TerminalNode* XeasyPKParser::NumberContext::Simple_name() {
  return getToken(XeasyPKParser::Simple_name, 0);
}


size_t XeasyPKParser::NumberContext::getRuleIndex() const {
  return XeasyPKParser::RuleNumber;
}


std::any XeasyPKParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::NumberContext* XeasyPKParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 30, XeasyPKParser::RuleNumber);
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
    setState(290);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 36352) != 0))) {
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

//----------------- Type_codeContext ------------------------------------------------------------------

XeasyPKParser::Type_codeContext::Type_codeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::Type_codeContext::Integer() {
  return getToken(XeasyPKParser::Integer, 0);
}

tree::TerminalNode* XeasyPKParser::Type_codeContext::Simple_name() {
  return getToken(XeasyPKParser::Simple_name, 0);
}


size_t XeasyPKParser::Type_codeContext::getRuleIndex() const {
  return XeasyPKParser::RuleType_code;
}


std::any XeasyPKParser::Type_codeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitType_code(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::Type_codeContext* XeasyPKParser::type_code() {
  Type_codeContext *_localctx = _tracker.createInstance<Type_codeContext>(_ctx, getState());
  enterRule(_localctx, 32, XeasyPKParser::RuleType_code);
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
    _la = _input->LA(1);
    if (!(_la == XeasyPKParser::Integer

    || _la == XeasyPKParser::Simple_name)) {
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

//----------------- AssignContext ------------------------------------------------------------------

XeasyPKParser::AssignContext::AssignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::AssignContext::Integer() {
  return getToken(XeasyPKParser::Integer, 0);
}

tree::TerminalNode* XeasyPKParser::AssignContext::Simple_name() {
  return getToken(XeasyPKParser::Simple_name, 0);
}


size_t XeasyPKParser::AssignContext::getRuleIndex() const {
  return XeasyPKParser::RuleAssign;
}


std::any XeasyPKParser::AssignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitAssign(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::AssignContext* XeasyPKParser::assign() {
  AssignContext *_localctx = _tracker.createInstance<AssignContext>(_ctx, getState());
  enterRule(_localctx, 34, XeasyPKParser::RuleAssign);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(299);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case XeasyPKParser::Integer: {
        enterOuterAlt(_localctx, 1);
        setState(294);
        match(XeasyPKParser::Integer);
        break;
      }

      case XeasyPKParser::Simple_name: {
        enterOuterAlt(_localctx, 2);
        setState(295);
        match(XeasyPKParser::Simple_name);
        setState(297);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 43, _ctx)) {
        case 1: {
          setState(296);
          match(XeasyPKParser::Integer);
          break;
        }

        default:
          break;
        }
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

//----------------- CommentContext ------------------------------------------------------------------

XeasyPKParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPKParser::CommentContext::COMMENT() {
  return getToken(XeasyPKParser::COMMENT, 0);
}

tree::TerminalNode* XeasyPKParser::CommentContext::RETURN_CM() {
  return getToken(XeasyPKParser::RETURN_CM, 0);
}

tree::TerminalNode* XeasyPKParser::CommentContext::EOF() {
  return getToken(XeasyPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> XeasyPKParser::CommentContext::Any_name() {
  return getTokens(XeasyPKParser::Any_name);
}

tree::TerminalNode* XeasyPKParser::CommentContext::Any_name(size_t i) {
  return getToken(XeasyPKParser::Any_name, i);
}


size_t XeasyPKParser::CommentContext::getRuleIndex() const {
  return XeasyPKParser::RuleComment;
}


std::any XeasyPKParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPKParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

XeasyPKParser::CommentContext* XeasyPKParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 36, XeasyPKParser::RuleComment);
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
    setState(301);
    match(XeasyPKParser::COMMENT);
    setState(305);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == XeasyPKParser::Any_name) {
      setState(302);
      match(XeasyPKParser::Any_name);
      setState(307);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(308);
    _la = _input->LA(1);
    if (!(_la == XeasyPKParser::EOF

    || _la == XeasyPKParser::RETURN_CM)) {
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

void XeasyPKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  xeasypkparserParserInitialize();
#else
  ::antlr4::internal::call_once(xeasypkparserParserOnceFlag, xeasypkparserParserInitialize);
#endif
}
