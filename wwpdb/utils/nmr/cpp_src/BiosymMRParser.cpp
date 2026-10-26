
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BiosymMRParser.g4 by ANTLR 4.13.2


#include "BiosymMRParserVisitor.h"

#include "BiosymMRParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct BiosymMRParserStaticData final {
  BiosymMRParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  BiosymMRParserStaticData(const BiosymMRParserStaticData&) = delete;
  BiosymMRParserStaticData(BiosymMRParserStaticData&&) = delete;
  BiosymMRParserStaticData& operator=(const BiosymMRParserStaticData&) = delete;
  BiosymMRParserStaticData& operator=(BiosymMRParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag biosymmrparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<BiosymMRParserStaticData> biosymmrparserParserStaticData = nullptr;

void biosymmrparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (biosymmrparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(biosymmrparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<BiosymMRParserStaticData>(
    std::vector<std::string>{
      "biosym_mr", "distance_restraints", "distance_restraint", "distance_constraints", 
      "distance_constraint", "dihedral_angle_restraints", "dihedral_angle_restraint", 
      "dihedral_angle_constraints", "dihedral_angle_constraint", "chirality_constraints", 
      "chirality_constraint", "prochirality_constraints", "prochirality_constraint", 
      "mixing_time", "number", "ins_distance_restraints", "ins_distance_restraint", 
      "decl_create", "decl_function", "decl_target"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "", "", "", "'restraint'", "", "", 
      "", "", "", "'create'", "'function'", "'target'", "'distance'", "'quadratic'", 
      "'flatBottomed'", "'relative'"
    },
    std::vector<std::string>{
      "", "Integer", "Float", "Float_DecimalComma", "Real", "SHARP_COMMENT", 
      "EXCLM_COMMENT", "SMCLN_COMMENT", "Chiral_code", "Atom_selection", 
      "Ordinal", "Restraint", "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", 
      "LINE_COMMENT", "Double_quote_string", "Create", "Function", "Target", 
      "Distance", "Quadratic", "Flat_bottomed", "Relative", "SPACE_II", 
      "RETURN_II"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,25,208,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,1,0,1,0,1,0,
  	1,0,1,0,1,0,1,0,5,0,49,8,0,10,0,12,0,52,9,0,1,0,1,0,1,1,4,1,57,8,1,11,
  	1,12,1,58,1,2,3,2,62,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,73,8,
  	2,1,3,4,3,76,8,3,11,3,12,3,77,1,4,3,4,81,8,4,1,4,1,4,1,4,1,4,1,4,1,4,
  	1,4,1,4,3,4,91,8,4,1,5,4,5,94,8,5,11,5,12,5,95,1,6,3,6,99,8,6,1,6,1,6,
  	1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,115,8,6,1,6,1,6,1,
  	6,3,6,120,8,6,1,6,1,6,1,6,3,6,125,8,6,1,7,4,7,128,8,7,11,7,12,7,129,1,
  	8,3,8,133,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,145,8,8,1,9,
  	4,9,148,8,9,11,9,12,9,149,1,10,3,10,153,8,10,1,10,1,10,1,10,1,11,4,11,
  	159,8,11,11,11,12,11,160,1,12,3,12,164,8,12,1,12,1,12,1,12,1,12,1,12,
  	1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,
  	1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,197,
  	8,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,0,0,20,0,2,4,6,
  	8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,3,1,0,1,3,1,0,21,22,
  	2,0,16,16,23,23,214,0,50,1,0,0,0,2,56,1,0,0,0,4,61,1,0,0,0,6,75,1,0,0,
  	0,8,80,1,0,0,0,10,93,1,0,0,0,12,98,1,0,0,0,14,127,1,0,0,0,16,132,1,0,
  	0,0,18,147,1,0,0,0,20,152,1,0,0,0,22,158,1,0,0,0,24,163,1,0,0,0,26,171,
  	1,0,0,0,28,173,1,0,0,0,30,175,1,0,0,0,32,177,1,0,0,0,34,181,1,0,0,0,36,
  	189,1,0,0,0,38,200,1,0,0,0,40,49,3,2,1,0,41,49,3,6,3,0,42,49,3,10,5,0,
  	43,49,3,14,7,0,44,49,3,18,9,0,45,49,3,22,11,0,46,49,3,26,13,0,47,49,3,
  	30,15,0,48,40,1,0,0,0,48,41,1,0,0,0,48,42,1,0,0,0,48,43,1,0,0,0,48,44,
  	1,0,0,0,48,45,1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,
  	1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,54,5,0,0,1,54,1,
  	1,0,0,0,55,57,3,4,2,0,56,55,1,0,0,0,57,58,1,0,0,0,58,56,1,0,0,0,58,59,
  	1,0,0,0,59,3,1,0,0,0,60,62,5,10,0,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,
  	1,0,0,0,63,64,5,9,0,0,64,65,5,9,0,0,65,66,3,28,14,0,66,67,3,28,14,0,67,
  	68,3,28,14,0,68,69,3,28,14,0,69,70,3,28,14,0,70,72,3,28,14,0,71,73,3,
  	28,14,0,72,71,1,0,0,0,72,73,1,0,0,0,73,5,1,0,0,0,74,76,3,8,4,0,75,74,
  	1,0,0,0,76,77,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,7,1,0,0,0,79,81,
  	5,10,0,0,80,79,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,5,9,0,0,83,84,
  	5,9,0,0,84,85,3,28,14,0,85,90,3,28,14,0,86,87,3,28,14,0,87,88,3,28,14,
  	0,88,89,3,28,14,0,89,91,1,0,0,0,90,86,1,0,0,0,90,91,1,0,0,0,91,9,1,0,
  	0,0,92,94,3,12,6,0,93,92,1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,95,96,1,
  	0,0,0,96,11,1,0,0,0,97,99,5,10,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,
  	1,0,0,0,100,101,5,9,0,0,101,102,5,9,0,0,102,103,5,9,0,0,103,104,5,9,0,
  	0,104,105,3,28,14,0,105,106,3,28,14,0,106,107,3,28,14,0,107,108,3,28,
  	14,0,108,109,3,28,14,0,109,110,3,28,14,0,110,114,3,28,14,0,111,112,3,
  	28,14,0,112,113,3,28,14,0,113,115,1,0,0,0,114,111,1,0,0,0,114,115,1,0,
  	0,0,115,119,1,0,0,0,116,117,3,28,14,0,117,118,3,28,14,0,118,120,1,0,0,
  	0,119,116,1,0,0,0,119,120,1,0,0,0,120,124,1,0,0,0,121,122,3,28,14,0,122,
  	123,3,28,14,0,123,125,1,0,0,0,124,121,1,0,0,0,124,125,1,0,0,0,125,13,
  	1,0,0,0,126,128,3,16,8,0,127,126,1,0,0,0,128,129,1,0,0,0,129,127,1,0,
  	0,0,129,130,1,0,0,0,130,15,1,0,0,0,131,133,5,10,0,0,132,131,1,0,0,0,132,
  	133,1,0,0,0,133,134,1,0,0,0,134,135,5,9,0,0,135,136,5,9,0,0,136,137,5,
  	9,0,0,137,138,5,9,0,0,138,139,3,28,14,0,139,144,3,28,14,0,140,141,3,28,
  	14,0,141,142,3,28,14,0,142,143,3,28,14,0,143,145,1,0,0,0,144,140,1,0,
  	0,0,144,145,1,0,0,0,145,17,1,0,0,0,146,148,3,20,10,0,147,146,1,0,0,0,
  	148,149,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,19,1,0,0,0,151,153,
  	5,10,0,0,152,151,1,0,0,0,152,153,1,0,0,0,153,154,1,0,0,0,154,155,5,9,
  	0,0,155,156,5,8,0,0,156,21,1,0,0,0,157,159,3,24,12,0,158,157,1,0,0,0,
  	159,160,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,23,1,0,0,0,162,164,
  	5,10,0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,0,165,166,5,9,
  	0,0,166,167,5,9,0,0,167,168,5,9,0,0,168,169,5,9,0,0,169,170,5,9,0,0,170,
  	25,1,0,0,0,171,172,5,4,0,0,172,27,1,0,0,0,173,174,7,0,0,0,174,29,1,0,
  	0,0,175,176,3,32,16,0,176,31,1,0,0,0,177,178,3,34,17,0,178,179,3,36,18,
  	0,179,180,3,38,19,0,180,33,1,0,0,0,181,182,5,11,0,0,182,183,5,17,0,0,
  	183,184,5,16,0,0,184,185,5,20,0,0,185,186,5,16,0,0,186,187,5,16,0,0,187,
  	188,5,25,0,0,188,35,1,0,0,0,189,190,5,11,0,0,190,191,5,18,0,0,191,192,
  	5,16,0,0,192,193,7,1,0,0,193,194,5,16,0,0,194,196,5,16,0,0,195,197,5,
  	16,0,0,196,195,1,0,0,0,196,197,1,0,0,0,197,198,1,0,0,0,198,199,5,25,0,
  	0,199,37,1,0,0,0,200,201,5,11,0,0,201,202,5,19,0,0,202,203,5,16,0,0,203,
  	204,7,2,0,0,204,205,5,16,0,0,205,206,5,25,0,0,206,39,1,0,0,0,21,48,50,
  	58,61,72,77,80,90,95,98,114,119,124,129,132,144,149,152,160,163,196
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  biosymmrparserParserStaticData = std::move(staticData);
}

}

BiosymMRParser::BiosymMRParser(TokenStream *input) : BiosymMRParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

BiosymMRParser::BiosymMRParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  BiosymMRParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *biosymmrparserParserStaticData->atn, biosymmrparserParserStaticData->decisionToDFA, biosymmrparserParserStaticData->sharedContextCache, options);
}

BiosymMRParser::~BiosymMRParser() {
  delete _interpreter;
}

const atn::ATN& BiosymMRParser::getATN() const {
  return *biosymmrparserParserStaticData->atn;
}

std::string BiosymMRParser::getGrammarFileName() const {
  return "BiosymMRParser.g4";
}

const std::vector<std::string>& BiosymMRParser::getRuleNames() const {
  return biosymmrparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& BiosymMRParser::getVocabulary() const {
  return biosymmrparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView BiosymMRParser::getSerializedATN() const {
  return biosymmrparserParserStaticData->serializedATN;
}


//----------------- Biosym_mrContext ------------------------------------------------------------------

BiosymMRParser::Biosym_mrContext::Biosym_mrContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Biosym_mrContext::EOF() {
  return getToken(BiosymMRParser::EOF, 0);
}

std::vector<BiosymMRParser::Distance_restraintsContext *> BiosymMRParser::Biosym_mrContext::distance_restraints() {
  return getRuleContexts<BiosymMRParser::Distance_restraintsContext>();
}

BiosymMRParser::Distance_restraintsContext* BiosymMRParser::Biosym_mrContext::distance_restraints(size_t i) {
  return getRuleContext<BiosymMRParser::Distance_restraintsContext>(i);
}

std::vector<BiosymMRParser::Distance_constraintsContext *> BiosymMRParser::Biosym_mrContext::distance_constraints() {
  return getRuleContexts<BiosymMRParser::Distance_constraintsContext>();
}

BiosymMRParser::Distance_constraintsContext* BiosymMRParser::Biosym_mrContext::distance_constraints(size_t i) {
  return getRuleContext<BiosymMRParser::Distance_constraintsContext>(i);
}

std::vector<BiosymMRParser::Dihedral_angle_restraintsContext *> BiosymMRParser::Biosym_mrContext::dihedral_angle_restraints() {
  return getRuleContexts<BiosymMRParser::Dihedral_angle_restraintsContext>();
}

BiosymMRParser::Dihedral_angle_restraintsContext* BiosymMRParser::Biosym_mrContext::dihedral_angle_restraints(size_t i) {
  return getRuleContext<BiosymMRParser::Dihedral_angle_restraintsContext>(i);
}

std::vector<BiosymMRParser::Dihedral_angle_constraintsContext *> BiosymMRParser::Biosym_mrContext::dihedral_angle_constraints() {
  return getRuleContexts<BiosymMRParser::Dihedral_angle_constraintsContext>();
}

BiosymMRParser::Dihedral_angle_constraintsContext* BiosymMRParser::Biosym_mrContext::dihedral_angle_constraints(size_t i) {
  return getRuleContext<BiosymMRParser::Dihedral_angle_constraintsContext>(i);
}

std::vector<BiosymMRParser::Chirality_constraintsContext *> BiosymMRParser::Biosym_mrContext::chirality_constraints() {
  return getRuleContexts<BiosymMRParser::Chirality_constraintsContext>();
}

BiosymMRParser::Chirality_constraintsContext* BiosymMRParser::Biosym_mrContext::chirality_constraints(size_t i) {
  return getRuleContext<BiosymMRParser::Chirality_constraintsContext>(i);
}

std::vector<BiosymMRParser::Prochirality_constraintsContext *> BiosymMRParser::Biosym_mrContext::prochirality_constraints() {
  return getRuleContexts<BiosymMRParser::Prochirality_constraintsContext>();
}

BiosymMRParser::Prochirality_constraintsContext* BiosymMRParser::Biosym_mrContext::prochirality_constraints(size_t i) {
  return getRuleContext<BiosymMRParser::Prochirality_constraintsContext>(i);
}

std::vector<BiosymMRParser::Mixing_timeContext *> BiosymMRParser::Biosym_mrContext::mixing_time() {
  return getRuleContexts<BiosymMRParser::Mixing_timeContext>();
}

BiosymMRParser::Mixing_timeContext* BiosymMRParser::Biosym_mrContext::mixing_time(size_t i) {
  return getRuleContext<BiosymMRParser::Mixing_timeContext>(i);
}

std::vector<BiosymMRParser::Ins_distance_restraintsContext *> BiosymMRParser::Biosym_mrContext::ins_distance_restraints() {
  return getRuleContexts<BiosymMRParser::Ins_distance_restraintsContext>();
}

BiosymMRParser::Ins_distance_restraintsContext* BiosymMRParser::Biosym_mrContext::ins_distance_restraints(size_t i) {
  return getRuleContext<BiosymMRParser::Ins_distance_restraintsContext>(i);
}


size_t BiosymMRParser::Biosym_mrContext::getRuleIndex() const {
  return BiosymMRParser::RuleBiosym_mr;
}


std::any BiosymMRParser::Biosym_mrContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitBiosym_mr(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Biosym_mrContext* BiosymMRParser::biosym_mr() {
  Biosym_mrContext *_localctx = _tracker.createInstance<Biosym_mrContext>(_ctx, getState());
  enterRule(_localctx, 0, BiosymMRParser::RuleBiosym_mr);
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
    setState(50);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 3600) != 0)) {
      setState(48);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
      case 1: {
        setState(40);
        distance_restraints();
        break;
      }

      case 2: {
        setState(41);
        distance_constraints();
        break;
      }

      case 3: {
        setState(42);
        dihedral_angle_restraints();
        break;
      }

      case 4: {
        setState(43);
        dihedral_angle_constraints();
        break;
      }

      case 5: {
        setState(44);
        chirality_constraints();
        break;
      }

      case 6: {
        setState(45);
        prochirality_constraints();
        break;
      }

      case 7: {
        setState(46);
        mixing_time();
        break;
      }

      case 8: {
        setState(47);
        ins_distance_restraints();
        break;
      }

      default:
        break;
      }
      setState(52);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(53);
    match(BiosymMRParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_restraintsContext ------------------------------------------------------------------

BiosymMRParser::Distance_restraintsContext::Distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Distance_restraintContext *> BiosymMRParser::Distance_restraintsContext::distance_restraint() {
  return getRuleContexts<BiosymMRParser::Distance_restraintContext>();
}

BiosymMRParser::Distance_restraintContext* BiosymMRParser::Distance_restraintsContext::distance_restraint(size_t i) {
  return getRuleContext<BiosymMRParser::Distance_restraintContext>(i);
}


size_t BiosymMRParser::Distance_restraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleDistance_restraints;
}


std::any BiosymMRParser::Distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Distance_restraintsContext* BiosymMRParser::distance_restraints() {
  Distance_restraintsContext *_localctx = _tracker.createInstance<Distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 2, BiosymMRParser::RuleDistance_restraints);

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
    setState(56); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(55);
              distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(58); 
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

BiosymMRParser::Distance_restraintContext::Distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_restraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Distance_restraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Distance_restraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Distance_restraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

tree::TerminalNode* BiosymMRParser::Distance_restraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Distance_restraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleDistance_restraint;
}


std::any BiosymMRParser::Distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Distance_restraintContext* BiosymMRParser::distance_restraint() {
  Distance_restraintContext *_localctx = _tracker.createInstance<Distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 4, BiosymMRParser::RuleDistance_restraint);
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
    setState(61);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(60);
      match(BiosymMRParser::Ordinal);
    }
    setState(63);
    match(BiosymMRParser::Atom_selection);
    setState(64);
    match(BiosymMRParser::Atom_selection);
    setState(65);
    number();
    setState(66);
    number();
    setState(67);
    number();
    setState(68);
    number();
    setState(69);
    number();
    setState(70);
    number();
    setState(72);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0)) {
      setState(71);
      number();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_constraintsContext ------------------------------------------------------------------

BiosymMRParser::Distance_constraintsContext::Distance_constraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Distance_constraintContext *> BiosymMRParser::Distance_constraintsContext::distance_constraint() {
  return getRuleContexts<BiosymMRParser::Distance_constraintContext>();
}

BiosymMRParser::Distance_constraintContext* BiosymMRParser::Distance_constraintsContext::distance_constraint(size_t i) {
  return getRuleContext<BiosymMRParser::Distance_constraintContext>(i);
}


size_t BiosymMRParser::Distance_constraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleDistance_constraints;
}


