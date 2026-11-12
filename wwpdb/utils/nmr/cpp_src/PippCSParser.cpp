
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
      "residue_list", "shift_list", "number"
    },
    std::vector<std::string>{
      "", "'SHIFT_FL_FRMT'", "'RES_SIAD'", "'FIRST_RES_IN_SEQ'", "'EXP_PEAK_PICK_TBL'", 
      "", "'RES_TYPE'", "'PREV_TYPE'", "'SPIN_SYSTEM_ID'", "'HETEROGENEITY'", 
      "'END_RES_DEF'", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "'Label'", "'Exp Par Fl'", "'Peak-Pick Fl'", "'#-Cross-Ref'"
    },
    std::vector<std::string>{
      "", "Shift_fl_frmt", "Res_siad", "First_res_in_seq", "Exp_peak_pick_tbl", 
      "Res_ID", "Res_type", "Prev_type", "Spin_system_ID", "Heterogeneity", 
      "End_res_def", "Type_pred", "Single_note", "Note_begin", "Integer", 
      "Float", "SHARP_COMMENT", "EXCLM_COMMENT", "Simple_name", "SPACE", 
      "RETURN", "SECTION_COMMENT", "LINE_COMMENT", "Res_ID_", "Label", "Exp_par_fl", 
      "Peak_pick_fl", "Cross_ref", "Simple_name_ET", "SPACE_ET", "RETURN_ET", 
      "Note_middle", "Note_end", "SPACE_MN"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,33,112,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,1,
  	0,3,0,16,8,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,1,1,1,
  	3,1,30,8,1,1,1,1,1,1,1,3,1,35,8,1,1,1,3,1,38,8,1,1,1,4,1,41,8,1,11,1,
  	12,1,42,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,53,8,2,11,2,12,2,54,1,3,1,
  	3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,71,8,4,11,4,12,
  	4,72,1,4,3,4,76,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,85,8,4,11,4,12,4,
  	86,1,4,1,4,1,4,1,5,1,5,1,5,3,5,95,8,5,1,5,1,5,1,5,5,5,100,8,5,10,5,12,
  	5,103,9,5,1,5,3,5,106,8,5,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,
  	3,2,0,5,5,23,23,1,1,20,20,1,0,14,15,119,0,15,1,0,0,0,2,29,1,0,0,0,4,44,
  	1,0,0,0,6,56,1,0,0,0,8,62,1,0,0,0,10,91,1,0,0,0,12,109,1,0,0,0,14,16,
  	5,20,0,0,15,14,1,0,0,0,15,16,1,0,0,0,16,21,1,0,0,0,17,20,3,2,1,0,18,20,
  	5,20,0,0,19,17,1,0,0,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,
  	1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,27,
  	5,1,0,0,27,28,5,2,0,0,28,30,5,20,0,0,29,26,1,0,0,0,29,30,1,0,0,0,30,34,
  	1,0,0,0,31,32,5,3,0,0,32,33,5,14,0,0,33,35,5,20,0,0,34,31,1,0,0,0,34,
  	35,1,0,0,0,35,37,1,0,0,0,36,38,3,4,2,0,37,36,1,0,0,0,37,38,1,0,0,0,38,
  	40,1,0,0,0,39,41,3,8,4,0,40,39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,
  	43,1,0,0,0,43,3,1,0,0,0,44,45,5,4,0,0,45,46,5,30,0,0,46,47,5,24,0,0,47,
  	48,5,25,0,0,48,49,5,26,0,0,49,50,5,27,0,0,50,52,5,30,0,0,51,53,3,6,3,
  	0,52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,5,1,0,0,
  	0,56,57,5,28,0,0,57,58,5,28,0,0,58,59,5,28,0,0,59,60,5,28,0,0,60,61,5,
  	30,0,0,61,7,1,0,0,0,62,63,7,0,0,0,63,64,5,14,0,0,64,65,5,20,0,0,65,66,
  	5,6,0,0,66,67,5,18,0,0,67,75,5,20,0,0,68,70,5,7,0,0,69,71,5,11,0,0,70,
  	69,1,0,0,0,71,72,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,
  	76,5,20,0,0,75,68,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,5,8,0,0,78,
  	79,5,14,0,0,79,80,5,20,0,0,80,81,5,9,0,0,81,82,5,14,0,0,82,84,5,20,0,
  	0,83,85,3,10,5,0,84,83,1,0,0,0,85,86,1,0,0,0,86,84,1,0,0,0,86,87,1,0,
  	0,0,87,88,1,0,0,0,88,89,5,10,0,0,89,90,7,1,0,0,90,9,1,0,0,0,91,92,5,18,
  	0,0,92,94,3,12,6,0,93,95,3,12,6,0,94,93,1,0,0,0,94,95,1,0,0,0,95,105,
  	1,0,0,0,96,106,5,12,0,0,97,101,5,13,0,0,98,100,5,31,0,0,99,98,1,0,0,0,
  	100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,101,
  	1,0,0,0,104,106,5,32,0,0,105,96,1,0,0,0,105,97,1,0,0,0,105,106,1,0,0,
  	0,106,107,1,0,0,0,107,108,5,20,0,0,108,11,1,0,0,0,109,110,7,2,0,0,110,
  	13,1,0,0,0,14,15,19,21,29,34,37,42,54,72,75,86,94,101,105
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
    setState(15);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(14);
      match(PippCSParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(21);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 9437242) != 0)) {
      setState(19);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case PippCSParser::Shift_fl_frmt:
        case PippCSParser::First_res_in_seq:
        case PippCSParser::Exp_peak_pick_tbl:
        case PippCSParser::Res_ID:
        case PippCSParser::Res_ID_: {
          setState(17);
          pipp_format();
          break;
        }

        case PippCSParser::RETURN: {
          setState(18);
          match(PippCSParser::RETURN);
          break;
        }

      default:
        throw NoViableAltException(this);
      }
      setState(23);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(24);
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
    setState(29);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::Shift_fl_frmt) {
      setState(26);
      match(PippCSParser::Shift_fl_frmt);
      setState(27);
      match(PippCSParser::Res_siad);
      setState(28);
      match(PippCSParser::RETURN);
    }
    setState(34);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::First_res_in_seq) {
      setState(31);
      match(PippCSParser::First_res_in_seq);
      setState(32);
      match(PippCSParser::Integer);
      setState(33);
      match(PippCSParser::RETURN);
    }
    setState(37);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::Exp_peak_pick_tbl) {
      setState(36);
      ext_peak_pick_tbl();
    }
    setState(40); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(39);
              residue_list();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(42); 
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
    setState(44);
    match(PippCSParser::Exp_peak_pick_tbl);
    setState(45);
    match(PippCSParser::RETURN_ET);
    setState(46);
    match(PippCSParser::Label);
    setState(47);
    match(PippCSParser::Exp_par_fl);
    setState(48);
    match(PippCSParser::Peak_pick_fl);
    setState(49);
    match(PippCSParser::Cross_ref);
    setState(50);
    match(PippCSParser::RETURN_ET);
    setState(52); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(51);
      ext_peak_pick_tbl_row();
      setState(54); 
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
    setState(56);
    match(PippCSParser::Simple_name_ET);
    setState(57);
    match(PippCSParser::Simple_name_ET);
    setState(58);
    match(PippCSParser::Simple_name_ET);
    setState(59);
    match(PippCSParser::Simple_name_ET);
    setState(60);
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

