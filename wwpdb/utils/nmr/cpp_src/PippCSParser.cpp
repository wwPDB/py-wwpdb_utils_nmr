
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PippCSParser.g4 by ANTLR 4.13.2


#include "PippCSParserVisitor.h"

#include "PippCSParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct PippCSParserStaticData final {
  PippCSParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  PippCSParserStaticData(const PippCSParserStaticData&) = delete;
  PippCSParserStaticData(PippCSParserStaticData&&) = delete;
  PippCSParserStaticData& operator=(const PippCSParserStaticData&) = delete;
  PippCSParserStaticData& operator=(PippCSParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag pippcsparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<PippCSParserStaticData> pippcsparserParserStaticData = nullptr;

void pippcsparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (pippcsparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(pippcsparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<PippCSParserStaticData>(
    std::vector<std::string>{
      "pipp_cs", "pipp_format", "ext_peak_pick_tbl", "ext_peak_pick_tbl_row", 
      "residue_list", "res_id", "res_type", "shift_list", "number"
    },
    std::vector<std::string>{
      "", "'SHIFT_FL_FRMT'", "'RES_SIAD'", "'FIRST_RES_IN_SEQ'", "'EXP_PEAK_PICK_TBL'", 
      "", "'RES_TYPE'", "'PREV_TYPE'", "'CUR_TYPE'", "'SPIN_SYSTEM_ID'", 
      "'HETEROGENEITY'", "'END_RES_DEF'", "", "'('", "", "", "", "", "", 
      "", "", "", "", "", "", "'Label'", "'Exp Par Fl'", "'Peak-Pick Fl'", 
      "'#-Cross-Ref'", "", "", "", "", "')'"
    },
    std::vector<std::string>{
      "", "Shift_fl_frmt", "Res_siad", "First_res_in_seq", "Exp_peak_pick_tbl", 
      "Res_ID", "Res_type", "Prev_type", "Cur_type", "Spin_system_ID", "Heterogeneity", 
      "End_res_def", "Type_pred", "Note_begin", "Integer", "Float", "SHARP_COMMENT", 
      "EXCLM_COMMENT", "Simple_name", "CONTINUE", "SPACE", "RETURN", "SECTION_COMMENT", 
      "LINE_COMMENT", "Res_ID_", "Label", "Exp_par_fl", "Peak_pick_fl", 
      "Cross_ref", "Simple_name_ET", "SPACE_ET", "RETURN_ET", "Note", "Note_end", 
      "SPACE_MN"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,34,146,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,9,0,1,0,
  	1,0,1,1,1,1,1,1,3,1,34,8,1,1,1,1,1,1,1,3,1,39,8,1,1,1,3,1,42,8,1,1,1,
  	4,1,45,8,1,11,1,12,1,46,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,57,8,2,11,
  	2,12,2,58,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,
  	75,8,4,10,4,12,4,78,9,4,1,4,3,4,81,8,4,1,4,1,4,5,4,85,8,4,10,4,12,4,88,
  	9,4,1,4,3,4,91,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,99,8,4,1,4,5,4,102,8,4,
  	10,4,12,4,105,9,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,3,7,117,8,7,
  	1,7,1,7,5,7,121,8,7,10,7,12,7,124,9,7,1,7,3,7,127,8,7,1,7,3,7,130,8,7,
  	1,7,1,7,5,7,134,8,7,10,7,12,7,137,9,7,1,7,3,7,140,8,7,1,7,1,7,1,8,1,8,
  	1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,5,2,0,5,5,24,24,1,1,21,21,2,0,14,14,
  	18,18,2,0,12,12,18,18,1,0,14,15,156,0,19,1,0,0,0,2,33,1,0,0,0,4,48,1,
  	0,0,0,6,60,1,0,0,0,8,66,1,0,0,0,10,109,1,0,0,0,12,111,1,0,0,0,14,113,
  	1,0,0,0,16,143,1,0,0,0,18,20,5,21,0,0,19,18,1,0,0,0,19,20,1,0,0,0,20,
  	25,1,0,0,0,21,24,3,2,1,0,22,24,5,21,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,
  	27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,
  	29,5,0,0,1,29,1,1,0,0,0,30,31,5,1,0,0,31,32,5,2,0,0,32,34,5,21,0,0,33,
  	30,1,0,0,0,33,34,1,0,0,0,34,38,1,0,0,0,35,36,5,3,0,0,36,37,5,14,0,0,37,
  	39,5,21,0,0,38,35,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,42,3,4,2,0,41,
  	40,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,45,3,8,4,0,44,43,1,0,0,0,45,
  	46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,3,1,0,0,0,48,49,5,4,0,0,49,
  	50,5,31,0,0,50,51,5,25,0,0,51,52,5,26,0,0,52,53,5,27,0,0,53,54,5,28,0,
  	0,54,56,5,31,0,0,55,57,3,6,3,0,56,55,1,0,0,0,57,58,1,0,0,0,58,56,1,0,
  	0,0,58,59,1,0,0,0,59,5,1,0,0,0,60,61,5,29,0,0,61,62,5,29,0,0,62,63,5,
  	29,0,0,63,64,5,29,0,0,64,65,5,31,0,0,65,7,1,0,0,0,66,67,7,0,0,0,67,68,
  	3,10,5,0,68,69,5,21,0,0,69,70,5,6,0,0,70,71,3,12,6,0,71,80,5,21,0,0,72,
  	76,5,7,0,0,73,75,3,12,6,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,
  	77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,81,5,21,0,0,80,72,1,0,0,0,80,
  	81,1,0,0,0,81,90,1,0,0,0,82,86,5,8,0,0,83,85,3,12,6,0,84,83,1,0,0,0,85,
  	88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,89,
  	91,5,21,0,0,90,82,1,0,0,0,90,91,1,0,0,0,91,92,1,0,0,0,92,93,5,9,0,0,93,
  	94,5,14,0,0,94,98,5,21,0,0,95,96,5,10,0,0,96,97,5,14,0,0,97,99,5,21,0,
  	0,98,95,1,0,0,0,98,99,1,0,0,0,99,103,1,0,0,0,100,102,3,14,7,0,101,100,
  	1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,106,1,0,0,
  	0,105,103,1,0,0,0,106,107,5,11,0,0,107,108,7,1,0,0,108,9,1,0,0,0,109,
  	110,7,2,0,0,110,11,1,0,0,0,111,112,7,3,0,0,112,13,1,0,0,0,113,114,5,18,
  	0,0,114,116,3,16,8,0,115,117,3,16,8,0,116,115,1,0,0,0,116,117,1,0,0,0,
  	117,126,1,0,0,0,118,122,5,13,0,0,119,121,5,32,0,0,120,119,1,0,0,0,121,
  	124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,122,1,
  	0,0,0,125,127,5,33,0,0,126,118,1,0,0,0,126,127,1,0,0,0,127,129,1,0,0,
  	0,128,130,3,16,8,0,129,128,1,0,0,0,129,130,1,0,0,0,130,139,1,0,0,0,131,
  	135,5,13,0,0,132,134,5,32,0,0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,
  	1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,135,1,0,0,0,138,140,5,33,
  	0,0,139,131,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,142,5,21,0,0,
  	142,15,1,0,0,0,143,144,7,4,0,0,144,17,1,0,0,0,20,19,23,25,33,38,41,46,
  	58,76,80,86,90,98,103,116,122,126,129,135,139
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  pippcsparserParserStaticData = std::move(staticData);
}

}

PippCSParser::PippCSParser(TokenStream *input) : PippCSParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

PippCSParser::PippCSParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  PippCSParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *pippcsparserParserStaticData->atn, pippcsparserParserStaticData->decisionToDFA, pippcsparserParserStaticData->sharedContextCache, options);
}

PippCSParser::~PippCSParser() {
  delete _interpreter;
}

const atn::ATN& PippCSParser::getATN() const {
  return *pippcsparserParserStaticData->atn;
}

std::string PippCSParser::getGrammarFileName() const {
  return "PippCSParser.g4";
}

const std::vector<std::string>& PippCSParser::getRuleNames() const {
  return pippcsparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& PippCSParser::getVocabulary() const {
  return pippcsparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView PippCSParser::getSerializedATN() const {
  return pippcsparserParserStaticData->serializedATN;
}


//----------------- Pipp_csContext ------------------------------------------------------------------

PippCSParser::Pipp_csContext::Pipp_csContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PippCSParser::Pipp_csContext::EOF() {
  return getToken(PippCSParser::EOF, 0);
}

std::vector<tree::TerminalNode *> PippCSParser::Pipp_csContext::RETURN() {
  return getTokens(PippCSParser::RETURN);
}

tree::TerminalNode* PippCSParser::Pipp_csContext::RETURN(size_t i) {
  return getToken(PippCSParser::RETURN, i);
}

std::vector<PippCSParser::Pipp_formatContext *> PippCSParser::Pipp_csContext::pipp_format() {
  return getRuleContexts<PippCSParser::Pipp_formatContext>();
}

PippCSParser::Pipp_formatContext* PippCSParser::Pipp_csContext::pipp_format(size_t i) {
  return getRuleContext<PippCSParser::Pipp_formatContext>(i);
}


size_t PippCSParser::Pipp_csContext::getRuleIndex() const {
  return PippCSParser::RulePipp_cs;
}


std::any PippCSParser::Pipp_csContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PippCSParserVisitor*>(visitor))
    return parserVisitor->visitPipp_cs(this);
  else
    return visitor->visitChildren(this);
}

PippCSParser::Pipp_csContext* PippCSParser::pipp_cs() {
  Pipp_csContext *_localctx = _tracker.createInstance<Pipp_csContext>(_ctx, getState());
  enterRule(_localctx, 0, PippCSParser::RulePipp_cs);
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
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(18);
      match(PippCSParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(25);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 18874426) != 0)) {
      setState(23);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case PippCSParser::Shift_fl_frmt:
        case PippCSParser::First_res_in_seq:
        case PippCSParser::Exp_peak_pick_tbl:
        case PippCSParser::Res_ID:
        case PippCSParser::Res_ID_: {
          setState(21);
          pipp_format();
          break;
        }

        case PippCSParser::RETURN: {
          setState(22);
          match(PippCSParser::RETURN);
          break;
        }

      default:
        throw NoViableAltException(this);
      }
      setState(27);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(28);
    match(PippCSParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pipp_formatContext ------------------------------------------------------------------

PippCSParser::Pipp_formatContext::Pipp_formatContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PippCSParser::Pipp_formatContext::Shift_fl_frmt() {
  return getToken(PippCSParser::Shift_fl_frmt, 0);
}

tree::TerminalNode* PippCSParser::Pipp_formatContext::Res_siad() {
  return getToken(PippCSParser::Res_siad, 0);
}

std::vector<tree::TerminalNode *> PippCSParser::Pipp_formatContext::RETURN() {
  return getTokens(PippCSParser::RETURN);
}

tree::TerminalNode* PippCSParser::Pipp_formatContext::RETURN(size_t i) {
  return getToken(PippCSParser::RETURN, i);
}

tree::TerminalNode* PippCSParser::Pipp_formatContext::First_res_in_seq() {
  return getToken(PippCSParser::First_res_in_seq, 0);
}

tree::TerminalNode* PippCSParser::Pipp_formatContext::Integer() {
  return getToken(PippCSParser::Integer, 0);
}

PippCSParser::Ext_peak_pick_tblContext* PippCSParser::Pipp_formatContext::ext_peak_pick_tbl() {
  return getRuleContext<PippCSParser::Ext_peak_pick_tblContext>(0);
}

std::vector<PippCSParser::Residue_listContext *> PippCSParser::Pipp_formatContext::residue_list() {
  return getRuleContexts<PippCSParser::Residue_listContext>();
}

PippCSParser::Residue_listContext* PippCSParser::Pipp_formatContext::residue_list(size_t i) {
  return getRuleContext<PippCSParser::Residue_listContext>(i);
}


size_t PippCSParser::Pipp_formatContext::getRuleIndex() const {
  return PippCSParser::RulePipp_format;
}


std::any PippCSParser::Pipp_formatContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PippCSParserVisitor*>(visitor))
    return parserVisitor->visitPipp_format(this);
  else
    return visitor->visitChildren(this);
}