std::any BiosymMRParser::Distance_constraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_constraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Distance_constraintsContext* BiosymMRParser::distance_constraints() {
  Distance_constraintsContext *_localctx = _tracker.createInstance<Distance_constraintsContext>(_ctx, getState());
  enterRule(_localctx, 6, BiosymMRParser::RuleDistance_constraints);

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
    setState(75); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(74);
              distance_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(77); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_constraintContext ------------------------------------------------------------------

BiosymMRParser::Distance_constraintContext::Distance_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_constraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Distance_constraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Distance_constraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Distance_constraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

tree::TerminalNode* BiosymMRParser::Distance_constraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Distance_constraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleDistance_constraint;
}


std::any BiosymMRParser::Distance_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_constraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Distance_constraintContext* BiosymMRParser::distance_constraint() {
  Distance_constraintContext *_localctx = _tracker.createInstance<Distance_constraintContext>(_ctx, getState());
  enterRule(_localctx, 8, BiosymMRParser::RuleDistance_constraint);
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
    setState(80);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(79);
      match(BiosymMRParser::Ordinal);
    }
    setState(82);
    match(BiosymMRParser::Atom_selection);
    setState(83);
    match(BiosymMRParser::Atom_selection);
    setState(84);
    number();
    setState(85);
    number();
    setState(90);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0)) {
      setState(86);
      number();
      setState(87);
      number();
      setState(88);
      number();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_restraintsContext ------------------------------------------------------------------

BiosymMRParser::Dihedral_angle_restraintsContext::Dihedral_angle_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Dihedral_angle_restraintContext *> BiosymMRParser::Dihedral_angle_restraintsContext::dihedral_angle_restraint() {
  return getRuleContexts<BiosymMRParser::Dihedral_angle_restraintContext>();
}

BiosymMRParser::Dihedral_angle_restraintContext* BiosymMRParser::Dihedral_angle_restraintsContext::dihedral_angle_restraint(size_t i) {
  return getRuleContext<BiosymMRParser::Dihedral_angle_restraintContext>(i);
}


size_t BiosymMRParser::Dihedral_angle_restraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleDihedral_angle_restraints;
}


