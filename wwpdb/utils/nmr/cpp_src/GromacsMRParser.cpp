
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GromacsMRParser.g4 by ANTLR 4.13.0


#include "GromacsMRParserVisitor.h"

#include "GromacsMRParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct GromacsMRParserStaticData final {
  GromacsMRParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  GromacsMRParserStaticData(const GromacsMRParserStaticData&) = delete;
  GromacsMRParserStaticData(GromacsMRParserStaticData&&) = delete;
  GromacsMRParserStaticData& operator=(const GromacsMRParserStaticData&) = delete;
  GromacsMRParserStaticData& operator=(GromacsMRParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag gromacsmrparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
GromacsMRParserStaticData *gromacsmrparserParserStaticData = nullptr;

void gromacsmrparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (gromacsmrparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(gromacsmrparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<GromacsMRParserStaticData>(
    std::vector<std::string>{
      "gromacs_mr", "distance_restraints", "distance_restraint", "dihedral_restraints", 
      "dihedral_restraint", "orientation_restraints", "orientation_restraint", 
      "angle_restraints", "angle_restraint", "angle_restraints_z", "angle_restraint_z", 
      "position_restraints", "position_restraint", "number"
    },
    std::vector<std::string>{
      "", "'['", "']'", "'distance_restraints'", "'dihedral_restraints'", 
      "'orientation_restraints'", "'angle_restraints'", "'angle_restraints_z'", 
      "'position_restraints'"
    },
    std::vector<std::string>{
      "", "L_brkt", "R_brkt", "Distance_restraints", "Dihedral_restraints", 
      "Orientation_restraints", "Angle_restraints", "Angle_restraints_z", 
      "Position_restraints", "Intermolecular_interactions", "Integer", "Float", 
      "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", "Simple_name", 
      "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,19,158,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,1,0,1,0,
  	1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,38,8,0,10,0,12,0,41,9,0,1,0,1,0,1,1,1,
  	1,1,1,1,1,4,1,49,8,1,11,1,12,1,50,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
  	1,2,3,2,63,8,2,1,3,1,3,1,3,1,3,4,3,69,8,3,11,3,12,3,70,1,4,1,4,1,4,1,
  	4,1,4,1,4,1,4,1,4,1,4,3,4,82,8,4,1,5,1,5,1,5,1,5,4,5,88,8,5,11,5,12,5,
  	89,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,102,8,6,1,7,1,7,1,7,1,
  	7,4,7,108,8,7,11,7,12,7,109,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,121,
  	8,8,1,9,1,9,1,9,1,9,4,9,127,8,9,11,9,12,9,128,1,10,1,10,1,10,1,10,1,10,
  	1,10,1,10,3,10,138,8,10,1,11,1,11,1,11,1,11,4,11,144,8,11,11,11,12,11,
  	145,1,12,1,12,1,12,1,12,1,12,1,12,3,12,154,8,12,1,13,1,13,1,13,0,0,14,
  	0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,1,1,0,10,11,162,0,39,1,0,0,0,2,
  	44,1,0,0,0,4,52,1,0,0,0,6,64,1,0,0,0,8,72,1,0,0,0,10,83,1,0,0,0,12,91,
  	1,0,0,0,14,103,1,0,0,0,16,111,1,0,0,0,18,122,1,0,0,0,20,130,1,0,0,0,22,
  	139,1,0,0,0,24,147,1,0,0,0,26,155,1,0,0,0,28,38,3,2,1,0,29,38,3,6,3,0,
  	30,38,3,10,5,0,31,38,3,14,7,0,32,38,3,18,9,0,33,38,3,22,11,0,34,35,5,
  	1,0,0,35,36,5,9,0,0,36,38,5,2,0,0,37,28,1,0,0,0,37,29,1,0,0,0,37,30,1,
  	0,0,0,37,31,1,0,0,0,37,32,1,0,0,0,37,33,1,0,0,0,37,34,1,0,0,0,38,41,1,
  	0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,42,43,5,
  	0,0,1,43,1,1,0,0,0,44,45,5,1,0,0,45,46,5,3,0,0,46,48,5,2,0,0,47,49,3,
  	4,2,0,48,47,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,3,1,
  	0,0,0,52,53,5,10,0,0,53,54,5,10,0,0,54,55,5,10,0,0,55,56,5,10,0,0,56,
  	57,5,10,0,0,57,58,3,26,13,0,58,59,3,26,13,0,59,60,3,26,13,0,60,62,3,26,
  	13,0,61,63,5,15,0,0,62,61,1,0,0,0,62,63,1,0,0,0,63,5,1,0,0,0,64,65,5,
  	1,0,0,65,66,5,4,0,0,66,68,5,2,0,0,67,69,3,8,4,0,68,67,1,0,0,0,69,70,1,
  	0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,7,1,0,0,0,72,73,5,10,0,0,73,74,5,
  	10,0,0,74,75,5,10,0,0,75,76,5,10,0,0,76,77,5,10,0,0,77,78,3,26,13,0,78,
  	79,3,26,13,0,79,81,3,26,13,0,80,82,5,15,0,0,81,80,1,0,0,0,81,82,1,0,0,
  	0,82,9,1,0,0,0,83,84,5,1,0,0,84,85,5,5,0,0,85,87,5,2,0,0,86,88,3,12,6,
  	0,87,86,1,0,0,0,88,89,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,11,1,0,0,
  	0,91,92,5,10,0,0,92,93,5,10,0,0,93,94,5,10,0,0,94,95,5,10,0,0,95,96,5,
  	10,0,0,96,97,3,26,13,0,97,98,3,26,13,0,98,99,3,26,13,0,99,101,3,26,13,
  	0,100,102,5,15,0,0,101,100,1,0,0,0,101,102,1,0,0,0,102,13,1,0,0,0,103,
  	104,5,1,0,0,104,105,5,6,0,0,105,107,5,2,0,0,106,108,3,16,8,0,107,106,
  	1,0,0,0,108,109,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,15,1,0,0,
  	0,111,112,5,10,0,0,112,113,5,10,0,0,113,114,5,10,0,0,114,115,5,10,0,0,
  	115,116,5,10,0,0,116,117,3,26,13,0,117,118,3,26,13,0,118,120,5,10,0,0,
  	119,121,5,15,0,0,120,119,1,0,0,0,120,121,1,0,0,0,121,17,1,0,0,0,122,123,
  	5,1,0,0,123,124,5,7,0,0,124,126,5,2,0,0,125,127,3,20,10,0,126,125,1,0,
  	0,0,127,128,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,19,1,0,0,0,130,
  	131,5,10,0,0,131,132,5,10,0,0,132,133,5,10,0,0,133,134,3,26,13,0,134,
  	135,3,26,13,0,135,137,5,10,0,0,136,138,5,15,0,0,137,136,1,0,0,0,137,138,
  	1,0,0,0,138,21,1,0,0,0,139,140,5,1,0,0,140,141,5,8,0,0,141,143,5,2,0,
  	0,142,144,3,24,12,0,143,142,1,0,0,0,144,145,1,0,0,0,145,143,1,0,0,0,145,
  	146,1,0,0,0,146,23,1,0,0,0,147,148,5,10,0,0,148,149,5,10,0,0,149,150,
  	3,26,13,0,150,151,3,26,13,0,151,153,3,26,13,0,152,154,5,15,0,0,153,152,
  	1,0,0,0,153,154,1,0,0,0,154,25,1,0,0,0,155,156,7,0,0,0,156,27,1,0,0,0,
  	14,37,39,50,62,70,81,89,101,109,120,128,137,145,153
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  gromacsmrparserParserStaticData = staticData.release();
}

}

GromacsMRParser::GromacsMRParser(TokenStream *input) : GromacsMRParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

GromacsMRParser::GromacsMRParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  GromacsMRParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *gromacsmrparserParserStaticData->atn, gromacsmrparserParserStaticData->decisionToDFA, gromacsmrparserParserStaticData->sharedContextCache, options);
}

GromacsMRParser::~GromacsMRParser() {
  delete _interpreter;
}

const atn::ATN& GromacsMRParser::getATN() const {
  return *gromacsmrparserParserStaticData->atn;
}

std::string GromacsMRParser::getGrammarFileName() const {
  return "GromacsMRParser.g4";
}

const std::vector<std::string>& GromacsMRParser::getRuleNames() const {
  return gromacsmrparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& GromacsMRParser::getVocabulary() const {
  return gromacsmrparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView GromacsMRParser::getSerializedATN() const {
  return gromacsmrparserParserStaticData->serializedATN;
}


//----------------- Gromacs_mrContext ------------------------------------------------------------------

GromacsMRParser::Gromacs_mrContext::Gromacs_mrContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsMRParser::Gromacs_mrContext::EOF() {
  return getToken(GromacsMRParser::EOF, 0);
}

std::vector<GromacsMRParser::Distance_restraintsContext *> GromacsMRParser::Gromacs_mrContext::distance_restraints() {
  return getRuleContexts<GromacsMRParser::Distance_restraintsContext>();
}

GromacsMRParser::Distance_restraintsContext* GromacsMRParser::Gromacs_mrContext::distance_restraints(size_t i) {
  return getRuleContext<GromacsMRParser::Distance_restraintsContext>(i);
}

std::vector<GromacsMRParser::Dihedral_restraintsContext *> GromacsMRParser::Gromacs_mrContext::dihedral_restraints() {
  return getRuleContexts<GromacsMRParser::Dihedral_restraintsContext>();
}

GromacsMRParser::Dihedral_restraintsContext* GromacsMRParser::Gromacs_mrContext::dihedral_restraints(size_t i) {
  return getRuleContext<GromacsMRParser::Dihedral_restraintsContext>(i);
}

std::vector<GromacsMRParser::Orientation_restraintsContext *> GromacsMRParser::Gromacs_mrContext::orientation_restraints() {
  return getRuleContexts<GromacsMRParser::Orientation_restraintsContext>();
}

GromacsMRParser::Orientation_restraintsContext* GromacsMRParser::Gromacs_mrContext::orientation_restraints(size_t i) {
  return getRuleContext<GromacsMRParser::Orientation_restraintsContext>(i);
}

std::vector<GromacsMRParser::Angle_restraintsContext *> GromacsMRParser::Gromacs_mrContext::angle_restraints() {
  return getRuleContexts<GromacsMRParser::Angle_restraintsContext>();
}

GromacsMRParser::Angle_restraintsContext* GromacsMRParser::Gromacs_mrContext::angle_restraints(size_t i) {
  return getRuleContext<GromacsMRParser::Angle_restraintsContext>(i);
}

std::vector<GromacsMRParser::Angle_restraints_zContext *> GromacsMRParser::Gromacs_mrContext::angle_restraints_z() {
  return getRuleContexts<GromacsMRParser::Angle_restraints_zContext>();
}

GromacsMRParser::Angle_restraints_zContext* GromacsMRParser::Gromacs_mrContext::angle_restraints_z(size_t i) {
  return getRuleContext<GromacsMRParser::Angle_restraints_zContext>(i);
}

std::vector<GromacsMRParser::Position_restraintsContext *> GromacsMRParser::Gromacs_mrContext::position_restraints() {
  return getRuleContexts<GromacsMRParser::Position_restraintsContext>();
}

GromacsMRParser::Position_restraintsContext* GromacsMRParser::Gromacs_mrContext::position_restraints(size_t i) {
  return getRuleContext<GromacsMRParser::Position_restraintsContext>(i);
}

std::vector<tree::TerminalNode *> GromacsMRParser::Gromacs_mrContext::L_brkt() {
  return getTokens(GromacsMRParser::L_brkt);
}

tree::TerminalNode* GromacsMRParser::Gromacs_mrContext::L_brkt(size_t i) {
  return getToken(GromacsMRParser::L_brkt, i);
}

std::vector<tree::TerminalNode *> GromacsMRParser::Gromacs_mrContext::Intermolecular_interactions() {
  return getTokens(GromacsMRParser::Intermolecular_interactions);
}

tree::TerminalNode* GromacsMRParser::Gromacs_mrContext::Intermolecular_interactions(size_t i) {
  return getToken(GromacsMRParser::Intermolecular_interactions, i);
}

std::vector<tree::TerminalNode *> GromacsMRParser::Gromacs_mrContext::R_brkt() {
  return getTokens(GromacsMRParser::R_brkt);
}

tree::TerminalNode* GromacsMRParser::Gromacs_mrContext::R_brkt(size_t i) {
  return getToken(GromacsMRParser::R_brkt, i);
}


size_t GromacsMRParser::Gromacs_mrContext::getRuleIndex() const {
  return GromacsMRParser::RuleGromacs_mr;
}


std::any GromacsMRParser::Gromacs_mrContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitGromacs_mr(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Gromacs_mrContext* GromacsMRParser::gromacs_mr() {
  Gromacs_mrContext *_localctx = _tracker.createInstance<Gromacs_mrContext>(_ctx, getState());
  enterRule(_localctx, 0, GromacsMRParser::RuleGromacs_mr);
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
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsMRParser::L_brkt) {
      setState(37);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
      case 1: {
        setState(28);
        distance_restraints();
        break;
      }

      case 2: {
        setState(29);
        dihedral_restraints();
        break;
      }

      case 3: {
        setState(30);
        orientation_restraints();
        break;
      }

      case 4: {
        setState(31);
        angle_restraints();
        break;
      }

      case 5: {
        setState(32);
        angle_restraints_z();
        break;
      }

      case 6: {
        setState(33);
        position_restraints();
        break;
      }

      case 7: {
        setState(34);
        match(GromacsMRParser::L_brkt);
        setState(35);
        match(GromacsMRParser::Intermolecular_interactions);
        setState(36);
        match(GromacsMRParser::R_brkt);
        break;
      }

      default:
        break;
      }
      setState(41);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(42);
    match(GromacsMRParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_restraintsContext ------------------------------------------------------------------

GromacsMRParser::Distance_restraintsContext::Distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsMRParser::Distance_restraintsContext::L_brkt() {
  return getToken(GromacsMRParser::L_brkt, 0);
}

tree::TerminalNode* GromacsMRParser::Distance_restraintsContext::Distance_restraints() {
  return getToken(GromacsMRParser::Distance_restraints, 0);
}

tree::TerminalNode* GromacsMRParser::Distance_restraintsContext::R_brkt() {
  return getToken(GromacsMRParser::R_brkt, 0);
}

std::vector<GromacsMRParser::Distance_restraintContext *> GromacsMRParser::Distance_restraintsContext::distance_restraint() {
  return getRuleContexts<GromacsMRParser::Distance_restraintContext>();
}

GromacsMRParser::Distance_restraintContext* GromacsMRParser::Distance_restraintsContext::distance_restraint(size_t i) {
  return getRuleContext<GromacsMRParser::Distance_restraintContext>(i);
}


size_t GromacsMRParser::Distance_restraintsContext::getRuleIndex() const {
  return GromacsMRParser::RuleDistance_restraints;
}


std::any GromacsMRParser::Distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraints(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Distance_restraintsContext* GromacsMRParser::distance_restraints() {
  Distance_restraintsContext *_localctx = _tracker.createInstance<Distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 2, GromacsMRParser::RuleDistance_restraints);
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
    match(GromacsMRParser::L_brkt);
    setState(45);
    match(GromacsMRParser::Distance_restraints);
    setState(46);
    match(GromacsMRParser::R_brkt);
    setState(48); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(47);
      distance_restraint();
      setState(50); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GromacsMRParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_restraintContext ------------------------------------------------------------------

GromacsMRParser::Distance_restraintContext::Distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsMRParser::Distance_restraintContext::Integer() {
  return getTokens(GromacsMRParser::Integer);
}

tree::TerminalNode* GromacsMRParser::Distance_restraintContext::Integer(size_t i) {
  return getToken(GromacsMRParser::Integer, i);
}

std::vector<GromacsMRParser::NumberContext *> GromacsMRParser::Distance_restraintContext::number() {
  return getRuleContexts<GromacsMRParser::NumberContext>();
}

GromacsMRParser::NumberContext* GromacsMRParser::Distance_restraintContext::number(size_t i) {
  return getRuleContext<GromacsMRParser::NumberContext>(i);
}

tree::TerminalNode* GromacsMRParser::Distance_restraintContext::Simple_name() {
  return getToken(GromacsMRParser::Simple_name, 0);
}


size_t GromacsMRParser::Distance_restraintContext::getRuleIndex() const {
  return GromacsMRParser::RuleDistance_restraint;
}


std::any GromacsMRParser::Distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraint(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Distance_restraintContext* GromacsMRParser::distance_restraint() {
  Distance_restraintContext *_localctx = _tracker.createInstance<Distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 4, GromacsMRParser::RuleDistance_restraint);
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
    setState(52);
    match(GromacsMRParser::Integer);
    setState(53);
    match(GromacsMRParser::Integer);
    setState(54);
    match(GromacsMRParser::Integer);
    setState(55);
    match(GromacsMRParser::Integer);
    setState(56);
    match(GromacsMRParser::Integer);
    setState(57);
    number();
    setState(58);
    number();
    setState(59);
    number();
    setState(60);
    number();
    setState(62);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsMRParser::Simple_name) {
      setState(61);
      match(GromacsMRParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_restraintsContext ------------------------------------------------------------------

GromacsMRParser::Dihedral_restraintsContext::Dihedral_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsMRParser::Dihedral_restraintsContext::L_brkt() {
  return getToken(GromacsMRParser::L_brkt, 0);
}

tree::TerminalNode* GromacsMRParser::Dihedral_restraintsContext::Dihedral_restraints() {
  return getToken(GromacsMRParser::Dihedral_restraints, 0);
}

tree::TerminalNode* GromacsMRParser::Dihedral_restraintsContext::R_brkt() {
  return getToken(GromacsMRParser::R_brkt, 0);
}

std::vector<GromacsMRParser::Dihedral_restraintContext *> GromacsMRParser::Dihedral_restraintsContext::dihedral_restraint() {
  return getRuleContexts<GromacsMRParser::Dihedral_restraintContext>();
}

GromacsMRParser::Dihedral_restraintContext* GromacsMRParser::Dihedral_restraintsContext::dihedral_restraint(size_t i) {
  return getRuleContext<GromacsMRParser::Dihedral_restraintContext>(i);
}


size_t GromacsMRParser::Dihedral_restraintsContext::getRuleIndex() const {
  return GromacsMRParser::RuleDihedral_restraints;
}


std::any GromacsMRParser::Dihedral_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_restraints(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Dihedral_restraintsContext* GromacsMRParser::dihedral_restraints() {
  Dihedral_restraintsContext *_localctx = _tracker.createInstance<Dihedral_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 6, GromacsMRParser::RuleDihedral_restraints);
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
    setState(64);
    match(GromacsMRParser::L_brkt);
    setState(65);
    match(GromacsMRParser::Dihedral_restraints);
    setState(66);
    match(GromacsMRParser::R_brkt);
    setState(68); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(67);
      dihedral_restraint();
      setState(70); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GromacsMRParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_restraintContext ------------------------------------------------------------------

GromacsMRParser::Dihedral_restraintContext::Dihedral_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsMRParser::Dihedral_restraintContext::Integer() {
  return getTokens(GromacsMRParser::Integer);
}

tree::TerminalNode* GromacsMRParser::Dihedral_restraintContext::Integer(size_t i) {
  return getToken(GromacsMRParser::Integer, i);
}

std::vector<GromacsMRParser::NumberContext *> GromacsMRParser::Dihedral_restraintContext::number() {
  return getRuleContexts<GromacsMRParser::NumberContext>();
}

GromacsMRParser::NumberContext* GromacsMRParser::Dihedral_restraintContext::number(size_t i) {
  return getRuleContext<GromacsMRParser::NumberContext>(i);
}

tree::TerminalNode* GromacsMRParser::Dihedral_restraintContext::Simple_name() {
  return getToken(GromacsMRParser::Simple_name, 0);
}


size_t GromacsMRParser::Dihedral_restraintContext::getRuleIndex() const {
  return GromacsMRParser::RuleDihedral_restraint;
}


std::any GromacsMRParser::Dihedral_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_restraint(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Dihedral_restraintContext* GromacsMRParser::dihedral_restraint() {
  Dihedral_restraintContext *_localctx = _tracker.createInstance<Dihedral_restraintContext>(_ctx, getState());
  enterRule(_localctx, 8, GromacsMRParser::RuleDihedral_restraint);
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
    setState(72);
    match(GromacsMRParser::Integer);
    setState(73);
    match(GromacsMRParser::Integer);
    setState(74);
    match(GromacsMRParser::Integer);
    setState(75);
    match(GromacsMRParser::Integer);
    setState(76);
    match(GromacsMRParser::Integer);
    setState(77);
    number();
    setState(78);
    number();
    setState(79);
    number();
    setState(81);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsMRParser::Simple_name) {
      setState(80);
      match(GromacsMRParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Orientation_restraintsContext ------------------------------------------------------------------

GromacsMRParser::Orientation_restraintsContext::Orientation_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsMRParser::Orientation_restraintsContext::L_brkt() {
  return getToken(GromacsMRParser::L_brkt, 0);
}

tree::TerminalNode* GromacsMRParser::Orientation_restraintsContext::Orientation_restraints() {
  return getToken(GromacsMRParser::Orientation_restraints, 0);
}

tree::TerminalNode* GromacsMRParser::Orientation_restraintsContext::R_brkt() {
  return getToken(GromacsMRParser::R_brkt, 0);
}

std::vector<GromacsMRParser::Orientation_restraintContext *> GromacsMRParser::Orientation_restraintsContext::orientation_restraint() {
  return getRuleContexts<GromacsMRParser::Orientation_restraintContext>();
}

GromacsMRParser::Orientation_restraintContext* GromacsMRParser::Orientation_restraintsContext::orientation_restraint(size_t i) {
  return getRuleContext<GromacsMRParser::Orientation_restraintContext>(i);
}


size_t GromacsMRParser::Orientation_restraintsContext::getRuleIndex() const {
  return GromacsMRParser::RuleOrientation_restraints;
}


std::any GromacsMRParser::Orientation_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitOrientation_restraints(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Orientation_restraintsContext* GromacsMRParser::orientation_restraints() {
  Orientation_restraintsContext *_localctx = _tracker.createInstance<Orientation_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 10, GromacsMRParser::RuleOrientation_restraints);
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
    setState(83);
    match(GromacsMRParser::L_brkt);
    setState(84);
    match(GromacsMRParser::Orientation_restraints);
    setState(85);
    match(GromacsMRParser::R_brkt);
    setState(87); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(86);
      orientation_restraint();
      setState(89); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GromacsMRParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Orientation_restraintContext ------------------------------------------------------------------

GromacsMRParser::Orientation_restraintContext::Orientation_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsMRParser::Orientation_restraintContext::Integer() {
  return getTokens(GromacsMRParser::Integer);
}

tree::TerminalNode* GromacsMRParser::Orientation_restraintContext::Integer(size_t i) {
  return getToken(GromacsMRParser::Integer, i);
}

std::vector<GromacsMRParser::NumberContext *> GromacsMRParser::Orientation_restraintContext::number() {
  return getRuleContexts<GromacsMRParser::NumberContext>();
}

GromacsMRParser::NumberContext* GromacsMRParser::Orientation_restraintContext::number(size_t i) {
  return getRuleContext<GromacsMRParser::NumberContext>(i);
}

tree::TerminalNode* GromacsMRParser::Orientation_restraintContext::Simple_name() {
  return getToken(GromacsMRParser::Simple_name, 0);
}


size_t GromacsMRParser::Orientation_restraintContext::getRuleIndex() const {
  return GromacsMRParser::RuleOrientation_restraint;
}


std::any GromacsMRParser::Orientation_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitOrientation_restraint(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Orientation_restraintContext* GromacsMRParser::orientation_restraint() {
  Orientation_restraintContext *_localctx = _tracker.createInstance<Orientation_restraintContext>(_ctx, getState());
  enterRule(_localctx, 12, GromacsMRParser::RuleOrientation_restraint);
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
    match(GromacsMRParser::Integer);
    setState(92);
    match(GromacsMRParser::Integer);
    setState(93);
    match(GromacsMRParser::Integer);
    setState(94);
    match(GromacsMRParser::Integer);
    setState(95);
    match(GromacsMRParser::Integer);
    setState(96);
    number();
    setState(97);
    number();
    setState(98);
    number();
    setState(99);
    number();
    setState(101);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsMRParser::Simple_name) {
      setState(100);
      match(GromacsMRParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Angle_restraintsContext ------------------------------------------------------------------

GromacsMRParser::Angle_restraintsContext::Angle_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsMRParser::Angle_restraintsContext::L_brkt() {
  return getToken(GromacsMRParser::L_brkt, 0);
}

tree::TerminalNode* GromacsMRParser::Angle_restraintsContext::Angle_restraints() {
  return getToken(GromacsMRParser::Angle_restraints, 0);
}

tree::TerminalNode* GromacsMRParser::Angle_restraintsContext::R_brkt() {
  return getToken(GromacsMRParser::R_brkt, 0);
}

std::vector<GromacsMRParser::Angle_restraintContext *> GromacsMRParser::Angle_restraintsContext::angle_restraint() {
  return getRuleContexts<GromacsMRParser::Angle_restraintContext>();
}

GromacsMRParser::Angle_restraintContext* GromacsMRParser::Angle_restraintsContext::angle_restraint(size_t i) {
  return getRuleContext<GromacsMRParser::Angle_restraintContext>(i);
}


size_t GromacsMRParser::Angle_restraintsContext::getRuleIndex() const {
  return GromacsMRParser::RuleAngle_restraints;
}


std::any GromacsMRParser::Angle_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitAngle_restraints(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Angle_restraintsContext* GromacsMRParser::angle_restraints() {
  Angle_restraintsContext *_localctx = _tracker.createInstance<Angle_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 14, GromacsMRParser::RuleAngle_restraints);
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
    match(GromacsMRParser::L_brkt);
    setState(104);
    match(GromacsMRParser::Angle_restraints);
    setState(105);
    match(GromacsMRParser::R_brkt);
    setState(107); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(106);
      angle_restraint();
      setState(109); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GromacsMRParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Angle_restraintContext ------------------------------------------------------------------

GromacsMRParser::Angle_restraintContext::Angle_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsMRParser::Angle_restraintContext::Integer() {
  return getTokens(GromacsMRParser::Integer);
}

tree::TerminalNode* GromacsMRParser::Angle_restraintContext::Integer(size_t i) {
  return getToken(GromacsMRParser::Integer, i);
}

std::vector<GromacsMRParser::NumberContext *> GromacsMRParser::Angle_restraintContext::number() {
  return getRuleContexts<GromacsMRParser::NumberContext>();
}

GromacsMRParser::NumberContext* GromacsMRParser::Angle_restraintContext::number(size_t i) {
  return getRuleContext<GromacsMRParser::NumberContext>(i);
}

tree::TerminalNode* GromacsMRParser::Angle_restraintContext::Simple_name() {
  return getToken(GromacsMRParser::Simple_name, 0);
}


size_t GromacsMRParser::Angle_restraintContext::getRuleIndex() const {
  return GromacsMRParser::RuleAngle_restraint;
}


std::any GromacsMRParser::Angle_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitAngle_restraint(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Angle_restraintContext* GromacsMRParser::angle_restraint() {
  Angle_restraintContext *_localctx = _tracker.createInstance<Angle_restraintContext>(_ctx, getState());
  enterRule(_localctx, 16, GromacsMRParser::RuleAngle_restraint);
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
    match(GromacsMRParser::Integer);
    setState(112);
    match(GromacsMRParser::Integer);
    setState(113);
    match(GromacsMRParser::Integer);
    setState(114);
    match(GromacsMRParser::Integer);
    setState(115);
    match(GromacsMRParser::Integer);
    setState(116);
    number();
    setState(117);
    number();
    setState(118);
    match(GromacsMRParser::Integer);
    setState(120);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsMRParser::Simple_name) {
      setState(119);
      match(GromacsMRParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Angle_restraints_zContext ------------------------------------------------------------------

GromacsMRParser::Angle_restraints_zContext::Angle_restraints_zContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsMRParser::Angle_restraints_zContext::L_brkt() {
  return getToken(GromacsMRParser::L_brkt, 0);
}

tree::TerminalNode* GromacsMRParser::Angle_restraints_zContext::Angle_restraints_z() {
  return getToken(GromacsMRParser::Angle_restraints_z, 0);
}

tree::TerminalNode* GromacsMRParser::Angle_restraints_zContext::R_brkt() {
  return getToken(GromacsMRParser::R_brkt, 0);
}

std::vector<GromacsMRParser::Angle_restraint_zContext *> GromacsMRParser::Angle_restraints_zContext::angle_restraint_z() {
  return getRuleContexts<GromacsMRParser::Angle_restraint_zContext>();
}

GromacsMRParser::Angle_restraint_zContext* GromacsMRParser::Angle_restraints_zContext::angle_restraint_z(size_t i) {
  return getRuleContext<GromacsMRParser::Angle_restraint_zContext>(i);
}


size_t GromacsMRParser::Angle_restraints_zContext::getRuleIndex() const {
  return GromacsMRParser::RuleAngle_restraints_z;
}


std::any GromacsMRParser::Angle_restraints_zContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitAngle_restraints_z(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Angle_restraints_zContext* GromacsMRParser::angle_restraints_z() {
  Angle_restraints_zContext *_localctx = _tracker.createInstance<Angle_restraints_zContext>(_ctx, getState());
  enterRule(_localctx, 18, GromacsMRParser::RuleAngle_restraints_z);
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
    setState(122);
    match(GromacsMRParser::L_brkt);
    setState(123);
    match(GromacsMRParser::Angle_restraints_z);
    setState(124);
    match(GromacsMRParser::R_brkt);
    setState(126); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(125);
      angle_restraint_z();
      setState(128); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GromacsMRParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Angle_restraint_zContext ------------------------------------------------------------------

GromacsMRParser::Angle_restraint_zContext::Angle_restraint_zContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsMRParser::Angle_restraint_zContext::Integer() {
  return getTokens(GromacsMRParser::Integer);
}

tree::TerminalNode* GromacsMRParser::Angle_restraint_zContext::Integer(size_t i) {
  return getToken(GromacsMRParser::Integer, i);
}

std::vector<GromacsMRParser::NumberContext *> GromacsMRParser::Angle_restraint_zContext::number() {
  return getRuleContexts<GromacsMRParser::NumberContext>();
}

GromacsMRParser::NumberContext* GromacsMRParser::Angle_restraint_zContext::number(size_t i) {
  return getRuleContext<GromacsMRParser::NumberContext>(i);
}

tree::TerminalNode* GromacsMRParser::Angle_restraint_zContext::Simple_name() {
  return getToken(GromacsMRParser::Simple_name, 0);
}


size_t GromacsMRParser::Angle_restraint_zContext::getRuleIndex() const {
  return GromacsMRParser::RuleAngle_restraint_z;
}


std::any GromacsMRParser::Angle_restraint_zContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitAngle_restraint_z(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Angle_restraint_zContext* GromacsMRParser::angle_restraint_z() {
  Angle_restraint_zContext *_localctx = _tracker.createInstance<Angle_restraint_zContext>(_ctx, getState());
  enterRule(_localctx, 20, GromacsMRParser::RuleAngle_restraint_z);
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
    setState(130);
    match(GromacsMRParser::Integer);
    setState(131);
    match(GromacsMRParser::Integer);
    setState(132);
    match(GromacsMRParser::Integer);
    setState(133);
    number();
    setState(134);
    number();
    setState(135);
    match(GromacsMRParser::Integer);
    setState(137);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsMRParser::Simple_name) {
      setState(136);
      match(GromacsMRParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Position_restraintsContext ------------------------------------------------------------------

GromacsMRParser::Position_restraintsContext::Position_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsMRParser::Position_restraintsContext::L_brkt() {
  return getToken(GromacsMRParser::L_brkt, 0);
}

tree::TerminalNode* GromacsMRParser::Position_restraintsContext::Position_restraints() {
  return getToken(GromacsMRParser::Position_restraints, 0);
}

tree::TerminalNode* GromacsMRParser::Position_restraintsContext::R_brkt() {
  return getToken(GromacsMRParser::R_brkt, 0);
}

std::vector<GromacsMRParser::Position_restraintContext *> GromacsMRParser::Position_restraintsContext::position_restraint() {
  return getRuleContexts<GromacsMRParser::Position_restraintContext>();
}

GromacsMRParser::Position_restraintContext* GromacsMRParser::Position_restraintsContext::position_restraint(size_t i) {
  return getRuleContext<GromacsMRParser::Position_restraintContext>(i);
}


size_t GromacsMRParser::Position_restraintsContext::getRuleIndex() const {
  return GromacsMRParser::RulePosition_restraints;
}


std::any GromacsMRParser::Position_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitPosition_restraints(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Position_restraintsContext* GromacsMRParser::position_restraints() {
  Position_restraintsContext *_localctx = _tracker.createInstance<Position_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 22, GromacsMRParser::RulePosition_restraints);
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
    setState(139);
    match(GromacsMRParser::L_brkt);
    setState(140);
    match(GromacsMRParser::Position_restraints);
    setState(141);
    match(GromacsMRParser::R_brkt);
    setState(143); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(142);
      position_restraint();
      setState(145); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GromacsMRParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Position_restraintContext ------------------------------------------------------------------

GromacsMRParser::Position_restraintContext::Position_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsMRParser::Position_restraintContext::Integer() {
  return getTokens(GromacsMRParser::Integer);
}

tree::TerminalNode* GromacsMRParser::Position_restraintContext::Integer(size_t i) {
  return getToken(GromacsMRParser::Integer, i);
}

std::vector<GromacsMRParser::NumberContext *> GromacsMRParser::Position_restraintContext::number() {
  return getRuleContexts<GromacsMRParser::NumberContext>();
}

GromacsMRParser::NumberContext* GromacsMRParser::Position_restraintContext::number(size_t i) {
  return getRuleContext<GromacsMRParser::NumberContext>(i);
}

tree::TerminalNode* GromacsMRParser::Position_restraintContext::Simple_name() {
  return getToken(GromacsMRParser::Simple_name, 0);
}


size_t GromacsMRParser::Position_restraintContext::getRuleIndex() const {
  return GromacsMRParser::RulePosition_restraint;
}


std::any GromacsMRParser::Position_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitPosition_restraint(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::Position_restraintContext* GromacsMRParser::position_restraint() {
  Position_restraintContext *_localctx = _tracker.createInstance<Position_restraintContext>(_ctx, getState());
  enterRule(_localctx, 24, GromacsMRParser::RulePosition_restraint);
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
    setState(147);
    match(GromacsMRParser::Integer);
    setState(148);
    match(GromacsMRParser::Integer);
    setState(149);
    number();
    setState(150);
    number();
    setState(151);
    number();
    setState(153);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsMRParser::Simple_name) {
      setState(152);
      match(GromacsMRParser::Simple_name);
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

GromacsMRParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsMRParser::NumberContext::Float() {
  return getToken(GromacsMRParser::Float, 0);
}

tree::TerminalNode* GromacsMRParser::NumberContext::Integer() {
  return getToken(GromacsMRParser::Integer, 0);
}


size_t GromacsMRParser::NumberContext::getRuleIndex() const {
  return GromacsMRParser::RuleNumber;
}


std::any GromacsMRParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

GromacsMRParser::NumberContext* GromacsMRParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 26, GromacsMRParser::RuleNumber);
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
    if (!(_la == GromacsMRParser::Integer

    || _la == GromacsMRParser::Float)) {
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

void GromacsMRParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  gromacsmrparserParserInitialize();
#else
  ::antlr4::internal::call_once(gromacsmrparserParserOnceFlag, gromacsmrparserParserInitialize);
#endif
}
