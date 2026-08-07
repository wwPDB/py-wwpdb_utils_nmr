
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CharmmMRParser.g4 by ANTLR 4.13.0


#include "CharmmMRParserVisitor.h"

#include "CharmmMRParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct CharmmMRParserStaticData final {
  CharmmMRParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  CharmmMRParserStaticData(const CharmmMRParserStaticData&) = delete;
  CharmmMRParserStaticData(CharmmMRParserStaticData&&) = delete;
  CharmmMRParserStaticData& operator=(const CharmmMRParserStaticData&) = delete;
  CharmmMRParserStaticData& operator=(CharmmMRParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag charmmmrparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
CharmmMRParserStaticData *charmmmrparserParserStaticData = nullptr;

void charmmmrparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (charmmmrparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(charmmmrparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<CharmmMRParserStaticData>(
    std::vector<std::string>{
      "charmm_mr", "comment", "distance_restraint", "point_distance_restraint", 
      "dihedral_angle_restraint", "harmonic_restraint", "manipulate_internal_coordinate", 
      "droplet_potential", "fix_atom_constraint", "center_of_mass_constraint", 
      "fix_bond_or_angle_constraint", "restrained_distance", "external_force", 
      "rmsd_restraint", "gyration_restraint", "distance_matrix_restraint", 
      "noe_statement", "noe_assign", "pnoe_statement", "pnoe_assign", "dihedral_statement", 
      "dihedral_assign", "harmonic_statement", "absolute_spec", "force_const_spec", 
      "bestfit_spec", "coordinate_spec", "ic_statement", "droplet_statement", 
      "fix_atom_statement", "center_of_mass_statement", "fix_bond_or_angle_statement", 
      "shake_opt", "fast_opt", "restrained_distance_statement", "external_force_statement", 
      "rmsd_statement", "rmsd_orient_spec", "rmsd_force_const_spec", "rmsd_coordinate_spec", 
      "gyration_statement", "distance_matrix_statement", "selection", "selection_expression", 
      "term", "factor", "number", "number_f", "number_s", "set_statement"
    },
    std::vector<std::string>{
      "", "'SET'", "'END'", "", "", "", "", "", "", "", "'MASS'", "", "", 
      "", "", "", "", "", "'MAIN'", "'COMP'", "'KEEP'", "", "", "'MIN'", 
      "", "", "'CLDH'", "'IC'", "'BOND'", "", "", "", "", "", "'FIX'", "'PURG'", 
      "'THET'", "'PHI'", "'IMPH'", "'HMCM'", "'REFX'", "'REFY'", "'REFZ'", 
      "", "'OFF'", "", "'BONH'", "'TOL'", "", "'ANGH'", "", "", "'FAST'", 
      "", "", "'NOE'", "", "'PNOE'", "", "'KMIN'", "'KMAX'", "'RMIN'", "'RMAX'", 
      "'FMAX'", "'MINDIST'", "'RSWI'", "'SEXP'", "'SUMR'", "'TCON'", "'REXP'", 
      "'CNOX'", "'CNOY'", "'CNOZ'", "", "'INOE'", "'TNOX'", "'TNOY'", "'TNOZ'", 
      "", "'READ'", "", "'UNIT'", "", "'ANAL'", "'CUT'", "", "", "", "'KVAL'", 
      "'RVAL'", "'EVAL'", "'IVAL'", "", "", "'PULL'", "'XDIR'", "'YDIR'", 
      "'ZDIR'", "", "'LIST'", "", "", "'RMSD'", "'MAXN'", "'NPRT'", "'SHOW'", 
      "", "", "", "", "", "", "", "", "", "", "", "'.OR.'", "'.AND.'", "'.NOT.'", 
      "'.AROUND.'", "'.SUBSET.'", "'.BONDED.'", "'.BYRES.'", "'.BYGROUP.'", 
      "", "'ISEG'", "", "'IRES'", "", "", "'TYPE'", "", "'ATOM'", "", "", 
      "", "'LONE'", "", "'USER'", "", "", "'ALL'", "'NONE'", "", "", "", 
      "", "", "", "", "", "'('", "')'", "':'", "'.EQ.'", "'.LT.'", "'.GT.'", 
      "'.LE.'", "'.GE.'", "'.NE.'", "'.AE.'", "", "", "", "", "", "", "'='", 
      "", "", "", "", "", "", "", "", "'ABS'"
    },
    std::vector<std::string>{
      "", "Set", "End", "Cons", "Harmonic", "Absolute", "Bestfit", "Relative", 
      "Clear", "Force", "Mass", "Weight", "Exponent", "XScale", "YScale", 
      "ZScale", "NoRotation", "NoTranslation", "Main", "Comp", "Keep", "Dihedral", 
      "ByNumber", "Min", "Period", "Width", "ClDh", "IC", "Bond", "Upper", 
      "Angle", "Improper", "Droplet", "NoMass", "Fix", "Purg", "Thet", "Phi", 
      "Imph", "Hmcm", "RefX", "RefY", "RefZ", "Shake", "Off", "NoReset", 
      "BonH", "Tol", "MxIter", "AngH", "Parameters", "ShkScale", "Fast", 
      "Water", "NoFast", "Noe", "Reset", "PNoe", "Assign", "KMin", "KMax", 
      "RMin", "RMax", "FMax", "MinDist", "RSwi", "SExp", "SumR", "TCon", 
      "RExp", "CnoX", "CnoY", "CnoZ", "MPNoe", "INoe", "TnoX", "TnoY", "TnoZ", 
      "NMPNoe", "Read", "Write", "Unit", "Print", "Anal", "Cut", "Scale", 
      "Temperature", "ResDistance", "KVal", "RVal", "EVal", "IVal", "Positive", 
      "Negative", "Pull", "XDir", "YDir", "ZDir", "EField", "List", "Switch", 
      "SForce", "RMSD", "MaxN", "NPrt", "Show", "Offset", "BOffset", "RGyration", 
      "Reference", "Orient", "Output", "NSave", "DMConstrain", "Cutoff", 
      "NContact", "Selection", "Or_op", "And_op", "Not_op", "Around", "Subset", 
      "Bonded", "ByRes", "ByGroup", "SegIdentifier", "ISeg", "Residue", 
      "IRes", "Resname", "IGroup", "Type", "Chemical", "Atom", "Property", 
      "Point", "Initial", "Lone", "Hydrogen", "User", "Previous", "Recall", 
      "All", "NONE", "Integer", "Real", "Double_quote_string", "SMCLN_COMMENT", 
      "COMMENT", "Simple_name", "Simple_names", "Integers", "L_paren", "R_paren", 
      "Colon", "Equ_op", "Lt_op", "Gt_op", "Leq_op", "Geq_op", "Neq_op", 
      "Aeq_op", "Symbol_name", "SPACE", "CONTINUE", "ENCLOSE_COMMENT", "SECTION_COMMENT", 
      "LINE_COMMENT", "Equ_op_VE", "Integer_VE", "Real_VE", "Simple_name_VE", 
      "SPACE_VE", "RETURN_VE", "Any_name", "SPACE_CM", "RETURN_CM", "Abs", 
      "Attr_properties", "Comparison_ops", "SPACE_AP"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,180,828,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,
  	35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,
  	42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,
  	49,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,
  	0,117,8,0,10,0,12,0,120,9,0,1,0,1,0,1,1,1,1,5,1,126,8,1,10,1,12,1,129,
  	9,1,1,1,1,1,1,2,1,2,5,2,135,8,2,10,2,12,2,138,9,2,1,2,1,2,1,3,1,3,5,3,
  	144,8,3,10,3,12,3,147,9,3,1,3,1,3,1,4,1,4,1,4,5,4,154,8,4,10,4,12,4,157,
  	9,4,1,4,3,4,160,8,4,1,5,1,5,1,5,5,5,165,8,5,10,5,12,5,168,9,5,1,6,1,6,
  	1,6,5,6,173,8,6,10,6,12,6,176,9,6,1,7,1,7,1,7,5,7,181,8,7,10,7,12,7,184,
  	9,7,1,8,1,8,1,8,5,8,189,8,8,10,8,12,8,192,9,8,1,9,1,9,1,9,5,9,197,8,9,
  	10,9,12,9,200,9,9,1,10,1,10,5,10,204,8,10,10,10,12,10,207,9,10,1,10,3,
  	10,210,8,10,1,11,1,11,5,11,214,8,11,10,11,12,11,217,9,11,1,12,1,12,5,
  	12,221,8,12,10,12,12,12,224,9,12,1,13,1,13,1,13,5,13,229,8,13,10,13,12,
  	13,232,9,13,1,13,1,13,3,13,236,8,13,1,14,1,14,5,14,240,8,14,10,14,12,
  	14,243,9,14,1,15,1,15,5,15,247,8,15,10,15,12,15,250,9,15,1,16,1,16,1,
  	16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
  	16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
  	16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,293,8,16,1,
  	16,1,16,1,16,1,16,3,16,299,8,16,3,16,301,8,16,1,16,1,16,1,16,1,16,3,16,
  	307,8,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
  	1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
  	1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
  	1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,360,8,18,
  	1,18,1,18,1,18,1,18,3,18,366,8,18,3,18,368,8,18,1,18,1,18,1,18,1,18,3,
  	18,374,8,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
  	20,1,20,1,20,3,20,390,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
  	21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,411,8,21,1,
  	21,1,21,1,21,3,21,416,8,21,1,21,1,21,1,21,3,21,421,8,21,1,21,1,21,1,21,
  	3,21,426,8,21,1,21,1,21,3,21,430,8,21,1,22,3,22,433,8,22,1,22,5,22,436,
  	8,22,10,22,12,22,439,9,22,1,22,5,22,442,8,22,10,22,12,22,445,9,22,1,22,
  	1,22,5,22,449,8,22,10,22,12,22,452,9,22,1,22,3,22,455,8,22,1,22,1,22,
  	3,22,459,8,22,1,22,5,22,462,8,22,10,22,12,22,465,9,22,1,22,3,22,468,8,
  	22,1,22,1,22,3,22,472,8,22,1,22,5,22,475,8,22,10,22,12,22,478,9,22,1,
  	22,1,22,5,22,482,8,22,10,22,12,22,485,9,22,1,22,1,22,1,22,3,22,490,8,
  	22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,500,8,23,1,24,1,24,1,
  	24,1,24,3,24,506,8,24,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,27,3,27,516,
  	8,27,1,27,3,27,519,8,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,527,8,27,1,
  	28,1,28,1,28,1,28,1,28,3,28,534,8,28,1,29,1,29,3,29,538,8,29,1,29,3,29,
  	541,8,29,1,29,3,29,544,8,29,1,29,3,29,547,8,29,1,29,3,29,550,8,29,1,30,
  	1,30,1,30,3,30,555,8,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,
  	1,31,1,31,1,31,1,31,1,31,3,31,571,8,31,1,32,1,32,3,32,575,8,32,1,32,1,
  	32,3,32,579,8,32,1,32,1,32,3,32,583,8,32,1,32,1,32,3,32,587,8,32,1,32,
  	1,32,3,32,591,8,32,1,33,1,33,1,33,3,33,596,8,33,1,33,3,33,599,8,33,1,
  	34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,3,34,611,8,34,1,35,1,
  	35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,623,8,35,1,36,1,36,1,
  	36,1,36,1,36,1,36,1,36,1,36,3,36,633,8,36,1,37,1,37,1,38,1,38,1,38,1,
  	38,1,38,1,38,1,38,3,38,644,8,38,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,
  	40,1,40,1,40,1,40,3,40,657,8,40,1,41,1,41,1,41,1,41,1,41,3,41,664,8,41,
  	1,42,1,42,1,42,3,42,669,8,42,1,42,1,42,1,43,1,43,1,43,5,43,676,8,43,10,
  	43,12,43,679,9,43,1,44,1,44,1,44,5,44,684,8,44,10,44,12,44,687,9,44,1,
  	45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,3,45,701,8,
  	45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,
  	45,3,45,717,8,45,1,45,3,45,720,8,45,1,45,1,45,1,45,1,45,1,45,3,45,727,
  	8,45,1,45,3,45,730,8,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,
  	1,45,1,45,1,45,3,45,744,8,45,1,45,3,45,747,8,45,1,45,1,45,1,45,1,45,1,
  	45,1,45,1,45,1,45,1,45,3,45,758,8,45,1,45,3,45,761,8,45,1,45,1,45,1,45,
  	1,45,1,45,3,45,768,8,45,1,45,3,45,771,8,45,1,45,1,45,1,45,1,45,1,45,3,
  	45,778,8,45,1,45,1,45,1,45,3,45,783,8,45,1,45,1,45,3,45,787,8,45,1,45,
  	1,45,1,45,1,45,3,45,793,8,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,
  	1,45,3,45,804,8,45,1,45,3,45,807,8,45,5,45,809,8,45,10,45,12,45,812,9,
  	45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,49,3,49,823,8,49,1,49,1,
  	49,1,49,1,49,0,1,90,50,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
  	34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
  	80,82,84,86,88,90,92,94,96,98,0,19,1,1,176,176,1,0,16,17,1,0,18,20,4,
  	0,28,28,30,30,46,46,49,49,2,0,85,85,88,89,1,0,90,91,3,0,24,24,95,98,101,
  	101,1,0,18,19,2,0,9,9,109,109,1,0,111,112,4,0,9,9,11,11,109,109,114,114,
  	2,0,111,112,115,115,1,0,149,150,2,0,144,144,151,151,2,0,22,22,127,127,
  	3,0,126,126,128,128,130,130,2,0,144,145,162,162,1,0,144,145,1,0,169,171,
  	993,0,118,1,0,0,0,2,123,1,0,0,0,4,132,1,0,0,0,6,141,1,0,0,0,8,150,1,0,
  	0,0,10,161,1,0,0,0,12,169,1,0,0,0,14,177,1,0,0,0,16,185,1,0,0,0,18,193,
  	1,0,0,0,20,201,1,0,0,0,22,211,1,0,0,0,24,218,1,0,0,0,26,225,1,0,0,0,28,
  	237,1,0,0,0,30,244,1,0,0,0,32,306,1,0,0,0,34,308,1,0,0,0,36,373,1,0,0,
  	0,38,375,1,0,0,0,40,389,1,0,0,0,42,429,1,0,0,0,44,489,1,0,0,0,46,499,
  	1,0,0,0,48,505,1,0,0,0,50,507,1,0,0,0,52,509,1,0,0,0,54,526,1,0,0,0,56,
  	533,1,0,0,0,58,535,1,0,0,0,60,551,1,0,0,0,62,570,1,0,0,0,64,572,1,0,0,
  	0,66,598,1,0,0,0,68,610,1,0,0,0,70,622,1,0,0,0,72,632,1,0,0,0,74,634,
  	1,0,0,0,76,643,1,0,0,0,78,645,1,0,0,0,80,656,1,0,0,0,82,663,1,0,0,0,84,
  	665,1,0,0,0,86,672,1,0,0,0,88,680,1,0,0,0,90,792,1,0,0,0,92,813,1,0,0,
  	0,94,815,1,0,0,0,96,817,1,0,0,0,98,819,1,0,0,0,100,117,3,2,1,0,101,117,
  	3,4,2,0,102,117,3,6,3,0,103,117,3,8,4,0,104,117,3,10,5,0,105,117,3,12,
  	6,0,106,117,3,14,7,0,107,117,3,16,8,0,108,117,3,18,9,0,109,117,3,20,10,
  	0,110,117,3,22,11,0,111,117,3,24,12,0,112,117,3,26,13,0,113,117,3,28,
  	14,0,114,117,3,30,15,0,115,117,3,98,49,0,116,100,1,0,0,0,116,101,1,0,
  	0,0,116,102,1,0,0,0,116,103,1,0,0,0,116,104,1,0,0,0,116,105,1,0,0,0,116,
  	106,1,0,0,0,116,107,1,0,0,0,116,108,1,0,0,0,116,109,1,0,0,0,116,110,1,
  	0,0,0,116,111,1,0,0,0,116,112,1,0,0,0,116,113,1,0,0,0,116,114,1,0,0,0,
  	116,115,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,121,
  	1,0,0,0,120,118,1,0,0,0,121,122,5,0,0,1,122,1,1,0,0,0,123,127,5,148,0,
  	0,124,126,5,174,0,0,125,124,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,
  	128,1,0,0,0,128,130,1,0,0,0,129,127,1,0,0,0,130,131,7,0,0,0,131,3,1,0,
  	0,0,132,136,5,55,0,0,133,135,3,32,16,0,134,133,1,0,0,0,135,138,1,0,0,
  	0,136,134,1,0,0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,136,1,0,0,0,139,
  	140,5,2,0,0,140,5,1,0,0,0,141,145,5,57,0,0,142,144,3,36,18,0,143,142,
  	1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,148,1,0,0,
  	0,147,145,1,0,0,0,148,149,5,2,0,0,149,7,1,0,0,0,150,159,5,3,0,0,151,155,
  	5,21,0,0,152,154,3,40,20,0,153,152,1,0,0,0,154,157,1,0,0,0,155,153,1,
  	0,0,0,155,156,1,0,0,0,156,160,1,0,0,0,157,155,1,0,0,0,158,160,5,26,0,
  	0,159,151,1,0,0,0,159,158,1,0,0,0,160,9,1,0,0,0,161,162,5,3,0,0,162,166,
  	5,4,0,0,163,165,3,44,22,0,164,163,1,0,0,0,165,168,1,0,0,0,166,164,1,0,
  	0,0,166,167,1,0,0,0,167,11,1,0,0,0,168,166,1,0,0,0,169,170,5,3,0,0,170,
  	174,5,27,0,0,171,173,3,54,27,0,172,171,1,0,0,0,173,176,1,0,0,0,174,172,
  	1,0,0,0,174,175,1,0,0,0,175,13,1,0,0,0,176,174,1,0,0,0,177,178,5,3,0,
  	0,178,182,5,32,0,0,179,181,3,56,28,0,180,179,1,0,0,0,181,184,1,0,0,0,
  	182,180,1,0,0,0,182,183,1,0,0,0,183,15,1,0,0,0,184,182,1,0,0,0,185,186,
  	5,3,0,0,186,190,5,34,0,0,187,189,3,58,29,0,188,187,1,0,0,0,189,192,1,
  	0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,17,1,0,0,0,192,190,1,0,0,0,
  	193,194,5,3,0,0,194,198,5,39,0,0,195,197,3,60,30,0,196,195,1,0,0,0,197,
  	200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,19,1,0,0,0,200,198,1,
  	0,0,0,201,209,5,43,0,0,202,204,3,62,31,0,203,202,1,0,0,0,204,207,1,0,
  	0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,210,1,0,0,0,207,205,1,0,0,0,208,
  	210,5,44,0,0,209,205,1,0,0,0,209,208,1,0,0,0,210,21,1,0,0,0,211,215,5,
  	87,0,0,212,214,3,68,34,0,213,212,1,0,0,0,214,217,1,0,0,0,215,213,1,0,
  	0,0,215,216,1,0,0,0,216,23,1,0,0,0,217,215,1,0,0,0,218,222,5,94,0,0,219,
  	221,3,70,35,0,220,219,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,
  	1,0,0,0,223,25,1,0,0,0,224,222,1,0,0,0,225,226,5,3,0,0,226,235,5,102,
  	0,0,227,229,3,72,36,0,228,227,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,
  	230,231,1,0,0,0,231,236,1,0,0,0,232,230,1,0,0,0,233,236,5,105,0,0,234,
  	236,5,8,0,0,235,230,1,0,0,0,235,233,1,0,0,0,235,234,1,0,0,0,236,27,1,
  	0,0,0,237,241,5,108,0,0,238,240,3,80,40,0,239,238,1,0,0,0,240,243,1,0,
  	0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,29,1,0,0,0,243,241,1,0,0,0,244,
  	248,5,113,0,0,245,247,3,82,41,0,246,245,1,0,0,0,247,250,1,0,0,0,248,246,
  	1,0,0,0,248,249,1,0,0,0,249,31,1,0,0,0,250,248,1,0,0,0,251,307,3,34,17,
  	0,252,307,5,56,0,0,253,254,5,59,0,0,254,307,3,96,48,0,255,256,5,61,0,
  	0,256,307,3,96,48,0,257,258,5,60,0,0,258,307,3,96,48,0,259,260,5,62,0,
  	0,260,307,3,96,48,0,261,262,5,63,0,0,262,307,3,96,48,0,263,307,5,64,0,
  	0,264,265,5,65,0,0,265,307,3,96,48,0,266,267,5,66,0,0,267,307,3,96,48,
  	0,268,307,5,67,0,0,269,270,5,68,0,0,270,307,3,96,48,0,271,272,5,69,0,
  	0,272,307,3,96,48,0,273,274,5,73,0,0,274,275,5,74,0,0,275,276,5,144,0,
  	0,276,277,5,75,0,0,277,278,3,96,48,0,278,279,5,76,0,0,279,280,3,96,48,
  	0,280,281,5,77,0,0,281,282,3,96,48,0,282,307,1,0,0,0,283,284,5,78,0,0,
  	284,307,5,144,0,0,285,286,5,79,0,0,286,287,5,81,0,0,287,307,5,144,0,0,
  	288,289,5,80,0,0,289,290,5,81,0,0,290,292,5,144,0,0,291,293,5,83,0,0,
  	292,291,1,0,0,0,292,293,1,0,0,0,293,307,1,0,0,0,294,300,5,82,0,0,295,
  	298,5,83,0,0,296,297,5,84,0,0,297,299,3,96,48,0,298,296,1,0,0,0,298,299,
  	1,0,0,0,299,301,1,0,0,0,300,295,1,0,0,0,300,301,1,0,0,0,301,307,1,0,0,
  	0,302,303,5,85,0,0,303,307,3,96,48,0,304,305,5,86,0,0,305,307,3,96,48,
  	0,306,251,1,0,0,0,306,252,1,0,0,0,306,253,1,0,0,0,306,255,1,0,0,0,306,
  	257,1,0,0,0,306,259,1,0,0,0,306,261,1,0,0,0,306,263,1,0,0,0,306,264,1,
  	0,0,0,306,266,1,0,0,0,306,268,1,0,0,0,306,269,1,0,0,0,306,271,1,0,0,0,
  	306,273,1,0,0,0,306,283,1,0,0,0,306,285,1,0,0,0,306,288,1,0,0,0,306,294,
  	1,0,0,0,306,302,1,0,0,0,306,304,1,0,0,0,307,33,1,0,0,0,308,309,5,58,0,
  	0,309,310,3,84,42,0,310,311,3,84,42,0,311,35,1,0,0,0,312,374,3,38,19,
  	0,313,374,5,56,0,0,314,315,5,59,0,0,315,374,3,96,48,0,316,317,5,61,0,
  	0,317,374,3,96,48,0,318,319,5,60,0,0,319,374,3,96,48,0,320,321,5,62,0,
  	0,321,374,3,96,48,0,322,323,5,63,0,0,323,374,3,96,48,0,324,325,5,70,0,
  	0,325,374,3,96,48,0,326,327,5,71,0,0,327,374,3,96,48,0,328,329,5,72,0,
  	0,329,374,3,96,48,0,330,374,5,64,0,0,331,332,5,65,0,0,332,374,3,96,48,
  	0,333,334,5,66,0,0,334,374,3,96,48,0,335,374,5,67,0,0,336,337,5,68,0,
  	0,337,374,3,96,48,0,338,339,5,69,0,0,339,374,3,96,48,0,340,341,5,73,0,
  	0,341,342,5,74,0,0,342,343,5,144,0,0,343,344,5,75,0,0,344,345,3,96,48,
  	0,345,346,5,76,0,0,346,347,3,96,48,0,347,348,5,77,0,0,348,349,3,96,48,
  	0,349,374,1,0,0,0,350,351,5,78,0,0,351,374,5,144,0,0,352,353,5,79,0,0,
  	353,354,5,81,0,0,354,374,5,144,0,0,355,356,5,80,0,0,356,357,5,81,0,0,
  	357,359,5,144,0,0,358,360,5,83,0,0,359,358,1,0,0,0,359,360,1,0,0,0,360,
  	374,1,0,0,0,361,367,5,82,0,0,362,365,5,83,0,0,363,364,5,84,0,0,364,366,
  	3,96,48,0,365,363,1,0,0,0,365,366,1,0,0,0,366,368,1,0,0,0,367,362,1,0,
  	0,0,367,368,1,0,0,0,368,374,1,0,0,0,369,370,5,85,0,0,370,374,3,96,48,
  	0,371,372,5,86,0,0,372,374,3,96,48,0,373,312,1,0,0,0,373,313,1,0,0,0,
  	373,314,1,0,0,0,373,316,1,0,0,0,373,318,1,0,0,0,373,320,1,0,0,0,373,322,
  	1,0,0,0,373,324,1,0,0,0,373,326,1,0,0,0,373,328,1,0,0,0,373,330,1,0,0,
  	0,373,331,1,0,0,0,373,333,1,0,0,0,373,335,1,0,0,0,373,336,1,0,0,0,373,
  	338,1,0,0,0,373,340,1,0,0,0,373,350,1,0,0,0,373,352,1,0,0,0,373,355,1,
  	0,0,0,373,361,1,0,0,0,373,369,1,0,0,0,373,371,1,0,0,0,374,37,1,0,0,0,
  	375,376,5,58,0,0,376,377,3,84,42,0,377,39,1,0,0,0,378,390,3,42,21,0,379,
  	380,5,9,0,0,380,390,3,96,48,0,381,382,5,23,0,0,382,390,3,96,48,0,383,
  	384,5,24,0,0,384,390,5,144,0,0,385,390,5,19,0,0,386,387,5,25,0,0,387,
  	390,3,96,48,0,388,390,5,18,0,0,389,378,1,0,0,0,389,379,1,0,0,0,389,381,
  	1,0,0,0,389,383,1,0,0,0,389,385,1,0,0,0,389,386,1,0,0,0,389,388,1,0,0,
  	0,390,41,1,0,0,0,391,392,3,84,42,0,392,393,3,84,42,0,393,394,3,84,42,
  	0,394,395,3,84,42,0,395,430,1,0,0,0,396,397,5,22,0,0,397,398,5,144,0,
  	0,398,399,5,144,0,0,399,400,5,144,0,0,400,430,5,144,0,0,401,402,5,144,
  	0,0,402,403,5,149,0,0,403,404,5,144,0,0,404,405,5,149,0,0,405,406,5,144,
  	0,0,406,407,5,149,0,0,407,408,5,144,0,0,408,430,5,149,0,0,409,411,5,149,
  	0,0,410,409,1,0,0,0,410,411,1,0,0,0,411,412,1,0,0,0,412,413,5,144,0,0,
  	413,415,5,149,0,0,414,416,5,149,0,0,415,414,1,0,0,0,415,416,1,0,0,0,416,
  	417,1,0,0,0,417,418,5,144,0,0,418,420,5,149,0,0,419,421,5,149,0,0,420,
  	419,1,0,0,0,420,421,1,0,0,0,421,422,1,0,0,0,422,423,5,144,0,0,423,425,
  	5,149,0,0,424,426,5,149,0,0,425,424,1,0,0,0,425,426,1,0,0,0,426,427,1,
  	0,0,0,427,428,5,144,0,0,428,430,5,149,0,0,429,391,1,0,0,0,429,396,1,0,
  	0,0,429,401,1,0,0,0,429,410,1,0,0,0,430,43,1,0,0,0,431,433,5,5,0,0,432,
  	431,1,0,0,0,432,433,1,0,0,0,433,437,1,0,0,0,434,436,3,46,23,0,435,434,
  	1,0,0,0,436,439,1,0,0,0,437,435,1,0,0,0,437,438,1,0,0,0,438,443,1,0,0,
  	0,439,437,1,0,0,0,440,442,3,48,24,0,441,440,1,0,0,0,442,445,1,0,0,0,443,
  	441,1,0,0,0,443,444,1,0,0,0,444,446,1,0,0,0,445,443,1,0,0,0,446,450,3,
  	84,42,0,447,449,3,48,24,0,448,447,1,0,0,0,449,452,1,0,0,0,450,448,1,0,
  	0,0,450,451,1,0,0,0,451,454,1,0,0,0,452,450,1,0,0,0,453,455,3,52,26,0,
  	454,453,1,0,0,0,454,455,1,0,0,0,455,490,1,0,0,0,456,458,5,6,0,0,457,459,
  	3,50,25,0,458,457,1,0,0,0,458,459,1,0,0,0,459,463,1,0,0,0,460,462,3,48,
  	24,0,461,460,1,0,0,0,462,465,1,0,0,0,463,461,1,0,0,0,463,464,1,0,0,0,
  	464,467,1,0,0,0,465,463,1,0,0,0,466,468,3,52,26,0,467,466,1,0,0,0,467,
  	468,1,0,0,0,468,490,1,0,0,0,469,471,5,7,0,0,470,472,3,50,25,0,471,470,
  	1,0,0,0,471,472,1,0,0,0,472,476,1,0,0,0,473,475,3,48,24,0,474,473,1,0,
  	0,0,475,478,1,0,0,0,476,474,1,0,0,0,476,477,1,0,0,0,477,479,1,0,0,0,478,
  	476,1,0,0,0,479,483,3,84,42,0,480,482,3,48,24,0,481,480,1,0,0,0,482,485,
  	1,0,0,0,483,481,1,0,0,0,483,484,1,0,0,0,484,486,1,0,0,0,485,483,1,0,0,
  	0,486,487,3,84,42,0,487,490,1,0,0,0,488,490,5,8,0,0,489,432,1,0,0,0,489,
  	456,1,0,0,0,489,469,1,0,0,0,489,488,1,0,0,0,490,45,1,0,0,0,491,492,5,
  	12,0,0,492,500,5,144,0,0,493,494,5,13,0,0,494,500,3,92,46,0,495,496,5,
  	14,0,0,496,500,3,92,46,0,497,498,5,15,0,0,498,500,3,92,46,0,499,491,1,
  	0,0,0,499,493,1,0,0,0,499,495,1,0,0,0,499,497,1,0,0,0,500,47,1,0,0,0,
  	501,502,5,9,0,0,502,506,3,92,46,0,503,506,5,10,0,0,504,506,5,11,0,0,505,
  	501,1,0,0,0,505,503,1,0,0,0,505,504,1,0,0,0,506,49,1,0,0,0,507,508,7,
  	1,0,0,508,51,1,0,0,0,509,510,7,2,0,0,510,53,1,0,0,0,511,512,5,28,0,0,
  	512,515,3,92,46,0,513,514,5,12,0,0,514,516,5,144,0,0,515,513,1,0,0,0,
  	515,516,1,0,0,0,516,518,1,0,0,0,517,519,5,29,0,0,518,517,1,0,0,0,518,
  	519,1,0,0,0,519,527,1,0,0,0,520,521,5,30,0,0,521,527,3,92,46,0,522,523,
  	5,21,0,0,523,527,3,92,46,0,524,525,5,31,0,0,525,527,3,92,46,0,526,511,
  	1,0,0,0,526,520,1,0,0,0,526,522,1,0,0,0,526,524,1,0,0,0,527,55,1,0,0,
  	0,528,529,5,9,0,0,529,534,3,92,46,0,530,531,5,12,0,0,531,534,5,144,0,
  	0,532,534,5,33,0,0,533,528,1,0,0,0,533,530,1,0,0,0,533,532,1,0,0,0,534,
  	57,1,0,0,0,535,537,3,84,42,0,536,538,5,35,0,0,537,536,1,0,0,0,537,538,
  	1,0,0,0,538,540,1,0,0,0,539,541,5,28,0,0,540,539,1,0,0,0,540,541,1,0,
  	0,0,541,543,1,0,0,0,542,544,5,36,0,0,543,542,1,0,0,0,543,544,1,0,0,0,
  	544,546,1,0,0,0,545,547,5,37,0,0,546,545,1,0,0,0,546,547,1,0,0,0,547,
  	549,1,0,0,0,548,550,5,38,0,0,549,548,1,0,0,0,549,550,1,0,0,0,550,59,1,
  	0,0,0,551,552,5,9,0,0,552,554,3,92,46,0,553,555,5,11,0,0,554,553,1,0,
  	0,0,554,555,1,0,0,0,555,556,1,0,0,0,556,557,5,40,0,0,557,558,3,92,46,
  	0,558,559,5,41,0,0,559,560,3,92,46,0,560,561,5,42,0,0,561,562,3,92,46,
  	0,562,563,3,84,42,0,563,61,1,0,0,0,564,565,3,84,42,0,565,566,3,84,42,
  	0,566,567,3,64,32,0,567,571,1,0,0,0,568,571,3,66,33,0,569,571,5,45,0,
  	0,570,564,1,0,0,0,570,568,1,0,0,0,570,569,1,0,0,0,571,63,1,0,0,0,572,
  	578,7,3,0,0,573,575,5,18,0,0,574,573,1,0,0,0,574,575,1,0,0,0,575,579,
  	1,0,0,0,576,579,5,19,0,0,577,579,5,50,0,0,578,574,1,0,0,0,578,576,1,0,
  	0,0,578,577,1,0,0,0,579,582,1,0,0,0,580,581,5,47,0,0,581,583,3,92,46,
  	0,582,580,1,0,0,0,582,583,1,0,0,0,583,586,1,0,0,0,584,585,5,48,0,0,585,
  	587,5,144,0,0,586,584,1,0,0,0,586,587,1,0,0,0,587,590,1,0,0,0,588,589,
  	5,51,0,0,589,591,3,92,46,0,590,588,1,0,0,0,590,591,1,0,0,0,591,65,1,0,
  	0,0,592,595,5,52,0,0,593,594,5,53,0,0,594,596,5,149,0,0,595,593,1,0,0,
  	0,595,596,1,0,0,0,596,599,1,0,0,0,597,599,5,54,0,0,598,592,1,0,0,0,598,
  	597,1,0,0,0,599,67,1,0,0,0,600,611,5,56,0,0,601,602,7,4,0,0,602,611,3,
  	92,46,0,603,604,7,5,0,0,604,611,5,144,0,0,605,611,5,92,0,0,606,611,5,
  	93,0,0,607,608,3,84,42,0,608,609,3,84,42,0,609,611,1,0,0,0,610,600,1,
  	0,0,0,610,601,1,0,0,0,610,603,1,0,0,0,610,605,1,0,0,0,610,606,1,0,0,0,
  	610,607,1,0,0,0,611,69,1,0,0,0,612,613,5,9,0,0,613,623,3,92,46,0,614,
  	615,7,6,0,0,615,623,3,92,46,0,616,623,5,44,0,0,617,623,5,99,0,0,618,619,
  	5,100,0,0,619,623,5,144,0,0,620,623,5,11,0,0,621,623,3,84,42,0,622,612,
  	1,0,0,0,622,614,1,0,0,0,622,616,1,0,0,0,622,617,1,0,0,0,622,618,1,0,0,
  	0,622,620,1,0,0,0,622,621,1,0,0,0,623,71,1,0,0,0,624,633,5,7,0,0,625,
  	626,5,103,0,0,626,633,5,144,0,0,627,633,5,104,0,0,628,633,3,74,37,0,629,
  	633,3,76,38,0,630,633,3,78,39,0,631,633,3,84,42,0,632,624,1,0,0,0,632,
  	625,1,0,0,0,632,627,1,0,0,0,632,628,1,0,0,0,632,629,1,0,0,0,632,630,1,
  	0,0,0,632,631,1,0,0,0,633,73,1,0,0,0,634,635,7,1,0,0,635,75,1,0,0,0,636,
  	637,5,9,0,0,637,644,3,92,46,0,638,644,5,10,0,0,639,640,5,106,0,0,640,
  	644,3,92,46,0,641,642,5,107,0,0,642,644,3,92,46,0,643,636,1,0,0,0,643,
  	638,1,0,0,0,643,639,1,0,0,0,643,641,1,0,0,0,644,77,1,0,0,0,645,646,7,
  	7,0,0,646,79,1,0,0,0,647,657,5,56,0,0,648,649,7,8,0,0,649,657,3,92,46,
  	0,650,657,5,102,0,0,651,657,5,19,0,0,652,657,5,110,0,0,653,654,7,9,0,
  	0,654,657,5,144,0,0,655,657,3,84,42,0,656,647,1,0,0,0,656,648,1,0,0,0,
  	656,650,1,0,0,0,656,651,1,0,0,0,656,652,1,0,0,0,656,653,1,0,0,0,656,655,
  	1,0,0,0,657,81,1,0,0,0,658,659,7,10,0,0,659,664,3,92,46,0,660,661,7,11,
  	0,0,661,664,5,144,0,0,662,664,3,84,42,0,663,658,1,0,0,0,663,660,1,0,0,
  	0,663,662,1,0,0,0,664,83,1,0,0,0,665,666,5,116,0,0,666,668,3,86,43,0,
  	667,669,5,105,0,0,668,667,1,0,0,0,668,669,1,0,0,0,669,670,1,0,0,0,670,
  	671,5,2,0,0,671,85,1,0,0,0,672,677,3,88,44,0,673,674,5,117,0,0,674,676,
  	3,88,44,0,675,673,1,0,0,0,676,679,1,0,0,0,677,675,1,0,0,0,677,678,1,0,
  	0,0,678,87,1,0,0,0,679,677,1,0,0,0,680,685,3,90,45,0,681,682,5,118,0,
  	0,682,684,3,90,45,0,683,681,1,0,0,0,684,687,1,0,0,0,685,683,1,0,0,0,685,
  	686,1,0,0,0,686,89,1,0,0,0,687,685,1,0,0,0,688,689,6,45,-1,0,689,690,
  	5,152,0,0,690,691,3,86,43,0,691,692,5,153,0,0,692,793,1,0,0,0,693,793,
  	5,142,0,0,694,695,5,133,0,0,695,696,7,12,0,0,696,697,7,13,0,0,697,793,
  	7,12,0,0,698,700,5,134,0,0,699,701,5,177,0,0,700,699,1,0,0,0,700,701,
  	1,0,0,0,701,702,1,0,0,0,702,703,5,178,0,0,703,704,5,179,0,0,704,793,3,
  	94,47,0,705,706,5,122,0,0,706,793,3,90,45,18,707,708,5,124,0,0,708,793,
  	3,90,45,17,709,710,5,123,0,0,710,793,3,90,45,16,711,719,5,131,0,0,712,
  	720,5,150,0,0,713,716,5,149,0,0,714,715,5,154,0,0,715,717,5,149,0,0,716,
  	714,1,0,0,0,716,717,1,0,0,0,717,720,1,0,0,0,718,720,5,162,0,0,719,712,
  	1,0,0,0,719,713,1,0,0,0,719,718,1,0,0,0,720,793,1,0,0,0,721,729,5,132,
  	0,0,722,730,5,150,0,0,723,726,5,149,0,0,724,725,5,154,0,0,725,727,5,149,
  	0,0,726,724,1,0,0,0,726,727,1,0,0,0,727,730,1,0,0,0,728,730,5,162,0,0,
  	729,722,1,0,0,0,729,723,1,0,0,0,729,728,1,0,0,0,730,793,1,0,0,0,731,793,
  	5,136,0,0,732,793,5,137,0,0,733,793,5,138,0,0,734,793,5,143,0,0,735,736,
  	5,119,0,0,736,793,3,90,45,9,737,738,5,135,0,0,738,739,3,94,47,0,739,740,
  	3,94,47,0,740,743,3,94,47,0,741,742,5,84,0,0,742,744,3,94,47,0,743,741,
  	1,0,0,0,743,744,1,0,0,0,744,746,1,0,0,0,745,747,5,24,0,0,746,745,1,0,
  	0,0,746,747,1,0,0,0,747,793,1,0,0,0,748,793,5,139,0,0,749,793,5,140,0,
  	0,750,751,5,141,0,0,751,793,5,144,0,0,752,760,7,14,0,0,753,761,5,151,
  	0,0,754,757,5,144,0,0,755,756,5,154,0,0,756,758,5,144,0,0,757,755,1,0,
  	0,0,757,758,1,0,0,0,758,761,1,0,0,0,759,761,5,162,0,0,760,753,1,0,0,0,
  	760,754,1,0,0,0,760,759,1,0,0,0,761,793,1,0,0,0,762,770,5,129,0,0,763,
  	771,5,150,0,0,764,767,5,149,0,0,765,766,5,154,0,0,766,768,5,149,0,0,767,
  	765,1,0,0,0,767,768,1,0,0,0,768,771,1,0,0,0,769,771,5,162,0,0,770,763,
  	1,0,0,0,770,764,1,0,0,0,770,769,1,0,0,0,771,793,1,0,0,0,772,786,5,125,
  	0,0,773,787,5,150,0,0,774,777,5,149,0,0,775,776,5,154,0,0,776,778,5,149,
  	0,0,777,775,1,0,0,0,777,778,1,0,0,0,778,787,1,0,0,0,779,782,5,146,0,0,
  	780,781,5,154,0,0,781,783,5,146,0,0,782,780,1,0,0,0,782,783,1,0,0,0,783,
  	787,1,0,0,0,784,787,5,162,0,0,785,787,5,144,0,0,786,773,1,0,0,0,786,774,
  	1,0,0,0,786,779,1,0,0,0,786,784,1,0,0,0,786,785,1,0,0,0,787,793,1,0,0,
  	0,788,789,7,15,0,0,789,790,5,144,0,0,790,791,5,154,0,0,791,793,5,144,
  	0,0,792,688,1,0,0,0,792,693,1,0,0,0,792,694,1,0,0,0,792,698,1,0,0,0,792,
  	705,1,0,0,0,792,707,1,0,0,0,792,709,1,0,0,0,792,711,1,0,0,0,792,721,1,
  	0,0,0,792,731,1,0,0,0,792,732,1,0,0,0,792,733,1,0,0,0,792,734,1,0,0,0,
  	792,735,1,0,0,0,792,737,1,0,0,0,792,748,1,0,0,0,792,749,1,0,0,0,792,750,
  	1,0,0,0,792,752,1,0,0,0,792,762,1,0,0,0,792,772,1,0,0,0,792,788,1,0,0,
  	0,793,810,1,0,0,0,794,795,10,22,0,0,795,796,5,120,0,0,796,809,3,94,47,
  	0,797,798,10,21,0,0,798,806,5,121,0,0,799,807,5,151,0,0,800,803,5,144,
  	0,0,801,802,5,154,0,0,802,804,5,144,0,0,803,801,1,0,0,0,803,804,1,0,0,
  	0,804,807,1,0,0,0,805,807,5,162,0,0,806,799,1,0,0,0,806,800,1,0,0,0,806,
  	805,1,0,0,0,807,809,1,0,0,0,808,794,1,0,0,0,808,797,1,0,0,0,809,812,1,
  	0,0,0,810,808,1,0,0,0,810,811,1,0,0,0,811,91,1,0,0,0,812,810,1,0,0,0,
  	813,814,7,16,0,0,814,93,1,0,0,0,815,816,7,17,0,0,816,95,1,0,0,0,817,818,
  	7,16,0,0,818,97,1,0,0,0,819,820,5,1,0,0,820,822,5,171,0,0,821,823,5,168,
  	0,0,822,821,1,0,0,0,822,823,1,0,0,0,823,824,1,0,0,0,824,825,7,18,0,0,
  	825,826,5,173,0,0,826,99,1,0,0,0,95,116,118,127,136,145,155,159,166,174,
  	182,190,198,205,209,215,222,230,235,241,248,292,298,300,306,359,365,367,
  	373,389,410,415,420,425,429,432,437,443,450,454,458,463,467,471,476,483,
  	489,499,505,515,518,526,533,537,540,543,546,549,554,570,574,578,582,586,
  	590,595,598,610,622,632,643,656,663,668,677,685,700,716,719,726,729,743,
  	746,757,760,767,770,777,782,786,792,803,806,808,810,822
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  charmmmrparserParserStaticData = staticData.release();
}

}

CharmmMRParser::CharmmMRParser(TokenStream *input) : CharmmMRParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

CharmmMRParser::CharmmMRParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  CharmmMRParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *charmmmrparserParserStaticData->atn, charmmmrparserParserStaticData->decisionToDFA, charmmmrparserParserStaticData->sharedContextCache, options);
}

CharmmMRParser::~CharmmMRParser() {
  delete _interpreter;
}

const atn::ATN& CharmmMRParser::getATN() const {
  return *charmmmrparserParserStaticData->atn;
}

std::string CharmmMRParser::getGrammarFileName() const {
  return "CharmmMRParser.g4";
}

const std::vector<std::string>& CharmmMRParser::getRuleNames() const {
  return charmmmrparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& CharmmMRParser::getVocabulary() const {
  return charmmmrparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView CharmmMRParser::getSerializedATN() const {
  return charmmmrparserParserStaticData->serializedATN;
}


//----------------- Charmm_mrContext ------------------------------------------------------------------

CharmmMRParser::Charmm_mrContext::Charmm_mrContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Charmm_mrContext::EOF() {
  return getToken(CharmmMRParser::EOF, 0);
}

std::vector<CharmmMRParser::CommentContext *> CharmmMRParser::Charmm_mrContext::comment() {
  return getRuleContexts<CharmmMRParser::CommentContext>();
}

CharmmMRParser::CommentContext* CharmmMRParser::Charmm_mrContext::comment(size_t i) {
  return getRuleContext<CharmmMRParser::CommentContext>(i);
}

std::vector<CharmmMRParser::Distance_restraintContext *> CharmmMRParser::Charmm_mrContext::distance_restraint() {
  return getRuleContexts<CharmmMRParser::Distance_restraintContext>();
}

CharmmMRParser::Distance_restraintContext* CharmmMRParser::Charmm_mrContext::distance_restraint(size_t i) {
  return getRuleContext<CharmmMRParser::Distance_restraintContext>(i);
}

std::vector<CharmmMRParser::Point_distance_restraintContext *> CharmmMRParser::Charmm_mrContext::point_distance_restraint() {
  return getRuleContexts<CharmmMRParser::Point_distance_restraintContext>();
}

CharmmMRParser::Point_distance_restraintContext* CharmmMRParser::Charmm_mrContext::point_distance_restraint(size_t i) {
  return getRuleContext<CharmmMRParser::Point_distance_restraintContext>(i);
}

std::vector<CharmmMRParser::Dihedral_angle_restraintContext *> CharmmMRParser::Charmm_mrContext::dihedral_angle_restraint() {
  return getRuleContexts<CharmmMRParser::Dihedral_angle_restraintContext>();
}

CharmmMRParser::Dihedral_angle_restraintContext* CharmmMRParser::Charmm_mrContext::dihedral_angle_restraint(size_t i) {
  return getRuleContext<CharmmMRParser::Dihedral_angle_restraintContext>(i);
}

std::vector<CharmmMRParser::Harmonic_restraintContext *> CharmmMRParser::Charmm_mrContext::harmonic_restraint() {
  return getRuleContexts<CharmmMRParser::Harmonic_restraintContext>();
}

CharmmMRParser::Harmonic_restraintContext* CharmmMRParser::Charmm_mrContext::harmonic_restraint(size_t i) {
  return getRuleContext<CharmmMRParser::Harmonic_restraintContext>(i);
}

std::vector<CharmmMRParser::Manipulate_internal_coordinateContext *> CharmmMRParser::Charmm_mrContext::manipulate_internal_coordinate() {
  return getRuleContexts<CharmmMRParser::Manipulate_internal_coordinateContext>();
}

CharmmMRParser::Manipulate_internal_coordinateContext* CharmmMRParser::Charmm_mrContext::manipulate_internal_coordinate(size_t i) {
  return getRuleContext<CharmmMRParser::Manipulate_internal_coordinateContext>(i);
}

std::vector<CharmmMRParser::Droplet_potentialContext *> CharmmMRParser::Charmm_mrContext::droplet_potential() {
  return getRuleContexts<CharmmMRParser::Droplet_potentialContext>();
}

CharmmMRParser::Droplet_potentialContext* CharmmMRParser::Charmm_mrContext::droplet_potential(size_t i) {
  return getRuleContext<CharmmMRParser::Droplet_potentialContext>(i);
}

std::vector<CharmmMRParser::Fix_atom_constraintContext *> CharmmMRParser::Charmm_mrContext::fix_atom_constraint() {
  return getRuleContexts<CharmmMRParser::Fix_atom_constraintContext>();
}

CharmmMRParser::Fix_atom_constraintContext* CharmmMRParser::Charmm_mrContext::fix_atom_constraint(size_t i) {
  return getRuleContext<CharmmMRParser::Fix_atom_constraintContext>(i);
}

std::vector<CharmmMRParser::Center_of_mass_constraintContext *> CharmmMRParser::Charmm_mrContext::center_of_mass_constraint() {
  return getRuleContexts<CharmmMRParser::Center_of_mass_constraintContext>();
}

CharmmMRParser::Center_of_mass_constraintContext* CharmmMRParser::Charmm_mrContext::center_of_mass_constraint(size_t i) {
  return getRuleContext<CharmmMRParser::Center_of_mass_constraintContext>(i);
}

std::vector<CharmmMRParser::Fix_bond_or_angle_constraintContext *> CharmmMRParser::Charmm_mrContext::fix_bond_or_angle_constraint() {
  return getRuleContexts<CharmmMRParser::Fix_bond_or_angle_constraintContext>();
}

CharmmMRParser::Fix_bond_or_angle_constraintContext* CharmmMRParser::Charmm_mrContext::fix_bond_or_angle_constraint(size_t i) {
  return getRuleContext<CharmmMRParser::Fix_bond_or_angle_constraintContext>(i);
}

std::vector<CharmmMRParser::Restrained_distanceContext *> CharmmMRParser::Charmm_mrContext::restrained_distance() {
  return getRuleContexts<CharmmMRParser::Restrained_distanceContext>();
}

CharmmMRParser::Restrained_distanceContext* CharmmMRParser::Charmm_mrContext::restrained_distance(size_t i) {
  return getRuleContext<CharmmMRParser::Restrained_distanceContext>(i);
}

std::vector<CharmmMRParser::External_forceContext *> CharmmMRParser::Charmm_mrContext::external_force() {
  return getRuleContexts<CharmmMRParser::External_forceContext>();
}

CharmmMRParser::External_forceContext* CharmmMRParser::Charmm_mrContext::external_force(size_t i) {
  return getRuleContext<CharmmMRParser::External_forceContext>(i);
}

std::vector<CharmmMRParser::Rmsd_restraintContext *> CharmmMRParser::Charmm_mrContext::rmsd_restraint() {
  return getRuleContexts<CharmmMRParser::Rmsd_restraintContext>();
}

CharmmMRParser::Rmsd_restraintContext* CharmmMRParser::Charmm_mrContext::rmsd_restraint(size_t i) {
  return getRuleContext<CharmmMRParser::Rmsd_restraintContext>(i);
}

std::vector<CharmmMRParser::Gyration_restraintContext *> CharmmMRParser::Charmm_mrContext::gyration_restraint() {
  return getRuleContexts<CharmmMRParser::Gyration_restraintContext>();
}

CharmmMRParser::Gyration_restraintContext* CharmmMRParser::Charmm_mrContext::gyration_restraint(size_t i) {
  return getRuleContext<CharmmMRParser::Gyration_restraintContext>(i);
}

std::vector<CharmmMRParser::Distance_matrix_restraintContext *> CharmmMRParser::Charmm_mrContext::distance_matrix_restraint() {
  return getRuleContexts<CharmmMRParser::Distance_matrix_restraintContext>();
}

CharmmMRParser::Distance_matrix_restraintContext* CharmmMRParser::Charmm_mrContext::distance_matrix_restraint(size_t i) {
  return getRuleContext<CharmmMRParser::Distance_matrix_restraintContext>(i);
}

std::vector<CharmmMRParser::Set_statementContext *> CharmmMRParser::Charmm_mrContext::set_statement() {
  return getRuleContexts<CharmmMRParser::Set_statementContext>();
}

CharmmMRParser::Set_statementContext* CharmmMRParser::Charmm_mrContext::set_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Set_statementContext>(i);
}


size_t CharmmMRParser::Charmm_mrContext::getRuleIndex() const {
  return CharmmMRParser::RuleCharmm_mr;
}


std::any CharmmMRParser::Charmm_mrContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitCharmm_mr(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Charmm_mrContext* CharmmMRParser::charmm_mr() {
  Charmm_mrContext *_localctx = _tracker.createInstance<Charmm_mrContext>(_ctx, getState());
  enterRule(_localctx, 0, CharmmMRParser::RuleCharmm_mr);
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
    setState(118);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 180152781187842058) != 0) || ((((_la - 87) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 87)) & 2305843009282900097) != 0)) {
      setState(116);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
      case 1: {
        setState(100);
        comment();
        break;
      }

      case 2: {
        setState(101);
        distance_restraint();
        break;
      }

      case 3: {
        setState(102);
        point_distance_restraint();
        break;
      }

      case 4: {
        setState(103);
        dihedral_angle_restraint();
        break;
      }

      case 5: {
        setState(104);
        harmonic_restraint();
        break;
      }

      case 6: {
        setState(105);
        manipulate_internal_coordinate();
        break;
      }

      case 7: {
        setState(106);
        droplet_potential();
        break;
      }

      case 8: {
        setState(107);
        fix_atom_constraint();
        break;
      }

      case 9: {
        setState(108);
        center_of_mass_constraint();
        break;
      }

      case 10: {
        setState(109);
        fix_bond_or_angle_constraint();
        break;
      }

      case 11: {
        setState(110);
        restrained_distance();
        break;
      }

      case 12: {
        setState(111);
        external_force();
        break;
      }

      case 13: {
        setState(112);
        rmsd_restraint();
        break;
      }

      case 14: {
        setState(113);
        gyration_restraint();
        break;
      }

      case 15: {
        setState(114);
        distance_matrix_restraint();
        break;
      }

      case 16: {
        setState(115);
        set_statement();
        break;
      }

      default:
        break;
      }
      setState(120);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(121);
    match(CharmmMRParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CommentContext ------------------------------------------------------------------

CharmmMRParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::CommentContext::COMMENT() {
  return getToken(CharmmMRParser::COMMENT, 0);
}

tree::TerminalNode* CharmmMRParser::CommentContext::RETURN_CM() {
  return getToken(CharmmMRParser::RETURN_CM, 0);
}

tree::TerminalNode* CharmmMRParser::CommentContext::EOF() {
  return getToken(CharmmMRParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CharmmMRParser::CommentContext::Any_name() {
  return getTokens(CharmmMRParser::Any_name);
}

tree::TerminalNode* CharmmMRParser::CommentContext::Any_name(size_t i) {
  return getToken(CharmmMRParser::Any_name, i);
}


size_t CharmmMRParser::CommentContext::getRuleIndex() const {
  return CharmmMRParser::RuleComment;
}


std::any CharmmMRParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::CommentContext* CharmmMRParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 2, CharmmMRParser::RuleComment);
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
    setState(123);
    match(CharmmMRParser::COMMENT);
    setState(127);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CharmmMRParser::Any_name) {
      setState(124);
      match(CharmmMRParser::Any_name);
      setState(129);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(130);
    _la = _input->LA(1);
    if (!(_la == CharmmMRParser::EOF || _la == CharmmMRParser::RETURN_CM)) {
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

//----------------- Distance_restraintContext ------------------------------------------------------------------

CharmmMRParser::Distance_restraintContext::Distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Distance_restraintContext::Noe() {
  return getToken(CharmmMRParser::Noe, 0);
}

tree::TerminalNode* CharmmMRParser::Distance_restraintContext::End() {
  return getToken(CharmmMRParser::End, 0);
}

std::vector<CharmmMRParser::Noe_statementContext *> CharmmMRParser::Distance_restraintContext::noe_statement() {
  return getRuleContexts<CharmmMRParser::Noe_statementContext>();
}

CharmmMRParser::Noe_statementContext* CharmmMRParser::Distance_restraintContext::noe_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Noe_statementContext>(i);
}


size_t CharmmMRParser::Distance_restraintContext::getRuleIndex() const {
  return CharmmMRParser::RuleDistance_restraint;
}


std::any CharmmMRParser::Distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Distance_restraintContext* CharmmMRParser::distance_restraint() {
  Distance_restraintContext *_localctx = _tracker.createInstance<Distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 4, CharmmMRParser::RuleDistance_restraint);
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
    match(CharmmMRParser::Noe);
    setState(136);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((((_la - 56) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 56)) & 1707229181) != 0)) {
      setState(133);
      noe_statement();
      setState(138);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(139);
    match(CharmmMRParser::End);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Point_distance_restraintContext ------------------------------------------------------------------

CharmmMRParser::Point_distance_restraintContext::Point_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Point_distance_restraintContext::PNoe() {
  return getToken(CharmmMRParser::PNoe, 0);
}

tree::TerminalNode* CharmmMRParser::Point_distance_restraintContext::End() {
  return getToken(CharmmMRParser::End, 0);
}

std::vector<CharmmMRParser::Pnoe_statementContext *> CharmmMRParser::Point_distance_restraintContext::pnoe_statement() {
  return getRuleContexts<CharmmMRParser::Pnoe_statementContext>();
}

CharmmMRParser::Pnoe_statementContext* CharmmMRParser::Point_distance_restraintContext::pnoe_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Pnoe_statementContext>(i);
}


