
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaNOAParser.g4 by ANTLR 4.13.0


#include "CyanaNOAParserVisitor.h"

#include "CyanaNOAParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct CyanaNOAParserStaticData final {
  CyanaNOAParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  CyanaNOAParserStaticData(const CyanaNOAParserStaticData&) = delete;
  CyanaNOAParserStaticData(CyanaNOAParserStaticData&&) = delete;
  CyanaNOAParserStaticData& operator=(const CyanaNOAParserStaticData&) = delete;
  CyanaNOAParserStaticData& operator=(CyanaNOAParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag cyananoaparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
CyanaNOAParserStaticData *cyananoaparserParserStaticData = nullptr;

void cyananoaparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (cyananoaparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(cyananoaparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<CyanaNOAParserStaticData>(
    std::vector<std::string>{
      "cyana_noa", "comment", "noe_peaks", "peak_header", "peak_quality", 
      "noe_assignments", "noe_assignment", "numerical_report", "extended_report", 
      "noe_stat", "list_of_proton", "peak_stat"
    },
    std::vector<std::string>{
      "", "'|i-j|'", "'from'", "'ppm;'", "'increased from'", "'|i-j|'", 
      "'diagonal'", "'out of'", "", "'quality'", "'OK'", "'lone'", "'poor'", 
      "'far'", "", "'Violated in'", "'structures by'", "'Average quality of peak assignments'", 
      "'Average number of used assignments'", "'Peaks with increased upper limit'", 
      "'Peaks with decreased upper limit'", "'Protons used in less than 30% of expected peaks'", 
      "'Peak observation distance'", "'Atom'", "'Residue'", "'Peaks'", "'Shift'", 
      "'Used'", "'Expect'", "'selected'", "'assigned'", "'unassigned'", 
      "'without assignment possibility'", "'with violation below'", "'with violation between'", 
      "'with violation above'", "'with diagonal assignment'", "'and'", "'Cross peaks'", 
      "'with off-diagonal assignment'", "'with unique assignment'", "'with short-range assignment'", 
      "'with medium-range assignment'", "'with long-range assignment'", 
      "", "'1<|i-j|<5'", "", "'('", "')'", "':'", "'.'", "','", "'='", "'+'", 
      "'-'", "'/'"
    },
    std::vector<std::string>{
      "", "Peak", "From", "Ppm_SC", "Increased_from", "Decreased_from", 
      "Diagonal", "Out_of", "Assignments_used", "Quality", "Ok", "Lone", 
      "Poor", "Far", "Distance_range", "Violated_in", "Structures_by", "Average_quality", 
      "Average_number", "Peaks_inc_upl", "Peaks_dec_upl", "Protons_used_in_less", 
      "Peak_obs_dist", "Atom", "Residue", "Peaks", "Shift", "Used", "Expect", 
      "Selected", "Assigned", "Unassigned", "Without_possibility", "With_viol_below", 
      "With_viol_between", "With_viol_above", "With_diagonal", "And", "Cross_peaks", 
      "With_off_diagonal", "With_unique", "With_short_range", "With_medium_range", 
      "With_long_range", "Short_range_ex", "Medium_range_ex", "Long_range_ex", 
      "L_paren", "R_paren", "Colon", "Period", "Comma", "Equ_op", "Add_op", 
      "Sub_op", "Div_op", "Angstrome", "Integer", "Float", "Numerical_report1", 
      "Numerical_report2", "Numerical_report3", "Numerical_report4", "COMMENT", 
      "Simple_name", "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT", 
      "File_name", "SPACE_FN", "Any_name", "SPACE_CM", "RETURN_CM"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,73,212,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,5,0,29,8,0,
  	10,0,12,0,32,9,0,1,0,1,0,1,1,1,1,5,1,38,8,1,10,1,12,1,41,9,1,1,1,1,1,
  	1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
  	3,1,3,1,3,3,3,64,8,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
  	1,4,1,5,4,5,80,8,5,11,5,12,5,81,1,5,1,5,1,5,1,5,1,5,3,5,89,8,5,1,6,1,
  	6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,106,8,7,1,7,
  	3,7,109,8,7,1,8,1,8,3,8,113,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
  	9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,139,8,9,
  	10,9,12,9,142,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,
  	11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,166,8,
  	11,1,11,1,11,1,11,1,11,3,11,172,8,11,1,11,1,11,1,11,1,11,1,11,1,11,3,
  	11,180,8,11,1,11,1,11,1,11,1,11,3,11,186,8,11,1,11,1,11,1,11,1,11,1,11,
  	1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
  	1,11,1,11,1,11,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,
  	6,1,1,73,73,1,0,4,5,1,0,53,54,1,0,10,13,2,0,54,54,57,57,1,0,59,62,217,
  	0,30,1,0,0,0,2,35,1,0,0,0,4,44,1,0,0,0,6,49,1,0,0,0,8,68,1,0,0,0,10,79,
  	1,0,0,0,12,90,1,0,0,0,14,101,1,0,0,0,16,110,1,0,0,0,18,114,1,0,0,0,20,
  	143,1,0,0,0,22,151,1,0,0,0,24,29,3,2,1,0,25,29,3,4,2,0,26,29,3,18,9,0,
  	27,29,3,22,11,0,28,24,1,0,0,0,28,25,1,0,0,0,28,26,1,0,0,0,28,27,1,0,0,
  	0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,
  	0,33,34,5,0,0,1,34,1,1,0,0,0,35,39,5,63,0,0,36,38,5,71,0,0,37,36,1,0,
  	0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,1,0,
  	0,0,42,43,7,0,0,0,43,3,1,0,0,0,44,45,3,6,3,0,45,47,3,8,4,0,46,48,3,10,
  	5,0,47,46,1,0,0,0,47,48,1,0,0,0,48,5,1,0,0,0,49,50,5,1,0,0,50,51,5,57,
  	0,0,51,52,5,2,0,0,52,53,5,69,0,0,53,54,5,47,0,0,54,55,5,58,0,0,55,56,
  	5,51,0,0,56,57,5,58,0,0,57,63,5,3,0,0,58,64,5,56,0,0,59,60,5,56,0,0,60,
  	61,7,1,0,0,61,64,5,56,0,0,62,64,5,6,0,0,63,58,1,0,0,0,63,59,1,0,0,0,63,
  	62,1,0,0,0,64,65,1,0,0,0,65,66,5,48,0,0,66,67,5,49,0,0,67,7,1,0,0,0,68,
  	69,5,57,0,0,69,70,5,7,0,0,70,71,5,57,0,0,71,72,5,8,0,0,72,73,5,51,0,0,
  	73,74,5,9,0,0,74,75,5,52,0,0,75,76,5,58,0,0,76,77,5,49,0,0,77,9,1,0,0,
  	0,78,80,3,12,6,0,79,78,1,0,0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,
  	0,0,82,88,1,0,0,0,83,84,5,15,0,0,84,85,5,57,0,0,85,86,5,16,0,0,86,87,
  	5,56,0,0,87,89,5,50,0,0,88,83,1,0,0,0,88,89,1,0,0,0,89,11,1,0,0,0,90,
  	91,5,64,0,0,91,92,5,64,0,0,92,93,5,57,0,0,93,94,7,2,0,0,94,95,5,64,0,
  	0,95,96,5,64,0,0,96,97,5,57,0,0,97,98,7,3,0,0,98,99,5,57,0,0,99,100,3,
  	14,7,0,100,13,1,0,0,0,101,102,5,57,0,0,102,103,7,4,0,0,103,105,7,4,0,
  	0,104,106,5,14,0,0,105,104,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,
  	109,3,16,8,0,108,107,1,0,0,0,108,109,1,0,0,0,109,15,1,0,0,0,110,112,7,
  	5,0,0,111,113,3,16,8,0,112,111,1,0,0,0,112,113,1,0,0,0,113,17,1,0,0,0,
  	114,115,5,17,0,0,115,116,5,49,0,0,116,117,5,58,0,0,117,118,5,18,0,0,118,
  	119,5,49,0,0,119,120,5,58,0,0,120,121,5,19,0,0,121,122,5,49,0,0,122,123,
  	5,57,0,0,123,124,5,20,0,0,124,125,5,49,0,0,125,126,5,57,0,0,126,127,5,
  	21,0,0,127,128,5,49,0,0,128,129,5,22,0,0,129,130,5,49,0,0,130,131,5,56,
  	0,0,131,132,5,23,0,0,132,133,5,24,0,0,133,134,5,26,0,0,134,135,5,25,0,
  	0,135,136,5,27,0,0,136,140,5,28,0,0,137,139,3,20,10,0,138,137,1,0,0,0,
  	139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,19,1,0,0,0,142,140,
  	1,0,0,0,143,144,5,64,0,0,144,145,5,64,0,0,145,146,5,57,0,0,146,147,5,
  	58,0,0,147,148,5,57,0,0,148,149,5,57,0,0,149,150,5,57,0,0,150,21,1,0,
  	0,0,151,152,5,25,0,0,152,153,5,49,0,0,153,154,5,29,0,0,154,155,5,49,0,
  	0,155,156,5,57,0,0,156,157,5,30,0,0,157,158,5,49,0,0,158,159,5,57,0,0,
  	159,160,5,31,0,0,160,161,5,49,0,0,161,165,5,57,0,0,162,163,5,32,0,0,163,
  	164,5,49,0,0,164,166,5,57,0,0,165,162,1,0,0,0,165,166,1,0,0,0,166,171,
  	1,0,0,0,167,168,5,33,0,0,168,169,5,56,0,0,169,170,5,49,0,0,170,172,5,
  	57,0,0,171,167,1,0,0,0,171,172,1,0,0,0,172,179,1,0,0,0,173,174,5,34,0,
  	0,174,175,5,58,0,0,175,176,5,37,0,0,176,177,5,56,0,0,177,178,5,49,0,0,
  	178,180,5,57,0,0,179,173,1,0,0,0,179,180,1,0,0,0,180,185,1,0,0,0,181,
  	182,5,35,0,0,182,183,5,56,0,0,183,184,5,49,0,0,184,186,5,57,0,0,185,181,
  	1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,188,5,36,0,0,188,189,5,49,
  	0,0,189,190,5,57,0,0,190,191,5,38,0,0,191,192,5,49,0,0,192,193,5,39,0,
  	0,193,194,5,49,0,0,194,195,5,57,0,0,195,196,5,40,0,0,196,197,5,49,0,0,
  	197,198,5,57,0,0,198,199,5,41,0,0,199,200,5,44,0,0,200,201,5,49,0,0,201,
  	202,5,57,0,0,202,203,5,42,0,0,203,204,5,45,0,0,204,205,5,49,0,0,205,206,
  	5,57,0,0,206,207,5,43,0,0,207,208,5,46,0,0,208,209,5,49,0,0,209,210,5,
  	57,0,0,210,23,1,0,0,0,15,28,30,39,47,63,81,88,105,108,112,140,165,171,
  	179,185
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  cyananoaparserParserStaticData = staticData.release();
}

}

CyanaNOAParser::CyanaNOAParser(TokenStream *input) : CyanaNOAParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

CyanaNOAParser::CyanaNOAParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  CyanaNOAParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *cyananoaparserParserStaticData->atn, cyananoaparserParserStaticData->decisionToDFA, cyananoaparserParserStaticData->sharedContextCache, options);
}

CyanaNOAParser::~CyanaNOAParser() {
  delete _interpreter;
}

const atn::ATN& CyanaNOAParser::getATN() const {
  return *cyananoaparserParserStaticData->atn;
}

std::string CyanaNOAParser::getGrammarFileName() const {
  return "CyanaNOAParser.g4";
}

const std::vector<std::string>& CyanaNOAParser::getRuleNames() const {
  return cyananoaparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& CyanaNOAParser::getVocabulary() const {
  return cyananoaparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView CyanaNOAParser::getSerializedATN() const {
  return cyananoaparserParserStaticData->serializedATN;
}


//----------------- Cyana_noaContext ------------------------------------------------------------------

CyanaNOAParser::Cyana_noaContext::Cyana_noaContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaNOAParser::Cyana_noaContext::EOF() {
  return getToken(CyanaNOAParser::EOF, 0);
}

std::vector<CyanaNOAParser::CommentContext *> CyanaNOAParser::Cyana_noaContext::comment() {
  return getRuleContexts<CyanaNOAParser::CommentContext>();
}

CyanaNOAParser::CommentContext* CyanaNOAParser::Cyana_noaContext::comment(size_t i) {
  return getRuleContext<CyanaNOAParser::CommentContext>(i);
}

std::vector<CyanaNOAParser::Noe_peaksContext *> CyanaNOAParser::Cyana_noaContext::noe_peaks() {
  return getRuleContexts<CyanaNOAParser::Noe_peaksContext>();
}

CyanaNOAParser::Noe_peaksContext* CyanaNOAParser::Cyana_noaContext::noe_peaks(size_t i) {
  return getRuleContext<CyanaNOAParser::Noe_peaksContext>(i);
}

std::vector<CyanaNOAParser::Noe_statContext *> CyanaNOAParser::Cyana_noaContext::noe_stat() {
  return getRuleContexts<CyanaNOAParser::Noe_statContext>();
}

CyanaNOAParser::Noe_statContext* CyanaNOAParser::Cyana_noaContext::noe_stat(size_t i) {
  return getRuleContext<CyanaNOAParser::Noe_statContext>(i);
}

std::vector<CyanaNOAParser::Peak_statContext *> CyanaNOAParser::Cyana_noaContext::peak_stat() {
  return getRuleContexts<CyanaNOAParser::Peak_statContext>();
}

CyanaNOAParser::Peak_statContext* CyanaNOAParser::Cyana_noaContext::peak_stat(size_t i) {
  return getRuleContext<CyanaNOAParser::Peak_statContext>(i);
}


size_t CyanaNOAParser::Cyana_noaContext::getRuleIndex() const {
  return CyanaNOAParser::RuleCyana_noa;
}


std::any CyanaNOAParser::Cyana_noaContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaNOAParserVisitor*>(visitor))
    return parserVisitor->visitCyana_noa(this);
  else
    return visitor->visitChildren(this);
}

CyanaNOAParser::Cyana_noaContext* CyanaNOAParser::cyana_noa() {
  Cyana_noaContext *_localctx = _tracker.createInstance<Cyana_noaContext>(_ctx, getState());
  enterRule(_localctx, 0, CyanaNOAParser::RuleCyana_noa);
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
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & -9223372036821090302) != 0)) {
      setState(28);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case CyanaNOAParser::COMMENT: {
          setState(24);
          comment();
          break;
        }

        case CyanaNOAParser::Peak: {
          setState(25);
          noe_peaks();
          break;
        }

        case CyanaNOAParser::Average_quality: {
          setState(26);
          noe_stat();
          break;
        }

        case CyanaNOAParser::Peaks: {
          setState(27);
          peak_stat();
          break;
        }

      default:
        throw NoViableAltException(this);
      }
      setState(32);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(33);
    match(CyanaNOAParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CommentContext ------------------------------------------------------------------

CyanaNOAParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaNOAParser::CommentContext::COMMENT() {
  return getToken(CyanaNOAParser::COMMENT, 0);
}

tree::TerminalNode* CyanaNOAParser::CommentContext::RETURN_CM() {
  return getToken(CyanaNOAParser::RETURN_CM, 0);
}

tree::TerminalNode* CyanaNOAParser::CommentContext::EOF() {
  return getToken(CyanaNOAParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CyanaNOAParser::CommentContext::Any_name() {
  return getTokens(CyanaNOAParser::Any_name);
}

tree::TerminalNode* CyanaNOAParser::CommentContext::Any_name(size_t i) {
  return getToken(CyanaNOAParser::Any_name, i);
}


size_t CyanaNOAParser::CommentContext::getRuleIndex() const {
  return CyanaNOAParser::RuleComment;
}


std::any CyanaNOAParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaNOAParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

CyanaNOAParser::CommentContext* CyanaNOAParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 2, CyanaNOAParser::RuleComment);
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
    setState(35);
    match(CyanaNOAParser::COMMENT);
    setState(39);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaNOAParser::Any_name) {
      setState(36);
      match(CyanaNOAParser::Any_name);
      setState(41);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(42);
    _la = _input->LA(1);
    if (!(_la == CyanaNOAParser::EOF || _la == CyanaNOAParser::RETURN_CM)) {
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

//----------------- Noe_peaksContext ------------------------------------------------------------------

CyanaNOAParser::Noe_peaksContext::Noe_peaksContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CyanaNOAParser::Peak_headerContext* CyanaNOAParser::Noe_peaksContext::peak_header() {
  return getRuleContext<CyanaNOAParser::Peak_headerContext>(0);
}

CyanaNOAParser::Peak_qualityContext* CyanaNOAParser::Noe_peaksContext::peak_quality() {
  return getRuleContext<CyanaNOAParser::Peak_qualityContext>(0);
}

CyanaNOAParser::Noe_assignmentsContext* CyanaNOAParser::Noe_peaksContext::noe_assignments() {
  return getRuleContext<CyanaNOAParser::Noe_assignmentsContext>(0);
}


size_t CyanaNOAParser::Noe_peaksContext::getRuleIndex() const {
  return CyanaNOAParser::RuleNoe_peaks;
}


std::any CyanaNOAParser::Noe_peaksContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaNOAParserVisitor*>(visitor))
    return parserVisitor->visitNoe_peaks(this);
  else
    return visitor->visitChildren(this);
}

CyanaNOAParser::Noe_peaksContext* CyanaNOAParser::noe_peaks() {
  Noe_peaksContext *_localctx = _tracker.createInstance<Noe_peaksContext>(_ctx, getState());
  enterRule(_localctx, 4, CyanaNOAParser::RuleNoe_peaks);
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
    peak_header();
    setState(45);
    peak_quality();
    setState(47);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaNOAParser::Simple_name) {
      setState(46);
      noe_assignments();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_headerContext ------------------------------------------------------------------

CyanaNOAParser::Peak_headerContext::Peak_headerContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::Peak() {
  return getToken(CyanaNOAParser::Peak, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::Integer() {
  return getToken(CyanaNOAParser::Integer, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::From() {
  return getToken(CyanaNOAParser::From, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::File_name() {
  return getToken(CyanaNOAParser::File_name, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::L_paren() {
  return getToken(CyanaNOAParser::L_paren, 0);
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Peak_headerContext::Float() {
  return getTokens(CyanaNOAParser::Float);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::Float(size_t i) {
  return getToken(CyanaNOAParser::Float, i);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::Comma() {
  return getToken(CyanaNOAParser::Comma, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::Ppm_SC() {
  return getToken(CyanaNOAParser::Ppm_SC, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::R_paren() {
  return getToken(CyanaNOAParser::R_paren, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::Colon() {
  return getToken(CyanaNOAParser::Colon, 0);
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Peak_headerContext::Angstrome() {
  return getTokens(CyanaNOAParser::Angstrome);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::Angstrome(size_t i) {
  return getToken(CyanaNOAParser::Angstrome, i);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::Diagonal() {
  return getToken(CyanaNOAParser::Diagonal, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::Increased_from() {
  return getToken(CyanaNOAParser::Increased_from, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_headerContext::Decreased_from() {
  return getToken(CyanaNOAParser::Decreased_from, 0);
}


size_t CyanaNOAParser::Peak_headerContext::getRuleIndex() const {
  return CyanaNOAParser::RulePeak_header;
}


std::any CyanaNOAParser::Peak_headerContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaNOAParserVisitor*>(visitor))
    return parserVisitor->visitPeak_header(this);
  else
    return visitor->visitChildren(this);
}

CyanaNOAParser::Peak_headerContext* CyanaNOAParser::peak_header() {
  Peak_headerContext *_localctx = _tracker.createInstance<Peak_headerContext>(_ctx, getState());
  enterRule(_localctx, 6, CyanaNOAParser::RulePeak_header);
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
    setState(49);
    match(CyanaNOAParser::Peak);
    setState(50);
    match(CyanaNOAParser::Integer);
    setState(51);
    match(CyanaNOAParser::From);
    setState(52);
    match(CyanaNOAParser::File_name);
    setState(53);
    match(CyanaNOAParser::L_paren);
    setState(54);
    match(CyanaNOAParser::Float);
    setState(55);
    match(CyanaNOAParser::Comma);
    setState(56);
    match(CyanaNOAParser::Float);
    setState(57);
    match(CyanaNOAParser::Ppm_SC);
    setState(63);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx)) {
    case 1: {
      setState(58);
      match(CyanaNOAParser::Angstrome);
      break;
    }

    case 2: {
      setState(59);
      match(CyanaNOAParser::Angstrome);
      setState(60);
      _la = _input->LA(1);
      if (!(_la == CyanaNOAParser::Increased_from

      || _la == CyanaNOAParser::Decreased_from)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(61);
      match(CyanaNOAParser::Angstrome);
      break;
    }

    case 3: {
      setState(62);
      match(CyanaNOAParser::Diagonal);
      break;
    }

    default:
      break;
    }
    setState(65);
    match(CyanaNOAParser::R_paren);
    setState(66);
    match(CyanaNOAParser::Colon);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_qualityContext ------------------------------------------------------------------

CyanaNOAParser::Peak_qualityContext::Peak_qualityContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Peak_qualityContext::Integer() {
  return getTokens(CyanaNOAParser::Integer);
}

tree::TerminalNode* CyanaNOAParser::Peak_qualityContext::Integer(size_t i) {
  return getToken(CyanaNOAParser::Integer, i);
}

tree::TerminalNode* CyanaNOAParser::Peak_qualityContext::Out_of() {
  return getToken(CyanaNOAParser::Out_of, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_qualityContext::Assignments_used() {
  return getToken(CyanaNOAParser::Assignments_used, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_qualityContext::Comma() {
  return getToken(CyanaNOAParser::Comma, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_qualityContext::Quality() {
  return getToken(CyanaNOAParser::Quality, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_qualityContext::Equ_op() {
  return getToken(CyanaNOAParser::Equ_op, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_qualityContext::Float() {
  return getToken(CyanaNOAParser::Float, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_qualityContext::Colon() {
  return getToken(CyanaNOAParser::Colon, 0);
}


size_t CyanaNOAParser::Peak_qualityContext::getRuleIndex() const {
  return CyanaNOAParser::RulePeak_quality;
}


std::any CyanaNOAParser::Peak_qualityContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaNOAParserVisitor*>(visitor))
    return parserVisitor->visitPeak_quality(this);
  else
    return visitor->visitChildren(this);
}

CyanaNOAParser::Peak_qualityContext* CyanaNOAParser::peak_quality() {
  Peak_qualityContext *_localctx = _tracker.createInstance<Peak_qualityContext>(_ctx, getState());
  enterRule(_localctx, 8, CyanaNOAParser::RulePeak_quality);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(68);
    match(CyanaNOAParser::Integer);
    setState(69);
    match(CyanaNOAParser::Out_of);
    setState(70);
    match(CyanaNOAParser::Integer);
    setState(71);
    match(CyanaNOAParser::Assignments_used);
    setState(72);
    match(CyanaNOAParser::Comma);
    setState(73);
    match(CyanaNOAParser::Quality);
    setState(74);
    match(CyanaNOAParser::Equ_op);
    setState(75);
    match(CyanaNOAParser::Float);
    setState(76);
    match(CyanaNOAParser::Colon);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Noe_assignmentsContext ------------------------------------------------------------------

CyanaNOAParser::Noe_assignmentsContext::Noe_assignmentsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaNOAParser::Noe_assignmentContext *> CyanaNOAParser::Noe_assignmentsContext::noe_assignment() {
  return getRuleContexts<CyanaNOAParser::Noe_assignmentContext>();
}

CyanaNOAParser::Noe_assignmentContext* CyanaNOAParser::Noe_assignmentsContext::noe_assignment(size_t i) {
  return getRuleContext<CyanaNOAParser::Noe_assignmentContext>(i);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentsContext::Violated_in() {
  return getToken(CyanaNOAParser::Violated_in, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentsContext::Integer() {
  return getToken(CyanaNOAParser::Integer, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentsContext::Structures_by() {
  return getToken(CyanaNOAParser::Structures_by, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentsContext::Angstrome() {
  return getToken(CyanaNOAParser::Angstrome, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentsContext::Period() {
  return getToken(CyanaNOAParser::Period, 0);
}


size_t CyanaNOAParser::Noe_assignmentsContext::getRuleIndex() const {
  return CyanaNOAParser::RuleNoe_assignments;
}


std::any CyanaNOAParser::Noe_assignmentsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaNOAParserVisitor*>(visitor))
    return parserVisitor->visitNoe_assignments(this);
  else
    return visitor->visitChildren(this);
}

CyanaNOAParser::Noe_assignmentsContext* CyanaNOAParser::noe_assignments() {
  Noe_assignmentsContext *_localctx = _tracker.createInstance<Noe_assignmentsContext>(_ctx, getState());
  enterRule(_localctx, 10, CyanaNOAParser::RuleNoe_assignments);
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
    setState(79); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(78);
      noe_assignment();
      setState(81); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == CyanaNOAParser::Simple_name);
    setState(88);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaNOAParser::Violated_in) {
      setState(83);
      match(CyanaNOAParser::Violated_in);
      setState(84);
      match(CyanaNOAParser::Integer);
      setState(85);
      match(CyanaNOAParser::Structures_by);
      setState(86);
      match(CyanaNOAParser::Angstrome);
      setState(87);
      match(CyanaNOAParser::Period);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Noe_assignmentContext ------------------------------------------------------------------

CyanaNOAParser::Noe_assignmentContext::Noe_assignmentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Noe_assignmentContext::Simple_name() {
  return getTokens(CyanaNOAParser::Simple_name);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentContext::Simple_name(size_t i) {
  return getToken(CyanaNOAParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Noe_assignmentContext::Integer() {
  return getTokens(CyanaNOAParser::Integer);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentContext::Integer(size_t i) {
  return getToken(CyanaNOAParser::Integer, i);
}

CyanaNOAParser::Numerical_reportContext* CyanaNOAParser::Noe_assignmentContext::numerical_report() {
  return getRuleContext<CyanaNOAParser::Numerical_reportContext>(0);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentContext::Add_op() {
  return getToken(CyanaNOAParser::Add_op, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentContext::Sub_op() {
  return getToken(CyanaNOAParser::Sub_op, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentContext::Ok() {
  return getToken(CyanaNOAParser::Ok, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentContext::Lone() {
  return getToken(CyanaNOAParser::Lone, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentContext::Poor() {
  return getToken(CyanaNOAParser::Poor, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_assignmentContext::Far() {
  return getToken(CyanaNOAParser::Far, 0);
}


size_t CyanaNOAParser::Noe_assignmentContext::getRuleIndex() const {
  return CyanaNOAParser::RuleNoe_assignment;
}


std::any CyanaNOAParser::Noe_assignmentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaNOAParserVisitor*>(visitor))
    return parserVisitor->visitNoe_assignment(this);
  else
    return visitor->visitChildren(this);
}

CyanaNOAParser::Noe_assignmentContext* CyanaNOAParser::noe_assignment() {
  Noe_assignmentContext *_localctx = _tracker.createInstance<Noe_assignmentContext>(_ctx, getState());
  enterRule(_localctx, 12, CyanaNOAParser::RuleNoe_assignment);
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
    setState(90);
    match(CyanaNOAParser::Simple_name);
    setState(91);
    match(CyanaNOAParser::Simple_name);
    setState(92);
    match(CyanaNOAParser::Integer);
    setState(93);
    _la = _input->LA(1);
    if (!(_la == CyanaNOAParser::Add_op

    || _la == CyanaNOAParser::Sub_op)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(94);
    match(CyanaNOAParser::Simple_name);
    setState(95);
    match(CyanaNOAParser::Simple_name);
    setState(96);
    match(CyanaNOAParser::Integer);
    setState(97);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 15360) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(98);
    match(CyanaNOAParser::Integer);
    setState(99);
    numerical_report();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Numerical_reportContext ------------------------------------------------------------------

CyanaNOAParser::Numerical_reportContext::Numerical_reportContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Numerical_reportContext::Integer() {
  return getTokens(CyanaNOAParser::Integer);
}

tree::TerminalNode* CyanaNOAParser::Numerical_reportContext::Integer(size_t i) {
  return getToken(CyanaNOAParser::Integer, i);
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Numerical_reportContext::Sub_op() {
  return getTokens(CyanaNOAParser::Sub_op);
}

tree::TerminalNode* CyanaNOAParser::Numerical_reportContext::Sub_op(size_t i) {
  return getToken(CyanaNOAParser::Sub_op, i);
}

tree::TerminalNode* CyanaNOAParser::Numerical_reportContext::Distance_range() {
  return getToken(CyanaNOAParser::Distance_range, 0);
}

CyanaNOAParser::Extended_reportContext* CyanaNOAParser::Numerical_reportContext::extended_report() {
  return getRuleContext<CyanaNOAParser::Extended_reportContext>(0);
}


size_t CyanaNOAParser::Numerical_reportContext::getRuleIndex() const {
  return CyanaNOAParser::RuleNumerical_report;
}


std::any CyanaNOAParser::Numerical_reportContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaNOAParserVisitor*>(visitor))
    return parserVisitor->visitNumerical_report(this);
  else
    return visitor->visitChildren(this);
}

CyanaNOAParser::Numerical_reportContext* CyanaNOAParser::numerical_report() {
  Numerical_reportContext *_localctx = _tracker.createInstance<Numerical_reportContext>(_ctx, getState());
  enterRule(_localctx, 14, CyanaNOAParser::RuleNumerical_report);
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
    setState(101);
    match(CyanaNOAParser::Integer);
    setState(102);
    _la = _input->LA(1);
    if (!(_la == CyanaNOAParser::Sub_op

    || _la == CyanaNOAParser::Integer)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(103);
    _la = _input->LA(1);
    if (!(_la == CyanaNOAParser::Sub_op

    || _la == CyanaNOAParser::Integer)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(105);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaNOAParser::Distance_range) {
      setState(104);
      match(CyanaNOAParser::Distance_range);
    }
    setState(108);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8646911284551352320) != 0)) {
      setState(107);
      extended_report();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Extended_reportContext ------------------------------------------------------------------

CyanaNOAParser::Extended_reportContext::Extended_reportContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaNOAParser::Extended_reportContext::Numerical_report1() {
  return getToken(CyanaNOAParser::Numerical_report1, 0);
}

tree::TerminalNode* CyanaNOAParser::Extended_reportContext::Numerical_report2() {
  return getToken(CyanaNOAParser::Numerical_report2, 0);
}

tree::TerminalNode* CyanaNOAParser::Extended_reportContext::Numerical_report3() {
  return getToken(CyanaNOAParser::Numerical_report3, 0);
}

tree::TerminalNode* CyanaNOAParser::Extended_reportContext::Numerical_report4() {
  return getToken(CyanaNOAParser::Numerical_report4, 0);
}

CyanaNOAParser::Extended_reportContext* CyanaNOAParser::Extended_reportContext::extended_report() {
  return getRuleContext<CyanaNOAParser::Extended_reportContext>(0);
}


size_t CyanaNOAParser::Extended_reportContext::getRuleIndex() const {
  return CyanaNOAParser::RuleExtended_report;
}


std::any CyanaNOAParser::Extended_reportContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaNOAParserVisitor*>(visitor))
    return parserVisitor->visitExtended_report(this);
  else
    return visitor->visitChildren(this);
}

CyanaNOAParser::Extended_reportContext* CyanaNOAParser::extended_report() {
  Extended_reportContext *_localctx = _tracker.createInstance<Extended_reportContext>(_ctx, getState());
  enterRule(_localctx, 16, CyanaNOAParser::RuleExtended_report);
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
    setState(110);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8646911284551352320) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(112);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8646911284551352320) != 0)) {
      setState(111);
      extended_report();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Noe_statContext ------------------------------------------------------------------

CyanaNOAParser::Noe_statContext::Noe_statContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Average_quality() {
  return getToken(CyanaNOAParser::Average_quality, 0);
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Noe_statContext::Colon() {
  return getTokens(CyanaNOAParser::Colon);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Colon(size_t i) {
  return getToken(CyanaNOAParser::Colon, i);
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Noe_statContext::Float() {
  return getTokens(CyanaNOAParser::Float);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Float(size_t i) {
  return getToken(CyanaNOAParser::Float, i);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Average_number() {
  return getToken(CyanaNOAParser::Average_number, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Peaks_inc_upl() {
  return getToken(CyanaNOAParser::Peaks_inc_upl, 0);
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Noe_statContext::Integer() {
  return getTokens(CyanaNOAParser::Integer);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Integer(size_t i) {
  return getToken(CyanaNOAParser::Integer, i);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Peaks_dec_upl() {
  return getToken(CyanaNOAParser::Peaks_dec_upl, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Protons_used_in_less() {
  return getToken(CyanaNOAParser::Protons_used_in_less, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Peak_obs_dist() {
  return getToken(CyanaNOAParser::Peak_obs_dist, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Angstrome() {
  return getToken(CyanaNOAParser::Angstrome, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Atom() {
  return getToken(CyanaNOAParser::Atom, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Residue() {
  return getToken(CyanaNOAParser::Residue, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Shift() {
  return getToken(CyanaNOAParser::Shift, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Peaks() {
  return getToken(CyanaNOAParser::Peaks, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Used() {
  return getToken(CyanaNOAParser::Used, 0);
}

tree::TerminalNode* CyanaNOAParser::Noe_statContext::Expect() {
  return getToken(CyanaNOAParser::Expect, 0);
}

std::vector<CyanaNOAParser::List_of_protonContext *> CyanaNOAParser::Noe_statContext::list_of_proton() {
  return getRuleContexts<CyanaNOAParser::List_of_protonContext>();
}

CyanaNOAParser::List_of_protonContext* CyanaNOAParser::Noe_statContext::list_of_proton(size_t i) {
  return getRuleContext<CyanaNOAParser::List_of_protonContext>(i);
}


size_t CyanaNOAParser::Noe_statContext::getRuleIndex() const {
  return CyanaNOAParser::RuleNoe_stat;
}


std::any CyanaNOAParser::Noe_statContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaNOAParserVisitor*>(visitor))
    return parserVisitor->visitNoe_stat(this);
  else
    return visitor->visitChildren(this);
}

CyanaNOAParser::Noe_statContext* CyanaNOAParser::noe_stat() {
  Noe_statContext *_localctx = _tracker.createInstance<Noe_statContext>(_ctx, getState());
  enterRule(_localctx, 18, CyanaNOAParser::RuleNoe_stat);
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
    setState(114);
    match(CyanaNOAParser::Average_quality);
    setState(115);
    match(CyanaNOAParser::Colon);
    setState(116);
    match(CyanaNOAParser::Float);
    setState(117);
    match(CyanaNOAParser::Average_number);
    setState(118);
    match(CyanaNOAParser::Colon);
    setState(119);
    match(CyanaNOAParser::Float);
    setState(120);
    match(CyanaNOAParser::Peaks_inc_upl);
    setState(121);
    match(CyanaNOAParser::Colon);
    setState(122);
    match(CyanaNOAParser::Integer);
    setState(123);
    match(CyanaNOAParser::Peaks_dec_upl);
    setState(124);
    match(CyanaNOAParser::Colon);
    setState(125);
    match(CyanaNOAParser::Integer);
    setState(126);
    match(CyanaNOAParser::Protons_used_in_less);
    setState(127);
    match(CyanaNOAParser::Colon);
    setState(128);
    match(CyanaNOAParser::Peak_obs_dist);
    setState(129);
    match(CyanaNOAParser::Colon);
    setState(130);
    match(CyanaNOAParser::Angstrome);
    setState(131);
    match(CyanaNOAParser::Atom);
    setState(132);
    match(CyanaNOAParser::Residue);
    setState(133);
    match(CyanaNOAParser::Shift);
    setState(134);
    match(CyanaNOAParser::Peaks);
    setState(135);
    match(CyanaNOAParser::Used);
    setState(136);
    match(CyanaNOAParser::Expect);
    setState(140);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaNOAParser::Simple_name) {
      setState(137);
      list_of_proton();
      setState(142);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- List_of_protonContext ------------------------------------------------------------------

CyanaNOAParser::List_of_protonContext::List_of_protonContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> CyanaNOAParser::List_of_protonContext::Simple_name() {
  return getTokens(CyanaNOAParser::Simple_name);
}

tree::TerminalNode* CyanaNOAParser::List_of_protonContext::Simple_name(size_t i) {
  return getToken(CyanaNOAParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> CyanaNOAParser::List_of_protonContext::Integer() {
  return getTokens(CyanaNOAParser::Integer);
}

tree::TerminalNode* CyanaNOAParser::List_of_protonContext::Integer(size_t i) {
  return getToken(CyanaNOAParser::Integer, i);
}

tree::TerminalNode* CyanaNOAParser::List_of_protonContext::Float() {
  return getToken(CyanaNOAParser::Float, 0);
}


size_t CyanaNOAParser::List_of_protonContext::getRuleIndex() const {
  return CyanaNOAParser::RuleList_of_proton;
}


std::any CyanaNOAParser::List_of_protonContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaNOAParserVisitor*>(visitor))
    return parserVisitor->visitList_of_proton(this);
  else
    return visitor->visitChildren(this);
}

CyanaNOAParser::List_of_protonContext* CyanaNOAParser::list_of_proton() {
  List_of_protonContext *_localctx = _tracker.createInstance<List_of_protonContext>(_ctx, getState());
  enterRule(_localctx, 20, CyanaNOAParser::RuleList_of_proton);

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
    match(CyanaNOAParser::Simple_name);
    setState(144);
    match(CyanaNOAParser::Simple_name);
    setState(145);
    match(CyanaNOAParser::Integer);
    setState(146);
    match(CyanaNOAParser::Float);
    setState(147);
    match(CyanaNOAParser::Integer);
    setState(148);
    match(CyanaNOAParser::Integer);
    setState(149);
    match(CyanaNOAParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_statContext ------------------------------------------------------------------

CyanaNOAParser::Peak_statContext::Peak_statContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Peaks() {
  return getToken(CyanaNOAParser::Peaks, 0);
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Peak_statContext::Colon() {
  return getTokens(CyanaNOAParser::Colon);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Colon(size_t i) {
  return getToken(CyanaNOAParser::Colon, i);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Selected() {
  return getToken(CyanaNOAParser::Selected, 0);
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Peak_statContext::Integer() {
  return getTokens(CyanaNOAParser::Integer);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Integer(size_t i) {
  return getToken(CyanaNOAParser::Integer, i);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Assigned() {
  return getToken(CyanaNOAParser::Assigned, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Unassigned() {
  return getToken(CyanaNOAParser::Unassigned, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::With_diagonal() {
  return getToken(CyanaNOAParser::With_diagonal, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Cross_peaks() {
  return getToken(CyanaNOAParser::Cross_peaks, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::With_off_diagonal() {
  return getToken(CyanaNOAParser::With_off_diagonal, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::With_unique() {
  return getToken(CyanaNOAParser::With_unique, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::With_short_range() {
  return getToken(CyanaNOAParser::With_short_range, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Short_range_ex() {
  return getToken(CyanaNOAParser::Short_range_ex, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::With_medium_range() {
  return getToken(CyanaNOAParser::With_medium_range, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Medium_range_ex() {
  return getToken(CyanaNOAParser::Medium_range_ex, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::With_long_range() {
  return getToken(CyanaNOAParser::With_long_range, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Long_range_ex() {
  return getToken(CyanaNOAParser::Long_range_ex, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Without_possibility() {
  return getToken(CyanaNOAParser::Without_possibility, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::With_viol_below() {
  return getToken(CyanaNOAParser::With_viol_below, 0);
}

std::vector<tree::TerminalNode *> CyanaNOAParser::Peak_statContext::Angstrome() {
  return getTokens(CyanaNOAParser::Angstrome);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Angstrome(size_t i) {
  return getToken(CyanaNOAParser::Angstrome, i);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::With_viol_between() {
  return getToken(CyanaNOAParser::With_viol_between, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::Float() {
  return getToken(CyanaNOAParser::Float, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::And() {
  return getToken(CyanaNOAParser::And, 0);
}

tree::TerminalNode* CyanaNOAParser::Peak_statContext::With_viol_above() {
  return getToken(CyanaNOAParser::With_viol_above, 0);
}


size_t CyanaNOAParser::Peak_statContext::getRuleIndex() const {
  return CyanaNOAParser::RulePeak_stat;
}


std::any CyanaNOAParser::Peak_statContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaNOAParserVisitor*>(visitor))
    return parserVisitor->visitPeak_stat(this);
  else
    return visitor->visitChildren(this);
}

CyanaNOAParser::Peak_statContext* CyanaNOAParser::peak_stat() {
  Peak_statContext *_localctx = _tracker.createInstance<Peak_statContext>(_ctx, getState());
  enterRule(_localctx, 22, CyanaNOAParser::RulePeak_stat);
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
    setState(151);
    match(CyanaNOAParser::Peaks);
    setState(152);
    match(CyanaNOAParser::Colon);
    setState(153);
    match(CyanaNOAParser::Selected);
    setState(154);
    match(CyanaNOAParser::Colon);
    setState(155);
    match(CyanaNOAParser::Integer);
    setState(156);
    match(CyanaNOAParser::Assigned);
    setState(157);
    match(CyanaNOAParser::Colon);
    setState(158);
    match(CyanaNOAParser::Integer);
    setState(159);
    match(CyanaNOAParser::Unassigned);
    setState(160);
    match(CyanaNOAParser::Colon);
    setState(161);
    match(CyanaNOAParser::Integer);
    setState(165);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaNOAParser::Without_possibility) {
      setState(162);
      match(CyanaNOAParser::Without_possibility);
      setState(163);
      match(CyanaNOAParser::Colon);
      setState(164);
      match(CyanaNOAParser::Integer);
    }
    setState(171);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaNOAParser::With_viol_below) {
      setState(167);
      match(CyanaNOAParser::With_viol_below);
      setState(168);
      match(CyanaNOAParser::Angstrome);
      setState(169);
      match(CyanaNOAParser::Colon);
      setState(170);
      match(CyanaNOAParser::Integer);
    }
    setState(179);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaNOAParser::With_viol_between) {
      setState(173);
      match(CyanaNOAParser::With_viol_between);
      setState(174);
      match(CyanaNOAParser::Float);
      setState(175);
      match(CyanaNOAParser::And);
      setState(176);
      match(CyanaNOAParser::Angstrome);
      setState(177);
      match(CyanaNOAParser::Colon);
      setState(178);
      match(CyanaNOAParser::Integer);
    }
    setState(185);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaNOAParser::With_viol_above) {
      setState(181);
      match(CyanaNOAParser::With_viol_above);
      setState(182);
      match(CyanaNOAParser::Angstrome);
      setState(183);
      match(CyanaNOAParser::Colon);
      setState(184);
      match(CyanaNOAParser::Integer);
    }
    setState(187);
    match(CyanaNOAParser::With_diagonal);
    setState(188);
    match(CyanaNOAParser::Colon);
    setState(189);
    match(CyanaNOAParser::Integer);
    setState(190);
    match(CyanaNOAParser::Cross_peaks);
    setState(191);
    match(CyanaNOAParser::Colon);
    setState(192);
    match(CyanaNOAParser::With_off_diagonal);
    setState(193);
    match(CyanaNOAParser::Colon);
    setState(194);
    match(CyanaNOAParser::Integer);
    setState(195);
    match(CyanaNOAParser::With_unique);
    setState(196);
    match(CyanaNOAParser::Colon);
    setState(197);
    match(CyanaNOAParser::Integer);
    setState(198);
    match(CyanaNOAParser::With_short_range);
    setState(199);
    match(CyanaNOAParser::Short_range_ex);
    setState(200);
    match(CyanaNOAParser::Colon);
    setState(201);
    match(CyanaNOAParser::Integer);
    setState(202);
    match(CyanaNOAParser::With_medium_range);
    setState(203);
    match(CyanaNOAParser::Medium_range_ex);
    setState(204);
    match(CyanaNOAParser::Colon);
    setState(205);
    match(CyanaNOAParser::Integer);
    setState(206);
    match(CyanaNOAParser::With_long_range);
    setState(207);
    match(CyanaNOAParser::Long_range_ex);
    setState(208);
    match(CyanaNOAParser::Colon);
    setState(209);
    match(CyanaNOAParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

void CyanaNOAParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  cyananoaparserParserInitialize();
#else
  ::antlr4::internal::call_once(cyananoaparserParserOnceFlag, cyananoaparserParserInitialize);
#endif
}
