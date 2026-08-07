
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XMLParser.g4 by ANTLR 4.13.0


#include "XMLParserVisitor.h"

#include "XMLParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct XMLParserStaticData final {
  XMLParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  XMLParserStaticData(const XMLParserStaticData&) = delete;
  XMLParserStaticData(XMLParserStaticData&&) = delete;
  XMLParserStaticData& operator=(const XMLParserStaticData&) = delete;
  XMLParserStaticData& operator=(XMLParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag xmlparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
XMLParserStaticData *xmlparserParserStaticData = nullptr;

void xmlparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (xmlparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(xmlparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<XMLParserStaticData>(
    std::vector<std::string>{
      "document", "prolog", "content", "element", "reference", "attribute", 
      "chardata", "misc"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "'<'", "", "", "'>'", "", "'/>'", "'/'", 
      "'='"
    },
    std::vector<std::string>{
      "", "COMMENT", "CDATA", "DTD", "EntityRef", "CharRef", "SEA_WS", "OPEN", 
      "XMLDeclOpen", "TEXT", "CLOSE", "SPECIAL_CLOSE", "SLASH_CLOSE", "SLASH", 
      "EQUALS", "STRING", "Name", "S", "PI"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,18,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,1,0,3,0,18,8,0,1,0,5,0,21,8,0,10,0,12,0,24,9,0,1,0,1,0,5,0,28,8,
  	0,10,0,12,0,31,9,0,4,0,33,8,0,11,0,12,0,34,1,0,1,0,1,1,1,1,5,1,41,8,1,
  	10,1,12,1,44,9,1,1,1,1,1,1,2,3,2,49,8,2,1,2,1,2,1,2,1,2,1,2,3,2,56,8,
  	2,1,2,3,2,59,8,2,5,2,61,8,2,10,2,12,2,64,9,2,1,3,1,3,1,3,5,3,69,8,3,10,
  	3,12,3,72,9,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,84,8,3,10,3,
  	12,3,87,9,3,1,3,3,3,90,8,3,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,
  	7,0,0,8,0,2,4,6,8,10,12,14,0,3,1,0,4,5,2,0,6,6,9,9,3,0,1,1,6,6,18,18,
  	108,0,32,1,0,0,0,2,38,1,0,0,0,4,48,1,0,0,0,6,89,1,0,0,0,8,91,1,0,0,0,
  	10,93,1,0,0,0,12,97,1,0,0,0,14,99,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,
  	17,18,1,0,0,0,18,22,1,0,0,0,19,21,3,14,7,0,20,19,1,0,0,0,21,24,1,0,0,
  	0,22,20,1,0,0,0,22,23,1,0,0,0,23,25,1,0,0,0,24,22,1,0,0,0,25,29,3,6,3,
  	0,26,28,3,14,7,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,
  	0,0,30,33,1,0,0,0,31,29,1,0,0,0,32,17,1,0,0,0,33,34,1,0,0,0,34,32,1,0,
  	0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,37,5,0,0,1,37,1,1,0,0,0,38,42,5,8,
  	0,0,39,41,3,10,5,0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,
  	0,0,0,43,45,1,0,0,0,44,42,1,0,0,0,45,46,5,11,0,0,46,3,1,0,0,0,47,49,3,
  	12,6,0,48,47,1,0,0,0,48,49,1,0,0,0,49,62,1,0,0,0,50,56,3,6,3,0,51,56,
  	3,8,4,0,52,56,5,2,0,0,53,56,5,18,0,0,54,56,5,1,0,0,55,50,1,0,0,0,55,51,
  	1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,58,1,0,0,0,57,59,
  	3,12,6,0,58,57,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,55,1,0,0,0,61,64,
  	1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,5,1,0,0,0,64,62,1,0,0,0,65,66,
  	5,7,0,0,66,70,5,16,0,0,67,69,3,10,5,0,68,67,1,0,0,0,69,72,1,0,0,0,70,
  	68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,70,1,0,0,0,73,74,5,10,0,0,74,
  	75,3,4,2,0,75,76,5,7,0,0,76,77,5,13,0,0,77,78,5,16,0,0,78,79,5,10,0,0,
  	79,90,1,0,0,0,80,81,5,7,0,0,81,85,5,16,0,0,82,84,3,10,5,0,83,82,1,0,0,
  	0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,
  	0,88,90,5,12,0,0,89,65,1,0,0,0,89,80,1,0,0,0,90,7,1,0,0,0,91,92,7,0,0,
  	0,92,9,1,0,0,0,93,94,5,16,0,0,94,95,5,14,0,0,95,96,5,15,0,0,96,11,1,0,
  	0,0,97,98,7,1,0,0,98,13,1,0,0,0,99,100,7,2,0,0,100,15,1,0,0,0,12,17,22,
  	29,34,42,48,55,58,62,70,85,89
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  xmlparserParserStaticData = staticData.release();
}

}

XMLParser::XMLParser(TokenStream *input) : XMLParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

XMLParser::XMLParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  XMLParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *xmlparserParserStaticData->atn, xmlparserParserStaticData->decisionToDFA, xmlparserParserStaticData->sharedContextCache, options);
}

XMLParser::~XMLParser() {
  delete _interpreter;
}

const atn::ATN& XMLParser::getATN() const {
  return *xmlparserParserStaticData->atn;
}

std::string XMLParser::getGrammarFileName() const {
  return "XMLParser.g4";
}

const std::vector<std::string>& XMLParser::getRuleNames() const {
  return xmlparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& XMLParser::getVocabulary() const {
  return xmlparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView XMLParser::getSerializedATN() const {
  return xmlparserParserStaticData->serializedATN;
}


//----------------- DocumentContext ------------------------------------------------------------------

XMLParser::DocumentContext::DocumentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XMLParser::DocumentContext::EOF() {
  return getToken(XMLParser::EOF, 0);
}

std::vector<XMLParser::ElementContext *> XMLParser::DocumentContext::element() {
  return getRuleContexts<XMLParser::ElementContext>();
}

XMLParser::ElementContext* XMLParser::DocumentContext::element(size_t i) {
  return getRuleContext<XMLParser::ElementContext>(i);
}

std::vector<XMLParser::PrologContext *> XMLParser::DocumentContext::prolog() {
  return getRuleContexts<XMLParser::PrologContext>();
}

XMLParser::PrologContext* XMLParser::DocumentContext::prolog(size_t i) {
  return getRuleContext<XMLParser::PrologContext>(i);
}

std::vector<XMLParser::MiscContext *> XMLParser::DocumentContext::misc() {
  return getRuleContexts<XMLParser::MiscContext>();
}

XMLParser::MiscContext* XMLParser::DocumentContext::misc(size_t i) {
  return getRuleContext<XMLParser::MiscContext>(i);
}


size_t XMLParser::DocumentContext::getRuleIndex() const {
  return XMLParser::RuleDocument;
}


std::any XMLParser::DocumentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XMLParserVisitor*>(visitor))
    return parserVisitor->visitDocument(this);
  else
    return visitor->visitChildren(this);
}

XMLParser::DocumentContext* XMLParser::document() {
  DocumentContext *_localctx = _tracker.createInstance<DocumentContext>(_ctx, getState());
  enterRule(_localctx, 0, XMLParser::RuleDocument);
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
    setState(32); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(17);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == XMLParser::XMLDeclOpen) {
        setState(16);
        prolog();
      }
      setState(22);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while ((((_la & ~ 0x3fULL) == 0) &&
        ((1ULL << _la) & 262210) != 0)) {
        setState(19);
        misc();
        setState(24);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(25);
      element();
      setState(29);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
      while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
        if (alt == 1) {
          setState(26);
          misc(); 
        }
        setState(31);
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
      }
      setState(34); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 262594) != 0));
    setState(36);
    match(XMLParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- PrologContext ------------------------------------------------------------------

XMLParser::PrologContext::PrologContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XMLParser::PrologContext::XMLDeclOpen() {
  return getToken(XMLParser::XMLDeclOpen, 0);
}

tree::TerminalNode* XMLParser::PrologContext::SPECIAL_CLOSE() {
  return getToken(XMLParser::SPECIAL_CLOSE, 0);
}

std::vector<XMLParser::AttributeContext *> XMLParser::PrologContext::attribute() {
  return getRuleContexts<XMLParser::AttributeContext>();
}

XMLParser::AttributeContext* XMLParser::PrologContext::attribute(size_t i) {
  return getRuleContext<XMLParser::AttributeContext>(i);
}


size_t XMLParser::PrologContext::getRuleIndex() const {
  return XMLParser::RuleProlog;
}


std::any XMLParser::PrologContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XMLParserVisitor*>(visitor))
    return parserVisitor->visitProlog(this);
  else
    return visitor->visitChildren(this);
}