size_t CharmmMRParser::Point_distance_restraintContext::getRuleIndex() const {
  return CharmmMRParser::RulePoint_distance_restraint;
}


std::any CharmmMRParser::Point_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitPoint_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Point_distance_restraintContext* CharmmMRParser::point_distance_restraint() {
  Point_distance_restraintContext *_localctx = _tracker.createInstance<Point_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 6, CharmmMRParser::RulePoint_distance_restraint);
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
    setState(141);
    match(CharmmMRParser::PNoe);
    setState(145);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((((_la - 56) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 56)) & 1707343869) != 0)) {
      setState(142);
      pnoe_statement();
      setState(147);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(148);
    match(CharmmMRParser::End);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_restraintContext ------------------------------------------------------------------

CharmmMRParser::Dihedral_angle_restraintContext::Dihedral_angle_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Dihedral_angle_restraintContext::Cons() {
  return getToken(CharmmMRParser::Cons, 0);
}

tree::TerminalNode* CharmmMRParser::Dihedral_angle_restraintContext::Dihedral() {
  return getToken(CharmmMRParser::Dihedral, 0);
}

tree::TerminalNode* CharmmMRParser::Dihedral_angle_restraintContext::ClDh() {
  return getToken(CharmmMRParser::ClDh, 0);
}

std::vector<CharmmMRParser::Dihedral_statementContext *> CharmmMRParser::Dihedral_angle_restraintContext::dihedral_statement() {
  return getRuleContexts<CharmmMRParser::Dihedral_statementContext>();
}

CharmmMRParser::Dihedral_statementContext* CharmmMRParser::Dihedral_angle_restraintContext::dihedral_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Dihedral_statementContext>(i);
}


