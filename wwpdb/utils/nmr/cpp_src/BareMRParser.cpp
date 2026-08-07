
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BareMRParser.g4 by ANTLR 4.13.0


#include "BareMRParserVisitor.h"

#include "BareMRParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct BareMRParserStaticData final {
  BareMRParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  BareMRParserStaticData(const BareMRParserStaticData&) = delete;
  BareMRParserStaticData(BareMRParserStaticData&&) = delete;
  BareMRParserStaticData& operator=(const BareMRParserStaticData&) = delete;
  BareMRParserStaticData& operator=(BareMRParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag baremrparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
BareMRParserStaticData *baremrparserParserStaticData = nullptr;

void baremrparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (baremrparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(baremrparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<BareMRParserStaticData>(
    std::vector<std::string>{
      "bare_mr", "mr_row_format", "header", "mr_row_list", "any", "column_name"
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
  baremrparserParserStaticData = staticData.release();
}

}

BareMRParser::BareMRParser(TokenStream *input) : BareMRParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

BareMRParser::BareMRParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  BareMRParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *baremrparserParserStaticData->atn, baremrparserParserStaticData->decisionToDFA, baremrparserParserStaticData->sharedContextCache, options);
}

BareMRParser::~BareMRParser() {
  delete _interpreter;
}

const atn::ATN& BareMRParser::getATN() const {
  return *baremrparserParserStaticData->atn;
}

std::string BareMRParser::getGrammarFileName() const {
  return "BareMRParser.g4";
}

const std::vector<std::string>& BareMRParser::getRuleNames() const {
  return baremrparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& BareMRParser::getVocabulary() const {
  return baremrparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView BareMRParser::getSerializedATN() const {
  return baremrparserParserStaticData->serializedATN;
}


//----------------- Bare_mrContext ------------------------------------------------------------------

BareMRParser::Bare_mrContext::Bare_mrContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BareMRParser::Bare_mrContext::EOF() {
  return getToken(BareMRParser::EOF, 0);
}

std::vector<tree::TerminalNode *> BareMRParser::Bare_mrContext::RETURN() {
  return getTokens(BareMRParser::RETURN);
}

tree::TerminalNode* BareMRParser::Bare_mrContext::RETURN(size_t i) {
  return getToken(BareMRParser::RETURN, i);
}

std::vector<BareMRParser::Mr_row_formatContext *> BareMRParser::Bare_mrContext::mr_row_format() {
  return getRuleContexts<BareMRParser::Mr_row_formatContext>();
}

BareMRParser::Mr_row_formatContext* BareMRParser::Bare_mrContext::mr_row_format(size_t i) {
  return getRuleContext<BareMRParser::Mr_row_formatContext>(i);
}


size_t BareMRParser::Bare_mrContext::getRuleIndex() const {
  return BareMRParser::RuleBare_mr;
}


std::any BareMRParser::Bare_mrContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BareMRParserVisitor*>(visitor))
    return parserVisitor->visitBare_mr(this);
  else
    return visitor->visitChildren(this);
}

BareMRParser::Bare_mrContext* BareMRParser::bare_mr() {
  Bare_mrContext *_localctx = _tracker.createInstance<Bare_mrContext>(_ctx, getState());
  enterRule(_localctx, 0, BareMRParser::RuleBare_mr);
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
      match(BareMRParser::RETURN);
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
        case BareMRParser::Number_of_name:
        case BareMRParser::Simple_name:
        case BareMRParser::Double_quote_string: {
          setState(15);
          mr_row_format();
          break;
        }

        case BareMRParser::RETURN: {
          setState(16);
          match(BareMRParser::RETURN);
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
    match(BareMRParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Mr_row_formatContext ------------------------------------------------------------------

BareMRParser::Mr_row_formatContext::Mr_row_formatContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BareMRParser::HeaderContext* BareMRParser::Mr_row_formatContext::header() {
  return getRuleContext<BareMRParser::HeaderContext>(0);
}

std::vector<BareMRParser::Mr_row_listContext *> BareMRParser::Mr_row_formatContext::mr_row_list() {
  return getRuleContexts<BareMRParser::Mr_row_listContext>();
}

BareMRParser::Mr_row_listContext* BareMRParser::Mr_row_formatContext::mr_row_list(size_t i) {
  return getRuleContext<BareMRParser::Mr_row_listContext>(i);
}


size_t BareMRParser::Mr_row_formatContext::getRuleIndex() const {
  return BareMRParser::RuleMr_row_format;
}


std::any BareMRParser::Mr_row_formatContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BareMRParserVisitor*>(visitor))
    return parserVisitor->visitMr_row_format(this);
  else
    return visitor->visitChildren(this);
}

BareMRParser::Mr_row_formatContext* BareMRParser::mr_row_format() {
  Mr_row_formatContext *_localctx = _tracker.createInstance<Mr_row_formatContext>(_ctx, getState());
  enterRule(_localctx, 2, BareMRParser::RuleMr_row_format);

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
              mr_row_list();
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

BareMRParser::HeaderContext::HeaderContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BareMRParser::HeaderContext::RETURN() {
  return getToken(BareMRParser::RETURN, 0);
}

std::vector<BareMRParser::Column_nameContext *> BareMRParser::HeaderContext::column_name() {
  return getRuleContexts<BareMRParser::Column_nameContext>();
}

BareMRParser::Column_nameContext* BareMRParser::HeaderContext::column_name(size_t i) {
  return getRuleContext<BareMRParser::Column_nameContext>(i);
}


size_t BareMRParser::HeaderContext::getRuleIndex() const {
  return BareMRParser::RuleHeader;
}


std::any BareMRParser::HeaderContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BareMRParserVisitor*>(visitor))
    return parserVisitor->visitHeader(this);
  else
    return visitor->visitChildren(this);
}

BareMRParser::HeaderContext* BareMRParser::header() {
  HeaderContext *_localctx = _tracker.createInstance<HeaderContext>(_ctx, getState());
  enterRule(_localctx, 4, BareMRParser::RuleHeader);
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
    match(BareMRParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Mr_row_listContext ------------------------------------------------------------------

BareMRParser::Mr_row_listContext::Mr_row_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BareMRParser::Mr_row_listContext::RETURN() {
  return getToken(BareMRParser::RETURN, 0);
}

tree::TerminalNode* BareMRParser::Mr_row_listContext::EOF() {
  return getToken(BareMRParser::EOF, 0);
}

std::vector<BareMRParser::AnyContext *> BareMRParser::Mr_row_listContext::any() {
  return getRuleContexts<BareMRParser::AnyContext>();
}

BareMRParser::AnyContext* BareMRParser::Mr_row_listContext::any(size_t i) {
  return getRuleContext<BareMRParser::AnyContext>(i);
}


size_t BareMRParser::Mr_row_listContext::getRuleIndex() const {
  return BareMRParser::RuleMr_row_list;
}


std::any BareMRParser::Mr_row_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BareMRParserVisitor*>(visitor))
    return parserVisitor->visitMr_row_list(this);
  else
    return visitor->visitChildren(this);
}

BareMRParser::Mr_row_listContext* BareMRParser::mr_row_list() {
  Mr_row_listContext *_localctx = _tracker.createInstance<Mr_row_listContext>(_ctx, getState());
  enterRule(_localctx, 6, BareMRParser::RuleMr_row_list);
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
    if (!(_la == BareMRParser::EOF

    || _la == BareMRParser::RETURN)) {
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

BareMRParser::AnyContext::AnyContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BareMRParser::AnyContext::Float() {
  return getToken(BareMRParser::Float, 0);
}

tree::TerminalNode* BareMRParser::AnyContext::Integer() {
  return getToken(BareMRParser::Integer, 0);
}

tree::TerminalNode* BareMRParser::AnyContext::Simple_name() {
  return getToken(BareMRParser::Simple_name, 0);
}

tree::TerminalNode* BareMRParser::AnyContext::Double_quote_float() {
  return getToken(BareMRParser::Double_quote_float, 0);
}

tree::TerminalNode* BareMRParser::AnyContext::Double_quote_integer() {
  return getToken(BareMRParser::Double_quote_integer, 0);
}

tree::TerminalNode* BareMRParser::AnyContext::Double_quote_string() {
  return getToken(BareMRParser::Double_quote_string, 0);
}


size_t BareMRParser::AnyContext::getRuleIndex() const {
  return BareMRParser::RuleAny;
}


std::any BareMRParser::AnyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BareMRParserVisitor*>(visitor))
    return parserVisitor->visitAny(this);
  else
    return visitor->visitChildren(this);
}

BareMRParser::AnyContext* BareMRParser::any() {
  AnyContext *_localctx = _tracker.createInstance<AnyContext>(_ctx, getState());
  enterRule(_localctx, 8, BareMRParser::RuleAny);
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

BareMRParser::Column_nameContext::Column_nameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BareMRParser::Column_nameContext::Simple_name() {
  return getToken(BareMRParser::Simple_name, 0);
}

tree::TerminalNode* BareMRParser::Column_nameContext::Double_quote_string() {
  return getToken(BareMRParser::Double_quote_string, 0);
}

tree::TerminalNode* BareMRParser::Column_nameContext::Number_of_name() {
  return getToken(BareMRParser::Number_of_name, 0);
}


size_t BareMRParser::Column_nameContext::getRuleIndex() const {
  return BareMRParser::RuleColumn_name;
}


std::any BareMRParser::Column_nameContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BareMRParserVisitor*>(visitor))
    return parserVisitor->visitColumn_name(this);
  else
    return visitor->visitChildren(this);
}

BareMRParser::Column_nameContext* BareMRParser::column_name() {
  Column_nameContext *_localctx = _tracker.createInstance<Column_nameContext>(_ctx, getState());
  enterRule(_localctx, 10, BareMRParser::RuleColumn_name);
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

void BareMRParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  baremrparserParserInitialize();
#else
  ::antlr4::internal::call_once(baremrparserParserOnceFlag, baremrparserParserInitialize);
#endif
}