std::any BiosymMRParser::Dihedral_angle_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_restraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Dihedral_angle_restraintsContext* BiosymMRParser::dihedral_angle_restraints() {
  Dihedral_angle_restraintsContext *_localctx = _tracker.createInstance<Dihedral_angle_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 10, BiosymMRParser::RuleDihedral_angle_restraints);

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
    setState(93); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(92);
              dihedral_angle_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(95); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_restraintContext ------------------------------------------------------------------

BiosymMRParser::Dihedral_angle_restraintContext::Dihedral_angle_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Dihedral_angle_restraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_restraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Dihedral_angle_restraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Dihedral_angle_restraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_restraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Dihedral_angle_restraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleDihedral_angle_restraint;
}


std::any BiosymMRParser::Dihedral_angle_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_restraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Dihedral_angle_restraintContext* BiosymMRParser::dihedral_angle_restraint() {
  Dihedral_angle_restraintContext *_localctx = _tracker.createInstance<Dihedral_angle_restraintContext>(_ctx, getState());
  enterRule(_localctx, 12, BiosymMRParser::RuleDihedral_angle_restraint);
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
    setState(98);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(97);
      match(BiosymMRParser::Ordinal);
    }
    setState(100);
    match(BiosymMRParser::Atom_selection);
    setState(101);
    match(BiosymMRParser::Atom_selection);
    setState(102);
    match(BiosymMRParser::Atom_selection);
    setState(103);
    match(BiosymMRParser::Atom_selection);
    setState(104);
    number();
    setState(105);
    number();
    setState(106);
    number();
    setState(107);
    number();
    setState(108);
    number();
    setState(109);
    number();
    setState(110);
    number();
    setState(114);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 10, _ctx)) {
    case 1: {
      setState(111);
      number();
      setState(112);
      number();
      break;
    }

    default:
      break;
    }
    setState(119);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx)) {
    case 1: {
      setState(116);
      number();
      setState(117);
      number();
      break;
    }

    default:
      break;
    }
    setState(124);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0)) {
      setState(121);
      number();
      setState(122);
      number();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_constraintsContext ------------------------------------------------------------------

BiosymMRParser::Dihedral_angle_constraintsContext::Dihedral_angle_constraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Dihedral_angle_constraintContext *> BiosymMRParser::Dihedral_angle_constraintsContext::dihedral_angle_constraint() {
  return getRuleContexts<BiosymMRParser::Dihedral_angle_constraintContext>();
}

BiosymMRParser::Dihedral_angle_constraintContext* BiosymMRParser::Dihedral_angle_constraintsContext::dihedral_angle_constraint(size_t i) {
  return getRuleContext<BiosymMRParser::Dihedral_angle_constraintContext>(i);
}


size_t BiosymMRParser::Dihedral_angle_constraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleDihedral_angle_constraints;
}