size_t CharmmMRParser::Dihedral_angle_restraintContext::getRuleIndex() const {
  return CharmmMRParser::RuleDihedral_angle_restraint;
}


std::any CharmmMRParser::Dihedral_angle_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_restraint(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Dihedral_angle_restraintContext* CharmmMRParser::dihedral_angle_restraint() {
  Dihedral_angle_restraintContext *_localctx = _tracker.createInstance<Dihedral_angle_restraintContext>(_ctx, getState());
  enterRule(_localctx, 8, CharmmMRParser::RuleDihedral_angle_restraint);
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
    setState(150);
    match(CharmmMRParser::Cons);
    setState(159);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Dihedral: {
        setState(151);
        match(CharmmMRParser::Dihedral);
        setState(155);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while ((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 63701504) != 0) || ((((_la - 116) & ~ 0x3fULL) == 0) &&
          ((1ULL << (_la - 116)) & 8858370049) != 0)) {
          setState(152);
          dihedral_statement();
          setState(157);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        break;
      }

      case CharmmMRParser::ClDh: {
        setState(158);
        match(CharmmMRParser::ClDh);
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

//----------------- Harmonic_restraintContext ------------------------------------------------------------------

CharmmMRParser::Harmonic_restraintContext::Harmonic_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Harmonic_restraintContext::Cons() {
  return getToken(CharmmMRParser::Cons, 0);
}

tree::TerminalNode* CharmmMRParser::Harmonic_restraintContext::Harmonic() {
  return getToken(CharmmMRParser::Harmonic, 0);
}

std::vector<CharmmMRParser::Harmonic_statementContext *> CharmmMRParser::Harmonic_restraintContext::harmonic_statement() {
  return getRuleContexts<CharmmMRParser::Harmonic_statementContext>();
}

CharmmMRParser::Harmonic_statementContext* CharmmMRParser::Harmonic_restraintContext::harmonic_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Harmonic_statementContext>(i);
}


size_t CharmmMRParser::Harmonic_restraintContext::getRuleIndex() const {
  return CharmmMRParser::RuleHarmonic_restraint;
}


std::any CharmmMRParser::Harmonic_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitHarmonic_restraint(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Harmonic_restraintContext* CharmmMRParser::harmonic_restraint() {
  Harmonic_restraintContext *_localctx = _tracker.createInstance<Harmonic_restraintContext>(_ctx, getState());
  enterRule(_localctx, 10, CharmmMRParser::RuleHarmonic_restraint);
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
    setState(161);
    match(CharmmMRParser::Cons);
    setState(162);
    match(CharmmMRParser::Harmonic);
    setState(166);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 65504) != 0) || _la == CharmmMRParser::Selection) {
      setState(163);
      harmonic_statement();
      setState(168);
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

//----------------- Manipulate_internal_coordinateContext ------------------------------------------------------------------

CharmmMRParser::Manipulate_internal_coordinateContext::Manipulate_internal_coordinateContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Manipulate_internal_coordinateContext::Cons() {
  return getToken(CharmmMRParser::Cons, 0);
}

tree::TerminalNode* CharmmMRParser::Manipulate_internal_coordinateContext::IC() {
  return getToken(CharmmMRParser::IC, 0);
}

std::vector<CharmmMRParser::Ic_statementContext *> CharmmMRParser::Manipulate_internal_coordinateContext::ic_statement() {
  return getRuleContexts<CharmmMRParser::Ic_statementContext>();
}

CharmmMRParser::Ic_statementContext* CharmmMRParser::Manipulate_internal_coordinateContext::ic_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Ic_statementContext>(i);
}


size_t CharmmMRParser::Manipulate_internal_coordinateContext::getRuleIndex() const {
  return CharmmMRParser::RuleManipulate_internal_coordinate;
}


std::any CharmmMRParser::Manipulate_internal_coordinateContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitManipulate_internal_coordinate(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Manipulate_internal_coordinateContext* CharmmMRParser::manipulate_internal_coordinate() {
  Manipulate_internal_coordinateContext *_localctx = _tracker.createInstance<Manipulate_internal_coordinateContext>(_ctx, getState());
  enterRule(_localctx, 12, CharmmMRParser::RuleManipulate_internal_coordinate);
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
    setState(169);
    match(CharmmMRParser::Cons);
    setState(170);
    match(CharmmMRParser::IC);
    setState(174);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 3491758080) != 0)) {
      setState(171);
      ic_statement();
      setState(176);
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

//----------------- Droplet_potentialContext ------------------------------------------------------------------

CharmmMRParser::Droplet_potentialContext::Droplet_potentialContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Droplet_potentialContext::Cons() {
  return getToken(CharmmMRParser::Cons, 0);
}

tree::TerminalNode* CharmmMRParser::Droplet_potentialContext::Droplet() {
  return getToken(CharmmMRParser::Droplet, 0);
}

std::vector<CharmmMRParser::Droplet_statementContext *> CharmmMRParser::Droplet_potentialContext::droplet_statement() {
  return getRuleContexts<CharmmMRParser::Droplet_statementContext>();
}

CharmmMRParser::Droplet_statementContext* CharmmMRParser::Droplet_potentialContext::droplet_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Droplet_statementContext>(i);
}


size_t CharmmMRParser::Droplet_potentialContext::getRuleIndex() const {
  return CharmmMRParser::RuleDroplet_potential;
}


std::any CharmmMRParser::Droplet_potentialContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitDroplet_potential(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Droplet_potentialContext* CharmmMRParser::droplet_potential() {
  Droplet_potentialContext *_localctx = _tracker.createInstance<Droplet_potentialContext>(_ctx, getState());
  enterRule(_localctx, 14, CharmmMRParser::RuleDroplet_potential);
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
    setState(177);
    match(CharmmMRParser::Cons);
    setState(178);
    match(CharmmMRParser::Droplet);
    setState(182);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8589939200) != 0)) {
      setState(179);
      droplet_statement();
      setState(184);
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

//----------------- Fix_atom_constraintContext ------------------------------------------------------------------

CharmmMRParser::Fix_atom_constraintContext::Fix_atom_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Fix_atom_constraintContext::Cons() {
  return getToken(CharmmMRParser::Cons, 0);
}

tree::TerminalNode* CharmmMRParser::Fix_atom_constraintContext::Fix() {
  return getToken(CharmmMRParser::Fix, 0);
}

std::vector<CharmmMRParser::Fix_atom_statementContext *> CharmmMRParser::Fix_atom_constraintContext::fix_atom_statement() {
  return getRuleContexts<CharmmMRParser::Fix_atom_statementContext>();
}

CharmmMRParser::Fix_atom_statementContext* CharmmMRParser::Fix_atom_constraintContext::fix_atom_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Fix_atom_statementContext>(i);
}


size_t CharmmMRParser::Fix_atom_constraintContext::getRuleIndex() const {
  return CharmmMRParser::RuleFix_atom_constraint;
}


