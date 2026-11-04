
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewCSParser.g4 by ANTLR 4.13.2


#include "NmrViewCSParserVisitor.h"

#include "NmrViewCSParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct NmrViewCSParserStaticData final {
  NmrViewCSParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  NmrViewCSParserStaticData(const NmrViewCSParserStaticData&) = delete;
  NmrViewCSParserStaticData(NmrViewCSParserStaticData&&) = delete;
  NmrViewCSParserStaticData& operator=(const NmrViewCSParserStaticData&) = delete;
  NmrViewCSParserStaticData& operator=(NmrViewCSParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag nmrviewcsparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<NmrViewCSParserStaticData> nmrviewcsparserParserStaticData = nullptr;

void nmrviewcsparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (nmrviewcsparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(nmrviewcsparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<NmrViewCSParserStaticData>(
    std::vector<std::string>{
      "nmrview_cs", "res_def_list", "res_id_def", "res_type_def", "prev_type_def", 
      "spin_system_def", "heterogeneity_def", "shift_list"
    },
    std::vector<std::string>{
      "", "", "", "", "", "'RES_ID'", "'RES_TYPE'", "'PREV_TYPE'", "'SPIN_SYSTEM_ID'", 
      "'HETEROGENEITY'", "'END_RES_DEF'"
    },
    std::vector<std::string>{
      "", "Integer", "Float", "SHARP_COMMENT", "EXCLM_COMMENT", "Res_ID", 
      "Res_Type", "Prev_Type", "Spin_System_ID", "Heterogeneity", "End_Res_Def", 
      "Type_pred", "Single_note", "Note_begin", "Simple_name", "SPACE", 
      "RETURN", "SECTION_COMMENT", "LINE_COMMENT", "Note_middle", "Note_end", 
      "SPACE_MN"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,21,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,7,
  	7,7,1,0,3,0,18,8,0,1,0,4,0,21,8,0,11,0,12,0,22,1,0,5,0,26,8,0,10,0,12,
  	0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,40,8,1,1,1,1,1,1,1,1,
  	1,1,1,1,1,1,1,4,1,49,8,1,11,1,12,1,50,1,1,1,1,3,1,55,8,1,1,2,1,2,1,2,
  	1,3,1,3,1,3,1,4,1,4,4,4,65,8,4,11,4,12,4,66,1,5,1,5,1,5,1,6,1,6,1,6,1,
  	7,1,7,1,7,1,7,1,7,5,7,80,8,7,10,7,12,7,83,9,7,1,7,3,7,86,8,7,1,7,0,0,
  	8,0,2,4,6,8,10,12,14,0,1,1,1,16,16,89,0,17,1,0,0,0,2,32,1,0,0,0,4,56,
  	1,0,0,0,6,59,1,0,0,0,8,62,1,0,0,0,10,68,1,0,0,0,12,71,1,0,0,0,14,74,1,
  	0,0,0,16,18,5,16,0,0,17,16,1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,19,21,
  	3,2,1,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,27,
  	1,0,0,0,24,26,5,16,0,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,
  	1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,0,0,1,31,1,1,0,0,0,32,33,
  	3,4,2,0,33,34,5,16,0,0,34,35,3,6,3,0,35,39,5,16,0,0,36,37,3,8,4,0,37,
  	38,5,16,0,0,38,40,1,0,0,0,39,36,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,
  	42,3,10,5,0,42,43,5,16,0,0,43,44,3,12,6,0,44,48,5,16,0,0,45,46,3,14,7,
  	0,46,47,5,16,0,0,47,49,1,0,0,0,48,45,1,0,0,0,49,50,1,0,0,0,50,48,1,0,
  	0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,54,5,10,0,0,53,55,7,0,0,0,54,53,1,
  	0,0,0,54,55,1,0,0,0,55,3,1,0,0,0,56,57,5,5,0,0,57,58,5,1,0,0,58,5,1,0,
  	0,0,59,60,5,6,0,0,60,61,5,14,0,0,61,7,1,0,0,0,62,64,5,7,0,0,63,65,5,11,
  	0,0,64,63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,9,1,0,
  	0,0,68,69,5,8,0,0,69,70,5,1,0,0,70,11,1,0,0,0,71,72,5,9,0,0,72,73,5,1,
  	0,0,73,13,1,0,0,0,74,75,5,14,0,0,75,85,5,2,0,0,76,86,5,12,0,0,77,81,5,
  	13,0,0,78,80,5,19,0,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,
  	1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,86,5,20,0,0,85,76,1,0,0,0,85,77,
  	1,0,0,0,85,86,1,0,0,0,86,15,1,0,0,0,9,17,22,27,39,50,54,66,81,85
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  nmrviewcsparserParserStaticData = std::move(staticData);
}

}

NmrViewCSParser::NmrViewCSParser(TokenStream *input) : NmrViewCSParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

NmrViewCSParser::NmrViewCSParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  NmrViewCSParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *nmrviewcsparserParserStaticData->atn, nmrviewcsparserParserStaticData->decisionToDFA, nmrviewcsparserParserStaticData->sharedContextCache, options);
}

NmrViewCSParser::~NmrViewCSParser() {
  delete _interpreter;
}

const atn::ATN& NmrViewCSParser::getATN() const {
  return *nmrviewcsparserParserStaticData->atn;
}

std::string NmrViewCSParser::getGrammarFileName() const {
  return "NmrViewCSParser.g4";
}

const std::vector<std::string>& NmrViewCSParser::getRuleNames() const {
  return nmrviewcsparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& NmrViewCSParser::getVocabulary() const {
  return nmrviewcsparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView NmrViewCSParser::getSerializedATN() const {
  return nmrviewcsparserParserStaticData->serializedATN;
}


//----------------- Nmrview_csContext ------------------------------------------------------------------

NmrViewCSParser::Nmrview_csContext::Nmrview_csContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewCSParser::Nmrview_csContext::EOF() {
  return getToken(NmrViewCSParser::EOF, 0);
}

std::vector<tree::TerminalNode *> NmrViewCSParser::Nmrview_csContext::RETURN() {
  return getTokens(NmrViewCSParser::RETURN);
}

tree::TerminalNode* NmrViewCSParser::Nmrview_csContext::RETURN(size_t i) {
  return getToken(NmrViewCSParser::RETURN, i);
}

std::vector<NmrViewCSParser::Res_def_listContext *> NmrViewCSParser::Nmrview_csContext::res_def_list() {
  return getRuleContexts<NmrViewCSParser::Res_def_listContext>();
}

NmrViewCSParser::Res_def_listContext* NmrViewCSParser::Nmrview_csContext::res_def_list(size_t i) {
  return getRuleContext<NmrViewCSParser::Res_def_listContext>(i);
}


size_t NmrViewCSParser::Nmrview_csContext::getRuleIndex() const {
  return NmrViewCSParser::RuleNmrview_cs;
}


std::any NmrViewCSParser::Nmrview_csContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewCSParserVisitor*>(visitor))
    return parserVisitor->visitNmrview_cs(this);
  else
    return visitor->visitChildren(this);
}

NmrViewCSParser::Nmrview_csContext* NmrViewCSParser::nmrview_cs() {
  Nmrview_csContext *_localctx = _tracker.createInstance<Nmrview_csContext>(_ctx, getState());
  enterRule(_localctx, 0, NmrViewCSParser::RuleNmrview_cs);
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

    _la = _input->LA(1);
    if (_la == NmrViewCSParser::RETURN) {
      setState(16);
      match(NmrViewCSParser::RETURN);
    }
    setState(20); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(19);
      res_def_list();
      setState(22); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewCSParser::Res_ID);
    setState(27);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == NmrViewCSParser::RETURN) {
      setState(24);
      match(NmrViewCSParser::RETURN);
      setState(29);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(30);
    match(NmrViewCSParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Res_def_listContext ------------------------------------------------------------------

NmrViewCSParser::Res_def_listContext::Res_def_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

NmrViewCSParser::Res_id_defContext* NmrViewCSParser::Res_def_listContext::res_id_def() {
  return getRuleContext<NmrViewCSParser::Res_id_defContext>(0);
}

std::vector<tree::TerminalNode *> NmrViewCSParser::Res_def_listContext::RETURN() {
  return getTokens(NmrViewCSParser::RETURN);
}

tree::TerminalNode* NmrViewCSParser::Res_def_listContext::RETURN(size_t i) {
  return getToken(NmrViewCSParser::RETURN, i);
}

NmrViewCSParser::Res_type_defContext* NmrViewCSParser::Res_def_listContext::res_type_def() {
  return getRuleContext<NmrViewCSParser::Res_type_defContext>(0);
}

NmrViewCSParser::Spin_system_defContext* NmrViewCSParser::Res_def_listContext::spin_system_def() {
  return getRuleContext<NmrViewCSParser::Spin_system_defContext>(0);
}

NmrViewCSParser::Heterogeneity_defContext* NmrViewCSParser::Res_def_listContext::heterogeneity_def() {
  return getRuleContext<NmrViewCSParser::Heterogeneity_defContext>(0);
}

tree::TerminalNode* NmrViewCSParser::Res_def_listContext::End_Res_Def() {
  return getToken(NmrViewCSParser::End_Res_Def, 0);
}

NmrViewCSParser::Prev_type_defContext* NmrViewCSParser::Res_def_listContext::prev_type_def() {
  return getRuleContext<NmrViewCSParser::Prev_type_defContext>(0);
}

std::vector<NmrViewCSParser::Shift_listContext *> NmrViewCSParser::Res_def_listContext::shift_list() {
  return getRuleContexts<NmrViewCSParser::Shift_listContext>();
}

NmrViewCSParser::Shift_listContext* NmrViewCSParser::Res_def_listContext::shift_list(size_t i) {
  return getRuleContext<NmrViewCSParser::Shift_listContext>(i);
}

tree::TerminalNode* NmrViewCSParser::Res_def_listContext::EOF() {
  return getToken(NmrViewCSParser::EOF, 0);
}


size_t NmrViewCSParser::Res_def_listContext::getRuleIndex() const {
  return NmrViewCSParser::RuleRes_def_list;
}


std::any NmrViewCSParser::Res_def_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewCSParserVisitor*>(visitor))
    return parserVisitor->visitRes_def_list(this);
  else
    return visitor->visitChildren(this);
}