std::any BiosymMRParser::Dihedral_angle_constraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_constraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Dihedral_angle_constraintsContext* BiosymMRParser::dihedral_angle_constraints() {
  Dihedral_angle_constraintsContext *_localctx = _tracker.createInstance<Dihedral_angle_constraintsContext>(_ctx, getState());
  enterRule(_localctx, 14, BiosymMRParser::RuleDihedral_angle_constraints);

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
    setState(127); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(126);
              dihedral_angle_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(129); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 13, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_constraintContext ------------------------------------------------------------------

BiosymMRParser::Dihedral_angle_constraintContext::Dihedral_angle_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Dihedral_angle_constraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_constraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Dihedral_angle_constraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Dihedral_angle_constraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_constraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Dihedral_angle_constraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleDihedral_angle_constraint;
}


std::any BiosymMRParser::Dihedral_angle_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_constraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Dihedral_angle_constraintContext* BiosymMRParser::dihedral_angle_constraint() {
  Dihedral_angle_constraintContext *_localctx = _tracker.createInstance<Dihedral_angle_constraintContext>(_ctx, getState());
  enterRule(_localctx, 16, BiosymMRParser::RuleDihedral_angle_constraint);
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
    setState(132);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(131);
      match(BiosymMRParser::Ordinal);
    }
    setState(134);
    match(BiosymMRParser::Atom_selection);
    setState(135);
    match(BiosymMRParser::Atom_selection);
    setState(136);
    match(BiosymMRParser::Atom_selection);
    setState(137);
    match(BiosymMRParser::Atom_selection);
    setState(138);
    number();
    setState(139);
    number();
    setState(144);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0)) {
      setState(140);
      number();
      setState(141);
      number();
      setState(142);
      number();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Chirality_constraintsContext ------------------------------------------------------------------

BiosymMRParser::Chirality_constraintsContext::Chirality_constraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Chirality_constraintContext *> BiosymMRParser::Chirality_constraintsContext::chirality_constraint() {
  return getRuleContexts<BiosymMRParser::Chirality_constraintContext>();
}

BiosymMRParser::Chirality_constraintContext* BiosymMRParser::Chirality_constraintsContext::chirality_constraint(size_t i) {
  return getRuleContext<BiosymMRParser::Chirality_constraintContext>(i);
}


size_t BiosymMRParser::Chirality_constraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleChirality_constraints;
}