PippCSParser::Pipp_formatContext* PippCSParser::pipp_format() {
  Pipp_formatContext *_localctx = _tracker.createInstance<Pipp_formatContext>(_ctx, getState());
  enterRule(_localctx, 2, PippCSParser::RulePipp_format);
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
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::Shift_fl_frmt) {
      setState(30);
      match(PippCSParser::Shift_fl_frmt);
      setState(31);
      match(PippCSParser::Res_siad);
      setState(32);
      match(PippCSParser::RETURN);
    }
    setState(38);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::First_res_in_seq) {
      setState(35);
      match(PippCSParser::First_res_in_seq);
      setState(36);
      match(PippCSParser::Integer);
      setState(37);
      match(PippCSParser::RETURN);
    }
    setState(41);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::Exp_peak_pick_tbl) {
      setState(40);
      ext_peak_pick_tbl();
    }
    setState(44); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(43);
              residue_list();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(46); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 6, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ext_peak_pick_tblContext ------------------------------------------------------------------

PippCSParser::Ext_peak_pick_tblContext::Ext_peak_pick_tblContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PippCSParser::Ext_peak_pick_tblContext::Exp_peak_pick_tbl() {
  return getToken(PippCSParser::Exp_peak_pick_tbl, 0);
}

std::vector<tree::TerminalNode *> PippCSParser::Ext_peak_pick_tblContext::RETURN_ET() {
  return getTokens(PippCSParser::RETURN_ET);
}