XMLParser::PrologContext* XMLParser::prolog() {
  PrologContext *_localctx = _tracker.createInstance<PrologContext>(_ctx, getState());
  enterRule(_localctx, 2, XMLParser::RuleProlog);
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
    match(XMLParser::XMLDeclOpen);
    setState(42);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == XMLParser::Name) {
      setState(39);
      attribute();
      setState(44);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(45);
    match(XMLParser::SPECIAL_CLOSE);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ContentContext ------------------------------------------------------------------

XMLParser::ContentContext::ContentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<XMLParser::ChardataContext *> XMLParser::ContentContext::chardata() {
  return getRuleContexts<XMLParser::ChardataContext>();
}

XMLParser::ChardataContext* XMLParser::ContentContext::chardata(size_t i) {
  return getRuleContext<XMLParser::ChardataContext>(i);
}

std::vector<XMLParser::ElementContext *> XMLParser::ContentContext::element() {
  return getRuleContexts<XMLParser::ElementContext>();
}

XMLParser::ElementContext* XMLParser::ContentContext::element(size_t i) {
  return getRuleContext<XMLParser::ElementContext>(i);
}

std::vector<XMLParser::ReferenceContext *> XMLParser::ContentContext::reference() {
  return getRuleContexts<XMLParser::ReferenceContext>();
}

XMLParser::ReferenceContext* XMLParser::ContentContext::reference(size_t i) {
  return getRuleContext<XMLParser::ReferenceContext>(i);
}

std::vector<tree::TerminalNode *> XMLParser::ContentContext::CDATA() {
  return getTokens(XMLParser::CDATA);
}

tree::TerminalNode* XMLParser::ContentContext::CDATA(size_t i) {
  return getToken(XMLParser::CDATA, i);
}

std::vector<tree::TerminalNode *> XMLParser::ContentContext::PI() {
  return getTokens(XMLParser::PI);
}

tree::TerminalNode* XMLParser::ContentContext::PI(size_t i) {
  return getToken(XMLParser::PI, i);
}

std::vector<tree::TerminalNode *> XMLParser::ContentContext::COMMENT() {
  return getTokens(XMLParser::COMMENT);
}

tree::TerminalNode* XMLParser::ContentContext::COMMENT(size_t i) {
  return getToken(XMLParser::COMMENT, i);
}


size_t XMLParser::ContentContext::getRuleIndex() const {
  return XMLParser::RuleContent;
}


std::any XMLParser::ContentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XMLParserVisitor*>(visitor))
    return parserVisitor->visitContent(this);
  else
    return visitor->visitChildren(this);
}