std::any BiosymMRParser::Chirality_constraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitChirality_constraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Chirality_constraintsContext* BiosymMRParser::chirality_constraints() {
  Chirality_constraintsContext *_localctx = _tracker.createInstance<Chirality_constraintsContext>(_ctx, getState());
  enterRule(_localctx, 18, BiosymMRParser::RuleChirality_constraints);

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
    setState(147); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(146);
              chirality_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(149); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 16, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Chirality_constraintContext ------------------------------------------------------------------

BiosymMRParser::Chirality_constraintContext::Chirality_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Chirality_constraintContext::Atom_selection() {
  return getToken(BiosymMRParser::Atom_selection, 0);
}

tree::TerminalNode* BiosymMRParser::Chirality_constraintContext::Chiral_code() {
  return getToken(BiosymMRParser::Chiral_code, 0);
}

tree::TerminalNode* BiosymMRParser::Chirality_constraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Chirality_constraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleChirality_constraint;
}


std::any BiosymMRParser::Chirality_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitChirality_constraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Chirality_constraintContext* BiosymMRParser::chirality_constraint() {
  Chirality_constraintContext *_localctx = _tracker.createInstance<Chirality_constraintContext>(_ctx, getState());
  enterRule(_localctx, 20, BiosymMRParser::RuleChirality_constraint);
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
    setState(152);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(151);
      match(BiosymMRParser::Ordinal);
    }
    setState(154);
    match(BiosymMRParser::Atom_selection);
    setState(155);
    match(BiosymMRParser::Chiral_code);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Prochirality_constraintsContext ------------------------------------------------------------------

