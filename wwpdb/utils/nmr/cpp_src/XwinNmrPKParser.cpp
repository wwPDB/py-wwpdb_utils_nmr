
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XwinNmrPKParser.g4 by ANTLR 4.13.0


#include "XwinNmrPKParserVisitor.h"

#include "XwinNmrPKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct XwinNmrPKParserStaticData final {
  XwinNmrPKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  XwinNmrPKParserStaticData(const XwinNmrPKParserStaticData&) = delete;
  XwinNmrPKParserStaticData(XwinNmrPKParserStaticData&&) = delete;
  XwinNmrPKParserStaticData& operator=(const XwinNmrPKParserStaticData&) = delete;
  XwinNmrPKParserStaticData& operator=(XwinNmrPKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag xwinnmrpkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
XwinNmrPKParserStaticData *xwinnmrpkparserParserStaticData = nullptr;

void xwinnmrpkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (xwinnmrpkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(xwinnmrpkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<XwinNmrPKParserStaticData>(
    std::vector<std::string>{
      "xwinnmr_pk", "comment", "dimension", "peak_2d", "peak_3d", "peak_4d"
    },
    std::vector<std::string>{
      "", "'# PEAKLIST_DIMENSION'"
    },
    std::vector<std::string>{
      "", "Num_of_dim", "Integer", "Float", "COMMENT", "SPACE", "RETURN", 
      "SECTION_COMMENT", "LINE_COMMENT", "Annotation", "Integer_ND", "SPACE_ND", 
      "RETURN_ND", "Any_name", "SPACE_CM", "RETURN_CM"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,15,111,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,3,0,14,
  	8,0,1,0,1,0,1,0,4,0,19,8,0,11,0,12,0,20,1,0,4,0,24,8,0,11,0,12,0,25,1,
  	0,4,0,29,8,0,11,0,12,0,30,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
  	1,1,5,1,43,8,1,10,1,12,1,46,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
  	3,1,3,1,3,1,3,3,3,61,8,3,1,3,5,3,64,8,3,10,3,12,3,67,9,3,1,3,1,3,1,4,
  	1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,80,8,4,1,4,5,4,83,8,4,10,4,12,4,86,
  	9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,101,8,5,1,
  	5,5,5,104,8,5,10,5,12,5,107,9,5,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,2,1,
  	1,15,15,1,1,6,6,121,0,13,1,0,0,0,2,40,1,0,0,0,4,49,1,0,0,0,6,53,1,0,0,
  	0,8,70,1,0,0,0,10,89,1,0,0,0,12,14,5,6,0,0,13,12,1,0,0,0,13,14,1,0,0,
  	0,14,35,1,0,0,0,15,34,3,2,1,0,16,34,3,4,2,0,17,19,3,6,3,0,18,17,1,0,0,
  	0,19,20,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,34,1,0,0,0,22,24,3,8,4,
  	0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,34,1,0,0,
  	0,27,29,3,10,5,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,
  	0,0,31,34,1,0,0,0,32,34,5,6,0,0,33,15,1,0,0,0,33,16,1,0,0,0,33,18,1,0,
  	0,0,33,23,1,0,0,0,33,28,1,0,0,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,
  	0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,0,0,1,39,1,1,0,
  	0,0,40,44,5,4,0,0,41,43,5,13,0,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,
  	0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,47,48,7,0,0,0,48,3,1,
  	0,0,0,49,50,5,1,0,0,50,51,5,10,0,0,51,52,5,12,0,0,52,5,1,0,0,0,53,54,
  	5,2,0,0,54,55,5,3,0,0,55,56,5,3,0,0,56,57,5,3,0,0,57,58,5,3,0,0,58,60,
  	5,3,0,0,59,61,5,3,0,0,60,59,1,0,0,0,60,61,1,0,0,0,61,65,1,0,0,0,62,64,
  	5,9,0,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,
  	1,0,0,0,67,65,1,0,0,0,68,69,7,1,0,0,69,7,1,0,0,0,70,71,5,2,0,0,71,72,
  	5,3,0,0,72,73,5,3,0,0,73,74,5,3,0,0,74,75,5,3,0,0,75,76,5,3,0,0,76,77,
  	5,3,0,0,77,79,5,3,0,0,78,80,5,3,0,0,79,78,1,0,0,0,79,80,1,0,0,0,80,84,
  	1,0,0,0,81,83,5,9,0,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,
  	1,0,0,0,85,87,1,0,0,0,86,84,1,0,0,0,87,88,7,1,0,0,88,9,1,0,0,0,89,90,
  	5,2,0,0,90,91,5,3,0,0,91,92,5,3,0,0,92,93,5,3,0,0,93,94,5,3,0,0,94,95,
  	5,3,0,0,95,96,5,3,0,0,96,97,5,3,0,0,97,98,5,3,0,0,98,100,5,3,0,0,99,101,
  	5,3,0,0,100,99,1,0,0,0,100,101,1,0,0,0,101,105,1,0,0,0,102,104,5,9,0,
  	0,103,102,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,
  	108,1,0,0,0,107,105,1,0,0,0,108,109,7,1,0,0,109,11,1,0,0,0,13,13,20,25,
  	30,33,35,44,60,65,79,84,100,105
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  xwinnmrpkparserParserStaticData = staticData.release();
}

}

XwinNmrPKParser::XwinNmrPKParser(TokenStream *input) : XwinNmrPKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

XwinNmrPKParser::XwinNmrPKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  XwinNmrPKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *xwinnmrpkparserParserStaticData->atn, xwinnmrpkparserParserStaticData->decisionToDFA, xwinnmrpkparserParserStaticData->sharedContextCache, options);
}

XwinNmrPKParser::~XwinNmrPKParser() {
  delete _interpreter;
}

const atn::ATN& XwinNmrPKParser::getATN() const {
  return *xwinnmrpkparserParserStaticData->atn;
}

std::string XwinNmrPKParser::getGrammarFileName() const {
  return "XwinNmrPKParser.g4";
}

const std::vector<std::string>& XwinNmrPKParser::getRuleNames() const {
  return xwinnmrpkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& XwinNmrPKParser::getVocabulary() const {
  return xwinnmrpkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView XwinNmrPKParser::getSerializedATN() const {
  return xwinnmrpkparserParserStaticData->serializedATN;
}


//----------------- Xwinnmr_pkContext ------------------------------------------------------------------

XwinNmrPKParser::Xwinnmr_pkContext::Xwinnmr_pkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XwinNmrPKParser::Xwinnmr_pkContext::EOF() {
  return getToken(XwinNmrPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> XwinNmrPKParser::Xwinnmr_pkContext::RETURN() {
  return getTokens(XwinNmrPKParser::RETURN);
}

tree::TerminalNode* XwinNmrPKParser::Xwinnmr_pkContext::RETURN(size_t i) {
  return getToken(XwinNmrPKParser::RETURN, i);
}

std::vector<XwinNmrPKParser::CommentContext *> XwinNmrPKParser::Xwinnmr_pkContext::comment() {
  return getRuleContexts<XwinNmrPKParser::CommentContext>();
}

XwinNmrPKParser::CommentContext* XwinNmrPKParser::Xwinnmr_pkContext::comment(size_t i) {
  return getRuleContext<XwinNmrPKParser::CommentContext>(i);
}

std::vector<XwinNmrPKParser::DimensionContext *> XwinNmrPKParser::Xwinnmr_pkContext::dimension() {
  return getRuleContexts<XwinNmrPKParser::DimensionContext>();
}

XwinNmrPKParser::DimensionContext* XwinNmrPKParser::Xwinnmr_pkContext::dimension(size_t i) {
  return getRuleContext<XwinNmrPKParser::DimensionContext>(i);
}

std::vector<XwinNmrPKParser::Peak_2dContext *> XwinNmrPKParser::Xwinnmr_pkContext::peak_2d() {
  return getRuleContexts<XwinNmrPKParser::Peak_2dContext>();
}

XwinNmrPKParser::Peak_2dContext* XwinNmrPKParser::Xwinnmr_pkContext::peak_2d(size_t i) {
  return getRuleContext<XwinNmrPKParser::Peak_2dContext>(i);
}

std::vector<XwinNmrPKParser::Peak_3dContext *> XwinNmrPKParser::Xwinnmr_pkContext::peak_3d() {
  return getRuleContexts<XwinNmrPKParser::Peak_3dContext>();
}

XwinNmrPKParser::Peak_3dContext* XwinNmrPKParser::Xwinnmr_pkContext::peak_3d(size_t i) {
  return getRuleContext<XwinNmrPKParser::Peak_3dContext>(i);
}

std::vector<XwinNmrPKParser::Peak_4dContext *> XwinNmrPKParser::Xwinnmr_pkContext::peak_4d() {
  return getRuleContexts<XwinNmrPKParser::Peak_4dContext>();
}

XwinNmrPKParser::Peak_4dContext* XwinNmrPKParser::Xwinnmr_pkContext::peak_4d(size_t i) {
  return getRuleContext<XwinNmrPKParser::Peak_4dContext>(i);
}


size_t XwinNmrPKParser::Xwinnmr_pkContext::getRuleIndex() const {
  return XwinNmrPKParser::RuleXwinnmr_pk;
}


std::any XwinNmrPKParser::Xwinnmr_pkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XwinNmrPKParserVisitor*>(visitor))
    return parserVisitor->visitXwinnmr_pk(this);
  else
    return visitor->visitChildren(this);
}

XwinNmrPKParser::Xwinnmr_pkContext* XwinNmrPKParser::xwinnmr_pk() {
  Xwinnmr_pkContext *_localctx = _tracker.createInstance<Xwinnmr_pkContext>(_ctx, getState());
  enterRule(_localctx, 0, XwinNmrPKParser::RuleXwinnmr_pk);
  size_t _la = 0;

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
    setState(13);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(12);
      match(XwinNmrPKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(35);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 86) != 0)) {
      setState(33);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx)) {
      case 1: {
        setState(15);
        comment();
        break;
      }

      case 2: {
        setState(16);
        dimension();
        break;
      }

      case 3: {
        setState(18); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(17);
                  peak_2d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(20); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 4: {
        setState(23); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(22);
                  peak_3d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(25); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 5: {
        setState(28); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(27);
                  peak_4d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(30); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 6: {
        setState(32);
        match(XwinNmrPKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(37);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(38);
    match(XwinNmrPKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CommentContext ------------------------------------------------------------------

XwinNmrPKParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XwinNmrPKParser::CommentContext::COMMENT() {
  return getToken(XwinNmrPKParser::COMMENT, 0);
}

tree::TerminalNode* XwinNmrPKParser::CommentContext::RETURN_CM() {
  return getToken(XwinNmrPKParser::RETURN_CM, 0);
}

tree::TerminalNode* XwinNmrPKParser::CommentContext::EOF() {
  return getToken(XwinNmrPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> XwinNmrPKParser::CommentContext::Any_name() {
  return getTokens(XwinNmrPKParser::Any_name);
}

tree::TerminalNode* XwinNmrPKParser::CommentContext::Any_name(size_t i) {
  return getToken(XwinNmrPKParser::Any_name, i);
}


size_t XwinNmrPKParser::CommentContext::getRuleIndex() const {
  return XwinNmrPKParser::RuleComment;
}


std::any XwinNmrPKParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XwinNmrPKParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

XwinNmrPKParser::CommentContext* XwinNmrPKParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 2, XwinNmrPKParser::RuleComment);
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
    setState(40);
    match(XwinNmrPKParser::COMMENT);
    setState(44);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == XwinNmrPKParser::Any_name) {
      setState(41);
      match(XwinNmrPKParser::Any_name);
      setState(46);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(47);
    _la = _input->LA(1);
    if (!(_la == XwinNmrPKParser::EOF

    || _la == XwinNmrPKParser::RETURN_CM)) {
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

//----------------- DimensionContext ------------------------------------------------------------------

XwinNmrPKParser::DimensionContext::DimensionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XwinNmrPKParser::DimensionContext::Num_of_dim() {
  return getToken(XwinNmrPKParser::Num_of_dim, 0);
}

tree::TerminalNode* XwinNmrPKParser::DimensionContext::Integer_ND() {
  return getToken(XwinNmrPKParser::Integer_ND, 0);
}

tree::TerminalNode* XwinNmrPKParser::DimensionContext::RETURN_ND() {
  return getToken(XwinNmrPKParser::RETURN_ND, 0);
}


size_t XwinNmrPKParser::DimensionContext::getRuleIndex() const {
  return XwinNmrPKParser::RuleDimension;
}


std::any XwinNmrPKParser::DimensionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XwinNmrPKParserVisitor*>(visitor))
    return parserVisitor->visitDimension(this);
  else
    return visitor->visitChildren(this);
}

XwinNmrPKParser::DimensionContext* XwinNmrPKParser::dimension() {
  DimensionContext *_localctx = _tracker.createInstance<DimensionContext>(_ctx, getState());
  enterRule(_localctx, 4, XwinNmrPKParser::RuleDimension);

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
    match(XwinNmrPKParser::Num_of_dim);
    setState(50);
    match(XwinNmrPKParser::Integer_ND);
    setState(51);
    match(XwinNmrPKParser::RETURN_ND);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_2dContext ------------------------------------------------------------------

XwinNmrPKParser::Peak_2dContext::Peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XwinNmrPKParser::Peak_2dContext::Integer() {
  return getToken(XwinNmrPKParser::Integer, 0);
}

std::vector<tree::TerminalNode *> XwinNmrPKParser::Peak_2dContext::Float() {
  return getTokens(XwinNmrPKParser::Float);
}

tree::TerminalNode* XwinNmrPKParser::Peak_2dContext::Float(size_t i) {
  return getToken(XwinNmrPKParser::Float, i);
}

tree::TerminalNode* XwinNmrPKParser::Peak_2dContext::RETURN() {
  return getToken(XwinNmrPKParser::RETURN, 0);
}

tree::TerminalNode* XwinNmrPKParser::Peak_2dContext::EOF() {
  return getToken(XwinNmrPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> XwinNmrPKParser::Peak_2dContext::Annotation() {
  return getTokens(XwinNmrPKParser::Annotation);
}

tree::TerminalNode* XwinNmrPKParser::Peak_2dContext::Annotation(size_t i) {
  return getToken(XwinNmrPKParser::Annotation, i);
}


size_t XwinNmrPKParser::Peak_2dContext::getRuleIndex() const {
  return XwinNmrPKParser::RulePeak_2d;
}


std::any XwinNmrPKParser::Peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XwinNmrPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d(this);
  else
    return visitor->visitChildren(this);
}

XwinNmrPKParser::Peak_2dContext* XwinNmrPKParser::peak_2d() {
  Peak_2dContext *_localctx = _tracker.createInstance<Peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 6, XwinNmrPKParser::RulePeak_2d);
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
    setState(53);
    match(XwinNmrPKParser::Integer);
    setState(54);
    match(XwinNmrPKParser::Float);
    setState(55);
    match(XwinNmrPKParser::Float);
    setState(56);
    match(XwinNmrPKParser::Float);
    setState(57);
    match(XwinNmrPKParser::Float);
    setState(58);
    match(XwinNmrPKParser::Float);
    setState(60);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == XwinNmrPKParser::Float) {
      setState(59);
      match(XwinNmrPKParser::Float);
    }
    setState(65);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == XwinNmrPKParser::Annotation) {
      setState(62);
      match(XwinNmrPKParser::Annotation);
      setState(67);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(68);
    _la = _input->LA(1);
    if (!(_la == XwinNmrPKParser::EOF

    || _la == XwinNmrPKParser::RETURN)) {
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

//----------------- Peak_3dContext ------------------------------------------------------------------

XwinNmrPKParser::Peak_3dContext::Peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XwinNmrPKParser::Peak_3dContext::Integer() {
  return getToken(XwinNmrPKParser::Integer, 0);
}

std::vector<tree::TerminalNode *> XwinNmrPKParser::Peak_3dContext::Float() {
  return getTokens(XwinNmrPKParser::Float);
}

tree::TerminalNode* XwinNmrPKParser::Peak_3dContext::Float(size_t i) {
  return getToken(XwinNmrPKParser::Float, i);
}

tree::TerminalNode* XwinNmrPKParser::Peak_3dContext::RETURN() {
  return getToken(XwinNmrPKParser::RETURN, 0);
}

tree::TerminalNode* XwinNmrPKParser::Peak_3dContext::EOF() {
  return getToken(XwinNmrPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> XwinNmrPKParser::Peak_3dContext::Annotation() {
  return getTokens(XwinNmrPKParser::Annotation);
}

tree::TerminalNode* XwinNmrPKParser::Peak_3dContext::Annotation(size_t i) {
  return getToken(XwinNmrPKParser::Annotation, i);
}


size_t XwinNmrPKParser::Peak_3dContext::getRuleIndex() const {
  return XwinNmrPKParser::RulePeak_3d;
}


std::any XwinNmrPKParser::Peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XwinNmrPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d(this);
  else
    return visitor->visitChildren(this);
}

XwinNmrPKParser::Peak_3dContext* XwinNmrPKParser::peak_3d() {
  Peak_3dContext *_localctx = _tracker.createInstance<Peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 8, XwinNmrPKParser::RulePeak_3d);
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
    setState(70);
    match(XwinNmrPKParser::Integer);
    setState(71);
    match(XwinNmrPKParser::Float);
    setState(72);
    match(XwinNmrPKParser::Float);
    setState(73);
    match(XwinNmrPKParser::Float);
    setState(74);
    match(XwinNmrPKParser::Float);
    setState(75);
    match(XwinNmrPKParser::Float);
    setState(76);
    match(XwinNmrPKParser::Float);
    setState(77);
    match(XwinNmrPKParser::Float);
    setState(79);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == XwinNmrPKParser::Float) {
      setState(78);
      match(XwinNmrPKParser::Float);
    }
    setState(84);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == XwinNmrPKParser::Annotation) {
      setState(81);
      match(XwinNmrPKParser::Annotation);
      setState(86);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(87);
    _la = _input->LA(1);
    if (!(_la == XwinNmrPKParser::EOF

    || _la == XwinNmrPKParser::RETURN)) {
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

//----------------- Peak_4dContext ------------------------------------------------------------------

XwinNmrPKParser::Peak_4dContext::Peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XwinNmrPKParser::Peak_4dContext::Integer() {
  return getToken(XwinNmrPKParser::Integer, 0);
}

std::vector<tree::TerminalNode *> XwinNmrPKParser::Peak_4dContext::Float() {
  return getTokens(XwinNmrPKParser::Float);
}

tree::TerminalNode* XwinNmrPKParser::Peak_4dContext::Float(size_t i) {
  return getToken(XwinNmrPKParser::Float, i);
}

tree::TerminalNode* XwinNmrPKParser::Peak_4dContext::RETURN() {
  return getToken(XwinNmrPKParser::RETURN, 0);
}

tree::TerminalNode* XwinNmrPKParser::Peak_4dContext::EOF() {
  return getToken(XwinNmrPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> XwinNmrPKParser::Peak_4dContext::Annotation() {
  return getTokens(XwinNmrPKParser::Annotation);
}

tree::TerminalNode* XwinNmrPKParser::Peak_4dContext::Annotation(size_t i) {
  return getToken(XwinNmrPKParser::Annotation, i);
}


size_t XwinNmrPKParser::Peak_4dContext::getRuleIndex() const {
  return XwinNmrPKParser::RulePeak_4d;
}


std::any XwinNmrPKParser::Peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XwinNmrPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d(this);
  else
    return visitor->visitChildren(this);
}

XwinNmrPKParser::Peak_4dContext* XwinNmrPKParser::peak_4d() {
  Peak_4dContext *_localctx = _tracker.createInstance<Peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 10, XwinNmrPKParser::RulePeak_4d);
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
    setState(89);
    match(XwinNmrPKParser::Integer);
    setState(90);
    match(XwinNmrPKParser::Float);
    setState(91);
    match(XwinNmrPKParser::Float);
    setState(92);
    match(XwinNmrPKParser::Float);
    setState(93);
    match(XwinNmrPKParser::Float);
    setState(94);
    match(XwinNmrPKParser::Float);
    setState(95);
    match(XwinNmrPKParser::Float);
    setState(96);
    match(XwinNmrPKParser::Float);
    setState(97);
    match(XwinNmrPKParser::Float);
    setState(98);
    match(XwinNmrPKParser::Float);
    setState(100);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == XwinNmrPKParser::Float) {
      setState(99);
      match(XwinNmrPKParser::Float);
    }
    setState(105);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == XwinNmrPKParser::Annotation) {
      setState(102);
      match(XwinNmrPKParser::Annotation);
      setState(107);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(108);
    _la = _input->LA(1);
    if (!(_la == XwinNmrPKParser::EOF

    || _la == XwinNmrPKParser::RETURN)) {
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

void XwinNmrPKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  xwinnmrpkparserParserInitialize();
#else
  ::antlr4::internal::call_once(xwinnmrpkparserParserOnceFlag, xwinnmrpkparserParserInitialize);
#endif
}
