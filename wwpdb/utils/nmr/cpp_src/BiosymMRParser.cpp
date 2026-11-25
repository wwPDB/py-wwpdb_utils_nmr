
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
      "distance_constraint", "distance_wo_w_constraints", "distance_wo_w_constraint", 
      "dihedral_angle_restraints", "dihedral_angle_restraint", "dihedral_angle_constraints", 
      "dihedral_angle_constraint", "dihedral_angle_wo_w_constraints", "dihedral_angle_wo_w_constraint", 
      "rdc_restraints", "rdc_restraint", "chirality_constraints", "chirality_constraint", 
      "prochirality_constraints", "prochirality_constraint", "mixing_time", 
      "number", "ins_distance_restraints", "ins_distance_restraint", "decl_create", 
      "decl_function", "decl_target"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "", "", "", "'+'", "'restraint'", 
      "", "", "", "", "", "", "'create'", "'function'", "'target'", "'distance'", 
      "'quadratic'", "'flatBottomed'", "'relative'", "", "", "", "", "", 
      "','", "'.'"
    },
    std::vector<std::string>{
      "", "Integer", "Float", "Float_DecimalComma", "Real", "SHARP_COMMENT", 
      "EXCLM_COMMENT", "SMCLN_COMMENT", "Chiral_code", "Atom_selection", 
      "Ordinal", "Or", "Restraint", "Mixing_times", "SPACE", "ENCLOSE_COMMENT", 
      "SECTION_COMMENT", "LINE_COMMENT", "Double_quote_string", "Create", 
      "Function", "Target", "Distance", "Quadratic", "Flat_bottomed", "Relative", 
      "SPACE_II", "RETURN_II", "Real_MT", "Float_MT", "Integer_MT", "Comma_MT", 
      "Period_MT", "SPACE_MT", "RETURN_MT"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,34,298,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,0,1,0,1,0,1,0,1,
  	0,1,0,1,0,1,0,1,0,5,0,64,8,0,10,0,12,0,67,9,0,1,0,1,0,1,1,4,1,72,8,1,
  	11,1,12,1,73,1,2,3,2,77,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,88,
  	8,2,1,2,1,2,1,2,5,2,93,8,2,10,2,12,2,96,9,2,1,3,4,3,99,8,3,11,3,12,3,
  	100,1,4,3,4,104,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,116,8,
  	4,10,4,12,4,119,9,4,1,5,4,5,122,8,5,11,5,12,5,123,1,6,3,6,127,8,6,1,6,
  	1,6,1,6,1,6,1,6,3,6,134,8,6,1,6,1,6,1,6,5,6,139,8,6,10,6,12,6,142,9,6,
  	1,7,4,7,145,8,7,11,7,12,7,146,1,8,3,8,150,8,8,1,8,1,8,1,8,1,8,1,8,1,8,
  	1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,166,8,8,1,8,1,8,1,8,3,8,171,8,8,1,
  	8,1,8,1,8,3,8,176,8,8,1,9,4,9,179,8,9,11,9,12,9,180,1,10,3,10,184,8,10,
  	1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,195,8,10,1,11,4,11,
  	198,8,11,11,11,12,11,199,1,12,3,12,203,8,12,1,12,1,12,1,12,1,12,1,12,
  	1,12,1,12,1,13,4,13,213,8,13,11,13,12,13,214,1,14,3,14,218,8,14,1,14,
  	1,14,1,14,1,14,1,14,1,14,1,14,1,15,4,15,228,8,15,11,15,12,15,229,1,16,
  	3,16,233,8,16,1,16,1,16,1,16,1,17,4,17,239,8,17,11,17,12,17,240,1,18,
  	3,18,244,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,3,19,255,8,
  	19,5,19,257,8,19,10,19,12,19,260,9,19,1,19,1,19,1,20,1,20,1,21,1,21,1,
  	22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,
  	24,1,24,1,24,1,24,1,24,3,24,287,8,24,1,24,1,24,1,25,1,25,1,25,1,25,1,
  	25,1,25,1,25,1,25,0,0,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
  	34,36,38,40,42,44,46,48,50,0,5,1,0,28,30,1,0,31,32,1,0,1,3,1,0,23,24,
  	2,0,18,18,25,25,312,0,65,1,0,0,0,2,71,1,0,0,0,4,76,1,0,0,0,6,98,1,0,0,
  	0,8,103,1,0,0,0,10,121,1,0,0,0,12,126,1,0,0,0,14,144,1,0,0,0,16,149,1,
  	0,0,0,18,178,1,0,0,0,20,183,1,0,0,0,22,197,1,0,0,0,24,202,1,0,0,0,26,
  	212,1,0,0,0,28,217,1,0,0,0,30,227,1,0,0,0,32,232,1,0,0,0,34,238,1,0,0,
  	0,36,243,1,0,0,0,38,251,1,0,0,0,40,263,1,0,0,0,42,265,1,0,0,0,44,267,
  	1,0,0,0,46,271,1,0,0,0,48,279,1,0,0,0,50,290,1,0,0,0,52,64,3,2,1,0,53,
  	64,3,6,3,0,54,64,3,10,5,0,55,64,3,14,7,0,56,64,3,18,9,0,57,64,3,22,11,
  	0,58,64,3,26,13,0,59,64,3,30,15,0,60,64,3,34,17,0,61,64,3,38,19,0,62,
  	64,3,42,21,0,63,52,1,0,0,0,63,53,1,0,0,0,63,54,1,0,0,0,63,55,1,0,0,0,
  	63,56,1,0,0,0,63,57,1,0,0,0,63,58,1,0,0,0,63,59,1,0,0,0,63,60,1,0,0,0,
  	63,61,1,0,0,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,
  	66,68,1,0,0,0,67,65,1,0,0,0,68,69,5,0,0,1,69,1,1,0,0,0,70,72,3,4,2,0,
  	71,70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,3,1,0,0,0,
  	75,77,5,10,0,0,76,75,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,79,5,9,0,
  	0,79,80,5,9,0,0,80,81,3,40,20,0,81,82,3,40,20,0,82,83,3,40,20,0,83,84,
  	3,40,20,0,84,85,3,40,20,0,85,87,3,40,20,0,86,88,3,40,20,0,87,86,1,0,0,
  	0,87,88,1,0,0,0,88,94,1,0,0,0,89,90,5,11,0,0,90,91,5,9,0,0,91,93,5,9,
  	0,0,92,89,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,5,1,0,
  	0,0,96,94,1,0,0,0,97,99,3,8,4,0,98,97,1,0,0,0,99,100,1,0,0,0,100,98,1,
  	0,0,0,100,101,1,0,0,0,101,7,1,0,0,0,102,104,5,10,0,0,103,102,1,0,0,0,
  	103,104,1,0,0,0,104,105,1,0,0,0,105,106,5,9,0,0,106,107,5,9,0,0,107,108,
  	3,40,20,0,108,109,3,40,20,0,109,110,3,40,20,0,110,111,3,40,20,0,111,117,
  	3,40,20,0,112,113,5,11,0,0,113,114,5,9,0,0,114,116,5,9,0,0,115,112,1,
  	0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,9,1,0,0,0,119,
  	117,1,0,0,0,120,122,3,12,6,0,121,120,1,0,0,0,122,123,1,0,0,0,123,121,
  	1,0,0,0,123,124,1,0,0,0,124,11,1,0,0,0,125,127,5,10,0,0,126,125,1,0,0,
  	0,126,127,1,0,0,0,127,128,1,0,0,0,128,129,5,9,0,0,129,130,5,9,0,0,130,
  	131,3,40,20,0,131,133,3,40,20,0,132,134,3,40,20,0,133,132,1,0,0,0,133,
  	134,1,0,0,0,134,140,1,0,0,0,135,136,5,11,0,0,136,137,5,9,0,0,137,139,
  	5,9,0,0,138,135,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,
  	0,141,13,1,0,0,0,142,140,1,0,0,0,143,145,3,16,8,0,144,143,1,0,0,0,145,
  	146,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,15,1,0,0,0,148,150,5,
  	10,0,0,149,148,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,152,5,9,0,
  	0,152,153,5,9,0,0,153,154,5,9,0,0,154,155,5,9,0,0,155,156,3,40,20,0,156,
  	157,3,40,20,0,157,158,3,40,20,0,158,159,3,40,20,0,159,160,3,40,20,0,160,
  	161,3,40,20,0,161,165,3,40,20,0,162,163,3,40,20,0,163,164,3,40,20,0,164,
  	166,1,0,0,0,165,162,1,0,0,0,165,166,1,0,0,0,166,170,1,0,0,0,167,168,3,
  	40,20,0,168,169,3,40,20,0,169,171,1,0,0,0,170,167,1,0,0,0,170,171,1,0,
  	0,0,171,175,1,0,0,0,172,173,3,40,20,0,173,174,3,40,20,0,174,176,1,0,0,
  	0,175,172,1,0,0,0,175,176,1,0,0,0,176,17,1,0,0,0,177,179,3,20,10,0,178,
  	177,1,0,0,0,179,180,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,19,1,
  	0,0,0,182,184,5,10,0,0,183,182,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,
  	0,185,186,5,9,0,0,186,187,5,9,0,0,187,188,5,9,0,0,188,189,5,9,0,0,189,
  	190,3,40,20,0,190,191,3,40,20,0,191,192,3,40,20,0,192,194,3,40,20,0,193,
  	195,3,40,20,0,194,193,1,0,0,0,194,195,1,0,0,0,195,21,1,0,0,0,196,198,
  	3,24,12,0,197,196,1,0,0,0,198,199,1,0,0,0,199,197,1,0,0,0,199,200,1,0,
  	0,0,200,23,1,0,0,0,201,203,5,10,0,0,202,201,1,0,0,0,202,203,1,0,0,0,203,
  	204,1,0,0,0,204,205,5,9,0,0,205,206,5,9,0,0,206,207,5,9,0,0,207,208,5,
  	9,0,0,208,209,3,40,20,0,209,210,3,40,20,0,210,25,1,0,0,0,211,213,3,28,
  	14,0,212,211,1,0,0,0,213,214,1,0,0,0,214,212,1,0,0,0,214,215,1,0,0,0,
  	215,27,1,0,0,0,216,218,5,10,0,0,217,216,1,0,0,0,217,218,1,0,0,0,218,219,
  	1,0,0,0,219,220,5,9,0,0,220,221,5,9,0,0,221,222,3,40,20,0,222,223,3,40,
  	20,0,223,224,3,40,20,0,224,225,3,40,20,0,225,29,1,0,0,0,226,228,3,32,
  	16,0,227,226,1,0,0,0,228,229,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,
  	230,31,1,0,0,0,231,233,5,10,0,0,232,231,1,0,0,0,232,233,1,0,0,0,233,234,
  	1,0,0,0,234,235,5,9,0,0,235,236,5,8,0,0,236,33,1,0,0,0,237,239,3,36,18,
  	0,238,237,1,0,0,0,239,240,1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,0,241,
  	35,1,0,0,0,242,244,5,10,0,0,243,242,1,0,0,0,243,244,1,0,0,0,244,245,1,
  	0,0,0,245,246,5,9,0,0,246,247,5,9,0,0,247,248,5,9,0,0,248,249,5,9,0,0,
  	249,250,5,9,0,0,250,37,1,0,0,0,251,258,5,13,0,0,252,254,7,0,0,0,253,255,
  	7,1,0,0,254,253,1,0,0,0,254,255,1,0,0,0,255,257,1,0,0,0,256,252,1,0,0,
  	0,257,260,1,0,0,0,258,256,1,0,0,0,258,259,1,0,0,0,259,261,1,0,0,0,260,
  	258,1,0,0,0,261,262,5,34,0,0,262,39,1,0,0,0,263,264,7,2,0,0,264,41,1,
  	0,0,0,265,266,3,44,22,0,266,43,1,0,0,0,267,268,3,46,23,0,268,269,3,48,
  	24,0,269,270,3,50,25,0,270,45,1,0,0,0,271,272,5,12,0,0,272,273,5,19,0,
  	0,273,274,5,18,0,0,274,275,5,22,0,0,275,276,5,18,0,0,276,277,5,18,0,0,
  	277,278,5,27,0,0,278,47,1,0,0,0,279,280,5,12,0,0,280,281,5,20,0,0,281,
  	282,5,18,0,0,282,283,7,3,0,0,283,284,5,18,0,0,284,286,5,18,0,0,285,287,
  	5,18,0,0,286,285,1,0,0,0,286,287,1,0,0,0,287,288,1,0,0,0,288,289,5,27,
  	0,0,289,49,1,0,0,0,290,291,5,12,0,0,291,292,5,21,0,0,292,293,5,18,0,0,
  	293,294,7,4,0,0,294,295,5,18,0,0,295,296,5,27,0,0,296,51,1,0,0,0,32,63,
  	65,73,76,87,94,100,103,117,123,126,133,140,146,149,165,170,175,180,183,
  	194,199,202,214,217,229,232,240,243,254,258,286
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

std::vector<BiosymMRParser::Distance_wo_w_constraintsContext *> BiosymMRParser::Biosym_mrContext::distance_wo_w_constraints() {
  return getRuleContexts<BiosymMRParser::Distance_wo_w_constraintsContext>();
}

BiosymMRParser::Distance_wo_w_constraintsContext* BiosymMRParser::Biosym_mrContext::distance_wo_w_constraints(size_t i) {
  return getRuleContext<BiosymMRParser::Distance_wo_w_constraintsContext>(i);
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

std::vector<BiosymMRParser::Dihedral_angle_wo_w_constraintsContext *> BiosymMRParser::Biosym_mrContext::dihedral_angle_wo_w_constraints() {
  return getRuleContexts<BiosymMRParser::Dihedral_angle_wo_w_constraintsContext>();
}

BiosymMRParser::Dihedral_angle_wo_w_constraintsContext* BiosymMRParser::Biosym_mrContext::dihedral_angle_wo_w_constraints(size_t i) {
  return getRuleContext<BiosymMRParser::Dihedral_angle_wo_w_constraintsContext>(i);
}

std::vector<BiosymMRParser::Rdc_restraintsContext *> BiosymMRParser::Biosym_mrContext::rdc_restraints() {
  return getRuleContexts<BiosymMRParser::Rdc_restraintsContext>();
}

BiosymMRParser::Rdc_restraintsContext* BiosymMRParser::Biosym_mrContext::rdc_restraints(size_t i) {
  return getRuleContext<BiosymMRParser::Rdc_restraintsContext>(i);
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
    setState(65);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 13824) != 0)) {
      setState(63);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
      case 1: {
        setState(52);
        distance_restraints();
        break;
      }

      case 2: {
        setState(53);
        distance_constraints();
        break;
      }

      case 3: {
        setState(54);
        distance_wo_w_constraints();
        break;
      }

      case 4: {
        setState(55);
        dihedral_angle_restraints();
        break;
      }

      case 5: {
        setState(56);
        dihedral_angle_constraints();
        break;
      }

      case 6: {
        setState(57);
        dihedral_angle_wo_w_constraints();
        break;
      }

      case 7: {
        setState(58);
        rdc_restraints();
        break;
      }

      case 8: {
        setState(59);
        chirality_constraints();
        break;
      }

      case 9: {
        setState(60);
        prochirality_constraints();
        break;
      }

      case 10: {
        setState(61);
        mixing_time();
        break;
      }

      case 11: {
        setState(62);
        ins_distance_restraints();
        break;
      }

      default:
        break;
      }
      setState(67);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(68);
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
    setState(71); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(70);
              distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(73); 
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

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_restraintContext::Or() {
  return getTokens(BiosymMRParser::Or);
}