BiosymMRParser::Prochirality_constraintsContext::Prochirality_constraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Prochirality_constraintContext *> BiosymMRParser::Prochirality_constraintsContext::prochirality_constraint() {
  return getRuleContexts<BiosymMRParser::Prochirality_constraintContext>();
}

BiosymMRParser::Prochirality_constraintContext* BiosymMRParser::Prochirality_constraintsContext::prochirality_constraint(size_t i) {
  return getRuleContext<BiosymMRParser::Prochirality_constraintContext>(i);
}


size_t BiosymMRParser::Prochirality_constraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleProchirality_constraints;
}


std::any BiosymMRParser::Prochirality_constraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitProchirality_constraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Prochirality_constraintsContext* BiosymMRParser::prochirality_constraints() {
  Prochirality_constraintsContext *_localctx = _tracker.createInstance<Prochirality_constraintsContext>(_ctx, getState());
  enterRule(_localctx, 22, BiosymMRParser::RuleProchirality_constraints);

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
    setState(158); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(157);
              prochirality_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(160); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Prochirality_constraintContext ------------------------------------------------------------------

BiosymMRParser::Prochirality_constraintContext::Prochirality_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Prochirality_constraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Prochirality_constraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

tree::TerminalNode* BiosymMRParser::Prochirality_constraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Prochirality_constraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleProchirality_constraint;
}


