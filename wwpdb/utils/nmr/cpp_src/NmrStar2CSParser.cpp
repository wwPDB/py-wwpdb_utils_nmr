
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrStar2CSParser.g4 by ANTLR 4.13.2


#include "NmrStar2CSParserVisitor.h"

#include "NmrStar2CSParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct NmrStar2CSParserStaticData final {
  NmrStar2CSParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  NmrStar2CSParserStaticData(const NmrStar2CSParserStaticData&) = delete;
  NmrStar2CSParserStaticData(NmrStar2CSParserStaticData&&) = delete;
  NmrStar2CSParserStaticData& operator=(const NmrStar2CSParserStaticData&) = delete;
  NmrStar2CSParserStaticData& operator=(NmrStar2CSParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag nmrstar2csparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<NmrStar2CSParserStaticData> nmrstar2csparserParserStaticData = nullptr;

void nmrstar2csparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (nmrstar2csparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(nmrstar2csparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<NmrStar2CSParserStaticData>(
    std::vector<std::string>{
      "nmrstar2_cs", "seq_loop", "seq_tags", "seq_data", "cs_loop", "cs_tags", 
      "cs_data", "any"
    },
    std::vector<std::string>{
      "", "'loop_'", "'stop_'", "'_Residue_seq_code'", "'_Residue_label'", 
      "'_Atom_shift_assign_ID'", "'_Residue_author_seq_code'", "'_Atom_name'", 
      "'_Atom_type'", "'_Chem_shift_value'", "'_Chem_shift_value_error'", 
      "'_Chem_shift_ambiguity_code'"
    },
    std::vector<std::string>{
      "", "Loop", "Stop", "Residue_seq_code", "Residue_label", "Atom_shift_assign_ID", 
      "Residue_author_seq_code", "Atom_name", "Atom_type", "Chem_shift_value", 
      "Chem_shift_value_error", "Chem_shift_ambiguity_code", "Integer", 
      "Float", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", "Simple_name", 
      "Double_quote_string", "Single_quote_string", "SPACE", "RETURN", "SECTION_COMMENT", 
      "LINE_COMMENT"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,23,84,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,7,
  	7,7,1,0,3,0,18,8,0,1,0,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,1,0,1,0,1,
  	1,1,1,1,1,4,1,33,8,1,11,1,12,1,34,1,1,4,1,38,8,1,11,1,12,1,39,1,1,1,1,
  	3,1,44,8,1,1,2,1,2,1,2,1,3,4,3,50,8,3,11,3,12,3,51,1,3,1,3,1,4,1,4,1,
  	4,4,4,59,8,4,11,4,12,4,60,1,4,4,4,64,8,4,11,4,12,4,65,1,4,1,4,3,4,70,
  	8,4,1,5,1,5,1,5,1,6,4,6,76,8,6,11,6,12,6,77,1,6,1,6,1,7,1,7,1,7,0,0,8,
  	0,2,4,6,8,10,12,14,0,4,1,1,21,21,1,0,3,4,1,0,3,11,2,0,12,13,17,19,87,
  	0,17,1,0,0,0,2,29,1,0,0,0,4,45,1,0,0,0,6,49,1,0,0,0,8,55,1,0,0,0,10,71,
  	1,0,0,0,12,75,1,0,0,0,14,81,1,0,0,0,16,18,5,21,0,0,17,16,1,0,0,0,17,18,
  	1,0,0,0,18,24,1,0,0,0,19,23,3,2,1,0,20,23,3,8,4,0,21,23,5,21,0,0,22,19,
  	1,0,0,0,22,20,1,0,0,0,22,21,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,
  	1,0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,30,
  	5,1,0,0,30,32,5,21,0,0,31,33,3,4,2,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,
  	1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,38,3,6,3,0,37,36,1,0,0,0,38,39,
  	1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,43,5,2,0,0,42,44,
  	7,0,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,3,1,0,0,0,45,46,7,1,0,0,46,47,
  	5,21,0,0,47,5,1,0,0,0,48,50,3,14,7,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,
  	1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,21,0,0,54,7,1,0,0,0,55,56,
  	5,1,0,0,56,58,5,21,0,0,57,59,3,10,5,0,58,57,1,0,0,0,59,60,1,0,0,0,60,
  	58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,64,3,12,6,0,63,62,1,0,0,0,64,
  	65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,69,5,2,0,0,68,
  	70,7,0,0,0,69,68,1,0,0,0,69,70,1,0,0,0,70,9,1,0,0,0,71,72,7,2,0,0,72,
  	73,5,21,0,0,73,11,1,0,0,0,74,76,3,14,7,0,75,74,1,0,0,0,76,77,1,0,0,0,
  	77,75,1,0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,79,80,5,21,0,0,80,13,1,0,0,
  	0,81,82,7,3,0,0,82,15,1,0,0,0,11,17,22,24,34,39,43,51,60,65,69,77
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  nmrstar2csparserParserStaticData = std::move(staticData);
}

}

NmrStar2CSParser::NmrStar2CSParser(TokenStream *input) : NmrStar2CSParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

NmrStar2CSParser::NmrStar2CSParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  NmrStar2CSParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *nmrstar2csparserParserStaticData->atn, nmrstar2csparserParserStaticData->decisionToDFA, nmrstar2csparserParserStaticData->sharedContextCache, options);
}

NmrStar2CSParser::~NmrStar2CSParser() {
  delete _interpreter;
}

const atn::ATN& NmrStar2CSParser::getATN() const {
  return *nmrstar2csparserParserStaticData->atn;
}

std::string NmrStar2CSParser::getGrammarFileName() const {
  return "NmrStar2CSParser.g4";
}

const std::vector<std::string>& NmrStar2CSParser::getRuleNames() const {
  return nmrstar2csparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& NmrStar2CSParser::getVocabulary() const {
  return nmrstar2csparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView NmrStar2CSParser::getSerializedATN() const {
  return nmrstar2csparserParserStaticData->serializedATN;
}


//----------------- Nmrstar2_csContext ------------------------------------------------------------------

NmrStar2CSParser::Nmrstar2_csContext::Nmrstar2_csContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrStar2CSParser::Nmrstar2_csContext::EOF() {
  return getToken(NmrStar2CSParser::EOF, 0);
}

std::vector<tree::TerminalNode *> NmrStar2CSParser::Nmrstar2_csContext::RETURN() {
  return getTokens(NmrStar2CSParser::RETURN);
}

tree::TerminalNode* NmrStar2CSParser::Nmrstar2_csContext::RETURN(size_t i) {
  return getToken(NmrStar2CSParser::RETURN, i);
}

std::vector<NmrStar2CSParser::Seq_loopContext *> NmrStar2CSParser::Nmrstar2_csContext::seq_loop() {
  return getRuleContexts<NmrStar2CSParser::Seq_loopContext>();
}

NmrStar2CSParser::Seq_loopContext* NmrStar2CSParser::Nmrstar2_csContext::seq_loop(size_t i) {
  return getRuleContext<NmrStar2CSParser::Seq_loopContext>(i);
}

std::vector<NmrStar2CSParser::Cs_loopContext *> NmrStar2CSParser::Nmrstar2_csContext::cs_loop() {
  return getRuleContexts<NmrStar2CSParser::Cs_loopContext>();
}

NmrStar2CSParser::Cs_loopContext* NmrStar2CSParser::Nmrstar2_csContext::cs_loop(size_t i) {
  return getRuleContext<NmrStar2CSParser::Cs_loopContext>(i);
}


size_t NmrStar2CSParser::Nmrstar2_csContext::getRuleIndex() const {
  return NmrStar2CSParser::RuleNmrstar2_cs;
}


std::any NmrStar2CSParser::Nmrstar2_csContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrStar2CSParserVisitor*>(visitor))
    return parserVisitor->visitNmrstar2_cs(this);
  else
    return visitor->visitChildren(this);
}

NmrStar2CSParser::Nmrstar2_csContext* NmrStar2CSParser::nmrstar2_cs() {
  Nmrstar2_csContext *_localctx = _tracker.createInstance<Nmrstar2_csContext>(_ctx, getState());
  enterRule(_localctx, 0, NmrStar2CSParser::RuleNmrstar2_cs);
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
      match(NmrStar2CSParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(24);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == NmrStar2CSParser::Loop

    || _la == NmrStar2CSParser::RETURN) {
      setState(22);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(19);
        seq_loop();
        break;
      }

      case 2: {
        setState(20);
        cs_loop();
        break;
      }

      case 3: {
        setState(21);
        match(NmrStar2CSParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(26);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(27);
    match(NmrStar2CSParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Seq_loopContext ------------------------------------------------------------------

NmrStar2CSParser::Seq_loopContext::Seq_loopContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrStar2CSParser::Seq_loopContext::Loop() {
  return getToken(NmrStar2CSParser::Loop, 0);
}

std::vector<tree::TerminalNode *> NmrStar2CSParser::Seq_loopContext::RETURN() {
  return getTokens(NmrStar2CSParser::RETURN);
}

tree::TerminalNode* NmrStar2CSParser::Seq_loopContext::RETURN(size_t i) {
  return getToken(NmrStar2CSParser::RETURN, i);
}

tree::TerminalNode* NmrStar2CSParser::Seq_loopContext::Stop() {
  return getToken(NmrStar2CSParser::Stop, 0);
}

std::vector<NmrStar2CSParser::Seq_tagsContext *> NmrStar2CSParser::Seq_loopContext::seq_tags() {
  return getRuleContexts<NmrStar2CSParser::Seq_tagsContext>();
}

NmrStar2CSParser::Seq_tagsContext* NmrStar2CSParser::Seq_loopContext::seq_tags(size_t i) {
  return getRuleContext<NmrStar2CSParser::Seq_tagsContext>(i);
}

std::vector<NmrStar2CSParser::Seq_dataContext *> NmrStar2CSParser::Seq_loopContext::seq_data() {
  return getRuleContexts<NmrStar2CSParser::Seq_dataContext>();
}

NmrStar2CSParser::Seq_dataContext* NmrStar2CSParser::Seq_loopContext::seq_data(size_t i) {
  return getRuleContext<NmrStar2CSParser::Seq_dataContext>(i);
}

tree::TerminalNode* NmrStar2CSParser::Seq_loopContext::EOF() {
  return getToken(NmrStar2CSParser::EOF, 0);
}


size_t NmrStar2CSParser::Seq_loopContext::getRuleIndex() const {
  return NmrStar2CSParser::RuleSeq_loop;
}


std::any NmrStar2CSParser::Seq_loopContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrStar2CSParserVisitor*>(visitor))
    return parserVisitor->visitSeq_loop(this);
  else
    return visitor->visitChildren(this);
}

NmrStar2CSParser::Seq_loopContext* NmrStar2CSParser::seq_loop() {
  Seq_loopContext *_localctx = _tracker.createInstance<Seq_loopContext>(_ctx, getState());
  enterRule(_localctx, 2, NmrStar2CSParser::RuleSeq_loop);
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
    setState(29);
    match(NmrStar2CSParser::Loop);
    setState(30);
    match(NmrStar2CSParser::RETURN);
    setState(32); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(31);
      seq_tags();
      setState(34); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrStar2CSParser::Residue_seq_code

    || _la == NmrStar2CSParser::Residue_label);
    setState(37); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(36);
      seq_data();
      setState(39); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 929792) != 0));
    setState(41);
    match(NmrStar2CSParser::Stop);
    setState(43);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx)) {
    case 1: {
      setState(42);
      _la = _input->LA(1);
      if (!(_la == NmrStar2CSParser::EOF

      || _la == NmrStar2CSParser::RETURN)) {
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

//----------------- Seq_tagsContext ------------------------------------------------------------------

NmrStar2CSParser::Seq_tagsContext::Seq_tagsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrStar2CSParser::Seq_tagsContext::RETURN() {
  return getToken(NmrStar2CSParser::RETURN, 0);
}

tree::TerminalNode* NmrStar2CSParser::Seq_tagsContext::Residue_seq_code() {
  return getToken(NmrStar2CSParser::Residue_seq_code, 0);
}

tree::TerminalNode* NmrStar2CSParser::Seq_tagsContext::Residue_label() {
  return getToken(NmrStar2CSParser::Residue_label, 0);
}


size_t NmrStar2CSParser::Seq_tagsContext::getRuleIndex() const {
  return NmrStar2CSParser::RuleSeq_tags;
}


std::any NmrStar2CSParser::Seq_tagsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrStar2CSParserVisitor*>(visitor))
    return parserVisitor->visitSeq_tags(this);
  else
    return visitor->visitChildren(this);
}

NmrStar2CSParser::Seq_tagsContext* NmrStar2CSParser::seq_tags() {
  Seq_tagsContext *_localctx = _tracker.createInstance<Seq_tagsContext>(_ctx, getState());
  enterRule(_localctx, 4, NmrStar2CSParser::RuleSeq_tags);
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
    setState(45);
    _la = _input->LA(1);
    if (!(_la == NmrStar2CSParser::Residue_seq_code

    || _la == NmrStar2CSParser::Residue_label)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(46);
    match(NmrStar2CSParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Seq_dataContext ------------------------------------------------------------------

NmrStar2CSParser::Seq_dataContext::Seq_dataContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrStar2CSParser::Seq_dataContext::RETURN() {
  return getToken(NmrStar2CSParser::RETURN, 0);
}

std::vector<NmrStar2CSParser::AnyContext *> NmrStar2CSParser::Seq_dataContext::any() {
  return getRuleContexts<NmrStar2CSParser::AnyContext>();
}

NmrStar2CSParser::AnyContext* NmrStar2CSParser::Seq_dataContext::any(size_t i) {
  return getRuleContext<NmrStar2CSParser::AnyContext>(i);
}


size_t NmrStar2CSParser::Seq_dataContext::getRuleIndex() const {
  return NmrStar2CSParser::RuleSeq_data;
}


std::any NmrStar2CSParser::Seq_dataContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrStar2CSParserVisitor*>(visitor))
    return parserVisitor->visitSeq_data(this);
  else
    return visitor->visitChildren(this);
}

NmrStar2CSParser::Seq_dataContext* NmrStar2CSParser::seq_data() {
  Seq_dataContext *_localctx = _tracker.createInstance<Seq_dataContext>(_ctx, getState());
  enterRule(_localctx, 6, NmrStar2CSParser::RuleSeq_data);
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
    setState(49); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(48);
      any();
      setState(51); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 929792) != 0));
    setState(53);
    match(NmrStar2CSParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Cs_loopContext ------------------------------------------------------------------

NmrStar2CSParser::Cs_loopContext::Cs_loopContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrStar2CSParser::Cs_loopContext::Loop() {
  return getToken(NmrStar2CSParser::Loop, 0);
}

std::vector<tree::TerminalNode *> NmrStar2CSParser::Cs_loopContext::RETURN() {
  return getTokens(NmrStar2CSParser::RETURN);
}

tree::TerminalNode* NmrStar2CSParser::Cs_loopContext::RETURN(size_t i) {
  return getToken(NmrStar2CSParser::RETURN, i);
}

tree::TerminalNode* NmrStar2CSParser::Cs_loopContext::Stop() {
  return getToken(NmrStar2CSParser::Stop, 0);
}

std::vector<NmrStar2CSParser::Cs_tagsContext *> NmrStar2CSParser::Cs_loopContext::cs_tags() {
  return getRuleContexts<NmrStar2CSParser::Cs_tagsContext>();
}

NmrStar2CSParser::Cs_tagsContext* NmrStar2CSParser::Cs_loopContext::cs_tags(size_t i) {
  return getRuleContext<NmrStar2CSParser::Cs_tagsContext>(i);
}

std::vector<NmrStar2CSParser::Cs_dataContext *> NmrStar2CSParser::Cs_loopContext::cs_data() {
  return getRuleContexts<NmrStar2CSParser::Cs_dataContext>();
}

NmrStar2CSParser::Cs_dataContext* NmrStar2CSParser::Cs_loopContext::cs_data(size_t i) {
  return getRuleContext<NmrStar2CSParser::Cs_dataContext>(i);
}

tree::TerminalNode* NmrStar2CSParser::Cs_loopContext::EOF() {
  return getToken(NmrStar2CSParser::EOF, 0);
}


size_t NmrStar2CSParser::Cs_loopContext::getRuleIndex() const {
  return NmrStar2CSParser::RuleCs_loop;
}


std::any NmrStar2CSParser::Cs_loopContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrStar2CSParserVisitor*>(visitor))
    return parserVisitor->visitCs_loop(this);
  else
    return visitor->visitChildren(this);
}