tree::TerminalNode* PippCSParser::Ext_peak_pick_tblContext::RETURN_ET(size_t i) {
  return getToken(PippCSParser::RETURN_ET, i);
}

tree::TerminalNode* PippCSParser::Ext_peak_pick_tblContext::Label() {
  return getToken(PippCSParser::Label, 0);
}

tree::TerminalNode* PippCSParser::Ext_peak_pick_tblContext::Exp_par_fl() {
  return getToken(PippCSParser::Exp_par_fl, 0);
}

tree::TerminalNode* PippCSParser::Ext_peak_pick_tblContext::Peak_pick_fl() {
  return getToken(PippCSParser::Peak_pick_fl, 0);
}

tree::TerminalNode* PippCSParser::Ext_peak_pick_tblContext::Cross_ref() {
  return getToken(PippCSParser::Cross_ref, 0);
}

std::vector<PippCSParser::Ext_peak_pick_tbl_rowContext *> PippCSParser::Ext_peak_pick_tblContext::ext_peak_pick_tbl_row() {
  return getRuleContexts<PippCSParser::Ext_peak_pick_tbl_rowContext>();
}

PippCSParser::Ext_peak_pick_tbl_rowContext* PippCSParser::Ext_peak_pick_tblContext::ext_peak_pick_tbl_row(size_t i) {
  return getRuleContext<PippCSParser::Ext_peak_pick_tbl_rowContext>(i);
}


