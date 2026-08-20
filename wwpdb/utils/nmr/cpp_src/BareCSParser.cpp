
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BareCSParser.g4 by ANTLR 4.13.2


#include "BareCSParserVisitor.h"

#include "BareCSParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct BareCSParserStaticData final {
  BareCSParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  BareCSParserStaticData(const BareCSParserStaticData&) = delete;
  BareCSParserStaticData(BareCSParserStaticData&&) = delete;
  BareCSParserStaticData& operator=(const BareCSParserStaticData&) = delete;
  BareCSParserStaticData& operator=(BareCSParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag barecsparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<BareCSParserStaticData> barecsparserParserStaticData = nullptr;

void barecsparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (barecsparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(barecsparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<BareCSParserStaticData>(
    std::vector<std::string>{
      "bare_cs", "cs_row_format", "header", "cs_row_list", "any", "column_name"
    },
    std::vector<std::string>{
    },
    std::vector<std::string>{
      "", "Integer", "Float", "SHARP_COMMENT", "EXCLM_COMMENT", "Number_of_name", 
      "Simple_name", "Double_quote_string", "Double_quote_integer", "Double_quote_float", 
      "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,13,49,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,3,0,14,
  	8,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,4,1,27,8,1,11,
  	1,12,1,28,1,2,4,2,32,8,2,11,2,12,2,33,1,2,1,2,1,3,4,3,39,8,3,11,3,12,
  	3,40,1,3,1,3,1,4,1,4,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,3,1,1,11,11,2,0,
  	1,2,6,9,1,0,5,7,48,0,13,1,0,0,0,2,24,1,0,0,0,4,31,1,0,0,0,6,38,1,0,0,
  	0,8,44,1,0,0,0,10,46,1,0,0,0,12,14,5,11,0,0,13,12,1,0,0,0,13,14,1,0,0,
  	0,14,19,1,0,0,0,15,18,3,2,1,0,16,18,5,11,0,0,17,15,1,0,0,0,17,16,1,0,
  	0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,19,1,0,
  	0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,26,3,4,2,0,25,27,3,6,3,0,26,25,1,0,
  	0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,3,1,0,0,0,30,32,3,10,
  	5,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,35,1,0,
  	0,0,35,36,5,11,0,0,36,5,1,0,0,0,37,39,3,8,4,0,38,37,1,0,0,0,39,40,1,0,
  	0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,7,0,0,0,43,7,1,0,
  	0,0,44,45,7,1,0,0,45,9,1,0,0,0,46,47,7,2,0,0,47,11,1,0,0,0,6,13,17,19,
  	28,33,40
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  barecsparserParserStaticData = std::move(staticData);
}

}

BareCSParser::BareCSParser(TokenStream *input) : BareCSParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

BareCSParser::BareCSParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  BareCSParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *barecsparserParserStaticData->atn, barecsparserParserStaticData->decisionToDFA, barecsparserParserStaticData->sharedContextCache, options);
}

BareCSParser::~BareCSParser() {
  delete _interpreter;
}

const atn::ATN& BareCSParser::getATN() const {
  return *barecsparserParserStaticData->atn;
}

std::string BareCSParser::getGrammarFileName() const {
  return "BareCSParser.g4";
}

const std::vector<std::string>& BareCSParser::getRuleNames() const {
  return barecsparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& BareCSParser::getVocabulary() const {
  return barecsparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView BareCSParser::getSerializedATN() const {
  return barecsparserParserStaticData->serializedATN;
}


//----------------- Bare_csContext ------------------------------------------------------------------

BareCSParser::Bare_csContext::Bare_csContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BareCSParser::Bare_csContext::EOF() {
  return getToken(BareCSParser::EOF, 0);
}

std::vector<tree::TerminalNode *> BareCSParser::Bare_csContext::RETURN() {
  return getTokens(BareCSParser::RETURN);
}

tree::TerminalNode* BareCSParser::Bare_csContext::RETURN(size_t i) {
  return getToken(BareCSParser::RETURN, i);
}

std::vector<BareCSParser::Cs_row_formatContext *> BareCSParser::Bare_csContext::cs_row_format() {
  return getRuleContexts<BareCSParser::Cs_row_formatContext>();
}

BareCSParser::Cs_row_formatContext* BareCSParser::Bare_csContext::cs_row_format(size_t i) {
  return getRuleContext<BareCSParser::Cs_row_formatContext>(i);
}


size_t BareCSParser::Bare_csContext::getRuleIndex() const {
  return BareCSParser::RuleBare_cs;
}


std::any BareCSParser::Bare_csContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BareCSParserVisitor*>(visitor))
    return parserVisitor->visitBare_cs(this);
  else
    return visitor->visitChildren(this);
}

BareCSParser::Bare_csContext* BareCSParser::bare_cs() {
  Bare_csContext *_localctx = _tracker.createInstance<Bare_csContext>(_ctx, getState());
  enterRule(_localctx, 0, BareCSParser::RuleBare_cs);
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
    setState(13);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(12);
      match(BareCSParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(19);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2272) != 0)) {
      setState(17);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case BareCSParser::Number_of_name:
        case BareCSParser::Simple_name:
        case BareCSParser::Double_quote_string: {
          setState(15);
          cs_row_format();
          break;
        }

        case BareCSParser::RETURN: {
          setState(16);
          match(BareCSParser::RETURN);
          break;
        }

      default:
        throw NoViableAltException(this);
      }
      setState(21);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(22);
    match(BareCSParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Cs_row_formatContext ------------------------------------------------------------------

BareCSParser::Cs_row_formatContext::Cs_row_formatContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BareCSParser::HeaderContext* BareCSParser::Cs_row_formatContext::header() {
  return getRuleContext<BareCSParser::HeaderContext>(0);
}

std::vector<BareCSParser::Cs_row_listContext *> BareCSParser::Cs_row_formatContext::cs_row_list() {
  return getRuleContexts<BareCSParser::Cs_row_listContext>();
}

BareCSParser::Cs_row_listContext* BareCSParser::Cs_row_formatContext::cs_row_list(size_t i) {
  return getRuleContext<BareCSParser::Cs_row_listContext>(i);
}


size_t BareCSParser::Cs_row_formatContext::getRuleIndex() const {
  return BareCSParser::RuleCs_row_format;
}


std::any BareCSParser::Cs_row_formatContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BareCSParserVisitor*>(visitor))
    return parserVisitor->visitCs_row_format(this);
  else
    return visitor->visitChildren(this);
}