tree::TerminalNode* BiosymMRParser::Distance_restraintContext::Or(size_t i) {
  return getToken(BiosymMRParser::Or, i);
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
    setState(76);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(75);
      match(BiosymMRParser::Ordinal);
    }
    setState(78);
    match(BiosymMRParser::Atom_selection);
    setState(79);
    match(BiosymMRParser::Atom_selection);
    setState(80);
    number();
    setState(81);
    number();
    setState(82);
    number();
    setState(83);
    number();
    setState(84);
    number();
    setState(85);
    number();
    setState(87);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0)) {
      setState(86);
      number();
    }
    setState(94);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BiosymMRParser::Or) {
      setState(89);
      match(BiosymMRParser::Or);
      setState(90);
      match(BiosymMRParser::Atom_selection);
      setState(91);
      match(BiosymMRParser::Atom_selection);
      setState(96);
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
    setState(98); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(97);
              distance_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(100); 
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

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_constraintContext::Or() {
  return getTokens(BiosymMRParser::Or);
}

tree::TerminalNode* BiosymMRParser::Distance_constraintContext::Or(size_t i) {
  return getToken(BiosymMRParser::Or, i);
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
    setState(103);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(102);
      match(BiosymMRParser::Ordinal);
    }
    setState(105);
    match(BiosymMRParser::Atom_selection);
    setState(106);
    match(BiosymMRParser::Atom_selection);
    setState(107);
    number();
    setState(108);
    number();
    setState(109);
    number();
    setState(110);
    number();
    setState(111);
    number();
    setState(117);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BiosymMRParser::Or) {
      setState(112);
      match(BiosymMRParser::Or);
      setState(113);
      match(BiosymMRParser::Atom_selection);
      setState(114);
      match(BiosymMRParser::Atom_selection);
      setState(119);
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

//----------------- Distance_wo_w_constraintsContext ------------------------------------------------------------------

BiosymMRParser::Distance_wo_w_constraintsContext::Distance_wo_w_constraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Distance_wo_w_constraintContext *> BiosymMRParser::Distance_wo_w_constraintsContext::distance_wo_w_constraint() {
  return getRuleContexts<BiosymMRParser::Distance_wo_w_constraintContext>();
}

BiosymMRParser::Distance_wo_w_constraintContext* BiosymMRParser::Distance_wo_w_constraintsContext::distance_wo_w_constraint(size_t i) {
  return getRuleContext<BiosymMRParser::Distance_wo_w_constraintContext>(i);
}


size_t BiosymMRParser::Distance_wo_w_constraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleDistance_wo_w_constraints;
}


