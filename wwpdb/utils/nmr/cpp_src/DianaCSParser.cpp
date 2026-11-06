
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/DianaCSParser.g4 by ANTLR 4.13.2


#include "DianaCSParserVisitor.h"

#include "DianaCSParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct DianaCSParserStaticData final {
  DianaCSParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  DianaCSParserStaticData(const DianaCSParserStaticData&) = delete;
  DianaCSParserStaticData(DianaCSParserStaticData&&) = delete;
  DianaCSParserStaticData& operator=(const DianaCSParserStaticData&) = delete;
  DianaCSParserStaticData& operator=(DianaCSParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag dianacsparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<DianaCSParserStaticData> dianacsparserParserStaticData = nullptr;

void dianacsparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (dianacsparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(dianacsparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<DianaCSParserStaticData>(
    std::vector<std::string>{
      "diana_cs", "comment", "chemical_shifts", "chemical_shift", "atom_chemical_shift"
    },
    std::vector<std::string>{
      "", "", "", "", "", "'SHIFTS'"
    },
    std::vector<std::string>{
      "", "Integer", "Float", "SMCLN_COMMENT", "COMMENT", "Shifts", "Simple_name", 
      "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT", "Any_name", 
      "SPACE_CM", "RETURN_CM"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,13,53,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,5,0,13,8,0,
  	10,0,12,0,16,9,0,1,0,1,0,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,1,1,1,1,
  	1,2,4,2,30,8,2,11,2,12,2,31,1,3,1,3,1,3,1,3,4,3,38,8,3,11,3,12,3,39,1,
  	3,3,3,43,8,3,1,3,3,3,46,8,3,1,4,1,4,1,4,3,4,51,8,4,1,4,0,0,5,0,2,4,6,
  	8,0,1,1,1,13,13,55,0,14,1,0,0,0,2,19,1,0,0,0,4,29,1,0,0,0,6,33,1,0,0,
  	0,8,47,1,0,0,0,10,13,3,2,1,0,11,13,3,4,2,0,12,10,1,0,0,0,12,11,1,0,0,
  	0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,17,1,0,0,0,16,14,1,0,0,
  	0,17,18,5,0,0,1,18,1,1,0,0,0,19,23,5,4,0,0,20,22,5,11,0,0,21,20,1,0,0,
  	0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,
  	0,26,27,7,0,0,0,27,3,1,0,0,0,28,30,3,6,3,0,29,28,1,0,0,0,30,31,1,0,0,
  	0,31,29,1,0,0,0,31,32,1,0,0,0,32,5,1,0,0,0,33,34,5,5,0,0,34,35,5,6,0,
  	0,35,37,5,1,0,0,36,38,3,8,4,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,
  	0,39,40,1,0,0,0,40,42,1,0,0,0,41,43,5,6,0,0,42,41,1,0,0,0,42,43,1,0,0,
  	0,43,45,1,0,0,0,44,46,5,1,0,0,45,44,1,0,0,0,45,46,1,0,0,0,46,7,1,0,0,
  	0,47,48,5,6,0,0,48,50,5,2,0,0,49,51,5,2,0,0,50,49,1,0,0,0,50,51,1,0,0,
  	0,51,9,1,0,0,0,8,12,14,23,31,39,42,45,50
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  dianacsparserParserStaticData = std::move(staticData);
}

}

DianaCSParser::DianaCSParser(TokenStream *input) : DianaCSParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

DianaCSParser::DianaCSParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  DianaCSParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *dianacsparserParserStaticData->atn, dianacsparserParserStaticData->decisionToDFA, dianacsparserParserStaticData->sharedContextCache, options);
}

DianaCSParser::~DianaCSParser() {
  delete _interpreter;
}

const atn::ATN& DianaCSParser::getATN() const {
  return *dianacsparserParserStaticData->atn;
}

std::string DianaCSParser::getGrammarFileName() const {
  return "DianaCSParser.g4";
}

const std::vector<std::string>& DianaCSParser::getRuleNames() const {
  return dianacsparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& DianaCSParser::getVocabulary() const {
  return dianacsparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView DianaCSParser::getSerializedATN() const {
  return dianacsparserParserStaticData->serializedATN;
}


//----------------- Diana_csContext ------------------------------------------------------------------

DianaCSParser::Diana_csContext::Diana_csContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* DianaCSParser::Diana_csContext::EOF() {
  return getToken(DianaCSParser::EOF, 0);
}

std::vector<DianaCSParser::CommentContext *> DianaCSParser::Diana_csContext::comment() {
  return getRuleContexts<DianaCSParser::CommentContext>();
}

DianaCSParser::CommentContext* DianaCSParser::Diana_csContext::comment(size_t i) {
  return getRuleContext<DianaCSParser::CommentContext>(i);
}

std::vector<DianaCSParser::Chemical_shiftsContext *> DianaCSParser::Diana_csContext::chemical_shifts() {
  return getRuleContexts<DianaCSParser::Chemical_shiftsContext>();
}

DianaCSParser::Chemical_shiftsContext* DianaCSParser::Diana_csContext::chemical_shifts(size_t i) {
  return getRuleContext<DianaCSParser::Chemical_shiftsContext>(i);
}


size_t DianaCSParser::Diana_csContext::getRuleIndex() const {
  return DianaCSParser::RuleDiana_cs;
}


std::any DianaCSParser::Diana_csContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<DianaCSParserVisitor*>(visitor))
    return parserVisitor->visitDiana_cs(this);
  else
    return visitor->visitChildren(this);
}

DianaCSParser::Diana_csContext* DianaCSParser::diana_cs() {
  Diana_csContext *_localctx = _tracker.createInstance<Diana_csContext>(_ctx, getState());
  enterRule(_localctx, 0, DianaCSParser::RuleDiana_cs);
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
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == DianaCSParser::COMMENT

    || _la == DianaCSParser::Shifts) {
      setState(12);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case DianaCSParser::COMMENT: {
          setState(10);
          comment();
          break;
        }

        case DianaCSParser::Shifts: {
          setState(11);
          chemical_shifts();
          break;
        }

      default:
        throw NoViableAltException(this);
      }
      setState(16);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(17);
    match(DianaCSParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CommentContext ------------------------------------------------------------------

DianaCSParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* DianaCSParser::CommentContext::COMMENT() {
  return getToken(DianaCSParser::COMMENT, 0);
}

tree::TerminalNode* DianaCSParser::CommentContext::RETURN_CM() {
  return getToken(DianaCSParser::RETURN_CM, 0);
}

tree::TerminalNode* DianaCSParser::CommentContext::EOF() {
  return getToken(DianaCSParser::EOF, 0);
}

std::vector<tree::TerminalNode *> DianaCSParser::CommentContext::Any_name() {
  return getTokens(DianaCSParser::Any_name);
}

tree::TerminalNode* DianaCSParser::CommentContext::Any_name(size_t i) {
  return getToken(DianaCSParser::Any_name, i);
}


size_t DianaCSParser::CommentContext::getRuleIndex() const {
  return DianaCSParser::RuleComment;
}


std::any DianaCSParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<DianaCSParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

DianaCSParser::CommentContext* DianaCSParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 2, DianaCSParser::RuleComment);
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
    setState(19);
    match(DianaCSParser::COMMENT);
    setState(23);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == DianaCSParser::Any_name) {
      setState(20);
      match(DianaCSParser::Any_name);
      setState(25);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(26);
    _la = _input->LA(1);
    if (!(_la == DianaCSParser::EOF

    || _la == DianaCSParser::RETURN_CM)) {
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

//----------------- Chemical_shiftsContext ------------------------------------------------------------------

DianaCSParser::Chemical_shiftsContext::Chemical_shiftsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<DianaCSParser::Chemical_shiftContext *> DianaCSParser::Chemical_shiftsContext::chemical_shift() {
  return getRuleContexts<DianaCSParser::Chemical_shiftContext>();
}

DianaCSParser::Chemical_shiftContext* DianaCSParser::Chemical_shiftsContext::chemical_shift(size_t i) {
  return getRuleContext<DianaCSParser::Chemical_shiftContext>(i);
}


size_t DianaCSParser::Chemical_shiftsContext::getRuleIndex() const {
  return DianaCSParser::RuleChemical_shifts;
}


std::any DianaCSParser::Chemical_shiftsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<DianaCSParserVisitor*>(visitor))
    return parserVisitor->visitChemical_shifts(this);
  else
    return visitor->visitChildren(this);
}