NmrViewCSParser::Res_def_listContext* NmrViewCSParser::res_def_list() {
  Res_def_listContext *_localctx = _tracker.createInstance<Res_def_listContext>(_ctx, getState());
  enterRule(_localctx, 2, NmrViewCSParser::RuleRes_def_list);
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
    setState(32);
    res_id_def();
    setState(33);
    match(NmrViewCSParser::RETURN);
    setState(34);
    res_type_def();
    setState(35);
    match(NmrViewCSParser::RETURN);
    setState(39);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewCSParser::Prev_Type) {
      setState(36);
      prev_type_def();
      setState(37);
      match(NmrViewCSParser::RETURN);
    }
    setState(41);
    spin_system_def();
    setState(42);
    match(NmrViewCSParser::RETURN);
    setState(43);
    heterogeneity_def();
    setState(44);
    match(NmrViewCSParser::RETURN);
    setState(48); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(45);
      shift_list();
      setState(46);
      match(NmrViewCSParser::RETURN);
      setState(50); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewCSParser::Simple_name);
    setState(52);
    match(NmrViewCSParser::End_Res_Def);
    setState(54);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx)) {
    case 1: {
      setState(53);
      _la = _input->LA(1);
      if (!(_la == NmrViewCSParser::EOF

      || _la == NmrViewCSParser::RETURN)) {
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

//----------------- Res_id_defContext ------------------------------------------------------------------

NmrViewCSParser::Res_id_defContext::Res_id_defContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewCSParser::Res_id_defContext::Res_ID() {
  return getToken(NmrViewCSParser::Res_ID, 0);
}

tree::TerminalNode* NmrViewCSParser::Res_id_defContext::Integer() {
  return getToken(NmrViewCSParser::Integer, 0);
}


size_t NmrViewCSParser::Res_id_defContext::getRuleIndex() const {
  return NmrViewCSParser::RuleRes_id_def;
}


std::any NmrViewCSParser::Res_id_defContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewCSParserVisitor*>(visitor))
    return parserVisitor->visitRes_id_def(this);
  else
    return visitor->visitChildren(this);
}

NmrViewCSParser::Res_id_defContext* NmrViewCSParser::res_id_def() {
  Res_id_defContext *_localctx = _tracker.createInstance<Res_id_defContext>(_ctx, getState());
  enterRule(_localctx, 4, NmrViewCSParser::RuleRes_id_def);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(56);
    match(NmrViewCSParser::Res_ID);
    setState(57);
    match(NmrViewCSParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Res_type_defContext ------------------------------------------------------------------

NmrViewCSParser::Res_type_defContext::Res_type_defContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewCSParser::Res_type_defContext::Res_Type() {
  return getToken(NmrViewCSParser::Res_Type, 0);
}

tree::TerminalNode* NmrViewCSParser::Res_type_defContext::Simple_name() {
  return getToken(NmrViewCSParser::Simple_name, 0);
}


size_t NmrViewCSParser::Res_type_defContext::getRuleIndex() const {
  return NmrViewCSParser::RuleRes_type_def;
}


std::any NmrViewCSParser::Res_type_defContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewCSParserVisitor*>(visitor))
    return parserVisitor->visitRes_type_def(this);
  else
    return visitor->visitChildren(this);
}

NmrViewCSParser::Res_type_defContext* NmrViewCSParser::res_type_def() {
  Res_type_defContext *_localctx = _tracker.createInstance<Res_type_defContext>(_ctx, getState());
  enterRule(_localctx, 6, NmrViewCSParser::RuleRes_type_def);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(59);
    match(NmrViewCSParser::Res_Type);
    setState(60);
    match(NmrViewCSParser::Simple_name);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Prev_type_defContext ------------------------------------------------------------------

NmrViewCSParser::Prev_type_defContext::Prev_type_defContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewCSParser::Prev_type_defContext::Prev_Type() {
  return getToken(NmrViewCSParser::Prev_Type, 0);
}

std::vector<tree::TerminalNode *> NmrViewCSParser::Prev_type_defContext::Type_pred() {
  return getTokens(NmrViewCSParser::Type_pred);
}

tree::TerminalNode* NmrViewCSParser::Prev_type_defContext::Type_pred(size_t i) {
  return getToken(NmrViewCSParser::Type_pred, i);
}


size_t NmrViewCSParser::Prev_type_defContext::getRuleIndex() const {
  return NmrViewCSParser::RulePrev_type_def;
}


std::any NmrViewCSParser::Prev_type_defContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewCSParserVisitor*>(visitor))
    return parserVisitor->visitPrev_type_def(this);
  else
    return visitor->visitChildren(this);
}

