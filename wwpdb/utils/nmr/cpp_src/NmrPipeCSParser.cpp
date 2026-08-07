
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrPipeCSParser.g4 by ANTLR 4.13.0


#include "NmrPipeCSParserVisitor.h"

#include "NmrPipeCSParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct NmrPipeCSParserStaticData final {
  NmrPipeCSParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  NmrPipeCSParserStaticData(const NmrPipeCSParserStaticData&) = delete;
  NmrPipeCSParserStaticData(NmrPipeCSParserStaticData&&) = delete;
  NmrPipeCSParserStaticData& operator=(const NmrPipeCSParserStaticData&) = delete;
  NmrPipeCSParserStaticData& operator=(NmrPipeCSParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag nmrpipecsparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
NmrPipeCSParserStaticData *nmrpipecsparserParserStaticData = nullptr;

void nmrpipecsparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (nmrpipecsparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(nmrpipecsparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<NmrPipeCSParserStaticData>(
    std::vector<std::string>{
      "nmrpipe_cs", "sequence", "chemical_shifts", "chemical_shift", "chemical_shifts_sw_segid", 
      "chemical_shift_sw_segid", "chemical_shifts_ew_segid", "chemical_shift_ew_segid", 
      "number"
    },
    std::vector<std::string>{
      "", "'DATA'", "'VARS'", "'FORMAT'", "", "", "", "", "", "", "", "", 
      "", "", "", "'FIRST_RESID'", "'SEQUENCE'", "'DB_NAME'", "'TAB_NAME'", 
      "'TAB_ID'", "", "", "", "", "", "", "", "", "", "'SEGNAME'", "'RESID'", 
      "'RESNAME'", "'ATOMNAME'", "'SHIFT'"
    },
    std::vector<std::string>{
      "", "Data", "Vars", "Format", "Integer", "Float", "Float_DecimalComma", 
      "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", "Simple_name", 
      "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT", "First_resid", 
      "Sequence", "Db_name", "Tab_name", "Tab_id", "Integer_DA", "Simple_name_DA", 
      "SPACE_DA", "RETURN_DA", "LINE_COMMENT_DA", "One_letter_code", "SPACE_SQ", 
      "RETURN_SQ", "LINE_COMMENT_SQ", "Segname", "Resid", "Resname", "Atomname", 
      "Shift", "SPACE_VA", "RETURN_VA", "LINE_COMMENT_VA", "Format_code", 
      "SPACE_FO", "RETURN_FO", "LINE_COMMENT_FO"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,40,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,1,0,1,0,1,1,
  	1,1,1,1,1,1,1,1,1,1,4,1,36,8,1,11,1,12,1,37,1,1,1,1,1,1,1,1,1,1,1,1,5,
  	1,46,8,1,10,1,12,1,49,9,1,1,1,1,1,1,1,1,1,3,1,55,8,1,1,2,1,2,1,2,1,2,
  	1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,70,8,2,11,2,12,2,71,1,3,1,3,1,
  	3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
  	4,4,94,8,4,11,4,12,4,95,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
  	6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,119,8,6,11,6,12,6,120,1,7,1,
  	7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,4,6,
  	134,0,24,1,0,0,0,2,29,1,0,0,0,4,56,1,0,0,0,6,73,1,0,0,0,8,78,1,0,0,0,
  	10,97,1,0,0,0,12,103,1,0,0,0,14,122,1,0,0,0,16,128,1,0,0,0,18,23,3,2,
  	1,0,19,23,3,4,2,0,20,23,3,8,4,0,21,23,3,12,6,0,22,18,1,0,0,0,22,19,1,
  	0,0,0,22,20,1,0,0,0,22,21,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,
  	0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,54,5,
  	1,0,0,30,31,5,15,0,0,31,32,5,20,0,0,32,55,5,23,0,0,33,35,5,16,0,0,34,
  	36,5,25,0,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,
  	39,1,0,0,0,39,55,5,27,0,0,40,41,5,17,0,0,41,42,5,21,0,0,42,55,5,23,0,
  	0,43,47,5,18,0,0,44,46,5,21,0,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,
  	0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,55,5,23,0,0,51,52,5,
  	19,0,0,52,53,5,20,0,0,53,55,5,23,0,0,54,30,1,0,0,0,54,33,1,0,0,0,54,40,
  	1,0,0,0,54,43,1,0,0,0,54,51,1,0,0,0,55,3,1,0,0,0,56,57,5,2,0,0,57,58,
  	5,30,0,0,58,59,5,31,0,0,59,60,5,32,0,0,60,61,5,33,0,0,61,62,5,35,0,0,
  	62,63,5,3,0,0,63,64,5,37,0,0,64,65,5,37,0,0,65,66,5,37,0,0,66,67,5,37,
  	0,0,67,69,5,39,0,0,68,70,3,6,3,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,
  	0,0,0,71,72,1,0,0,0,72,5,1,0,0,0,73,74,5,4,0,0,74,75,5,10,0,0,75,76,5,
  	10,0,0,76,77,3,16,8,0,77,7,1,0,0,0,78,79,5,2,0,0,79,80,5,29,0,0,80,81,
  	5,30,0,0,81,82,5,31,0,0,82,83,5,32,0,0,83,84,5,33,0,0,84,85,5,35,0,0,
  	85,86,5,3,0,0,86,87,5,37,0,0,87,88,5,37,0,0,88,89,5,37,0,0,89,90,5,37,
  	0,0,90,91,5,37,0,0,91,93,5,39,0,0,92,94,3,10,5,0,93,92,1,0,0,0,94,95,
  	1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,9,1,0,0,0,97,98,5,10,0,0,98,99,
  	5,4,0,0,99,100,5,10,0,0,100,101,5,10,0,0,101,102,3,16,8,0,102,11,1,0,
  	0,0,103,104,5,2,0,0,104,105,5,30,0,0,105,106,5,31,0,0,106,107,5,32,0,
  	0,107,108,5,29,0,0,108,109,5,33,0,0,109,110,5,35,0,0,110,111,5,3,0,0,
  	111,112,5,37,0,0,112,113,5,37,0,0,113,114,5,37,0,0,114,115,5,37,0,0,115,
  	116,5,37,0,0,116,118,5,39,0,0,117,119,3,14,7,0,118,117,1,0,0,0,119,120,
  	1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,13,1,0,0,0,122,123,5,4,0,
  	0,123,124,5,10,0,0,124,125,5,10,0,0,125,126,5,10,0,0,126,127,3,16,8,0,
  	127,15,1,0,0,0,128,129,7,0,0,0,129,17,1,0,0,0,8,22,24,37,47,54,71,95,
  	120
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  nmrpipecsparserParserStaticData = staticData.release();
}

}

NmrPipeCSParser::NmrPipeCSParser(TokenStream *input) : NmrPipeCSParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

NmrPipeCSParser::NmrPipeCSParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  NmrPipeCSParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *nmrpipecsparserParserStaticData->atn, nmrpipecsparserParserStaticData->decisionToDFA, nmrpipecsparserParserStaticData->sharedContextCache, options);
}

NmrPipeCSParser::~NmrPipeCSParser() {
  delete _interpreter;
}

const atn::ATN& NmrPipeCSParser::getATN() const {
  return *nmrpipecsparserParserStaticData->atn;
}

std::string NmrPipeCSParser::getGrammarFileName() const {
  return "NmrPipeCSParser.g4";
}

const std::vector<std::string>& NmrPipeCSParser::getRuleNames() const {
  return nmrpipecsparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& NmrPipeCSParser::getVocabulary() const {
  return nmrpipecsparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView NmrPipeCSParser::getSerializedATN() const {
  return nmrpipecsparserParserStaticData->serializedATN;
}


//----------------- Nmrpipe_csContext ------------------------------------------------------------------

NmrPipeCSParser::Nmrpipe_csContext::Nmrpipe_csContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipeCSParser::Nmrpipe_csContext::EOF() {
  return getToken(NmrPipeCSParser::EOF, 0);
}

std::vector<NmrPipeCSParser::SequenceContext *> NmrPipeCSParser::Nmrpipe_csContext::sequence() {
  return getRuleContexts<NmrPipeCSParser::SequenceContext>();
}

NmrPipeCSParser::SequenceContext* NmrPipeCSParser::Nmrpipe_csContext::sequence(size_t i) {
  return getRuleContext<NmrPipeCSParser::SequenceContext>(i);
}

std::vector<NmrPipeCSParser::Chemical_shiftsContext *> NmrPipeCSParser::Nmrpipe_csContext::chemical_shifts() {
  return getRuleContexts<NmrPipeCSParser::Chemical_shiftsContext>();
}

NmrPipeCSParser::Chemical_shiftsContext* NmrPipeCSParser::Nmrpipe_csContext::chemical_shifts(size_t i) {
  return getRuleContext<NmrPipeCSParser::Chemical_shiftsContext>(i);
}

std::vector<NmrPipeCSParser::Chemical_shifts_sw_segidContext *> NmrPipeCSParser::Nmrpipe_csContext::chemical_shifts_sw_segid() {
  return getRuleContexts<NmrPipeCSParser::Chemical_shifts_sw_segidContext>();
}

NmrPipeCSParser::Chemical_shifts_sw_segidContext* NmrPipeCSParser::Nmrpipe_csContext::chemical_shifts_sw_segid(size_t i) {
  return getRuleContext<NmrPipeCSParser::Chemical_shifts_sw_segidContext>(i);
}

std::vector<NmrPipeCSParser::Chemical_shifts_ew_segidContext *> NmrPipeCSParser::Nmrpipe_csContext::chemical_shifts_ew_segid() {
  return getRuleContexts<NmrPipeCSParser::Chemical_shifts_ew_segidContext>();
}

NmrPipeCSParser::Chemical_shifts_ew_segidContext* NmrPipeCSParser::Nmrpipe_csContext::chemical_shifts_ew_segid(size_t i) {
  return getRuleContext<NmrPipeCSParser::Chemical_shifts_ew_segidContext>(i);
}


size_t NmrPipeCSParser::Nmrpipe_csContext::getRuleIndex() const {
  return NmrPipeCSParser::RuleNmrpipe_cs;
}


std::any NmrPipeCSParser::Nmrpipe_csContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipeCSParserVisitor*>(visitor))
    return parserVisitor->visitNmrpipe_cs(this);
  else
    return visitor->visitChildren(this);
}

NmrPipeCSParser::Nmrpipe_csContext* NmrPipeCSParser::nmrpipe_cs() {
  Nmrpipe_csContext *_localctx = _tracker.createInstance<Nmrpipe_csContext>(_ctx, getState());
  enterRule(_localctx, 0, NmrPipeCSParser::RuleNmrpipe_cs);
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
    setState(24);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == NmrPipeCSParser::Data

    || _la == NmrPipeCSParser::Vars) {
      setState(22);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
      case 1: {
        setState(18);
        sequence();
        break;
      }

      case 2: {
        setState(19);
        chemical_shifts();
        break;
      }

      case 3: {
        setState(20);
        chemical_shifts_sw_segid();
        break;
      }

      case 4: {
        setState(21);
        chemical_shifts_ew_segid();
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
    match(NmrPipeCSParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- SequenceContext ------------------------------------------------------------------

NmrPipeCSParser::SequenceContext::SequenceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipeCSParser::SequenceContext::Data() {
  return getToken(NmrPipeCSParser::Data, 0);
}

tree::TerminalNode* NmrPipeCSParser::SequenceContext::First_resid() {
  return getToken(NmrPipeCSParser::First_resid, 0);
}

tree::TerminalNode* NmrPipeCSParser::SequenceContext::Integer_DA() {
  return getToken(NmrPipeCSParser::Integer_DA, 0);
}

tree::TerminalNode* NmrPipeCSParser::SequenceContext::RETURN_DA() {
  return getToken(NmrPipeCSParser::RETURN_DA, 0);
}

tree::TerminalNode* NmrPipeCSParser::SequenceContext::Sequence() {
  return getToken(NmrPipeCSParser::Sequence, 0);
}

tree::TerminalNode* NmrPipeCSParser::SequenceContext::RETURN_SQ() {
  return getToken(NmrPipeCSParser::RETURN_SQ, 0);
}

tree::TerminalNode* NmrPipeCSParser::SequenceContext::Db_name() {
  return getToken(NmrPipeCSParser::Db_name, 0);
}

std::vector<tree::TerminalNode *> NmrPipeCSParser::SequenceContext::Simple_name_DA() {
  return getTokens(NmrPipeCSParser::Simple_name_DA);
}

tree::TerminalNode* NmrPipeCSParser::SequenceContext::Simple_name_DA(size_t i) {
  return getToken(NmrPipeCSParser::Simple_name_DA, i);
}

tree::TerminalNode* NmrPipeCSParser::SequenceContext::Tab_name() {
  return getToken(NmrPipeCSParser::Tab_name, 0);
}

tree::TerminalNode* NmrPipeCSParser::SequenceContext::Tab_id() {
  return getToken(NmrPipeCSParser::Tab_id, 0);
}

std::vector<tree::TerminalNode *> NmrPipeCSParser::SequenceContext::One_letter_code() {
  return getTokens(NmrPipeCSParser::One_letter_code);
}

tree::TerminalNode* NmrPipeCSParser::SequenceContext::One_letter_code(size_t i) {
  return getToken(NmrPipeCSParser::One_letter_code, i);
}


size_t NmrPipeCSParser::SequenceContext::getRuleIndex() const {
  return NmrPipeCSParser::RuleSequence;
}


std::any NmrPipeCSParser::SequenceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipeCSParserVisitor*>(visitor))
    return parserVisitor->visitSequence(this);
  else
    return visitor->visitChildren(this);
}

NmrPipeCSParser::SequenceContext* NmrPipeCSParser::sequence() {
  SequenceContext *_localctx = _tracker.createInstance<SequenceContext>(_ctx, getState());
  enterRule(_localctx, 2, NmrPipeCSParser::RuleSequence);
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
    match(NmrPipeCSParser::Data);
    setState(54);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case NmrPipeCSParser::First_resid: {
        setState(30);
        match(NmrPipeCSParser::First_resid);
        setState(31);
        match(NmrPipeCSParser::Integer_DA);
        setState(32);
        match(NmrPipeCSParser::RETURN_DA);
        break;
      }

      case NmrPipeCSParser::Sequence: {
        setState(33);
        match(NmrPipeCSParser::Sequence);
        setState(35); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(34);
          match(NmrPipeCSParser::One_letter_code);
          setState(37); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == NmrPipeCSParser::One_letter_code);
        setState(39);
        match(NmrPipeCSParser::RETURN_SQ);
        break;
      }

      case NmrPipeCSParser::Db_name: {
        setState(40);
        match(NmrPipeCSParser::Db_name);
        setState(41);
        match(NmrPipeCSParser::Simple_name_DA);
        setState(42);
        match(NmrPipeCSParser::RETURN_DA);
        break;
      }

      case NmrPipeCSParser::Tab_name: {
        setState(43);
        match(NmrPipeCSParser::Tab_name);
        setState(47);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == NmrPipeCSParser::Simple_name_DA) {
          setState(44);
          match(NmrPipeCSParser::Simple_name_DA);
          setState(49);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        setState(50);
        match(NmrPipeCSParser::RETURN_DA);
        break;
      }

      case NmrPipeCSParser::Tab_id: {
        setState(51);
        match(NmrPipeCSParser::Tab_id);
        setState(52);
        match(NmrPipeCSParser::Integer_DA);
        setState(53);
        match(NmrPipeCSParser::RETURN_DA);
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

//----------------- Chemical_shiftsContext ------------------------------------------------------------------

NmrPipeCSParser::Chemical_shiftsContext::Chemical_shiftsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shiftsContext::Vars() {
  return getToken(NmrPipeCSParser::Vars, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shiftsContext::Resid() {
  return getToken(NmrPipeCSParser::Resid, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shiftsContext::Resname() {
  return getToken(NmrPipeCSParser::Resname, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shiftsContext::Atomname() {
  return getToken(NmrPipeCSParser::Atomname, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shiftsContext::Shift() {
  return getToken(NmrPipeCSParser::Shift, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shiftsContext::RETURN_VA() {
  return getToken(NmrPipeCSParser::RETURN_VA, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shiftsContext::Format() {
  return getToken(NmrPipeCSParser::Format, 0);
}

std::vector<tree::TerminalNode *> NmrPipeCSParser::Chemical_shiftsContext::Format_code() {
  return getTokens(NmrPipeCSParser::Format_code);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shiftsContext::Format_code(size_t i) {
  return getToken(NmrPipeCSParser::Format_code, i);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shiftsContext::RETURN_FO() {
  return getToken(NmrPipeCSParser::RETURN_FO, 0);
}

std::vector<NmrPipeCSParser::Chemical_shiftContext *> NmrPipeCSParser::Chemical_shiftsContext::chemical_shift() {
  return getRuleContexts<NmrPipeCSParser::Chemical_shiftContext>();
}

NmrPipeCSParser::Chemical_shiftContext* NmrPipeCSParser::Chemical_shiftsContext::chemical_shift(size_t i) {
  return getRuleContext<NmrPipeCSParser::Chemical_shiftContext>(i);
}


size_t NmrPipeCSParser::Chemical_shiftsContext::getRuleIndex() const {
  return NmrPipeCSParser::RuleChemical_shifts;
}


std::any NmrPipeCSParser::Chemical_shiftsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipeCSParserVisitor*>(visitor))
    return parserVisitor->visitChemical_shifts(this);
  else
    return visitor->visitChildren(this);
}

NmrPipeCSParser::Chemical_shiftsContext* NmrPipeCSParser::chemical_shifts() {
  Chemical_shiftsContext *_localctx = _tracker.createInstance<Chemical_shiftsContext>(_ctx, getState());
  enterRule(_localctx, 4, NmrPipeCSParser::RuleChemical_shifts);
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
    setState(56);
    match(NmrPipeCSParser::Vars);
    setState(57);
    match(NmrPipeCSParser::Resid);
    setState(58);
    match(NmrPipeCSParser::Resname);
    setState(59);
    match(NmrPipeCSParser::Atomname);
    setState(60);
    match(NmrPipeCSParser::Shift);
    setState(61);
    match(NmrPipeCSParser::RETURN_VA);
    setState(62);
    match(NmrPipeCSParser::Format);
    setState(63);
    match(NmrPipeCSParser::Format_code);
    setState(64);
    match(NmrPipeCSParser::Format_code);
    setState(65);
    match(NmrPipeCSParser::Format_code);
    setState(66);
    match(NmrPipeCSParser::Format_code);
    setState(67);
    match(NmrPipeCSParser::RETURN_FO);
    setState(69); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(68);
      chemical_shift();
      setState(71); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrPipeCSParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Chemical_shiftContext ------------------------------------------------------------------

NmrPipeCSParser::Chemical_shiftContext::Chemical_shiftContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shiftContext::Integer() {
  return getToken(NmrPipeCSParser::Integer, 0);
}

std::vector<tree::TerminalNode *> NmrPipeCSParser::Chemical_shiftContext::Simple_name() {
  return getTokens(NmrPipeCSParser::Simple_name);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shiftContext::Simple_name(size_t i) {
  return getToken(NmrPipeCSParser::Simple_name, i);
}

NmrPipeCSParser::NumberContext* NmrPipeCSParser::Chemical_shiftContext::number() {
  return getRuleContext<NmrPipeCSParser::NumberContext>(0);
}


size_t NmrPipeCSParser::Chemical_shiftContext::getRuleIndex() const {
  return NmrPipeCSParser::RuleChemical_shift;
}


std::any NmrPipeCSParser::Chemical_shiftContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipeCSParserVisitor*>(visitor))
    return parserVisitor->visitChemical_shift(this);
  else
    return visitor->visitChildren(this);
}

NmrPipeCSParser::Chemical_shiftContext* NmrPipeCSParser::chemical_shift() {
  Chemical_shiftContext *_localctx = _tracker.createInstance<Chemical_shiftContext>(_ctx, getState());
  enterRule(_localctx, 6, NmrPipeCSParser::RuleChemical_shift);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(73);
    match(NmrPipeCSParser::Integer);
    setState(74);
    match(NmrPipeCSParser::Simple_name);
    setState(75);
    match(NmrPipeCSParser::Simple_name);
    setState(76);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Chemical_shifts_sw_segidContext ------------------------------------------------------------------

NmrPipeCSParser::Chemical_shifts_sw_segidContext::Chemical_shifts_sw_segidContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_sw_segidContext::Vars() {
  return getToken(NmrPipeCSParser::Vars, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_sw_segidContext::Segname() {
  return getToken(NmrPipeCSParser::Segname, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_sw_segidContext::Resid() {
  return getToken(NmrPipeCSParser::Resid, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_sw_segidContext::Resname() {
  return getToken(NmrPipeCSParser::Resname, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_sw_segidContext::Atomname() {
  return getToken(NmrPipeCSParser::Atomname, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_sw_segidContext::Shift() {
  return getToken(NmrPipeCSParser::Shift, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_sw_segidContext::RETURN_VA() {
  return getToken(NmrPipeCSParser::RETURN_VA, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_sw_segidContext::Format() {
  return getToken(NmrPipeCSParser::Format, 0);
}

std::vector<tree::TerminalNode *> NmrPipeCSParser::Chemical_shifts_sw_segidContext::Format_code() {
  return getTokens(NmrPipeCSParser::Format_code);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_sw_segidContext::Format_code(size_t i) {
  return getToken(NmrPipeCSParser::Format_code, i);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_sw_segidContext::RETURN_FO() {
  return getToken(NmrPipeCSParser::RETURN_FO, 0);
}

std::vector<NmrPipeCSParser::Chemical_shift_sw_segidContext *> NmrPipeCSParser::Chemical_shifts_sw_segidContext::chemical_shift_sw_segid() {
  return getRuleContexts<NmrPipeCSParser::Chemical_shift_sw_segidContext>();
}

NmrPipeCSParser::Chemical_shift_sw_segidContext* NmrPipeCSParser::Chemical_shifts_sw_segidContext::chemical_shift_sw_segid(size_t i) {
  return getRuleContext<NmrPipeCSParser::Chemical_shift_sw_segidContext>(i);
}


size_t NmrPipeCSParser::Chemical_shifts_sw_segidContext::getRuleIndex() const {
  return NmrPipeCSParser::RuleChemical_shifts_sw_segid;
}


std::any NmrPipeCSParser::Chemical_shifts_sw_segidContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipeCSParserVisitor*>(visitor))
    return parserVisitor->visitChemical_shifts_sw_segid(this);
  else
    return visitor->visitChildren(this);
}

NmrPipeCSParser::Chemical_shifts_sw_segidContext* NmrPipeCSParser::chemical_shifts_sw_segid() {
  Chemical_shifts_sw_segidContext *_localctx = _tracker.createInstance<Chemical_shifts_sw_segidContext>(_ctx, getState());
  enterRule(_localctx, 8, NmrPipeCSParser::RuleChemical_shifts_sw_segid);
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
    setState(78);
    match(NmrPipeCSParser::Vars);
    setState(79);
    match(NmrPipeCSParser::Segname);
    setState(80);
    match(NmrPipeCSParser::Resid);
    setState(81);
    match(NmrPipeCSParser::Resname);
    setState(82);
    match(NmrPipeCSParser::Atomname);
    setState(83);
    match(NmrPipeCSParser::Shift);
    setState(84);
    match(NmrPipeCSParser::RETURN_VA);
    setState(85);
    match(NmrPipeCSParser::Format);
    setState(86);
    match(NmrPipeCSParser::Format_code);
    setState(87);
    match(NmrPipeCSParser::Format_code);
    setState(88);
    match(NmrPipeCSParser::Format_code);
    setState(89);
    match(NmrPipeCSParser::Format_code);
    setState(90);
    match(NmrPipeCSParser::Format_code);
    setState(91);
    match(NmrPipeCSParser::RETURN_FO);
    setState(93); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(92);
      chemical_shift_sw_segid();
      setState(95); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrPipeCSParser::Simple_name);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Chemical_shift_sw_segidContext ------------------------------------------------------------------

NmrPipeCSParser::Chemical_shift_sw_segidContext::Chemical_shift_sw_segidContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrPipeCSParser::Chemical_shift_sw_segidContext::Simple_name() {
  return getTokens(NmrPipeCSParser::Simple_name);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shift_sw_segidContext::Simple_name(size_t i) {
  return getToken(NmrPipeCSParser::Simple_name, i);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shift_sw_segidContext::Integer() {
  return getToken(NmrPipeCSParser::Integer, 0);
}

NmrPipeCSParser::NumberContext* NmrPipeCSParser::Chemical_shift_sw_segidContext::number() {
  return getRuleContext<NmrPipeCSParser::NumberContext>(0);
}


size_t NmrPipeCSParser::Chemical_shift_sw_segidContext::getRuleIndex() const {
  return NmrPipeCSParser::RuleChemical_shift_sw_segid;
}


std::any NmrPipeCSParser::Chemical_shift_sw_segidContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipeCSParserVisitor*>(visitor))
    return parserVisitor->visitChemical_shift_sw_segid(this);
  else
    return visitor->visitChildren(this);
}

NmrPipeCSParser::Chemical_shift_sw_segidContext* NmrPipeCSParser::chemical_shift_sw_segid() {
  Chemical_shift_sw_segidContext *_localctx = _tracker.createInstance<Chemical_shift_sw_segidContext>(_ctx, getState());
  enterRule(_localctx, 10, NmrPipeCSParser::RuleChemical_shift_sw_segid);

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
    match(NmrPipeCSParser::Simple_name);
    setState(98);
    match(NmrPipeCSParser::Integer);
    setState(99);
    match(NmrPipeCSParser::Simple_name);
    setState(100);
    match(NmrPipeCSParser::Simple_name);
    setState(101);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Chemical_shifts_ew_segidContext ------------------------------------------------------------------

NmrPipeCSParser::Chemical_shifts_ew_segidContext::Chemical_shifts_ew_segidContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_ew_segidContext::Vars() {
  return getToken(NmrPipeCSParser::Vars, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_ew_segidContext::Resid() {
  return getToken(NmrPipeCSParser::Resid, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_ew_segidContext::Resname() {
  return getToken(NmrPipeCSParser::Resname, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_ew_segidContext::Atomname() {
  return getToken(NmrPipeCSParser::Atomname, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_ew_segidContext::Segname() {
  return getToken(NmrPipeCSParser::Segname, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_ew_segidContext::Shift() {
  return getToken(NmrPipeCSParser::Shift, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_ew_segidContext::RETURN_VA() {
  return getToken(NmrPipeCSParser::RETURN_VA, 0);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_ew_segidContext::Format() {
  return getToken(NmrPipeCSParser::Format, 0);
}

std::vector<tree::TerminalNode *> NmrPipeCSParser::Chemical_shifts_ew_segidContext::Format_code() {
  return getTokens(NmrPipeCSParser::Format_code);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_ew_segidContext::Format_code(size_t i) {
  return getToken(NmrPipeCSParser::Format_code, i);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shifts_ew_segidContext::RETURN_FO() {
  return getToken(NmrPipeCSParser::RETURN_FO, 0);
}

std::vector<NmrPipeCSParser::Chemical_shift_ew_segidContext *> NmrPipeCSParser::Chemical_shifts_ew_segidContext::chemical_shift_ew_segid() {
  return getRuleContexts<NmrPipeCSParser::Chemical_shift_ew_segidContext>();
}

NmrPipeCSParser::Chemical_shift_ew_segidContext* NmrPipeCSParser::Chemical_shifts_ew_segidContext::chemical_shift_ew_segid(size_t i) {
  return getRuleContext<NmrPipeCSParser::Chemical_shift_ew_segidContext>(i);
}


size_t NmrPipeCSParser::Chemical_shifts_ew_segidContext::getRuleIndex() const {
  return NmrPipeCSParser::RuleChemical_shifts_ew_segid;
}


std::any NmrPipeCSParser::Chemical_shifts_ew_segidContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipeCSParserVisitor*>(visitor))
    return parserVisitor->visitChemical_shifts_ew_segid(this);
  else
    return visitor->visitChildren(this);
}

NmrPipeCSParser::Chemical_shifts_ew_segidContext* NmrPipeCSParser::chemical_shifts_ew_segid() {
  Chemical_shifts_ew_segidContext *_localctx = _tracker.createInstance<Chemical_shifts_ew_segidContext>(_ctx, getState());
  enterRule(_localctx, 12, NmrPipeCSParser::RuleChemical_shifts_ew_segid);
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
    setState(103);
    match(NmrPipeCSParser::Vars);
    setState(104);
    match(NmrPipeCSParser::Resid);
    setState(105);
    match(NmrPipeCSParser::Resname);
    setState(106);
    match(NmrPipeCSParser::Atomname);
    setState(107);
    match(NmrPipeCSParser::Segname);
    setState(108);
    match(NmrPipeCSParser::Shift);
    setState(109);
    match(NmrPipeCSParser::RETURN_VA);
    setState(110);
    match(NmrPipeCSParser::Format);
    setState(111);
    match(NmrPipeCSParser::Format_code);
    setState(112);
    match(NmrPipeCSParser::Format_code);
    setState(113);
    match(NmrPipeCSParser::Format_code);
    setState(114);
    match(NmrPipeCSParser::Format_code);
    setState(115);
    match(NmrPipeCSParser::Format_code);
    setState(116);
    match(NmrPipeCSParser::RETURN_FO);
    setState(118); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(117);
      chemical_shift_ew_segid();
      setState(120); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrPipeCSParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Chemical_shift_ew_segidContext ------------------------------------------------------------------

NmrPipeCSParser::Chemical_shift_ew_segidContext::Chemical_shift_ew_segidContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shift_ew_segidContext::Integer() {
  return getToken(NmrPipeCSParser::Integer, 0);
}

std::vector<tree::TerminalNode *> NmrPipeCSParser::Chemical_shift_ew_segidContext::Simple_name() {
  return getTokens(NmrPipeCSParser::Simple_name);
}

tree::TerminalNode* NmrPipeCSParser::Chemical_shift_ew_segidContext::Simple_name(size_t i) {
  return getToken(NmrPipeCSParser::Simple_name, i);
}

NmrPipeCSParser::NumberContext* NmrPipeCSParser::Chemical_shift_ew_segidContext::number() {
  return getRuleContext<NmrPipeCSParser::NumberContext>(0);
}


size_t NmrPipeCSParser::Chemical_shift_ew_segidContext::getRuleIndex() const {
  return NmrPipeCSParser::RuleChemical_shift_ew_segid;
}


std::any NmrPipeCSParser::Chemical_shift_ew_segidContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipeCSParserVisitor*>(visitor))
    return parserVisitor->visitChemical_shift_ew_segid(this);
  else
    return visitor->visitChildren(this);
}

NmrPipeCSParser::Chemical_shift_ew_segidContext* NmrPipeCSParser::chemical_shift_ew_segid() {
  Chemical_shift_ew_segidContext *_localctx = _tracker.createInstance<Chemical_shift_ew_segidContext>(_ctx, getState());
  enterRule(_localctx, 14, NmrPipeCSParser::RuleChemical_shift_ew_segid);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(122);
    match(NmrPipeCSParser::Integer);
    setState(123);
    match(NmrPipeCSParser::Simple_name);
    setState(124);
    match(NmrPipeCSParser::Simple_name);
    setState(125);
    match(NmrPipeCSParser::Simple_name);
    setState(126);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberContext ------------------------------------------------------------------

NmrPipeCSParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrPipeCSParser::NumberContext::Float() {
  return getToken(NmrPipeCSParser::Float, 0);
}

tree::TerminalNode* NmrPipeCSParser::NumberContext::Float_DecimalComma() {
  return getToken(NmrPipeCSParser::Float_DecimalComma, 0);
}

tree::TerminalNode* NmrPipeCSParser::NumberContext::Integer() {
  return getToken(NmrPipeCSParser::Integer, 0);
}


size_t NmrPipeCSParser::NumberContext::getRuleIndex() const {
  return NmrPipeCSParser::RuleNumber;
}


std::any NmrPipeCSParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrPipeCSParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

NmrPipeCSParser::NumberContext* NmrPipeCSParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 16, NmrPipeCSParser::RuleNumber);
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
    setState(128);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 112) != 0))) {
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

void NmrPipeCSParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  nmrpipecsparserParserInitialize();
#else
  ::antlr4::internal::call_once(nmrpipecsparserParserOnceFlag, nmrpipecsparserParserInitialize);
#endif
}
