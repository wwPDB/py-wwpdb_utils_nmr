
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/OliviaCSParser.g4 by ANTLR 4.13.0


#include "OliviaCSParserVisitor.h"

#include "OliviaCSParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct OliviaCSParserStaticData final {
  OliviaCSParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  OliviaCSParserStaticData(const OliviaCSParserStaticData&) = delete;
  OliviaCSParserStaticData(OliviaCSParserStaticData&&) = delete;
  OliviaCSParserStaticData& operator=(const OliviaCSParserStaticData&) = delete;
  OliviaCSParserStaticData& operator=(OliviaCSParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag oliviacsparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
OliviaCSParserStaticData *oliviacsparserParserStaticData = nullptr;

void oliviacsparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (oliviacsparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(oliviacsparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<OliviaCSParserStaticData>(
    std::vector<std::string>{
      "olivia_cs", "sequence", "residue", "chemical_shifts", "chemical_shift", 
      "number", "comment"
    },
    std::vector<std::string>{
      "", "'TYPEDEF'", "'SEPARATOR'", "'FORMAT\\n'", "'UNFORMAT'", "'EOF'", 
      "", "", "", "", "'REMARK'", "", "", "", "", "", "", "", "'SEQUENCE'", 
      "'ASS_TBL_H2O'", "'ASS_TBL_TRO'", "'ASS_TBL_D2O'", "", "", "'TAB'", 
      "'COMMA'", "'SPACE'", "", "", "'CHAIN'", "'RESNAME'", "'SEQNUM'", 
      "'ATOMNAME'", "'SHIFT'", "'STDDEV'"
    },
    std::vector<std::string>{
      "", "Typedef", "Separator", "Format", "Unformat", "Eof", "Null_string", 
      "Integer", "Float", "Real", "COMMENT", "SHARP_COMMENT", "EXCLM_COMMENT", 
      "Simple_name", "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT", 
      "Sequence", "Ass_tbl_h2o", "Ass_tbl_tro", "Ass_tbl_d2o", "SPACE_TD", 
      "RETURN_TD", "Tab", "Comma", "Space", "SPACE_SE", "RETURN_SE", "Chain", 
      "Resname", "Seqnum", "Atomname", "Shift", "Stddev", "SPACE_FO", "RETURN_FO", 
      "Printf_string", "SPACE_PF", "RETURN_PF", "Any_name", "SPACE_CM", 
      "RETURN_CM"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,42,103,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,1,
  	0,3,0,16,8,0,1,0,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,0,1,1,
  	1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,45,8,
  	1,11,1,12,1,46,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
  	3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,4,3,78,
  	8,3,11,3,12,3,79,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,
  	1,6,5,6,96,8,6,10,6,12,6,99,9,6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,3,
  	1,0,24,26,1,0,19,21,1,0,7,9,103,0,15,1,0,0,0,2,28,1,0,0,0,4,50,1,0,0,
  	0,6,55,1,0,0,0,8,83,1,0,0,0,10,91,1,0,0,0,12,93,1,0,0,0,14,16,5,15,0,
  	0,15,14,1,0,0,0,15,16,1,0,0,0,16,23,1,0,0,0,17,22,3,12,6,0,18,22,3,2,
  	1,0,19,22,3,6,3,0,20,22,5,15,0,0,21,17,1,0,0,0,21,18,1,0,0,0,21,19,1,
  	0,0,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,
  	0,0,0,25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,29,5,1,0,0,29,30,5,
  	18,0,0,30,31,5,23,0,0,31,32,5,2,0,0,32,33,7,0,0,0,33,34,5,28,0,0,34,35,
  	5,3,0,0,35,36,5,29,0,0,36,37,5,30,0,0,37,38,5,31,0,0,38,39,5,36,0,0,39,
  	40,5,37,0,0,40,41,5,37,0,0,41,42,5,37,0,0,42,44,5,39,0,0,43,45,3,4,2,
  	0,44,43,1,0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,
  	0,48,49,5,4,0,0,49,3,1,0,0,0,50,51,5,13,0,0,51,52,5,13,0,0,52,53,5,7,
  	0,0,53,54,5,15,0,0,54,5,1,0,0,0,55,56,5,1,0,0,56,57,7,1,0,0,57,58,5,23,
  	0,0,58,59,5,2,0,0,59,60,7,0,0,0,60,61,5,28,0,0,61,62,5,3,0,0,62,63,5,
  	29,0,0,63,64,5,30,0,0,64,65,5,31,0,0,65,66,5,32,0,0,66,67,5,33,0,0,67,
  	68,5,34,0,0,68,69,5,36,0,0,69,70,5,37,0,0,70,71,5,37,0,0,71,72,5,37,0,
  	0,72,73,5,37,0,0,73,74,5,37,0,0,74,75,5,37,0,0,75,77,5,39,0,0,76,78,3,
  	8,4,0,77,76,1,0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,81,1,
  	0,0,0,81,82,5,4,0,0,82,7,1,0,0,0,83,84,5,13,0,0,84,85,5,13,0,0,85,86,
  	5,7,0,0,86,87,5,13,0,0,87,88,3,10,5,0,88,89,3,10,5,0,89,90,5,15,0,0,90,
  	9,1,0,0,0,91,92,7,2,0,0,92,11,1,0,0,0,93,97,5,10,0,0,94,96,5,40,0,0,95,
  	94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,
  	97,1,0,0,0,100,101,5,42,0,0,101,13,1,0,0,0,6,15,21,23,46,79,97
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  oliviacsparserParserStaticData = staticData.release();
}

}

OliviaCSParser::OliviaCSParser(TokenStream *input) : OliviaCSParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

OliviaCSParser::OliviaCSParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  OliviaCSParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *oliviacsparserParserStaticData->atn, oliviacsparserParserStaticData->decisionToDFA, oliviacsparserParserStaticData->sharedContextCache, options);
}

OliviaCSParser::~OliviaCSParser() {
  delete _interpreter;
}

const atn::ATN& OliviaCSParser::getATN() const {
  return *oliviacsparserParserStaticData->atn;
}

std::string OliviaCSParser::getGrammarFileName() const {
  return "OliviaCSParser.g4";
}

const std::vector<std::string>& OliviaCSParser::getRuleNames() const {
  return oliviacsparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& OliviaCSParser::getVocabulary() const {
  return oliviacsparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView OliviaCSParser::getSerializedATN() const {
  return oliviacsparserParserStaticData->serializedATN;
}


//----------------- Olivia_csContext ------------------------------------------------------------------

OliviaCSParser::Olivia_csContext::Olivia_csContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaCSParser::Olivia_csContext::EOF() {
  return getToken(OliviaCSParser::EOF, 0);
}

std::vector<tree::TerminalNode *> OliviaCSParser::Olivia_csContext::RETURN() {
  return getTokens(OliviaCSParser::RETURN);
}

tree::TerminalNode* OliviaCSParser::Olivia_csContext::RETURN(size_t i) {
  return getToken(OliviaCSParser::RETURN, i);
}

std::vector<OliviaCSParser::CommentContext *> OliviaCSParser::Olivia_csContext::comment() {
  return getRuleContexts<OliviaCSParser::CommentContext>();
}

OliviaCSParser::CommentContext* OliviaCSParser::Olivia_csContext::comment(size_t i) {
  return getRuleContext<OliviaCSParser::CommentContext>(i);
}

std::vector<OliviaCSParser::SequenceContext *> OliviaCSParser::Olivia_csContext::sequence() {
  return getRuleContexts<OliviaCSParser::SequenceContext>();
}

OliviaCSParser::SequenceContext* OliviaCSParser::Olivia_csContext::sequence(size_t i) {
  return getRuleContext<OliviaCSParser::SequenceContext>(i);
}

std::vector<OliviaCSParser::Chemical_shiftsContext *> OliviaCSParser::Olivia_csContext::chemical_shifts() {
  return getRuleContexts<OliviaCSParser::Chemical_shiftsContext>();
}

OliviaCSParser::Chemical_shiftsContext* OliviaCSParser::Olivia_csContext::chemical_shifts(size_t i) {
  return getRuleContext<OliviaCSParser::Chemical_shiftsContext>(i);
}


size_t OliviaCSParser::Olivia_csContext::getRuleIndex() const {
  return OliviaCSParser::RuleOlivia_cs;
}


std::any OliviaCSParser::Olivia_csContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaCSParserVisitor*>(visitor))
    return parserVisitor->visitOlivia_cs(this);
  else
    return visitor->visitChildren(this);
}

OliviaCSParser::Olivia_csContext* OliviaCSParser::olivia_cs() {
  Olivia_csContext *_localctx = _tracker.createInstance<Olivia_csContext>(_ctx, getState());
  enterRule(_localctx, 0, OliviaCSParser::RuleOlivia_cs);
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
    setState(15);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(14);
      match(OliviaCSParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(23);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 33794) != 0)) {
      setState(21);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(17);
        comment();
        break;
      }

      case 2: {
        setState(18);
        sequence();
        break;
      }

      case 3: {
        setState(19);
        chemical_shifts();
        break;
      }

      case 4: {
        setState(20);
        match(OliviaCSParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(25);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(26);
    match(OliviaCSParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- SequenceContext ------------------------------------------------------------------

OliviaCSParser::SequenceContext::SequenceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaCSParser::SequenceContext::Typedef() {
  return getToken(OliviaCSParser::Typedef, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::Sequence() {
  return getToken(OliviaCSParser::Sequence, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::RETURN_TD() {
  return getToken(OliviaCSParser::RETURN_TD, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::Separator() {
  return getToken(OliviaCSParser::Separator, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::RETURN_SE() {
  return getToken(OliviaCSParser::RETURN_SE, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::Format() {
  return getToken(OliviaCSParser::Format, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::Chain() {
  return getToken(OliviaCSParser::Chain, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::Resname() {
  return getToken(OliviaCSParser::Resname, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::Seqnum() {
  return getToken(OliviaCSParser::Seqnum, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::RETURN_FO() {
  return getToken(OliviaCSParser::RETURN_FO, 0);
}

std::vector<tree::TerminalNode *> OliviaCSParser::SequenceContext::Printf_string() {
  return getTokens(OliviaCSParser::Printf_string);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::Printf_string(size_t i) {
  return getToken(OliviaCSParser::Printf_string, i);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::RETURN_PF() {
  return getToken(OliviaCSParser::RETURN_PF, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::Unformat() {
  return getToken(OliviaCSParser::Unformat, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::Tab() {
  return getToken(OliviaCSParser::Tab, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::Comma() {
  return getToken(OliviaCSParser::Comma, 0);
}

tree::TerminalNode* OliviaCSParser::SequenceContext::Space() {
  return getToken(OliviaCSParser::Space, 0);
}

std::vector<OliviaCSParser::ResidueContext *> OliviaCSParser::SequenceContext::residue() {
  return getRuleContexts<OliviaCSParser::ResidueContext>();
}

OliviaCSParser::ResidueContext* OliviaCSParser::SequenceContext::residue(size_t i) {
  return getRuleContext<OliviaCSParser::ResidueContext>(i);
}


size_t OliviaCSParser::SequenceContext::getRuleIndex() const {
  return OliviaCSParser::RuleSequence;
}


std::any OliviaCSParser::SequenceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaCSParserVisitor*>(visitor))
    return parserVisitor->visitSequence(this);
  else
    return visitor->visitChildren(this);
}

OliviaCSParser::SequenceContext* OliviaCSParser::sequence() {
  SequenceContext *_localctx = _tracker.createInstance<SequenceContext>(_ctx, getState());
  enterRule(_localctx, 2, OliviaCSParser::RuleSequence);
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
    setState(28);
    match(OliviaCSParser::Typedef);
    setState(29);
    match(OliviaCSParser::Sequence);
    setState(30);
    match(OliviaCSParser::RETURN_TD);
    setState(31);
    match(OliviaCSParser::Separator);
    setState(32);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 117440512) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(33);
    match(OliviaCSParser::RETURN_SE);
    setState(34);
    match(OliviaCSParser::Format);
    setState(35);
    match(OliviaCSParser::Chain);
    setState(36);
    match(OliviaCSParser::Resname);
    setState(37);
    match(OliviaCSParser::Seqnum);
    setState(38);
    match(OliviaCSParser::RETURN_FO);
    setState(39);
    match(OliviaCSParser::Printf_string);
    setState(40);
    match(OliviaCSParser::Printf_string);
    setState(41);
    match(OliviaCSParser::Printf_string);
    setState(42);
    match(OliviaCSParser::RETURN_PF);
    setState(44); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(43);
      residue();
      setState(46); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == OliviaCSParser::Simple_name);
    setState(48);
    match(OliviaCSParser::Unformat);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ResidueContext ------------------------------------------------------------------

OliviaCSParser::ResidueContext::ResidueContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> OliviaCSParser::ResidueContext::Simple_name() {
  return getTokens(OliviaCSParser::Simple_name);
}

tree::TerminalNode* OliviaCSParser::ResidueContext::Simple_name(size_t i) {
  return getToken(OliviaCSParser::Simple_name, i);
}

tree::TerminalNode* OliviaCSParser::ResidueContext::Integer() {
  return getToken(OliviaCSParser::Integer, 0);
}

tree::TerminalNode* OliviaCSParser::ResidueContext::RETURN() {
  return getToken(OliviaCSParser::RETURN, 0);
}


size_t OliviaCSParser::ResidueContext::getRuleIndex() const {
  return OliviaCSParser::RuleResidue;
}


std::any OliviaCSParser::ResidueContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaCSParserVisitor*>(visitor))
    return parserVisitor->visitResidue(this);
  else
    return visitor->visitChildren(this);
}

OliviaCSParser::ResidueContext* OliviaCSParser::residue() {
  ResidueContext *_localctx = _tracker.createInstance<ResidueContext>(_ctx, getState());
  enterRule(_localctx, 4, OliviaCSParser::RuleResidue);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(50);
    match(OliviaCSParser::Simple_name);
    setState(51);
    match(OliviaCSParser::Simple_name);
    setState(52);
    match(OliviaCSParser::Integer);
    setState(53);
    match(OliviaCSParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Chemical_shiftsContext ------------------------------------------------------------------

OliviaCSParser::Chemical_shiftsContext::Chemical_shiftsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Typedef() {
  return getToken(OliviaCSParser::Typedef, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::RETURN_TD() {
  return getToken(OliviaCSParser::RETURN_TD, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Separator() {
  return getToken(OliviaCSParser::Separator, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::RETURN_SE() {
  return getToken(OliviaCSParser::RETURN_SE, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Format() {
  return getToken(OliviaCSParser::Format, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Chain() {
  return getToken(OliviaCSParser::Chain, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Resname() {
  return getToken(OliviaCSParser::Resname, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Seqnum() {
  return getToken(OliviaCSParser::Seqnum, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Atomname() {
  return getToken(OliviaCSParser::Atomname, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Shift() {
  return getToken(OliviaCSParser::Shift, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Stddev() {
  return getToken(OliviaCSParser::Stddev, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::RETURN_FO() {
  return getToken(OliviaCSParser::RETURN_FO, 0);
}

std::vector<tree::TerminalNode *> OliviaCSParser::Chemical_shiftsContext::Printf_string() {
  return getTokens(OliviaCSParser::Printf_string);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Printf_string(size_t i) {
  return getToken(OliviaCSParser::Printf_string, i);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::RETURN_PF() {
  return getToken(OliviaCSParser::RETURN_PF, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Unformat() {
  return getToken(OliviaCSParser::Unformat, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Ass_tbl_h2o() {
  return getToken(OliviaCSParser::Ass_tbl_h2o, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Ass_tbl_tro() {
  return getToken(OliviaCSParser::Ass_tbl_tro, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Ass_tbl_d2o() {
  return getToken(OliviaCSParser::Ass_tbl_d2o, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Tab() {
  return getToken(OliviaCSParser::Tab, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Comma() {
  return getToken(OliviaCSParser::Comma, 0);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftsContext::Space() {
  return getToken(OliviaCSParser::Space, 0);
}

std::vector<OliviaCSParser::Chemical_shiftContext *> OliviaCSParser::Chemical_shiftsContext::chemical_shift() {
  return getRuleContexts<OliviaCSParser::Chemical_shiftContext>();
}

OliviaCSParser::Chemical_shiftContext* OliviaCSParser::Chemical_shiftsContext::chemical_shift(size_t i) {
  return getRuleContext<OliviaCSParser::Chemical_shiftContext>(i);
}


size_t OliviaCSParser::Chemical_shiftsContext::getRuleIndex() const {
  return OliviaCSParser::RuleChemical_shifts;
}


std::any OliviaCSParser::Chemical_shiftsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaCSParserVisitor*>(visitor))
    return parserVisitor->visitChemical_shifts(this);
  else
    return visitor->visitChildren(this);
}

OliviaCSParser::Chemical_shiftsContext* OliviaCSParser::chemical_shifts() {
  Chemical_shiftsContext *_localctx = _tracker.createInstance<Chemical_shiftsContext>(_ctx, getState());
  enterRule(_localctx, 6, OliviaCSParser::RuleChemical_shifts);
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
    match(OliviaCSParser::Typedef);
    setState(56);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 3670016) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(57);
    match(OliviaCSParser::RETURN_TD);
    setState(58);
    match(OliviaCSParser::Separator);
    setState(59);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 117440512) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(60);
    match(OliviaCSParser::RETURN_SE);
    setState(61);
    match(OliviaCSParser::Format);
    setState(62);
    match(OliviaCSParser::Chain);
    setState(63);
    match(OliviaCSParser::Resname);
    setState(64);
    match(OliviaCSParser::Seqnum);
    setState(65);
    match(OliviaCSParser::Atomname);
    setState(66);
    match(OliviaCSParser::Shift);
    setState(67);
    match(OliviaCSParser::Stddev);
    setState(68);
    match(OliviaCSParser::RETURN_FO);
    setState(69);
    match(OliviaCSParser::Printf_string);
    setState(70);
    match(OliviaCSParser::Printf_string);
    setState(71);
    match(OliviaCSParser::Printf_string);
    setState(72);
    match(OliviaCSParser::Printf_string);
    setState(73);
    match(OliviaCSParser::Printf_string);
    setState(74);
    match(OliviaCSParser::Printf_string);
    setState(75);
    match(OliviaCSParser::RETURN_PF);
    setState(77); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(76);
      chemical_shift();
      setState(79); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == OliviaCSParser::Simple_name);
    setState(81);
    match(OliviaCSParser::Unformat);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Chemical_shiftContext ------------------------------------------------------------------

OliviaCSParser::Chemical_shiftContext::Chemical_shiftContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> OliviaCSParser::Chemical_shiftContext::Simple_name() {
  return getTokens(OliviaCSParser::Simple_name);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftContext::Simple_name(size_t i) {
  return getToken(OliviaCSParser::Simple_name, i);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftContext::Integer() {
  return getToken(OliviaCSParser::Integer, 0);
}

std::vector<OliviaCSParser::NumberContext *> OliviaCSParser::Chemical_shiftContext::number() {
  return getRuleContexts<OliviaCSParser::NumberContext>();
}

OliviaCSParser::NumberContext* OliviaCSParser::Chemical_shiftContext::number(size_t i) {
  return getRuleContext<OliviaCSParser::NumberContext>(i);
}

tree::TerminalNode* OliviaCSParser::Chemical_shiftContext::RETURN() {
  return getToken(OliviaCSParser::RETURN, 0);
}


size_t OliviaCSParser::Chemical_shiftContext::getRuleIndex() const {
  return OliviaCSParser::RuleChemical_shift;
}


std::any OliviaCSParser::Chemical_shiftContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaCSParserVisitor*>(visitor))
    return parserVisitor->visitChemical_shift(this);
  else
    return visitor->visitChildren(this);
}

OliviaCSParser::Chemical_shiftContext* OliviaCSParser::chemical_shift() {
  Chemical_shiftContext *_localctx = _tracker.createInstance<Chemical_shiftContext>(_ctx, getState());
  enterRule(_localctx, 8, OliviaCSParser::RuleChemical_shift);

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
    match(OliviaCSParser::Simple_name);
    setState(84);
    match(OliviaCSParser::Simple_name);
    setState(85);
    match(OliviaCSParser::Integer);
    setState(86);
    match(OliviaCSParser::Simple_name);
    setState(87);
    number();
    setState(88);
    number();
    setState(89);
    match(OliviaCSParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberContext ------------------------------------------------------------------

OliviaCSParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaCSParser::NumberContext::Integer() {
  return getToken(OliviaCSParser::Integer, 0);
}

tree::TerminalNode* OliviaCSParser::NumberContext::Float() {
  return getToken(OliviaCSParser::Float, 0);
}

tree::TerminalNode* OliviaCSParser::NumberContext::Real() {
  return getToken(OliviaCSParser::Real, 0);
}


size_t OliviaCSParser::NumberContext::getRuleIndex() const {
  return OliviaCSParser::RuleNumber;
}


std::any OliviaCSParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaCSParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

OliviaCSParser::NumberContext* OliviaCSParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 10, OliviaCSParser::RuleNumber);
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
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 896) != 0))) {
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

//----------------- CommentContext ------------------------------------------------------------------

OliviaCSParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* OliviaCSParser::CommentContext::COMMENT() {
  return getToken(OliviaCSParser::COMMENT, 0);
}

tree::TerminalNode* OliviaCSParser::CommentContext::RETURN_CM() {
  return getToken(OliviaCSParser::RETURN_CM, 0);
}

std::vector<tree::TerminalNode *> OliviaCSParser::CommentContext::Any_name() {
  return getTokens(OliviaCSParser::Any_name);
}

tree::TerminalNode* OliviaCSParser::CommentContext::Any_name(size_t i) {
  return getToken(OliviaCSParser::Any_name, i);
}


size_t OliviaCSParser::CommentContext::getRuleIndex() const {
  return OliviaCSParser::RuleComment;
}


std::any OliviaCSParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<OliviaCSParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

OliviaCSParser::CommentContext* OliviaCSParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 12, OliviaCSParser::RuleComment);
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
    setState(93);
    match(OliviaCSParser::COMMENT);
    setState(97);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == OliviaCSParser::Any_name) {
      setState(94);
      match(OliviaCSParser::Any_name);
      setState(99);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(100);
    match(OliviaCSParser::RETURN_CM);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

void OliviaCSParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  oliviacsparserParserInitialize();
#else
  ::antlr4::internal::call_once(oliviacsparserParserOnceFlag, oliviacsparserParserInitialize);
#endif
}