BareCSParser::Cs_row_formatContext* BareCSParser::cs_row_format() {
  Cs_row_formatContext *_localctx = _tracker.createInstance<Cs_row_formatContext>(_ctx, getState());
  enterRule(_localctx, 2, BareCSParser::RuleCs_row_format);

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
    setState(24);
    header();
    setState(26); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(25);
              cs_row_list();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(28); 
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

//----------------- HeaderContext ------------------------------------------------------------------

BareCSParser::HeaderContext::HeaderContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BareCSParser::HeaderContext::RETURN() {
  return getToken(BareCSParser::RETURN, 0);
}

std::vector<BareCSParser::Column_nameContext *> BareCSParser::HeaderContext::column_name() {
  return getRuleContexts<BareCSParser::Column_nameContext>();
}

BareCSParser::Column_nameContext* BareCSParser::HeaderContext::column_name(size_t i) {
  return getRuleContext<BareCSParser::Column_nameContext>(i);
}


size_t BareCSParser::HeaderContext::getRuleIndex() const {
  return BareCSParser::RuleHeader;
}


std::any BareCSParser::HeaderContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BareCSParserVisitor*>(visitor))
    return parserVisitor->visitHeader(this);
  else
    return visitor->visitChildren(this);
}

BareCSParser::HeaderContext* BareCSParser::header() {
  HeaderContext *_localctx = _tracker.createInstance<HeaderContext>(_ctx, getState());
  enterRule(_localctx, 4, BareCSParser::RuleHeader);
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
    setState(31); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(30);
      column_name();
      setState(33); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 224) != 0));
    setState(35);
    match(BareCSParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Cs_row_listContext ------------------------------------------------------------------

BareCSParser::Cs_row_listContext::Cs_row_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BareCSParser::Cs_row_listContext::RETURN() {
  return getToken(BareCSParser::RETURN, 0);
}

tree::TerminalNode* BareCSParser::Cs_row_listContext::EOF() {
  return getToken(BareCSParser::EOF, 0);
}

std::vector<BareCSParser::AnyContext *> BareCSParser::Cs_row_listContext::any() {
  return getRuleContexts<BareCSParser::AnyContext>();
}

BareCSParser::AnyContext* BareCSParser::Cs_row_listContext::any(size_t i) {
  return getRuleContext<BareCSParser::AnyContext>(i);
}


size_t BareCSParser::Cs_row_listContext::getRuleIndex() const {
  return BareCSParser::RuleCs_row_list;
}


std::any BareCSParser::Cs_row_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BareCSParserVisitor*>(visitor))
    return parserVisitor->visitCs_row_list(this);
  else
    return visitor->visitChildren(this);
}

