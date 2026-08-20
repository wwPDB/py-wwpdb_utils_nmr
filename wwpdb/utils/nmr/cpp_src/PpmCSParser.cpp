
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PpmCSParser.g4 by ANTLR 4.13.2


#include "PpmCSParserVisitor.h"

#include "PpmCSParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct PpmCSParserStaticData final {
  PpmCSParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  PpmCSParserStaticData(const PpmCSParserStaticData&) = delete;
  PpmCSParserStaticData(PpmCSParserStaticData&&) = delete;
  PpmCSParserStaticData& operator=(const PpmCSParserStaticData&) = delete;
  PpmCSParserStaticData& operator=(PpmCSParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag ppmcsparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<PpmCSParserStaticData> ppmcsparserParserStaticData = nullptr;

void ppmcsparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (ppmcsparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(ppmcsparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<PpmCSParserStaticData>(
    std::vector<std::string>{
      "ppm_cs", "ppm_list", "number"
    },
    std::vector<std::string>{
    },
    std::vector<std::string>{
      "", "Integer", "Float", "SHARP_COMMENT", "EXCLM_COMMENT", "Atom_selection_2d_ex", 
      "Atom_selection_3d_ex", "Simple_name", "SPACE", "RETURN", "SECTION_COMMENT", 
      "LINE_COMMENT"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,11,33,2,0,7,0,2,1,7,1,2,2,7,2,1,0,3,0,8,8,0,1,0,4,0,11,8,0,11,0,12,
  	0,12,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,3,1,26,8,1,1,
  	1,3,1,29,8,1,1,2,1,2,1,2,0,0,3,0,2,4,0,3,1,0,5,7,1,1,9,9,2,0,1,2,7,7,
  	34,0,7,1,0,0,0,2,22,1,0,0,0,4,30,1,0,0,0,6,8,5,9,0,0,7,6,1,0,0,0,7,8,
  	1,0,0,0,8,10,1,0,0,0,9,11,3,2,1,0,10,9,1,0,0,0,11,12,1,0,0,0,12,10,1,
  	0,0,0,12,13,1,0,0,0,13,17,1,0,0,0,14,16,5,9,0,0,15,14,1,0,0,0,16,19,1,
  	0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,
  	0,0,1,21,1,1,0,0,0,22,23,7,0,0,0,23,25,3,4,2,0,24,26,5,1,0,0,25,24,1,
  	0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,29,7,1,0,0,28,27,1,0,0,0,28,29,1,
  	0,0,0,29,3,1,0,0,0,30,31,7,2,0,0,31,5,1,0,0,0,5,7,12,17,25,28
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  ppmcsparserParserStaticData = std::move(staticData);
}

}

PpmCSParser::PpmCSParser(TokenStream *input) : PpmCSParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

PpmCSParser::PpmCSParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  PpmCSParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *ppmcsparserParserStaticData->atn, ppmcsparserParserStaticData->decisionToDFA, ppmcsparserParserStaticData->sharedContextCache, options);
}

PpmCSParser::~PpmCSParser() {
  delete _interpreter;
}

const atn::ATN& PpmCSParser::getATN() const {
  return *ppmcsparserParserStaticData->atn;
}

std::string PpmCSParser::getGrammarFileName() const {
  return "PpmCSParser.g4";
}

const std::vector<std::string>& PpmCSParser::getRuleNames() const {
  return ppmcsparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& PpmCSParser::getVocabulary() const {
  return ppmcsparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView PpmCSParser::getSerializedATN() const {
  return ppmcsparserParserStaticData->serializedATN;
}


//----------------- Ppm_csContext ------------------------------------------------------------------

PpmCSParser::Ppm_csContext::Ppm_csContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PpmCSParser::Ppm_csContext::EOF() {
  return getToken(PpmCSParser::EOF, 0);
}

std::vector<tree::TerminalNode *> PpmCSParser::Ppm_csContext::RETURN() {
  return getTokens(PpmCSParser::RETURN);
}

tree::TerminalNode* PpmCSParser::Ppm_csContext::RETURN(size_t i) {
  return getToken(PpmCSParser::RETURN, i);
}

std::vector<PpmCSParser::Ppm_listContext *> PpmCSParser::Ppm_csContext::ppm_list() {
  return getRuleContexts<PpmCSParser::Ppm_listContext>();
}

PpmCSParser::Ppm_listContext* PpmCSParser::Ppm_csContext::ppm_list(size_t i) {
  return getRuleContext<PpmCSParser::Ppm_listContext>(i);
}


size_t PpmCSParser::Ppm_csContext::getRuleIndex() const {
  return PpmCSParser::RulePpm_cs;
}


std::any PpmCSParser::Ppm_csContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PpmCSParserVisitor*>(visitor))
    return parserVisitor->visitPpm_cs(this);
  else
    return visitor->visitChildren(this);
}

PpmCSParser::Ppm_csContext* PpmCSParser::ppm_cs() {
  Ppm_csContext *_localctx = _tracker.createInstance<Ppm_csContext>(_ctx, getState());
  enterRule(_localctx, 0, PpmCSParser::RulePpm_cs);
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
    setState(7);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PpmCSParser::RETURN) {
      setState(6);
      match(PpmCSParser::RETURN);
    }
    setState(10); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(9);
      ppm_list();
      setState(12); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 224) != 0));
    setState(17);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == PpmCSParser::RETURN) {
      setState(14);
      match(PpmCSParser::RETURN);
      setState(19);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(20);
    match(PpmCSParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ppm_listContext ------------------------------------------------------------------

PpmCSParser::Ppm_listContext::Ppm_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PpmCSParser::NumberContext* PpmCSParser::Ppm_listContext::number() {
  return getRuleContext<PpmCSParser::NumberContext>(0);
}

tree::TerminalNode* PpmCSParser::Ppm_listContext::Simple_name() {
  return getToken(PpmCSParser::Simple_name, 0);
}

tree::TerminalNode* PpmCSParser::Ppm_listContext::Atom_selection_2d_ex() {
  return getToken(PpmCSParser::Atom_selection_2d_ex, 0);
}

tree::TerminalNode* PpmCSParser::Ppm_listContext::Atom_selection_3d_ex() {
  return getToken(PpmCSParser::Atom_selection_3d_ex, 0);
}

tree::TerminalNode* PpmCSParser::Ppm_listContext::Integer() {
  return getToken(PpmCSParser::Integer, 0);
}

tree::TerminalNode* PpmCSParser::Ppm_listContext::RETURN() {
  return getToken(PpmCSParser::RETURN, 0);
}

tree::TerminalNode* PpmCSParser::Ppm_listContext::EOF() {
  return getToken(PpmCSParser::EOF, 0);
}


size_t PpmCSParser::Ppm_listContext::getRuleIndex() const {
  return PpmCSParser::RulePpm_list;
}


std::any PpmCSParser::Ppm_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PpmCSParserVisitor*>(visitor))
    return parserVisitor->visitPpm_list(this);
  else
    return visitor->visitChildren(this);
}