NmrStar2CSParser::Cs_loopContext* NmrStar2CSParser::cs_loop() {
  Cs_loopContext *_localctx = _tracker.createInstance<Cs_loopContext>(_ctx, getState());
  enterRule(_localctx, 8, NmrStar2CSParser::RuleCs_loop);
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
    setState(55);
    match(NmrStar2CSParser::Loop);
    setState(56);
    match(NmrStar2CSParser::RETURN);
    setState(58); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(57);
      cs_tags();
      setState(60); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 4088) != 0));
    setState(63); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(62);
      cs_data();
      setState(65); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 929792) != 0));
    setState(67);
    match(NmrStar2CSParser::Stop);
    setState(69);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx)) {
    case 1: {
      setState(68);
      _la = _input->LA(1);
      if (!(_la == NmrStar2CSParser::EOF

      || _la == NmrStar2CSParser::RETURN)) {
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

//----------------- Cs_tagsContext ------------------------------------------------------------------

NmrStar2CSParser::Cs_tagsContext::Cs_tagsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrStar2CSParser::Cs_tagsContext::RETURN() {
  return getToken(NmrStar2CSParser::RETURN, 0);
}

tree::TerminalNode* NmrStar2CSParser::Cs_tagsContext::Atom_shift_assign_ID() {
  return getToken(NmrStar2CSParser::Atom_shift_assign_ID, 0);
}

tree::TerminalNode* NmrStar2CSParser::Cs_tagsContext::Residue_author_seq_code() {
  return getToken(NmrStar2CSParser::Residue_author_seq_code, 0);
}

tree::TerminalNode* NmrStar2CSParser::Cs_tagsContext::Residue_seq_code() {
  return getToken(NmrStar2CSParser::Residue_seq_code, 0);
}

tree::TerminalNode* NmrStar2CSParser::Cs_tagsContext::Residue_label() {
  return getToken(NmrStar2CSParser::Residue_label, 0);
}

tree::TerminalNode* NmrStar2CSParser::Cs_tagsContext::Atom_name() {
  return getToken(NmrStar2CSParser::Atom_name, 0);
}

tree::TerminalNode* NmrStar2CSParser::Cs_tagsContext::Atom_type() {
  return getToken(NmrStar2CSParser::Atom_type, 0);
}

tree::TerminalNode* NmrStar2CSParser::Cs_tagsContext::Chem_shift_value() {
  return getToken(NmrStar2CSParser::Chem_shift_value, 0);
}

tree::TerminalNode* NmrStar2CSParser::Cs_tagsContext::Chem_shift_value_error() {
  return getToken(NmrStar2CSParser::Chem_shift_value_error, 0);
}

tree::TerminalNode* NmrStar2CSParser::Cs_tagsContext::Chem_shift_ambiguity_code() {
  return getToken(NmrStar2CSParser::Chem_shift_ambiguity_code, 0);
}


size_t NmrStar2CSParser::Cs_tagsContext::getRuleIndex() const {
  return NmrStar2CSParser::RuleCs_tags;
}


std::any NmrStar2CSParser::Cs_tagsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrStar2CSParserVisitor*>(visitor))
    return parserVisitor->visitCs_tags(this);
  else
    return visitor->visitChildren(this);
}

NmrStar2CSParser::Cs_tagsContext* NmrStar2CSParser::cs_tags() {
  Cs_tagsContext *_localctx = _tracker.createInstance<Cs_tagsContext>(_ctx, getState());
  enterRule(_localctx, 10, NmrStar2CSParser::RuleCs_tags);
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
    setState(71);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 4088) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(72);
    match(NmrStar2CSParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Cs_dataContext ------------------------------------------------------------------

NmrStar2CSParser::Cs_dataContext::Cs_dataContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrStar2CSParser::Cs_dataContext::RETURN() {
  return getToken(NmrStar2CSParser::RETURN, 0);
}

std::vector<NmrStar2CSParser::AnyContext *> NmrStar2CSParser::Cs_dataContext::any() {
  return getRuleContexts<NmrStar2CSParser::AnyContext>();
}

NmrStar2CSParser::AnyContext* NmrStar2CSParser::Cs_dataContext::any(size_t i) {
  return getRuleContext<NmrStar2CSParser::AnyContext>(i);
}


size_t NmrStar2CSParser::Cs_dataContext::getRuleIndex() const {
  return NmrStar2CSParser::RuleCs_data;
}


std::any NmrStar2CSParser::Cs_dataContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrStar2CSParserVisitor*>(visitor))
    return parserVisitor->visitCs_data(this);
  else
    return visitor->visitChildren(this);
}