BareCSParser::Cs_row_listContext* BareCSParser::cs_row_list() {
  Cs_row_listContext *_localctx = _tracker.createInstance<Cs_row_listContext>(_ctx, getState());
  enterRule(_localctx, 6, BareCSParser::RuleCs_row_list);
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
    setState(38); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(37);
      any();
      setState(40); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 966) != 0));
    setState(42);
    _la = _input->LA(1);
    if (!(_la == BareCSParser::EOF

    || _la == BareCSParser::RETURN)) {
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

//----------------- AnyContext ------------------------------------------------------------------

BareCSParser::AnyContext::AnyContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BareCSParser::AnyContext::Float() {
  return getToken(BareCSParser::Float, 0);
}

tree::TerminalNode* BareCSParser::AnyContext::Integer() {
  return getToken(BareCSParser::Integer, 0);
}

tree::TerminalNode* BareCSParser::AnyContext::Simple_name() {
  return getToken(BareCSParser::Simple_name, 0);
}

tree::TerminalNode* BareCSParser::AnyContext::Double_quote_float() {
  return getToken(BareCSParser::Double_quote_float, 0);
}

tree::TerminalNode* BareCSParser::AnyContext::Double_quote_integer() {
  return getToken(BareCSParser::Double_quote_integer, 0);
}

tree::TerminalNode* BareCSParser::AnyContext::Double_quote_string() {
  return getToken(BareCSParser::Double_quote_string, 0);
}


size_t BareCSParser::AnyContext::getRuleIndex() const {
  return BareCSParser::RuleAny;
}


std::any BareCSParser::AnyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BareCSParserVisitor*>(visitor))
    return parserVisitor->visitAny(this);
  else
    return visitor->visitChildren(this);
}

BareCSParser::AnyContext* BareCSParser::any() {
  AnyContext *_localctx = _tracker.createInstance<AnyContext>(_ctx, getState());
  enterRule(_localctx, 8, BareCSParser::RuleAny);
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
    setState(44);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 966) != 0))) {
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

//----------------- Column_nameContext ------------------------------------------------------------------

BareCSParser::Column_nameContext::Column_nameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BareCSParser::Column_nameContext::Simple_name() {
  return getToken(BareCSParser::Simple_name, 0);
}

tree::TerminalNode* BareCSParser::Column_nameContext::Double_quote_string() {
  return getToken(BareCSParser::Double_quote_string, 0);
}

tree::TerminalNode* BareCSParser::Column_nameContext::Number_of_name() {
  return getToken(BareCSParser::Number_of_name, 0);
}


size_t BareCSParser::Column_nameContext::getRuleIndex() const {
  return BareCSParser::RuleColumn_name;
}


std::any BareCSParser::Column_nameContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BareCSParserVisitor*>(visitor))
    return parserVisitor->visitColumn_name(this);
  else
    return visitor->visitChildren(this);
}

BareCSParser::Column_nameContext* BareCSParser::column_name() {
  Column_nameContext *_localctx = _tracker.createInstance<Column_nameContext>(_ctx, getState());
  enterRule(_localctx, 10, BareCSParser::RuleColumn_name);
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
    setState(46);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 224) != 0))) {
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

void BareCSParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  barecsparserParserInitialize();
#else
  ::antlr4::internal::call_once(barecsparserParserOnceFlag, barecsparserParserInitialize);
#endif
}
