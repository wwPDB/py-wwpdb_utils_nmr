
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XeasyPROTParser.g4 by ANTLR 4.13.0


#include "XeasyPROTParserVisitor.h"

#include "XeasyPROTParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct XeasyPROTParserStaticData final {
  XeasyPROTParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  XeasyPROTParserStaticData(const XeasyPROTParserStaticData&) = delete;
  XeasyPROTParserStaticData(XeasyPROTParserStaticData&&) = delete;
  XeasyPROTParserStaticData& operator=(const XeasyPROTParserStaticData&) = delete;
  XeasyPROTParserStaticData& operator=(XeasyPROTParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag xeasyprotparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
XeasyPROTParserStaticData *xeasyprotparserParserStaticData = nullptr;

void xeasyprotparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (xeasyprotparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(xeasyprotparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<XeasyPROTParserStaticData>(
    std::vector<std::string>{
      "xeasy_prot", "prot", "residue"
    },
    std::vector<std::string>{
    },
    std::vector<std::string>{
      "", "Integer", "Float", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
      "Simple_name", "SPACE", "RETURN", "ENCLOSE_COMMENT", "SECTION_COMMENT", 
      "LINE_COMMENT"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,11,33,2,0,7,0,2,1,7,1,2,2,7,2,1,0,3,0,8,8,0,1,0,4,0,11,8,0,11,0,12,
  	0,12,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
  	3,1,29,8,1,1,2,1,2,1,2,0,0,3,0,2,4,0,2,1,1,8,8,2,0,1,1,6,6,33,0,7,1,0,
  	0,0,2,22,1,0,0,0,4,30,1,0,0,0,6,8,5,8,0,0,7,6,1,0,0,0,7,8,1,0,0,0,8,10,
  	1,0,0,0,9,11,3,2,1,0,10,9,1,0,0,0,11,12,1,0,0,0,12,10,1,0,0,0,12,13,1,
  	0,0,0,13,17,1,0,0,0,14,16,5,8,0,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,
  	0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,
  	0,0,0,22,23,5,1,0,0,23,24,5,2,0,0,24,25,5,2,0,0,25,26,5,6,0,0,26,28,3,
  	4,2,0,27,29,7,0,0,0,28,27,1,0,0,0,28,29,1,0,0,0,29,3,1,0,0,0,30,31,7,
  	1,0,0,31,5,1,0,0,0,4,7,12,17,28
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  xeasyprotparserParserStaticData = staticData.release();
}

}

XeasyPROTParser::XeasyPROTParser(TokenStream *input) : XeasyPROTParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

XeasyPROTParser::XeasyPROTParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  XeasyPROTParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *xeasyprotparserParserStaticData->atn, xeasyprotparserParserStaticData->decisionToDFA, xeasyprotparserParserStaticData->sharedContextCache, options);
}

XeasyPROTParser::~XeasyPROTParser() {
  delete _interpreter;
}

const atn::ATN& XeasyPROTParser::getATN() const {
  return *xeasyprotparserParserStaticData->atn;
}

std::string XeasyPROTParser::getGrammarFileName() const {
  return "XeasyPROTParser.g4";
}

const std::vector<std::string>& XeasyPROTParser::getRuleNames() const {
  return xeasyprotparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& XeasyPROTParser::getVocabulary() const {
  return xeasyprotparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView XeasyPROTParser::getSerializedATN() const {
  return xeasyprotparserParserStaticData->serializedATN;
}


//----------------- Xeasy_protContext ------------------------------------------------------------------

XeasyPROTParser::Xeasy_protContext::Xeasy_protContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPROTParser::Xeasy_protContext::EOF() {
  return getToken(XeasyPROTParser::EOF, 0);
}

std::vector<tree::TerminalNode *> XeasyPROTParser::Xeasy_protContext::RETURN() {
  return getTokens(XeasyPROTParser::RETURN);
}

tree::TerminalNode* XeasyPROTParser::Xeasy_protContext::RETURN(size_t i) {
  return getToken(XeasyPROTParser::RETURN, i);
}

std::vector<XeasyPROTParser::ProtContext *> XeasyPROTParser::Xeasy_protContext::prot() {
  return getRuleContexts<XeasyPROTParser::ProtContext>();
}

XeasyPROTParser::ProtContext* XeasyPROTParser::Xeasy_protContext::prot(size_t i) {
  return getRuleContext<XeasyPROTParser::ProtContext>(i);
}


size_t XeasyPROTParser::Xeasy_protContext::getRuleIndex() const {
  return XeasyPROTParser::RuleXeasy_prot;
}


std::any XeasyPROTParser::Xeasy_protContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPROTParserVisitor*>(visitor))
    return parserVisitor->visitXeasy_prot(this);
  else
    return visitor->visitChildren(this);
}

XeasyPROTParser::Xeasy_protContext* XeasyPROTParser::xeasy_prot() {
  Xeasy_protContext *_localctx = _tracker.createInstance<Xeasy_protContext>(_ctx, getState());
  enterRule(_localctx, 0, XeasyPROTParser::RuleXeasy_prot);
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
    if (_la == XeasyPROTParser::RETURN) {
      setState(6);
      match(XeasyPROTParser::RETURN);
    }
    setState(10); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(9);
      prot();
      setState(12); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == XeasyPROTParser::Integer);
    setState(17);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == XeasyPROTParser::RETURN) {
      setState(14);
      match(XeasyPROTParser::RETURN);
      setState(19);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(20);
    match(XeasyPROTParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ProtContext ------------------------------------------------------------------

XeasyPROTParser::ProtContext::ProtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPROTParser::ProtContext::Integer() {
  return getToken(XeasyPROTParser::Integer, 0);
}

std::vector<tree::TerminalNode *> XeasyPROTParser::ProtContext::Float() {
  return getTokens(XeasyPROTParser::Float);
}

tree::TerminalNode* XeasyPROTParser::ProtContext::Float(size_t i) {
  return getToken(XeasyPROTParser::Float, i);
}

tree::TerminalNode* XeasyPROTParser::ProtContext::Simple_name() {
  return getToken(XeasyPROTParser::Simple_name, 0);
}

XeasyPROTParser::ResidueContext* XeasyPROTParser::ProtContext::residue() {
  return getRuleContext<XeasyPROTParser::ResidueContext>(0);
}

tree::TerminalNode* XeasyPROTParser::ProtContext::RETURN() {
  return getToken(XeasyPROTParser::RETURN, 0);
}

tree::TerminalNode* XeasyPROTParser::ProtContext::EOF() {
  return getToken(XeasyPROTParser::EOF, 0);
}


size_t XeasyPROTParser::ProtContext::getRuleIndex() const {
  return XeasyPROTParser::RuleProt;
}


std::any XeasyPROTParser::ProtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPROTParserVisitor*>(visitor))
    return parserVisitor->visitProt(this);
  else
    return visitor->visitChildren(this);
}