NmrViewCSParser::Prev_type_defContext* NmrViewCSParser::prev_type_def() {
  Prev_type_defContext *_localctx = _tracker.createInstance<Prev_type_defContext>(_ctx, getState());
  enterRule(_localctx, 8, NmrViewCSParser::RulePrev_type_def);
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
    setState(62);
    match(NmrViewCSParser::Prev_Type);
    setState(64); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(63);
      match(NmrViewCSParser::Type_pred);
      setState(66); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewCSParser::Type_pred);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Spin_system_defContext ------------------------------------------------------------------

NmrViewCSParser::Spin_system_defContext::Spin_system_defContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewCSParser::Spin_system_defContext::Spin_System_ID() {
  return getToken(NmrViewCSParser::Spin_System_ID, 0);
}

tree::TerminalNode* NmrViewCSParser::Spin_system_defContext::Integer() {
  return getToken(NmrViewCSParser::Integer, 0);
}


size_t NmrViewCSParser::Spin_system_defContext::getRuleIndex() const {
  return NmrViewCSParser::RuleSpin_system_def;
}


std::any NmrViewCSParser::Spin_system_defContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewCSParserVisitor*>(visitor))
    return parserVisitor->visitSpin_system_def(this);
  else
    return visitor->visitChildren(this);
}