NmrStar2CSParser::Cs_dataContext* NmrStar2CSParser::cs_data() {
  Cs_dataContext *_localctx = _tracker.createInstance<Cs_dataContext>(_ctx, getState());
  enterRule(_localctx, 12, NmrStar2CSParser::RuleCs_data);
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
    setState(75); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(74);
      any();
      setState(77); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 929792) != 0));
    setState(79);
    match(NmrStar2CSParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AnyContext ------------------------------------------------------------------

NmrStar2CSParser::AnyContext::AnyContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrStar2CSParser::AnyContext::Float() {
  return getToken(NmrStar2CSParser::Float, 0);
}

tree::TerminalNode* NmrStar2CSParser::AnyContext::Integer() {
  return getToken(NmrStar2CSParser::Integer, 0);
}

tree::TerminalNode* NmrStar2CSParser::AnyContext::Simple_name() {
  return getToken(NmrStar2CSParser::Simple_name, 0);
}

tree::TerminalNode* NmrStar2CSParser::AnyContext::Double_quote_string() {
  return getToken(NmrStar2CSParser::Double_quote_string, 0);
}

tree::TerminalNode* NmrStar2CSParser::AnyContext::Single_quote_string() {
  return getToken(NmrStar2CSParser::Single_quote_string, 0);
}


size_t NmrStar2CSParser::AnyContext::getRuleIndex() const {
  return NmrStar2CSParser::RuleAny;
}


std::any NmrStar2CSParser::AnyContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrStar2CSParserVisitor*>(visitor))
    return parserVisitor->visitAny(this);
  else
    return visitor->visitChildren(this);
}

NmrStar2CSParser::AnyContext* NmrStar2CSParser::any() {
  AnyContext *_localctx = _tracker.createInstance<AnyContext>(_ctx, getState());
  enterRule(_localctx, 14, NmrStar2CSParser::RuleAny);
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
    setState(81);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 929792) != 0))) {
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

void NmrStar2CSParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  nmrstar2csparserParserInitialize();
#else
  ::antlr4::internal::call_once(nmrstar2csparserParserOnceFlag, nmrstar2csparserParserInitialize);
#endif
}