std::any BiosymMRParser::Prochirality_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitProchirality_constraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Prochirality_constraintContext* BiosymMRParser::prochirality_constraint() {
  Prochirality_constraintContext *_localctx = _tracker.createInstance<Prochirality_constraintContext>(_ctx, getState());
  enterRule(_localctx, 24, BiosymMRParser::RuleProchirality_constraint);
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
    setState(163);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(162);
      match(BiosymMRParser::Ordinal);
    }
    setState(165);
    match(BiosymMRParser::Atom_selection);
    setState(166);
    match(BiosymMRParser::Atom_selection);
    setState(167);
    match(BiosymMRParser::Atom_selection);
    setState(168);
    match(BiosymMRParser::Atom_selection);
    setState(169);
    match(BiosymMRParser::Atom_selection);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Mixing_timeContext ------------------------------------------------------------------

BiosymMRParser::Mixing_timeContext::Mixing_timeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::Real() {
  return getToken(BiosymMRParser::Real, 0);
}


size_t BiosymMRParser::Mixing_timeContext::getRuleIndex() const {
  return BiosymMRParser::RuleMixing_time;
}


std::any BiosymMRParser::Mixing_timeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitMixing_time(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Mixing_timeContext* BiosymMRParser::mixing_time() {
  Mixing_timeContext *_localctx = _tracker.createInstance<Mixing_timeContext>(_ctx, getState());
  enterRule(_localctx, 26, BiosymMRParser::RuleMixing_time);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(171);
    match(BiosymMRParser::Real);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberContext ------------------------------------------------------------------

BiosymMRParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::NumberContext::Float() {
  return getToken(BiosymMRParser::Float, 0);
}

tree::TerminalNode* BiosymMRParser::NumberContext::Float_DecimalComma() {
  return getToken(BiosymMRParser::Float_DecimalComma, 0);
}

tree::TerminalNode* BiosymMRParser::NumberContext::Integer() {
  return getToken(BiosymMRParser::Integer, 0);
}


size_t BiosymMRParser::NumberContext::getRuleIndex() const {
  return BiosymMRParser::RuleNumber;
}


std::any BiosymMRParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::NumberContext* BiosymMRParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 28, BiosymMRParser::RuleNumber);
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
    setState(173);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0))) {
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

//----------------- Ins_distance_restraintsContext ------------------------------------------------------------------

BiosymMRParser::Ins_distance_restraintsContext::Ins_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BiosymMRParser::Ins_distance_restraintContext* BiosymMRParser::Ins_distance_restraintsContext::ins_distance_restraint() {
  return getRuleContext<BiosymMRParser::Ins_distance_restraintContext>(0);
}


size_t BiosymMRParser::Ins_distance_restraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleIns_distance_restraints;
}


std::any BiosymMRParser::Ins_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitIns_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Ins_distance_restraintsContext* BiosymMRParser::ins_distance_restraints() {
  Ins_distance_restraintsContext *_localctx = _tracker.createInstance<Ins_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 30, BiosymMRParser::RuleIns_distance_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(175);
    ins_distance_restraint();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ins_distance_restraintContext ------------------------------------------------------------------

BiosymMRParser::Ins_distance_restraintContext::Ins_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BiosymMRParser::Decl_createContext* BiosymMRParser::Ins_distance_restraintContext::decl_create() {
  return getRuleContext<BiosymMRParser::Decl_createContext>(0);
}

BiosymMRParser::Decl_functionContext* BiosymMRParser::Ins_distance_restraintContext::decl_function() {
  return getRuleContext<BiosymMRParser::Decl_functionContext>(0);
}

BiosymMRParser::Decl_targetContext* BiosymMRParser::Ins_distance_restraintContext::decl_target() {
  return getRuleContext<BiosymMRParser::Decl_targetContext>(0);
}


size_t BiosymMRParser::Ins_distance_restraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleIns_distance_restraint;
}