NmrViewCSParser::Spin_system_defContext* NmrViewCSParser::spin_system_def() {
  Spin_system_defContext *_localctx = _tracker.createInstance<Spin_system_defContext>(_ctx, getState());
  enterRule(_localctx, 10, NmrViewCSParser::RuleSpin_system_def);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(68);
    match(NmrViewCSParser::Spin_System_ID);
    setState(69);
    match(NmrViewCSParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Heterogeneity_defContext ------------------------------------------------------------------

NmrViewCSParser::Heterogeneity_defContext::Heterogeneity_defContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewCSParser::Heterogeneity_defContext::Heterogeneity() {
  return getToken(NmrViewCSParser::Heterogeneity, 0);
}

tree::TerminalNode* NmrViewCSParser::Heterogeneity_defContext::Integer() {
  return getToken(NmrViewCSParser::Integer, 0);
}


size_t NmrViewCSParser::Heterogeneity_defContext::getRuleIndex() const {
  return NmrViewCSParser::RuleHeterogeneity_def;
}


std::any NmrViewCSParser::Heterogeneity_defContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewCSParserVisitor*>(visitor))
    return parserVisitor->visitHeterogeneity_def(this);
  else
    return visitor->visitChildren(this);
}

NmrViewCSParser::Heterogeneity_defContext* NmrViewCSParser::heterogeneity_def() {
  Heterogeneity_defContext *_localctx = _tracker.createInstance<Heterogeneity_defContext>(_ctx, getState());
  enterRule(_localctx, 12, NmrViewCSParser::RuleHeterogeneity_def);

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
    match(NmrViewCSParser::Heterogeneity);
    setState(72);
    match(NmrViewCSParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Shift_listContext ------------------------------------------------------------------

NmrViewCSParser::Shift_listContext::Shift_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewCSParser::Shift_listContext::Simple_name() {
  return getToken(NmrViewCSParser::Simple_name, 0);
}

tree::TerminalNode* NmrViewCSParser::Shift_listContext::Float() {
  return getToken(NmrViewCSParser::Float, 0);
}

tree::TerminalNode* NmrViewCSParser::Shift_listContext::Single_note() {
  return getToken(NmrViewCSParser::Single_note, 0);
}

tree::TerminalNode* NmrViewCSParser::Shift_listContext::Note_begin() {
  return getToken(NmrViewCSParser::Note_begin, 0);
}

tree::TerminalNode* NmrViewCSParser::Shift_listContext::Note_end() {
  return getToken(NmrViewCSParser::Note_end, 0);
}

std::vector<tree::TerminalNode *> NmrViewCSParser::Shift_listContext::Note_middle() {
  return getTokens(NmrViewCSParser::Note_middle);
}

tree::TerminalNode* NmrViewCSParser::Shift_listContext::Note_middle(size_t i) {
  return getToken(NmrViewCSParser::Note_middle, i);
}


size_t NmrViewCSParser::Shift_listContext::getRuleIndex() const {
  return NmrViewCSParser::RuleShift_list;
}


std::any NmrViewCSParser::Shift_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewCSParserVisitor*>(visitor))
    return parserVisitor->visitShift_list(this);
  else
    return visitor->visitChildren(this);
}

NmrViewCSParser::Shift_listContext* NmrViewCSParser::shift_list() {
  Shift_listContext *_localctx = _tracker.createInstance<Shift_listContext>(_ctx, getState());
  enterRule(_localctx, 14, NmrViewCSParser::RuleShift_list);
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
    setState(74);
    match(NmrViewCSParser::Simple_name);
    setState(75);
    match(NmrViewCSParser::Float);
    setState(85);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case NmrViewCSParser::Single_note: {
        setState(76);
        match(NmrViewCSParser::Single_note);
        break;
      }

      case NmrViewCSParser::Note_begin: {
        setState(77);
        match(NmrViewCSParser::Note_begin);
        setState(81);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == NmrViewCSParser::Note_middle) {
          setState(78);
          match(NmrViewCSParser::Note_middle);
          setState(83);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        setState(84);
        match(NmrViewCSParser::Note_end);
        break;
      }

      case NmrViewCSParser::RETURN: {
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

void NmrViewCSParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  nmrviewcsparserParserInitialize();
#else
  ::antlr4::internal::call_once(nmrviewcsparserParserOnceFlag, nmrviewcsparserParserInitialize);
#endif
}
