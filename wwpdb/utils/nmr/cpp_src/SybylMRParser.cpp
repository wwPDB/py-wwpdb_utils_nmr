
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SybylMRParser.g4 by ANTLR 4.13.0


#include "SybylMRParserVisitor.h"

#include "SybylMRParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct SybylMRParserStaticData final {
  SybylMRParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  SybylMRParserStaticData(const SybylMRParserStaticData&) = delete;
  SybylMRParserStaticData(SybylMRParserStaticData&&) = delete;
  SybylMRParserStaticData& operator=(const SybylMRParserStaticData&) = delete;
  SybylMRParserStaticData& operator=(SybylMRParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag sybylmrparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
SybylMRParserStaticData *sybylmrparserParserStaticData = nullptr;

void sybylmrparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (sybylmrparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(sybylmrparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<SybylMRParserStaticData>(
    std::vector<std::string>{
      "sybyl_mr", "distance_restraints", "distance_restraint", "number"
    },
    std::vector<std::string>{
      "", "'ATOM1'", "'ATOM2'", "'LOWER'", "'UPPER'"
    },
    std::vector<std::string>{
      "", "Atom1", "Atom2", "Lower", "Upper", "Integer", "Float", "Float_DecimalComma", 
      "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", "Atom_selection", 
      "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,15,33,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,0,13,
  	9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,4,1,22,8,1,11,1,12,1,23,1,2,1,2,1,2,1,
  	2,1,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,1,1,0,5,7,30,0,11,1,0,0,0,2,16,1,0,
  	0,0,4,25,1,0,0,0,6,30,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,
  	11,9,1,0,0,0,11,12,1,0,0,0,12,14,1,0,0,0,13,11,1,0,0,0,14,15,5,0,0,1,
  	15,1,1,0,0,0,16,17,5,1,0,0,17,18,5,2,0,0,18,19,5,3,0,0,19,21,5,4,0,0,
  	20,22,3,4,2,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,
  	24,3,1,0,0,0,25,26,5,11,0,0,26,27,5,11,0,0,27,28,3,6,3,0,28,29,3,6,3,
  	0,29,5,1,0,0,0,30,31,7,0,0,0,31,7,1,0,0,0,2,11,23
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  sybylmrparserParserStaticData = staticData.release();
}

}

SybylMRParser::SybylMRParser(TokenStream *input) : SybylMRParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

SybylMRParser::SybylMRParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  SybylMRParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *sybylmrparserParserStaticData->atn, sybylmrparserParserStaticData->decisionToDFA, sybylmrparserParserStaticData->sharedContextCache, options);
}

SybylMRParser::~SybylMRParser() {
  delete _interpreter;
}

const atn::ATN& SybylMRParser::getATN() const {
  return *sybylmrparserParserStaticData->atn;
}

std::string SybylMRParser::getGrammarFileName() const {
  return "SybylMRParser.g4";
}

const std::vector<std::string>& SybylMRParser::getRuleNames() const {
  return sybylmrparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& SybylMRParser::getVocabulary() const {
  return sybylmrparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView SybylMRParser::getSerializedATN() const {
  return sybylmrparserParserStaticData->serializedATN;
}


//----------------- Sybyl_mrContext ------------------------------------------------------------------

SybylMRParser::Sybyl_mrContext::Sybyl_mrContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SybylMRParser::Sybyl_mrContext::EOF() {
  return getToken(SybylMRParser::EOF, 0);
}

std::vector<SybylMRParser::Distance_restraintsContext *> SybylMRParser::Sybyl_mrContext::distance_restraints() {
  return getRuleContexts<SybylMRParser::Distance_restraintsContext>();
}

SybylMRParser::Distance_restraintsContext* SybylMRParser::Sybyl_mrContext::distance_restraints(size_t i) {
  return getRuleContext<SybylMRParser::Distance_restraintsContext>(i);
}


size_t SybylMRParser::Sybyl_mrContext::getRuleIndex() const {
  return SybylMRParser::RuleSybyl_mr;
}


std::any SybylMRParser::Sybyl_mrContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SybylMRParserVisitor*>(visitor))
    return parserVisitor->visitSybyl_mr(this);
  else
    return visitor->visitChildren(this);
}

SybylMRParser::Sybyl_mrContext* SybylMRParser::sybyl_mr() {
  Sybyl_mrContext *_localctx = _tracker.createInstance<Sybyl_mrContext>(_ctx, getState());
  enterRule(_localctx, 0, SybylMRParser::RuleSybyl_mr);
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
    setState(11);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == SybylMRParser::Atom1) {
      setState(8);
      distance_restraints();
      setState(13);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(14);
    match(SybylMRParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_restraintsContext ------------------------------------------------------------------

SybylMRParser::Distance_restraintsContext::Distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SybylMRParser::Distance_restraintsContext::Atom1() {
  return getToken(SybylMRParser::Atom1, 0);
}

tree::TerminalNode* SybylMRParser::Distance_restraintsContext::Atom2() {
  return getToken(SybylMRParser::Atom2, 0);
}

tree::TerminalNode* SybylMRParser::Distance_restraintsContext::Lower() {
  return getToken(SybylMRParser::Lower, 0);
}

tree::TerminalNode* SybylMRParser::Distance_restraintsContext::Upper() {
  return getToken(SybylMRParser::Upper, 0);
}

std::vector<SybylMRParser::Distance_restraintContext *> SybylMRParser::Distance_restraintsContext::distance_restraint() {
  return getRuleContexts<SybylMRParser::Distance_restraintContext>();
}

SybylMRParser::Distance_restraintContext* SybylMRParser::Distance_restraintsContext::distance_restraint(size_t i) {
  return getRuleContext<SybylMRParser::Distance_restraintContext>(i);
}


size_t SybylMRParser::Distance_restraintsContext::getRuleIndex() const {
  return SybylMRParser::RuleDistance_restraints;
}


std::any SybylMRParser::Distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SybylMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraints(this);
  else
    return visitor->visitChildren(this);
}

SybylMRParser::Distance_restraintsContext* SybylMRParser::distance_restraints() {
  Distance_restraintsContext *_localctx = _tracker.createInstance<Distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 2, SybylMRParser::RuleDistance_restraints);
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
    setState(16);
    match(SybylMRParser::Atom1);
    setState(17);
    match(SybylMRParser::Atom2);
    setState(18);
    match(SybylMRParser::Lower);
    setState(19);
    match(SybylMRParser::Upper);
    setState(21); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(20);
      distance_restraint();
      setState(23); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == SybylMRParser::Atom_selection);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_restraintContext ------------------------------------------------------------------

SybylMRParser::Distance_restraintContext::Distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> SybylMRParser::Distance_restraintContext::Atom_selection() {
  return getTokens(SybylMRParser::Atom_selection);
}

tree::TerminalNode* SybylMRParser::Distance_restraintContext::Atom_selection(size_t i) {
  return getToken(SybylMRParser::Atom_selection, i);
}

std::vector<SybylMRParser::NumberContext *> SybylMRParser::Distance_restraintContext::number() {
  return getRuleContexts<SybylMRParser::NumberContext>();
}

SybylMRParser::NumberContext* SybylMRParser::Distance_restraintContext::number(size_t i) {
  return getRuleContext<SybylMRParser::NumberContext>(i);
}


size_t SybylMRParser::Distance_restraintContext::getRuleIndex() const {
  return SybylMRParser::RuleDistance_restraint;
}


std::any SybylMRParser::Distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SybylMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraint(this);
  else
    return visitor->visitChildren(this);
}

