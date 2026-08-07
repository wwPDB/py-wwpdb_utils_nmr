
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CharmmCRDParser.g4 by ANTLR 4.13.0


#include "CharmmCRDParserVisitor.h"

#include "CharmmCRDParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct CharmmCRDParserStaticData final {
  CharmmCRDParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  CharmmCRDParserStaticData(const CharmmCRDParserStaticData&) = delete;
  CharmmCRDParserStaticData(CharmmCRDParserStaticData&&) = delete;
  CharmmCRDParserStaticData& operator=(const CharmmCRDParserStaticData&) = delete;
  CharmmCRDParserStaticData& operator=(CharmmCRDParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag charmmcrdparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
CharmmCRDParserStaticData *charmmcrdparserParserStaticData = nullptr;

void charmmcrdparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (charmmcrdparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(charmmcrdparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<CharmmCRDParserStaticData>(
    std::vector<std::string>{
      "charmm_crd", "comment", "coordinates", "atom_coordinate"
    },
    std::vector<std::string>{
      "", "", "", "", "", "'EXT'"
    },
    std::vector<std::string>{
      "", "Integer", "Float", "Double_quote_string", "COMMENT", "Ext", "Simple_name", 
      "SPACE", "CONTINUE", "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT", 
      "Any_name", "SPACE_CM", "RETURN_CM"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,14,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,5,0,11,8,0,10,0,12,
  	0,14,9,0,1,0,1,0,1,1,1,1,5,1,20,8,1,10,1,12,1,23,9,1,1,1,1,1,1,2,1,2,
  	1,2,4,2,30,8,2,11,2,12,2,31,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
  	3,1,3,0,0,4,0,2,4,6,0,1,1,1,14,14,44,0,12,1,0,0,0,2,17,1,0,0,0,4,26,1,
  	0,0,0,6,33,1,0,0,0,8,11,3,2,1,0,9,11,3,4,2,0,10,8,1,0,0,0,10,9,1,0,0,
  	0,11,14,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,15,1,0,0,0,14,12,1,0,0,
  	0,15,16,5,0,0,1,16,1,1,0,0,0,17,21,5,4,0,0,18,20,5,12,0,0,19,18,1,0,0,
  	0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,
  	0,24,25,7,0,0,0,25,3,1,0,0,0,26,27,5,1,0,0,27,29,5,5,0,0,28,30,3,6,3,
  	0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,5,1,0,0,
  	0,33,34,5,1,0,0,34,35,5,1,0,0,35,36,5,6,0,0,36,37,5,6,0,0,37,38,5,2,0,
  	0,38,39,5,2,0,0,39,40,5,2,0,0,40,41,5,6,0,0,41,42,5,1,0,0,42,43,5,2,0,
  	0,43,7,1,0,0,0,4,10,12,21,31
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  charmmcrdparserParserStaticData = staticData.release();
}

}

CharmmCRDParser::CharmmCRDParser(TokenStream *input) : CharmmCRDParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

CharmmCRDParser::CharmmCRDParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  CharmmCRDParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *charmmcrdparserParserStaticData->atn, charmmcrdparserParserStaticData->decisionToDFA, charmmcrdparserParserStaticData->sharedContextCache, options);
}

CharmmCRDParser::~CharmmCRDParser() {
  delete _interpreter;
}

const atn::ATN& CharmmCRDParser::getATN() const {
  return *charmmcrdparserParserStaticData->atn;
}

std::string CharmmCRDParser::getGrammarFileName() const {
  return "CharmmCRDParser.g4";
}

const std::vector<std::string>& CharmmCRDParser::getRuleNames() const {
  return charmmcrdparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& CharmmCRDParser::getVocabulary() const {
  return charmmcrdparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView CharmmCRDParser::getSerializedATN() const {
  return charmmcrdparserParserStaticData->serializedATN;
}


//----------------- Charmm_crdContext ------------------------------------------------------------------

CharmmCRDParser::Charmm_crdContext::Charmm_crdContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmCRDParser::Charmm_crdContext::EOF() {
  return getToken(CharmmCRDParser::EOF, 0);
}

std::vector<CharmmCRDParser::CommentContext *> CharmmCRDParser::Charmm_crdContext::comment() {
  return getRuleContexts<CharmmCRDParser::CommentContext>();
}

CharmmCRDParser::CommentContext* CharmmCRDParser::Charmm_crdContext::comment(size_t i) {
  return getRuleContext<CharmmCRDParser::CommentContext>(i);
}

std::vector<CharmmCRDParser::CoordinatesContext *> CharmmCRDParser::Charmm_crdContext::coordinates() {
  return getRuleContexts<CharmmCRDParser::CoordinatesContext>();
}

CharmmCRDParser::CoordinatesContext* CharmmCRDParser::Charmm_crdContext::coordinates(size_t i) {
  return getRuleContext<CharmmCRDParser::CoordinatesContext>(i);
}


size_t CharmmCRDParser::Charmm_crdContext::getRuleIndex() const {
  return CharmmCRDParser::RuleCharmm_crd;
}


std::any CharmmCRDParser::Charmm_crdContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmCRDParserVisitor*>(visitor))
    return parserVisitor->visitCharmm_crd(this);
  else
    return visitor->visitChildren(this);
}

CharmmCRDParser::Charmm_crdContext* CharmmCRDParser::charmm_crd() {
  Charmm_crdContext *_localctx = _tracker.createInstance<Charmm_crdContext>(_ctx, getState());
  enterRule(_localctx, 0, CharmmCRDParser::RuleCharmm_crd);
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
    setState(12);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CharmmCRDParser::Integer

    || _la == CharmmCRDParser::COMMENT) {
      setState(10);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case CharmmCRDParser::COMMENT: {
          setState(8);
          comment();
          break;
        }

        case CharmmCRDParser::Integer: {
          setState(9);
          coordinates();
          break;
        }

      default:
        throw NoViableAltException(this);
      }
      setState(14);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(15);
    match(CharmmCRDParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CommentContext ------------------------------------------------------------------

CharmmCRDParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmCRDParser::CommentContext::COMMENT() {
  return getToken(CharmmCRDParser::COMMENT, 0);
}

tree::TerminalNode* CharmmCRDParser::CommentContext::RETURN_CM() {
  return getToken(CharmmCRDParser::RETURN_CM, 0);
}

tree::TerminalNode* CharmmCRDParser::CommentContext::EOF() {
  return getToken(CharmmCRDParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CharmmCRDParser::CommentContext::Any_name() {
  return getTokens(CharmmCRDParser::Any_name);
}

tree::TerminalNode* CharmmCRDParser::CommentContext::Any_name(size_t i) {
  return getToken(CharmmCRDParser::Any_name, i);
}


size_t CharmmCRDParser::CommentContext::getRuleIndex() const {
  return CharmmCRDParser::RuleComment;
}


std::any CharmmCRDParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmCRDParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

CharmmCRDParser::CommentContext* CharmmCRDParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 2, CharmmCRDParser::RuleComment);
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
    match(CharmmCRDParser::COMMENT);
    setState(21);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CharmmCRDParser::Any_name) {
      setState(18);
      match(CharmmCRDParser::Any_name);
      setState(23);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(24);
    _la = _input->LA(1);
    if (!(_la == CharmmCRDParser::EOF

    || _la == CharmmCRDParser::RETURN_CM)) {
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

//----------------- CoordinatesContext ------------------------------------------------------------------

CharmmCRDParser::CoordinatesContext::CoordinatesContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmCRDParser::CoordinatesContext::Integer() {
  return getToken(CharmmCRDParser::Integer, 0);
}

tree::TerminalNode* CharmmCRDParser::CoordinatesContext::Ext() {
  return getToken(CharmmCRDParser::Ext, 0);
}

std::vector<CharmmCRDParser::Atom_coordinateContext *> CharmmCRDParser::CoordinatesContext::atom_coordinate() {
  return getRuleContexts<CharmmCRDParser::Atom_coordinateContext>();
}

CharmmCRDParser::Atom_coordinateContext* CharmmCRDParser::CoordinatesContext::atom_coordinate(size_t i) {
  return getRuleContext<CharmmCRDParser::Atom_coordinateContext>(i);
}


size_t CharmmCRDParser::CoordinatesContext::getRuleIndex() const {
  return CharmmCRDParser::RuleCoordinates;
}


std::any CharmmCRDParser::CoordinatesContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmCRDParserVisitor*>(visitor))
    return parserVisitor->visitCoordinates(this);
  else
    return visitor->visitChildren(this);
}

CharmmCRDParser::CoordinatesContext* CharmmCRDParser::coordinates() {
  CoordinatesContext *_localctx = _tracker.createInstance<CoordinatesContext>(_ctx, getState());
  enterRule(_localctx, 4, CharmmCRDParser::RuleCoordinates);

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
    setState(26);
    match(CharmmCRDParser::Integer);
    setState(27);
    match(CharmmCRDParser::Ext);
    setState(29); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(28);
              atom_coordinate();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(31); 
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

//----------------- Atom_coordinateContext ------------------------------------------------------------------

CharmmCRDParser::Atom_coordinateContext::Atom_coordinateContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> CharmmCRDParser::Atom_coordinateContext::Integer() {
  return getTokens(CharmmCRDParser::Integer);
}

tree::TerminalNode* CharmmCRDParser::Atom_coordinateContext::Integer(size_t i) {
  return getToken(CharmmCRDParser::Integer, i);
}

std::vector<tree::TerminalNode *> CharmmCRDParser::Atom_coordinateContext::Simple_name() {
  return getTokens(CharmmCRDParser::Simple_name);
}

tree::TerminalNode* CharmmCRDParser::Atom_coordinateContext::Simple_name(size_t i) {
  return getToken(CharmmCRDParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> CharmmCRDParser::Atom_coordinateContext::Float() {
  return getTokens(CharmmCRDParser::Float);
}

tree::TerminalNode* CharmmCRDParser::Atom_coordinateContext::Float(size_t i) {
  return getToken(CharmmCRDParser::Float, i);
}


size_t CharmmCRDParser::Atom_coordinateContext::getRuleIndex() const {
  return CharmmCRDParser::RuleAtom_coordinate;
}


std::any CharmmCRDParser::Atom_coordinateContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmCRDParserVisitor*>(visitor))
    return parserVisitor->visitAtom_coordinate(this);
  else
    return visitor->visitChildren(this);
}

CharmmCRDParser::Atom_coordinateContext* CharmmCRDParser::atom_coordinate() {
  Atom_coordinateContext *_localctx = _tracker.createInstance<Atom_coordinateContext>(_ctx, getState());
  enterRule(_localctx, 6, CharmmCRDParser::RuleAtom_coordinate);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(33);
    match(CharmmCRDParser::Integer);
    setState(34);
    match(CharmmCRDParser::Integer);
    setState(35);
    match(CharmmCRDParser::Simple_name);
    setState(36);
    match(CharmmCRDParser::Simple_name);
    setState(37);
    match(CharmmCRDParser::Float);
    setState(38);
    match(CharmmCRDParser::Float);
    setState(39);
    match(CharmmCRDParser::Float);
    setState(40);
    match(CharmmCRDParser::Simple_name);
    setState(41);
    match(CharmmCRDParser::Integer);
    setState(42);
    match(CharmmCRDParser::Float);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

void CharmmCRDParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  charmmcrdparserParserInitialize();
#else
  ::antlr4::internal::call_once(charmmcrdparserParserOnceFlag, charmmcrdparserParserInitialize);
#endif
}
