
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BarePDBParser.g4 by ANTLR 4.13.2


#include "BarePDBParserVisitor.h"

#include "BarePDBParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct BarePDBParserStaticData final {
  BarePDBParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  BarePDBParserStaticData(const BarePDBParserStaticData&) = delete;
  BarePDBParserStaticData(BarePDBParserStaticData&&) = delete;
  BarePDBParserStaticData& operator=(const BarePDBParserStaticData&) = delete;
  BarePDBParserStaticData& operator=(BarePDBParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag barepdbparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<BarePDBParserStaticData> barepdbparserParserStaticData = nullptr;

void barepdbparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (barepdbparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(barepdbparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<BarePDBParserStaticData>(
    std::vector<std::string>{
      "bare_pdb", "comment", "coordinates", "atom_coordinate", "atom_num", 
      "atom_name", "xyz", "x_yz", "xy_z", "x_y_z", "undefined", "number", 
      "terminal", "end"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "'ATOM'", "'HETATM'", "'TER'", "'END'"
    },
    std::vector<std::string>{
      "", "Integer", "Float", "COMMENT", "Hetatm_decimal", "Integer_concat_alt", 
      "Float_concat_2", "Float_concat_3", "Atom", "Hetatm", "Ter", "End", 
      "Simple_name", "Null_value", "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", 
      "LINE_COMMENT", "Any_name", "SPACE_CM", "RETURN_CM"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,20,133,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,1,0,1,0,
  	1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,1,0,1,1,1,1,5,1,42,8,1,10,1,12,
  	1,45,9,1,1,1,1,1,1,2,4,2,50,8,2,11,2,12,2,51,1,3,1,3,1,3,1,3,1,3,1,3,
  	3,3,60,8,3,1,3,1,3,3,3,64,8,3,1,3,1,3,1,3,1,3,1,3,3,3,71,8,3,1,3,3,3,
  	74,8,3,1,3,3,3,77,8,3,1,4,1,4,1,4,1,4,1,4,3,4,84,8,4,1,5,1,5,1,6,1,6,
  	1,6,1,6,1,6,1,6,1,6,3,6,95,8,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,10,1,
  	10,1,11,1,11,1,12,3,12,110,8,12,1,12,3,12,113,8,12,1,12,1,12,5,12,117,
  	8,12,10,12,12,12,120,9,12,1,12,1,12,1,13,1,13,5,13,126,8,13,10,13,12,
  	13,129,9,13,1,13,1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
  	0,5,1,1,20,20,2,0,1,1,5,5,2,0,5,5,12,12,2,0,1,2,12,13,1,0,1,2,140,0,34,
  	1,0,0,0,2,39,1,0,0,0,4,49,1,0,0,0,6,53,1,0,0,0,8,83,1,0,0,0,10,85,1,0,
  	0,0,12,94,1,0,0,0,14,96,1,0,0,0,16,99,1,0,0,0,18,102,1,0,0,0,20,104,1,
  	0,0,0,22,106,1,0,0,0,24,109,1,0,0,0,26,123,1,0,0,0,28,33,3,2,1,0,29,33,
  	3,4,2,0,30,33,3,24,12,0,31,33,3,26,13,0,32,28,1,0,0,0,32,29,1,0,0,0,32,
  	30,1,0,0,0,32,31,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,
  	37,1,0,0,0,36,34,1,0,0,0,37,38,5,0,0,1,38,1,1,0,0,0,39,43,5,3,0,0,40,
  	42,5,18,0,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,
  	46,1,0,0,0,45,43,1,0,0,0,46,47,7,0,0,0,47,3,1,0,0,0,48,50,3,6,3,0,49,
  	48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,5,1,0,0,0,53,
  	54,3,8,4,0,54,55,3,10,5,0,55,63,3,10,5,0,56,57,5,1,0,0,57,64,5,1,0,0,
  	58,60,5,12,0,0,59,58,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,64,7,1,0,
  	0,62,64,5,12,0,0,63,56,1,0,0,0,63,59,1,0,0,0,63,62,1,0,0,0,64,65,1,0,
  	0,0,65,70,3,12,6,0,66,67,3,22,11,0,67,68,3,22,11,0,68,71,1,0,0,0,69,71,
  	5,6,0,0,70,66,1,0,0,0,70,69,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,74,
  	3,20,10,0,73,72,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,77,3,20,10,0,76,
  	75,1,0,0,0,76,77,1,0,0,0,77,7,1,0,0,0,78,79,5,8,0,0,79,84,5,1,0,0,80,
  	81,5,9,0,0,81,84,5,1,0,0,82,84,5,4,0,0,83,78,1,0,0,0,83,80,1,0,0,0,83,
  	82,1,0,0,0,84,9,1,0,0,0,85,86,7,2,0,0,86,11,1,0,0,0,87,88,3,22,11,0,88,
  	89,3,22,11,0,89,90,3,22,11,0,90,95,1,0,0,0,91,95,3,14,7,0,92,95,3,16,
  	8,0,93,95,3,18,9,0,94,87,1,0,0,0,94,91,1,0,0,0,94,92,1,0,0,0,94,93,1,
  	0,0,0,95,13,1,0,0,0,96,97,3,22,11,0,97,98,5,6,0,0,98,15,1,0,0,0,99,100,
  	5,6,0,0,100,101,3,22,11,0,101,17,1,0,0,0,102,103,5,7,0,0,103,19,1,0,0,
  	0,104,105,7,3,0,0,105,21,1,0,0,0,106,107,7,4,0,0,107,23,1,0,0,0,108,110,
  	5,8,0,0,109,108,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,113,5,9,0,
  	0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,118,5,10,0,0,115,
  	117,5,18,0,0,116,115,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,
  	1,0,0,0,119,121,1,0,0,0,120,118,1,0,0,0,121,122,7,0,0,0,122,25,1,0,0,
  	0,123,127,5,11,0,0,124,126,5,18,0,0,125,124,1,0,0,0,126,129,1,0,0,0,127,
  	125,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,127,1,0,0,0,130,131,7,
  	0,0,0,131,27,1,0,0,0,15,32,34,43,51,59,63,70,73,76,83,94,109,112,118,
  	127
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  barepdbparserParserStaticData = std::move(staticData);
}

}

BarePDBParser::BarePDBParser(TokenStream *input) : BarePDBParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

BarePDBParser::BarePDBParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  BarePDBParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *barepdbparserParserStaticData->atn, barepdbparserParserStaticData->decisionToDFA, barepdbparserParserStaticData->sharedContextCache, options);
}

BarePDBParser::~BarePDBParser() {
  delete _interpreter;
}

const atn::ATN& BarePDBParser::getATN() const {
  return *barepdbparserParserStaticData->atn;
}

std::string BarePDBParser::getGrammarFileName() const {
  return "BarePDBParser.g4";
}

const std::vector<std::string>& BarePDBParser::getRuleNames() const {
  return barepdbparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& BarePDBParser::getVocabulary() const {
  return barepdbparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView BarePDBParser::getSerializedATN() const {
  return barepdbparserParserStaticData->serializedATN;
}


//----------------- Bare_pdbContext ------------------------------------------------------------------

BarePDBParser::Bare_pdbContext::Bare_pdbContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePDBParser::Bare_pdbContext::EOF() {
  return getToken(BarePDBParser::EOF, 0);
}

std::vector<BarePDBParser::CommentContext *> BarePDBParser::Bare_pdbContext::comment() {
  return getRuleContexts<BarePDBParser::CommentContext>();
}

BarePDBParser::CommentContext* BarePDBParser::Bare_pdbContext::comment(size_t i) {
  return getRuleContext<BarePDBParser::CommentContext>(i);
}

std::vector<BarePDBParser::CoordinatesContext *> BarePDBParser::Bare_pdbContext::coordinates() {
  return getRuleContexts<BarePDBParser::CoordinatesContext>();
}

BarePDBParser::CoordinatesContext* BarePDBParser::Bare_pdbContext::coordinates(size_t i) {
  return getRuleContext<BarePDBParser::CoordinatesContext>(i);
}

std::vector<BarePDBParser::TerminalContext *> BarePDBParser::Bare_pdbContext::terminal() {
  return getRuleContexts<BarePDBParser::TerminalContext>();
}

BarePDBParser::TerminalContext* BarePDBParser::Bare_pdbContext::terminal(size_t i) {
  return getRuleContext<BarePDBParser::TerminalContext>(i);
}

std::vector<BarePDBParser::EndContext *> BarePDBParser::Bare_pdbContext::end() {
  return getRuleContexts<BarePDBParser::EndContext>();
}

BarePDBParser::EndContext* BarePDBParser::Bare_pdbContext::end(size_t i) {
  return getRuleContext<BarePDBParser::EndContext>(i);
}


size_t BarePDBParser::Bare_pdbContext::getRuleIndex() const {
  return BarePDBParser::RuleBare_pdb;
}


std::any BarePDBParser::Bare_pdbContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitBare_pdb(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::Bare_pdbContext* BarePDBParser::bare_pdb() {
  Bare_pdbContext *_localctx = _tracker.createInstance<Bare_pdbContext>(_ctx, getState());
  enterRule(_localctx, 0, BarePDBParser::RuleBare_pdb);
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
    setState(34);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 3864) != 0)) {
      setState(32);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
      case 1: {
        setState(28);
        comment();
        break;
      }

      case 2: {
        setState(29);
        coordinates();
        break;
      }

      case 3: {
        setState(30);
        terminal();
        break;
      }

      case 4: {
        setState(31);
        end();
        break;
      }

      default:
        break;
      }
      setState(36);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(37);
    match(BarePDBParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CommentContext ------------------------------------------------------------------

BarePDBParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePDBParser::CommentContext::COMMENT() {
  return getToken(BarePDBParser::COMMENT, 0);
}

tree::TerminalNode* BarePDBParser::CommentContext::RETURN_CM() {
  return getToken(BarePDBParser::RETURN_CM, 0);
}

tree::TerminalNode* BarePDBParser::CommentContext::EOF() {
  return getToken(BarePDBParser::EOF, 0);
}

std::vector<tree::TerminalNode *> BarePDBParser::CommentContext::Any_name() {
  return getTokens(BarePDBParser::Any_name);
}

tree::TerminalNode* BarePDBParser::CommentContext::Any_name(size_t i) {
  return getToken(BarePDBParser::Any_name, i);
}


size_t BarePDBParser::CommentContext::getRuleIndex() const {
  return BarePDBParser::RuleComment;
}


std::any BarePDBParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::CommentContext* BarePDBParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 2, BarePDBParser::RuleComment);
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
    setState(39);
    match(BarePDBParser::COMMENT);
    setState(43);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BarePDBParser::Any_name) {
      setState(40);
      match(BarePDBParser::Any_name);
      setState(45);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(46);
    _la = _input->LA(1);
    if (!(_la == BarePDBParser::EOF

    || _la == BarePDBParser::RETURN_CM)) {
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

BarePDBParser::CoordinatesContext::CoordinatesContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BarePDBParser::Atom_coordinateContext *> BarePDBParser::CoordinatesContext::atom_coordinate() {
  return getRuleContexts<BarePDBParser::Atom_coordinateContext>();
}

BarePDBParser::Atom_coordinateContext* BarePDBParser::CoordinatesContext::atom_coordinate(size_t i) {
  return getRuleContext<BarePDBParser::Atom_coordinateContext>(i);
}


size_t BarePDBParser::CoordinatesContext::getRuleIndex() const {
  return BarePDBParser::RuleCoordinates;
}


std::any BarePDBParser::CoordinatesContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitCoordinates(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::CoordinatesContext* BarePDBParser::coordinates() {
  CoordinatesContext *_localctx = _tracker.createInstance<CoordinatesContext>(_ctx, getState());
  enterRule(_localctx, 4, BarePDBParser::RuleCoordinates);

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
    setState(49); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(48);
              atom_coordinate();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(51); 
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

BarePDBParser::Atom_coordinateContext::Atom_coordinateContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BarePDBParser::Atom_numContext* BarePDBParser::Atom_coordinateContext::atom_num() {
  return getRuleContext<BarePDBParser::Atom_numContext>(0);
}

std::vector<BarePDBParser::Atom_nameContext *> BarePDBParser::Atom_coordinateContext::atom_name() {
  return getRuleContexts<BarePDBParser::Atom_nameContext>();
}

BarePDBParser::Atom_nameContext* BarePDBParser::Atom_coordinateContext::atom_name(size_t i) {
  return getRuleContext<BarePDBParser::Atom_nameContext>(i);
}

BarePDBParser::XyzContext* BarePDBParser::Atom_coordinateContext::xyz() {
  return getRuleContext<BarePDBParser::XyzContext>(0);
}

std::vector<tree::TerminalNode *> BarePDBParser::Atom_coordinateContext::Integer() {
  return getTokens(BarePDBParser::Integer);
}

tree::TerminalNode* BarePDBParser::Atom_coordinateContext::Integer(size_t i) {
  return getToken(BarePDBParser::Integer, i);
}

tree::TerminalNode* BarePDBParser::Atom_coordinateContext::Simple_name() {
  return getToken(BarePDBParser::Simple_name, 0);
}

tree::TerminalNode* BarePDBParser::Atom_coordinateContext::Integer_concat_alt() {
  return getToken(BarePDBParser::Integer_concat_alt, 0);
}

std::vector<BarePDBParser::NumberContext *> BarePDBParser::Atom_coordinateContext::number() {
  return getRuleContexts<BarePDBParser::NumberContext>();
}

BarePDBParser::NumberContext* BarePDBParser::Atom_coordinateContext::number(size_t i) {
  return getRuleContext<BarePDBParser::NumberContext>(i);
}

tree::TerminalNode* BarePDBParser::Atom_coordinateContext::Float_concat_2() {
  return getToken(BarePDBParser::Float_concat_2, 0);
}

std::vector<BarePDBParser::UndefinedContext *> BarePDBParser::Atom_coordinateContext::undefined() {
  return getRuleContexts<BarePDBParser::UndefinedContext>();
}

BarePDBParser::UndefinedContext* BarePDBParser::Atom_coordinateContext::undefined(size_t i) {
  return getRuleContext<BarePDBParser::UndefinedContext>(i);
}


size_t BarePDBParser::Atom_coordinateContext::getRuleIndex() const {
  return BarePDBParser::RuleAtom_coordinate;
}


std::any BarePDBParser::Atom_coordinateContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitAtom_coordinate(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::Atom_coordinateContext* BarePDBParser::atom_coordinate() {
  Atom_coordinateContext *_localctx = _tracker.createInstance<Atom_coordinateContext>(_ctx, getState());
  enterRule(_localctx, 6, BarePDBParser::RuleAtom_coordinate);
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
    atom_num();
    setState(54);
    atom_name();
    setState(55);
    atom_name();
    setState(63);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx)) {
    case 1: {
      setState(56);
      match(BarePDBParser::Integer);
      setState(57);
      match(BarePDBParser::Integer);
      break;
    }

    case 2: {
      setState(59);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == BarePDBParser::Simple_name) {
        setState(58);
        match(BarePDBParser::Simple_name);
      }
      setState(61);
      _la = _input->LA(1);
      if (!(_la == BarePDBParser::Integer

      || _la == BarePDBParser::Integer_concat_alt)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      break;
    }

    case 3: {
      setState(62);
      match(BarePDBParser::Simple_name);
      break;
    }

    default:
      break;
    }
    setState(65);
    xyz();
    setState(70);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 6, _ctx)) {
    case 1: {
      setState(66);
      number();
      setState(67);
      number();
      break;
    }

    case 2: {
      setState(69);
      match(BarePDBParser::Float_concat_2);
      break;
    }

    default:
      break;
    }
    setState(73);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx)) {
    case 1: {
      setState(72);
      undefined();
      break;
    }

    default:
      break;
    }
    setState(76);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 12294) != 0)) {
      setState(75);
      undefined();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Atom_numContext ------------------------------------------------------------------

BarePDBParser::Atom_numContext::Atom_numContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePDBParser::Atom_numContext::Atom() {
  return getToken(BarePDBParser::Atom, 0);
}

tree::TerminalNode* BarePDBParser::Atom_numContext::Integer() {
  return getToken(BarePDBParser::Integer, 0);
}

tree::TerminalNode* BarePDBParser::Atom_numContext::Hetatm() {
  return getToken(BarePDBParser::Hetatm, 0);
}

tree::TerminalNode* BarePDBParser::Atom_numContext::Hetatm_decimal() {
  return getToken(BarePDBParser::Hetatm_decimal, 0);
}


size_t BarePDBParser::Atom_numContext::getRuleIndex() const {
  return BarePDBParser::RuleAtom_num;
}


std::any BarePDBParser::Atom_numContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitAtom_num(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::Atom_numContext* BarePDBParser::atom_num() {
  Atom_numContext *_localctx = _tracker.createInstance<Atom_numContext>(_ctx, getState());
  enterRule(_localctx, 8, BarePDBParser::RuleAtom_num);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(83);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BarePDBParser::Atom: {
        setState(78);
        match(BarePDBParser::Atom);
        setState(79);
        match(BarePDBParser::Integer);
        break;
      }

      case BarePDBParser::Hetatm: {
        setState(80);
        match(BarePDBParser::Hetatm);
        setState(81);
        match(BarePDBParser::Integer);
        break;
      }

      case BarePDBParser::Hetatm_decimal: {
        setState(82);
        match(BarePDBParser::Hetatm_decimal);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Atom_nameContext ------------------------------------------------------------------

BarePDBParser::Atom_nameContext::Atom_nameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePDBParser::Atom_nameContext::Simple_name() {
  return getToken(BarePDBParser::Simple_name, 0);
}

tree::TerminalNode* BarePDBParser::Atom_nameContext::Integer_concat_alt() {
  return getToken(BarePDBParser::Integer_concat_alt, 0);
}


size_t BarePDBParser::Atom_nameContext::getRuleIndex() const {
  return BarePDBParser::RuleAtom_name;
}


std::any BarePDBParser::Atom_nameContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitAtom_name(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::Atom_nameContext* BarePDBParser::atom_name() {
  Atom_nameContext *_localctx = _tracker.createInstance<Atom_nameContext>(_ctx, getState());
  enterRule(_localctx, 10, BarePDBParser::RuleAtom_name);
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
    setState(85);
    _la = _input->LA(1);
    if (!(_la == BarePDBParser::Integer_concat_alt

    || _la == BarePDBParser::Simple_name)) {
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

//----------------- XyzContext ------------------------------------------------------------------

BarePDBParser::XyzContext::XyzContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BarePDBParser::NumberContext *> BarePDBParser::XyzContext::number() {
  return getRuleContexts<BarePDBParser::NumberContext>();
}

BarePDBParser::NumberContext* BarePDBParser::XyzContext::number(size_t i) {
  return getRuleContext<BarePDBParser::NumberContext>(i);
}

BarePDBParser::X_yzContext* BarePDBParser::XyzContext::x_yz() {
  return getRuleContext<BarePDBParser::X_yzContext>(0);
}

BarePDBParser::Xy_zContext* BarePDBParser::XyzContext::xy_z() {
  return getRuleContext<BarePDBParser::Xy_zContext>(0);
}

BarePDBParser::X_y_zContext* BarePDBParser::XyzContext::x_y_z() {
  return getRuleContext<BarePDBParser::X_y_zContext>(0);
}


size_t BarePDBParser::XyzContext::getRuleIndex() const {
  return BarePDBParser::RuleXyz;
}


std::any BarePDBParser::XyzContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitXyz(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::XyzContext* BarePDBParser::xyz() {
  XyzContext *_localctx = _tracker.createInstance<XyzContext>(_ctx, getState());
  enterRule(_localctx, 12, BarePDBParser::RuleXyz);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(94);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 10, _ctx)) {
    case 1: {
      setState(87);
      number();
      setState(88);
      number();
      setState(89);
      number();
      break;
    }

    case 2: {
      setState(91);
      x_yz();
      break;
    }

    case 3: {
      setState(92);
      xy_z();
      break;
    }

    case 4: {
      setState(93);
      x_y_z();
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

//----------------- X_yzContext ------------------------------------------------------------------

BarePDBParser::X_yzContext::X_yzContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BarePDBParser::NumberContext* BarePDBParser::X_yzContext::number() {
  return getRuleContext<BarePDBParser::NumberContext>(0);
}

tree::TerminalNode* BarePDBParser::X_yzContext::Float_concat_2() {
  return getToken(BarePDBParser::Float_concat_2, 0);
}


size_t BarePDBParser::X_yzContext::getRuleIndex() const {
  return BarePDBParser::RuleX_yz;
}


std::any BarePDBParser::X_yzContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitX_yz(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::X_yzContext* BarePDBParser::x_yz() {
  X_yzContext *_localctx = _tracker.createInstance<X_yzContext>(_ctx, getState());
  enterRule(_localctx, 14, BarePDBParser::RuleX_yz);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(96);
    number();
    setState(97);
    match(BarePDBParser::Float_concat_2);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Xy_zContext ------------------------------------------------------------------

BarePDBParser::Xy_zContext::Xy_zContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePDBParser::Xy_zContext::Float_concat_2() {
  return getToken(BarePDBParser::Float_concat_2, 0);
}

BarePDBParser::NumberContext* BarePDBParser::Xy_zContext::number() {
  return getRuleContext<BarePDBParser::NumberContext>(0);
}


size_t BarePDBParser::Xy_zContext::getRuleIndex() const {
  return BarePDBParser::RuleXy_z;
}


std::any BarePDBParser::Xy_zContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitXy_z(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::Xy_zContext* BarePDBParser::xy_z() {
  Xy_zContext *_localctx = _tracker.createInstance<Xy_zContext>(_ctx, getState());
  enterRule(_localctx, 16, BarePDBParser::RuleXy_z);

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
    match(BarePDBParser::Float_concat_2);
    setState(100);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- X_y_zContext ------------------------------------------------------------------

BarePDBParser::X_y_zContext::X_y_zContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePDBParser::X_y_zContext::Float_concat_3() {
  return getToken(BarePDBParser::Float_concat_3, 0);
}


size_t BarePDBParser::X_y_zContext::getRuleIndex() const {
  return BarePDBParser::RuleX_y_z;
}


std::any BarePDBParser::X_y_zContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitX_y_z(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::X_y_zContext* BarePDBParser::x_y_z() {
  X_y_zContext *_localctx = _tracker.createInstance<X_y_zContext>(_ctx, getState());
  enterRule(_localctx, 18, BarePDBParser::RuleX_y_z);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(102);
    match(BarePDBParser::Float_concat_3);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- UndefinedContext ------------------------------------------------------------------

BarePDBParser::UndefinedContext::UndefinedContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePDBParser::UndefinedContext::Simple_name() {
  return getToken(BarePDBParser::Simple_name, 0);
}

tree::TerminalNode* BarePDBParser::UndefinedContext::Integer() {
  return getToken(BarePDBParser::Integer, 0);
}

tree::TerminalNode* BarePDBParser::UndefinedContext::Float() {
  return getToken(BarePDBParser::Float, 0);
}

tree::TerminalNode* BarePDBParser::UndefinedContext::Null_value() {
  return getToken(BarePDBParser::Null_value, 0);
}


size_t BarePDBParser::UndefinedContext::getRuleIndex() const {
  return BarePDBParser::RuleUndefined;
}


std::any BarePDBParser::UndefinedContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitUndefined(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::UndefinedContext* BarePDBParser::undefined() {
  UndefinedContext *_localctx = _tracker.createInstance<UndefinedContext>(_ctx, getState());
  enterRule(_localctx, 20, BarePDBParser::RuleUndefined);
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
    setState(104);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 12294) != 0))) {
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

//----------------- NumberContext ------------------------------------------------------------------

BarePDBParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePDBParser::NumberContext::Float() {
  return getToken(BarePDBParser::Float, 0);
}

tree::TerminalNode* BarePDBParser::NumberContext::Integer() {
  return getToken(BarePDBParser::Integer, 0);
}


size_t BarePDBParser::NumberContext::getRuleIndex() const {
  return BarePDBParser::RuleNumber;
}


std::any BarePDBParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::NumberContext* BarePDBParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 22, BarePDBParser::RuleNumber);
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
    setState(106);
    _la = _input->LA(1);
    if (!(_la == BarePDBParser::Integer

    || _la == BarePDBParser::Float)) {
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

//----------------- TerminalContext ------------------------------------------------------------------

BarePDBParser::TerminalContext::TerminalContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePDBParser::TerminalContext::Ter() {
  return getToken(BarePDBParser::Ter, 0);
}

tree::TerminalNode* BarePDBParser::TerminalContext::RETURN_CM() {
  return getToken(BarePDBParser::RETURN_CM, 0);
}

tree::TerminalNode* BarePDBParser::TerminalContext::EOF() {
  return getToken(BarePDBParser::EOF, 0);
}

tree::TerminalNode* BarePDBParser::TerminalContext::Atom() {
  return getToken(BarePDBParser::Atom, 0);
}

tree::TerminalNode* BarePDBParser::TerminalContext::Hetatm() {
  return getToken(BarePDBParser::Hetatm, 0);
}

std::vector<tree::TerminalNode *> BarePDBParser::TerminalContext::Any_name() {
  return getTokens(BarePDBParser::Any_name);
}

tree::TerminalNode* BarePDBParser::TerminalContext::Any_name(size_t i) {
  return getToken(BarePDBParser::Any_name, i);
}


size_t BarePDBParser::TerminalContext::getRuleIndex() const {
  return BarePDBParser::RuleTerminal;
}


std::any BarePDBParser::TerminalContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitTerminal(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::TerminalContext* BarePDBParser::terminal() {
  TerminalContext *_localctx = _tracker.createInstance<TerminalContext>(_ctx, getState());
  enterRule(_localctx, 24, BarePDBParser::RuleTerminal);
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
    setState(109);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePDBParser::Atom) {
      setState(108);
      match(BarePDBParser::Atom);
    }
    setState(112);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BarePDBParser::Hetatm) {
      setState(111);
      match(BarePDBParser::Hetatm);
    }
    setState(114);
    match(BarePDBParser::Ter);
    setState(118);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BarePDBParser::Any_name) {
      setState(115);
      match(BarePDBParser::Any_name);
      setState(120);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(121);
    _la = _input->LA(1);
    if (!(_la == BarePDBParser::EOF

    || _la == BarePDBParser::RETURN_CM)) {
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

//----------------- EndContext ------------------------------------------------------------------

BarePDBParser::EndContext::EndContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BarePDBParser::EndContext::End() {
  return getToken(BarePDBParser::End, 0);
}

tree::TerminalNode* BarePDBParser::EndContext::RETURN_CM() {
  return getToken(BarePDBParser::RETURN_CM, 0);
}

tree::TerminalNode* BarePDBParser::EndContext::EOF() {
  return getToken(BarePDBParser::EOF, 0);
}

std::vector<tree::TerminalNode *> BarePDBParser::EndContext::Any_name() {
  return getTokens(BarePDBParser::Any_name);
}

tree::TerminalNode* BarePDBParser::EndContext::Any_name(size_t i) {
  return getToken(BarePDBParser::Any_name, i);
}


size_t BarePDBParser::EndContext::getRuleIndex() const {
  return BarePDBParser::RuleEnd;
}


std::any BarePDBParser::EndContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BarePDBParserVisitor*>(visitor))
    return parserVisitor->visitEnd(this);
  else
    return visitor->visitChildren(this);
}

BarePDBParser::EndContext* BarePDBParser::end() {
  EndContext *_localctx = _tracker.createInstance<EndContext>(_ctx, getState());
  enterRule(_localctx, 26, BarePDBParser::RuleEnd);
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
    setState(123);
    match(BarePDBParser::End);
    setState(127);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BarePDBParser::Any_name) {
      setState(124);
      match(BarePDBParser::Any_name);
      setState(129);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(130);
    _la = _input->LA(1);
    if (!(_la == BarePDBParser::EOF

    || _la == BarePDBParser::RETURN_CM)) {
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

void BarePDBParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  barepdbparserParserInitialize();
#else
  ::antlr4::internal::call_once(barepdbparserParserOnceFlag, barepdbparserParserInitialize);
#endif
}