SybylMRParser::Distance_restraintContext* SybylMRParser::distance_restraint() {
  Distance_restraintContext *_localctx = _tracker.createInstance<Distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 4, SybylMRParser::RuleDistance_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(25);
    match(SybylMRParser::Atom_selection);
    setState(26);
    match(SybylMRParser::Atom_selection);
    setState(27);
    number();
    setState(28);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberContext ------------------------------------------------------------------

SybylMRParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SybylMRParser::NumberContext::Float() {
  return getToken(SybylMRParser::Float, 0);
}

tree::TerminalNode* SybylMRParser::NumberContext::Float_DecimalComma() {
  return getToken(SybylMRParser::Float_DecimalComma, 0);
}

tree::TerminalNode* SybylMRParser::NumberContext::Integer() {
  return getToken(SybylMRParser::Integer, 0);
}


size_t SybylMRParser::NumberContext::getRuleIndex() const {
  return SybylMRParser::RuleNumber;
}


std::any SybylMRParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SybylMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

SybylMRParser::NumberContext* SybylMRParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 6, SybylMRParser::RuleNumber);
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

void SybylMRParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  sybylmrparserParserInitialize();
#else
  ::antlr4::internal::call_once(sybylmrparserParserOnceFlag, sybylmrparserParserInitialize);
#endif
}