size_t PippCSParser::Ext_peak_pick_tblContext::getRuleIndex() const {
  return PippCSParser::RuleExt_peak_pick_tbl;
}


std::any PippCSParser::Ext_peak_pick_tblContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PippCSParserVisitor*>(visitor))
    return parserVisitor->visitExt_peak_pick_tbl(this);
  else
    return visitor->visitChildren(this);
}

PippCSParser::Ext_peak_pick_tblContext* PippCSParser::ext_peak_pick_tbl() {
  Ext_peak_pick_tblContext *_localctx = _tracker.createInstance<Ext_peak_pick_tblContext>(_ctx, getState());
  enterRule(_localctx, 4, PippCSParser::RuleExt_peak_pick_tbl);
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
    setState(48);
    match(PippCSParser::Exp_peak_pick_tbl);
    setState(49);
    match(PippCSParser::RETURN_ET);
    setState(50);
    match(PippCSParser::Label);
    setState(51);
    match(PippCSParser::Exp_par_fl);
    setState(52);
    match(PippCSParser::Peak_pick_fl);
    setState(53);
    match(PippCSParser::Cross_ref);
    setState(54);
    match(PippCSParser::RETURN_ET);
    setState(56); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(55);
      ext_peak_pick_tbl_row();
      setState(58); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == PippCSParser::Simple_name_ET);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ext_peak_pick_tbl_rowContext ------------------------------------------------------------------

PippCSParser::Ext_peak_pick_tbl_rowContext::Ext_peak_pick_tbl_rowContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> PippCSParser::Ext_peak_pick_tbl_rowContext::Simple_name_ET() {
  return getTokens(PippCSParser::Simple_name_ET);
}