std::any BiosymMRParser::Distance_wo_w_constraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_wo_w_constraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Distance_wo_w_constraintsContext* BiosymMRParser::distance_wo_w_constraints() {
  Distance_wo_w_constraintsContext *_localctx = _tracker.createInstance<Distance_wo_w_constraintsContext>(_ctx, getState());
  enterRule(_localctx, 10, BiosymMRParser::RuleDistance_wo_w_constraints);

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
    setState(121); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(120);
              distance_wo_w_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(123); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_wo_w_constraintContext ------------------------------------------------------------------

BiosymMRParser::Distance_wo_w_constraintContext::Distance_wo_w_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_wo_w_constraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Distance_wo_w_constraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Distance_wo_w_constraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Distance_wo_w_constraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

tree::TerminalNode* BiosymMRParser::Distance_wo_w_constraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_wo_w_constraintContext::Or() {
  return getTokens(BiosymMRParser::Or);
}

tree::TerminalNode* BiosymMRParser::Distance_wo_w_constraintContext::Or(size_t i) {
  return getToken(BiosymMRParser::Or, i);
}


size_t BiosymMRParser::Distance_wo_w_constraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleDistance_wo_w_constraint;
}


std::any BiosymMRParser::Distance_wo_w_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_wo_w_constraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Distance_wo_w_constraintContext* BiosymMRParser::distance_wo_w_constraint() {
  Distance_wo_w_constraintContext *_localctx = _tracker.createInstance<Distance_wo_w_constraintContext>(_ctx, getState());
  enterRule(_localctx, 12, BiosymMRParser::RuleDistance_wo_w_constraint);
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
    setState(126);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(125);
      match(BiosymMRParser::Ordinal);
    }
    setState(128);
    match(BiosymMRParser::Atom_selection);
    setState(129);
    match(BiosymMRParser::Atom_selection);
    setState(130);
    number();
    setState(131);
    number();
    setState(133);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0)) {
      setState(132);
      number();
    }
    setState(140);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BiosymMRParser::Or) {
      setState(135);
      match(BiosymMRParser::Or);
      setState(136);
      match(BiosymMRParser::Atom_selection);
      setState(137);
      match(BiosymMRParser::Atom_selection);
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
  enterRule(_localctx, 14, BiosymMRParser::RuleDihedral_angle_restraints);

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
    setState(144); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(143);
              dihedral_angle_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(146); 
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
  enterRule(_localctx, 16, BiosymMRParser::RuleDihedral_angle_restraint);
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
    setState(149);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(148);
      match(BiosymMRParser::Ordinal);
    }
    setState(151);
    match(BiosymMRParser::Atom_selection);
    setState(152);
    match(BiosymMRParser::Atom_selection);
    setState(153);
    match(BiosymMRParser::Atom_selection);
    setState(154);
    match(BiosymMRParser::Atom_selection);
    setState(155);
    number();
    setState(156);
    number();
    setState(157);
    number();
    setState(158);
    number();
    setState(159);
    number();
    setState(160);
    number();
    setState(161);
    number();
    setState(165);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 15, _ctx)) {
    case 1: {
      setState(162);
      number();
      setState(163);
      number();
      break;
    }

    default:
      break;
    }
    setState(170);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 16, _ctx)) {
    case 1: {
      setState(167);
      number();
      setState(168);
      number();
      break;
    }

    default:
      break;
    }
    setState(175);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0)) {
      setState(172);
      number();
      setState(173);
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
  enterRule(_localctx, 18, BiosymMRParser::RuleDihedral_angle_constraints);

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
    setState(178); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(177);
              dihedral_angle_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(180); 
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
  enterRule(_localctx, 20, BiosymMRParser::RuleDihedral_angle_constraint);
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
    setState(183);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(182);
      match(BiosymMRParser::Ordinal);
    }
    setState(185);
    match(BiosymMRParser::Atom_selection);
    setState(186);
    match(BiosymMRParser::Atom_selection);
    setState(187);
    match(BiosymMRParser::Atom_selection);
    setState(188);
    match(BiosymMRParser::Atom_selection);
    setState(189);
    number();
    setState(190);
    number();
    setState(191);
    number();
    setState(192);
    number();
    setState(194);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0)) {
      setState(193);
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

//----------------- Dihedral_angle_wo_w_constraintsContext ------------------------------------------------------------------

BiosymMRParser::Dihedral_angle_wo_w_constraintsContext::Dihedral_angle_wo_w_constraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Dihedral_angle_wo_w_constraintContext *> BiosymMRParser::Dihedral_angle_wo_w_constraintsContext::dihedral_angle_wo_w_constraint() {
  return getRuleContexts<BiosymMRParser::Dihedral_angle_wo_w_constraintContext>();
}

BiosymMRParser::Dihedral_angle_wo_w_constraintContext* BiosymMRParser::Dihedral_angle_wo_w_constraintsContext::dihedral_angle_wo_w_constraint(size_t i) {
  return getRuleContext<BiosymMRParser::Dihedral_angle_wo_w_constraintContext>(i);
}


size_t BiosymMRParser::Dihedral_angle_wo_w_constraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleDihedral_angle_wo_w_constraints;
}