PpmCSParser::Ppm_listContext* PpmCSParser::ppm_list() {
  Ppm_listContext *_localctx = _tracker.createInstance<Ppm_listContext>(_ctx, getState());
  enterRule(_localctx, 2, PpmCSParser::RulePpm_list);
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
    setState(22);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 224) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(23);
    number();
    setState(25);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PpmCSParser::Integer) {
      setState(24);
      match(PpmCSParser::Integer);
    }
    setState(28);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx)) {
    case 1: {
      setState(27);
      _la = _input->LA(1);
      if (!(_la == PpmCSParser::EOF

      || _la == PpmCSParser::RETURN)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
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

//----------------- NumberContext ------------------------------------------------------------------

PpmCSParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PpmCSParser::NumberContext::Float() {
  return getToken(PpmCSParser::Float, 0);
}

tree::TerminalNode* PpmCSParser::NumberContext::Integer() {
  return getToken(PpmCSParser::Integer, 0);
}

tree::TerminalNode* PpmCSParser::NumberContext::Simple_name() {
  return getToken(PpmCSParser::Simple_name, 0);
}


size_t PpmCSParser::NumberContext::getRuleIndex() const {
  return PpmCSParser::RuleNumber;
}


std::any PpmCSParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PpmCSParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

PpmCSParser::NumberContext* PpmCSParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 4, PpmCSParser::RuleNumber);
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
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 134) != 0))) {
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

void PpmCSParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  ppmcsparserParserInitialize();
#else
  ::antlr4::internal::call_once(ppmcsparserParserOnceFlag, ppmcsparserParserInitialize);
#endif
}
