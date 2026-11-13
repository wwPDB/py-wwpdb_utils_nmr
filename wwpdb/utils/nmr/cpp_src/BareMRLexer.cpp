
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BareMRLexer.g4 by ANTLR 4.13.2


#include "BareMRLexer.h"


using namespace antlr4;



using namespace antlr4;

namespace {

struct BareMRLexerStaticData final {
  BareMRLexerStaticData(std::vector<std::string> ruleNames,
                          std::vector<std::string> channelNames,
                          std::vector<std::string> modeNames,
                          std::vector<std::string> literalNames,
                          std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), channelNames(std::move(channelNames)),
        modeNames(std::move(modeNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  BareMRLexerStaticData(const BareMRLexerStaticData&) = delete;
  BareMRLexerStaticData(BareMRLexerStaticData&&) = delete;
  BareMRLexerStaticData& operator=(const BareMRLexerStaticData&) = delete;
  BareMRLexerStaticData& operator=(BareMRLexerStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> channelNames;
  const std::vector<std::string> modeNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag baremrlexerLexerOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<BareMRLexerStaticData> baremrlexerLexerStaticData = nullptr;

void baremrlexerLexerInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (baremrlexerLexerStaticData != nullptr) {
    return;
  }
#else
  assert(baremrlexerLexerStaticData == nullptr);
#endif
  auto staticData = std::make_unique<BareMRLexerStaticData>(
    std::vector<std::string>{
      "Data_block", "Integer", "Float", "DEC_DOT_DEC", "DEC_DIGIT", "DECIMAL", 
      "SHARP_COMMENT", "EXCLM_COMMENT", "Number_of_name", "Simple_name", 
      "ALPHA", "ALPHA_NUM", "START_CHAR", "NAME_CHAR", "SIMPLE_NAME", "Double_quote_string", 
      "Double_quote_integer", "Double_quote_float", "SPACE", "RETURN", "COMMENT_START_CHAR", 
      "SECTION_COMMENT", "LINE_COMMENT"
    },
    std::vector<std::string>{
      "DEFAULT_TOKEN_CHANNEL", "HIDDEN"
    },
    std::vector<std::string>{
      "DEFAULT_MODE"
    },
    std::vector<std::string>{
    },
    std::vector<std::string>{
      "", "Data_block", "Integer", "Float", "SHARP_COMMENT", "EXCLM_COMMENT", 
      "Number_of_name", "Simple_name", "Double_quote_string", "Double_quote_integer", 
      "Double_quote_float", "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,0,14,276,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
  	6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,
  	7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,
  	7,21,2,22,7,22,1,0,1,0,1,0,1,0,1,0,1,0,1,0,4,0,55,8,0,11,0,12,0,56,1,
  	1,3,1,60,8,1,1,1,1,1,1,2,3,2,65,8,2,1,2,1,2,3,2,69,8,2,1,3,1,3,1,3,3,
  	3,74,8,3,1,3,1,3,3,3,78,8,3,1,4,1,4,1,5,4,5,83,8,5,11,5,12,5,84,1,6,4,
  	6,88,8,6,11,6,12,6,89,1,6,1,6,5,6,94,8,6,10,6,12,6,97,9,6,1,6,5,6,100,
  	8,6,10,6,12,6,103,9,6,1,6,5,6,106,8,6,10,6,12,6,109,9,6,1,6,1,6,1,7,4,
  	7,114,8,7,11,7,12,7,115,1,7,5,7,119,8,7,10,7,12,7,122,9,7,1,7,5,7,125,
  	8,7,10,7,12,7,128,9,7,1,7,5,7,131,8,7,10,7,12,7,134,9,7,1,7,1,7,1,8,1,
  	8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,3,11,149,8,11,1,12,1,12,3,12,
  	153,8,12,1,13,1,13,3,13,157,8,13,1,14,1,14,5,14,161,8,14,10,14,12,14,
  	164,9,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,
  	1,18,4,18,179,8,18,11,18,12,18,180,1,18,1,18,1,19,4,19,186,8,19,11,19,
  	12,19,187,1,20,1,20,1,20,3,20,193,8,20,1,21,1,21,1,21,4,21,198,8,21,11,
  	21,12,21,199,1,21,1,21,4,21,204,8,21,11,21,12,21,205,1,21,1,21,4,21,210,
  	8,21,11,21,12,21,211,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,222,
  	8,21,3,21,224,8,21,1,21,5,21,227,8,21,10,21,12,21,230,9,21,1,21,1,21,
  	1,21,1,21,1,22,1,22,1,22,4,22,239,8,22,11,22,12,22,240,1,22,1,22,4,22,
  	245,8,22,11,22,12,22,246,1,22,1,22,4,22,251,8,22,11,22,12,22,252,1,22,
  	1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,263,8,22,3,22,265,8,22,1,22,5,
  	22,268,8,22,10,22,12,22,271,9,22,1,22,1,22,1,22,1,22,0,0,23,1,1,3,2,5,
  	3,7,0,9,0,11,0,13,4,15,5,17,6,19,7,21,0,23,0,25,0,27,0,29,0,31,8,33,9,
  	35,10,37,11,39,12,41,0,43,13,45,14,1,0,9,2,0,10,10,13,13,2,0,43,43,45,
  	45,1,0,48,57,1,0,95,95,2,0,65,90,97,122,6,0,40,40,42,43,45,46,63,63,95,
  	95,123,123,7,0,34,35,37,37,39,39,41,41,47,47,59,59,124,125,3,0,9,9,32,
  	32,44,44,6,0,33,33,36,36,38,38,47,47,61,61,92,92,306,0,1,1,0,0,0,0,3,
  	1,0,0,0,0,5,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
  	0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,
  	43,1,0,0,0,0,45,1,0,0,0,1,47,1,0,0,0,3,59,1,0,0,0,5,64,1,0,0,0,7,77,1,
  	0,0,0,9,79,1,0,0,0,11,82,1,0,0,0,13,87,1,0,0,0,15,113,1,0,0,0,17,137,
  	1,0,0,0,19,142,1,0,0,0,21,144,1,0,0,0,23,148,1,0,0,0,25,152,1,0,0,0,27,
  	156,1,0,0,0,29,158,1,0,0,0,31,165,1,0,0,0,33,169,1,0,0,0,35,173,1,0,0,
  	0,37,178,1,0,0,0,39,185,1,0,0,0,41,192,1,0,0,0,43,223,1,0,0,0,45,264,
  	1,0,0,0,47,48,5,100,0,0,48,49,5,97,0,0,49,50,5,116,0,0,50,51,5,97,0,0,
  	51,52,5,95,0,0,52,54,1,0,0,0,53,55,8,0,0,0,54,53,1,0,0,0,55,56,1,0,0,
  	0,56,54,1,0,0,0,56,57,1,0,0,0,57,2,1,0,0,0,58,60,7,1,0,0,59,58,1,0,0,
  	0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,3,11,5,0,62,4,1,0,0,0,63,65,7,1,0,
  	0,64,63,1,0,0,0,64,65,1,0,0,0,65,68,1,0,0,0,66,69,3,11,5,0,67,69,3,7,
  	3,0,68,66,1,0,0,0,68,67,1,0,0,0,69,6,1,0,0,0,70,71,3,11,5,0,71,73,5,46,
  	0,0,72,74,3,11,5,0,73,72,1,0,0,0,73,74,1,0,0,0,74,78,1,0,0,0,75,76,5,
  	46,0,0,76,78,3,11,5,0,77,70,1,0,0,0,77,75,1,0,0,0,78,8,1,0,0,0,79,80,
  	7,2,0,0,80,10,1,0,0,0,81,83,3,9,4,0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,
  	1,0,0,0,84,85,1,0,0,0,85,12,1,0,0,0,86,88,5,35,0,0,87,86,1,0,0,0,88,89,
  	1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,95,8,3,0,0,92,94,
  	8,0,0,0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,101,
  	1,0,0,0,97,95,1,0,0,0,98,100,5,35,0,0,99,98,1,0,0,0,100,103,1,0,0,0,101,
  	99,1,0,0,0,101,102,1,0,0,0,102,107,1,0,0,0,103,101,1,0,0,0,104,106,8,
  	0,0,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,
  	108,110,1,0,0,0,109,107,1,0,0,0,110,111,6,6,0,0,111,14,1,0,0,0,112,114,
  	5,33,0,0,113,112,1,0,0,0,114,115,1,0,0,0,115,113,1,0,0,0,115,116,1,0,
  	0,0,116,120,1,0,0,0,117,119,8,0,0,0,118,117,1,0,0,0,119,122,1,0,0,0,120,
  	118,1,0,0,0,120,121,1,0,0,0,121,126,1,0,0,0,122,120,1,0,0,0,123,125,5,
  	33,0,0,124,123,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,
  	0,127,132,1,0,0,0,128,126,1,0,0,0,129,131,8,0,0,0,130,129,1,0,0,0,131,
  	134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,135,1,0,0,0,134,132,1,
  	0,0,0,135,136,6,7,0,0,136,16,1,0,0,0,137,138,5,35,0,0,138,139,5,95,0,
  	0,139,140,1,0,0,0,140,141,3,29,14,0,141,18,1,0,0,0,142,143,3,29,14,0,
  	143,20,1,0,0,0,144,145,7,4,0,0,145,22,1,0,0,0,146,149,3,21,10,0,147,149,
  	3,9,4,0,148,146,1,0,0,0,148,147,1,0,0,0,149,24,1,0,0,0,150,153,3,23,11,
  	0,151,153,7,5,0,0,152,150,1,0,0,0,152,151,1,0,0,0,153,26,1,0,0,0,154,
  	157,3,25,12,0,155,157,7,6,0,0,156,154,1,0,0,0,156,155,1,0,0,0,157,28,
  	1,0,0,0,158,162,3,25,12,0,159,161,3,27,13,0,160,159,1,0,0,0,161,164,1,
  	0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,30,1,0,0,0,164,162,1,0,0,0,
  	165,166,5,34,0,0,166,167,3,29,14,0,167,168,5,34,0,0,168,32,1,0,0,0,169,
  	170,5,34,0,0,170,171,3,3,1,0,171,172,5,34,0,0,172,34,1,0,0,0,173,174,
  	5,34,0,0,174,175,3,5,2,0,175,176,5,34,0,0,176,36,1,0,0,0,177,179,7,7,
  	0,0,178,177,1,0,0,0,179,180,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,
  	182,1,0,0,0,182,183,6,18,1,0,183,38,1,0,0,0,184,186,7,0,0,0,185,184,1,
  	0,0,0,186,187,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,40,1,0,0,0,
  	189,190,5,35,0,0,190,193,8,3,0,0,191,193,7,8,0,0,192,189,1,0,0,0,192,
  	191,1,0,0,0,193,42,1,0,0,0,194,224,3,41,20,0,195,197,3,41,20,0,196,198,
  	5,47,0,0,197,196,1,0,0,0,198,199,1,0,0,0,199,197,1,0,0,0,199,200,1,0,
  	0,0,200,224,1,0,0,0,201,203,3,41,20,0,202,204,5,42,0,0,203,202,1,0,0,
  	0,204,205,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,224,1,0,0,0,207,
  	209,3,41,20,0,208,210,5,61,0,0,209,208,1,0,0,0,210,211,1,0,0,0,211,209,
  	1,0,0,0,211,212,1,0,0,0,212,224,1,0,0,0,213,214,5,82,0,0,214,215,5,69,
  	0,0,215,216,5,77,0,0,216,217,5,65,0,0,217,218,5,82,0,0,218,219,5,75,0,
  	0,219,221,1,0,0,0,220,222,5,83,0,0,221,220,1,0,0,0,221,222,1,0,0,0,222,
  	224,1,0,0,0,223,194,1,0,0,0,223,195,1,0,0,0,223,201,1,0,0,0,223,207,1,
  	0,0,0,223,213,1,0,0,0,224,228,1,0,0,0,225,227,5,32,0,0,226,225,1,0,0,
  	0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,231,1,0,0,0,230,
  	228,1,0,0,0,231,232,3,39,19,0,232,233,1,0,0,0,233,234,6,21,0,0,234,44,
  	1,0,0,0,235,265,3,41,20,0,236,238,3,41,20,0,237,239,5,47,0,0,238,237,
  	1,0,0,0,239,240,1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,0,241,265,1,0,0,
  	0,242,244,3,41,20,0,243,245,5,42,0,0,244,243,1,0,0,0,245,246,1,0,0,0,
  	246,244,1,0,0,0,246,247,1,0,0,0,247,265,1,0,0,0,248,250,3,41,20,0,249,
  	251,5,61,0,0,250,249,1,0,0,0,251,252,1,0,0,0,252,250,1,0,0,0,252,253,
  	1,0,0,0,253,265,1,0,0,0,254,255,5,82,0,0,255,256,5,69,0,0,256,257,5,77,
  	0,0,257,258,5,65,0,0,258,259,5,82,0,0,259,260,5,75,0,0,260,262,1,0,0,
  	0,261,263,5,83,0,0,262,261,1,0,0,0,262,263,1,0,0,0,263,265,1,0,0,0,264,
  	235,1,0,0,0,264,236,1,0,0,0,264,242,1,0,0,0,264,248,1,0,0,0,264,254,1,
  	0,0,0,265,269,1,0,0,0,266,268,8,0,0,0,267,266,1,0,0,0,268,271,1,0,0,0,
  	269,267,1,0,0,0,269,270,1,0,0,0,270,272,1,0,0,0,271,269,1,0,0,0,272,273,
  	3,39,19,0,273,274,1,0,0,0,274,275,6,22,0,0,275,46,1,0,0,0,35,0,56,59,
  	64,68,73,77,84,89,95,101,107,115,120,126,132,148,152,156,162,180,187,
  	192,199,205,211,221,223,228,240,246,252,262,264,269,2,0,1,0,6,0,0
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  baremrlexerLexerStaticData = std::move(staticData);
}

}

BareMRLexer::BareMRLexer(CharStream *input) : Lexer(input) {
  BareMRLexer::initialize();
  _interpreter = new atn::LexerATNSimulator(this, *baremrlexerLexerStaticData->atn, baremrlexerLexerStaticData->decisionToDFA, baremrlexerLexerStaticData->sharedContextCache);
}

BareMRLexer::~BareMRLexer() {
  delete _interpreter;
}

std::string BareMRLexer::getGrammarFileName() const {
  return "BareMRLexer.g4";
}

const std::vector<std::string>& BareMRLexer::getRuleNames() const {
  return baremrlexerLexerStaticData->ruleNames;
}

const std::vector<std::string>& BareMRLexer::getChannelNames() const {
  return baremrlexerLexerStaticData->channelNames;
}

const std::vector<std::string>& BareMRLexer::getModeNames() const {
  return baremrlexerLexerStaticData->modeNames;
}

const dfa::Vocabulary& BareMRLexer::getVocabulary() const {
  return baremrlexerLexerStaticData->vocabulary;
}

antlr4::atn::SerializedATNView BareMRLexer::getSerializedATN() const {
  return baremrlexerLexerStaticData->serializedATN;
}

const atn::ATN& BareMRLexer::getATN() const {
  return *baremrlexerLexerStaticData->atn;
}




void BareMRLexer::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  baremrlexerLexerInitialize();
#else
  ::antlr4::internal::call_once(baremrlexerLexerOnceFlag, baremrlexerLexerInitialize);
#endif
}