XeasyPROTParser::ProtContext* XeasyPROTParser::prot() {
  ProtContext *_localctx = _tracker.createInstance<ProtContext>(_ctx, getState());
  enterRule(_localctx, 2, XeasyPROTParser::RuleProt);
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
    match(XeasyPROTParser::Integer);
    setState(23);
    match(XeasyPROTParser::Float);
    setState(24);
    match(XeasyPROTParser::Float);
    setState(25);
    match(XeasyPROTParser::Simple_name);
    setState(26);
    residue();
    setState(28);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx)) {
    case 1: {
      setState(27);
      _la = _input->LA(1);
      if (!(_la == XeasyPROTParser::EOF

      || _la == XeasyPROTParser::RETURN)) {
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

//----------------- ResidueContext ------------------------------------------------------------------

XeasyPROTParser::ResidueContext::ResidueContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XeasyPROTParser::ResidueContext::Integer() {
  return getToken(XeasyPROTParser::Integer, 0);
}

tree::TerminalNode* XeasyPROTParser::ResidueContext::Simple_name() {
  return getToken(XeasyPROTParser::Simple_name, 0);
}


size_t XeasyPROTParser::ResidueContext::getRuleIndex() const {
  return XeasyPROTParser::RuleResidue;
}


std::any XeasyPROTParser::ResidueContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XeasyPROTParserVisitor*>(visitor))
    return parserVisitor->visitResidue(this);
  else
    return visitor->visitChildren(this);
}

XeasyPROTParser::ResidueContext* XeasyPROTParser::residue() {
  ResidueContext *_localctx = _tracker.createInstance<ResidueContext>(_ctx, getState());
  enterRule(_localctx, 4, XeasyPROTParser::RuleResidue);
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
    if (!(_la == XeasyPROTParser::Integer

    || _la == XeasyPROTParser::Simple_name)) {
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

void XeasyPROTParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  xeasyprotparserParserInitialize();
#else
  ::antlr4::internal::call_once(xeasyprotparserParserOnceFlag, xeasyprotparserParserInitialize);
#endif
}