tree::TerminalNode* PippCSParser::Ext_peak_pick_tbl_rowContext::Simple_name_ET(size_t i) {
  return getToken(PippCSParser::Simple_name_ET, i);
}

tree::TerminalNode* PippCSParser::Ext_peak_pick_tbl_rowContext::RETURN_ET() {
  return getToken(PippCSParser::RETURN_ET, 0);
}


size_t PippCSParser::Ext_peak_pick_tbl_rowContext::getRuleIndex() const {
  return PippCSParser::RuleExt_peak_pick_tbl_row;
}


std::any PippCSParser::Ext_peak_pick_tbl_rowContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PippCSParserVisitor*>(visitor))
    return parserVisitor->visitExt_peak_pick_tbl_row(this);
  else
    return visitor->visitChildren(this);
}

PippCSParser::Ext_peak_pick_tbl_rowContext* PippCSParser::ext_peak_pick_tbl_row() {
  Ext_peak_pick_tbl_rowContext *_localctx = _tracker.createInstance<Ext_peak_pick_tbl_rowContext>(_ctx, getState());
  enterRule(_localctx, 6, PippCSParser::RuleExt_peak_pick_tbl_row);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(60);
    match(PippCSParser::Simple_name_ET);
    setState(61);
    match(PippCSParser::Simple_name_ET);
    setState(62);
    match(PippCSParser::Simple_name_ET);
    setState(63);
    match(PippCSParser::Simple_name_ET);
    setState(64);
    match(PippCSParser::RETURN_ET);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Residue_listContext ------------------------------------------------------------------

PippCSParser::Residue_listContext::Residue_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PippCSParser::Res_idContext* PippCSParser::Residue_listContext::res_id() {
  return getRuleContext<PippCSParser::Res_idContext>(0);
}

std::vector<tree::TerminalNode *> PippCSParser::Residue_listContext::RETURN() {
  return getTokens(PippCSParser::RETURN);
}

tree::TerminalNode* PippCSParser::Residue_listContext::RETURN(size_t i) {
  return getToken(PippCSParser::RETURN, i);
}

tree::TerminalNode* PippCSParser::Residue_listContext::Res_type() {
  return getToken(PippCSParser::Res_type, 0);
}

std::vector<PippCSParser::Res_typeContext *> PippCSParser::Residue_listContext::res_type() {
  return getRuleContexts<PippCSParser::Res_typeContext>();
}

PippCSParser::Res_typeContext* PippCSParser::Residue_listContext::res_type(size_t i) {
  return getRuleContext<PippCSParser::Res_typeContext>(i);
}

tree::TerminalNode* PippCSParser::Residue_listContext::Spin_system_ID() {
  return getToken(PippCSParser::Spin_system_ID, 0);
}

std::vector<tree::TerminalNode *> PippCSParser::Residue_listContext::Integer() {
  return getTokens(PippCSParser::Integer);
}

tree::TerminalNode* PippCSParser::Residue_listContext::Integer(size_t i) {
  return getToken(PippCSParser::Integer, i);
}

tree::TerminalNode* PippCSParser::Residue_listContext::End_res_def() {
  return getToken(PippCSParser::End_res_def, 0);
}

tree::TerminalNode* PippCSParser::Residue_listContext::Res_ID() {
  return getToken(PippCSParser::Res_ID, 0);
}

tree::TerminalNode* PippCSParser::Residue_listContext::Res_ID_() {
  return getToken(PippCSParser::Res_ID_, 0);
}

tree::TerminalNode* PippCSParser::Residue_listContext::EOF() {
  return getToken(PippCSParser::EOF, 0);
}

tree::TerminalNode* PippCSParser::Residue_listContext::Prev_type() {
  return getToken(PippCSParser::Prev_type, 0);
}

tree::TerminalNode* PippCSParser::Residue_listContext::Cur_type() {
  return getToken(PippCSParser::Cur_type, 0);
}

tree::TerminalNode* PippCSParser::Residue_listContext::Heterogeneity() {
  return getToken(PippCSParser::Heterogeneity, 0);
}

std::vector<PippCSParser::Shift_listContext *> PippCSParser::Residue_listContext::shift_list() {
  return getRuleContexts<PippCSParser::Shift_listContext>();
}

PippCSParser::Shift_listContext* PippCSParser::Residue_listContext::shift_list(size_t i) {
  return getRuleContext<PippCSParser::Shift_listContext>(i);
}


size_t PippCSParser::Residue_listContext::getRuleIndex() const {
  return PippCSParser::RuleResidue_list;
}


std::any PippCSParser::Residue_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PippCSParserVisitor*>(visitor))
    return parserVisitor->visitResidue_list(this);
  else
    return visitor->visitChildren(this);
}

