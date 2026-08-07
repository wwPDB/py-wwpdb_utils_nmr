
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GarretCSParser.g4 by ANTLR 4.13.0


#include "GarretCSParserVisitor.h"

#include "GarretCSParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct GarretCSParserStaticData final {
  GarretCSParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  GarretCSParserStaticData(const GarretCSParserStaticData&) = delete;
  GarretCSParserStaticData(GarretCSParserStaticData&&) = delete;
  GarretCSParserStaticData& operator=(const GarretCSParserStaticData&) = delete;
  GarretCSParserStaticData& operator=(GarretCSParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag garretcsparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
GarretCSParserStaticData *garretcsparserParserStaticData = nullptr;

void garretcsparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (garretcsparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(garretcsparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<GarretCSParserStaticData>(
    std::vector<std::string>{
      "garret_cs", "residue_list", "shift_list", "number"
    },
    std::vector<std::string>{
    },
    std::vector<std::string>{
      "", "Integer", "Float", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
      "Simple_name", "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,10,42,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,3,0,10,8,0,1,0,4,0,13,8,
  	0,11,0,12,0,14,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,1,
  	1,4,1,29,8,1,11,1,12,1,30,1,1,1,1,1,2,1,2,1,2,3,2,38,8,2,1,3,1,3,1,3,
  	0,0,4,0,2,4,6,0,1,2,0,1,2,6,6,42,0,9,1,0,0,0,2,24,1,0,0,0,4,34,1,0,0,
  	0,6,39,1,0,0,0,8,10,5,8,0,0,9,8,1,0,0,0,9,10,1,0,0,0,10,12,1,0,0,0,11,
  	13,3,2,1,0,12,11,1,0,0,0,13,14,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,
  	19,1,0,0,0,16,18,5,8,0,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,
  	20,1,0,0,0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,
  	25,5,1,0,0,25,26,5,6,0,0,26,28,5,8,0,0,27,29,3,4,2,0,28,27,1,0,0,0,29,
  	30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,33,5,5,0,0,33,
  	3,1,0,0,0,34,35,5,6,0,0,35,37,3,6,3,0,36,38,5,8,0,0,37,36,1,0,0,0,37,
  	38,1,0,0,0,38,5,1,0,0,0,39,40,7,0,0,0,40,7,1,0,0,0,5,9,14,19,30,37
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  garretcsparserParserStaticData = staticData.release();
}

}

GarretCSParser::GarretCSParser(TokenStream *input) : GarretCSParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

GarretCSParser::GarretCSParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  GarretCSParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *garretcsparserParserStaticData->atn, garretcsparserParserStaticData->decisionToDFA, garretcsparserParserStaticData->sharedContextCache, options);
}

GarretCSParser::~GarretCSParser() {
  delete _interpreter;
}

const atn::ATN& GarretCSParser::getATN() const {
  return *garretcsparserParserStaticData->atn;
}

std::string GarretCSParser::getGrammarFileName() const {
  return "GarretCSParser.g4";
}

const std::vector<std::string>& GarretCSParser::getRuleNames() const {
  return garretcsparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& GarretCSParser::getVocabulary() const {
  return garretcsparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView GarretCSParser::getSerializedATN() const {
  return garretcsparserParserStaticData->serializedATN;
}


//----------------- Garret_csContext ------------------------------------------------------------------

GarretCSParser::Garret_csContext::Garret_csContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GarretCSParser::Garret_csContext::EOF() {
  return getToken(GarretCSParser::EOF, 0);
}

std::vector<tree::TerminalNode *> GarretCSParser::Garret_csContext::RETURN() {
  return getTokens(GarretCSParser::RETURN);
}

tree::TerminalNode* GarretCSParser::Garret_csContext::RETURN(size_t i) {
  return getToken(GarretCSParser::RETURN, i);
}

std::vector<GarretCSParser::Residue_listContext *> GarretCSParser::Garret_csContext::residue_list() {
  return getRuleContexts<GarretCSParser::Residue_listContext>();
}

GarretCSParser::Residue_listContext* GarretCSParser::Garret_csContext::residue_list(size_t i) {
  return getRuleContext<GarretCSParser::Residue_listContext>(i);
}


size_t GarretCSParser::Garret_csContext::getRuleIndex() const {
  return GarretCSParser::RuleGarret_cs;
}


std::any GarretCSParser::Garret_csContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GarretCSParserVisitor*>(visitor))
    return parserVisitor->visitGarret_cs(this);
  else
    return visitor->visitChildren(this);
}

GarretCSParser::Garret_csContext* GarretCSParser::garret_cs() {
  Garret_csContext *_localctx = _tracker.createInstance<Garret_csContext>(_ctx, getState());
  enterRule(_localctx, 0, GarretCSParser::RuleGarret_cs);
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
    setState(9);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GarretCSParser::RETURN) {
      setState(8);
      match(GarretCSParser::RETURN);
    }
    setState(12); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(11);
      residue_list();
      setState(14); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GarretCSParser::Integer);
    setState(19);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GarretCSParser::RETURN) {
      setState(16);
      match(GarretCSParser::RETURN);
      setState(21);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(22);
    match(GarretCSParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Residue_listContext ------------------------------------------------------------------

GarretCSParser::Residue_listContext::Residue_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GarretCSParser::Residue_listContext::Integer() {
  return getToken(GarretCSParser::Integer, 0);
}

tree::TerminalNode* GarretCSParser::Residue_listContext::Simple_name() {
  return getToken(GarretCSParser::Simple_name, 0);
}

tree::TerminalNode* GarretCSParser::Residue_listContext::RETURN() {
  return getToken(GarretCSParser::RETURN, 0);
}

tree::TerminalNode* GarretCSParser::Residue_listContext::SMCLN_COMMENT() {
  return getToken(GarretCSParser::SMCLN_COMMENT, 0);
}

std::vector<GarretCSParser::Shift_listContext *> GarretCSParser::Residue_listContext::shift_list() {
  return getRuleContexts<GarretCSParser::Shift_listContext>();
}

GarretCSParser::Shift_listContext* GarretCSParser::Residue_listContext::shift_list(size_t i) {
  return getRuleContext<GarretCSParser::Shift_listContext>(i);
}


size_t GarretCSParser::Residue_listContext::getRuleIndex() const {
  return GarretCSParser::RuleResidue_list;
}


std::any GarretCSParser::Residue_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GarretCSParserVisitor*>(visitor))
    return parserVisitor->visitResidue_list(this);
  else
    return visitor->visitChildren(this);
}