DianaCSParser::Chemical_shiftsContext* DianaCSParser::chemical_shifts() {
  Chemical_shiftsContext *_localctx = _tracker.createInstance<Chemical_shiftsContext>(_ctx, getState());
  enterRule(_localctx, 4, DianaCSParser::RuleChemical_shifts);

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
    setState(29); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(28);
              chemical_shift();
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

//----------------- Chemical_shiftContext ------------------------------------------------------------------

DianaCSParser::Chemical_shiftContext::Chemical_shiftContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* DianaCSParser::Chemical_shiftContext::Shifts() {
  return getToken(DianaCSParser::Shifts, 0);
}

std::vector<tree::TerminalNode *> DianaCSParser::Chemical_shiftContext::Simple_name() {
  return getTokens(DianaCSParser::Simple_name);
}

tree::TerminalNode* DianaCSParser::Chemical_shiftContext::Simple_name(size_t i) {
  return getToken(DianaCSParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> DianaCSParser::Chemical_shiftContext::Integer() {
  return getTokens(DianaCSParser::Integer);
}

tree::TerminalNode* DianaCSParser::Chemical_shiftContext::Integer(size_t i) {
  return getToken(DianaCSParser::Integer, i);
}

std::vector<DianaCSParser::Atom_chemical_shiftContext *> DianaCSParser::Chemical_shiftContext::atom_chemical_shift() {
  return getRuleContexts<DianaCSParser::Atom_chemical_shiftContext>();
}

DianaCSParser::Atom_chemical_shiftContext* DianaCSParser::Chemical_shiftContext::atom_chemical_shift(size_t i) {
  return getRuleContext<DianaCSParser::Atom_chemical_shiftContext>(i);
}


size_t DianaCSParser::Chemical_shiftContext::getRuleIndex() const {
  return DianaCSParser::RuleChemical_shift;
}


std::any DianaCSParser::Chemical_shiftContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<DianaCSParserVisitor*>(visitor))
    return parserVisitor->visitChemical_shift(this);
  else
    return visitor->visitChildren(this);
}

DianaCSParser::Chemical_shiftContext* DianaCSParser::chemical_shift() {
  Chemical_shiftContext *_localctx = _tracker.createInstance<Chemical_shiftContext>(_ctx, getState());
  enterRule(_localctx, 6, DianaCSParser::RuleChemical_shift);
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
    setState(33);
    match(DianaCSParser::Shifts);
    setState(34);
    match(DianaCSParser::Simple_name);
    setState(35);
    match(DianaCSParser::Integer);
    setState(37); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(36);
              atom_chemical_shift();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(39); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(42);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == DianaCSParser::Simple_name) {
      setState(41);
      match(DianaCSParser::Simple_name);
    }
    setState(45);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == DianaCSParser::Integer) {
      setState(44);
      match(DianaCSParser::Integer);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Atom_chemical_shiftContext ------------------------------------------------------------------

DianaCSParser::Atom_chemical_shiftContext::Atom_chemical_shiftContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* DianaCSParser::Atom_chemical_shiftContext::Simple_name() {
  return getToken(DianaCSParser::Simple_name, 0);
}

std::vector<tree::TerminalNode *> DianaCSParser::Atom_chemical_shiftContext::Float() {
  return getTokens(DianaCSParser::Float);
}

tree::TerminalNode* DianaCSParser::Atom_chemical_shiftContext::Float(size_t i) {
  return getToken(DianaCSParser::Float, i);
}


size_t DianaCSParser::Atom_chemical_shiftContext::getRuleIndex() const {
  return DianaCSParser::RuleAtom_chemical_shift;
}


std::any DianaCSParser::Atom_chemical_shiftContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<DianaCSParserVisitor*>(visitor))
    return parserVisitor->visitAtom_chemical_shift(this);
  else
    return visitor->visitChildren(this);
}

DianaCSParser::Atom_chemical_shiftContext* DianaCSParser::atom_chemical_shift() {
  Atom_chemical_shiftContext *_localctx = _tracker.createInstance<Atom_chemical_shiftContext>(_ctx, getState());
  enterRule(_localctx, 8, DianaCSParser::RuleAtom_chemical_shift);
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
    setState(47);
    match(DianaCSParser::Simple_name);
    setState(48);
    match(DianaCSParser::Float);
    setState(50);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == DianaCSParser::Float) {
      setState(49);
      match(DianaCSParser::Float);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

void DianaCSParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  dianacsparserParserInitialize();
#else
  ::antlr4::internal::call_once(dianacsparserParserOnceFlag, dianacsparserParserInitialize);
#endif
}