std::any BiosymMRParser::Ins_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitIns_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Ins_distance_restraintContext* BiosymMRParser::ins_distance_restraint() {
  Ins_distance_restraintContext *_localctx = _tracker.createInstance<Ins_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 32, BiosymMRParser::RuleIns_distance_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(177);
    decl_create();
    setState(178);
    decl_function();
    setState(179);
    decl_target();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Decl_createContext ------------------------------------------------------------------

BiosymMRParser::Decl_createContext::Decl_createContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Decl_createContext::Restraint() {
  return getToken(BiosymMRParser::Restraint, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_createContext::Create() {
  return getToken(BiosymMRParser::Create, 0);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Decl_createContext::Double_quote_string() {
  return getTokens(BiosymMRParser::Double_quote_string);
}

tree::TerminalNode* BiosymMRParser::Decl_createContext::Double_quote_string(size_t i) {
  return getToken(BiosymMRParser::Double_quote_string, i);
}

tree::TerminalNode* BiosymMRParser::Decl_createContext::Distance() {
  return getToken(BiosymMRParser::Distance, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_createContext::RETURN_II() {
  return getToken(BiosymMRParser::RETURN_II, 0);
}


size_t BiosymMRParser::Decl_createContext::getRuleIndex() const {
  return BiosymMRParser::RuleDecl_create;
}


std::any BiosymMRParser::Decl_createContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDecl_create(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Decl_createContext* BiosymMRParser::decl_create() {
  Decl_createContext *_localctx = _tracker.createInstance<Decl_createContext>(_ctx, getState());
  enterRule(_localctx, 34, BiosymMRParser::RuleDecl_create);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(181);
    match(BiosymMRParser::Restraint);
    setState(182);
    match(BiosymMRParser::Create);
    setState(183);
    match(BiosymMRParser::Double_quote_string);
    setState(184);
    match(BiosymMRParser::Distance);
    setState(185);
    match(BiosymMRParser::Double_quote_string);
    setState(186);
    match(BiosymMRParser::Double_quote_string);
    setState(187);
    match(BiosymMRParser::RETURN_II);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Decl_functionContext ------------------------------------------------------------------

BiosymMRParser::Decl_functionContext::Decl_functionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Decl_functionContext::Restraint() {
  return getToken(BiosymMRParser::Restraint, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_functionContext::Function() {
  return getToken(BiosymMRParser::Function, 0);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Decl_functionContext::Double_quote_string() {
  return getTokens(BiosymMRParser::Double_quote_string);
}

tree::TerminalNode* BiosymMRParser::Decl_functionContext::Double_quote_string(size_t i) {
  return getToken(BiosymMRParser::Double_quote_string, i);
}

tree::TerminalNode* BiosymMRParser::Decl_functionContext::RETURN_II() {
  return getToken(BiosymMRParser::RETURN_II, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_functionContext::Quadratic() {
  return getToken(BiosymMRParser::Quadratic, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_functionContext::Flat_bottomed() {
  return getToken(BiosymMRParser::Flat_bottomed, 0);
}


size_t BiosymMRParser::Decl_functionContext::getRuleIndex() const {
  return BiosymMRParser::RuleDecl_function;
}


std::any BiosymMRParser::Decl_functionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDecl_function(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Decl_functionContext* BiosymMRParser::decl_function() {
  Decl_functionContext *_localctx = _tracker.createInstance<Decl_functionContext>(_ctx, getState());
  enterRule(_localctx, 36, BiosymMRParser::RuleDecl_function);
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
    setState(189);
    match(BiosymMRParser::Restraint);
    setState(190);
    match(BiosymMRParser::Function);
    setState(191);
    match(BiosymMRParser::Double_quote_string);
    setState(192);
    _la = _input->LA(1);
    if (!(_la == BiosymMRParser::Quadratic

    || _la == BiosymMRParser::Flat_bottomed)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(193);
    match(BiosymMRParser::Double_quote_string);
    setState(194);
    match(BiosymMRParser::Double_quote_string);
    setState(196);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Double_quote_string) {
      setState(195);
      match(BiosymMRParser::Double_quote_string);
    }
    setState(198);
    match(BiosymMRParser::RETURN_II);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Decl_targetContext ------------------------------------------------------------------

BiosymMRParser::Decl_targetContext::Decl_targetContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Decl_targetContext::Restraint() {
  return getToken(BiosymMRParser::Restraint, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_targetContext::Target() {
  return getToken(BiosymMRParser::Target, 0);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Decl_targetContext::Double_quote_string() {
  return getTokens(BiosymMRParser::Double_quote_string);
}

tree::TerminalNode* BiosymMRParser::Decl_targetContext::Double_quote_string(size_t i) {
  return getToken(BiosymMRParser::Double_quote_string, i);
}

tree::TerminalNode* BiosymMRParser::Decl_targetContext::RETURN_II() {
  return getToken(BiosymMRParser::RETURN_II, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_targetContext::Relative() {
  return getToken(BiosymMRParser::Relative, 0);
}


size_t BiosymMRParser::Decl_targetContext::getRuleIndex() const {
  return BiosymMRParser::RuleDecl_target;
}


std::any BiosymMRParser::Decl_targetContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDecl_target(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Decl_targetContext* BiosymMRParser::decl_target() {
  Decl_targetContext *_localctx = _tracker.createInstance<Decl_targetContext>(_ctx, getState());
  enterRule(_localctx, 38, BiosymMRParser::RuleDecl_target);
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
    setState(200);
    match(BiosymMRParser::Restraint);
    setState(201);
    match(BiosymMRParser::Target);
    setState(202);
    match(BiosymMRParser::Double_quote_string);
    setState(203);
    _la = _input->LA(1);
    if (!(_la == BiosymMRParser::Double_quote_string

    || _la == BiosymMRParser::Relative)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(204);
    match(BiosymMRParser::Double_quote_string);
    setState(205);
    match(BiosymMRParser::RETURN_II);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

void BiosymMRParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  biosymmrparserParserInitialize();
#else
  ::antlr4::internal::call_once(biosymmrparserParserOnceFlag, biosymmrparserParserInitialize);
#endif
}