std::any BiosymMRParser::Dihedral_angle_wo_w_constraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_wo_w_constraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Dihedral_angle_wo_w_constraintsContext* BiosymMRParser::dihedral_angle_wo_w_constraints() {
  Dihedral_angle_wo_w_constraintsContext *_localctx = _tracker.createInstance<Dihedral_angle_wo_w_constraintsContext>(_ctx, getState());
  enterRule(_localctx, 22, BiosymMRParser::RuleDihedral_angle_wo_w_constraints);

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
    setState(197); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(196);
              dihedral_angle_wo_w_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(199); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 21, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_wo_w_constraintContext ------------------------------------------------------------------

BiosymMRParser::Dihedral_angle_wo_w_constraintContext::Dihedral_angle_wo_w_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Dihedral_angle_wo_w_constraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_wo_w_constraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Dihedral_angle_wo_w_constraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Dihedral_angle_wo_w_constraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_wo_w_constraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Dihedral_angle_wo_w_constraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleDihedral_angle_wo_w_constraint;
}


std::any BiosymMRParser::Dihedral_angle_wo_w_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_wo_w_constraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Dihedral_angle_wo_w_constraintContext* BiosymMRParser::dihedral_angle_wo_w_constraint() {
  Dihedral_angle_wo_w_constraintContext *_localctx = _tracker.createInstance<Dihedral_angle_wo_w_constraintContext>(_ctx, getState());
  enterRule(_localctx, 24, BiosymMRParser::RuleDihedral_angle_wo_w_constraint);
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
    setState(202);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(201);
      match(BiosymMRParser::Ordinal);
    }
    setState(204);
    match(BiosymMRParser::Atom_selection);
    setState(205);
    match(BiosymMRParser::Atom_selection);
    setState(206);
    match(BiosymMRParser::Atom_selection);
    setState(207);
    match(BiosymMRParser::Atom_selection);
    setState(208);
    number();
    setState(209);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Rdc_restraintsContext ------------------------------------------------------------------