GarretCSParser::Residue_listContext* GarretCSParser::residue_list() {
  Residue_listContext *_localctx = _tracker.createInstance<Residue_listContext>(_ctx, getState());
  enterRule(_localctx, 2, GarretCSParser::RuleResidue_list);
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
    setState(24);
    match(GarretCSParser::Integer);
    setState(25);
    match(GarretCSParser::Simple_name);
    setState(26);
    match(GarretCSParser::RETURN);
    setState(28); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(27);
      shift_list();
      setState(30); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GarretCSParser::Simple_name);
    setState(32);
    match(GarretCSParser::SMCLN_COMMENT);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Shift_listContext ------------------------------------------------------------------

GarretCSParser::Shift_listContext::Shift_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GarretCSParser::Shift_listContext::Simple_name() {
  return getToken(GarretCSParser::Simple_name, 0);
}

GarretCSParser::NumberContext* GarretCSParser::Shift_listContext::number() {
  return getRuleContext<GarretCSParser::NumberContext>(0);
}

tree::TerminalNode* GarretCSParser::Shift_listContext::RETURN() {
  return getToken(GarretCSParser::RETURN, 0);
}


size_t GarretCSParser::Shift_listContext::getRuleIndex() const {
  return GarretCSParser::RuleShift_list;
}


std::any GarretCSParser::Shift_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GarretCSParserVisitor*>(visitor))
    return parserVisitor->visitShift_list(this);
  else
    return visitor->visitChildren(this);
}

GarretCSParser::Shift_listContext* GarretCSParser::shift_list() {
  Shift_listContext *_localctx = _tracker.createInstance<Shift_listContext>(_ctx, getState());
  enterRule(_localctx, 4, GarretCSParser::RuleShift_list);
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
    setState(34);
    match(GarretCSParser::Simple_name);
    setState(35);
    number();
    setState(37);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GarretCSParser::RETURN) {
      setState(36);
      match(GarretCSParser::RETURN);
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

GarretCSParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GarretCSParser::NumberContext::Float() {
  return getToken(GarretCSParser::Float, 0);
}

tree::TerminalNode* GarretCSParser::NumberContext::Integer() {
  return getToken(GarretCSParser::Integer, 0);
}

tree::TerminalNode* GarretCSParser::NumberContext::Simple_name() {
  return getToken(GarretCSParser::Simple_name, 0);
}


size_t GarretCSParser::NumberContext::getRuleIndex() const {
  return GarretCSParser::RuleNumber;
}


std::any GarretCSParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GarretCSParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

GarretCSParser::NumberContext* GarretCSParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 6, GarretCSParser::RuleNumber);
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
    setState(39);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 70) != 0))) {
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

void GarretCSParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  garretcsparserParserInitialize();
#else
  ::antlr4::internal::call_once(garretcsparserParserOnceFlag, garretcsparserParserInitialize);
#endif
}
