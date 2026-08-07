
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AriaMRParser.g4 by ANTLR 4.13.0


#include "AriaMRParserVisitor.h"

#include "AriaMRParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct AriaMRParserStaticData final {
  AriaMRParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  AriaMRParserStaticData(const AriaMRParserStaticData&) = delete;
  AriaMRParserStaticData(AriaMRParserStaticData&&) = delete;
  AriaMRParserStaticData& operator=(const AriaMRParserStaticData&) = delete;
  AriaMRParserStaticData& operator=(AriaMRParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag ariamrparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
AriaMRParserStaticData *ariamrparserParserStaticData = nullptr;

void ariamrparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (ariamrparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(ariamrparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<AriaMRParserStaticData>(
    std::vector<std::string>{
      "aria_mr", "distance_restraints", "distance_restraint", "contribution", 
      "atom_pair", "atom_selection", "old_distance_restraints", "old_distance_restraint", 
      "p_row", "a_row", "c_row", "number", "number_c"
    },
    std::vector<std::string>{
      "", "','", "", "", "", "", "", "", "'ref_spec:'", "'ref_peak:'", "'id:'", 
      "'d:'", "'u:'", "'u_viol:'", "'%_viol:'", "'viol:'", "'reliable:'", 
      "'a_type:'", "'weight:'", "'+/-'", "'-'", "'p'", "'a'", "'c'"
    },
    std::vector<std::string>{
      "", "COMMA", "Integer", "Float", "Real", "SHARP_COMMENT", "EXCLM_COMMENT", 
      "SMCLN_COMMENT", "RefSpec", "RefPeak", "Id", "D", "U", "UViol", "PViol", 
      "Viol", "Reliable", "AType", "Weight", "PlusMinus", "Hyphen", "P_code", 
      "A_code", "C_code", "Simple_name", "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", 
      "LINE_COMMENT", "SPACE_RS", "RefSpecName", "RETURN_RS", "SPACE_V", 
      "ViolFlag", "RETURN_V", "SPACE_R", "ReliableFlag", "RETURN_R", "SPACE_A", 
      "ATypeFlag", "RETURN_A"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,40,158,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,5,0,29,8,
  	0,10,0,12,0,32,9,0,1,0,1,0,1,1,4,1,37,8,1,11,1,12,1,38,1,2,1,2,1,2,1,
  	2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
  	4,2,62,8,2,11,2,12,2,63,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,74,8,3,1,
  	4,1,4,1,4,1,4,1,5,1,5,1,5,3,5,83,8,5,1,6,4,6,86,8,6,11,6,12,6,87,1,7,
  	1,7,1,7,4,7,93,8,7,11,7,12,7,94,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
  	8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
  	1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
  	1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
  	1,10,1,11,1,11,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,
  	0,1,1,0,2,3,152,0,30,1,0,0,0,2,36,1,0,0,0,4,40,1,0,0,0,6,65,1,0,0,0,8,
  	75,1,0,0,0,10,79,1,0,0,0,12,85,1,0,0,0,14,89,1,0,0,0,16,96,1,0,0,0,18,
  	114,1,0,0,0,20,127,1,0,0,0,22,153,1,0,0,0,24,155,1,0,0,0,26,29,3,2,1,
  	0,27,29,3,12,6,0,28,26,1,0,0,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,1,0,
  	0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,34,5,0,0,1,34,1,1,0,
  	0,0,35,37,3,4,2,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,
  	0,0,39,3,1,0,0,0,40,41,5,8,0,0,41,42,5,30,0,0,42,43,5,9,0,0,43,44,5,2,
  	0,0,44,45,5,10,0,0,45,46,5,2,0,0,46,47,5,11,0,0,47,48,3,22,11,0,48,49,
  	5,12,0,0,49,50,3,22,11,0,50,51,5,13,0,0,51,52,3,22,11,0,52,53,5,14,0,
  	0,53,54,3,22,11,0,54,55,5,15,0,0,55,56,5,33,0,0,56,57,5,16,0,0,57,58,
  	5,36,0,0,58,59,5,17,0,0,59,61,5,39,0,0,60,62,3,6,3,0,61,60,1,0,0,0,62,
  	63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,5,1,0,0,0,65,73,3,8,4,0,66,
  	67,5,11,0,0,67,68,3,24,12,0,68,69,5,19,0,0,69,70,3,24,12,0,70,71,5,18,
  	0,0,71,72,3,24,12,0,72,74,1,0,0,0,73,66,1,0,0,0,73,74,1,0,0,0,74,7,1,
  	0,0,0,75,76,3,10,5,0,76,77,5,20,0,0,77,78,3,10,5,0,78,9,1,0,0,0,79,80,
  	5,24,0,0,80,82,5,24,0,0,81,83,5,24,0,0,82,81,1,0,0,0,82,83,1,0,0,0,83,
  	11,1,0,0,0,84,86,3,14,7,0,85,84,1,0,0,0,86,87,1,0,0,0,87,85,1,0,0,0,87,
  	88,1,0,0,0,88,13,1,0,0,0,89,90,3,16,8,0,90,92,3,18,9,0,91,93,3,20,10,
  	0,92,91,1,0,0,0,93,94,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,15,1,0,0,
  	0,96,97,5,21,0,0,97,98,5,2,0,0,98,99,5,2,0,0,99,100,5,2,0,0,100,101,5,
  	3,0,0,101,102,5,4,0,0,102,103,5,20,0,0,103,104,5,20,0,0,104,105,5,20,
  	0,0,105,106,5,20,0,0,106,107,5,3,0,0,107,108,5,3,0,0,108,109,5,3,0,0,
  	109,110,5,20,0,0,110,111,5,3,0,0,111,112,5,3,0,0,112,113,5,3,0,0,113,
  	17,1,0,0,0,114,115,5,22,0,0,115,116,5,2,0,0,116,117,5,3,0,0,117,118,5,
  	3,0,0,118,119,5,3,0,0,119,120,5,3,0,0,120,121,5,4,0,0,121,122,5,4,0,0,
  	122,123,5,4,0,0,123,124,5,4,0,0,124,125,5,2,0,0,125,126,5,2,0,0,126,19,
  	1,0,0,0,127,128,5,23,0,0,128,129,5,3,0,0,129,130,5,3,0,0,130,131,5,3,
  	0,0,131,132,5,3,0,0,132,133,5,3,0,0,133,134,5,3,0,0,134,135,5,20,0,0,
  	135,136,5,2,0,0,136,137,5,24,0,0,137,138,5,24,0,0,138,139,5,3,0,0,139,
  	140,5,3,0,0,140,141,5,24,0,0,141,142,5,3,0,0,142,143,5,3,0,0,143,144,
  	5,20,0,0,144,145,5,2,0,0,145,146,5,24,0,0,146,147,5,24,0,0,147,148,5,
  	3,0,0,148,149,5,3,0,0,149,150,5,24,0,0,150,151,5,3,0,0,151,152,5,3,0,
  	0,152,21,1,0,0,0,153,154,7,0,0,0,154,23,1,0,0,0,155,156,7,0,0,0,156,25,
  	1,0,0,0,8,28,30,38,63,73,82,87,94
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  ariamrparserParserStaticData = staticData.release();
}

}

AriaMRParser::AriaMRParser(TokenStream *input) : AriaMRParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

AriaMRParser::AriaMRParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  AriaMRParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *ariamrparserParserStaticData->atn, ariamrparserParserStaticData->decisionToDFA, ariamrparserParserStaticData->sharedContextCache, options);
}

AriaMRParser::~AriaMRParser() {
  delete _interpreter;
}

const atn::ATN& AriaMRParser::getATN() const {
  return *ariamrparserParserStaticData->atn;
}

std::string AriaMRParser::getGrammarFileName() const {
  return "AriaMRParser.g4";
}

const std::vector<std::string>& AriaMRParser::getRuleNames() const {
  return ariamrparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& AriaMRParser::getVocabulary() const {
  return ariamrparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView AriaMRParser::getSerializedATN() const {
  return ariamrparserParserStaticData->serializedATN;
}


//----------------- Aria_mrContext ------------------------------------------------------------------

AriaMRParser::Aria_mrContext::Aria_mrContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AriaMRParser::Aria_mrContext::EOF() {
  return getToken(AriaMRParser::EOF, 0);
}

std::vector<AriaMRParser::Distance_restraintsContext *> AriaMRParser::Aria_mrContext::distance_restraints() {
  return getRuleContexts<AriaMRParser::Distance_restraintsContext>();
}

AriaMRParser::Distance_restraintsContext* AriaMRParser::Aria_mrContext::distance_restraints(size_t i) {
  return getRuleContext<AriaMRParser::Distance_restraintsContext>(i);
}

std::vector<AriaMRParser::Old_distance_restraintsContext *> AriaMRParser::Aria_mrContext::old_distance_restraints() {
  return getRuleContexts<AriaMRParser::Old_distance_restraintsContext>();
}

AriaMRParser::Old_distance_restraintsContext* AriaMRParser::Aria_mrContext::old_distance_restraints(size_t i) {
  return getRuleContext<AriaMRParser::Old_distance_restraintsContext>(i);
}


size_t AriaMRParser::Aria_mrContext::getRuleIndex() const {
  return AriaMRParser::RuleAria_mr;
}


std::any AriaMRParser::Aria_mrContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitAria_mr(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::Aria_mrContext* AriaMRParser::aria_mr() {
  Aria_mrContext *_localctx = _tracker.createInstance<Aria_mrContext>(_ctx, getState());
  enterRule(_localctx, 0, AriaMRParser::RuleAria_mr);
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
    while (_la == AriaMRParser::RefSpec

    || _la == AriaMRParser::P_code) {
      setState(28);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case AriaMRParser::RefSpec: {
          setState(26);
          distance_restraints();
          break;
        }

        case AriaMRParser::P_code: {
          setState(27);
          old_distance_restraints();
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
    match(AriaMRParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_restraintsContext ------------------------------------------------------------------

AriaMRParser::Distance_restraintsContext::Distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<AriaMRParser::Distance_restraintContext *> AriaMRParser::Distance_restraintsContext::distance_restraint() {
  return getRuleContexts<AriaMRParser::Distance_restraintContext>();
}

AriaMRParser::Distance_restraintContext* AriaMRParser::Distance_restraintsContext::distance_restraint(size_t i) {
  return getRuleContext<AriaMRParser::Distance_restraintContext>(i);
}


size_t AriaMRParser::Distance_restraintsContext::getRuleIndex() const {
  return AriaMRParser::RuleDistance_restraints;
}


std::any AriaMRParser::Distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraints(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::Distance_restraintsContext* AriaMRParser::distance_restraints() {
  Distance_restraintsContext *_localctx = _tracker.createInstance<Distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 2, AriaMRParser::RuleDistance_restraints);

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
    setState(36); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(35);
              distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(38); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_restraintContext ------------------------------------------------------------------

AriaMRParser::Distance_restraintContext::Distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::RefSpec() {
  return getToken(AriaMRParser::RefSpec, 0);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::RefSpecName() {
  return getToken(AriaMRParser::RefSpecName, 0);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::RefPeak() {
  return getToken(AriaMRParser::RefPeak, 0);
}

std::vector<tree::TerminalNode *> AriaMRParser::Distance_restraintContext::Integer() {
  return getTokens(AriaMRParser::Integer);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::Integer(size_t i) {
  return getToken(AriaMRParser::Integer, i);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::Id() {
  return getToken(AriaMRParser::Id, 0);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::D() {
  return getToken(AriaMRParser::D, 0);
}

std::vector<AriaMRParser::NumberContext *> AriaMRParser::Distance_restraintContext::number() {
  return getRuleContexts<AriaMRParser::NumberContext>();
}

AriaMRParser::NumberContext* AriaMRParser::Distance_restraintContext::number(size_t i) {
  return getRuleContext<AriaMRParser::NumberContext>(i);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::U() {
  return getToken(AriaMRParser::U, 0);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::UViol() {
  return getToken(AriaMRParser::UViol, 0);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::PViol() {
  return getToken(AriaMRParser::PViol, 0);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::Viol() {
  return getToken(AriaMRParser::Viol, 0);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::ViolFlag() {
  return getToken(AriaMRParser::ViolFlag, 0);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::Reliable() {
  return getToken(AriaMRParser::Reliable, 0);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::ReliableFlag() {
  return getToken(AriaMRParser::ReliableFlag, 0);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::AType() {
  return getToken(AriaMRParser::AType, 0);
}

tree::TerminalNode* AriaMRParser::Distance_restraintContext::ATypeFlag() {
  return getToken(AriaMRParser::ATypeFlag, 0);
}

std::vector<AriaMRParser::ContributionContext *> AriaMRParser::Distance_restraintContext::contribution() {
  return getRuleContexts<AriaMRParser::ContributionContext>();
}

AriaMRParser::ContributionContext* AriaMRParser::Distance_restraintContext::contribution(size_t i) {
  return getRuleContext<AriaMRParser::ContributionContext>(i);
}


size_t AriaMRParser::Distance_restraintContext::getRuleIndex() const {
  return AriaMRParser::RuleDistance_restraint;
}


std::any AriaMRParser::Distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraint(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::Distance_restraintContext* AriaMRParser::distance_restraint() {
  Distance_restraintContext *_localctx = _tracker.createInstance<Distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 4, AriaMRParser::RuleDistance_restraint);
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
    match(AriaMRParser::RefSpec);
    setState(41);
    match(AriaMRParser::RefSpecName);
    setState(42);
    match(AriaMRParser::RefPeak);
    setState(43);
    match(AriaMRParser::Integer);
    setState(44);
    match(AriaMRParser::Id);
    setState(45);
    match(AriaMRParser::Integer);
    setState(46);
    match(AriaMRParser::D);
    setState(47);
    number();
    setState(48);
    match(AriaMRParser::U);
    setState(49);
    number();
    setState(50);
    match(AriaMRParser::UViol);
    setState(51);
    number();
    setState(52);
    match(AriaMRParser::PViol);
    setState(53);
    number();
    setState(54);
    match(AriaMRParser::Viol);
    setState(55);
    match(AriaMRParser::ViolFlag);
    setState(56);
    match(AriaMRParser::Reliable);
    setState(57);
    match(AriaMRParser::ReliableFlag);
    setState(58);
    match(AriaMRParser::AType);
    setState(59);
    match(AriaMRParser::ATypeFlag);
    setState(61); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(60);
      contribution();
      setState(63); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == AriaMRParser::Simple_name);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ContributionContext ------------------------------------------------------------------

AriaMRParser::ContributionContext::ContributionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

AriaMRParser::Atom_pairContext* AriaMRParser::ContributionContext::atom_pair() {
  return getRuleContext<AriaMRParser::Atom_pairContext>(0);
}

tree::TerminalNode* AriaMRParser::ContributionContext::D() {
  return getToken(AriaMRParser::D, 0);
}

std::vector<AriaMRParser::Number_cContext *> AriaMRParser::ContributionContext::number_c() {
  return getRuleContexts<AriaMRParser::Number_cContext>();
}

AriaMRParser::Number_cContext* AriaMRParser::ContributionContext::number_c(size_t i) {
  return getRuleContext<AriaMRParser::Number_cContext>(i);
}

tree::TerminalNode* AriaMRParser::ContributionContext::PlusMinus() {
  return getToken(AriaMRParser::PlusMinus, 0);
}

tree::TerminalNode* AriaMRParser::ContributionContext::Weight() {
  return getToken(AriaMRParser::Weight, 0);
}


size_t AriaMRParser::ContributionContext::getRuleIndex() const {
  return AriaMRParser::RuleContribution;
}


std::any AriaMRParser::ContributionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitContribution(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::ContributionContext* AriaMRParser::contribution() {
  ContributionContext *_localctx = _tracker.createInstance<ContributionContext>(_ctx, getState());
  enterRule(_localctx, 6, AriaMRParser::RuleContribution);
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
    setState(65);
    atom_pair();
    setState(73);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == AriaMRParser::D) {
      setState(66);
      match(AriaMRParser::D);
      setState(67);
      number_c();
      setState(68);
      match(AriaMRParser::PlusMinus);
      setState(69);
      number_c();
      setState(70);
      match(AriaMRParser::Weight);
      setState(71);
      number_c();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Atom_pairContext ------------------------------------------------------------------

AriaMRParser::Atom_pairContext::Atom_pairContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<AriaMRParser::Atom_selectionContext *> AriaMRParser::Atom_pairContext::atom_selection() {
  return getRuleContexts<AriaMRParser::Atom_selectionContext>();
}

AriaMRParser::Atom_selectionContext* AriaMRParser::Atom_pairContext::atom_selection(size_t i) {
  return getRuleContext<AriaMRParser::Atom_selectionContext>(i);
}

tree::TerminalNode* AriaMRParser::Atom_pairContext::Hyphen() {
  return getToken(AriaMRParser::Hyphen, 0);
}


size_t AriaMRParser::Atom_pairContext::getRuleIndex() const {
  return AriaMRParser::RuleAtom_pair;
}


std::any AriaMRParser::Atom_pairContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitAtom_pair(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::Atom_pairContext* AriaMRParser::atom_pair() {
  Atom_pairContext *_localctx = _tracker.createInstance<Atom_pairContext>(_ctx, getState());
  enterRule(_localctx, 8, AriaMRParser::RuleAtom_pair);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(75);
    atom_selection();
    setState(76);
    match(AriaMRParser::Hyphen);
    setState(77);
    atom_selection();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Atom_selectionContext ------------------------------------------------------------------

AriaMRParser::Atom_selectionContext::Atom_selectionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> AriaMRParser::Atom_selectionContext::Simple_name() {
  return getTokens(AriaMRParser::Simple_name);
}

tree::TerminalNode* AriaMRParser::Atom_selectionContext::Simple_name(size_t i) {
  return getToken(AriaMRParser::Simple_name, i);
}


size_t AriaMRParser::Atom_selectionContext::getRuleIndex() const {
  return AriaMRParser::RuleAtom_selection;
}


std::any AriaMRParser::Atom_selectionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitAtom_selection(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::Atom_selectionContext* AriaMRParser::atom_selection() {
  Atom_selectionContext *_localctx = _tracker.createInstance<Atom_selectionContext>(_ctx, getState());
  enterRule(_localctx, 10, AriaMRParser::RuleAtom_selection);

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
    match(AriaMRParser::Simple_name);
    setState(80);
    match(AriaMRParser::Simple_name);
    setState(82);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx)) {
    case 1: {
      setState(81);
      match(AriaMRParser::Simple_name);
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

//----------------- Old_distance_restraintsContext ------------------------------------------------------------------

AriaMRParser::Old_distance_restraintsContext::Old_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<AriaMRParser::Old_distance_restraintContext *> AriaMRParser::Old_distance_restraintsContext::old_distance_restraint() {
  return getRuleContexts<AriaMRParser::Old_distance_restraintContext>();
}

AriaMRParser::Old_distance_restraintContext* AriaMRParser::Old_distance_restraintsContext::old_distance_restraint(size_t i) {
  return getRuleContext<AriaMRParser::Old_distance_restraintContext>(i);
}


size_t AriaMRParser::Old_distance_restraintsContext::getRuleIndex() const {
  return AriaMRParser::RuleOld_distance_restraints;
}


std::any AriaMRParser::Old_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitOld_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::Old_distance_restraintsContext* AriaMRParser::old_distance_restraints() {
  Old_distance_restraintsContext *_localctx = _tracker.createInstance<Old_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 12, AriaMRParser::RuleOld_distance_restraints);

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
    setState(85); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(84);
              old_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(87); 
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

//----------------- Old_distance_restraintContext ------------------------------------------------------------------

AriaMRParser::Old_distance_restraintContext::Old_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

AriaMRParser::P_rowContext* AriaMRParser::Old_distance_restraintContext::p_row() {
  return getRuleContext<AriaMRParser::P_rowContext>(0);
}

AriaMRParser::A_rowContext* AriaMRParser::Old_distance_restraintContext::a_row() {
  return getRuleContext<AriaMRParser::A_rowContext>(0);
}

std::vector<AriaMRParser::C_rowContext *> AriaMRParser::Old_distance_restraintContext::c_row() {
  return getRuleContexts<AriaMRParser::C_rowContext>();
}

AriaMRParser::C_rowContext* AriaMRParser::Old_distance_restraintContext::c_row(size_t i) {
  return getRuleContext<AriaMRParser::C_rowContext>(i);
}


size_t AriaMRParser::Old_distance_restraintContext::getRuleIndex() const {
  return AriaMRParser::RuleOld_distance_restraint;
}


std::any AriaMRParser::Old_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitOld_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::Old_distance_restraintContext* AriaMRParser::old_distance_restraint() {
  Old_distance_restraintContext *_localctx = _tracker.createInstance<Old_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 14, AriaMRParser::RuleOld_distance_restraint);
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
    p_row();
    setState(90);
    a_row();
    setState(92); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(91);
      c_row();
      setState(94); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == AriaMRParser::C_code);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- P_rowContext ------------------------------------------------------------------

AriaMRParser::P_rowContext::P_rowContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AriaMRParser::P_rowContext::P_code() {
  return getToken(AriaMRParser::P_code, 0);
}

std::vector<tree::TerminalNode *> AriaMRParser::P_rowContext::Integer() {
  return getTokens(AriaMRParser::Integer);
}

tree::TerminalNode* AriaMRParser::P_rowContext::Integer(size_t i) {
  return getToken(AriaMRParser::Integer, i);
}

std::vector<tree::TerminalNode *> AriaMRParser::P_rowContext::Float() {
  return getTokens(AriaMRParser::Float);
}

tree::TerminalNode* AriaMRParser::P_rowContext::Float(size_t i) {
  return getToken(AriaMRParser::Float, i);
}

tree::TerminalNode* AriaMRParser::P_rowContext::Real() {
  return getToken(AriaMRParser::Real, 0);
}

std::vector<tree::TerminalNode *> AriaMRParser::P_rowContext::Hyphen() {
  return getTokens(AriaMRParser::Hyphen);
}

tree::TerminalNode* AriaMRParser::P_rowContext::Hyphen(size_t i) {
  return getToken(AriaMRParser::Hyphen, i);
}


size_t AriaMRParser::P_rowContext::getRuleIndex() const {
  return AriaMRParser::RuleP_row;
}


std::any AriaMRParser::P_rowContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitP_row(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::P_rowContext* AriaMRParser::p_row() {
  P_rowContext *_localctx = _tracker.createInstance<P_rowContext>(_ctx, getState());
  enterRule(_localctx, 16, AriaMRParser::RuleP_row);

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
    match(AriaMRParser::P_code);
    setState(97);
    match(AriaMRParser::Integer);
    setState(98);
    match(AriaMRParser::Integer);
    setState(99);
    match(AriaMRParser::Integer);
    setState(100);
    match(AriaMRParser::Float);
    setState(101);
    match(AriaMRParser::Real);
    setState(102);
    match(AriaMRParser::Hyphen);
    setState(103);
    match(AriaMRParser::Hyphen);
    setState(104);
    match(AriaMRParser::Hyphen);
    setState(105);
    match(AriaMRParser::Hyphen);
    setState(106);
    match(AriaMRParser::Float);
    setState(107);
    match(AriaMRParser::Float);
    setState(108);
    match(AriaMRParser::Float);
    setState(109);
    match(AriaMRParser::Hyphen);
    setState(110);
    match(AriaMRParser::Float);
    setState(111);
    match(AriaMRParser::Float);
    setState(112);
    match(AriaMRParser::Float);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- A_rowContext ------------------------------------------------------------------

AriaMRParser::A_rowContext::A_rowContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AriaMRParser::A_rowContext::A_code() {
  return getToken(AriaMRParser::A_code, 0);
}

std::vector<tree::TerminalNode *> AriaMRParser::A_rowContext::Integer() {
  return getTokens(AriaMRParser::Integer);
}

tree::TerminalNode* AriaMRParser::A_rowContext::Integer(size_t i) {
  return getToken(AriaMRParser::Integer, i);
}

std::vector<tree::TerminalNode *> AriaMRParser::A_rowContext::Float() {
  return getTokens(AriaMRParser::Float);
}

tree::TerminalNode* AriaMRParser::A_rowContext::Float(size_t i) {
  return getToken(AriaMRParser::Float, i);
}

std::vector<tree::TerminalNode *> AriaMRParser::A_rowContext::Real() {
  return getTokens(AriaMRParser::Real);
}

tree::TerminalNode* AriaMRParser::A_rowContext::Real(size_t i) {
  return getToken(AriaMRParser::Real, i);
}


size_t AriaMRParser::A_rowContext::getRuleIndex() const {
  return AriaMRParser::RuleA_row;
}


std::any AriaMRParser::A_rowContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitA_row(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::A_rowContext* AriaMRParser::a_row() {
  A_rowContext *_localctx = _tracker.createInstance<A_rowContext>(_ctx, getState());
  enterRule(_localctx, 18, AriaMRParser::RuleA_row);

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
    match(AriaMRParser::A_code);
    setState(115);
    match(AriaMRParser::Integer);
    setState(116);
    match(AriaMRParser::Float);
    setState(117);
    match(AriaMRParser::Float);
    setState(118);
    match(AriaMRParser::Float);
    setState(119);
    match(AriaMRParser::Float);
    setState(120);
    match(AriaMRParser::Real);
    setState(121);
    match(AriaMRParser::Real);
    setState(122);
    match(AriaMRParser::Real);
    setState(123);
    match(AriaMRParser::Real);
    setState(124);
    match(AriaMRParser::Integer);
    setState(125);
    match(AriaMRParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- C_rowContext ------------------------------------------------------------------

AriaMRParser::C_rowContext::C_rowContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AriaMRParser::C_rowContext::C_code() {
  return getToken(AriaMRParser::C_code, 0);
}

std::vector<tree::TerminalNode *> AriaMRParser::C_rowContext::Float() {
  return getTokens(AriaMRParser::Float);
}

tree::TerminalNode* AriaMRParser::C_rowContext::Float(size_t i) {
  return getToken(AriaMRParser::Float, i);
}

std::vector<tree::TerminalNode *> AriaMRParser::C_rowContext::Hyphen() {
  return getTokens(AriaMRParser::Hyphen);
}

tree::TerminalNode* AriaMRParser::C_rowContext::Hyphen(size_t i) {
  return getToken(AriaMRParser::Hyphen, i);
}

std::vector<tree::TerminalNode *> AriaMRParser::C_rowContext::Integer() {
  return getTokens(AriaMRParser::Integer);
}

tree::TerminalNode* AriaMRParser::C_rowContext::Integer(size_t i) {
  return getToken(AriaMRParser::Integer, i);
}

std::vector<tree::TerminalNode *> AriaMRParser::C_rowContext::Simple_name() {
  return getTokens(AriaMRParser::Simple_name);
}

tree::TerminalNode* AriaMRParser::C_rowContext::Simple_name(size_t i) {
  return getToken(AriaMRParser::Simple_name, i);
}


size_t AriaMRParser::C_rowContext::getRuleIndex() const {
  return AriaMRParser::RuleC_row;
}


std::any AriaMRParser::C_rowContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitC_row(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::C_rowContext* AriaMRParser::c_row() {
  C_rowContext *_localctx = _tracker.createInstance<C_rowContext>(_ctx, getState());
  enterRule(_localctx, 20, AriaMRParser::RuleC_row);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(127);
    match(AriaMRParser::C_code);
    setState(128);
    match(AriaMRParser::Float);
    setState(129);
    match(AriaMRParser::Float);
    setState(130);
    match(AriaMRParser::Float);
    setState(131);
    match(AriaMRParser::Float);
    setState(132);
    match(AriaMRParser::Float);
    setState(133);
    match(AriaMRParser::Float);
    setState(134);
    match(AriaMRParser::Hyphen);
    setState(135);
    match(AriaMRParser::Integer);
    setState(136);
    match(AriaMRParser::Simple_name);
    setState(137);
    match(AriaMRParser::Simple_name);
    setState(138);
    match(AriaMRParser::Float);
    setState(139);
    match(AriaMRParser::Float);
    setState(140);
    match(AriaMRParser::Simple_name);
    setState(141);
    match(AriaMRParser::Float);
    setState(142);
    match(AriaMRParser::Float);
    setState(143);
    match(AriaMRParser::Hyphen);
    setState(144);
    match(AriaMRParser::Integer);
    setState(145);
    match(AriaMRParser::Simple_name);
    setState(146);
    match(AriaMRParser::Simple_name);
    setState(147);
    match(AriaMRParser::Float);
    setState(148);
    match(AriaMRParser::Float);
    setState(149);
    match(AriaMRParser::Simple_name);
    setState(150);
    match(AriaMRParser::Float);
    setState(151);
    match(AriaMRParser::Float);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberContext ------------------------------------------------------------------

AriaMRParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AriaMRParser::NumberContext::Float() {
  return getToken(AriaMRParser::Float, 0);
}

tree::TerminalNode* AriaMRParser::NumberContext::Integer() {
  return getToken(AriaMRParser::Integer, 0);
}


size_t AriaMRParser::NumberContext::getRuleIndex() const {
  return AriaMRParser::RuleNumber;
}


std::any AriaMRParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::NumberContext* AriaMRParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 22, AriaMRParser::RuleNumber);
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
    setState(153);
    _la = _input->LA(1);
    if (!(_la == AriaMRParser::Integer

    || _la == AriaMRParser::Float)) {
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

//----------------- Number_cContext ------------------------------------------------------------------

AriaMRParser::Number_cContext::Number_cContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* AriaMRParser::Number_cContext::Float() {
  return getToken(AriaMRParser::Float, 0);
}

tree::TerminalNode* AriaMRParser::Number_cContext::Integer() {
  return getToken(AriaMRParser::Integer, 0);
}


size_t AriaMRParser::Number_cContext::getRuleIndex() const {
  return AriaMRParser::RuleNumber_c;
}


std::any AriaMRParser::Number_cContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<AriaMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber_c(this);
  else
    return visitor->visitChildren(this);
}

AriaMRParser::Number_cContext* AriaMRParser::number_c() {
  Number_cContext *_localctx = _tracker.createInstance<Number_cContext>(_ctx, getState());
  enterRule(_localctx, 24, AriaMRParser::RuleNumber_c);
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
    setState(155);
    _la = _input->LA(1);
    if (!(_la == AriaMRParser::Integer

    || _la == AriaMRParser::Float)) {
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

void AriaMRParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  ariamrparserParserInitialize();
#else
  ::antlr4::internal::call_once(ariamrparserParserOnceFlag, ariamrparserParserInitialize);
#endif
}