XMLParser::ContentContext* XMLParser::content() {
  ContentContext *_localctx = _tracker.createInstance<ContentContext>(_ctx, getState());
  enterRule(_localctx, 4, XMLParser::RuleContent);
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
    setState(48);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == XMLParser::SEA_WS

    || _la == XMLParser::TEXT) {
      setState(47);
      chardata();
    }
    setState(62);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(55);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case XMLParser::OPEN: {
            setState(50);
            element();
            break;
          }

          case XMLParser::EntityRef:
          case XMLParser::CharRef: {
            setState(51);
            reference();
            break;
          }

          case XMLParser::CDATA: {
            setState(52);
            match(XMLParser::CDATA);
            break;
          }

          case XMLParser::PI: {
            setState(53);
            match(XMLParser::PI);
            break;
          }

          case XMLParser::COMMENT: {
            setState(54);
            match(XMLParser::COMMENT);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        setState(58);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == XMLParser::SEA_WS

        || _la == XMLParser::TEXT) {
          setState(57);
          chardata();
        } 
      }
      setState(64);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ElementContext ------------------------------------------------------------------

XMLParser::ElementContext::ElementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> XMLParser::ElementContext::OPEN() {
  return getTokens(XMLParser::OPEN);
}

tree::TerminalNode* XMLParser::ElementContext::OPEN(size_t i) {
  return getToken(XMLParser::OPEN, i);
}

