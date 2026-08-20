
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PonderosaPKParser.g4 by ANTLR 4.13.2


#include "PonderosaPKParserVisitor.h"

#include "PonderosaPKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct PonderosaPKParserStaticData final {
  PonderosaPKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  PonderosaPKParserStaticData(const PonderosaPKParserStaticData&) = delete;
  PonderosaPKParserStaticData(PonderosaPKParserStaticData&&) = delete;
  PonderosaPKParserStaticData& operator=(const PonderosaPKParserStaticData&) = delete;
  PonderosaPKParserStaticData& operator=(PonderosaPKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag ponderosapkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<PonderosaPKParserStaticData> ponderosapkparserParserStaticData = nullptr;

void ponderosapkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (ponderosapkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(ponderosapkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<PonderosaPKParserStaticData>(
    std::vector<std::string>{
      "ponderosa_pk", "peak_list_2d", "peak_2d", "peak_list_3d", "peak_3d", 
      "peak_list_4d", "peak_4d", "number"
    },
    std::vector<std::string>{
      "", "'NOESYTYPE'", "'AXISORDER'"
    },
    std::vector<std::string>{
      "", "Noesy_type", "Axis_order", "Integer", "Float", "Real", "SHARP_COMMENT", 
      "EXCLM_COMMENT", "SMCLN_COMMENT", "Simple_name", "SPACE", "RETURN", 
      "SECTION_COMMENT", "LINE_COMMENT", "Integer_NT", "Simple_name_NT", 
      "SPACE_NT", "RETURN_NT", "Integer_AO", "Simple_name_AO", "SPACE_AO", 
      "RETURN_AO"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,21,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,7,
  	7,7,1,0,3,0,18,8,0,1,0,1,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,9,0,1,0,1,
  	0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,40,8,1,11,1,12,1,41,1,2,1,2,
  	1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,4,3,60,8,3,11,
  	3,12,3,61,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
  	1,5,1,5,1,5,4,5,82,8,5,11,5,12,5,83,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
  	6,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,1,1,11,11,1,0,4,5,
  	98,0,17,1,0,0,0,2,30,1,0,0,0,4,43,1,0,0,0,6,50,1,0,0,0,8,63,1,0,0,0,10,
  	72,1,0,0,0,12,85,1,0,0,0,14,96,1,0,0,0,16,18,5,11,0,0,17,16,1,0,0,0,17,
  	18,1,0,0,0,18,25,1,0,0,0,19,24,3,2,1,0,20,24,3,6,3,0,21,24,3,10,5,0,22,
  	24,5,11,0,0,23,19,1,0,0,0,23,20,1,0,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,
  	27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,
  	29,5,0,0,1,29,1,1,0,0,0,30,31,5,1,0,0,31,32,5,14,0,0,32,33,5,15,0,0,33,
  	34,5,17,0,0,34,35,5,2,0,0,35,36,5,18,0,0,36,37,5,19,0,0,37,39,5,21,0,
  	0,38,40,3,4,2,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,
  	0,42,3,1,0,0,0,43,44,5,4,0,0,44,45,5,4,0,0,45,46,3,14,7,0,46,47,5,9,0,
  	0,47,48,5,9,0,0,48,49,7,0,0,0,49,5,1,0,0,0,50,51,5,1,0,0,51,52,5,14,0,
  	0,52,53,5,15,0,0,53,54,5,17,0,0,54,55,5,2,0,0,55,56,5,18,0,0,56,57,5,
  	19,0,0,57,59,5,21,0,0,58,60,3,8,4,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,
  	1,0,0,0,61,62,1,0,0,0,62,7,1,0,0,0,63,64,5,4,0,0,64,65,5,4,0,0,65,66,
  	5,4,0,0,66,67,3,14,7,0,67,68,5,9,0,0,68,69,5,9,0,0,69,70,5,9,0,0,70,71,
  	7,0,0,0,71,9,1,0,0,0,72,73,5,1,0,0,73,74,5,14,0,0,74,75,5,15,0,0,75,76,
  	5,17,0,0,76,77,5,2,0,0,77,78,5,18,0,0,78,79,5,19,0,0,79,81,5,21,0,0,80,
  	82,3,12,6,0,81,80,1,0,0,0,82,83,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,
  	11,1,0,0,0,85,86,5,4,0,0,86,87,5,4,0,0,87,88,5,4,0,0,88,89,5,4,0,0,89,
  	90,3,14,7,0,90,91,5,9,0,0,91,92,5,9,0,0,92,93,5,9,0,0,93,94,5,9,0,0,94,
  	95,7,0,0,0,95,13,1,0,0,0,96,97,7,1,0,0,97,15,1,0,0,0,6,17,23,25,41,61,
  	83
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  ponderosapkparserParserStaticData = std::move(staticData);
}

}

PonderosaPKParser::PonderosaPKParser(TokenStream *input) : PonderosaPKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

PonderosaPKParser::PonderosaPKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  PonderosaPKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *ponderosapkparserParserStaticData->atn, ponderosapkparserParserStaticData->decisionToDFA, ponderosapkparserParserStaticData->sharedContextCache, options);
}

PonderosaPKParser::~PonderosaPKParser() {
  delete _interpreter;
}

const atn::ATN& PonderosaPKParser::getATN() const {
  return *ponderosapkparserParserStaticData->atn;
}

std::string PonderosaPKParser::getGrammarFileName() const {
  return "PonderosaPKParser.g4";
}

const std::vector<std::string>& PonderosaPKParser::getRuleNames() const {
  return ponderosapkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& PonderosaPKParser::getVocabulary() const {
  return ponderosapkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView PonderosaPKParser::getSerializedATN() const {
  return ponderosapkparserParserStaticData->serializedATN;
}


//----------------- Ponderosa_pkContext ------------------------------------------------------------------

PonderosaPKParser::Ponderosa_pkContext::Ponderosa_pkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PonderosaPKParser::Ponderosa_pkContext::EOF() {
  return getToken(PonderosaPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> PonderosaPKParser::Ponderosa_pkContext::RETURN() {
  return getTokens(PonderosaPKParser::RETURN);
}

tree::TerminalNode* PonderosaPKParser::Ponderosa_pkContext::RETURN(size_t i) {
  return getToken(PonderosaPKParser::RETURN, i);
}

std::vector<PonderosaPKParser::Peak_list_2dContext *> PonderosaPKParser::Ponderosa_pkContext::peak_list_2d() {
  return getRuleContexts<PonderosaPKParser::Peak_list_2dContext>();
}

PonderosaPKParser::Peak_list_2dContext* PonderosaPKParser::Ponderosa_pkContext::peak_list_2d(size_t i) {
  return getRuleContext<PonderosaPKParser::Peak_list_2dContext>(i);
}

std::vector<PonderosaPKParser::Peak_list_3dContext *> PonderosaPKParser::Ponderosa_pkContext::peak_list_3d() {
  return getRuleContexts<PonderosaPKParser::Peak_list_3dContext>();
}

PonderosaPKParser::Peak_list_3dContext* PonderosaPKParser::Ponderosa_pkContext::peak_list_3d(size_t i) {
  return getRuleContext<PonderosaPKParser::Peak_list_3dContext>(i);
}

std::vector<PonderosaPKParser::Peak_list_4dContext *> PonderosaPKParser::Ponderosa_pkContext::peak_list_4d() {
  return getRuleContexts<PonderosaPKParser::Peak_list_4dContext>();
}

PonderosaPKParser::Peak_list_4dContext* PonderosaPKParser::Ponderosa_pkContext::peak_list_4d(size_t i) {
  return getRuleContext<PonderosaPKParser::Peak_list_4dContext>(i);
}


size_t PonderosaPKParser::Ponderosa_pkContext::getRuleIndex() const {
  return PonderosaPKParser::RulePonderosa_pk;
}


std::any PonderosaPKParser::Ponderosa_pkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PonderosaPKParserVisitor*>(visitor))
    return parserVisitor->visitPonderosa_pk(this);
  else
    return visitor->visitChildren(this);
}

PonderosaPKParser::Ponderosa_pkContext* PonderosaPKParser::ponderosa_pk() {
  Ponderosa_pkContext *_localctx = _tracker.createInstance<Ponderosa_pkContext>(_ctx, getState());
  enterRule(_localctx, 0, PonderosaPKParser::RulePonderosa_pk);
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
    setState(17);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(16);
      match(PonderosaPKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(25);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == PonderosaPKParser::Noesy_type

    || _la == PonderosaPKParser::RETURN) {
      setState(23);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(19);
        peak_list_2d();
        break;
      }

      case 2: {
        setState(20);
        peak_list_3d();
        break;
      }

      case 3: {
        setState(21);
        peak_list_4d();
        break;
      }

      case 4: {
        setState(22);
        match(PonderosaPKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(27);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(28);
    match(PonderosaPKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_list_2dContext ------------------------------------------------------------------

PonderosaPKParser::Peak_list_2dContext::Peak_list_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PonderosaPKParser::Peak_list_2dContext::Noesy_type() {
  return getToken(PonderosaPKParser::Noesy_type, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_2dContext::Integer_NT() {
  return getToken(PonderosaPKParser::Integer_NT, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_2dContext::Simple_name_NT() {
  return getToken(PonderosaPKParser::Simple_name_NT, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_2dContext::RETURN_NT() {
  return getToken(PonderosaPKParser::RETURN_NT, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_2dContext::Axis_order() {
  return getToken(PonderosaPKParser::Axis_order, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_2dContext::Integer_AO() {
  return getToken(PonderosaPKParser::Integer_AO, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_2dContext::Simple_name_AO() {
  return getToken(PonderosaPKParser::Simple_name_AO, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_2dContext::RETURN_AO() {
  return getToken(PonderosaPKParser::RETURN_AO, 0);
}

std::vector<PonderosaPKParser::Peak_2dContext *> PonderosaPKParser::Peak_list_2dContext::peak_2d() {
  return getRuleContexts<PonderosaPKParser::Peak_2dContext>();
}

PonderosaPKParser::Peak_2dContext* PonderosaPKParser::Peak_list_2dContext::peak_2d(size_t i) {
  return getRuleContext<PonderosaPKParser::Peak_2dContext>(i);
}


size_t PonderosaPKParser::Peak_list_2dContext::getRuleIndex() const {
  return PonderosaPKParser::RulePeak_list_2d;
}


std::any PonderosaPKParser::Peak_list_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PonderosaPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_2d(this);
  else
    return visitor->visitChildren(this);
}

PonderosaPKParser::Peak_list_2dContext* PonderosaPKParser::peak_list_2d() {
  Peak_list_2dContext *_localctx = _tracker.createInstance<Peak_list_2dContext>(_ctx, getState());
  enterRule(_localctx, 2, PonderosaPKParser::RulePeak_list_2d);
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
    setState(30);
    match(PonderosaPKParser::Noesy_type);
    setState(31);
    match(PonderosaPKParser::Integer_NT);
    setState(32);
    match(PonderosaPKParser::Simple_name_NT);
    setState(33);
    match(PonderosaPKParser::RETURN_NT);
    setState(34);
    match(PonderosaPKParser::Axis_order);
    setState(35);
    match(PonderosaPKParser::Integer_AO);
    setState(36);
    match(PonderosaPKParser::Simple_name_AO);
    setState(37);
    match(PonderosaPKParser::RETURN_AO);
    setState(39); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(38);
      peak_2d();
      setState(41); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == PonderosaPKParser::Float);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_2dContext ------------------------------------------------------------------

PonderosaPKParser::Peak_2dContext::Peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> PonderosaPKParser::Peak_2dContext::Float() {
  return getTokens(PonderosaPKParser::Float);
}

tree::TerminalNode* PonderosaPKParser::Peak_2dContext::Float(size_t i) {
  return getToken(PonderosaPKParser::Float, i);
}

PonderosaPKParser::NumberContext* PonderosaPKParser::Peak_2dContext::number() {
  return getRuleContext<PonderosaPKParser::NumberContext>(0);
}

std::vector<tree::TerminalNode *> PonderosaPKParser::Peak_2dContext::Simple_name() {
  return getTokens(PonderosaPKParser::Simple_name);
}

tree::TerminalNode* PonderosaPKParser::Peak_2dContext::Simple_name(size_t i) {
  return getToken(PonderosaPKParser::Simple_name, i);
}

tree::TerminalNode* PonderosaPKParser::Peak_2dContext::RETURN() {
  return getToken(PonderosaPKParser::RETURN, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_2dContext::EOF() {
  return getToken(PonderosaPKParser::EOF, 0);
}


size_t PonderosaPKParser::Peak_2dContext::getRuleIndex() const {
  return PonderosaPKParser::RulePeak_2d;
}


std::any PonderosaPKParser::Peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PonderosaPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d(this);
  else
    return visitor->visitChildren(this);
}

PonderosaPKParser::Peak_2dContext* PonderosaPKParser::peak_2d() {
  Peak_2dContext *_localctx = _tracker.createInstance<Peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 4, PonderosaPKParser::RulePeak_2d);
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
    setState(43);
    match(PonderosaPKParser::Float);
    setState(44);
    match(PonderosaPKParser::Float);
    setState(45);
    number();
    setState(46);
    match(PonderosaPKParser::Simple_name);
    setState(47);
    match(PonderosaPKParser::Simple_name);
    setState(48);
    _la = _input->LA(1);
    if (!(_la == PonderosaPKParser::EOF

    || _la == PonderosaPKParser::RETURN)) {
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

PonderosaPKParser::Peak_list_3dContext::Peak_list_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PonderosaPKParser::Peak_list_3dContext::Noesy_type() {
  return getToken(PonderosaPKParser::Noesy_type, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_3dContext::Integer_NT() {
  return getToken(PonderosaPKParser::Integer_NT, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_3dContext::Simple_name_NT() {
  return getToken(PonderosaPKParser::Simple_name_NT, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_3dContext::RETURN_NT() {
  return getToken(PonderosaPKParser::RETURN_NT, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_3dContext::Axis_order() {
  return getToken(PonderosaPKParser::Axis_order, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_3dContext::Integer_AO() {
  return getToken(PonderosaPKParser::Integer_AO, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_3dContext::Simple_name_AO() {
  return getToken(PonderosaPKParser::Simple_name_AO, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_3dContext::RETURN_AO() {
  return getToken(PonderosaPKParser::RETURN_AO, 0);
}

std::vector<PonderosaPKParser::Peak_3dContext *> PonderosaPKParser::Peak_list_3dContext::peak_3d() {
  return getRuleContexts<PonderosaPKParser::Peak_3dContext>();
}

PonderosaPKParser::Peak_3dContext* PonderosaPKParser::Peak_list_3dContext::peak_3d(size_t i) {
  return getRuleContext<PonderosaPKParser::Peak_3dContext>(i);
}


size_t PonderosaPKParser::Peak_list_3dContext::getRuleIndex() const {
  return PonderosaPKParser::RulePeak_list_3d;
}


std::any PonderosaPKParser::Peak_list_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PonderosaPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_3d(this);
  else
    return visitor->visitChildren(this);
}

PonderosaPKParser::Peak_list_3dContext* PonderosaPKParser::peak_list_3d() {
  Peak_list_3dContext *_localctx = _tracker.createInstance<Peak_list_3dContext>(_ctx, getState());
  enterRule(_localctx, 6, PonderosaPKParser::RulePeak_list_3d);
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
    match(PonderosaPKParser::Noesy_type);
    setState(51);
    match(PonderosaPKParser::Integer_NT);
    setState(52);
    match(PonderosaPKParser::Simple_name_NT);
    setState(53);
    match(PonderosaPKParser::RETURN_NT);
    setState(54);
    match(PonderosaPKParser::Axis_order);
    setState(55);
    match(PonderosaPKParser::Integer_AO);
    setState(56);
    match(PonderosaPKParser::Simple_name_AO);
    setState(57);
    match(PonderosaPKParser::RETURN_AO);
    setState(59); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(58);
      peak_3d();
      setState(61); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == PonderosaPKParser::Float);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_3dContext ------------------------------------------------------------------

PonderosaPKParser::Peak_3dContext::Peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> PonderosaPKParser::Peak_3dContext::Float() {
  return getTokens(PonderosaPKParser::Float);
}

tree::TerminalNode* PonderosaPKParser::Peak_3dContext::Float(size_t i) {
  return getToken(PonderosaPKParser::Float, i);
}

PonderosaPKParser::NumberContext* PonderosaPKParser::Peak_3dContext::number() {
  return getRuleContext<PonderosaPKParser::NumberContext>(0);
}

std::vector<tree::TerminalNode *> PonderosaPKParser::Peak_3dContext::Simple_name() {
  return getTokens(PonderosaPKParser::Simple_name);
}

tree::TerminalNode* PonderosaPKParser::Peak_3dContext::Simple_name(size_t i) {
  return getToken(PonderosaPKParser::Simple_name, i);
}

tree::TerminalNode* PonderosaPKParser::Peak_3dContext::RETURN() {
  return getToken(PonderosaPKParser::RETURN, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_3dContext::EOF() {
  return getToken(PonderosaPKParser::EOF, 0);
}


size_t PonderosaPKParser::Peak_3dContext::getRuleIndex() const {
  return PonderosaPKParser::RulePeak_3d;
}


std::any PonderosaPKParser::Peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PonderosaPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d(this);
  else
    return visitor->visitChildren(this);
}

PonderosaPKParser::Peak_3dContext* PonderosaPKParser::peak_3d() {
  Peak_3dContext *_localctx = _tracker.createInstance<Peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 8, PonderosaPKParser::RulePeak_3d);
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
    setState(63);
    match(PonderosaPKParser::Float);
    setState(64);
    match(PonderosaPKParser::Float);
    setState(65);
    match(PonderosaPKParser::Float);
    setState(66);
    number();
    setState(67);
    match(PonderosaPKParser::Simple_name);
    setState(68);
    match(PonderosaPKParser::Simple_name);
    setState(69);
    match(PonderosaPKParser::Simple_name);
    setState(70);
    _la = _input->LA(1);
    if (!(_la == PonderosaPKParser::EOF

    || _la == PonderosaPKParser::RETURN)) {
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

PonderosaPKParser::Peak_list_4dContext::Peak_list_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PonderosaPKParser::Peak_list_4dContext::Noesy_type() {
  return getToken(PonderosaPKParser::Noesy_type, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_4dContext::Integer_NT() {
  return getToken(PonderosaPKParser::Integer_NT, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_4dContext::Simple_name_NT() {
  return getToken(PonderosaPKParser::Simple_name_NT, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_4dContext::RETURN_NT() {
  return getToken(PonderosaPKParser::RETURN_NT, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_4dContext::Axis_order() {
  return getToken(PonderosaPKParser::Axis_order, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_4dContext::Integer_AO() {
  return getToken(PonderosaPKParser::Integer_AO, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_4dContext::Simple_name_AO() {
  return getToken(PonderosaPKParser::Simple_name_AO, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_list_4dContext::RETURN_AO() {
  return getToken(PonderosaPKParser::RETURN_AO, 0);
}

std::vector<PonderosaPKParser::Peak_4dContext *> PonderosaPKParser::Peak_list_4dContext::peak_4d() {
  return getRuleContexts<PonderosaPKParser::Peak_4dContext>();
}

PonderosaPKParser::Peak_4dContext* PonderosaPKParser::Peak_list_4dContext::peak_4d(size_t i) {
  return getRuleContext<PonderosaPKParser::Peak_4dContext>(i);
}


size_t PonderosaPKParser::Peak_list_4dContext::getRuleIndex() const {
  return PonderosaPKParser::RulePeak_list_4d;
}


std::any PonderosaPKParser::Peak_list_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PonderosaPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_4d(this);
  else
    return visitor->visitChildren(this);
}

PonderosaPKParser::Peak_list_4dContext* PonderosaPKParser::peak_list_4d() {
  Peak_list_4dContext *_localctx = _tracker.createInstance<Peak_list_4dContext>(_ctx, getState());
  enterRule(_localctx, 10, PonderosaPKParser::RulePeak_list_4d);
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
    match(PonderosaPKParser::Noesy_type);
    setState(73);
    match(PonderosaPKParser::Integer_NT);
    setState(74);
    match(PonderosaPKParser::Simple_name_NT);
    setState(75);
    match(PonderosaPKParser::RETURN_NT);
    setState(76);
    match(PonderosaPKParser::Axis_order);
    setState(77);
    match(PonderosaPKParser::Integer_AO);
    setState(78);
    match(PonderosaPKParser::Simple_name_AO);
    setState(79);
    match(PonderosaPKParser::RETURN_AO);
    setState(81); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(80);
      peak_4d();
      setState(83); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == PonderosaPKParser::Float);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_4dContext ------------------------------------------------------------------

PonderosaPKParser::Peak_4dContext::Peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> PonderosaPKParser::Peak_4dContext::Float() {
  return getTokens(PonderosaPKParser::Float);
}

tree::TerminalNode* PonderosaPKParser::Peak_4dContext::Float(size_t i) {
  return getToken(PonderosaPKParser::Float, i);
}

PonderosaPKParser::NumberContext* PonderosaPKParser::Peak_4dContext::number() {
  return getRuleContext<PonderosaPKParser::NumberContext>(0);
}

std::vector<tree::TerminalNode *> PonderosaPKParser::Peak_4dContext::Simple_name() {
  return getTokens(PonderosaPKParser::Simple_name);
}

tree::TerminalNode* PonderosaPKParser::Peak_4dContext::Simple_name(size_t i) {
  return getToken(PonderosaPKParser::Simple_name, i);
}

tree::TerminalNode* PonderosaPKParser::Peak_4dContext::RETURN() {
  return getToken(PonderosaPKParser::RETURN, 0);
}

tree::TerminalNode* PonderosaPKParser::Peak_4dContext::EOF() {
  return getToken(PonderosaPKParser::EOF, 0);
}


size_t PonderosaPKParser::Peak_4dContext::getRuleIndex() const {
  return PonderosaPKParser::RulePeak_4d;
}


std::any PonderosaPKParser::Peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PonderosaPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d(this);
  else
    return visitor->visitChildren(this);
}

PonderosaPKParser::Peak_4dContext* PonderosaPKParser::peak_4d() {
  Peak_4dContext *_localctx = _tracker.createInstance<Peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 12, PonderosaPKParser::RulePeak_4d);
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
    setState(85);
    match(PonderosaPKParser::Float);
    setState(86);
    match(PonderosaPKParser::Float);
    setState(87);
    match(PonderosaPKParser::Float);
    setState(88);
    match(PonderosaPKParser::Float);
    setState(89);
    number();
    setState(90);
    match(PonderosaPKParser::Simple_name);
    setState(91);
    match(PonderosaPKParser::Simple_name);
    setState(92);
    match(PonderosaPKParser::Simple_name);
    setState(93);
    match(PonderosaPKParser::Simple_name);
    setState(94);
    _la = _input->LA(1);
    if (!(_la == PonderosaPKParser::EOF

    || _la == PonderosaPKParser::RETURN)) {
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

PonderosaPKParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PonderosaPKParser::NumberContext::Float() {
  return getToken(PonderosaPKParser::Float, 0);
}

tree::TerminalNode* PonderosaPKParser::NumberContext::Real() {
  return getToken(PonderosaPKParser::Real, 0);
}


size_t PonderosaPKParser::NumberContext::getRuleIndex() const {
  return PonderosaPKParser::RuleNumber;
}


std::any PonderosaPKParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PonderosaPKParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

PonderosaPKParser::NumberContext* PonderosaPKParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 14, PonderosaPKParser::RuleNumber);
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
    _la = _input->LA(1);
    if (!(_la == PonderosaPKParser::Float

    || _la == PonderosaPKParser::Real)) {
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

void PonderosaPKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  ponderosapkparserParserInitialize();
#else
  ::antlr4::internal::call_once(ponderosapkparserParserOnceFlag, ponderosapkparserParserInitialize);
#endif
}