PippCSParser::Residue_listContext* PippCSParser::residue_list() {
  Residue_listContext *_localctx = _tracker.createInstance<Residue_listContext>(_ctx, getState());
  enterRule(_localctx, 8, PippCSParser::RuleResidue_list);
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
    setState(66);
    _la = _input->LA(1);
    if (!(_la == PippCSParser::Res_ID

    || _la == PippCSParser::Res_ID_)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(67);
    res_id();
    setState(68);
    match(PippCSParser::RETURN);
    setState(69);
    match(PippCSParser::Res_type);
    setState(70);
    res_type();
    setState(71);
    match(PippCSParser::RETURN);
    setState(80);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::Prev_type) {
      setState(72);
      match(PippCSParser::Prev_type);
      setState(76);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == PippCSParser::Type_pred

      || _la == PippCSParser::Simple_name) {
        setState(73);
        res_type();
        setState(78);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(79);
      match(PippCSParser::RETURN);
    }
    setState(90);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::Cur_type) {
      setState(82);
      match(PippCSParser::Cur_type);
      setState(86);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == PippCSParser::Type_pred

      || _la == PippCSParser::Simple_name) {
        setState(83);
        res_type();
        setState(88);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(89);
      match(PippCSParser::RETURN);
    }
    setState(92);
    match(PippCSParser::Spin_system_ID);
    setState(93);
    match(PippCSParser::Integer);
    setState(94);
    match(PippCSParser::RETURN);
    setState(98);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::Heterogeneity) {
      setState(95);
      match(PippCSParser::Heterogeneity);
      setState(96);
      match(PippCSParser::Integer);
      setState(97);
      match(PippCSParser::RETURN);
    }
    setState(103);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == PippCSParser::Simple_name) {
      setState(100);
      shift_list();
      setState(105);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(106);
    match(PippCSParser::End_res_def);
    setState(107);
    _la = _input->LA(1);
    if (!(_la == PippCSParser::EOF

    || _la == PippCSParser::RETURN)) {
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

//----------------- Res_idContext ------------------------------------------------------------------

PippCSParser::Res_idContext::Res_idContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PippCSParser::Res_idContext::Integer() {
  return getToken(PippCSParser::Integer, 0);
}

tree::TerminalNode* PippCSParser::Res_idContext::Simple_name() {
  return getToken(PippCSParser::Simple_name, 0);
}


size_t PippCSParser::Res_idContext::getRuleIndex() const {
  return PippCSParser::RuleRes_id;
}


std::any PippCSParser::Res_idContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PippCSParserVisitor*>(visitor))
    return parserVisitor->visitRes_id(this);
  else
    return visitor->visitChildren(this);
}

PippCSParser::Res_idContext* PippCSParser::res_id() {
  Res_idContext *_localctx = _tracker.createInstance<Res_idContext>(_ctx, getState());
  enterRule(_localctx, 10, PippCSParser::RuleRes_id);
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
    _la = _input->LA(1);
    if (!(_la == PippCSParser::Integer

    || _la == PippCSParser::Simple_name)) {
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

//----------------- Res_typeContext ------------------------------------------------------------------

PippCSParser::Res_typeContext::Res_typeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PippCSParser::Res_typeContext::Simple_name() {
  return getToken(PippCSParser::Simple_name, 0);
}

tree::TerminalNode* PippCSParser::Res_typeContext::Type_pred() {
  return getToken(PippCSParser::Type_pred, 0);
}


size_t PippCSParser::Res_typeContext::getRuleIndex() const {
  return PippCSParser::RuleRes_type;
}


std::any PippCSParser::Res_typeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PippCSParserVisitor*>(visitor))
    return parserVisitor->visitRes_type(this);
  else
    return visitor->visitChildren(this);
}