std::any CharmmMRParser::Fix_atom_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitFix_atom_constraint(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Fix_atom_constraintContext* CharmmMRParser::fix_atom_constraint() {
  Fix_atom_constraintContext *_localctx = _tracker.createInstance<Fix_atom_constraintContext>(_ctx, getState());
  enterRule(_localctx, 16, CharmmMRParser::RuleFix_atom_constraint);
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
    setState(185);
    match(CharmmMRParser::Cons);
    setState(186);
    match(CharmmMRParser::Fix);
    setState(190);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CharmmMRParser::Selection) {
      setState(187);
      fix_atom_statement();
      setState(192);
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

//----------------- Center_of_mass_constraintContext ------------------------------------------------------------------

CharmmMRParser::Center_of_mass_constraintContext::Center_of_mass_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Center_of_mass_constraintContext::Cons() {
  return getToken(CharmmMRParser::Cons, 0);
}

tree::TerminalNode* CharmmMRParser::Center_of_mass_constraintContext::Hmcm() {
  return getToken(CharmmMRParser::Hmcm, 0);
}

std::vector<CharmmMRParser::Center_of_mass_statementContext *> CharmmMRParser::Center_of_mass_constraintContext::center_of_mass_statement() {
  return getRuleContexts<CharmmMRParser::Center_of_mass_statementContext>();
}

CharmmMRParser::Center_of_mass_statementContext* CharmmMRParser::Center_of_mass_constraintContext::center_of_mass_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Center_of_mass_statementContext>(i);
}


size_t CharmmMRParser::Center_of_mass_constraintContext::getRuleIndex() const {
  return CharmmMRParser::RuleCenter_of_mass_constraint;
}


std::any CharmmMRParser::Center_of_mass_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitCenter_of_mass_constraint(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Center_of_mass_constraintContext* CharmmMRParser::center_of_mass_constraint() {
  Center_of_mass_constraintContext *_localctx = _tracker.createInstance<Center_of_mass_constraintContext>(_ctx, getState());
  enterRule(_localctx, 18, CharmmMRParser::RuleCenter_of_mass_constraint);
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
    setState(193);
    match(CharmmMRParser::Cons);
    setState(194);
    match(CharmmMRParser::Hmcm);
    setState(198);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CharmmMRParser::Force) {
      setState(195);
      center_of_mass_statement();
      setState(200);
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

//----------------- Fix_bond_or_angle_constraintContext ------------------------------------------------------------------

CharmmMRParser::Fix_bond_or_angle_constraintContext::Fix_bond_or_angle_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Fix_bond_or_angle_constraintContext::Shake() {
  return getToken(CharmmMRParser::Shake, 0);
}

tree::TerminalNode* CharmmMRParser::Fix_bond_or_angle_constraintContext::Off() {
  return getToken(CharmmMRParser::Off, 0);
}

std::vector<CharmmMRParser::Fix_bond_or_angle_statementContext *> CharmmMRParser::Fix_bond_or_angle_constraintContext::fix_bond_or_angle_statement() {
  return getRuleContexts<CharmmMRParser::Fix_bond_or_angle_statementContext>();
}

CharmmMRParser::Fix_bond_or_angle_statementContext* CharmmMRParser::Fix_bond_or_angle_constraintContext::fix_bond_or_angle_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Fix_bond_or_angle_statementContext>(i);
}


size_t CharmmMRParser::Fix_bond_or_angle_constraintContext::getRuleIndex() const {
  return CharmmMRParser::RuleFix_bond_or_angle_constraint;
}


std::any CharmmMRParser::Fix_bond_or_angle_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitFix_bond_or_angle_constraint(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Fix_bond_or_angle_constraintContext* CharmmMRParser::fix_bond_or_angle_constraint() {
  Fix_bond_or_angle_constraintContext *_localctx = _tracker.createInstance<Fix_bond_or_angle_constraintContext>(_ctx, getState());
  enterRule(_localctx, 20, CharmmMRParser::RuleFix_bond_or_angle_constraint);
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
    setState(201);
    match(CharmmMRParser::Shake);
    setState(209);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::EOF:
      case CharmmMRParser::Set:
      case CharmmMRParser::Cons:
      case CharmmMRParser::Shake:
      case CharmmMRParser::NoReset:
      case CharmmMRParser::Fast:
      case CharmmMRParser::NoFast:
      case CharmmMRParser::Noe:
      case CharmmMRParser::PNoe:
      case CharmmMRParser::ResDistance:
      case CharmmMRParser::Pull:
      case CharmmMRParser::RGyration:
      case CharmmMRParser::DMConstrain:
      case CharmmMRParser::Selection:
      case CharmmMRParser::COMMENT: {
        setState(205);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while ((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 22553182508941312) != 0) || _la == CharmmMRParser::Selection) {
          setState(202);
          fix_bond_or_angle_statement();
          setState(207);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        break;
      }

      case CharmmMRParser::Off: {
        setState(208);
        match(CharmmMRParser::Off);
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

//----------------- Restrained_distanceContext ------------------------------------------------------------------

CharmmMRParser::Restrained_distanceContext::Restrained_distanceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Restrained_distanceContext::ResDistance() {
  return getToken(CharmmMRParser::ResDistance, 0);
}

std::vector<CharmmMRParser::Restrained_distance_statementContext *> CharmmMRParser::Restrained_distanceContext::restrained_distance_statement() {
  return getRuleContexts<CharmmMRParser::Restrained_distance_statementContext>();
}

CharmmMRParser::Restrained_distance_statementContext* CharmmMRParser::Restrained_distanceContext::restrained_distance_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Restrained_distance_statementContext>(i);
}


size_t CharmmMRParser::Restrained_distanceContext::getRuleIndex() const {
  return CharmmMRParser::RuleRestrained_distance;
}


std::any CharmmMRParser::Restrained_distanceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitRestrained_distance(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Restrained_distanceContext* CharmmMRParser::restrained_distance() {
  Restrained_distanceContext *_localctx = _tracker.createInstance<Restrained_distanceContext>(_ctx, getState());
  enterRule(_localctx, 22, CharmmMRParser::RuleRestrained_distance);
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
    setState(211);
    match(CharmmMRParser::ResDistance);
    setState(215);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((((_la - 56) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 56)) & 1152921775726657537) != 0)) {
      setState(212);
      restrained_distance_statement();
      setState(217);
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

//----------------- External_forceContext ------------------------------------------------------------------

CharmmMRParser::External_forceContext::External_forceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::External_forceContext::Pull() {
  return getToken(CharmmMRParser::Pull, 0);
}

std::vector<CharmmMRParser::External_force_statementContext *> CharmmMRParser::External_forceContext::external_force_statement() {
  return getRuleContexts<CharmmMRParser::External_force_statementContext>();
}

CharmmMRParser::External_force_statementContext* CharmmMRParser::External_forceContext::external_force_statement(size_t i) {
  return getRuleContext<CharmmMRParser::External_force_statementContext>(i);
}


size_t CharmmMRParser::External_forceContext::getRuleIndex() const {
  return CharmmMRParser::RuleExternal_force;
}


std::any CharmmMRParser::External_forceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitExternal_force(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::External_forceContext* CharmmMRParser::external_force() {
  External_forceContext *_localctx = _tracker.createInstance<External_forceContext>(_ctx, getState());
  enterRule(_localctx, 24, CharmmMRParser::RuleExternal_force);
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
    setState(218);
    match(CharmmMRParser::Pull);
    setState(222);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 17592202824192) != 0) || ((((_la - 95) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 95)) & 2097279) != 0)) {
      setState(219);
      external_force_statement();
      setState(224);
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

//----------------- Rmsd_restraintContext ------------------------------------------------------------------

CharmmMRParser::Rmsd_restraintContext::Rmsd_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Rmsd_restraintContext::Cons() {
  return getToken(CharmmMRParser::Cons, 0);
}

tree::TerminalNode* CharmmMRParser::Rmsd_restraintContext::RMSD() {
  return getToken(CharmmMRParser::RMSD, 0);
}

tree::TerminalNode* CharmmMRParser::Rmsd_restraintContext::Show() {
  return getToken(CharmmMRParser::Show, 0);
}

tree::TerminalNode* CharmmMRParser::Rmsd_restraintContext::Clear() {
  return getToken(CharmmMRParser::Clear, 0);
}

std::vector<CharmmMRParser::Rmsd_statementContext *> CharmmMRParser::Rmsd_restraintContext::rmsd_statement() {
  return getRuleContexts<CharmmMRParser::Rmsd_statementContext>();
}

CharmmMRParser::Rmsd_statementContext* CharmmMRParser::Rmsd_restraintContext::rmsd_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Rmsd_statementContext>(i);
}


size_t CharmmMRParser::Rmsd_restraintContext::getRuleIndex() const {
  return CharmmMRParser::RuleRmsd_restraint;
}


std::any CharmmMRParser::Rmsd_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitRmsd_restraint(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Rmsd_restraintContext* CharmmMRParser::rmsd_restraint() {
  Rmsd_restraintContext *_localctx = _tracker.createInstance<Rmsd_restraintContext>(_ctx, getState());
  enterRule(_localctx, 26, CharmmMRParser::RuleRmsd_restraint);
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
    setState(225);
    match(CharmmMRParser::Cons);
    setState(226);
    match(CharmmMRParser::RMSD);
    setState(235);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::EOF:
      case CharmmMRParser::Set:
      case CharmmMRParser::Cons:
      case CharmmMRParser::Relative:
      case CharmmMRParser::Force:
      case CharmmMRParser::Mass:
      case CharmmMRParser::NoRotation:
      case CharmmMRParser::NoTranslation:
      case CharmmMRParser::Main:
      case CharmmMRParser::Comp:
      case CharmmMRParser::Shake:
      case CharmmMRParser::Noe:
      case CharmmMRParser::PNoe:
      case CharmmMRParser::ResDistance:
      case CharmmMRParser::Pull:
      case CharmmMRParser::MaxN:
      case CharmmMRParser::NPrt:
      case CharmmMRParser::Offset:
      case CharmmMRParser::BOffset:
      case CharmmMRParser::RGyration:
      case CharmmMRParser::DMConstrain:
      case CharmmMRParser::Selection:
      case CharmmMRParser::COMMENT: {
        setState(230);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while ((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 984704) != 0) || ((((_la - 103) & ~ 0x3fULL) == 0) &&
          ((1ULL << (_la - 103)) & 8219) != 0)) {
          setState(227);
          rmsd_statement();
          setState(232);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        break;
      }

      case CharmmMRParser::Show: {
        setState(233);
        match(CharmmMRParser::Show);
        break;
      }

      case CharmmMRParser::Clear: {
        setState(234);
        match(CharmmMRParser::Clear);
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

//----------------- Gyration_restraintContext ------------------------------------------------------------------

CharmmMRParser::Gyration_restraintContext::Gyration_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Gyration_restraintContext::RGyration() {
  return getToken(CharmmMRParser::RGyration, 0);
}

std::vector<CharmmMRParser::Gyration_statementContext *> CharmmMRParser::Gyration_restraintContext::gyration_statement() {
  return getRuleContexts<CharmmMRParser::Gyration_statementContext>();
}

CharmmMRParser::Gyration_statementContext* CharmmMRParser::Gyration_restraintContext::gyration_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Gyration_statementContext>(i);
}


size_t CharmmMRParser::Gyration_restraintContext::getRuleIndex() const {
  return CharmmMRParser::RuleGyration_restraint;
}


std::any CharmmMRParser::Gyration_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitGyration_restraint(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Gyration_restraintContext* CharmmMRParser::gyration_restraint() {
  Gyration_restraintContext *_localctx = _tracker.createInstance<Gyration_restraintContext>(_ctx, getState());
  enterRule(_localctx, 28, CharmmMRParser::RuleGyration_restraint);
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
    setState(237);
    match(CharmmMRParser::RGyration);
    setState(241);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 72057594038452736) != 0) || ((((_la - 102) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 102)) & 18305) != 0)) {
      setState(238);
      gyration_statement();
      setState(243);
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

//----------------- Distance_matrix_restraintContext ------------------------------------------------------------------

CharmmMRParser::Distance_matrix_restraintContext::Distance_matrix_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Distance_matrix_restraintContext::DMConstrain() {
  return getToken(CharmmMRParser::DMConstrain, 0);
}

std::vector<CharmmMRParser::Distance_matrix_statementContext *> CharmmMRParser::Distance_matrix_restraintContext::distance_matrix_statement() {
  return getRuleContexts<CharmmMRParser::Distance_matrix_statementContext>();
}

CharmmMRParser::Distance_matrix_statementContext* CharmmMRParser::Distance_matrix_restraintContext::distance_matrix_statement(size_t i) {
  return getRuleContext<CharmmMRParser::Distance_matrix_statementContext>(i);
}


size_t CharmmMRParser::Distance_matrix_restraintContext::getRuleIndex() const {
  return CharmmMRParser::RuleDistance_matrix_restraint;
}


std::any CharmmMRParser::Distance_matrix_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_matrix_restraint(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Distance_matrix_restraintContext* CharmmMRParser::distance_matrix_restraint() {
  Distance_matrix_restraintContext *_localctx = _tracker.createInstance<Distance_matrix_restraintContext>(_ctx, getState());
  enterRule(_localctx, 30, CharmmMRParser::RuleDistance_matrix_restraint);
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
    setState(244);
    match(CharmmMRParser::DMConstrain);
    setState(248);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CharmmMRParser::Force

    || _la == CharmmMRParser::Weight || ((((_la - 109) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 109)) & 237) != 0)) {
      setState(245);
      distance_matrix_statement();
      setState(250);
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

//----------------- Noe_statementContext ------------------------------------------------------------------

CharmmMRParser::Noe_statementContext::Noe_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CharmmMRParser::Noe_assignContext* CharmmMRParser::Noe_statementContext::noe_assign() {
  return getRuleContext<CharmmMRParser::Noe_assignContext>(0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::Reset() {
  return getToken(CharmmMRParser::Reset, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::KMin() {
  return getToken(CharmmMRParser::KMin, 0);
}

std::vector<CharmmMRParser::Number_sContext *> CharmmMRParser::Noe_statementContext::number_s() {
  return getRuleContexts<CharmmMRParser::Number_sContext>();
}

CharmmMRParser::Number_sContext* CharmmMRParser::Noe_statementContext::number_s(size_t i) {
  return getRuleContext<CharmmMRParser::Number_sContext>(i);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::RMin() {
  return getToken(CharmmMRParser::RMin, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::KMax() {
  return getToken(CharmmMRParser::KMax, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::RMax() {
  return getToken(CharmmMRParser::RMax, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::FMax() {
  return getToken(CharmmMRParser::FMax, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::MinDist() {
  return getToken(CharmmMRParser::MinDist, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::RSwi() {
  return getToken(CharmmMRParser::RSwi, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::SExp() {
  return getToken(CharmmMRParser::SExp, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::SumR() {
  return getToken(CharmmMRParser::SumR, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::TCon() {
  return getToken(CharmmMRParser::TCon, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::RExp() {
  return getToken(CharmmMRParser::RExp, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::MPNoe() {
  return getToken(CharmmMRParser::MPNoe, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::INoe() {
  return getToken(CharmmMRParser::INoe, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::TnoX() {
  return getToken(CharmmMRParser::TnoX, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::TnoY() {
  return getToken(CharmmMRParser::TnoY, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::TnoZ() {
  return getToken(CharmmMRParser::TnoZ, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::NMPNoe() {
  return getToken(CharmmMRParser::NMPNoe, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::Read() {
  return getToken(CharmmMRParser::Read, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::Unit() {
  return getToken(CharmmMRParser::Unit, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::Write() {
  return getToken(CharmmMRParser::Write, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::Anal() {
  return getToken(CharmmMRParser::Anal, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::Print() {
  return getToken(CharmmMRParser::Print, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::Cut() {
  return getToken(CharmmMRParser::Cut, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::Scale() {
  return getToken(CharmmMRParser::Scale, 0);
}

tree::TerminalNode* CharmmMRParser::Noe_statementContext::Temperature() {
  return getToken(CharmmMRParser::Temperature, 0);
}


size_t CharmmMRParser::Noe_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleNoe_statement;
}


std::any CharmmMRParser::Noe_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitNoe_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Noe_statementContext* CharmmMRParser::noe_statement() {
  Noe_statementContext *_localctx = _tracker.createInstance<Noe_statementContext>(_ctx, getState());
  enterRule(_localctx, 32, CharmmMRParser::RuleNoe_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(306);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Assign: {
        enterOuterAlt(_localctx, 1);
        setState(251);
        noe_assign();
        break;
      }

      case CharmmMRParser::Reset: {
        enterOuterAlt(_localctx, 2);
        setState(252);
        match(CharmmMRParser::Reset);
        break;
      }

      case CharmmMRParser::KMin: {
        enterOuterAlt(_localctx, 3);
        setState(253);
        match(CharmmMRParser::KMin);
        setState(254);
        number_s();
        break;
      }

      case CharmmMRParser::RMin: {
        enterOuterAlt(_localctx, 4);
        setState(255);
        match(CharmmMRParser::RMin);
        setState(256);
        number_s();
        break;
      }

      case CharmmMRParser::KMax: {
        enterOuterAlt(_localctx, 5);
        setState(257);
        match(CharmmMRParser::KMax);
        setState(258);
        number_s();
        break;
      }

      case CharmmMRParser::RMax: {
        enterOuterAlt(_localctx, 6);
        setState(259);
        match(CharmmMRParser::RMax);
        setState(260);
        number_s();
        break;
      }

      case CharmmMRParser::FMax: {
        enterOuterAlt(_localctx, 7);
        setState(261);
        match(CharmmMRParser::FMax);
        setState(262);
        number_s();
        break;
      }

      case CharmmMRParser::MinDist: {
        enterOuterAlt(_localctx, 8);
        setState(263);
        match(CharmmMRParser::MinDist);
        break;
      }

      case CharmmMRParser::RSwi: {
        enterOuterAlt(_localctx, 9);
        setState(264);
        match(CharmmMRParser::RSwi);
        setState(265);
        number_s();
        break;
      }

      case CharmmMRParser::SExp: {
        enterOuterAlt(_localctx, 10);
        setState(266);
        match(CharmmMRParser::SExp);
        setState(267);
        number_s();
        break;
      }

      case CharmmMRParser::SumR: {
        enterOuterAlt(_localctx, 11);
        setState(268);
        match(CharmmMRParser::SumR);
        break;
      }

      case CharmmMRParser::TCon: {
        enterOuterAlt(_localctx, 12);
        setState(269);
        match(CharmmMRParser::TCon);
        setState(270);
        number_s();
        break;
      }

      case CharmmMRParser::RExp: {
        enterOuterAlt(_localctx, 13);
        setState(271);
        match(CharmmMRParser::RExp);
        setState(272);
        number_s();
        break;
      }

      case CharmmMRParser::MPNoe: {
        enterOuterAlt(_localctx, 14);
        setState(273);
        match(CharmmMRParser::MPNoe);
        setState(274);
        match(CharmmMRParser::INoe);
        setState(275);
        match(CharmmMRParser::Integer);
        setState(276);
        match(CharmmMRParser::TnoX);
        setState(277);
        number_s();
        setState(278);
        match(CharmmMRParser::TnoY);
        setState(279);
        number_s();
        setState(280);
        match(CharmmMRParser::TnoZ);
        setState(281);
        number_s();
        break;
      }

      case CharmmMRParser::NMPNoe: {
        enterOuterAlt(_localctx, 15);
        setState(283);
        match(CharmmMRParser::NMPNoe);
        setState(284);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::Read: {
        enterOuterAlt(_localctx, 16);
        setState(285);
        match(CharmmMRParser::Read);
        setState(286);
        match(CharmmMRParser::Unit);
        setState(287);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::Write: {
        enterOuterAlt(_localctx, 17);
        setState(288);
        match(CharmmMRParser::Write);
        setState(289);
        match(CharmmMRParser::Unit);
        setState(290);
        match(CharmmMRParser::Integer);
        setState(292);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CharmmMRParser::Anal) {
          setState(291);
          match(CharmmMRParser::Anal);
        }
        break;
      }

      case CharmmMRParser::Print: {
        enterOuterAlt(_localctx, 18);
        setState(294);
        match(CharmmMRParser::Print);
        setState(300);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CharmmMRParser::Anal) {
          setState(295);
          match(CharmmMRParser::Anal);
          setState(298);
          _errHandler->sync(this);

          _la = _input->LA(1);
          if (_la == CharmmMRParser::Cut) {
            setState(296);
            match(CharmmMRParser::Cut);
            setState(297);
            number_s();
          }
        }
        break;
      }

      case CharmmMRParser::Scale: {
        enterOuterAlt(_localctx, 19);
        setState(302);
        match(CharmmMRParser::Scale);
        setState(303);
        number_s();
        break;
      }

      case CharmmMRParser::Temperature: {
        enterOuterAlt(_localctx, 20);
        setState(304);
        match(CharmmMRParser::Temperature);
        setState(305);
        number_s();
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

//----------------- Noe_assignContext ------------------------------------------------------------------

CharmmMRParser::Noe_assignContext::Noe_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Noe_assignContext::Assign() {
  return getToken(CharmmMRParser::Assign, 0);
}

std::vector<CharmmMRParser::SelectionContext *> CharmmMRParser::Noe_assignContext::selection() {
  return getRuleContexts<CharmmMRParser::SelectionContext>();
}

CharmmMRParser::SelectionContext* CharmmMRParser::Noe_assignContext::selection(size_t i) {
  return getRuleContext<CharmmMRParser::SelectionContext>(i);
}


size_t CharmmMRParser::Noe_assignContext::getRuleIndex() const {
  return CharmmMRParser::RuleNoe_assign;
}


std::any CharmmMRParser::Noe_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitNoe_assign(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Noe_assignContext* CharmmMRParser::noe_assign() {
  Noe_assignContext *_localctx = _tracker.createInstance<Noe_assignContext>(_ctx, getState());
  enterRule(_localctx, 34, CharmmMRParser::RuleNoe_assign);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(308);
    match(CharmmMRParser::Assign);
    setState(309);
    selection();
    setState(310);
    selection();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pnoe_statementContext ------------------------------------------------------------------

CharmmMRParser::Pnoe_statementContext::Pnoe_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CharmmMRParser::Pnoe_assignContext* CharmmMRParser::Pnoe_statementContext::pnoe_assign() {
  return getRuleContext<CharmmMRParser::Pnoe_assignContext>(0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::Reset() {
  return getToken(CharmmMRParser::Reset, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::KMin() {
  return getToken(CharmmMRParser::KMin, 0);
}

std::vector<CharmmMRParser::Number_sContext *> CharmmMRParser::Pnoe_statementContext::number_s() {
  return getRuleContexts<CharmmMRParser::Number_sContext>();
}

CharmmMRParser::Number_sContext* CharmmMRParser::Pnoe_statementContext::number_s(size_t i) {
  return getRuleContext<CharmmMRParser::Number_sContext>(i);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::RMin() {
  return getToken(CharmmMRParser::RMin, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::KMax() {
  return getToken(CharmmMRParser::KMax, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::RMax() {
  return getToken(CharmmMRParser::RMax, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::FMax() {
  return getToken(CharmmMRParser::FMax, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::CnoX() {
  return getToken(CharmmMRParser::CnoX, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::CnoY() {
  return getToken(CharmmMRParser::CnoY, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::CnoZ() {
  return getToken(CharmmMRParser::CnoZ, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::MinDist() {
  return getToken(CharmmMRParser::MinDist, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::RSwi() {
  return getToken(CharmmMRParser::RSwi, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::SExp() {
  return getToken(CharmmMRParser::SExp, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::SumR() {
  return getToken(CharmmMRParser::SumR, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::TCon() {
  return getToken(CharmmMRParser::TCon, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::RExp() {
  return getToken(CharmmMRParser::RExp, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::MPNoe() {
  return getToken(CharmmMRParser::MPNoe, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::INoe() {
  return getToken(CharmmMRParser::INoe, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::TnoX() {
  return getToken(CharmmMRParser::TnoX, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::TnoY() {
  return getToken(CharmmMRParser::TnoY, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::TnoZ() {
  return getToken(CharmmMRParser::TnoZ, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::NMPNoe() {
  return getToken(CharmmMRParser::NMPNoe, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::Read() {
  return getToken(CharmmMRParser::Read, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::Unit() {
  return getToken(CharmmMRParser::Unit, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::Write() {
  return getToken(CharmmMRParser::Write, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::Anal() {
  return getToken(CharmmMRParser::Anal, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::Print() {
  return getToken(CharmmMRParser::Print, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::Cut() {
  return getToken(CharmmMRParser::Cut, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::Scale() {
  return getToken(CharmmMRParser::Scale, 0);
}

tree::TerminalNode* CharmmMRParser::Pnoe_statementContext::Temperature() {
  return getToken(CharmmMRParser::Temperature, 0);
}


size_t CharmmMRParser::Pnoe_statementContext::getRuleIndex() const {
  return CharmmMRParser::RulePnoe_statement;
}


std::any CharmmMRParser::Pnoe_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitPnoe_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Pnoe_statementContext* CharmmMRParser::pnoe_statement() {
  Pnoe_statementContext *_localctx = _tracker.createInstance<Pnoe_statementContext>(_ctx, getState());
  enterRule(_localctx, 36, CharmmMRParser::RulePnoe_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(373);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Assign: {
        enterOuterAlt(_localctx, 1);
        setState(312);
        pnoe_assign();
        break;
      }

      case CharmmMRParser::Reset: {
        enterOuterAlt(_localctx, 2);
        setState(313);
        match(CharmmMRParser::Reset);
        break;
      }

      case CharmmMRParser::KMin: {
        enterOuterAlt(_localctx, 3);
        setState(314);
        match(CharmmMRParser::KMin);
        setState(315);
        number_s();
        break;
      }

      case CharmmMRParser::RMin: {
        enterOuterAlt(_localctx, 4);
        setState(316);
        match(CharmmMRParser::RMin);
        setState(317);
        number_s();
        break;
      }

      case CharmmMRParser::KMax: {
        enterOuterAlt(_localctx, 5);
        setState(318);
        match(CharmmMRParser::KMax);
        setState(319);
        number_s();
        break;
      }

      case CharmmMRParser::RMax: {
        enterOuterAlt(_localctx, 6);
        setState(320);
        match(CharmmMRParser::RMax);
        setState(321);
        number_s();
        break;
      }

      case CharmmMRParser::FMax: {
        enterOuterAlt(_localctx, 7);
        setState(322);
        match(CharmmMRParser::FMax);
        setState(323);
        number_s();
        break;
      }

      case CharmmMRParser::CnoX: {
        enterOuterAlt(_localctx, 8);
        setState(324);
        match(CharmmMRParser::CnoX);
        setState(325);
        number_s();
        break;
      }

      case CharmmMRParser::CnoY: {
        enterOuterAlt(_localctx, 9);
        setState(326);
        match(CharmmMRParser::CnoY);
        setState(327);
        number_s();
        break;
      }

      case CharmmMRParser::CnoZ: {
        enterOuterAlt(_localctx, 10);
        setState(328);
        match(CharmmMRParser::CnoZ);
        setState(329);
        number_s();
        break;
      }

      case CharmmMRParser::MinDist: {
        enterOuterAlt(_localctx, 11);
        setState(330);
        match(CharmmMRParser::MinDist);
        break;
      }

      case CharmmMRParser::RSwi: {
        enterOuterAlt(_localctx, 12);
        setState(331);
        match(CharmmMRParser::RSwi);
        setState(332);
        number_s();
        break;
      }

      case CharmmMRParser::SExp: {
        enterOuterAlt(_localctx, 13);
        setState(333);
        match(CharmmMRParser::SExp);
        setState(334);
        number_s();
        break;
      }

      case CharmmMRParser::SumR: {
        enterOuterAlt(_localctx, 14);
        setState(335);
        match(CharmmMRParser::SumR);
        break;
      }

      case CharmmMRParser::TCon: {
        enterOuterAlt(_localctx, 15);
        setState(336);
        match(CharmmMRParser::TCon);
        setState(337);
        number_s();
        break;
      }

      case CharmmMRParser::RExp: {
        enterOuterAlt(_localctx, 16);
        setState(338);
        match(CharmmMRParser::RExp);
        setState(339);
        number_s();
        break;
      }

      case CharmmMRParser::MPNoe: {
        enterOuterAlt(_localctx, 17);
        setState(340);
        match(CharmmMRParser::MPNoe);
        setState(341);
        match(CharmmMRParser::INoe);
        setState(342);
        match(CharmmMRParser::Integer);
        setState(343);
        match(CharmmMRParser::TnoX);
        setState(344);
        number_s();
        setState(345);
        match(CharmmMRParser::TnoY);
        setState(346);
        number_s();
        setState(347);
        match(CharmmMRParser::TnoZ);
        setState(348);
        number_s();
        break;
      }

      case CharmmMRParser::NMPNoe: {
        enterOuterAlt(_localctx, 18);
        setState(350);
        match(CharmmMRParser::NMPNoe);
        setState(351);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::Read: {
        enterOuterAlt(_localctx, 19);
        setState(352);
        match(CharmmMRParser::Read);
        setState(353);
        match(CharmmMRParser::Unit);
        setState(354);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::Write: {
        enterOuterAlt(_localctx, 20);
        setState(355);
        match(CharmmMRParser::Write);
        setState(356);
        match(CharmmMRParser::Unit);
        setState(357);
        match(CharmmMRParser::Integer);
        setState(359);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CharmmMRParser::Anal) {
          setState(358);
          match(CharmmMRParser::Anal);
        }
        break;
      }

      case CharmmMRParser::Print: {
        enterOuterAlt(_localctx, 21);
        setState(361);
        match(CharmmMRParser::Print);
        setState(367);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CharmmMRParser::Anal) {
          setState(362);
          match(CharmmMRParser::Anal);
          setState(365);
          _errHandler->sync(this);

          _la = _input->LA(1);
          if (_la == CharmmMRParser::Cut) {
            setState(363);
            match(CharmmMRParser::Cut);
            setState(364);
            number_s();
          }
        }
        break;
      }

      case CharmmMRParser::Scale: {
        enterOuterAlt(_localctx, 22);
        setState(369);
        match(CharmmMRParser::Scale);
        setState(370);
        number_s();
        break;
      }

      case CharmmMRParser::Temperature: {
        enterOuterAlt(_localctx, 23);
        setState(371);
        match(CharmmMRParser::Temperature);
        setState(372);
        number_s();
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

//----------------- Pnoe_assignContext ------------------------------------------------------------------

CharmmMRParser::Pnoe_assignContext::Pnoe_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Pnoe_assignContext::Assign() {
  return getToken(CharmmMRParser::Assign, 0);
}

CharmmMRParser::SelectionContext* CharmmMRParser::Pnoe_assignContext::selection() {
  return getRuleContext<CharmmMRParser::SelectionContext>(0);
}


size_t CharmmMRParser::Pnoe_assignContext::getRuleIndex() const {
  return CharmmMRParser::RulePnoe_assign;
}


std::any CharmmMRParser::Pnoe_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitPnoe_assign(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Pnoe_assignContext* CharmmMRParser::pnoe_assign() {
  Pnoe_assignContext *_localctx = _tracker.createInstance<Pnoe_assignContext>(_ctx, getState());
  enterRule(_localctx, 38, CharmmMRParser::RulePnoe_assign);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(375);
    match(CharmmMRParser::Assign);
    setState(376);
    selection();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_statementContext ------------------------------------------------------------------

CharmmMRParser::Dihedral_statementContext::Dihedral_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CharmmMRParser::Dihedral_assignContext* CharmmMRParser::Dihedral_statementContext::dihedral_assign() {
  return getRuleContext<CharmmMRParser::Dihedral_assignContext>(0);
}

tree::TerminalNode* CharmmMRParser::Dihedral_statementContext::Force() {
  return getToken(CharmmMRParser::Force, 0);
}

CharmmMRParser::Number_sContext* CharmmMRParser::Dihedral_statementContext::number_s() {
  return getRuleContext<CharmmMRParser::Number_sContext>(0);
}

tree::TerminalNode* CharmmMRParser::Dihedral_statementContext::Min() {
  return getToken(CharmmMRParser::Min, 0);
}

tree::TerminalNode* CharmmMRParser::Dihedral_statementContext::Period() {
  return getToken(CharmmMRParser::Period, 0);
}

tree::TerminalNode* CharmmMRParser::Dihedral_statementContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::Dihedral_statementContext::Comp() {
  return getToken(CharmmMRParser::Comp, 0);
}

tree::TerminalNode* CharmmMRParser::Dihedral_statementContext::Width() {
  return getToken(CharmmMRParser::Width, 0);
}

tree::TerminalNode* CharmmMRParser::Dihedral_statementContext::Main() {
  return getToken(CharmmMRParser::Main, 0);
}


size_t CharmmMRParser::Dihedral_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleDihedral_statement;
}


std::any CharmmMRParser::Dihedral_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Dihedral_statementContext* CharmmMRParser::dihedral_statement() {
  Dihedral_statementContext *_localctx = _tracker.createInstance<Dihedral_statementContext>(_ctx, getState());
  enterRule(_localctx, 40, CharmmMRParser::RuleDihedral_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(389);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::ByNumber:
      case CharmmMRParser::Selection:
      case CharmmMRParser::Integer:
      case CharmmMRParser::Simple_name: {
        enterOuterAlt(_localctx, 1);
        setState(378);
        dihedral_assign();
        break;
      }

      case CharmmMRParser::Force: {
        enterOuterAlt(_localctx, 2);
        setState(379);
        match(CharmmMRParser::Force);
        setState(380);
        number_s();
        break;
      }

      case CharmmMRParser::Min: {
        enterOuterAlt(_localctx, 3);
        setState(381);
        match(CharmmMRParser::Min);
        setState(382);
        number_s();
        break;
      }

      case CharmmMRParser::Period: {
        enterOuterAlt(_localctx, 4);
        setState(383);
        match(CharmmMRParser::Period);
        setState(384);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::Comp: {
        enterOuterAlt(_localctx, 5);
        setState(385);
        match(CharmmMRParser::Comp);
        break;
      }

      case CharmmMRParser::Width: {
        enterOuterAlt(_localctx, 6);
        setState(386);
        match(CharmmMRParser::Width);
        setState(387);
        number_s();
        break;
      }

      case CharmmMRParser::Main: {
        enterOuterAlt(_localctx, 7);
        setState(388);
        match(CharmmMRParser::Main);
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

//----------------- Dihedral_assignContext ------------------------------------------------------------------

CharmmMRParser::Dihedral_assignContext::Dihedral_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CharmmMRParser::SelectionContext *> CharmmMRParser::Dihedral_assignContext::selection() {
  return getRuleContexts<CharmmMRParser::SelectionContext>();
}

CharmmMRParser::SelectionContext* CharmmMRParser::Dihedral_assignContext::selection(size_t i) {
  return getRuleContext<CharmmMRParser::SelectionContext>(i);
}

tree::TerminalNode* CharmmMRParser::Dihedral_assignContext::ByNumber() {
  return getToken(CharmmMRParser::ByNumber, 0);
}

std::vector<tree::TerminalNode *> CharmmMRParser::Dihedral_assignContext::Integer() {
  return getTokens(CharmmMRParser::Integer);
}

tree::TerminalNode* CharmmMRParser::Dihedral_assignContext::Integer(size_t i) {
  return getToken(CharmmMRParser::Integer, i);
}

std::vector<tree::TerminalNode *> CharmmMRParser::Dihedral_assignContext::Simple_name() {
  return getTokens(CharmmMRParser::Simple_name);
}

tree::TerminalNode* CharmmMRParser::Dihedral_assignContext::Simple_name(size_t i) {
  return getToken(CharmmMRParser::Simple_name, i);
}


size_t CharmmMRParser::Dihedral_assignContext::getRuleIndex() const {
  return CharmmMRParser::RuleDihedral_assign;
}


std::any CharmmMRParser::Dihedral_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_assign(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Dihedral_assignContext* CharmmMRParser::dihedral_assign() {
  Dihedral_assignContext *_localctx = _tracker.createInstance<Dihedral_assignContext>(_ctx, getState());
  enterRule(_localctx, 42, CharmmMRParser::RuleDihedral_assign);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(429);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 33, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(391);
      selection();
      setState(392);
      selection();
      setState(393);
      selection();
      setState(394);
      selection();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(396);
      match(CharmmMRParser::ByNumber);
      setState(397);
      match(CharmmMRParser::Integer);
      setState(398);
      match(CharmmMRParser::Integer);
      setState(399);
      match(CharmmMRParser::Integer);
      setState(400);
      match(CharmmMRParser::Integer);
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(401);
      match(CharmmMRParser::Integer);
      setState(402);
      match(CharmmMRParser::Simple_name);
      setState(403);
      match(CharmmMRParser::Integer);
      setState(404);
      match(CharmmMRParser::Simple_name);
      setState(405);
      match(CharmmMRParser::Integer);
      setState(406);
      match(CharmmMRParser::Simple_name);
      setState(407);
      match(CharmmMRParser::Integer);
      setState(408);
      match(CharmmMRParser::Simple_name);
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(410);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == CharmmMRParser::Simple_name) {
        setState(409);
        match(CharmmMRParser::Simple_name);
      }
      setState(412);
      match(CharmmMRParser::Integer);
      setState(413);
      match(CharmmMRParser::Simple_name);
      setState(415);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == CharmmMRParser::Simple_name) {
        setState(414);
        match(CharmmMRParser::Simple_name);
      }
      setState(417);
      match(CharmmMRParser::Integer);
      setState(418);
      match(CharmmMRParser::Simple_name);
      setState(420);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == CharmmMRParser::Simple_name) {
        setState(419);
        match(CharmmMRParser::Simple_name);
      }
      setState(422);
      match(CharmmMRParser::Integer);
      setState(423);
      match(CharmmMRParser::Simple_name);
      setState(425);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == CharmmMRParser::Simple_name) {
        setState(424);
        match(CharmmMRParser::Simple_name);
      }
      setState(427);
      match(CharmmMRParser::Integer);
      setState(428);
      match(CharmmMRParser::Simple_name);
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

//----------------- Harmonic_statementContext ------------------------------------------------------------------

CharmmMRParser::Harmonic_statementContext::Harmonic_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CharmmMRParser::SelectionContext *> CharmmMRParser::Harmonic_statementContext::selection() {
  return getRuleContexts<CharmmMRParser::SelectionContext>();
}

CharmmMRParser::SelectionContext* CharmmMRParser::Harmonic_statementContext::selection(size_t i) {
  return getRuleContext<CharmmMRParser::SelectionContext>(i);
}

tree::TerminalNode* CharmmMRParser::Harmonic_statementContext::Absolute() {
  return getToken(CharmmMRParser::Absolute, 0);
}

std::vector<CharmmMRParser::Absolute_specContext *> CharmmMRParser::Harmonic_statementContext::absolute_spec() {
  return getRuleContexts<CharmmMRParser::Absolute_specContext>();
}

CharmmMRParser::Absolute_specContext* CharmmMRParser::Harmonic_statementContext::absolute_spec(size_t i) {
  return getRuleContext<CharmmMRParser::Absolute_specContext>(i);
}

std::vector<CharmmMRParser::Force_const_specContext *> CharmmMRParser::Harmonic_statementContext::force_const_spec() {
  return getRuleContexts<CharmmMRParser::Force_const_specContext>();
}

CharmmMRParser::Force_const_specContext* CharmmMRParser::Harmonic_statementContext::force_const_spec(size_t i) {
  return getRuleContext<CharmmMRParser::Force_const_specContext>(i);
}

CharmmMRParser::Coordinate_specContext* CharmmMRParser::Harmonic_statementContext::coordinate_spec() {
  return getRuleContext<CharmmMRParser::Coordinate_specContext>(0);
}

tree::TerminalNode* CharmmMRParser::Harmonic_statementContext::Bestfit() {
  return getToken(CharmmMRParser::Bestfit, 0);
}

CharmmMRParser::Bestfit_specContext* CharmmMRParser::Harmonic_statementContext::bestfit_spec() {
  return getRuleContext<CharmmMRParser::Bestfit_specContext>(0);
}

tree::TerminalNode* CharmmMRParser::Harmonic_statementContext::Relative() {
  return getToken(CharmmMRParser::Relative, 0);
}

tree::TerminalNode* CharmmMRParser::Harmonic_statementContext::Clear() {
  return getToken(CharmmMRParser::Clear, 0);
}


size_t CharmmMRParser::Harmonic_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleHarmonic_statement;
}


std::any CharmmMRParser::Harmonic_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitHarmonic_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Harmonic_statementContext* CharmmMRParser::harmonic_statement() {
  Harmonic_statementContext *_localctx = _tracker.createInstance<Harmonic_statementContext>(_ctx, getState());
  enterRule(_localctx, 44, CharmmMRParser::RuleHarmonic_statement);
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
    setState(489);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Absolute:
      case CharmmMRParser::Force:
      case CharmmMRParser::Mass:
      case CharmmMRParser::Weight:
      case CharmmMRParser::Exponent:
      case CharmmMRParser::XScale:
      case CharmmMRParser::YScale:
      case CharmmMRParser::ZScale:
      case CharmmMRParser::Selection: {
        enterOuterAlt(_localctx, 1);
        setState(432);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CharmmMRParser::Absolute) {
          setState(431);
          match(CharmmMRParser::Absolute);
        }
        setState(437);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while ((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 61440) != 0)) {
          setState(434);
          absolute_spec();
          setState(439);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        setState(443);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while ((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 3584) != 0)) {
          setState(440);
          force_const_spec();
          setState(445);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        setState(446);
        selection();
        setState(450);
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 37, _ctx);
        while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
          if (alt == 1) {
            setState(447);
            force_const_spec(); 
          }
          setState(452);
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 37, _ctx);
        }
        setState(454);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if ((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 1835008) != 0)) {
          setState(453);
          coordinate_spec();
        }
        break;
      }

      case CharmmMRParser::Bestfit: {
        enterOuterAlt(_localctx, 2);
        setState(456);
        match(CharmmMRParser::Bestfit);
        setState(458);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CharmmMRParser::NoRotation

        || _la == CharmmMRParser::NoTranslation) {
          setState(457);
          bestfit_spec();
        }
        setState(463);
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 40, _ctx);
        while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
          if (alt == 1) {
            setState(460);
            force_const_spec(); 
          }
          setState(465);
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 40, _ctx);
        }
        setState(467);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if ((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 1835008) != 0)) {
          setState(466);
          coordinate_spec();
        }
        break;
      }

      case CharmmMRParser::Relative: {
        enterOuterAlt(_localctx, 3);
        setState(469);
        match(CharmmMRParser::Relative);
        setState(471);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CharmmMRParser::NoRotation

        || _la == CharmmMRParser::NoTranslation) {
          setState(470);
          bestfit_spec();
        }
        setState(476);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while ((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 3584) != 0)) {
          setState(473);
          force_const_spec();
          setState(478);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        setState(479);
        selection();
        setState(483);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while ((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 3584) != 0)) {
          setState(480);
          force_const_spec();
          setState(485);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        setState(486);
        selection();
        break;
      }

      case CharmmMRParser::Clear: {
        enterOuterAlt(_localctx, 4);
        setState(488);
        match(CharmmMRParser::Clear);
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

//----------------- Absolute_specContext ------------------------------------------------------------------

CharmmMRParser::Absolute_specContext::Absolute_specContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Absolute_specContext::Exponent() {
  return getToken(CharmmMRParser::Exponent, 0);
}

tree::TerminalNode* CharmmMRParser::Absolute_specContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::Absolute_specContext::XScale() {
  return getToken(CharmmMRParser::XScale, 0);
}

CharmmMRParser::NumberContext* CharmmMRParser::Absolute_specContext::number() {
  return getRuleContext<CharmmMRParser::NumberContext>(0);
}

tree::TerminalNode* CharmmMRParser::Absolute_specContext::YScale() {
  return getToken(CharmmMRParser::YScale, 0);
}

tree::TerminalNode* CharmmMRParser::Absolute_specContext::ZScale() {
  return getToken(CharmmMRParser::ZScale, 0);
}


size_t CharmmMRParser::Absolute_specContext::getRuleIndex() const {
  return CharmmMRParser::RuleAbsolute_spec;
}


std::any CharmmMRParser::Absolute_specContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitAbsolute_spec(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Absolute_specContext* CharmmMRParser::absolute_spec() {
  Absolute_specContext *_localctx = _tracker.createInstance<Absolute_specContext>(_ctx, getState());
  enterRule(_localctx, 46, CharmmMRParser::RuleAbsolute_spec);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(499);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Exponent: {
        enterOuterAlt(_localctx, 1);
        setState(491);
        match(CharmmMRParser::Exponent);
        setState(492);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::XScale: {
        enterOuterAlt(_localctx, 2);
        setState(493);
        match(CharmmMRParser::XScale);
        setState(494);
        number();
        break;
      }

      case CharmmMRParser::YScale: {
        enterOuterAlt(_localctx, 3);
        setState(495);
        match(CharmmMRParser::YScale);
        setState(496);
        number();
        break;
      }

      case CharmmMRParser::ZScale: {
        enterOuterAlt(_localctx, 4);
        setState(497);
        match(CharmmMRParser::ZScale);
        setState(498);
        number();
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

//----------------- Force_const_specContext ------------------------------------------------------------------

CharmmMRParser::Force_const_specContext::Force_const_specContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Force_const_specContext::Force() {
  return getToken(CharmmMRParser::Force, 0);
}

CharmmMRParser::NumberContext* CharmmMRParser::Force_const_specContext::number() {
  return getRuleContext<CharmmMRParser::NumberContext>(0);
}

tree::TerminalNode* CharmmMRParser::Force_const_specContext::Mass() {
  return getToken(CharmmMRParser::Mass, 0);
}

tree::TerminalNode* CharmmMRParser::Force_const_specContext::Weight() {
  return getToken(CharmmMRParser::Weight, 0);
}


size_t CharmmMRParser::Force_const_specContext::getRuleIndex() const {
  return CharmmMRParser::RuleForce_const_spec;
}


std::any CharmmMRParser::Force_const_specContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitForce_const_spec(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Force_const_specContext* CharmmMRParser::force_const_spec() {
  Force_const_specContext *_localctx = _tracker.createInstance<Force_const_specContext>(_ctx, getState());
  enterRule(_localctx, 48, CharmmMRParser::RuleForce_const_spec);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(505);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Force: {
        enterOuterAlt(_localctx, 1);
        setState(501);
        match(CharmmMRParser::Force);
        setState(502);
        number();
        break;
      }

      case CharmmMRParser::Mass: {
        enterOuterAlt(_localctx, 2);
        setState(503);
        match(CharmmMRParser::Mass);
        break;
      }

      case CharmmMRParser::Weight: {
        enterOuterAlt(_localctx, 3);
        setState(504);
        match(CharmmMRParser::Weight);
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

//----------------- Bestfit_specContext ------------------------------------------------------------------

CharmmMRParser::Bestfit_specContext::Bestfit_specContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Bestfit_specContext::NoRotation() {
  return getToken(CharmmMRParser::NoRotation, 0);
}

tree::TerminalNode* CharmmMRParser::Bestfit_specContext::NoTranslation() {
  return getToken(CharmmMRParser::NoTranslation, 0);
}


size_t CharmmMRParser::Bestfit_specContext::getRuleIndex() const {
  return CharmmMRParser::RuleBestfit_spec;
}


std::any CharmmMRParser::Bestfit_specContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitBestfit_spec(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Bestfit_specContext* CharmmMRParser::bestfit_spec() {
  Bestfit_specContext *_localctx = _tracker.createInstance<Bestfit_specContext>(_ctx, getState());
  enterRule(_localctx, 50, CharmmMRParser::RuleBestfit_spec);
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
    setState(507);
    _la = _input->LA(1);
    if (!(_la == CharmmMRParser::NoRotation

    || _la == CharmmMRParser::NoTranslation)) {
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

//----------------- Coordinate_specContext ------------------------------------------------------------------

CharmmMRParser::Coordinate_specContext::Coordinate_specContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Coordinate_specContext::Main() {
  return getToken(CharmmMRParser::Main, 0);
}

tree::TerminalNode* CharmmMRParser::Coordinate_specContext::Comp() {
  return getToken(CharmmMRParser::Comp, 0);
}

tree::TerminalNode* CharmmMRParser::Coordinate_specContext::Keep() {
  return getToken(CharmmMRParser::Keep, 0);
}


size_t CharmmMRParser::Coordinate_specContext::getRuleIndex() const {
  return CharmmMRParser::RuleCoordinate_spec;
}


std::any CharmmMRParser::Coordinate_specContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitCoordinate_spec(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Coordinate_specContext* CharmmMRParser::coordinate_spec() {
  Coordinate_specContext *_localctx = _tracker.createInstance<Coordinate_specContext>(_ctx, getState());
  enterRule(_localctx, 52, CharmmMRParser::RuleCoordinate_spec);
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
    setState(509);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1835008) != 0))) {
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

//----------------- Ic_statementContext ------------------------------------------------------------------

CharmmMRParser::Ic_statementContext::Ic_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Ic_statementContext::Bond() {
  return getToken(CharmmMRParser::Bond, 0);
}

CharmmMRParser::NumberContext* CharmmMRParser::Ic_statementContext::number() {
  return getRuleContext<CharmmMRParser::NumberContext>(0);
}

tree::TerminalNode* CharmmMRParser::Ic_statementContext::Exponent() {
  return getToken(CharmmMRParser::Exponent, 0);
}

tree::TerminalNode* CharmmMRParser::Ic_statementContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::Ic_statementContext::Upper() {
  return getToken(CharmmMRParser::Upper, 0);
}

tree::TerminalNode* CharmmMRParser::Ic_statementContext::Angle() {
  return getToken(CharmmMRParser::Angle, 0);
}

tree::TerminalNode* CharmmMRParser::Ic_statementContext::Dihedral() {
  return getToken(CharmmMRParser::Dihedral, 0);
}

tree::TerminalNode* CharmmMRParser::Ic_statementContext::Improper() {
  return getToken(CharmmMRParser::Improper, 0);
}


size_t CharmmMRParser::Ic_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleIc_statement;
}


std::any CharmmMRParser::Ic_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitIc_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Ic_statementContext* CharmmMRParser::ic_statement() {
  Ic_statementContext *_localctx = _tracker.createInstance<Ic_statementContext>(_ctx, getState());
  enterRule(_localctx, 54, CharmmMRParser::RuleIc_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(526);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Bond: {
        enterOuterAlt(_localctx, 1);
        setState(511);
        match(CharmmMRParser::Bond);
        setState(512);
        number();
        setState(515);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CharmmMRParser::Exponent) {
          setState(513);
          match(CharmmMRParser::Exponent);
          setState(514);
          match(CharmmMRParser::Integer);
        }
        setState(518);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CharmmMRParser::Upper) {
          setState(517);
          match(CharmmMRParser::Upper);
        }
        break;
      }

      case CharmmMRParser::Angle: {
        enterOuterAlt(_localctx, 2);
        setState(520);
        match(CharmmMRParser::Angle);
        setState(521);
        number();
        break;
      }

      case CharmmMRParser::Dihedral: {
        enterOuterAlt(_localctx, 3);
        setState(522);
        match(CharmmMRParser::Dihedral);
        setState(523);
        number();
        break;
      }

      case CharmmMRParser::Improper: {
        enterOuterAlt(_localctx, 4);
        setState(524);
        match(CharmmMRParser::Improper);
        setState(525);
        number();
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

//----------------- Droplet_statementContext ------------------------------------------------------------------

CharmmMRParser::Droplet_statementContext::Droplet_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Droplet_statementContext::Force() {
  return getToken(CharmmMRParser::Force, 0);
}

CharmmMRParser::NumberContext* CharmmMRParser::Droplet_statementContext::number() {
  return getRuleContext<CharmmMRParser::NumberContext>(0);
}

tree::TerminalNode* CharmmMRParser::Droplet_statementContext::Exponent() {
  return getToken(CharmmMRParser::Exponent, 0);
}

tree::TerminalNode* CharmmMRParser::Droplet_statementContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::Droplet_statementContext::NoMass() {
  return getToken(CharmmMRParser::NoMass, 0);
}


size_t CharmmMRParser::Droplet_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleDroplet_statement;
}


std::any CharmmMRParser::Droplet_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitDroplet_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Droplet_statementContext* CharmmMRParser::droplet_statement() {
  Droplet_statementContext *_localctx = _tracker.createInstance<Droplet_statementContext>(_ctx, getState());
  enterRule(_localctx, 56, CharmmMRParser::RuleDroplet_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(533);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Force: {
        enterOuterAlt(_localctx, 1);
        setState(528);
        match(CharmmMRParser::Force);
        setState(529);
        number();
        break;
      }

      case CharmmMRParser::Exponent: {
        enterOuterAlt(_localctx, 2);
        setState(530);
        match(CharmmMRParser::Exponent);
        setState(531);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::NoMass: {
        enterOuterAlt(_localctx, 3);
        setState(532);
        match(CharmmMRParser::NoMass);
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

//----------------- Fix_atom_statementContext ------------------------------------------------------------------

CharmmMRParser::Fix_atom_statementContext::Fix_atom_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CharmmMRParser::SelectionContext* CharmmMRParser::Fix_atom_statementContext::selection() {
  return getRuleContext<CharmmMRParser::SelectionContext>(0);
}

tree::TerminalNode* CharmmMRParser::Fix_atom_statementContext::Purg() {
  return getToken(CharmmMRParser::Purg, 0);
}

tree::TerminalNode* CharmmMRParser::Fix_atom_statementContext::Bond() {
  return getToken(CharmmMRParser::Bond, 0);
}

tree::TerminalNode* CharmmMRParser::Fix_atom_statementContext::Thet() {
  return getToken(CharmmMRParser::Thet, 0);
}

tree::TerminalNode* CharmmMRParser::Fix_atom_statementContext::Phi() {
  return getToken(CharmmMRParser::Phi, 0);
}

tree::TerminalNode* CharmmMRParser::Fix_atom_statementContext::Imph() {
  return getToken(CharmmMRParser::Imph, 0);
}


size_t CharmmMRParser::Fix_atom_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleFix_atom_statement;
}


std::any CharmmMRParser::Fix_atom_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitFix_atom_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Fix_atom_statementContext* CharmmMRParser::fix_atom_statement() {
  Fix_atom_statementContext *_localctx = _tracker.createInstance<Fix_atom_statementContext>(_ctx, getState());
  enterRule(_localctx, 58, CharmmMRParser::RuleFix_atom_statement);
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
    setState(535);
    selection();
    setState(537);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CharmmMRParser::Purg) {
      setState(536);
      match(CharmmMRParser::Purg);
    }
    setState(540);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CharmmMRParser::Bond) {
      setState(539);
      match(CharmmMRParser::Bond);
    }
    setState(543);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CharmmMRParser::Thet) {
      setState(542);
      match(CharmmMRParser::Thet);
    }
    setState(546);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CharmmMRParser::Phi) {
      setState(545);
      match(CharmmMRParser::Phi);
    }
    setState(549);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CharmmMRParser::Imph) {
      setState(548);
      match(CharmmMRParser::Imph);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Center_of_mass_statementContext ------------------------------------------------------------------

CharmmMRParser::Center_of_mass_statementContext::Center_of_mass_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Center_of_mass_statementContext::Force() {
  return getToken(CharmmMRParser::Force, 0);
}

std::vector<CharmmMRParser::NumberContext *> CharmmMRParser::Center_of_mass_statementContext::number() {
  return getRuleContexts<CharmmMRParser::NumberContext>();
}

CharmmMRParser::NumberContext* CharmmMRParser::Center_of_mass_statementContext::number(size_t i) {
  return getRuleContext<CharmmMRParser::NumberContext>(i);
}

tree::TerminalNode* CharmmMRParser::Center_of_mass_statementContext::RefX() {
  return getToken(CharmmMRParser::RefX, 0);
}

tree::TerminalNode* CharmmMRParser::Center_of_mass_statementContext::RefY() {
  return getToken(CharmmMRParser::RefY, 0);
}

tree::TerminalNode* CharmmMRParser::Center_of_mass_statementContext::RefZ() {
  return getToken(CharmmMRParser::RefZ, 0);
}

CharmmMRParser::SelectionContext* CharmmMRParser::Center_of_mass_statementContext::selection() {
  return getRuleContext<CharmmMRParser::SelectionContext>(0);
}

tree::TerminalNode* CharmmMRParser::Center_of_mass_statementContext::Weight() {
  return getToken(CharmmMRParser::Weight, 0);
}


size_t CharmmMRParser::Center_of_mass_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleCenter_of_mass_statement;
}


std::any CharmmMRParser::Center_of_mass_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitCenter_of_mass_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Center_of_mass_statementContext* CharmmMRParser::center_of_mass_statement() {
  Center_of_mass_statementContext *_localctx = _tracker.createInstance<Center_of_mass_statementContext>(_ctx, getState());
  enterRule(_localctx, 60, CharmmMRParser::RuleCenter_of_mass_statement);
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
    setState(551);
    match(CharmmMRParser::Force);
    setState(552);
    number();
    setState(554);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CharmmMRParser::Weight) {
      setState(553);
      match(CharmmMRParser::Weight);
    }
    setState(556);
    match(CharmmMRParser::RefX);
    setState(557);
    number();
    setState(558);
    match(CharmmMRParser::RefY);
    setState(559);
    number();
    setState(560);
    match(CharmmMRParser::RefZ);
    setState(561);
    number();
    setState(562);
    selection();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fix_bond_or_angle_statementContext ------------------------------------------------------------------

CharmmMRParser::Fix_bond_or_angle_statementContext::Fix_bond_or_angle_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CharmmMRParser::SelectionContext *> CharmmMRParser::Fix_bond_or_angle_statementContext::selection() {
  return getRuleContexts<CharmmMRParser::SelectionContext>();
}

CharmmMRParser::SelectionContext* CharmmMRParser::Fix_bond_or_angle_statementContext::selection(size_t i) {
  return getRuleContext<CharmmMRParser::SelectionContext>(i);
}

CharmmMRParser::Shake_optContext* CharmmMRParser::Fix_bond_or_angle_statementContext::shake_opt() {
  return getRuleContext<CharmmMRParser::Shake_optContext>(0);
}

CharmmMRParser::Fast_optContext* CharmmMRParser::Fix_bond_or_angle_statementContext::fast_opt() {
  return getRuleContext<CharmmMRParser::Fast_optContext>(0);
}

tree::TerminalNode* CharmmMRParser::Fix_bond_or_angle_statementContext::NoReset() {
  return getToken(CharmmMRParser::NoReset, 0);
}


size_t CharmmMRParser::Fix_bond_or_angle_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleFix_bond_or_angle_statement;
}


std::any CharmmMRParser::Fix_bond_or_angle_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitFix_bond_or_angle_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Fix_bond_or_angle_statementContext* CharmmMRParser::fix_bond_or_angle_statement() {
  Fix_bond_or_angle_statementContext *_localctx = _tracker.createInstance<Fix_bond_or_angle_statementContext>(_ctx, getState());
  enterRule(_localctx, 62, CharmmMRParser::RuleFix_bond_or_angle_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(570);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Selection: {
        enterOuterAlt(_localctx, 1);
        setState(564);
        selection();
        setState(565);
        selection();
        setState(566);
        shake_opt();
        break;
      }

      case CharmmMRParser::Fast:
      case CharmmMRParser::NoFast: {
        enterOuterAlt(_localctx, 2);
        setState(568);
        fast_opt();
        break;
      }

      case CharmmMRParser::NoReset: {
        enterOuterAlt(_localctx, 3);
        setState(569);
        match(CharmmMRParser::NoReset);
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

//----------------- Shake_optContext ------------------------------------------------------------------

CharmmMRParser::Shake_optContext::Shake_optContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Shake_optContext::BonH() {
  return getToken(CharmmMRParser::BonH, 0);
}

tree::TerminalNode* CharmmMRParser::Shake_optContext::Bond() {
  return getToken(CharmmMRParser::Bond, 0);
}

tree::TerminalNode* CharmmMRParser::Shake_optContext::AngH() {
  return getToken(CharmmMRParser::AngH, 0);
}

tree::TerminalNode* CharmmMRParser::Shake_optContext::Angle() {
  return getToken(CharmmMRParser::Angle, 0);
}

tree::TerminalNode* CharmmMRParser::Shake_optContext::Comp() {
  return getToken(CharmmMRParser::Comp, 0);
}

tree::TerminalNode* CharmmMRParser::Shake_optContext::Parameters() {
  return getToken(CharmmMRParser::Parameters, 0);
}

tree::TerminalNode* CharmmMRParser::Shake_optContext::Tol() {
  return getToken(CharmmMRParser::Tol, 0);
}

std::vector<CharmmMRParser::NumberContext *> CharmmMRParser::Shake_optContext::number() {
  return getRuleContexts<CharmmMRParser::NumberContext>();
}

CharmmMRParser::NumberContext* CharmmMRParser::Shake_optContext::number(size_t i) {
  return getRuleContext<CharmmMRParser::NumberContext>(i);
}

tree::TerminalNode* CharmmMRParser::Shake_optContext::MxIter() {
  return getToken(CharmmMRParser::MxIter, 0);
}

tree::TerminalNode* CharmmMRParser::Shake_optContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::Shake_optContext::ShkScale() {
  return getToken(CharmmMRParser::ShkScale, 0);
}

tree::TerminalNode* CharmmMRParser::Shake_optContext::Main() {
  return getToken(CharmmMRParser::Main, 0);
}


size_t CharmmMRParser::Shake_optContext::getRuleIndex() const {
  return CharmmMRParser::RuleShake_opt;
}


std::any CharmmMRParser::Shake_optContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitShake_opt(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Shake_optContext* CharmmMRParser::shake_opt() {
  Shake_optContext *_localctx = _tracker.createInstance<Shake_optContext>(_ctx, getState());
  enterRule(_localctx, 64, CharmmMRParser::RuleShake_opt);
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
    setState(572);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 633320039776256) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(578);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::EOF:
      case CharmmMRParser::Set:
      case CharmmMRParser::Cons:
      case CharmmMRParser::Main:
      case CharmmMRParser::Shake:
      case CharmmMRParser::NoReset:
      case CharmmMRParser::Tol:
      case CharmmMRParser::MxIter:
      case CharmmMRParser::ShkScale:
      case CharmmMRParser::Fast:
      case CharmmMRParser::NoFast:
      case CharmmMRParser::Noe:
      case CharmmMRParser::PNoe:
      case CharmmMRParser::ResDistance:
      case CharmmMRParser::Pull:
      case CharmmMRParser::RGyration:
      case CharmmMRParser::DMConstrain:
      case CharmmMRParser::Selection:
      case CharmmMRParser::COMMENT: {
        setState(574);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CharmmMRParser::Main) {
          setState(573);
          match(CharmmMRParser::Main);
        }
        break;
      }

      case CharmmMRParser::Comp: {
        setState(576);
        match(CharmmMRParser::Comp);
        break;
      }

      case CharmmMRParser::Parameters: {
        setState(577);
        match(CharmmMRParser::Parameters);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(582);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CharmmMRParser::Tol) {
      setState(580);
      match(CharmmMRParser::Tol);
      setState(581);
      number();
    }
    setState(586);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CharmmMRParser::MxIter) {
      setState(584);
      match(CharmmMRParser::MxIter);
      setState(585);
      match(CharmmMRParser::Integer);
    }
    setState(590);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CharmmMRParser::ShkScale) {
      setState(588);
      match(CharmmMRParser::ShkScale);
      setState(589);
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

//----------------- Fast_optContext ------------------------------------------------------------------

CharmmMRParser::Fast_optContext::Fast_optContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Fast_optContext::Fast() {
  return getToken(CharmmMRParser::Fast, 0);
}

tree::TerminalNode* CharmmMRParser::Fast_optContext::Water() {
  return getToken(CharmmMRParser::Water, 0);
}

tree::TerminalNode* CharmmMRParser::Fast_optContext::Simple_name() {
  return getToken(CharmmMRParser::Simple_name, 0);
}

tree::TerminalNode* CharmmMRParser::Fast_optContext::NoFast() {
  return getToken(CharmmMRParser::NoFast, 0);
}


size_t CharmmMRParser::Fast_optContext::getRuleIndex() const {
  return CharmmMRParser::RuleFast_opt;
}


std::any CharmmMRParser::Fast_optContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitFast_opt(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Fast_optContext* CharmmMRParser::fast_opt() {
  Fast_optContext *_localctx = _tracker.createInstance<Fast_optContext>(_ctx, getState());
  enterRule(_localctx, 66, CharmmMRParser::RuleFast_opt);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(598);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Fast: {
        enterOuterAlt(_localctx, 1);
        setState(592);
        match(CharmmMRParser::Fast);
        setState(595);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CharmmMRParser::Water) {
          setState(593);
          match(CharmmMRParser::Water);
          setState(594);
          match(CharmmMRParser::Simple_name);
        }
        break;
      }

      case CharmmMRParser::NoFast: {
        enterOuterAlt(_localctx, 2);
        setState(597);
        match(CharmmMRParser::NoFast);
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

//----------------- Restrained_distance_statementContext ------------------------------------------------------------------

CharmmMRParser::Restrained_distance_statementContext::Restrained_distance_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Restrained_distance_statementContext::Reset() {
  return getToken(CharmmMRParser::Reset, 0);
}

CharmmMRParser::NumberContext* CharmmMRParser::Restrained_distance_statementContext::number() {
  return getRuleContext<CharmmMRParser::NumberContext>(0);
}

tree::TerminalNode* CharmmMRParser::Restrained_distance_statementContext::Scale() {
  return getToken(CharmmMRParser::Scale, 0);
}

tree::TerminalNode* CharmmMRParser::Restrained_distance_statementContext::KVal() {
  return getToken(CharmmMRParser::KVal, 0);
}

tree::TerminalNode* CharmmMRParser::Restrained_distance_statementContext::RVal() {
  return getToken(CharmmMRParser::RVal, 0);
}

tree::TerminalNode* CharmmMRParser::Restrained_distance_statementContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::Restrained_distance_statementContext::EVal() {
  return getToken(CharmmMRParser::EVal, 0);
}

tree::TerminalNode* CharmmMRParser::Restrained_distance_statementContext::IVal() {
  return getToken(CharmmMRParser::IVal, 0);
}

tree::TerminalNode* CharmmMRParser::Restrained_distance_statementContext::Positive() {
  return getToken(CharmmMRParser::Positive, 0);
}

tree::TerminalNode* CharmmMRParser::Restrained_distance_statementContext::Negative() {
  return getToken(CharmmMRParser::Negative, 0);
}

std::vector<CharmmMRParser::SelectionContext *> CharmmMRParser::Restrained_distance_statementContext::selection() {
  return getRuleContexts<CharmmMRParser::SelectionContext>();
}

CharmmMRParser::SelectionContext* CharmmMRParser::Restrained_distance_statementContext::selection(size_t i) {
  return getRuleContext<CharmmMRParser::SelectionContext>(i);
}


size_t CharmmMRParser::Restrained_distance_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleRestrained_distance_statement;
}


std::any CharmmMRParser::Restrained_distance_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitRestrained_distance_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Restrained_distance_statementContext* CharmmMRParser::restrained_distance_statement() {
  Restrained_distance_statementContext *_localctx = _tracker.createInstance<Restrained_distance_statementContext>(_ctx, getState());
  enterRule(_localctx, 68, CharmmMRParser::RuleRestrained_distance_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(610);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Reset: {
        enterOuterAlt(_localctx, 1);
        setState(600);
        match(CharmmMRParser::Reset);
        break;
      }

      case CharmmMRParser::Scale:
      case CharmmMRParser::KVal:
      case CharmmMRParser::RVal: {
        enterOuterAlt(_localctx, 2);
        setState(601);
        _la = _input->LA(1);
        if (!(((((_la - 85) & ~ 0x3fULL) == 0) &&
          ((1ULL << (_la - 85)) & 25) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(602);
        number();
        break;
      }

      case CharmmMRParser::EVal:
      case CharmmMRParser::IVal: {
        enterOuterAlt(_localctx, 3);
        setState(603);
        _la = _input->LA(1);
        if (!(_la == CharmmMRParser::EVal

        || _la == CharmmMRParser::IVal)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(604);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::Positive: {
        enterOuterAlt(_localctx, 4);
        setState(605);
        match(CharmmMRParser::Positive);
        break;
      }

      case CharmmMRParser::Negative: {
        enterOuterAlt(_localctx, 5);
        setState(606);
        match(CharmmMRParser::Negative);
        break;
      }

      case CharmmMRParser::Selection: {
        enterOuterAlt(_localctx, 6);
        setState(607);
        selection();
        setState(608);
        selection();
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

//----------------- External_force_statementContext ------------------------------------------------------------------

CharmmMRParser::External_force_statementContext::External_force_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::External_force_statementContext::Force() {
  return getToken(CharmmMRParser::Force, 0);
}

CharmmMRParser::NumberContext* CharmmMRParser::External_force_statementContext::number() {
  return getRuleContext<CharmmMRParser::NumberContext>(0);
}

tree::TerminalNode* CharmmMRParser::External_force_statementContext::XDir() {
  return getToken(CharmmMRParser::XDir, 0);
}

tree::TerminalNode* CharmmMRParser::External_force_statementContext::YDir() {
  return getToken(CharmmMRParser::YDir, 0);
}

tree::TerminalNode* CharmmMRParser::External_force_statementContext::ZDir() {
  return getToken(CharmmMRParser::ZDir, 0);
}

tree::TerminalNode* CharmmMRParser::External_force_statementContext::Period() {
  return getToken(CharmmMRParser::Period, 0);
}

tree::TerminalNode* CharmmMRParser::External_force_statementContext::EField() {
  return getToken(CharmmMRParser::EField, 0);
}

tree::TerminalNode* CharmmMRParser::External_force_statementContext::SForce() {
  return getToken(CharmmMRParser::SForce, 0);
}

tree::TerminalNode* CharmmMRParser::External_force_statementContext::Off() {
  return getToken(CharmmMRParser::Off, 0);
}

tree::TerminalNode* CharmmMRParser::External_force_statementContext::List() {
  return getToken(CharmmMRParser::List, 0);
}

tree::TerminalNode* CharmmMRParser::External_force_statementContext::Switch() {
  return getToken(CharmmMRParser::Switch, 0);
}

tree::TerminalNode* CharmmMRParser::External_force_statementContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::External_force_statementContext::Weight() {
  return getToken(CharmmMRParser::Weight, 0);
}

CharmmMRParser::SelectionContext* CharmmMRParser::External_force_statementContext::selection() {
  return getRuleContext<CharmmMRParser::SelectionContext>(0);
}


size_t CharmmMRParser::External_force_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleExternal_force_statement;
}


std::any CharmmMRParser::External_force_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitExternal_force_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::External_force_statementContext* CharmmMRParser::external_force_statement() {
  External_force_statementContext *_localctx = _tracker.createInstance<External_force_statementContext>(_ctx, getState());
  enterRule(_localctx, 70, CharmmMRParser::RuleExternal_force_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(622);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Force: {
        enterOuterAlt(_localctx, 1);
        setState(612);
        match(CharmmMRParser::Force);
        setState(613);
        number();
        break;
      }

      case CharmmMRParser::Period:
      case CharmmMRParser::XDir:
      case CharmmMRParser::YDir:
      case CharmmMRParser::ZDir:
      case CharmmMRParser::EField:
      case CharmmMRParser::SForce: {
        enterOuterAlt(_localctx, 2);
        setState(614);
        _la = _input->LA(1);
        if (!(_la == CharmmMRParser::Period || ((((_la - 95) & ~ 0x3fULL) == 0) &&
          ((1ULL << (_la - 95)) & 79) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(615);
        number();
        break;
      }

      case CharmmMRParser::Off: {
        enterOuterAlt(_localctx, 3);
        setState(616);
        match(CharmmMRParser::Off);
        break;
      }

      case CharmmMRParser::List: {
        enterOuterAlt(_localctx, 4);
        setState(617);
        match(CharmmMRParser::List);
        break;
      }

      case CharmmMRParser::Switch: {
        enterOuterAlt(_localctx, 5);
        setState(618);
        match(CharmmMRParser::Switch);
        setState(619);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::Weight: {
        enterOuterAlt(_localctx, 6);
        setState(620);
        match(CharmmMRParser::Weight);
        break;
      }

      case CharmmMRParser::Selection: {
        enterOuterAlt(_localctx, 7);
        setState(621);
        selection();
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

//----------------- Rmsd_statementContext ------------------------------------------------------------------

CharmmMRParser::Rmsd_statementContext::Rmsd_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Rmsd_statementContext::Relative() {
  return getToken(CharmmMRParser::Relative, 0);
}

tree::TerminalNode* CharmmMRParser::Rmsd_statementContext::MaxN() {
  return getToken(CharmmMRParser::MaxN, 0);
}

tree::TerminalNode* CharmmMRParser::Rmsd_statementContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::Rmsd_statementContext::NPrt() {
  return getToken(CharmmMRParser::NPrt, 0);
}

CharmmMRParser::Rmsd_orient_specContext* CharmmMRParser::Rmsd_statementContext::rmsd_orient_spec() {
  return getRuleContext<CharmmMRParser::Rmsd_orient_specContext>(0);
}

CharmmMRParser::Rmsd_force_const_specContext* CharmmMRParser::Rmsd_statementContext::rmsd_force_const_spec() {
  return getRuleContext<CharmmMRParser::Rmsd_force_const_specContext>(0);
}

CharmmMRParser::Rmsd_coordinate_specContext* CharmmMRParser::Rmsd_statementContext::rmsd_coordinate_spec() {
  return getRuleContext<CharmmMRParser::Rmsd_coordinate_specContext>(0);
}

CharmmMRParser::SelectionContext* CharmmMRParser::Rmsd_statementContext::selection() {
  return getRuleContext<CharmmMRParser::SelectionContext>(0);
}


size_t CharmmMRParser::Rmsd_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleRmsd_statement;
}


std::any CharmmMRParser::Rmsd_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitRmsd_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Rmsd_statementContext* CharmmMRParser::rmsd_statement() {
  Rmsd_statementContext *_localctx = _tracker.createInstance<Rmsd_statementContext>(_ctx, getState());
  enterRule(_localctx, 72, CharmmMRParser::RuleRmsd_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(632);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Relative: {
        enterOuterAlt(_localctx, 1);
        setState(624);
        match(CharmmMRParser::Relative);
        break;
      }

      case CharmmMRParser::MaxN: {
        enterOuterAlt(_localctx, 2);
        setState(625);
        match(CharmmMRParser::MaxN);
        setState(626);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::NPrt: {
        enterOuterAlt(_localctx, 3);
        setState(627);
        match(CharmmMRParser::NPrt);
        break;
      }

      case CharmmMRParser::NoRotation:
      case CharmmMRParser::NoTranslation: {
        enterOuterAlt(_localctx, 4);
        setState(628);
        rmsd_orient_spec();
        break;
      }

      case CharmmMRParser::Force:
      case CharmmMRParser::Mass:
      case CharmmMRParser::Offset:
      case CharmmMRParser::BOffset: {
        enterOuterAlt(_localctx, 5);
        setState(629);
        rmsd_force_const_spec();
        break;
      }

      case CharmmMRParser::Main:
      case CharmmMRParser::Comp: {
        enterOuterAlt(_localctx, 6);
        setState(630);
        rmsd_coordinate_spec();
        break;
      }

      case CharmmMRParser::Selection: {
        enterOuterAlt(_localctx, 7);
        setState(631);
        selection();
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

//----------------- Rmsd_orient_specContext ------------------------------------------------------------------

CharmmMRParser::Rmsd_orient_specContext::Rmsd_orient_specContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Rmsd_orient_specContext::NoRotation() {
  return getToken(CharmmMRParser::NoRotation, 0);
}

tree::TerminalNode* CharmmMRParser::Rmsd_orient_specContext::NoTranslation() {
  return getToken(CharmmMRParser::NoTranslation, 0);
}


size_t CharmmMRParser::Rmsd_orient_specContext::getRuleIndex() const {
  return CharmmMRParser::RuleRmsd_orient_spec;
}


std::any CharmmMRParser::Rmsd_orient_specContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitRmsd_orient_spec(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Rmsd_orient_specContext* CharmmMRParser::rmsd_orient_spec() {
  Rmsd_orient_specContext *_localctx = _tracker.createInstance<Rmsd_orient_specContext>(_ctx, getState());
  enterRule(_localctx, 74, CharmmMRParser::RuleRmsd_orient_spec);
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
    setState(634);
    _la = _input->LA(1);
    if (!(_la == CharmmMRParser::NoRotation

    || _la == CharmmMRParser::NoTranslation)) {
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

//----------------- Rmsd_force_const_specContext ------------------------------------------------------------------

CharmmMRParser::Rmsd_force_const_specContext::Rmsd_force_const_specContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Rmsd_force_const_specContext::Force() {
  return getToken(CharmmMRParser::Force, 0);
}

CharmmMRParser::NumberContext* CharmmMRParser::Rmsd_force_const_specContext::number() {
  return getRuleContext<CharmmMRParser::NumberContext>(0);
}

tree::TerminalNode* CharmmMRParser::Rmsd_force_const_specContext::Mass() {
  return getToken(CharmmMRParser::Mass, 0);
}

tree::TerminalNode* CharmmMRParser::Rmsd_force_const_specContext::Offset() {
  return getToken(CharmmMRParser::Offset, 0);
}

tree::TerminalNode* CharmmMRParser::Rmsd_force_const_specContext::BOffset() {
  return getToken(CharmmMRParser::BOffset, 0);
}


size_t CharmmMRParser::Rmsd_force_const_specContext::getRuleIndex() const {
  return CharmmMRParser::RuleRmsd_force_const_spec;
}


std::any CharmmMRParser::Rmsd_force_const_specContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitRmsd_force_const_spec(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Rmsd_force_const_specContext* CharmmMRParser::rmsd_force_const_spec() {
  Rmsd_force_const_specContext *_localctx = _tracker.createInstance<Rmsd_force_const_specContext>(_ctx, getState());
  enterRule(_localctx, 76, CharmmMRParser::RuleRmsd_force_const_spec);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(643);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Force: {
        enterOuterAlt(_localctx, 1);
        setState(636);
        match(CharmmMRParser::Force);
        setState(637);
        number();
        break;
      }

      case CharmmMRParser::Mass: {
        enterOuterAlt(_localctx, 2);
        setState(638);
        match(CharmmMRParser::Mass);
        break;
      }

      case CharmmMRParser::Offset: {
        enterOuterAlt(_localctx, 3);
        setState(639);
        match(CharmmMRParser::Offset);
        setState(640);
        number();
        break;
      }

      case CharmmMRParser::BOffset: {
        enterOuterAlt(_localctx, 4);
        setState(641);
        match(CharmmMRParser::BOffset);
        setState(642);
        number();
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

//----------------- Rmsd_coordinate_specContext ------------------------------------------------------------------

CharmmMRParser::Rmsd_coordinate_specContext::Rmsd_coordinate_specContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Rmsd_coordinate_specContext::Main() {
  return getToken(CharmmMRParser::Main, 0);
}

tree::TerminalNode* CharmmMRParser::Rmsd_coordinate_specContext::Comp() {
  return getToken(CharmmMRParser::Comp, 0);
}


size_t CharmmMRParser::Rmsd_coordinate_specContext::getRuleIndex() const {
  return CharmmMRParser::RuleRmsd_coordinate_spec;
}


std::any CharmmMRParser::Rmsd_coordinate_specContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitRmsd_coordinate_spec(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Rmsd_coordinate_specContext* CharmmMRParser::rmsd_coordinate_spec() {
  Rmsd_coordinate_specContext *_localctx = _tracker.createInstance<Rmsd_coordinate_specContext>(_ctx, getState());
  enterRule(_localctx, 78, CharmmMRParser::RuleRmsd_coordinate_spec);
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
    setState(645);
    _la = _input->LA(1);
    if (!(_la == CharmmMRParser::Main

    || _la == CharmmMRParser::Comp)) {
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

//----------------- Gyration_statementContext ------------------------------------------------------------------

CharmmMRParser::Gyration_statementContext::Gyration_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Gyration_statementContext::Reset() {
  return getToken(CharmmMRParser::Reset, 0);
}

CharmmMRParser::NumberContext* CharmmMRParser::Gyration_statementContext::number() {
  return getRuleContext<CharmmMRParser::NumberContext>(0);
}

tree::TerminalNode* CharmmMRParser::Gyration_statementContext::Force() {
  return getToken(CharmmMRParser::Force, 0);
}

tree::TerminalNode* CharmmMRParser::Gyration_statementContext::Reference() {
  return getToken(CharmmMRParser::Reference, 0);
}

tree::TerminalNode* CharmmMRParser::Gyration_statementContext::RMSD() {
  return getToken(CharmmMRParser::RMSD, 0);
}

tree::TerminalNode* CharmmMRParser::Gyration_statementContext::Comp() {
  return getToken(CharmmMRParser::Comp, 0);
}

tree::TerminalNode* CharmmMRParser::Gyration_statementContext::Orient() {
  return getToken(CharmmMRParser::Orient, 0);
}

tree::TerminalNode* CharmmMRParser::Gyration_statementContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::Gyration_statementContext::Output() {
  return getToken(CharmmMRParser::Output, 0);
}

tree::TerminalNode* CharmmMRParser::Gyration_statementContext::NSave() {
  return getToken(CharmmMRParser::NSave, 0);
}

CharmmMRParser::SelectionContext* CharmmMRParser::Gyration_statementContext::selection() {
  return getRuleContext<CharmmMRParser::SelectionContext>(0);
}


size_t CharmmMRParser::Gyration_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleGyration_statement;
}


std::any CharmmMRParser::Gyration_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitGyration_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Gyration_statementContext* CharmmMRParser::gyration_statement() {
  Gyration_statementContext *_localctx = _tracker.createInstance<Gyration_statementContext>(_ctx, getState());
  enterRule(_localctx, 80, CharmmMRParser::RuleGyration_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(656);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Reset: {
        enterOuterAlt(_localctx, 1);
        setState(647);
        match(CharmmMRParser::Reset);
        break;
      }

      case CharmmMRParser::Force:
      case CharmmMRParser::Reference: {
        enterOuterAlt(_localctx, 2);
        setState(648);
        _la = _input->LA(1);
        if (!(_la == CharmmMRParser::Force || _la == CharmmMRParser::Reference)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(649);
        number();
        break;
      }

      case CharmmMRParser::RMSD: {
        enterOuterAlt(_localctx, 3);
        setState(650);
        match(CharmmMRParser::RMSD);
        break;
      }

      case CharmmMRParser::Comp: {
        enterOuterAlt(_localctx, 4);
        setState(651);
        match(CharmmMRParser::Comp);
        break;
      }

      case CharmmMRParser::Orient: {
        enterOuterAlt(_localctx, 5);
        setState(652);
        match(CharmmMRParser::Orient);
        break;
      }

      case CharmmMRParser::Output:
      case CharmmMRParser::NSave: {
        enterOuterAlt(_localctx, 6);
        setState(653);
        _la = _input->LA(1);
        if (!(_la == CharmmMRParser::Output

        || _la == CharmmMRParser::NSave)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(654);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::Selection: {
        enterOuterAlt(_localctx, 7);
        setState(655);
        selection();
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

//----------------- Distance_matrix_statementContext ------------------------------------------------------------------

CharmmMRParser::Distance_matrix_statementContext::Distance_matrix_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CharmmMRParser::NumberContext* CharmmMRParser::Distance_matrix_statementContext::number() {
  return getRuleContext<CharmmMRParser::NumberContext>(0);
}

tree::TerminalNode* CharmmMRParser::Distance_matrix_statementContext::Force() {
  return getToken(CharmmMRParser::Force, 0);
}

tree::TerminalNode* CharmmMRParser::Distance_matrix_statementContext::Reference() {
  return getToken(CharmmMRParser::Reference, 0);
}

tree::TerminalNode* CharmmMRParser::Distance_matrix_statementContext::Cutoff() {
  return getToken(CharmmMRParser::Cutoff, 0);
}

tree::TerminalNode* CharmmMRParser::Distance_matrix_statementContext::Weight() {
  return getToken(CharmmMRParser::Weight, 0);
}

tree::TerminalNode* CharmmMRParser::Distance_matrix_statementContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::Distance_matrix_statementContext::Output() {
  return getToken(CharmmMRParser::Output, 0);
}

tree::TerminalNode* CharmmMRParser::Distance_matrix_statementContext::NSave() {
  return getToken(CharmmMRParser::NSave, 0);
}

tree::TerminalNode* CharmmMRParser::Distance_matrix_statementContext::NContact() {
  return getToken(CharmmMRParser::NContact, 0);
}

CharmmMRParser::SelectionContext* CharmmMRParser::Distance_matrix_statementContext::selection() {
  return getRuleContext<CharmmMRParser::SelectionContext>(0);
}


size_t CharmmMRParser::Distance_matrix_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleDistance_matrix_statement;
}


std::any CharmmMRParser::Distance_matrix_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_matrix_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Distance_matrix_statementContext* CharmmMRParser::distance_matrix_statement() {
  Distance_matrix_statementContext *_localctx = _tracker.createInstance<Distance_matrix_statementContext>(_ctx, getState());
  enterRule(_localctx, 82, CharmmMRParser::RuleDistance_matrix_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(663);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::Force:
      case CharmmMRParser::Weight:
      case CharmmMRParser::Reference:
      case CharmmMRParser::Cutoff: {
        enterOuterAlt(_localctx, 1);
        setState(658);
        _la = _input->LA(1);
        if (!(_la == CharmmMRParser::Force

        || _la == CharmmMRParser::Weight || _la == CharmmMRParser::Reference

        || _la == CharmmMRParser::Cutoff)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(659);
        number();
        break;
      }

      case CharmmMRParser::Output:
      case CharmmMRParser::NSave:
      case CharmmMRParser::NContact: {
        enterOuterAlt(_localctx, 2);
        setState(660);
        _la = _input->LA(1);
        if (!(((((_la - 111) & ~ 0x3fULL) == 0) &&
          ((1ULL << (_la - 111)) & 19) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(661);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::Selection: {
        enterOuterAlt(_localctx, 3);
        setState(662);
        selection();
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

//----------------- SelectionContext ------------------------------------------------------------------

CharmmMRParser::SelectionContext::SelectionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::SelectionContext::Selection() {
  return getToken(CharmmMRParser::Selection, 0);
}

CharmmMRParser::Selection_expressionContext* CharmmMRParser::SelectionContext::selection_expression() {
  return getRuleContext<CharmmMRParser::Selection_expressionContext>(0);
}

tree::TerminalNode* CharmmMRParser::SelectionContext::End() {
  return getToken(CharmmMRParser::End, 0);
}

tree::TerminalNode* CharmmMRParser::SelectionContext::Show() {
  return getToken(CharmmMRParser::Show, 0);
}


size_t CharmmMRParser::SelectionContext::getRuleIndex() const {
  return CharmmMRParser::RuleSelection;
}


std::any CharmmMRParser::SelectionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitSelection(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::SelectionContext* CharmmMRParser::selection() {
  SelectionContext *_localctx = _tracker.createInstance<SelectionContext>(_ctx, getState());
  enterRule(_localctx, 84, CharmmMRParser::RuleSelection);
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
    setState(665);
    match(CharmmMRParser::Selection);
    setState(666);
    selection_expression();
    setState(668);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CharmmMRParser::Show) {
      setState(667);
      match(CharmmMRParser::Show);
    }
    setState(670);
    match(CharmmMRParser::End);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Selection_expressionContext ------------------------------------------------------------------

CharmmMRParser::Selection_expressionContext::Selection_expressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CharmmMRParser::TermContext *> CharmmMRParser::Selection_expressionContext::term() {
  return getRuleContexts<CharmmMRParser::TermContext>();
}

CharmmMRParser::TermContext* CharmmMRParser::Selection_expressionContext::term(size_t i) {
  return getRuleContext<CharmmMRParser::TermContext>(i);
}

std::vector<tree::TerminalNode *> CharmmMRParser::Selection_expressionContext::Or_op() {
  return getTokens(CharmmMRParser::Or_op);
}

tree::TerminalNode* CharmmMRParser::Selection_expressionContext::Or_op(size_t i) {
  return getToken(CharmmMRParser::Or_op, i);
}


size_t CharmmMRParser::Selection_expressionContext::getRuleIndex() const {
  return CharmmMRParser::RuleSelection_expression;
}


std::any CharmmMRParser::Selection_expressionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitSelection_expression(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Selection_expressionContext* CharmmMRParser::selection_expression() {
  Selection_expressionContext *_localctx = _tracker.createInstance<Selection_expressionContext>(_ctx, getState());
  enterRule(_localctx, 86, CharmmMRParser::RuleSelection_expression);
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
    setState(672);
    term();
    setState(677);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CharmmMRParser::Or_op) {
      setState(673);
      match(CharmmMRParser::Or_op);
      setState(674);
      term();
      setState(679);
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

//----------------- TermContext ------------------------------------------------------------------

CharmmMRParser::TermContext::TermContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CharmmMRParser::FactorContext *> CharmmMRParser::TermContext::factor() {
  return getRuleContexts<CharmmMRParser::FactorContext>();
}

CharmmMRParser::FactorContext* CharmmMRParser::TermContext::factor(size_t i) {
  return getRuleContext<CharmmMRParser::FactorContext>(i);
}

std::vector<tree::TerminalNode *> CharmmMRParser::TermContext::And_op() {
  return getTokens(CharmmMRParser::And_op);
}

tree::TerminalNode* CharmmMRParser::TermContext::And_op(size_t i) {
  return getToken(CharmmMRParser::And_op, i);
}


size_t CharmmMRParser::TermContext::getRuleIndex() const {
  return CharmmMRParser::RuleTerm;
}


std::any CharmmMRParser::TermContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitTerm(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::TermContext* CharmmMRParser::term() {
  TermContext *_localctx = _tracker.createInstance<TermContext>(_ctx, getState());
  enterRule(_localctx, 88, CharmmMRParser::RuleTerm);
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
    setState(680);
    factor(0);
    setState(685);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CharmmMRParser::And_op) {
      setState(681);
      match(CharmmMRParser::And_op);
      setState(682);
      factor(0);
      setState(687);
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

//----------------- FactorContext ------------------------------------------------------------------

CharmmMRParser::FactorContext::FactorContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::FactorContext::L_paren() {
  return getToken(CharmmMRParser::L_paren, 0);
}

CharmmMRParser::Selection_expressionContext* CharmmMRParser::FactorContext::selection_expression() {
  return getRuleContext<CharmmMRParser::Selection_expressionContext>(0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::R_paren() {
  return getToken(CharmmMRParser::R_paren, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::All() {
  return getToken(CharmmMRParser::All, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Atom() {
  return getToken(CharmmMRParser::Atom, 0);
}

std::vector<tree::TerminalNode *> CharmmMRParser::FactorContext::Simple_names() {
  return getTokens(CharmmMRParser::Simple_names);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Simple_names(size_t i) {
  return getToken(CharmmMRParser::Simple_names, i);
}

std::vector<tree::TerminalNode *> CharmmMRParser::FactorContext::Simple_name() {
  return getTokens(CharmmMRParser::Simple_name);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Simple_name(size_t i) {
  return getToken(CharmmMRParser::Simple_name, i);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Integers() {
  return getToken(CharmmMRParser::Integers, 0);
}

std::vector<tree::TerminalNode *> CharmmMRParser::FactorContext::Integer() {
  return getTokens(CharmmMRParser::Integer);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Integer(size_t i) {
  return getToken(CharmmMRParser::Integer, i);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Property() {
  return getToken(CharmmMRParser::Property, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Attr_properties() {
  return getToken(CharmmMRParser::Attr_properties, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Comparison_ops() {
  return getToken(CharmmMRParser::Comparison_ops, 0);
}

std::vector<CharmmMRParser::Number_fContext *> CharmmMRParser::FactorContext::number_f() {
  return getRuleContexts<CharmmMRParser::Number_fContext>();
}

CharmmMRParser::Number_fContext* CharmmMRParser::FactorContext::number_f(size_t i) {
  return getRuleContext<CharmmMRParser::Number_fContext>(i);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Abs() {
  return getToken(CharmmMRParser::Abs, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Bonded() {
  return getToken(CharmmMRParser::Bonded, 0);
}

CharmmMRParser::FactorContext* CharmmMRParser::FactorContext::factor() {
  return getRuleContext<CharmmMRParser::FactorContext>(0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::ByGroup() {
  return getToken(CharmmMRParser::ByGroup, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::ByRes() {
  return getToken(CharmmMRParser::ByRes, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Type() {
  return getToken(CharmmMRParser::Type, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Symbol_name() {
  return getToken(CharmmMRParser::Symbol_name, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Colon() {
  return getToken(CharmmMRParser::Colon, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Chemical() {
  return getToken(CharmmMRParser::Chemical, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Initial() {
  return getToken(CharmmMRParser::Initial, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Lone() {
  return getToken(CharmmMRParser::Lone, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Hydrogen() {
  return getToken(CharmmMRParser::Hydrogen, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::NONE() {
  return getToken(CharmmMRParser::NONE, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Not_op() {
  return getToken(CharmmMRParser::Not_op, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Point() {
  return getToken(CharmmMRParser::Point, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Cut() {
  return getToken(CharmmMRParser::Cut, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Period() {
  return getToken(CharmmMRParser::Period, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::User() {
  return getToken(CharmmMRParser::User, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Previous() {
  return getToken(CharmmMRParser::Previous, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Recall() {
  return getToken(CharmmMRParser::Recall, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::ByNumber() {
  return getToken(CharmmMRParser::ByNumber, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Residue() {
  return getToken(CharmmMRParser::Residue, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Resname() {
  return getToken(CharmmMRParser::Resname, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::SegIdentifier() {
  return getToken(CharmmMRParser::SegIdentifier, 0);
}

std::vector<tree::TerminalNode *> CharmmMRParser::FactorContext::Double_quote_string() {
  return getTokens(CharmmMRParser::Double_quote_string);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Double_quote_string(size_t i) {
  return getToken(CharmmMRParser::Double_quote_string, i);
}

tree::TerminalNode* CharmmMRParser::FactorContext::ISeg() {
  return getToken(CharmmMRParser::ISeg, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::IRes() {
  return getToken(CharmmMRParser::IRes, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::IGroup() {
  return getToken(CharmmMRParser::IGroup, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Around() {
  return getToken(CharmmMRParser::Around, 0);
}

tree::TerminalNode* CharmmMRParser::FactorContext::Subset() {
  return getToken(CharmmMRParser::Subset, 0);
}


size_t CharmmMRParser::FactorContext::getRuleIndex() const {
  return CharmmMRParser::RuleFactor;
}


std::any CharmmMRParser::FactorContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitFactor(this);
  else
    return visitor->visitChildren(this);
}


CharmmMRParser::FactorContext* CharmmMRParser::factor() {
   return factor(0);
}

CharmmMRParser::FactorContext* CharmmMRParser::factor(int precedence) {
  ParserRuleContext *parentContext = _ctx;
  size_t parentState = getState();
  CharmmMRParser::FactorContext *_localctx = _tracker.createInstance<FactorContext>(_ctx, parentState);
  CharmmMRParser::FactorContext *previousContext = _localctx;
  (void)previousContext; // Silence compiler, in case the context is not used by generated code.
  size_t startState = 90;
  enterRecursionRule(_localctx, 90, CharmmMRParser::RuleFactor, precedence);

    size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    unrollRecursionContexts(parentContext);
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(792);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CharmmMRParser::L_paren: {
        setState(689);
        match(CharmmMRParser::L_paren);
        setState(690);
        selection_expression();
        setState(691);
        match(CharmmMRParser::R_paren);
        break;
      }

      case CharmmMRParser::All: {
        setState(693);
        match(CharmmMRParser::All);
        break;
      }

      case CharmmMRParser::Atom: {
        setState(694);
        match(CharmmMRParser::Atom);
        setState(695);
        _la = _input->LA(1);
        if (!(_la == CharmmMRParser::Simple_name

        || _la == CharmmMRParser::Simple_names)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(696);
        _la = _input->LA(1);
        if (!(_la == CharmmMRParser::Integer

        || _la == CharmmMRParser::Integers)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(697);
        _la = _input->LA(1);
        if (!(_la == CharmmMRParser::Simple_name

        || _la == CharmmMRParser::Simple_names)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        break;
      }

      case CharmmMRParser::Property: {
        setState(698);
        match(CharmmMRParser::Property);
        setState(700);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == CharmmMRParser::Abs) {
          setState(699);
          match(CharmmMRParser::Abs);
        }
        setState(702);
        match(CharmmMRParser::Attr_properties);
        setState(703);
        match(CharmmMRParser::Comparison_ops);
        setState(704);
        number_f();
        break;
      }

      case CharmmMRParser::Bonded: {
        setState(705);
        match(CharmmMRParser::Bonded);
        setState(706);
        factor(18);
        break;
      }

      case CharmmMRParser::ByGroup: {
        setState(707);
        match(CharmmMRParser::ByGroup);
        setState(708);
        factor(17);
        break;
      }

      case CharmmMRParser::ByRes: {
        setState(709);
        match(CharmmMRParser::ByRes);
        setState(710);
        factor(16);
        break;
      }

      case CharmmMRParser::Type: {
        setState(711);
        match(CharmmMRParser::Type);
        setState(719);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CharmmMRParser::Simple_names: {
            setState(712);
            match(CharmmMRParser::Simple_names);
            break;
          }

          case CharmmMRParser::Simple_name: {
            setState(713);
            match(CharmmMRParser::Simple_name);
            setState(716);
            _errHandler->sync(this);

            switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 76, _ctx)) {
            case 1: {
              setState(714);
              match(CharmmMRParser::Colon);
              setState(715);
              match(CharmmMRParser::Simple_name);
              break;
            }

            default:
              break;
            }
            break;
          }

          case CharmmMRParser::Symbol_name: {
            setState(718);
            match(CharmmMRParser::Symbol_name);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case CharmmMRParser::Chemical: {
        setState(721);
        match(CharmmMRParser::Chemical);
        setState(729);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CharmmMRParser::Simple_names: {
            setState(722);
            match(CharmmMRParser::Simple_names);
            break;
          }

          case CharmmMRParser::Simple_name: {
            setState(723);
            match(CharmmMRParser::Simple_name);
            setState(726);
            _errHandler->sync(this);

            switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 78, _ctx)) {
            case 1: {
              setState(724);
              match(CharmmMRParser::Colon);
              setState(725);
              match(CharmmMRParser::Simple_name);
              break;
            }

            default:
              break;
            }
            break;
          }

          case CharmmMRParser::Symbol_name: {
            setState(728);
            match(CharmmMRParser::Symbol_name);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case CharmmMRParser::Initial: {
        setState(731);
        match(CharmmMRParser::Initial);
        break;
      }

      case CharmmMRParser::Lone: {
        setState(732);
        match(CharmmMRParser::Lone);
        break;
      }

      case CharmmMRParser::Hydrogen: {
        setState(733);
        match(CharmmMRParser::Hydrogen);
        break;
      }

      case CharmmMRParser::NONE: {
        setState(734);
        match(CharmmMRParser::NONE);
        break;
      }

      case CharmmMRParser::Not_op: {
        setState(735);
        match(CharmmMRParser::Not_op);
        setState(736);
        factor(9);
        break;
      }

      case CharmmMRParser::Point: {
        setState(737);
        match(CharmmMRParser::Point);
        setState(738);
        number_f();
        setState(739);
        number_f();
        setState(740);
        number_f();
        setState(743);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 80, _ctx)) {
        case 1: {
          setState(741);
          match(CharmmMRParser::Cut);
          setState(742);
          number_f();
          break;
        }

        default:
          break;
        }
        setState(746);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 81, _ctx)) {
        case 1: {
          setState(745);
          match(CharmmMRParser::Period);
          break;
        }

        default:
          break;
        }
        break;
      }

      case CharmmMRParser::User: {
        setState(748);
        match(CharmmMRParser::User);
        break;
      }

      case CharmmMRParser::Previous: {
        setState(749);
        match(CharmmMRParser::Previous);
        break;
      }

      case CharmmMRParser::Recall: {
        setState(750);
        match(CharmmMRParser::Recall);
        setState(751);
        match(CharmmMRParser::Integer);
        break;
      }

      case CharmmMRParser::ByNumber:
      case CharmmMRParser::Residue: {
        setState(752);
        _la = _input->LA(1);
        if (!(_la == CharmmMRParser::ByNumber || _la == CharmmMRParser::Residue)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(760);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CharmmMRParser::Integers: {
            setState(753);
            match(CharmmMRParser::Integers);
            break;
          }

          case CharmmMRParser::Integer: {
            setState(754);
            match(CharmmMRParser::Integer);
            setState(757);
            _errHandler->sync(this);

            switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 82, _ctx)) {
            case 1: {
              setState(755);
              match(CharmmMRParser::Colon);
              setState(756);
              match(CharmmMRParser::Integer);
              break;
            }

            default:
              break;
            }
            break;
          }

          case CharmmMRParser::Symbol_name: {
            setState(759);
            match(CharmmMRParser::Symbol_name);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case CharmmMRParser::Resname: {
        setState(762);
        match(CharmmMRParser::Resname);
        setState(770);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CharmmMRParser::Simple_names: {
            setState(763);
            match(CharmmMRParser::Simple_names);
            break;
          }

          case CharmmMRParser::Simple_name: {
            setState(764);
            match(CharmmMRParser::Simple_name);
            setState(767);
            _errHandler->sync(this);

            switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 84, _ctx)) {
            case 1: {
              setState(765);
              match(CharmmMRParser::Colon);
              setState(766);
              match(CharmmMRParser::Simple_name);
              break;
            }

            default:
              break;
            }
            break;
          }

          case CharmmMRParser::Symbol_name: {
            setState(769);
            match(CharmmMRParser::Symbol_name);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case CharmmMRParser::SegIdentifier: {
        setState(772);
        match(CharmmMRParser::SegIdentifier);
        setState(786);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case CharmmMRParser::Simple_names: {
            setState(773);
            match(CharmmMRParser::Simple_names);
            break;
          }

          case CharmmMRParser::Simple_name: {
            setState(774);
            match(CharmmMRParser::Simple_name);
            setState(777);
            _errHandler->sync(this);

            switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 86, _ctx)) {
            case 1: {
              setState(775);
              match(CharmmMRParser::Colon);
              setState(776);
              match(CharmmMRParser::Simple_name);
              break;
            }

            default:
              break;
            }
            break;
          }

          case CharmmMRParser::Double_quote_string: {
            setState(779);
            match(CharmmMRParser::Double_quote_string);
            setState(782);
            _errHandler->sync(this);

            switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 87, _ctx)) {
            case 1: {
              setState(780);
              match(CharmmMRParser::Colon);
              setState(781);
              match(CharmmMRParser::Double_quote_string);
              break;
            }

            default:
              break;
            }
            break;
          }

          case CharmmMRParser::Symbol_name: {
            setState(784);
            match(CharmmMRParser::Symbol_name);
            break;
          }

          case CharmmMRParser::Integer: {
            setState(785);
            match(CharmmMRParser::Integer);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case CharmmMRParser::ISeg:
      case CharmmMRParser::IRes:
      case CharmmMRParser::IGroup: {
        setState(788);
        _la = _input->LA(1);
        if (!(((((_la - 126) & ~ 0x3fULL) == 0) &&
          ((1ULL << (_la - 126)) & 21) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(789);
        match(CharmmMRParser::Integer);
        setState(790);
        match(CharmmMRParser::Colon);
        setState(791);
        match(CharmmMRParser::Integer);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    _ctx->stop = _input->LT(-1);
    setState(810);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 93, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        if (!_parseListeners.empty())
          triggerExitRuleEvent();
        previousContext = _localctx;
        setState(808);
        _errHandler->sync(this);
        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 92, _ctx)) {
        case 1: {
          _localctx = _tracker.createInstance<FactorContext>(parentContext, parentState);
          pushNewRecursionContext(_localctx, startState, RuleFactor);
          setState(794);

          if (!(precpred(_ctx, 22))) throw FailedPredicateException(this, "precpred(_ctx, 22)");
          setState(795);
          match(CharmmMRParser::Around);
          setState(796);
          number_f();
          break;
        }

        case 2: {
          _localctx = _tracker.createInstance<FactorContext>(parentContext, parentState);
          pushNewRecursionContext(_localctx, startState, RuleFactor);
          setState(797);

          if (!(precpred(_ctx, 21))) throw FailedPredicateException(this, "precpred(_ctx, 21)");
          setState(798);
          match(CharmmMRParser::Subset);
          setState(806);
          _errHandler->sync(this);
          switch (_input->LA(1)) {
            case CharmmMRParser::Integers: {
              setState(799);
              match(CharmmMRParser::Integers);
              break;
            }

            case CharmmMRParser::Integer: {
              setState(800);
              match(CharmmMRParser::Integer);
              setState(803);
              _errHandler->sync(this);

              switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 90, _ctx)) {
              case 1: {
                setState(801);
                match(CharmmMRParser::Colon);
                setState(802);
                match(CharmmMRParser::Integer);
                break;
              }

              default:
                break;
              }
              break;
            }

            case CharmmMRParser::Symbol_name: {
              setState(805);
              match(CharmmMRParser::Symbol_name);
              break;
            }

          default:
            throw NoViableAltException(this);
          }
          break;
        }

        default:
          break;
        } 
      }
      setState(812);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 93, _ctx);
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

CharmmMRParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::NumberContext::Real() {
  return getToken(CharmmMRParser::Real, 0);
}

tree::TerminalNode* CharmmMRParser::NumberContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::NumberContext::Symbol_name() {
  return getToken(CharmmMRParser::Symbol_name, 0);
}


size_t CharmmMRParser::NumberContext::getRuleIndex() const {
  return CharmmMRParser::RuleNumber;
}


std::any CharmmMRParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::NumberContext* CharmmMRParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 92, CharmmMRParser::RuleNumber);
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
    setState(813);
    _la = _input->LA(1);
    if (!(((((_la - 144) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 144)) & 262147) != 0))) {
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

//----------------- Number_fContext ------------------------------------------------------------------

CharmmMRParser::Number_fContext::Number_fContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Number_fContext::Real() {
  return getToken(CharmmMRParser::Real, 0);
}

tree::TerminalNode* CharmmMRParser::Number_fContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}


size_t CharmmMRParser::Number_fContext::getRuleIndex() const {
  return CharmmMRParser::RuleNumber_f;
}


std::any CharmmMRParser::Number_fContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber_f(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Number_fContext* CharmmMRParser::number_f() {
  Number_fContext *_localctx = _tracker.createInstance<Number_fContext>(_ctx, getState());
  enterRule(_localctx, 94, CharmmMRParser::RuleNumber_f);
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
    setState(815);
    _la = _input->LA(1);
    if (!(_la == CharmmMRParser::Integer

    || _la == CharmmMRParser::Real)) {
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

//----------------- Number_sContext ------------------------------------------------------------------

CharmmMRParser::Number_sContext::Number_sContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Number_sContext::Real() {
  return getToken(CharmmMRParser::Real, 0);
}

tree::TerminalNode* CharmmMRParser::Number_sContext::Integer() {
  return getToken(CharmmMRParser::Integer, 0);
}

tree::TerminalNode* CharmmMRParser::Number_sContext::Symbol_name() {
  return getToken(CharmmMRParser::Symbol_name, 0);
}


size_t CharmmMRParser::Number_sContext::getRuleIndex() const {
  return CharmmMRParser::RuleNumber_s;
}


std::any CharmmMRParser::Number_sContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber_s(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Number_sContext* CharmmMRParser::number_s() {
  Number_sContext *_localctx = _tracker.createInstance<Number_sContext>(_ctx, getState());
  enterRule(_localctx, 96, CharmmMRParser::RuleNumber_s);
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
    setState(817);
    _la = _input->LA(1);
    if (!(((((_la - 144) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 144)) & 262147) != 0))) {
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

//----------------- Set_statementContext ------------------------------------------------------------------

CharmmMRParser::Set_statementContext::Set_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CharmmMRParser::Set_statementContext::Set() {
  return getToken(CharmmMRParser::Set, 0);
}

std::vector<tree::TerminalNode *> CharmmMRParser::Set_statementContext::Simple_name_VE() {
  return getTokens(CharmmMRParser::Simple_name_VE);
}

tree::TerminalNode* CharmmMRParser::Set_statementContext::Simple_name_VE(size_t i) {
  return getToken(CharmmMRParser::Simple_name_VE, i);
}

tree::TerminalNode* CharmmMRParser::Set_statementContext::RETURN_VE() {
  return getToken(CharmmMRParser::RETURN_VE, 0);
}

tree::TerminalNode* CharmmMRParser::Set_statementContext::Real_VE() {
  return getToken(CharmmMRParser::Real_VE, 0);
}

tree::TerminalNode* CharmmMRParser::Set_statementContext::Integer_VE() {
  return getToken(CharmmMRParser::Integer_VE, 0);
}

tree::TerminalNode* CharmmMRParser::Set_statementContext::Equ_op_VE() {
  return getToken(CharmmMRParser::Equ_op_VE, 0);
}


size_t CharmmMRParser::Set_statementContext::getRuleIndex() const {
  return CharmmMRParser::RuleSet_statement;
}


std::any CharmmMRParser::Set_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CharmmMRParserVisitor*>(visitor))
    return parserVisitor->visitSet_statement(this);
  else
    return visitor->visitChildren(this);
}

CharmmMRParser::Set_statementContext* CharmmMRParser::set_statement() {
  Set_statementContext *_localctx = _tracker.createInstance<Set_statementContext>(_ctx, getState());
  enterRule(_localctx, 98, CharmmMRParser::RuleSet_statement);
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
    setState(819);
    match(CharmmMRParser::Set);
    setState(820);
    match(CharmmMRParser::Simple_name_VE);
    setState(822);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CharmmMRParser::Equ_op_VE) {
      setState(821);
      match(CharmmMRParser::Equ_op_VE);
    }
    setState(824);
    _la = _input->LA(1);
    if (!(((((_la - 169) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 169)) & 7) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(825);
    match(CharmmMRParser::RETURN_VE);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

bool CharmmMRParser::sempred(RuleContext *context, size_t ruleIndex, size_t predicateIndex) {
  switch (ruleIndex) {
    case 45: return factorSempred(antlrcpp::downCast<FactorContext *>(context), predicateIndex);

  default:
    break;
  }
  return true;
}

bool CharmmMRParser::factorSempred(FactorContext *_localctx, size_t predicateIndex) {
  switch (predicateIndex) {
    case 0: return precpred(_ctx, 22);
    case 1: return precpred(_ctx, 21);

  default:
    break;
  }
  return true;
}

void CharmmMRParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  charmmmrparserParserInitialize();
#else
  ::antlr4::internal::call_once(charmmmrparserParserOnceFlag, charmmmrparserParserInitialize);
#endif
}