std::vector<tree::TerminalNode *> XMLParser::ElementContext::Name() {
  return getTokens(XMLParser::Name);
}

tree::TerminalNode* XMLParser::ElementContext::Name(size_t i) {
  return getToken(XMLParser::Name, i);
}

std::vector<tree::TerminalNode *> XMLParser::ElementContext::CLOSE() {
  return getTokens(XMLParser::CLOSE);
}

tree::TerminalNode* XMLParser::ElementContext::CLOSE(size_t i) {
  return getToken(XMLParser::CLOSE, i);
}

XMLParser::ContentContext* XMLParser::ElementContext::content() {
  return getRuleContext<XMLParser::ContentContext>(0);
}

tree::TerminalNode* XMLParser::ElementContext::SLASH() {
  return getToken(XMLParser::SLASH, 0);
}

std::vector<XMLParser::AttributeContext *> XMLParser::ElementContext::attribute() {
  return getRuleContexts<XMLParser::AttributeContext>();
}

XMLParser::AttributeContext* XMLParser::ElementContext::attribute(size_t i) {
  return getRuleContext<XMLParser::AttributeContext>(i);
}

tree::TerminalNode* XMLParser::ElementContext::SLASH_CLOSE() {
  return getToken(XMLParser::SLASH_CLOSE, 0);
}


size_t XMLParser::ElementContext::getRuleIndex() const {
  return XMLParser::RuleElement;
}


std::any XMLParser::ElementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XMLParserVisitor*>(visitor))
    return parserVisitor->visitElement(this);
  else
    return visitor->visitChildren(this);
}

XMLParser::ElementContext* XMLParser::element() {
  ElementContext *_localctx = _tracker.createInstance<ElementContext>(_ctx, getState());
  enterRule(_localctx, 6, XMLParser::RuleElement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(89);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(65);
      match(XMLParser::OPEN);
      setState(66);
      match(XMLParser::Name);
      setState(70);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == XMLParser::Name) {
        setState(67);
        attribute();
        setState(72);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(73);
      match(XMLParser::CLOSE);
      setState(74);
      content();
      setState(75);
      match(XMLParser::OPEN);
      setState(76);
      match(XMLParser::SLASH);
      setState(77);
      match(XMLParser::Name);
      setState(78);
      match(XMLParser::CLOSE);
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(80);
      match(XMLParser::OPEN);
      setState(81);
      match(XMLParser::Name);
      setState(85);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == XMLParser::Name) {
        setState(82);
        attribute();
        setState(87);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(88);
      match(XMLParser::SLASH_CLOSE);
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

//----------------- ReferenceContext ------------------------------------------------------------------

XMLParser::ReferenceContext::ReferenceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XMLParser::ReferenceContext::EntityRef() {
  return getToken(XMLParser::EntityRef, 0);
}

tree::TerminalNode* XMLParser::ReferenceContext::CharRef() {
  return getToken(XMLParser::CharRef, 0);
}


size_t XMLParser::ReferenceContext::getRuleIndex() const {
  return XMLParser::RuleReference;
}


std::any XMLParser::ReferenceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XMLParserVisitor*>(visitor))
    return parserVisitor->visitReference(this);
  else
    return visitor->visitChildren(this);
}