PippCSParser::Res_typeContext* PippCSParser::res_type() {
  Res_typeContext *_localctx = _tracker.createInstance<Res_typeContext>(_ctx, getState());
  enterRule(_localctx, 12, PippCSParser::RuleRes_type);
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
    setState(111);
    _la = _input->LA(1);
    if (!(_la == PippCSParser::Type_pred

    || _la == PippCSParser::Simple_name)) {
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

//----------------- Shift_listContext ------------------------------------------------------------------

PippCSParser::Shift_listContext::Shift_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PippCSParser::Shift_listContext::Simple_name() {
  return getToken(PippCSParser::Simple_name, 0);
}

std::vector<PippCSParser::NumberContext *> PippCSParser::Shift_listContext::number() {
  return getRuleContexts<PippCSParser::NumberContext>();
}

PippCSParser::NumberContext* PippCSParser::Shift_listContext::number(size_t i) {
  return getRuleContext<PippCSParser::NumberContext>(i);
}

tree::TerminalNode* PippCSParser::Shift_listContext::RETURN() {
  return getToken(PippCSParser::RETURN, 0);
}

std::vector<tree::TerminalNode *> PippCSParser::Shift_listContext::Note_begin() {
  return getTokens(PippCSParser::Note_begin);
}

tree::TerminalNode* PippCSParser::Shift_listContext::Note_begin(size_t i) {
  return getToken(PippCSParser::Note_begin, i);
}

std::vector<tree::TerminalNode *> PippCSParser::Shift_listContext::Note_end() {
  return getTokens(PippCSParser::Note_end);
}

tree::TerminalNode* PippCSParser::Shift_listContext::Note_end(size_t i) {
  return getToken(PippCSParser::Note_end, i);
}

std::vector<tree::TerminalNode *> PippCSParser::Shift_listContext::Note() {
  return getTokens(PippCSParser::Note);
}

tree::TerminalNode* PippCSParser::Shift_listContext::Note(size_t i) {
  return getToken(PippCSParser::Note, i);
}


size_t PippCSParser::Shift_listContext::getRuleIndex() const {
  return PippCSParser::RuleShift_list;
}


std::any PippCSParser::Shift_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PippCSParserVisitor*>(visitor))
    return parserVisitor->visitShift_list(this);
  else
    return visitor->visitChildren(this);
}

PippCSParser::Shift_listContext* PippCSParser::shift_list() {
  Shift_listContext *_localctx = _tracker.createInstance<Shift_listContext>(_ctx, getState());
  enterRule(_localctx, 14, PippCSParser::RuleShift_list);
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
    setState(113);
    match(PippCSParser::Simple_name);
    setState(114);
    number();
    setState(116);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx)) {
    case 1: {
      setState(115);
      number();
      break;
    }

    default:
      break;
    }
    setState(126);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 16, _ctx)) {
    case 1: {
      setState(118);
      match(PippCSParser::Note_begin);
      setState(122);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == PippCSParser::Note) {
        setState(119);
        match(PippCSParser::Note);
        setState(124);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(125);
      match(PippCSParser::Note_end);
      break;
    }

    default:
      break;
    }
    setState(129);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::Integer

    || _la == PippCSParser::Float) {
      setState(128);
      number();
    }
    setState(139);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::Note_begin) {
      setState(131);
      match(PippCSParser::Note_begin);
      setState(135);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == PippCSParser::Note) {
        setState(132);
        match(PippCSParser::Note);
        setState(137);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(138);
      match(PippCSParser::Note_end);
    }
    setState(141);
    match(PippCSParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberContext ------------------------------------------------------------------

PippCSParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PippCSParser::NumberContext::Float() {
  return getToken(PippCSParser::Float, 0);
}

tree::TerminalNode* PippCSParser::NumberContext::Integer() {
  return getToken(PippCSParser::Integer, 0);
}


size_t PippCSParser::NumberContext::getRuleIndex() const {
  return PippCSParser::RuleNumber;
}


std::any PippCSParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PippCSParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

PippCSParser::NumberContext* PippCSParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 16, PippCSParser::RuleNumber);
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
    setState(143);
    _la = _input->LA(1);
    if (!(_la == PippCSParser::Integer

    || _la == PippCSParser::Float)) {
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

void PippCSParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  pippcsparserParserInitialize();
#else
  ::antlr4::internal::call_once(pippcsparserParserOnceFlag, pippcsparserParserInitialize);
#endif
}
