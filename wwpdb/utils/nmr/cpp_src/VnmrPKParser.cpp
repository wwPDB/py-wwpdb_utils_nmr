
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/VnmrPKParser.g4 by ANTLR 4.13.0


#include "VnmrPKParserVisitor.h"

#include "VnmrPKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct VnmrPKParserStaticData final {
  VnmrPKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  VnmrPKParserStaticData(const VnmrPKParserStaticData&) = delete;
  VnmrPKParserStaticData(VnmrPKParserStaticData&&) = delete;
  VnmrPKParserStaticData& operator=(const VnmrPKParserStaticData&) = delete;
  VnmrPKParserStaticData& operator=(VnmrPKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag vnmrpkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
VnmrPKParserStaticData *vnmrpkparserParserStaticData = nullptr;

void vnmrpkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (vnmrpkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(vnmrpkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<VnmrPKParserStaticData>(
    std::vector<std::string>{
      "vnmr_pk", "comment", "format", "peak_ll2d", "peak_ll3d", "peak_ll4d", 
      "data_label", "peak_2d", "peak_3d", "peak_4d", "number"
    },
    std::vector<std::string>{
      "", "'peak id.'", "'# Format:'", "", "", "", "", "", "", "", "", "", 
      "", "", "", "", "", "", "", "", "", "'Dev. 0'", "'Dev. 1'", "'Dev. 2'", 
      "'Dev. 3'", "", "", "'Assignment'", "", "", "'Peak_Number'", "", "", 
      "", "", "", "", "", "", "", "", "", "", "", "", "'Label'", "'Comment'"
    },
    std::vector<std::string>{
      "", "Peak_id", "Format", "Integer", "Float", "Real", "COMMENT", "Double_quote_string", 
      "EXCLM_COMMENT", "SMCLN_COMMENT", "Assignment_2d_ex", "Assignment_3d_ex", 
      "Assignment_4d_ex", "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT", 
      "Dim_0_ppm", "Dim_1_ppm", "Dim_2_ppm", "Dim_3_ppm", "Dev_0", "Dev_1", 
      "Dev_2", "Dev_3", "Amplitude_LA", "Volume_LA", "Assignment", "SPACE_LA", 
      "RETURN_LA", "Peak_number", "X_ppm", "Y_ppm", "Z_ppm", "A_ppm", "Amplitude", 
      "Volume", "Linewidth_X", "Linewidth_Y", "Linewidth_Z", "Linewidth_A", 
      "FWHM_X", "FWHM_Y", "FWHM_Z", "FWHM_A", "Label", "Comment", "SPACE_FO", 
      "RETURN_FO", "Any_name", "SPACE_CM", "RETURN_CM"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,51,249,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,3,0,24,8,0,1,0,1,0,1,0,1,0,4,0,30,
  	8,0,11,0,12,0,31,1,0,4,0,35,8,0,11,0,12,0,36,1,0,4,0,40,8,0,11,0,12,0,
  	41,1,0,5,0,45,8,0,10,0,12,0,48,9,0,1,0,1,0,1,1,1,1,5,1,54,8,1,10,1,12,
  	1,57,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,66,8,2,1,2,3,2,69,8,2,1,2,1,
  	2,3,2,73,8,2,1,2,3,2,76,8,2,1,2,3,2,79,8,2,1,2,3,2,82,8,2,1,2,3,2,85,
  	8,2,1,2,3,2,88,8,2,1,2,3,2,91,8,2,1,2,1,2,4,2,95,8,2,11,2,12,2,96,1,2,
  	4,2,100,8,2,11,2,12,2,101,1,2,4,2,105,8,2,11,2,12,2,106,3,2,109,8,2,1,
  	3,1,3,1,3,1,3,1,3,3,3,116,8,3,1,3,3,3,119,8,3,1,3,3,3,122,8,3,1,3,5,3,
  	125,8,3,10,3,12,3,128,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,138,8,4,
  	1,4,3,4,141,8,4,1,4,3,4,144,8,4,1,4,3,4,147,8,4,1,4,5,4,150,8,4,10,4,
  	12,4,153,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,164,8,5,1,5,3,5,
  	167,8,5,1,5,3,5,170,8,5,1,5,3,5,173,8,5,1,5,3,5,176,8,5,1,5,5,5,179,8,
  	5,10,5,12,5,182,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,195,
  	8,6,3,6,197,8,6,1,6,1,6,3,6,201,8,6,1,6,3,6,204,8,6,1,6,1,6,1,7,1,7,1,
  	7,1,7,1,7,1,7,1,7,3,7,215,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
  	1,8,3,8,228,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,
  	9,243,8,9,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,
  	7,1,1,51,51,2,0,37,37,41,41,2,0,38,38,42,42,2,0,39,39,43,43,2,0,40,40,
  	44,44,1,1,14,14,1,0,3,5,285,0,23,1,0,0,0,2,51,1,0,0,0,4,60,1,0,0,0,6,
  	110,1,0,0,0,8,131,1,0,0,0,10,156,1,0,0,0,12,185,1,0,0,0,14,207,1,0,0,
  	0,16,218,1,0,0,0,18,231,1,0,0,0,20,246,1,0,0,0,22,24,5,14,0,0,23,22,1,
  	0,0,0,23,24,1,0,0,0,24,46,1,0,0,0,25,45,3,2,1,0,26,45,3,4,2,0,27,45,3,
  	12,6,0,28,30,3,14,7,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,
  	1,0,0,0,32,45,1,0,0,0,33,35,3,16,8,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,
  	1,0,0,0,36,37,1,0,0,0,37,45,1,0,0,0,38,40,3,18,9,0,39,38,1,0,0,0,40,41,
  	1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,45,1,0,0,0,43,45,5,14,0,0,44,25,
  	1,0,0,0,44,26,1,0,0,0,44,27,1,0,0,0,44,29,1,0,0,0,44,34,1,0,0,0,44,39,
  	1,0,0,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,
  	1,0,0,0,48,46,1,0,0,0,49,50,5,0,0,1,50,1,1,0,0,0,51,55,5,6,0,0,52,54,
  	5,49,0,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,
  	1,0,0,0,57,55,1,0,0,0,58,59,7,0,0,0,59,3,1,0,0,0,60,61,5,2,0,0,61,62,
  	5,30,0,0,62,63,5,31,0,0,63,65,5,32,0,0,64,66,5,33,0,0,65,64,1,0,0,0,65,
  	66,1,0,0,0,66,68,1,0,0,0,67,69,5,34,0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,
  	70,1,0,0,0,70,72,5,35,0,0,71,73,5,36,0,0,72,71,1,0,0,0,72,73,1,0,0,0,
  	73,75,1,0,0,0,74,76,7,1,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,
  	77,79,7,2,0,0,78,77,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,82,7,3,0,0,
  	81,80,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,85,7,4,0,0,84,83,1,0,0,0,
  	84,85,1,0,0,0,85,87,1,0,0,0,86,88,5,45,0,0,87,86,1,0,0,0,87,88,1,0,0,
  	0,88,90,1,0,0,0,89,91,5,46,0,0,90,89,1,0,0,0,90,91,1,0,0,0,91,92,1,0,
  	0,0,92,108,5,48,0,0,93,95,3,6,3,0,94,93,1,0,0,0,95,96,1,0,0,0,96,94,1,
  	0,0,0,96,97,1,0,0,0,97,109,1,0,0,0,98,100,3,8,4,0,99,98,1,0,0,0,100,101,
  	1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,109,1,0,0,0,103,105,3,10,5,
  	0,104,103,1,0,0,0,105,106,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,
  	109,1,0,0,0,108,94,1,0,0,0,108,99,1,0,0,0,108,104,1,0,0,0,109,5,1,0,0,
  	0,110,111,5,3,0,0,111,112,5,4,0,0,112,113,5,4,0,0,113,115,3,20,10,0,114,
  	116,3,20,10,0,115,114,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,119,
  	3,20,10,0,118,117,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,122,3,20,
  	10,0,121,120,1,0,0,0,121,122,1,0,0,0,122,126,1,0,0,0,123,125,5,7,0,0,
  	124,123,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,129,
  	1,0,0,0,128,126,1,0,0,0,129,130,7,5,0,0,130,7,1,0,0,0,131,132,5,3,0,0,
  	132,133,5,4,0,0,133,134,5,4,0,0,134,135,5,4,0,0,135,137,3,20,10,0,136,
  	138,3,20,10,0,137,136,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,141,
  	3,20,10,0,140,139,1,0,0,0,140,141,1,0,0,0,141,143,1,0,0,0,142,144,3,20,
  	10,0,143,142,1,0,0,0,143,144,1,0,0,0,144,146,1,0,0,0,145,147,3,20,10,
  	0,146,145,1,0,0,0,146,147,1,0,0,0,147,151,1,0,0,0,148,150,5,7,0,0,149,
  	148,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,154,1,
  	0,0,0,153,151,1,0,0,0,154,155,7,5,0,0,155,9,1,0,0,0,156,157,5,3,0,0,157,
  	158,5,4,0,0,158,159,5,4,0,0,159,160,5,4,0,0,160,161,5,4,0,0,161,163,3,
  	20,10,0,162,164,3,20,10,0,163,162,1,0,0,0,163,164,1,0,0,0,164,166,1,0,
  	0,0,165,167,3,20,10,0,166,165,1,0,0,0,166,167,1,0,0,0,167,169,1,0,0,0,
  	168,170,3,20,10,0,169,168,1,0,0,0,169,170,1,0,0,0,170,172,1,0,0,0,171,
  	173,3,20,10,0,172,171,1,0,0,0,172,173,1,0,0,0,173,175,1,0,0,0,174,176,
  	3,20,10,0,175,174,1,0,0,0,175,176,1,0,0,0,176,180,1,0,0,0,177,179,5,7,
  	0,0,178,177,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,
  	183,1,0,0,0,182,180,1,0,0,0,183,184,7,5,0,0,184,11,1,0,0,0,185,186,5,
  	1,0,0,186,187,5,17,0,0,187,188,5,21,0,0,188,189,5,18,0,0,189,196,5,22,
  	0,0,190,191,5,19,0,0,191,194,5,23,0,0,192,193,5,20,0,0,193,195,5,24,0,
  	0,194,192,1,0,0,0,194,195,1,0,0,0,195,197,1,0,0,0,196,190,1,0,0,0,196,
  	197,1,0,0,0,197,198,1,0,0,0,198,200,5,25,0,0,199,201,5,26,0,0,200,199,
  	1,0,0,0,200,201,1,0,0,0,201,203,1,0,0,0,202,204,5,27,0,0,203,202,1,0,
  	0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,206,5,29,0,0,206,13,1,0,0,0,207,
  	208,5,3,0,0,208,209,5,4,0,0,209,210,5,4,0,0,210,211,5,4,0,0,211,212,5,
  	4,0,0,212,214,3,20,10,0,213,215,5,10,0,0,214,213,1,0,0,0,214,215,1,0,
  	0,0,215,216,1,0,0,0,216,217,7,5,0,0,217,15,1,0,0,0,218,219,5,3,0,0,219,
  	220,5,4,0,0,220,221,5,4,0,0,221,222,5,4,0,0,222,223,5,4,0,0,223,224,5,
  	4,0,0,224,225,5,4,0,0,225,227,3,20,10,0,226,228,5,11,0,0,227,226,1,0,
  	0,0,227,228,1,0,0,0,228,229,1,0,0,0,229,230,7,5,0,0,230,17,1,0,0,0,231,
  	232,5,3,0,0,232,233,5,4,0,0,233,234,5,4,0,0,234,235,5,4,0,0,235,236,5,
  	4,0,0,236,237,5,4,0,0,237,238,5,4,0,0,238,239,5,4,0,0,239,240,5,4,0,0,
  	240,242,3,20,10,0,241,243,5,12,0,0,242,241,1,0,0,0,242,243,1,0,0,0,243,
  	244,1,0,0,0,244,245,7,5,0,0,245,19,1,0,0,0,246,247,7,6,0,0,247,21,1,0,
  	0,0,42,23,31,36,41,44,46,55,65,68,72,75,78,81,84,87,90,96,101,106,108,
  	115,118,121,126,137,140,143,146,151,163,166,169,172,175,180,194,196,200,
  	203,214,227,242
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  vnmrpkparserParserStaticData = staticData.release();
}

}

VnmrPKParser::VnmrPKParser(TokenStream *input) : VnmrPKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

VnmrPKParser::VnmrPKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  VnmrPKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *vnmrpkparserParserStaticData->atn, vnmrpkparserParserStaticData->decisionToDFA, vnmrpkparserParserStaticData->sharedContextCache, options);
}

VnmrPKParser::~VnmrPKParser() {
  delete _interpreter;
}

const atn::ATN& VnmrPKParser::getATN() const {
  return *vnmrpkparserParserStaticData->atn;
}

std::string VnmrPKParser::getGrammarFileName() const {
  return "VnmrPKParser.g4";
}

const std::vector<std::string>& VnmrPKParser::getRuleNames() const {
  return vnmrpkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& VnmrPKParser::getVocabulary() const {
  return vnmrpkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView VnmrPKParser::getSerializedATN() const {
  return vnmrpkparserParserStaticData->serializedATN;
}


//----------------- Vnmr_pkContext ------------------------------------------------------------------

VnmrPKParser::Vnmr_pkContext::Vnmr_pkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* VnmrPKParser::Vnmr_pkContext::EOF() {
  return getToken(VnmrPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> VnmrPKParser::Vnmr_pkContext::RETURN() {
  return getTokens(VnmrPKParser::RETURN);
}

tree::TerminalNode* VnmrPKParser::Vnmr_pkContext::RETURN(size_t i) {
  return getToken(VnmrPKParser::RETURN, i);
}

std::vector<VnmrPKParser::CommentContext *> VnmrPKParser::Vnmr_pkContext::comment() {
  return getRuleContexts<VnmrPKParser::CommentContext>();
}

VnmrPKParser::CommentContext* VnmrPKParser::Vnmr_pkContext::comment(size_t i) {
  return getRuleContext<VnmrPKParser::CommentContext>(i);
}

std::vector<VnmrPKParser::FormatContext *> VnmrPKParser::Vnmr_pkContext::format() {
  return getRuleContexts<VnmrPKParser::FormatContext>();
}

VnmrPKParser::FormatContext* VnmrPKParser::Vnmr_pkContext::format(size_t i) {
  return getRuleContext<VnmrPKParser::FormatContext>(i);
}

std::vector<VnmrPKParser::Data_labelContext *> VnmrPKParser::Vnmr_pkContext::data_label() {
  return getRuleContexts<VnmrPKParser::Data_labelContext>();
}

VnmrPKParser::Data_labelContext* VnmrPKParser::Vnmr_pkContext::data_label(size_t i) {
  return getRuleContext<VnmrPKParser::Data_labelContext>(i);
}

std::vector<VnmrPKParser::Peak_2dContext *> VnmrPKParser::Vnmr_pkContext::peak_2d() {
  return getRuleContexts<VnmrPKParser::Peak_2dContext>();
}

VnmrPKParser::Peak_2dContext* VnmrPKParser::Vnmr_pkContext::peak_2d(size_t i) {
  return getRuleContext<VnmrPKParser::Peak_2dContext>(i);
}

std::vector<VnmrPKParser::Peak_3dContext *> VnmrPKParser::Vnmr_pkContext::peak_3d() {
  return getRuleContexts<VnmrPKParser::Peak_3dContext>();
}

VnmrPKParser::Peak_3dContext* VnmrPKParser::Vnmr_pkContext::peak_3d(size_t i) {
  return getRuleContext<VnmrPKParser::Peak_3dContext>(i);
}

std::vector<VnmrPKParser::Peak_4dContext *> VnmrPKParser::Vnmr_pkContext::peak_4d() {
  return getRuleContexts<VnmrPKParser::Peak_4dContext>();
}

VnmrPKParser::Peak_4dContext* VnmrPKParser::Vnmr_pkContext::peak_4d(size_t i) {
  return getRuleContext<VnmrPKParser::Peak_4dContext>(i);
}


size_t VnmrPKParser::Vnmr_pkContext::getRuleIndex() const {
  return VnmrPKParser::RuleVnmr_pk;
}


std::any VnmrPKParser::Vnmr_pkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<VnmrPKParserVisitor*>(visitor))
    return parserVisitor->visitVnmr_pk(this);
  else
    return visitor->visitChildren(this);
}

VnmrPKParser::Vnmr_pkContext* VnmrPKParser::vnmr_pk() {
  Vnmr_pkContext *_localctx = _tracker.createInstance<Vnmr_pkContext>(_ctx, getState());
  enterRule(_localctx, 0, VnmrPKParser::RuleVnmr_pk);
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
    setState(23);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(22);
      match(VnmrPKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(46);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 16462) != 0)) {
      setState(44);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx)) {
      case 1: {
        setState(25);
        comment();
        break;
      }

      case 2: {
        setState(26);
        format();
        break;
      }

      case 3: {
        setState(27);
        data_label();
        break;
      }

      case 4: {
        setState(29); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(28);
                  peak_2d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(31); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 5: {
        setState(34); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(33);
                  peak_3d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(36); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 6: {
        setState(39); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(38);
                  peak_4d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(41); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 7: {
        setState(43);
        match(VnmrPKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(48);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(49);
    match(VnmrPKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CommentContext ------------------------------------------------------------------

VnmrPKParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* VnmrPKParser::CommentContext::COMMENT() {
  return getToken(VnmrPKParser::COMMENT, 0);
}

tree::TerminalNode* VnmrPKParser::CommentContext::RETURN_CM() {
  return getToken(VnmrPKParser::RETURN_CM, 0);
}

tree::TerminalNode* VnmrPKParser::CommentContext::EOF() {
  return getToken(VnmrPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> VnmrPKParser::CommentContext::Any_name() {
  return getTokens(VnmrPKParser::Any_name);
}

tree::TerminalNode* VnmrPKParser::CommentContext::Any_name(size_t i) {
  return getToken(VnmrPKParser::Any_name, i);
}


size_t VnmrPKParser::CommentContext::getRuleIndex() const {
  return VnmrPKParser::RuleComment;
}


std::any VnmrPKParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<VnmrPKParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

VnmrPKParser::CommentContext* VnmrPKParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 2, VnmrPKParser::RuleComment);
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
    setState(51);
    match(VnmrPKParser::COMMENT);
    setState(55);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == VnmrPKParser::Any_name) {
      setState(52);
      match(VnmrPKParser::Any_name);
      setState(57);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(58);
    _la = _input->LA(1);
    if (!(_la == VnmrPKParser::EOF

    || _la == VnmrPKParser::RETURN_CM)) {
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

//----------------- FormatContext ------------------------------------------------------------------

VnmrPKParser::FormatContext::FormatContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* VnmrPKParser::FormatContext::Format() {
  return getToken(VnmrPKParser::Format, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::Peak_number() {
  return getToken(VnmrPKParser::Peak_number, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::X_ppm() {
  return getToken(VnmrPKParser::X_ppm, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::Y_ppm() {
  return getToken(VnmrPKParser::Y_ppm, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::Amplitude() {
  return getToken(VnmrPKParser::Amplitude, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::RETURN_FO() {
  return getToken(VnmrPKParser::RETURN_FO, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::Z_ppm() {
  return getToken(VnmrPKParser::Z_ppm, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::A_ppm() {
  return getToken(VnmrPKParser::A_ppm, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::Volume() {
  return getToken(VnmrPKParser::Volume, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::Label() {
  return getToken(VnmrPKParser::Label, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::Comment() {
  return getToken(VnmrPKParser::Comment, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::Linewidth_X() {
  return getToken(VnmrPKParser::Linewidth_X, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::FWHM_X() {
  return getToken(VnmrPKParser::FWHM_X, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::Linewidth_Y() {
  return getToken(VnmrPKParser::Linewidth_Y, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::FWHM_Y() {
  return getToken(VnmrPKParser::FWHM_Y, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::Linewidth_Z() {
  return getToken(VnmrPKParser::Linewidth_Z, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::FWHM_Z() {
  return getToken(VnmrPKParser::FWHM_Z, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::Linewidth_A() {
  return getToken(VnmrPKParser::Linewidth_A, 0);
}

tree::TerminalNode* VnmrPKParser::FormatContext::FWHM_A() {
  return getToken(VnmrPKParser::FWHM_A, 0);
}

std::vector<VnmrPKParser::Peak_ll2dContext *> VnmrPKParser::FormatContext::peak_ll2d() {
  return getRuleContexts<VnmrPKParser::Peak_ll2dContext>();
}

VnmrPKParser::Peak_ll2dContext* VnmrPKParser::FormatContext::peak_ll2d(size_t i) {
  return getRuleContext<VnmrPKParser::Peak_ll2dContext>(i);
}

std::vector<VnmrPKParser::Peak_ll3dContext *> VnmrPKParser::FormatContext::peak_ll3d() {
  return getRuleContexts<VnmrPKParser::Peak_ll3dContext>();
}

VnmrPKParser::Peak_ll3dContext* VnmrPKParser::FormatContext::peak_ll3d(size_t i) {
  return getRuleContext<VnmrPKParser::Peak_ll3dContext>(i);
}

std::vector<VnmrPKParser::Peak_ll4dContext *> VnmrPKParser::FormatContext::peak_ll4d() {
  return getRuleContexts<VnmrPKParser::Peak_ll4dContext>();
}

VnmrPKParser::Peak_ll4dContext* VnmrPKParser::FormatContext::peak_ll4d(size_t i) {
  return getRuleContext<VnmrPKParser::Peak_ll4dContext>(i);
}


size_t VnmrPKParser::FormatContext::getRuleIndex() const {
  return VnmrPKParser::RuleFormat;
}


std::any VnmrPKParser::FormatContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<VnmrPKParserVisitor*>(visitor))
    return parserVisitor->visitFormat(this);
  else
    return visitor->visitChildren(this);
}

VnmrPKParser::FormatContext* VnmrPKParser::format() {
  FormatContext *_localctx = _tracker.createInstance<FormatContext>(_ctx, getState());
  enterRule(_localctx, 4, VnmrPKParser::RuleFormat);
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
    setState(60);
    match(VnmrPKParser::Format);
    setState(61);
    match(VnmrPKParser::Peak_number);
    setState(62);
    match(VnmrPKParser::X_ppm);
    setState(63);
    match(VnmrPKParser::Y_ppm);
    setState(65);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Z_ppm) {
      setState(64);
      match(VnmrPKParser::Z_ppm);
    }
    setState(68);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::A_ppm) {
      setState(67);
      match(VnmrPKParser::A_ppm);
    }
    setState(70);
    match(VnmrPKParser::Amplitude);
    setState(72);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Volume) {
      setState(71);
      match(VnmrPKParser::Volume);
    }
    setState(75);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Linewidth_X

    || _la == VnmrPKParser::FWHM_X) {
      setState(74);
      _la = _input->LA(1);
      if (!(_la == VnmrPKParser::Linewidth_X

      || _la == VnmrPKParser::FWHM_X)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
    }
    setState(78);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Linewidth_Y

    || _la == VnmrPKParser::FWHM_Y) {
      setState(77);
      _la = _input->LA(1);
      if (!(_la == VnmrPKParser::Linewidth_Y

      || _la == VnmrPKParser::FWHM_Y)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
    }
    setState(81);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Linewidth_Z

    || _la == VnmrPKParser::FWHM_Z) {
      setState(80);
      _la = _input->LA(1);
      if (!(_la == VnmrPKParser::Linewidth_Z

      || _la == VnmrPKParser::FWHM_Z)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
    }
    setState(84);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Linewidth_A

    || _la == VnmrPKParser::FWHM_A) {
      setState(83);
      _la = _input->LA(1);
      if (!(_la == VnmrPKParser::Linewidth_A

      || _la == VnmrPKParser::FWHM_A)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
    }
    setState(87);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Label) {
      setState(86);
      match(VnmrPKParser::Label);
    }
    setState(90);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Comment) {
      setState(89);
      match(VnmrPKParser::Comment);
    }
    setState(92);
    match(VnmrPKParser::RETURN_FO);
    setState(108);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 19, _ctx)) {
    case 1: {
      setState(94); 
      _errHandler->sync(this);
      alt = 1;
      do {
        switch (alt) {
          case 1: {
                setState(93);
                peak_ll2d();
                break;
              }

        default:
          throw NoViableAltException(this);
        }
        setState(96); 
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 16, _ctx);
      } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
      break;
    }

    case 2: {
      setState(99); 
      _errHandler->sync(this);
      alt = 1;
      do {
        switch (alt) {
          case 1: {
                setState(98);
                peak_ll3d();
                break;
              }

        default:
          throw NoViableAltException(this);
        }
        setState(101); 
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx);
      } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
      break;
    }

    case 3: {
      setState(104); 
      _errHandler->sync(this);
      alt = 1;
      do {
        switch (alt) {
          case 1: {
                setState(103);
                peak_ll4d();
                break;
              }

        default:
          throw NoViableAltException(this);
        }
        setState(106); 
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx);
      } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
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

//----------------- Peak_ll2dContext ------------------------------------------------------------------

VnmrPKParser::Peak_ll2dContext::Peak_ll2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* VnmrPKParser::Peak_ll2dContext::Integer() {
  return getToken(VnmrPKParser::Integer, 0);
}

std::vector<tree::TerminalNode *> VnmrPKParser::Peak_ll2dContext::Float() {
  return getTokens(VnmrPKParser::Float);
}

tree::TerminalNode* VnmrPKParser::Peak_ll2dContext::Float(size_t i) {
  return getToken(VnmrPKParser::Float, i);
}

std::vector<VnmrPKParser::NumberContext *> VnmrPKParser::Peak_ll2dContext::number() {
  return getRuleContexts<VnmrPKParser::NumberContext>();
}

VnmrPKParser::NumberContext* VnmrPKParser::Peak_ll2dContext::number(size_t i) {
  return getRuleContext<VnmrPKParser::NumberContext>(i);
}

tree::TerminalNode* VnmrPKParser::Peak_ll2dContext::RETURN() {
  return getToken(VnmrPKParser::RETURN, 0);
}

tree::TerminalNode* VnmrPKParser::Peak_ll2dContext::EOF() {
  return getToken(VnmrPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> VnmrPKParser::Peak_ll2dContext::Double_quote_string() {
  return getTokens(VnmrPKParser::Double_quote_string);
}

tree::TerminalNode* VnmrPKParser::Peak_ll2dContext::Double_quote_string(size_t i) {
  return getToken(VnmrPKParser::Double_quote_string, i);
}


size_t VnmrPKParser::Peak_ll2dContext::getRuleIndex() const {
  return VnmrPKParser::RulePeak_ll2d;
}


std::any VnmrPKParser::Peak_ll2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<VnmrPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_ll2d(this);
  else
    return visitor->visitChildren(this);
}

VnmrPKParser::Peak_ll2dContext* VnmrPKParser::peak_ll2d() {
  Peak_ll2dContext *_localctx = _tracker.createInstance<Peak_ll2dContext>(_ctx, getState());
  enterRule(_localctx, 6, VnmrPKParser::RulePeak_ll2d);
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
    match(VnmrPKParser::Integer);
    setState(111);
    match(VnmrPKParser::Float);
    setState(112);
    match(VnmrPKParser::Float);
    setState(113);
    number();
    setState(115);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 20, _ctx)) {
    case 1: {
      setState(114);
      number();
      break;
    }

    default:
      break;
    }
    setState(118);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 21, _ctx)) {
    case 1: {
      setState(117);
      number();
      break;
    }

    default:
      break;
    }
    setState(121);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 56) != 0)) {
      setState(120);
      number();
    }
    setState(126);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == VnmrPKParser::Double_quote_string) {
      setState(123);
      match(VnmrPKParser::Double_quote_string);
      setState(128);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(129);
    _la = _input->LA(1);
    if (!(_la == VnmrPKParser::EOF

    || _la == VnmrPKParser::RETURN)) {
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

//----------------- Peak_ll3dContext ------------------------------------------------------------------

VnmrPKParser::Peak_ll3dContext::Peak_ll3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* VnmrPKParser::Peak_ll3dContext::Integer() {
  return getToken(VnmrPKParser::Integer, 0);
}

std::vector<tree::TerminalNode *> VnmrPKParser::Peak_ll3dContext::Float() {
  return getTokens(VnmrPKParser::Float);
}

tree::TerminalNode* VnmrPKParser::Peak_ll3dContext::Float(size_t i) {
  return getToken(VnmrPKParser::Float, i);
}

std::vector<VnmrPKParser::NumberContext *> VnmrPKParser::Peak_ll3dContext::number() {
  return getRuleContexts<VnmrPKParser::NumberContext>();
}

VnmrPKParser::NumberContext* VnmrPKParser::Peak_ll3dContext::number(size_t i) {
  return getRuleContext<VnmrPKParser::NumberContext>(i);
}

tree::TerminalNode* VnmrPKParser::Peak_ll3dContext::RETURN() {
  return getToken(VnmrPKParser::RETURN, 0);
}

tree::TerminalNode* VnmrPKParser::Peak_ll3dContext::EOF() {
  return getToken(VnmrPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> VnmrPKParser::Peak_ll3dContext::Double_quote_string() {
  return getTokens(VnmrPKParser::Double_quote_string);
}

tree::TerminalNode* VnmrPKParser::Peak_ll3dContext::Double_quote_string(size_t i) {
  return getToken(VnmrPKParser::Double_quote_string, i);
}


size_t VnmrPKParser::Peak_ll3dContext::getRuleIndex() const {
  return VnmrPKParser::RulePeak_ll3d;
}


std::any VnmrPKParser::Peak_ll3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<VnmrPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_ll3d(this);
  else
    return visitor->visitChildren(this);
}

VnmrPKParser::Peak_ll3dContext* VnmrPKParser::peak_ll3d() {
  Peak_ll3dContext *_localctx = _tracker.createInstance<Peak_ll3dContext>(_ctx, getState());
  enterRule(_localctx, 8, VnmrPKParser::RulePeak_ll3d);
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
    setState(131);
    match(VnmrPKParser::Integer);
    setState(132);
    match(VnmrPKParser::Float);
    setState(133);
    match(VnmrPKParser::Float);
    setState(134);
    match(VnmrPKParser::Float);
    setState(135);
    number();
    setState(137);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 24, _ctx)) {
    case 1: {
      setState(136);
      number();
      break;
    }

    default:
      break;
    }
    setState(140);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 25, _ctx)) {
    case 1: {
      setState(139);
      number();
      break;
    }

    default:
      break;
    }
    setState(143);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 26, _ctx)) {
    case 1: {
      setState(142);
      number();
      break;
    }

    default:
      break;
    }
    setState(146);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 56) != 0)) {
      setState(145);
      number();
    }
    setState(151);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == VnmrPKParser::Double_quote_string) {
      setState(148);
      match(VnmrPKParser::Double_quote_string);
      setState(153);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(154);
    _la = _input->LA(1);
    if (!(_la == VnmrPKParser::EOF

    || _la == VnmrPKParser::RETURN)) {
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

//----------------- Peak_ll4dContext ------------------------------------------------------------------

VnmrPKParser::Peak_ll4dContext::Peak_ll4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* VnmrPKParser::Peak_ll4dContext::Integer() {
  return getToken(VnmrPKParser::Integer, 0);
}

std::vector<tree::TerminalNode *> VnmrPKParser::Peak_ll4dContext::Float() {
  return getTokens(VnmrPKParser::Float);
}

tree::TerminalNode* VnmrPKParser::Peak_ll4dContext::Float(size_t i) {
  return getToken(VnmrPKParser::Float, i);
}

std::vector<VnmrPKParser::NumberContext *> VnmrPKParser::Peak_ll4dContext::number() {
  return getRuleContexts<VnmrPKParser::NumberContext>();
}

VnmrPKParser::NumberContext* VnmrPKParser::Peak_ll4dContext::number(size_t i) {
  return getRuleContext<VnmrPKParser::NumberContext>(i);
}

tree::TerminalNode* VnmrPKParser::Peak_ll4dContext::RETURN() {
  return getToken(VnmrPKParser::RETURN, 0);
}

tree::TerminalNode* VnmrPKParser::Peak_ll4dContext::EOF() {
  return getToken(VnmrPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> VnmrPKParser::Peak_ll4dContext::Double_quote_string() {
  return getTokens(VnmrPKParser::Double_quote_string);
}

tree::TerminalNode* VnmrPKParser::Peak_ll4dContext::Double_quote_string(size_t i) {
  return getToken(VnmrPKParser::Double_quote_string, i);
}


size_t VnmrPKParser::Peak_ll4dContext::getRuleIndex() const {
  return VnmrPKParser::RulePeak_ll4d;
}


std::any VnmrPKParser::Peak_ll4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<VnmrPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_ll4d(this);
  else
    return visitor->visitChildren(this);
}

VnmrPKParser::Peak_ll4dContext* VnmrPKParser::peak_ll4d() {
  Peak_ll4dContext *_localctx = _tracker.createInstance<Peak_ll4dContext>(_ctx, getState());
  enterRule(_localctx, 10, VnmrPKParser::RulePeak_ll4d);
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
    match(VnmrPKParser::Integer);
    setState(157);
    match(VnmrPKParser::Float);
    setState(158);
    match(VnmrPKParser::Float);
    setState(159);
    match(VnmrPKParser::Float);
    setState(160);
    match(VnmrPKParser::Float);
    setState(161);
    number();
    setState(163);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 29, _ctx)) {
    case 1: {
      setState(162);
      number();
      break;
    }

    default:
      break;
    }
    setState(166);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 30, _ctx)) {
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

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 31, _ctx)) {
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

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 32, _ctx)) {
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

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 56) != 0)) {
      setState(174);
      number();
    }
    setState(180);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == VnmrPKParser::Double_quote_string) {
      setState(177);
      match(VnmrPKParser::Double_quote_string);
      setState(182);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(183);
    _la = _input->LA(1);
    if (!(_la == VnmrPKParser::EOF

    || _la == VnmrPKParser::RETURN)) {
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

//----------------- Data_labelContext ------------------------------------------------------------------

VnmrPKParser::Data_labelContext::Data_labelContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::Peak_id() {
  return getToken(VnmrPKParser::Peak_id, 0);
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::Dim_0_ppm() {
  return getToken(VnmrPKParser::Dim_0_ppm, 0);
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::Dev_0() {
  return getToken(VnmrPKParser::Dev_0, 0);
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::Dim_1_ppm() {
  return getToken(VnmrPKParser::Dim_1_ppm, 0);
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::Dev_1() {
  return getToken(VnmrPKParser::Dev_1, 0);
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::Amplitude_LA() {
  return getToken(VnmrPKParser::Amplitude_LA, 0);
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::RETURN_LA() {
  return getToken(VnmrPKParser::RETURN_LA, 0);
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::Dim_2_ppm() {
  return getToken(VnmrPKParser::Dim_2_ppm, 0);
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::Dev_2() {
  return getToken(VnmrPKParser::Dev_2, 0);
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::Volume_LA() {
  return getToken(VnmrPKParser::Volume_LA, 0);
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::Assignment() {
  return getToken(VnmrPKParser::Assignment, 0);
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::Dim_3_ppm() {
  return getToken(VnmrPKParser::Dim_3_ppm, 0);
}

tree::TerminalNode* VnmrPKParser::Data_labelContext::Dev_3() {
  return getToken(VnmrPKParser::Dev_3, 0);
}


size_t VnmrPKParser::Data_labelContext::getRuleIndex() const {
  return VnmrPKParser::RuleData_label;
}


std::any VnmrPKParser::Data_labelContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<VnmrPKParserVisitor*>(visitor))
    return parserVisitor->visitData_label(this);
  else
    return visitor->visitChildren(this);
}

VnmrPKParser::Data_labelContext* VnmrPKParser::data_label() {
  Data_labelContext *_localctx = _tracker.createInstance<Data_labelContext>(_ctx, getState());
  enterRule(_localctx, 12, VnmrPKParser::RuleData_label);
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
    match(VnmrPKParser::Peak_id);
    setState(186);
    match(VnmrPKParser::Dim_0_ppm);
    setState(187);
    match(VnmrPKParser::Dev_0);
    setState(188);
    match(VnmrPKParser::Dim_1_ppm);
    setState(189);
    match(VnmrPKParser::Dev_1);
    setState(196);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Dim_2_ppm) {
      setState(190);
      match(VnmrPKParser::Dim_2_ppm);
      setState(191);
      match(VnmrPKParser::Dev_2);
      setState(194);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == VnmrPKParser::Dim_3_ppm) {
        setState(192);
        match(VnmrPKParser::Dim_3_ppm);
        setState(193);
        match(VnmrPKParser::Dev_3);
      }
    }
    setState(198);
    match(VnmrPKParser::Amplitude_LA);
    setState(200);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Volume_LA) {
      setState(199);
      match(VnmrPKParser::Volume_LA);
    }
    setState(203);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Assignment) {
      setState(202);
      match(VnmrPKParser::Assignment);
    }
    setState(205);
    match(VnmrPKParser::RETURN_LA);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_2dContext ------------------------------------------------------------------

VnmrPKParser::Peak_2dContext::Peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* VnmrPKParser::Peak_2dContext::Integer() {
  return getToken(VnmrPKParser::Integer, 0);
}

std::vector<tree::TerminalNode *> VnmrPKParser::Peak_2dContext::Float() {
  return getTokens(VnmrPKParser::Float);
}

tree::TerminalNode* VnmrPKParser::Peak_2dContext::Float(size_t i) {
  return getToken(VnmrPKParser::Float, i);
}

VnmrPKParser::NumberContext* VnmrPKParser::Peak_2dContext::number() {
  return getRuleContext<VnmrPKParser::NumberContext>(0);
}

tree::TerminalNode* VnmrPKParser::Peak_2dContext::RETURN() {
  return getToken(VnmrPKParser::RETURN, 0);
}

tree::TerminalNode* VnmrPKParser::Peak_2dContext::EOF() {
  return getToken(VnmrPKParser::EOF, 0);
}

tree::TerminalNode* VnmrPKParser::Peak_2dContext::Assignment_2d_ex() {
  return getToken(VnmrPKParser::Assignment_2d_ex, 0);
}


size_t VnmrPKParser::Peak_2dContext::getRuleIndex() const {
  return VnmrPKParser::RulePeak_2d;
}


std::any VnmrPKParser::Peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<VnmrPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d(this);
  else
    return visitor->visitChildren(this);
}

VnmrPKParser::Peak_2dContext* VnmrPKParser::peak_2d() {
  Peak_2dContext *_localctx = _tracker.createInstance<Peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 14, VnmrPKParser::RulePeak_2d);
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
    setState(207);
    match(VnmrPKParser::Integer);
    setState(208);
    match(VnmrPKParser::Float);
    setState(209);
    match(VnmrPKParser::Float);
    setState(210);
    match(VnmrPKParser::Float);
    setState(211);
    match(VnmrPKParser::Float);
    setState(212);
    number();
    setState(214);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Assignment_2d_ex) {
      setState(213);
      match(VnmrPKParser::Assignment_2d_ex);
    }
    setState(216);
    _la = _input->LA(1);
    if (!(_la == VnmrPKParser::EOF

    || _la == VnmrPKParser::RETURN)) {
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

//----------------- Peak_3dContext ------------------------------------------------------------------

VnmrPKParser::Peak_3dContext::Peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* VnmrPKParser::Peak_3dContext::Integer() {
  return getToken(VnmrPKParser::Integer, 0);
}

std::vector<tree::TerminalNode *> VnmrPKParser::Peak_3dContext::Float() {
  return getTokens(VnmrPKParser::Float);
}

tree::TerminalNode* VnmrPKParser::Peak_3dContext::Float(size_t i) {
  return getToken(VnmrPKParser::Float, i);
}

VnmrPKParser::NumberContext* VnmrPKParser::Peak_3dContext::number() {
  return getRuleContext<VnmrPKParser::NumberContext>(0);
}

tree::TerminalNode* VnmrPKParser::Peak_3dContext::RETURN() {
  return getToken(VnmrPKParser::RETURN, 0);
}

tree::TerminalNode* VnmrPKParser::Peak_3dContext::EOF() {
  return getToken(VnmrPKParser::EOF, 0);
}

tree::TerminalNode* VnmrPKParser::Peak_3dContext::Assignment_3d_ex() {
  return getToken(VnmrPKParser::Assignment_3d_ex, 0);
}


size_t VnmrPKParser::Peak_3dContext::getRuleIndex() const {
  return VnmrPKParser::RulePeak_3d;
}


std::any VnmrPKParser::Peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<VnmrPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d(this);
  else
    return visitor->visitChildren(this);
}

VnmrPKParser::Peak_3dContext* VnmrPKParser::peak_3d() {
  Peak_3dContext *_localctx = _tracker.createInstance<Peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 16, VnmrPKParser::RulePeak_3d);
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
    setState(218);
    match(VnmrPKParser::Integer);
    setState(219);
    match(VnmrPKParser::Float);
    setState(220);
    match(VnmrPKParser::Float);
    setState(221);
    match(VnmrPKParser::Float);
    setState(222);
    match(VnmrPKParser::Float);
    setState(223);
    match(VnmrPKParser::Float);
    setState(224);
    match(VnmrPKParser::Float);
    setState(225);
    number();
    setState(227);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Assignment_3d_ex) {
      setState(226);
      match(VnmrPKParser::Assignment_3d_ex);
    }
    setState(229);
    _la = _input->LA(1);
    if (!(_la == VnmrPKParser::EOF

    || _la == VnmrPKParser::RETURN)) {
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

//----------------- Peak_4dContext ------------------------------------------------------------------

VnmrPKParser::Peak_4dContext::Peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* VnmrPKParser::Peak_4dContext::Integer() {
  return getToken(VnmrPKParser::Integer, 0);
}

std::vector<tree::TerminalNode *> VnmrPKParser::Peak_4dContext::Float() {
  return getTokens(VnmrPKParser::Float);
}

tree::TerminalNode* VnmrPKParser::Peak_4dContext::Float(size_t i) {
  return getToken(VnmrPKParser::Float, i);
}

VnmrPKParser::NumberContext* VnmrPKParser::Peak_4dContext::number() {
  return getRuleContext<VnmrPKParser::NumberContext>(0);
}

tree::TerminalNode* VnmrPKParser::Peak_4dContext::RETURN() {
  return getToken(VnmrPKParser::RETURN, 0);
}

tree::TerminalNode* VnmrPKParser::Peak_4dContext::EOF() {
  return getToken(VnmrPKParser::EOF, 0);
}

tree::TerminalNode* VnmrPKParser::Peak_4dContext::Assignment_4d_ex() {
  return getToken(VnmrPKParser::Assignment_4d_ex, 0);
}


size_t VnmrPKParser::Peak_4dContext::getRuleIndex() const {
  return VnmrPKParser::RulePeak_4d;
}


std::any VnmrPKParser::Peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<VnmrPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d(this);
  else
    return visitor->visitChildren(this);
}

VnmrPKParser::Peak_4dContext* VnmrPKParser::peak_4d() {
  Peak_4dContext *_localctx = _tracker.createInstance<Peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 18, VnmrPKParser::RulePeak_4d);
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
    setState(231);
    match(VnmrPKParser::Integer);
    setState(232);
    match(VnmrPKParser::Float);
    setState(233);
    match(VnmrPKParser::Float);
    setState(234);
    match(VnmrPKParser::Float);
    setState(235);
    match(VnmrPKParser::Float);
    setState(236);
    match(VnmrPKParser::Float);
    setState(237);
    match(VnmrPKParser::Float);
    setState(238);
    match(VnmrPKParser::Float);
    setState(239);
    match(VnmrPKParser::Float);
    setState(240);
    number();
    setState(242);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == VnmrPKParser::Assignment_4d_ex) {
      setState(241);
      match(VnmrPKParser::Assignment_4d_ex);
    }
    setState(244);
    _la = _input->LA(1);
    if (!(_la == VnmrPKParser::EOF

    || _la == VnmrPKParser::RETURN)) {
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

VnmrPKParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* VnmrPKParser::NumberContext::Real() {
  return getToken(VnmrPKParser::Real, 0);
}

tree::TerminalNode* VnmrPKParser::NumberContext::Float() {
  return getToken(VnmrPKParser::Float, 0);
}

tree::TerminalNode* VnmrPKParser::NumberContext::Integer() {
  return getToken(VnmrPKParser::Integer, 0);
}


size_t VnmrPKParser::NumberContext::getRuleIndex() const {
  return VnmrPKParser::RuleNumber;
}


std::any VnmrPKParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<VnmrPKParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

VnmrPKParser::NumberContext* VnmrPKParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 20, VnmrPKParser::RuleNumber);
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
    setState(246);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 56) != 0))) {
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

void VnmrPKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  vnmrpkparserParserInitialize();
#else
  ::antlr4::internal::call_once(vnmrpkparserParserOnceFlag, vnmrpkparserParserInitialize);
#endif
}
