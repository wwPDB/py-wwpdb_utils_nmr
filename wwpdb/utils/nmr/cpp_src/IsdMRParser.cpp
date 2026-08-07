
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/IsdMRParser.g4 by ANTLR 4.13.0


#include "IsdMRParserVisitor.h"

#include "IsdMRParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct IsdMRParserStaticData final {
  IsdMRParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  IsdMRParserStaticData(const IsdMRParserStaticData&) = delete;
  IsdMRParserStaticData(IsdMRParserStaticData&&) = delete;
  IsdMRParserStaticData& operator=(const IsdMRParserStaticData&) = delete;
  IsdMRParserStaticData& operator=(IsdMRParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag isdmrparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
IsdMRParserStaticData *isdmrparserParserStaticData = nullptr;

void isdmrparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (isdmrparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(isdmrparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<IsdMRParserStaticData>(
    std::vector<std::string>{
      "isd_mr", "distance_restraints", "distance_restraint"
    },
    std::vector<std::string>{
    },
    std::vector<std::string>{
      "", "Distance", "Integer", "Float", "SHARP_COMMENT", "EXCLM_COMMENT", 
      "SMCLN_COMMENT", "Atom_selection", "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", 
      "LINE_COMMENT"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,11,24,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,1,0,
  	1,0,1,1,1,1,4,1,17,8,1,11,1,12,1,18,1,2,1,2,1,2,1,2,0,0,3,0,2,4,0,0,22,
  	0,9,1,0,0,0,2,14,1,0,0,0,4,20,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,11,1,
  	0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,12,1,0,0,0,11,9,1,0,0,0,12,13,5,0,0,
  	1,13,1,1,0,0,0,14,16,5,1,0,0,15,17,3,4,2,0,16,15,1,0,0,0,17,18,1,0,0,
  	0,18,16,1,0,0,0,18,19,1,0,0,0,19,3,1,0,0,0,20,21,5,7,0,0,21,22,5,7,0,
  	0,22,5,1,0,0,0,2,9,18
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  isdmrparserParserStaticData = staticData.release();
}

}

IsdMRParser::IsdMRParser(TokenStream *input) : IsdMRParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

IsdMRParser::IsdMRParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  IsdMRParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *isdmrparserParserStaticData->atn, isdmrparserParserStaticData->decisionToDFA, isdmrparserParserStaticData->sharedContextCache, options);
}

IsdMRParser::~IsdMRParser() {
  delete _interpreter;
}

const atn::ATN& IsdMRParser::getATN() const {
  return *isdmrparserParserStaticData->atn;
}

std::string IsdMRParser::getGrammarFileName() const {
  return "IsdMRParser.g4";
}

const std::vector<std::string>& IsdMRParser::getRuleNames() const {
  return isdmrparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& IsdMRParser::getVocabulary() const {
  return isdmrparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView IsdMRParser::getSerializedATN() const {
  return isdmrparserParserStaticData->serializedATN;
}


//----------------- Isd_mrContext ------------------------------------------------------------------

IsdMRParser::Isd_mrContext::Isd_mrContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* IsdMRParser::Isd_mrContext::EOF() {
  return getToken(IsdMRParser::EOF, 0);
}

std::vector<IsdMRParser::Distance_restraintsContext *> IsdMRParser::Isd_mrContext::distance_restraints() {
  return getRuleContexts<IsdMRParser::Distance_restraintsContext>();
}

IsdMRParser::Distance_restraintsContext* IsdMRParser::Isd_mrContext::distance_restraints(size_t i) {
  return getRuleContext<IsdMRParser::Distance_restraintsContext>(i);
}


size_t IsdMRParser::Isd_mrContext::getRuleIndex() const {
  return IsdMRParser::RuleIsd_mr;
}


std::any IsdMRParser::Isd_mrContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<IsdMRParserVisitor*>(visitor))
    return parserVisitor->visitIsd_mr(this);
  else
    return visitor->visitChildren(this);
}

IsdMRParser::Isd_mrContext* IsdMRParser::isd_mr() {
  Isd_mrContext *_localctx = _tracker.createInstance<Isd_mrContext>(_ctx, getState());
  enterRule(_localctx, 0, IsdMRParser::RuleIsd_mr);
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
    while (_la == IsdMRParser::Distance) {
      setState(6);
      distance_restraints();
      setState(11);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(12);
    match(IsdMRParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_restraintsContext ------------------------------------------------------------------

IsdMRParser::Distance_restraintsContext::Distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* IsdMRParser::Distance_restraintsContext::Distance() {
  return getToken(IsdMRParser::Distance, 0);
}

std::vector<IsdMRParser::Distance_restraintContext *> IsdMRParser::Distance_restraintsContext::distance_restraint() {
  return getRuleContexts<IsdMRParser::Distance_restraintContext>();
}

IsdMRParser::Distance_restraintContext* IsdMRParser::Distance_restraintsContext::distance_restraint(size_t i) {
  return getRuleContext<IsdMRParser::Distance_restraintContext>(i);
}


size_t IsdMRParser::Distance_restraintsContext::getRuleIndex() const {
  return IsdMRParser::RuleDistance_restraints;
}


std::any IsdMRParser::Distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<IsdMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraints(this);
  else
    return visitor->visitChildren(this);
}

IsdMRParser::Distance_restraintsContext* IsdMRParser::distance_restraints() {
  Distance_restraintsContext *_localctx = _tracker.createInstance<Distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 2, IsdMRParser::RuleDistance_restraints);
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
    setState(14);
    match(IsdMRParser::Distance);
    setState(16); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(15);
      distance_restraint();
      setState(18); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == IsdMRParser::Atom_selection);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_restraintContext ------------------------------------------------------------------

IsdMRParser::Distance_restraintContext::Distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> IsdMRParser::Distance_restraintContext::Atom_selection() {
  return getTokens(IsdMRParser::Atom_selection);
}

tree::TerminalNode* IsdMRParser::Distance_restraintContext::Atom_selection(size_t i) {
  return getToken(IsdMRParser::Atom_selection, i);
}


size_t IsdMRParser::Distance_restraintContext::getRuleIndex() const {
  return IsdMRParser::RuleDistance_restraint;
}


std::any IsdMRParser::Distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<IsdMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraint(this);
  else
    return visitor->visitChildren(this);
}

IsdMRParser::Distance_restraintContext* IsdMRParser::distance_restraint() {
  Distance_restraintContext *_localctx = _tracker.createInstance<Distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 4, IsdMRParser::RuleDistance_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(20);
    match(IsdMRParser::Atom_selection);
    setState(21);
    match(IsdMRParser::Atom_selection);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

void IsdMRParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  isdmrparserParserInitialize();
#else
  ::antlr4::internal::call_once(isdmrparserParserOnceFlag, isdmrparserParserInitialize);
#endif
}