std::vector<tree::TerminalNode *> PippCSParser::Residue_listContext::Integer() {
  return getTokens(PippCSParser::Integer);
}

tree::TerminalNode* PippCSParser::Residue_listContext::Integer(size_t i) {
  return getToken(PippCSParser::Integer, i);
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

tree::TerminalNode* PippCSParser::Residue_listContext::Simple_name() {
  return getToken(PippCSParser::Simple_name, 0);
}

tree::TerminalNode* PippCSParser::Residue_listContext::Spin_system_ID() {
  return getToken(PippCSParser::Spin_system_ID, 0);
}

tree::TerminalNode* PippCSParser::Residue_listContext::Heterogeneity() {
  return getToken(PippCSParser::Heterogeneity, 0);
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

std::vector<PippCSParser::Shift_listContext *> PippCSParser::Residue_listContext::shift_list() {
  return getRuleContexts<PippCSParser::Shift_listContext>();
}

PippCSParser::Shift_listContext* PippCSParser::Residue_listContext::shift_list(size_t i) {
  return getRuleContext<PippCSParser::Shift_listContext>(i);
}

std::vector<tree::TerminalNode *> PippCSParser::Residue_listContext::Type_pred() {
  return getTokens(PippCSParser::Type_pred);
}

tree::TerminalNode* PippCSParser::Residue_listContext::Type_pred(size_t i) {
  return getToken(PippCSParser::Type_pred, i);
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
    setState(62);
    _la = _input->LA(1);
    if (!(_la == PippCSParser::Res_ID

    || _la == PippCSParser::Res_ID_)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(63);
    match(PippCSParser::Integer);
    setState(64);
    match(PippCSParser::RETURN);
    setState(65);
    match(PippCSParser::Res_type);
    setState(66);
    match(PippCSParser::Simple_name);
    setState(67);
    match(PippCSParser::RETURN);
    setState(75);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::Prev_type) {
      setState(68);
      match(PippCSParser::Prev_type);
      setState(70); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(69);
        match(PippCSParser::Type_pred);
        setState(72); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == PippCSParser::Type_pred);
      setState(74);
      match(PippCSParser::RETURN);
    }
    setState(77);
    match(PippCSParser::Spin_system_ID);
    setState(78);
    match(PippCSParser::Integer);
    setState(79);
    match(PippCSParser::RETURN);
    setState(80);
    match(PippCSParser::Heterogeneity);
    setState(81);
    match(PippCSParser::Integer);
    setState(82);
    match(PippCSParser::RETURN);
    setState(84); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(83);
      shift_list();
      setState(86); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == PippCSParser::Simple_name);
    setState(88);
    match(PippCSParser::End_res_def);
    setState(89);
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

tree::TerminalNode* PippCSParser::Shift_listContext::Single_note() {
  return getToken(PippCSParser::Single_note, 0);
}

tree::TerminalNode* PippCSParser::Shift_listContext::Note_begin() {
  return getToken(PippCSParser::Note_begin, 0);
}

tree::TerminalNode* PippCSParser::Shift_listContext::Note_end() {
  return getToken(PippCSParser::Note_end, 0);
}

std::vector<tree::TerminalNode *> PippCSParser::Shift_listContext::Note_middle() {
  return getTokens(PippCSParser::Note_middle);
}

tree::TerminalNode* PippCSParser::Shift_listContext::Note_middle(size_t i) {
  return getToken(PippCSParser::Note_middle, i);
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
  enterRule(_localctx, 10, PippCSParser::RuleShift_list);
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
    match(PippCSParser::Simple_name);
    setState(92);
    number();
    setState(94);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PippCSParser::Integer

    || _la == PippCSParser::Float) {
      setState(93);
      number();
    }
    setState(105);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PippCSParser::Single_note: {
        setState(96);
        match(PippCSParser::Single_note);
        break;
      }

      case PippCSParser::Note_begin: {
        setState(97);
        match(PippCSParser::Note_begin);
        setState(101);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == PippCSParser::Note_middle) {
          setState(98);
          match(PippCSParser::Note_middle);
          setState(103);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        setState(104);
        match(PippCSParser::Note_end);
        break;
      }

      case PippCSParser::RETURN: {
        break;
      }

    default:
      break;
    }
    setState(107);
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
  enterRule(_localctx, 12, PippCSParser::RuleNumber);
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