XMLParser::ReferenceContext* XMLParser::reference() {
  ReferenceContext *_localctx = _tracker.createInstance<ReferenceContext>(_ctx, getState());
  enterRule(_localctx, 8, XMLParser::RuleReference);
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
    setState(91);
    _la = _input->LA(1);
    if (!(_la == XMLParser::EntityRef

    || _la == XMLParser::CharRef)) {
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

//----------------- AttributeContext ------------------------------------------------------------------

XMLParser::AttributeContext::AttributeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XMLParser::AttributeContext::Name() {
  return getToken(XMLParser::Name, 0);
}

tree::TerminalNode* XMLParser::AttributeContext::EQUALS() {
  return getToken(XMLParser::EQUALS, 0);
}

tree::TerminalNode* XMLParser::AttributeContext::STRING() {
  return getToken(XMLParser::STRING, 0);
}


size_t XMLParser::AttributeContext::getRuleIndex() const {
  return XMLParser::RuleAttribute;
}


std::any XMLParser::AttributeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XMLParserVisitor*>(visitor))
    return parserVisitor->visitAttribute(this);
  else
    return visitor->visitChildren(this);
}

XMLParser::AttributeContext* XMLParser::attribute() {
  AttributeContext *_localctx = _tracker.createInstance<AttributeContext>(_ctx, getState());
  enterRule(_localctx, 10, XMLParser::RuleAttribute);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(93);
    match(XMLParser::Name);
    setState(94);
    match(XMLParser::EQUALS);
    setState(95);
    match(XMLParser::STRING);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ChardataContext ------------------------------------------------------------------

XMLParser::ChardataContext::ChardataContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XMLParser::ChardataContext::TEXT() {
  return getToken(XMLParser::TEXT, 0);
}

tree::TerminalNode* XMLParser::ChardataContext::SEA_WS() {
  return getToken(XMLParser::SEA_WS, 0);
}


size_t XMLParser::ChardataContext::getRuleIndex() const {
  return XMLParser::RuleChardata;
}


std::any XMLParser::ChardataContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XMLParserVisitor*>(visitor))
    return parserVisitor->visitChardata(this);
  else
    return visitor->visitChildren(this);
}

XMLParser::ChardataContext* XMLParser::chardata() {
  ChardataContext *_localctx = _tracker.createInstance<ChardataContext>(_ctx, getState());
  enterRule(_localctx, 12, XMLParser::RuleChardata);
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
    setState(97);
    _la = _input->LA(1);
    if (!(_la == XMLParser::SEA_WS

    || _la == XMLParser::TEXT)) {
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

//----------------- MiscContext ------------------------------------------------------------------

XMLParser::MiscContext::MiscContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* XMLParser::MiscContext::COMMENT() {
  return getToken(XMLParser::COMMENT, 0);
}

tree::TerminalNode* XMLParser::MiscContext::PI() {
  return getToken(XMLParser::PI, 0);
}

tree::TerminalNode* XMLParser::MiscContext::SEA_WS() {
  return getToken(XMLParser::SEA_WS, 0);
}


size_t XMLParser::MiscContext::getRuleIndex() const {
  return XMLParser::RuleMisc;
}


std::any XMLParser::MiscContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<XMLParserVisitor*>(visitor))
    return parserVisitor->visitMisc(this);
  else
    return visitor->visitChildren(this);
}

XMLParser::MiscContext* XMLParser::misc() {
  MiscContext *_localctx = _tracker.createInstance<MiscContext>(_ctx, getState());
  enterRule(_localctx, 14, XMLParser::RuleMisc);
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
    setState(99);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 262210) != 0))) {
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

void XMLParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  xmlparserParserInitialize();
#else
  ::antlr4::internal::call_once(xmlparserParserOnceFlag, xmlparserParserInitialize);
#endif
}