BiosymMRParser::Rdc_restraintsContext::Rdc_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Rdc_restraintContext *> BiosymMRParser::Rdc_restraintsContext::rdc_restraint() {
  return getRuleContexts<BiosymMRParser::Rdc_restraintContext>();
}

BiosymMRParser::Rdc_restraintContext* BiosymMRParser::Rdc_restraintsContext::rdc_restraint(size_t i) {
  return getRuleContext<BiosymMRParser::Rdc_restraintContext>(i);
}


size_t BiosymMRParser::Rdc_restraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleRdc_restraints;
}


std::any BiosymMRParser::Rdc_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitRdc_restraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Rdc_restraintsContext* BiosymMRParser::rdc_restraints() {
  Rdc_restraintsContext *_localctx = _tracker.createInstance<Rdc_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 26, BiosymMRParser::RuleRdc_restraints);

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
    setState(212); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(211);
              rdc_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(214); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Rdc_restraintContext ------------------------------------------------------------------

BiosymMRParser::Rdc_restraintContext::Rdc_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Rdc_restraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Rdc_restraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Rdc_restraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Rdc_restraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

tree::TerminalNode* BiosymMRParser::Rdc_restraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Rdc_restraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleRdc_restraint;
}


std::any BiosymMRParser::Rdc_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitRdc_restraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Rdc_restraintContext* BiosymMRParser::rdc_restraint() {
  Rdc_restraintContext *_localctx = _tracker.createInstance<Rdc_restraintContext>(_ctx, getState());
  enterRule(_localctx, 28, BiosymMRParser::RuleRdc_restraint);
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
    setState(217);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(216);
      match(BiosymMRParser::Ordinal);
    }
    setState(219);
    match(BiosymMRParser::Atom_selection);
    setState(220);
    match(BiosymMRParser::Atom_selection);
    setState(221);
    number();
    setState(222);
    number();
    setState(223);
    number();
    setState(224);
    number();
   
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
  enterRule(_localctx, 30, BiosymMRParser::RuleChirality_constraints);

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
    setState(227); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(226);
              chirality_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(229); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 25, _ctx);
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
  enterRule(_localctx, 32, BiosymMRParser::RuleChirality_constraint);
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
    setState(232);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(231);
      match(BiosymMRParser::Ordinal);
    }
    setState(234);
    match(BiosymMRParser::Atom_selection);
    setState(235);
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
  enterRule(_localctx, 34, BiosymMRParser::RuleProchirality_constraints);

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
    setState(238); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(237);
              prochirality_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(240); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 27, _ctx);
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
  enterRule(_localctx, 36, BiosymMRParser::RuleProchirality_constraint);
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
    setState(243);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(242);
      match(BiosymMRParser::Ordinal);
    }
    setState(245);
    match(BiosymMRParser::Atom_selection);
    setState(246);
    match(BiosymMRParser::Atom_selection);
    setState(247);
    match(BiosymMRParser::Atom_selection);
    setState(248);
    match(BiosymMRParser::Atom_selection);
    setState(249);
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

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::Mixing_times() {
  return getToken(BiosymMRParser::Mixing_times, 0);
}

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::RETURN_MT() {
  return getToken(BiosymMRParser::RETURN_MT, 0);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Mixing_timeContext::Real_MT() {
  return getTokens(BiosymMRParser::Real_MT);
}

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::Real_MT(size_t i) {
  return getToken(BiosymMRParser::Real_MT, i);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Mixing_timeContext::Float_MT() {
  return getTokens(BiosymMRParser::Float_MT);
}

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::Float_MT(size_t i) {
  return getToken(BiosymMRParser::Float_MT, i);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Mixing_timeContext::Integer_MT() {
  return getTokens(BiosymMRParser::Integer_MT);
}

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::Integer_MT(size_t i) {
  return getToken(BiosymMRParser::Integer_MT, i);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Mixing_timeContext::Comma_MT() {
  return getTokens(BiosymMRParser::Comma_MT);
}

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::Comma_MT(size_t i) {
  return getToken(BiosymMRParser::Comma_MT, i);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Mixing_timeContext::Period_MT() {
  return getTokens(BiosymMRParser::Period_MT);
}

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::Period_MT(size_t i) {
  return getToken(BiosymMRParser::Period_MT, i);
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
  enterRule(_localctx, 38, BiosymMRParser::RuleMixing_time);
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
    setState(251);
    match(BiosymMRParser::Mixing_times);
    setState(258);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1879048192) != 0)) {
      setState(252);
      _la = _input->LA(1);
      if (!((((_la & ~ 0x3fULL) == 0) &&
        ((1ULL << _la) & 1879048192) != 0))) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(254);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == BiosymMRParser::Comma_MT

      || _la == BiosymMRParser::Period_MT) {
        setState(253);
        _la = _input->LA(1);
        if (!(_la == BiosymMRParser::Comma_MT

        || _la == BiosymMRParser::Period_MT)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
      }
      setState(260);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(261);
    match(BiosymMRParser::RETURN_MT);
   
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
  enterRule(_localctx, 40, BiosymMRParser::RuleNumber);
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
    setState(263);
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
  enterRule(_localctx, 42, BiosymMRParser::RuleIns_distance_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(265);
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
  enterRule(_localctx, 44, BiosymMRParser::RuleIns_distance_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(267);
    decl_create();
    setState(268);
    decl_function();
    setState(269);
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
  enterRule(_localctx, 46, BiosymMRParser::RuleDecl_create);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(271);
    match(BiosymMRParser::Restraint);
    setState(272);
    match(BiosymMRParser::Create);
    setState(273);
    match(BiosymMRParser::Double_quote_string);
    setState(274);
    match(BiosymMRParser::Distance);
    setState(275);
    match(BiosymMRParser::Double_quote_string);
    setState(276);
    match(BiosymMRParser::Double_quote_string);
    setState(277);
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
  enterRule(_localctx, 48, BiosymMRParser::RuleDecl_function);
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
    setState(279);
    match(BiosymMRParser::Restraint);
    setState(280);
    match(BiosymMRParser::Function);
    setState(281);
    match(BiosymMRParser::Double_quote_string);
    setState(282);
    _la = _input->LA(1);
    if (!(_la == BiosymMRParser::Quadratic

    || _la == BiosymMRParser::Flat_bottomed)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(283);
    match(BiosymMRParser::Double_quote_string);
    setState(284);
    match(BiosymMRParser::Double_quote_string);
    setState(286);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Double_quote_string) {
      setState(285);
      match(BiosymMRParser::Double_quote_string);
    }
    setState(288);
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
  enterRule(_localctx, 50, BiosymMRParser::RuleDecl_target);
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
    setState(290);
    match(BiosymMRParser::Restraint);
    setState(291);
    match(BiosymMRParser::Target);
    setState(292);
    match(BiosymMRParser::Double_quote_string);
    setState(293);
    _la = _input->LA(1);
    if (!(_la == BiosymMRParser::Double_quote_string

    || _la == BiosymMRParser::Relative)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(294);
    match(BiosymMRParser::Double_quote_string);
    setState(295);
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
