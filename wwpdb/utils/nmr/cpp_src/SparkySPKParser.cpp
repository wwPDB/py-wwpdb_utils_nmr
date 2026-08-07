
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkySPKParser.g4 by ANTLR 4.13.0


#include "SparkySPKParserVisitor.h"

#include "SparkySPKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct SparkySPKParserStaticData final {
  SparkySPKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  SparkySPKParserStaticData(const SparkySPKParserStaticData&) = delete;
  SparkySPKParserStaticData(SparkySPKParserStaticData&&) = delete;
  SparkySPKParserStaticData& operator=(const SparkySPKParserStaticData&) = delete;
  SparkySPKParserStaticData& operator=(SparkySPKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag sparkyspkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
SparkySPKParserStaticData *sparkyspkparserParserStaticData = nullptr;

void sparkyspkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (sparkyspkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(sparkyspkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<SparkySPKParserStaticData>(
    std::vector<std::string>{
      "sparky_spk", "user_block", "user_statement", "spectrum_block", "spectrum_statement", 
      "spectrum_name", "attached_data", "attached_data_statement", "view", 
      "view_statement", "view_name", "view_number", "params", "params_statement", 
      "ornament", "ornament_statement", "ornament_position", "label", "label_statement", 
      "label_position"
    },
    std::vector<std::string>{
      "", "'<sparky save file>'", "", "'<user>'", "'<spectrum>'", "", "", 
      "", "", "", "'<end user>'", "'set'", "", "'saveprompt'", "'saveinterval'", 
      "'resizeViews'", "'keytimeout'", "'cachesize'", "'contourgraying'", 
      "'default'", "'print'", "'command'", "'file'", "'options'", "", "", 
      "", "", "", "'<attached data>'", "'<view>'", "'<ornament>'", "'<end spectrum>'", 
      "", "'pathname'", "'dimension'", "'shift'", "'points'", "'extraPeakPlanes'", 
      "'assignMultiAxisGuess'", "'assignGuessThreshold'", "'assignRelation'", 
      "'assignRange'", "'assignFormat'", "'listTool'", "'sortBy'", "'nameType'", 
      "'sortAxis'", "'showFlags'", "'integrate.overlapped_sep'", "'integrate.methods'", 
      "'integrate.allow_motion'", "'integrate.adjust_linewidths'", "'integrate.motion_range'", 
      "'integrate.min_linewidth'", "'integrate.max_linewidth'", "'integrate.fit_baseline'", 
      "'integrate.subtract_peaks'", "'integrate.contoured_data'", "'integrate.rectangle_data'", 
      "'integrate.maxiterations'", "'integrate.tolerance'", "'peak.pick'", 
      "'peak.pick-minimum-linewidth'", "'peak.pick-minimum-dropoff'", "'noise.sigma'", 
      "'ornament.label.size'", "'ornament.line.size'", "'ornament.peak.size'", 
      "'ornament.grid.size'", "'ornament.peakgroup.size'", "'ornament.selectsize'", 
      "'ornament.pointersize'", "'ornament.lineendsize'", "", "", "", "", 
      "", "", "", "'<end attached data>'", "", "", "'<params>'", "'<end view>'", 
      "", "'precision'", "'precision_by_units'", "'viewmode'", "'show'", 
      "'axistype'", "", "'contour.pos'", "'contour.neg'", "", "", "", "", 
      "", "", "'<end params>'", "'orientation'", "'location'", "'size'", 
      "'offset'", "'scale'", "'zoom'", "", "", "", "", "", "", "'['", "'<end ornament>'", 
      "", "'peak'", "'grid'", "", "", "'id'", "", "'height'", "'linewidth'", 
      "'integral'", "'fr'", "'rs'", "", "", "", "", "", "", "", "']'", "", 
      "'label'", "", "", "", "", "'xy'"
    },
    std::vector<std::string>{
      "", "Sparky_save_file", "Version", "User", "Spectrum", "Integer", 
      "Float", "Real", "Simple_name", "SPACE", "End_user", "Set", "Mode_US", 
      "Save_prompt", "Save_interval", "Resize_views", "Key_timeout", "Cache_size", 
      "Contour_graying", "Default", "Print", "Command", "File", "Options", 
      "Integer_US", "Float_US", "Simple_name_US", "SPACE_US", "RETURN_US", 
      "Attached_data", "View", "Ornament", "End_spectrum", "Name_SP", "Path_name", 
      "Dimension", "Shift", "Points", "Extra_peak_planes", "Assign_multi_axis_guess", 
      "Assign_guess_threshhold", "Assign_relation", "Assign_range", "Assign_format", 
      "List_tool", "Sort_by", "Name_type", "Sort_axis", "Show_flags", "Integrate_overlapped_sep", 
      "Integrate_methods", "Integrate_allow_motion", "Integrate_adjust_linewidths", 
      "Integrate_motion_range", "Integrate_min_linewidth", "Integrate_max_linewidth", 
      "Integrate_fit_baseline", "Integrate_subtract_peaks", "Integrate_contoured_data", 
      "Integrate_rectangle_data", "Integrate_max_iterations", "Integrate_tolerance", 
      "Peak_pick", "Peak_pick_minimum_linewidth", "Peak_pick_minimum_dropoff", 
      "Noise_sigma", "Ornament_labe_size", "Ornament_line_size", "Ornament_peak_size", 
      "Ornament_grid_size", "Ornament_peak_group_size", "Ornament_select_size", 
      "Ornament_pointer_size", "Ornament_line_end_size", "Format_ex", "Integer_SP", 
      "Float_SP", "Simple_name_SP", "Any_name_SP", "SPACE_SP", "RETURN_SP", 
      "End_attached_data", "Any_name_AD", "SPACE_AD", "Params", "End_view", 
      "Name_VI", "Precision", "Precision_by_units", "View_mode", "Show", 
      "Axis_type", "Flags_VI", "Contour_pos", "Contour_neg", "Integer_VI", 
      "Float_VI", "Real_VI", "Simple_name_VI", "SPACE_VI", "RETURN_VI", 
      "End_params", "Orientation", "Location", "Size", "Offset", "Scale", 
      "Zoom", "Flags_PA", "Integer_PA", "Float_PA", "Simple_name_PA", "SPACE_PA", 
      "RETURN_PA", "L_brakt", "End_ornament", "Type_OR", "Peak", "Grid", 
      "Color_OR", "Flags_OR", "Id", "Pos_OR", "Height", "Line_width", "Integral", 
      "Fr", "Rs", "Rs_ex", "Integer_OR", "Float_OR", "Real_OR", "Simple_name_OR", 
      "SPACE_OR", "RETURN_OR", "R_brakt", "Type_LA", "Label", "Color_LA", 
      "Flags_LA", "Mode_LA", "Pos_LA", "Xy", "Assignment_2d_ex", "Assignment_3d_ex", 
      "Assignment_4d_ex", "Xy_pos", "Integer_LA", "Float_LA", "Simple_name_LA", 
      "SPACE_LA", "RETURN_LA"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,151,611,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,1,0,1,0,1,0,
  	1,0,4,0,46,8,0,11,0,12,0,47,1,0,1,0,1,1,1,1,5,1,54,8,1,10,1,12,1,57,9,
  	1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
  	1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
  	2,1,2,1,2,1,2,1,2,1,2,3,2,99,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
  	3,2,110,8,2,1,3,1,3,5,3,114,8,3,10,3,12,3,117,9,3,1,3,1,3,1,4,1,4,1,4,
  	5,4,124,8,4,10,4,12,4,127,9,4,1,4,1,4,1,4,5,4,132,8,4,10,4,12,4,135,9,
  	4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,143,8,4,11,4,12,4,144,1,4,1,4,1,4,4,4,150,
  	8,4,11,4,12,4,151,1,4,1,4,1,4,4,4,157,8,4,11,4,12,4,158,1,4,1,4,1,4,1,
  	4,1,4,1,4,1,4,1,4,1,4,4,4,170,8,4,11,4,12,4,171,1,4,1,4,1,4,1,4,1,4,1,
  	4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
  	5,4,197,8,4,10,4,12,4,200,9,4,1,4,1,4,1,4,4,4,205,8,4,11,4,12,4,206,1,
  	4,1,4,1,4,4,4,212,8,4,11,4,12,4,213,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
  	4,4,4,225,8,4,11,4,12,4,226,1,4,1,4,1,4,4,4,232,8,4,11,4,12,4,233,1,4,
  	1,4,1,4,4,4,239,8,4,11,4,12,4,240,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
  	1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,264,8,4,11,4,12,4,
  	265,1,4,1,4,1,4,1,4,4,4,272,8,4,11,4,12,4,273,1,4,1,4,1,4,1,4,1,4,1,4,
  	1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
  	4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
  	316,8,4,1,5,1,5,1,6,1,6,5,6,322,8,6,10,6,12,6,325,9,6,1,6,1,6,1,7,1,7,
  	1,8,1,8,5,8,333,8,8,10,8,12,8,336,9,8,1,8,1,8,1,9,1,9,1,9,5,9,343,8,9,
  	10,9,12,9,346,9,9,1,9,1,9,1,9,1,9,1,9,1,9,4,9,354,8,9,11,9,12,9,355,1,
  	9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,365,8,9,10,9,12,9,368,9,9,1,9,1,9,1,9,1,
  	9,1,9,1,9,5,9,376,8,9,10,9,12,9,379,9,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,4,
  	9,388,8,9,11,9,12,9,389,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,4,9,400,8,9,11,
  	9,12,9,401,1,9,1,9,1,9,1,9,1,9,3,9,409,8,9,1,10,1,10,1,11,1,11,1,12,1,
  	12,5,12,417,8,12,10,12,12,12,420,9,12,1,12,1,12,1,13,1,13,1,13,4,13,427,
  	8,13,11,13,12,13,428,1,13,1,13,1,13,4,13,434,8,13,11,13,12,13,435,1,13,
  	1,13,1,13,4,13,441,8,13,11,13,12,13,442,1,13,1,13,1,13,4,13,448,8,13,
  	11,13,12,13,449,1,13,1,13,1,13,4,13,455,8,13,11,13,12,13,456,1,13,1,13,
  	1,13,1,13,1,13,1,13,1,13,3,13,466,8,13,1,14,1,14,5,14,470,8,14,10,14,
  	12,14,473,9,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
  	4,15,486,8,15,11,15,12,15,487,1,15,4,15,491,8,15,11,15,12,15,492,1,15,
  	1,15,1,15,4,15,498,8,15,11,15,12,15,499,1,15,1,15,1,15,1,15,1,15,1,15,
  	4,15,508,8,15,11,15,12,15,509,1,15,1,15,1,15,1,15,4,15,516,8,15,11,15,
  	12,15,517,1,15,1,15,1,15,4,15,523,8,15,11,15,12,15,524,1,15,3,15,528,
  	8,15,1,15,1,15,1,15,1,15,3,15,534,8,15,1,15,1,15,1,15,1,15,1,15,1,15,
  	4,15,542,8,15,11,15,12,15,543,1,15,1,15,1,15,1,15,3,15,550,8,15,1,16,
  	1,16,1,17,1,17,5,17,556,8,17,10,17,12,17,559,9,17,1,17,1,17,1,18,1,18,
  	1,18,1,18,1,18,1,18,4,18,569,8,18,11,18,12,18,570,1,18,4,18,574,8,18,
  	11,18,12,18,575,1,18,1,18,1,18,4,18,581,8,18,11,18,12,18,582,1,18,1,18,
  	1,18,1,18,1,18,1,18,4,18,591,8,18,11,18,12,18,592,1,18,1,18,1,18,1,18,
  	1,18,1,18,1,18,4,18,602,8,18,11,18,12,18,603,1,18,3,18,607,8,18,1,19,
  	1,19,1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
  	38,0,7,2,0,20,20,26,26,1,0,75,78,1,0,95,98,1,0,95,97,1,0,129,130,1,0,
  	143,145,1,0,147,148,727,0,45,1,0,0,0,2,51,1,0,0,0,4,109,1,0,0,0,6,111,
  	1,0,0,0,8,315,1,0,0,0,10,317,1,0,0,0,12,319,1,0,0,0,14,328,1,0,0,0,16,
  	330,1,0,0,0,18,408,1,0,0,0,20,410,1,0,0,0,22,412,1,0,0,0,24,414,1,0,0,
  	0,26,465,1,0,0,0,28,467,1,0,0,0,30,549,1,0,0,0,32,551,1,0,0,0,34,553,
  	1,0,0,0,36,606,1,0,0,0,38,608,1,0,0,0,40,41,5,1,0,0,41,42,5,2,0,0,42,
  	43,3,2,1,0,43,44,3,6,3,0,44,46,1,0,0,0,45,40,1,0,0,0,46,47,1,0,0,0,47,
  	45,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,0,0,1,50,1,1,0,0,0,51,
  	55,5,3,0,0,52,54,3,4,2,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,
  	56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,5,10,0,0,59,3,1,0,0,0,60,
  	110,5,28,0,0,61,62,5,11,0,0,62,63,5,12,0,0,63,64,5,24,0,0,64,110,5,28,
  	0,0,65,66,5,11,0,0,66,67,5,13,0,0,67,68,5,24,0,0,68,110,5,28,0,0,69,70,
  	5,11,0,0,70,71,5,14,0,0,71,72,5,24,0,0,72,110,5,28,0,0,73,74,5,11,0,0,
  	74,75,5,15,0,0,75,76,5,24,0,0,76,110,5,28,0,0,77,78,5,11,0,0,78,79,5,
  	16,0,0,79,80,5,24,0,0,80,110,5,28,0,0,81,82,5,11,0,0,82,83,5,17,0,0,83,
  	84,5,24,0,0,84,110,5,28,0,0,85,86,5,11,0,0,86,87,5,18,0,0,87,88,5,24,
  	0,0,88,110,5,28,0,0,89,90,5,19,0,0,90,91,5,20,0,0,91,92,5,21,0,0,92,93,
  	7,0,0,0,93,110,5,28,0,0,94,95,5,19,0,0,95,96,5,20,0,0,96,98,5,22,0,0,
  	97,99,5,26,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,110,5,28,
  	0,0,101,102,5,19,0,0,102,103,5,20,0,0,103,104,5,23,0,0,104,105,5,24,0,
  	0,105,106,5,24,0,0,106,107,5,25,0,0,107,108,5,25,0,0,108,110,5,28,0,0,
  	109,60,1,0,0,0,109,61,1,0,0,0,109,65,1,0,0,0,109,69,1,0,0,0,109,73,1,
  	0,0,0,109,77,1,0,0,0,109,81,1,0,0,0,109,85,1,0,0,0,109,89,1,0,0,0,109,
  	94,1,0,0,0,109,101,1,0,0,0,110,5,1,0,0,0,111,115,5,4,0,0,112,114,3,8,
  	4,0,113,112,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,
  	118,1,0,0,0,117,115,1,0,0,0,118,119,5,32,0,0,119,7,1,0,0,0,120,316,5,
  	80,0,0,121,125,5,33,0,0,122,124,3,10,5,0,123,122,1,0,0,0,124,127,1,0,
  	0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,125,1,0,0,0,128,
  	316,5,80,0,0,129,133,5,34,0,0,130,132,3,10,5,0,131,130,1,0,0,0,132,135,
  	1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,133,1,0,0,
  	0,136,316,5,80,0,0,137,138,5,35,0,0,138,139,5,75,0,0,139,316,5,80,0,0,
  	140,142,5,36,0,0,141,143,5,76,0,0,142,141,1,0,0,0,143,144,1,0,0,0,144,
  	142,1,0,0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,316,5,80,0,0,147,149,
  	5,37,0,0,148,150,5,75,0,0,149,148,1,0,0,0,150,151,1,0,0,0,151,149,1,0,
  	0,0,151,152,1,0,0,0,152,153,1,0,0,0,153,316,5,80,0,0,154,156,5,38,0,0,
  	155,157,5,75,0,0,156,155,1,0,0,0,157,158,1,0,0,0,158,156,1,0,0,0,158,
  	159,1,0,0,0,159,160,1,0,0,0,160,316,5,80,0,0,161,162,5,39,0,0,162,163,
  	5,75,0,0,163,316,5,80,0,0,164,165,5,40,0,0,165,166,5,76,0,0,166,316,5,
  	80,0,0,167,169,5,41,0,0,168,170,5,75,0,0,169,168,1,0,0,0,170,171,1,0,
  	0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,316,5,80,0,0,
  	174,175,5,42,0,0,175,176,5,75,0,0,176,177,5,76,0,0,177,316,5,80,0,0,178,
  	179,5,43,0,0,179,180,5,74,0,0,180,316,5,80,0,0,181,182,5,44,0,0,182,183,
  	5,45,0,0,183,184,5,77,0,0,184,316,5,80,0,0,185,186,5,44,0,0,186,187,5,
  	46,0,0,187,188,5,77,0,0,188,316,5,80,0,0,189,190,5,44,0,0,190,191,5,47,
  	0,0,191,192,5,77,0,0,192,316,5,80,0,0,193,194,5,44,0,0,194,198,5,48,0,
  	0,195,197,5,77,0,0,196,195,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,
  	199,1,0,0,0,199,201,1,0,0,0,200,198,1,0,0,0,201,316,5,80,0,0,202,204,
  	5,49,0,0,203,205,5,76,0,0,204,203,1,0,0,0,205,206,1,0,0,0,206,204,1,0,
  	0,0,206,207,1,0,0,0,207,208,1,0,0,0,208,316,5,80,0,0,209,211,5,50,0,0,
  	210,212,5,75,0,0,211,210,1,0,0,0,212,213,1,0,0,0,213,211,1,0,0,0,213,
  	214,1,0,0,0,214,215,1,0,0,0,215,316,5,80,0,0,216,217,5,51,0,0,217,218,
  	5,75,0,0,218,316,5,80,0,0,219,220,5,52,0,0,220,221,5,75,0,0,221,316,5,
  	80,0,0,222,224,5,53,0,0,223,225,5,76,0,0,224,223,1,0,0,0,225,226,1,0,
  	0,0,226,224,1,0,0,0,226,227,1,0,0,0,227,228,1,0,0,0,228,316,5,80,0,0,
  	229,231,5,54,0,0,230,232,5,76,0,0,231,230,1,0,0,0,232,233,1,0,0,0,233,
  	231,1,0,0,0,233,234,1,0,0,0,234,235,1,0,0,0,235,316,5,80,0,0,236,238,
  	5,55,0,0,237,239,5,76,0,0,238,237,1,0,0,0,239,240,1,0,0,0,240,238,1,0,
  	0,0,240,241,1,0,0,0,241,242,1,0,0,0,242,316,5,80,0,0,243,244,5,56,0,0,
  	244,245,5,75,0,0,245,316,5,80,0,0,246,247,5,57,0,0,247,248,5,75,0,0,248,
  	316,5,80,0,0,249,250,5,58,0,0,250,251,5,75,0,0,251,316,5,80,0,0,252,253,
  	5,59,0,0,253,254,5,75,0,0,254,316,5,80,0,0,255,256,5,60,0,0,256,257,5,
  	75,0,0,257,316,5,80,0,0,258,259,5,61,0,0,259,260,5,76,0,0,260,316,5,80,
  	0,0,261,263,5,62,0,0,262,264,5,76,0,0,263,262,1,0,0,0,264,265,1,0,0,0,
  	265,263,1,0,0,0,265,266,1,0,0,0,266,267,1,0,0,0,267,268,5,75,0,0,268,
  	316,5,80,0,0,269,271,5,63,0,0,270,272,5,76,0,0,271,270,1,0,0,0,272,273,
  	1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,275,1,0,0,0,275,316,5,80,
  	0,0,276,277,5,64,0,0,277,278,5,76,0,0,278,316,5,80,0,0,279,280,5,65,0,
  	0,280,281,5,76,0,0,281,316,5,80,0,0,282,283,5,66,0,0,283,284,5,76,0,0,
  	284,316,5,80,0,0,285,286,5,67,0,0,286,287,5,76,0,0,287,316,5,80,0,0,288,
  	289,5,68,0,0,289,290,5,76,0,0,290,316,5,80,0,0,291,292,5,69,0,0,292,293,
  	5,76,0,0,293,316,5,80,0,0,294,295,5,70,0,0,295,296,5,76,0,0,296,316,5,
  	80,0,0,297,298,5,71,0,0,298,299,5,76,0,0,299,316,5,80,0,0,300,301,5,72,
  	0,0,301,302,5,76,0,0,302,316,5,80,0,0,303,304,5,73,0,0,304,305,5,76,0,
  	0,305,316,5,80,0,0,306,307,3,12,6,0,307,308,5,80,0,0,308,316,1,0,0,0,
  	309,310,3,16,8,0,310,311,5,80,0,0,311,316,1,0,0,0,312,313,3,28,14,0,313,
  	314,5,80,0,0,314,316,1,0,0,0,315,120,1,0,0,0,315,121,1,0,0,0,315,129,
  	1,0,0,0,315,137,1,0,0,0,315,140,1,0,0,0,315,147,1,0,0,0,315,154,1,0,0,
  	0,315,161,1,0,0,0,315,164,1,0,0,0,315,167,1,0,0,0,315,174,1,0,0,0,315,
  	178,1,0,0,0,315,181,1,0,0,0,315,185,1,0,0,0,315,189,1,0,0,0,315,193,1,
  	0,0,0,315,202,1,0,0,0,315,209,1,0,0,0,315,216,1,0,0,0,315,219,1,0,0,0,
  	315,222,1,0,0,0,315,229,1,0,0,0,315,236,1,0,0,0,315,243,1,0,0,0,315,246,
  	1,0,0,0,315,249,1,0,0,0,315,252,1,0,0,0,315,255,1,0,0,0,315,258,1,0,0,
  	0,315,261,1,0,0,0,315,269,1,0,0,0,315,276,1,0,0,0,315,279,1,0,0,0,315,
  	282,1,0,0,0,315,285,1,0,0,0,315,288,1,0,0,0,315,291,1,0,0,0,315,294,1,
  	0,0,0,315,297,1,0,0,0,315,300,1,0,0,0,315,303,1,0,0,0,315,306,1,0,0,0,
  	315,309,1,0,0,0,315,312,1,0,0,0,316,9,1,0,0,0,317,318,7,1,0,0,318,11,
  	1,0,0,0,319,323,5,29,0,0,320,322,3,14,7,0,321,320,1,0,0,0,322,325,1,0,
  	0,0,323,321,1,0,0,0,323,324,1,0,0,0,324,326,1,0,0,0,325,323,1,0,0,0,326,
  	327,5,81,0,0,327,13,1,0,0,0,328,329,5,82,0,0,329,15,1,0,0,0,330,334,5,
  	30,0,0,331,333,3,18,9,0,332,331,1,0,0,0,333,336,1,0,0,0,334,332,1,0,0,
  	0,334,335,1,0,0,0,335,337,1,0,0,0,336,334,1,0,0,0,337,338,5,85,0,0,338,
  	17,1,0,0,0,339,409,5,100,0,0,340,344,5,86,0,0,341,343,3,20,10,0,342,341,
  	1,0,0,0,343,346,1,0,0,0,344,342,1,0,0,0,344,345,1,0,0,0,345,347,1,0,0,
  	0,346,344,1,0,0,0,347,409,5,100,0,0,348,349,5,87,0,0,349,350,5,95,0,0,
  	350,409,5,100,0,0,351,353,5,88,0,0,352,354,5,95,0,0,353,352,1,0,0,0,354,
  	355,1,0,0,0,355,353,1,0,0,0,355,356,1,0,0,0,356,357,1,0,0,0,357,409,5,
  	100,0,0,358,359,5,89,0,0,359,360,5,95,0,0,360,409,5,100,0,0,361,362,5,
  	90,0,0,362,366,5,95,0,0,363,365,5,98,0,0,364,363,1,0,0,0,365,368,1,0,
  	0,0,366,364,1,0,0,0,366,367,1,0,0,0,367,369,1,0,0,0,368,366,1,0,0,0,369,
  	409,5,100,0,0,370,371,5,91,0,0,371,372,5,95,0,0,372,409,5,100,0,0,373,
  	377,5,92,0,0,374,376,5,98,0,0,375,374,1,0,0,0,376,379,1,0,0,0,377,375,
  	1,0,0,0,377,378,1,0,0,0,378,380,1,0,0,0,379,377,1,0,0,0,380,409,5,100,
  	0,0,381,382,5,93,0,0,382,383,5,95,0,0,383,384,3,22,11,0,384,385,5,96,
  	0,0,385,387,5,96,0,0,386,388,5,98,0,0,387,386,1,0,0,0,388,389,1,0,0,0,
  	389,387,1,0,0,0,389,390,1,0,0,0,390,391,1,0,0,0,391,392,5,100,0,0,392,
  	409,1,0,0,0,393,394,5,94,0,0,394,395,5,95,0,0,395,396,3,22,11,0,396,397,
  	5,96,0,0,397,399,5,96,0,0,398,400,5,98,0,0,399,398,1,0,0,0,400,401,1,
  	0,0,0,401,399,1,0,0,0,401,402,1,0,0,0,402,403,1,0,0,0,403,404,5,100,0,
  	0,404,409,1,0,0,0,405,406,3,24,12,0,406,407,5,100,0,0,407,409,1,0,0,0,
  	408,339,1,0,0,0,408,340,1,0,0,0,408,348,1,0,0,0,408,351,1,0,0,0,408,358,
  	1,0,0,0,408,361,1,0,0,0,408,370,1,0,0,0,408,373,1,0,0,0,408,381,1,0,0,
  	0,408,393,1,0,0,0,408,405,1,0,0,0,409,19,1,0,0,0,410,411,7,2,0,0,411,
  	21,1,0,0,0,412,413,7,3,0,0,413,23,1,0,0,0,414,418,5,84,0,0,415,417,3,
  	26,13,0,416,415,1,0,0,0,417,420,1,0,0,0,418,416,1,0,0,0,418,419,1,0,0,
  	0,419,421,1,0,0,0,420,418,1,0,0,0,421,422,5,101,0,0,422,25,1,0,0,0,423,
  	466,5,113,0,0,424,426,5,102,0,0,425,427,5,109,0,0,426,425,1,0,0,0,427,
  	428,1,0,0,0,428,426,1,0,0,0,428,429,1,0,0,0,429,430,1,0,0,0,430,466,5,
  	113,0,0,431,433,5,103,0,0,432,434,5,109,0,0,433,432,1,0,0,0,434,435,1,
  	0,0,0,435,433,1,0,0,0,435,436,1,0,0,0,436,437,1,0,0,0,437,466,5,113,0,
  	0,438,440,5,104,0,0,439,441,5,109,0,0,440,439,1,0,0,0,441,442,1,0,0,0,
  	442,440,1,0,0,0,442,443,1,0,0,0,443,444,1,0,0,0,444,466,5,113,0,0,445,
  	447,5,105,0,0,446,448,5,110,0,0,447,446,1,0,0,0,448,449,1,0,0,0,449,447,
  	1,0,0,0,449,450,1,0,0,0,450,451,1,0,0,0,451,466,5,113,0,0,452,454,5,106,
  	0,0,453,455,5,110,0,0,454,453,1,0,0,0,455,456,1,0,0,0,456,454,1,0,0,0,
  	456,457,1,0,0,0,457,458,1,0,0,0,458,466,5,113,0,0,459,460,5,107,0,0,460,
  	461,5,110,0,0,461,466,5,113,0,0,462,463,5,108,0,0,463,464,5,109,0,0,464,
  	466,5,113,0,0,465,423,1,0,0,0,465,424,1,0,0,0,465,431,1,0,0,0,465,438,
  	1,0,0,0,465,445,1,0,0,0,465,452,1,0,0,0,465,459,1,0,0,0,465,462,1,0,0,
  	0,466,27,1,0,0,0,467,471,5,31,0,0,468,470,3,30,15,0,469,468,1,0,0,0,470,
  	473,1,0,0,0,471,469,1,0,0,0,471,472,1,0,0,0,472,474,1,0,0,0,473,471,1,
  	0,0,0,474,475,5,115,0,0,475,29,1,0,0,0,476,550,5,134,0,0,477,478,5,116,
  	0,0,478,479,5,117,0,0,479,550,5,134,0,0,480,481,5,116,0,0,481,482,5,118,
  	0,0,482,550,5,134,0,0,483,485,5,119,0,0,484,486,5,129,0,0,485,484,1,0,
  	0,0,486,487,1,0,0,0,487,485,1,0,0,0,487,488,1,0,0,0,488,490,1,0,0,0,489,
  	491,5,132,0,0,490,489,1,0,0,0,491,492,1,0,0,0,492,490,1,0,0,0,492,493,
  	1,0,0,0,493,494,1,0,0,0,494,550,5,134,0,0,495,497,5,120,0,0,496,498,5,
  	129,0,0,497,496,1,0,0,0,498,499,1,0,0,0,499,497,1,0,0,0,499,500,1,0,0,
  	0,500,501,1,0,0,0,501,550,5,134,0,0,502,503,5,121,0,0,503,504,5,129,0,
  	0,504,550,5,134,0,0,505,507,5,122,0,0,506,508,3,32,16,0,507,506,1,0,0,
  	0,508,509,1,0,0,0,509,507,1,0,0,0,509,510,1,0,0,0,510,511,1,0,0,0,511,
  	512,5,134,0,0,512,550,1,0,0,0,513,515,5,123,0,0,514,516,5,130,0,0,515,
  	514,1,0,0,0,516,517,1,0,0,0,517,515,1,0,0,0,517,518,1,0,0,0,518,519,1,
  	0,0,0,519,550,5,134,0,0,520,522,5,124,0,0,521,523,5,130,0,0,522,521,1,
  	0,0,0,523,524,1,0,0,0,524,522,1,0,0,0,524,525,1,0,0,0,525,527,1,0,0,0,
  	526,528,5,132,0,0,527,526,1,0,0,0,527,528,1,0,0,0,528,529,1,0,0,0,529,
  	550,5,134,0,0,530,531,5,125,0,0,531,533,5,131,0,0,532,534,5,132,0,0,533,
  	532,1,0,0,0,533,534,1,0,0,0,534,535,1,0,0,0,535,550,5,134,0,0,536,537,
  	5,126,0,0,537,538,5,130,0,0,538,550,5,134,0,0,539,541,5,127,0,0,540,542,
  	5,128,0,0,541,540,1,0,0,0,542,543,1,0,0,0,543,541,1,0,0,0,543,544,1,0,
  	0,0,544,545,1,0,0,0,545,550,5,134,0,0,546,547,3,34,17,0,547,548,5,134,
  	0,0,548,550,1,0,0,0,549,476,1,0,0,0,549,477,1,0,0,0,549,480,1,0,0,0,549,
  	483,1,0,0,0,549,495,1,0,0,0,549,502,1,0,0,0,549,505,1,0,0,0,549,513,1,
  	0,0,0,549,520,1,0,0,0,549,530,1,0,0,0,549,536,1,0,0,0,549,539,1,0,0,0,
  	549,546,1,0,0,0,550,31,1,0,0,0,551,552,7,4,0,0,552,33,1,0,0,0,553,557,
  	5,114,0,0,554,556,3,36,18,0,555,554,1,0,0,0,556,559,1,0,0,0,557,555,1,
  	0,0,0,557,558,1,0,0,0,558,560,1,0,0,0,559,557,1,0,0,0,560,561,5,135,0,
  	0,561,35,1,0,0,0,562,607,5,151,0,0,563,564,5,136,0,0,564,565,5,137,0,
  	0,565,607,5,151,0,0,566,568,5,138,0,0,567,569,5,147,0,0,568,567,1,0,0,
  	0,569,570,1,0,0,0,570,568,1,0,0,0,570,571,1,0,0,0,571,573,1,0,0,0,572,
  	574,5,149,0,0,573,572,1,0,0,0,574,575,1,0,0,0,575,573,1,0,0,0,575,576,
  	1,0,0,0,576,577,1,0,0,0,577,607,5,151,0,0,578,580,5,139,0,0,579,581,5,
  	147,0,0,580,579,1,0,0,0,581,582,1,0,0,0,582,580,1,0,0,0,582,583,1,0,0,
  	0,583,584,1,0,0,0,584,607,5,151,0,0,585,586,5,140,0,0,586,587,5,147,0,
  	0,587,607,5,151,0,0,588,590,5,141,0,0,589,591,3,38,19,0,590,589,1,0,0,
  	0,591,592,1,0,0,0,592,590,1,0,0,0,592,593,1,0,0,0,593,594,1,0,0,0,594,
  	595,5,151,0,0,595,607,1,0,0,0,596,597,5,137,0,0,597,598,7,5,0,0,598,607,
  	5,151,0,0,599,601,5,142,0,0,600,602,5,146,0,0,601,600,1,0,0,0,602,603,
  	1,0,0,0,603,601,1,0,0,0,603,604,1,0,0,0,604,605,1,0,0,0,605,607,5,151,
  	0,0,606,562,1,0,0,0,606,563,1,0,0,0,606,566,1,0,0,0,606,578,1,0,0,0,606,
  	585,1,0,0,0,606,588,1,0,0,0,606,596,1,0,0,0,606,599,1,0,0,0,607,37,1,
  	0,0,0,608,609,7,6,0,0,609,39,1,0,0,0,54,47,55,98,109,115,125,133,144,
  	151,158,171,198,206,213,226,233,240,265,273,315,323,334,344,355,366,377,
  	389,401,408,418,428,435,442,449,456,465,471,487,492,499,509,517,524,527,
  	533,543,549,557,570,575,582,592,603,606
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  sparkyspkparserParserStaticData = staticData.release();
}

}

SparkySPKParser::SparkySPKParser(TokenStream *input) : SparkySPKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

SparkySPKParser::SparkySPKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  SparkySPKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *sparkyspkparserParserStaticData->atn, sparkyspkparserParserStaticData->decisionToDFA, sparkyspkparserParserStaticData->sharedContextCache, options);
}

SparkySPKParser::~SparkySPKParser() {
  delete _interpreter;
}

const atn::ATN& SparkySPKParser::getATN() const {
  return *sparkyspkparserParserStaticData->atn;
}

std::string SparkySPKParser::getGrammarFileName() const {
  return "SparkySPKParser.g4";
}

const std::vector<std::string>& SparkySPKParser::getRuleNames() const {
  return sparkyspkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& SparkySPKParser::getVocabulary() const {
  return sparkyspkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView SparkySPKParser::getSerializedATN() const {
  return sparkyspkparserParserStaticData->serializedATN;
}


//----------------- Sparky_spkContext ------------------------------------------------------------------

SparkySPKParser::Sparky_spkContext::Sparky_spkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::Sparky_spkContext::EOF() {
  return getToken(SparkySPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Sparky_spkContext::Sparky_save_file() {
  return getTokens(SparkySPKParser::Sparky_save_file);
}

tree::TerminalNode* SparkySPKParser::Sparky_spkContext::Sparky_save_file(size_t i) {
  return getToken(SparkySPKParser::Sparky_save_file, i);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Sparky_spkContext::Version() {
  return getTokens(SparkySPKParser::Version);
}

tree::TerminalNode* SparkySPKParser::Sparky_spkContext::Version(size_t i) {
  return getToken(SparkySPKParser::Version, i);
}

std::vector<SparkySPKParser::User_blockContext *> SparkySPKParser::Sparky_spkContext::user_block() {
  return getRuleContexts<SparkySPKParser::User_blockContext>();
}

SparkySPKParser::User_blockContext* SparkySPKParser::Sparky_spkContext::user_block(size_t i) {
  return getRuleContext<SparkySPKParser::User_blockContext>(i);
}

std::vector<SparkySPKParser::Spectrum_blockContext *> SparkySPKParser::Sparky_spkContext::spectrum_block() {
  return getRuleContexts<SparkySPKParser::Spectrum_blockContext>();
}

SparkySPKParser::Spectrum_blockContext* SparkySPKParser::Sparky_spkContext::spectrum_block(size_t i) {
  return getRuleContext<SparkySPKParser::Spectrum_blockContext>(i);
}


size_t SparkySPKParser::Sparky_spkContext::getRuleIndex() const {
  return SparkySPKParser::RuleSparky_spk;
}


std::any SparkySPKParser::Sparky_spkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitSparky_spk(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::Sparky_spkContext* SparkySPKParser::sparky_spk() {
  Sparky_spkContext *_localctx = _tracker.createInstance<Sparky_spkContext>(_ctx, getState());
  enterRule(_localctx, 0, SparkySPKParser::RuleSparky_spk);
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
    setState(45); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(40);
      match(SparkySPKParser::Sparky_save_file);
      setState(41);
      match(SparkySPKParser::Version);
      setState(42);
      user_block();
      setState(43);
      spectrum_block();
      setState(47); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == SparkySPKParser::Sparky_save_file);
    setState(49);
    match(SparkySPKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- User_blockContext ------------------------------------------------------------------

SparkySPKParser::User_blockContext::User_blockContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::User_blockContext::User() {
  return getToken(SparkySPKParser::User, 0);
}

tree::TerminalNode* SparkySPKParser::User_blockContext::End_user() {
  return getToken(SparkySPKParser::End_user, 0);
}

std::vector<SparkySPKParser::User_statementContext *> SparkySPKParser::User_blockContext::user_statement() {
  return getRuleContexts<SparkySPKParser::User_statementContext>();
}

SparkySPKParser::User_statementContext* SparkySPKParser::User_blockContext::user_statement(size_t i) {
  return getRuleContext<SparkySPKParser::User_statementContext>(i);
}


size_t SparkySPKParser::User_blockContext::getRuleIndex() const {
  return SparkySPKParser::RuleUser_block;
}


std::any SparkySPKParser::User_blockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitUser_block(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::User_blockContext* SparkySPKParser::user_block() {
  User_blockContext *_localctx = _tracker.createInstance<User_blockContext>(_ctx, getState());
  enterRule(_localctx, 2, SparkySPKParser::RuleUser_block);
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
    setState(51);
    match(SparkySPKParser::User);
    setState(55);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 268961792) != 0)) {
      setState(52);
      user_statement();
      setState(57);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(58);
    match(SparkySPKParser::End_user);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- User_statementContext ------------------------------------------------------------------

SparkySPKParser::User_statementContext::User_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::User_statementContext::RETURN_US() {
  return getToken(SparkySPKParser::RETURN_US, 0);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Set() {
  return getToken(SparkySPKParser::Set, 0);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Mode_US() {
  return getToken(SparkySPKParser::Mode_US, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::User_statementContext::Integer_US() {
  return getTokens(SparkySPKParser::Integer_US);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Integer_US(size_t i) {
  return getToken(SparkySPKParser::Integer_US, i);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Save_prompt() {
  return getToken(SparkySPKParser::Save_prompt, 0);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Save_interval() {
  return getToken(SparkySPKParser::Save_interval, 0);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Resize_views() {
  return getToken(SparkySPKParser::Resize_views, 0);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Key_timeout() {
  return getToken(SparkySPKParser::Key_timeout, 0);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Cache_size() {
  return getToken(SparkySPKParser::Cache_size, 0);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Contour_graying() {
  return getToken(SparkySPKParser::Contour_graying, 0);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Default() {
  return getToken(SparkySPKParser::Default, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::User_statementContext::Print() {
  return getTokens(SparkySPKParser::Print);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Print(size_t i) {
  return getToken(SparkySPKParser::Print, i);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Command() {
  return getToken(SparkySPKParser::Command, 0);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Simple_name_US() {
  return getToken(SparkySPKParser::Simple_name_US, 0);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::File() {
  return getToken(SparkySPKParser::File, 0);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Options() {
  return getToken(SparkySPKParser::Options, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::User_statementContext::Float_US() {
  return getTokens(SparkySPKParser::Float_US);
}

tree::TerminalNode* SparkySPKParser::User_statementContext::Float_US(size_t i) {
  return getToken(SparkySPKParser::Float_US, i);
}


size_t SparkySPKParser::User_statementContext::getRuleIndex() const {
  return SparkySPKParser::RuleUser_statement;
}


std::any SparkySPKParser::User_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitUser_statement(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::User_statementContext* SparkySPKParser::user_statement() {
  User_statementContext *_localctx = _tracker.createInstance<User_statementContext>(_ctx, getState());
  enterRule(_localctx, 4, SparkySPKParser::RuleUser_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(109);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(60);
      match(SparkySPKParser::RETURN_US);
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(61);
      match(SparkySPKParser::Set);
      setState(62);
      match(SparkySPKParser::Mode_US);
      setState(63);
      match(SparkySPKParser::Integer_US);
      setState(64);
      match(SparkySPKParser::RETURN_US);
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(65);
      match(SparkySPKParser::Set);
      setState(66);
      match(SparkySPKParser::Save_prompt);
      setState(67);
      match(SparkySPKParser::Integer_US);
      setState(68);
      match(SparkySPKParser::RETURN_US);
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(69);
      match(SparkySPKParser::Set);
      setState(70);
      match(SparkySPKParser::Save_interval);
      setState(71);
      match(SparkySPKParser::Integer_US);
      setState(72);
      match(SparkySPKParser::RETURN_US);
      break;
    }

    case 5: {
      enterOuterAlt(_localctx, 5);
      setState(73);
      match(SparkySPKParser::Set);
      setState(74);
      match(SparkySPKParser::Resize_views);
      setState(75);
      match(SparkySPKParser::Integer_US);
      setState(76);
      match(SparkySPKParser::RETURN_US);
      break;
    }

    case 6: {
      enterOuterAlt(_localctx, 6);
      setState(77);
      match(SparkySPKParser::Set);
      setState(78);
      match(SparkySPKParser::Key_timeout);
      setState(79);
      match(SparkySPKParser::Integer_US);
      setState(80);
      match(SparkySPKParser::RETURN_US);
      break;
    }

    case 7: {
      enterOuterAlt(_localctx, 7);
      setState(81);
      match(SparkySPKParser::Set);
      setState(82);
      match(SparkySPKParser::Cache_size);
      setState(83);
      match(SparkySPKParser::Integer_US);
      setState(84);
      match(SparkySPKParser::RETURN_US);
      break;
    }

    case 8: {
      enterOuterAlt(_localctx, 8);
      setState(85);
      match(SparkySPKParser::Set);
      setState(86);
      match(SparkySPKParser::Contour_graying);
      setState(87);
      match(SparkySPKParser::Integer_US);
      setState(88);
      match(SparkySPKParser::RETURN_US);
      break;
    }

    case 9: {
      enterOuterAlt(_localctx, 9);
      setState(89);
      match(SparkySPKParser::Default);
      setState(90);
      match(SparkySPKParser::Print);
      setState(91);
      match(SparkySPKParser::Command);
      setState(92);
      _la = _input->LA(1);
      if (!(_la == SparkySPKParser::Print

      || _la == SparkySPKParser::Simple_name_US)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(93);
      match(SparkySPKParser::RETURN_US);
      break;
    }

    case 10: {
      enterOuterAlt(_localctx, 10);
      setState(94);
      match(SparkySPKParser::Default);
      setState(95);
      match(SparkySPKParser::Print);
      setState(96);
      match(SparkySPKParser::File);
      setState(98);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == SparkySPKParser::Simple_name_US) {
        setState(97);
        match(SparkySPKParser::Simple_name_US);
      }
      setState(100);
      match(SparkySPKParser::RETURN_US);
      break;
    }

    case 11: {
      enterOuterAlt(_localctx, 11);
      setState(101);
      match(SparkySPKParser::Default);
      setState(102);
      match(SparkySPKParser::Print);
      setState(103);
      match(SparkySPKParser::Options);
      setState(104);
      match(SparkySPKParser::Integer_US);
      setState(105);
      match(SparkySPKParser::Integer_US);
      setState(106);
      match(SparkySPKParser::Float_US);
      setState(107);
      match(SparkySPKParser::Float_US);
      setState(108);
      match(SparkySPKParser::RETURN_US);
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

//----------------- Spectrum_blockContext ------------------------------------------------------------------

SparkySPKParser::Spectrum_blockContext::Spectrum_blockContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::Spectrum_blockContext::Spectrum() {
  return getToken(SparkySPKParser::Spectrum, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_blockContext::End_spectrum() {
  return getToken(SparkySPKParser::End_spectrum, 0);
}

std::vector<SparkySPKParser::Spectrum_statementContext *> SparkySPKParser::Spectrum_blockContext::spectrum_statement() {
  return getRuleContexts<SparkySPKParser::Spectrum_statementContext>();
}

SparkySPKParser::Spectrum_statementContext* SparkySPKParser::Spectrum_blockContext::spectrum_statement(size_t i) {
  return getRuleContext<SparkySPKParser::Spectrum_statementContext>(i);
}


size_t SparkySPKParser::Spectrum_blockContext::getRuleIndex() const {
  return SparkySPKParser::RuleSpectrum_block;
}


std::any SparkySPKParser::Spectrum_blockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitSpectrum_block(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::Spectrum_blockContext* SparkySPKParser::spectrum_block() {
  Spectrum_blockContext *_localctx = _tracker.createInstance<Spectrum_blockContext>(_ctx, getState());
  enterRule(_localctx, 6, SparkySPKParser::RuleSpectrum_block);
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
    match(SparkySPKParser::Spectrum);
    setState(115);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((((_la - 29) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 29)) & 2286984184791031) != 0)) {
      setState(112);
      spectrum_statement();
      setState(117);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(118);
    match(SparkySPKParser::End_spectrum);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Spectrum_statementContext ------------------------------------------------------------------

SparkySPKParser::Spectrum_statementContext::Spectrum_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::RETURN_SP() {
  return getToken(SparkySPKParser::RETURN_SP, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Name_SP() {
  return getToken(SparkySPKParser::Name_SP, 0);
}

std::vector<SparkySPKParser::Spectrum_nameContext *> SparkySPKParser::Spectrum_statementContext::spectrum_name() {
  return getRuleContexts<SparkySPKParser::Spectrum_nameContext>();
}

SparkySPKParser::Spectrum_nameContext* SparkySPKParser::Spectrum_statementContext::spectrum_name(size_t i) {
  return getRuleContext<SparkySPKParser::Spectrum_nameContext>(i);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Path_name() {
  return getToken(SparkySPKParser::Path_name, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Dimension() {
  return getToken(SparkySPKParser::Dimension, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Spectrum_statementContext::Integer_SP() {
  return getTokens(SparkySPKParser::Integer_SP);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integer_SP(size_t i) {
  return getToken(SparkySPKParser::Integer_SP, i);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Shift() {
  return getToken(SparkySPKParser::Shift, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Spectrum_statementContext::Float_SP() {
  return getTokens(SparkySPKParser::Float_SP);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Float_SP(size_t i) {
  return getToken(SparkySPKParser::Float_SP, i);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Points() {
  return getToken(SparkySPKParser::Points, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Extra_peak_planes() {
  return getToken(SparkySPKParser::Extra_peak_planes, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Assign_multi_axis_guess() {
  return getToken(SparkySPKParser::Assign_multi_axis_guess, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Assign_guess_threshhold() {
  return getToken(SparkySPKParser::Assign_guess_threshhold, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Assign_relation() {
  return getToken(SparkySPKParser::Assign_relation, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Assign_range() {
  return getToken(SparkySPKParser::Assign_range, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Assign_format() {
  return getToken(SparkySPKParser::Assign_format, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Format_ex() {
  return getToken(SparkySPKParser::Format_ex, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::List_tool() {
  return getToken(SparkySPKParser::List_tool, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Sort_by() {
  return getToken(SparkySPKParser::Sort_by, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Spectrum_statementContext::Simple_name_SP() {
  return getTokens(SparkySPKParser::Simple_name_SP);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Simple_name_SP(size_t i) {
  return getToken(SparkySPKParser::Simple_name_SP, i);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Name_type() {
  return getToken(SparkySPKParser::Name_type, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Sort_axis() {
  return getToken(SparkySPKParser::Sort_axis, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Show_flags() {
  return getToken(SparkySPKParser::Show_flags, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_overlapped_sep() {
  return getToken(SparkySPKParser::Integrate_overlapped_sep, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_methods() {
  return getToken(SparkySPKParser::Integrate_methods, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_allow_motion() {
  return getToken(SparkySPKParser::Integrate_allow_motion, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_adjust_linewidths() {
  return getToken(SparkySPKParser::Integrate_adjust_linewidths, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_motion_range() {
  return getToken(SparkySPKParser::Integrate_motion_range, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_min_linewidth() {
  return getToken(SparkySPKParser::Integrate_min_linewidth, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_max_linewidth() {
  return getToken(SparkySPKParser::Integrate_max_linewidth, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_fit_baseline() {
  return getToken(SparkySPKParser::Integrate_fit_baseline, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_subtract_peaks() {
  return getToken(SparkySPKParser::Integrate_subtract_peaks, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_contoured_data() {
  return getToken(SparkySPKParser::Integrate_contoured_data, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_rectangle_data() {
  return getToken(SparkySPKParser::Integrate_rectangle_data, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_max_iterations() {
  return getToken(SparkySPKParser::Integrate_max_iterations, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Integrate_tolerance() {
  return getToken(SparkySPKParser::Integrate_tolerance, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Peak_pick() {
  return getToken(SparkySPKParser::Peak_pick, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Peak_pick_minimum_linewidth() {
  return getToken(SparkySPKParser::Peak_pick_minimum_linewidth, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Peak_pick_minimum_dropoff() {
  return getToken(SparkySPKParser::Peak_pick_minimum_dropoff, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Noise_sigma() {
  return getToken(SparkySPKParser::Noise_sigma, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Ornament_labe_size() {
  return getToken(SparkySPKParser::Ornament_labe_size, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Ornament_line_size() {
  return getToken(SparkySPKParser::Ornament_line_size, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Ornament_peak_size() {
  return getToken(SparkySPKParser::Ornament_peak_size, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Ornament_grid_size() {
  return getToken(SparkySPKParser::Ornament_grid_size, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Ornament_peak_group_size() {
  return getToken(SparkySPKParser::Ornament_peak_group_size, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Ornament_select_size() {
  return getToken(SparkySPKParser::Ornament_select_size, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Ornament_pointer_size() {
  return getToken(SparkySPKParser::Ornament_pointer_size, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_statementContext::Ornament_line_end_size() {
  return getToken(SparkySPKParser::Ornament_line_end_size, 0);
}

SparkySPKParser::Attached_dataContext* SparkySPKParser::Spectrum_statementContext::attached_data() {
  return getRuleContext<SparkySPKParser::Attached_dataContext>(0);
}

SparkySPKParser::ViewContext* SparkySPKParser::Spectrum_statementContext::view() {
  return getRuleContext<SparkySPKParser::ViewContext>(0);
}

SparkySPKParser::OrnamentContext* SparkySPKParser::Spectrum_statementContext::ornament() {
  return getRuleContext<SparkySPKParser::OrnamentContext>(0);
}


size_t SparkySPKParser::Spectrum_statementContext::getRuleIndex() const {
  return SparkySPKParser::RuleSpectrum_statement;
}


std::any SparkySPKParser::Spectrum_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitSpectrum_statement(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::Spectrum_statementContext* SparkySPKParser::spectrum_statement() {
  Spectrum_statementContext *_localctx = _tracker.createInstance<Spectrum_statementContext>(_ctx, getState());
  enterRule(_localctx, 8, SparkySPKParser::RuleSpectrum_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(315);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 19, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(120);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(121);
      match(SparkySPKParser::Name_SP);
      setState(125);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (((((_la - 75) & ~ 0x3fULL) == 0) &&
        ((1ULL << (_la - 75)) & 15) != 0)) {
        setState(122);
        spectrum_name();
        setState(127);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(128);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(129);
      match(SparkySPKParser::Path_name);
      setState(133);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (((((_la - 75) & ~ 0x3fULL) == 0) &&
        ((1ULL << (_la - 75)) & 15) != 0)) {
        setState(130);
        spectrum_name();
        setState(135);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(136);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(137);
      match(SparkySPKParser::Dimension);
      setState(138);
      match(SparkySPKParser::Integer_SP);
      setState(139);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 5: {
      enterOuterAlt(_localctx, 5);
      setState(140);
      match(SparkySPKParser::Shift);
      setState(142); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(141);
        match(SparkySPKParser::Float_SP);
        setState(144); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Float_SP);
      setState(146);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 6: {
      enterOuterAlt(_localctx, 6);
      setState(147);
      match(SparkySPKParser::Points);
      setState(149); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(148);
        match(SparkySPKParser::Integer_SP);
        setState(151); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Integer_SP);
      setState(153);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 7: {
      enterOuterAlt(_localctx, 7);
      setState(154);
      match(SparkySPKParser::Extra_peak_planes);
      setState(156); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(155);
        match(SparkySPKParser::Integer_SP);
        setState(158); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Integer_SP);
      setState(160);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 8: {
      enterOuterAlt(_localctx, 8);
      setState(161);
      match(SparkySPKParser::Assign_multi_axis_guess);
      setState(162);
      match(SparkySPKParser::Integer_SP);
      setState(163);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 9: {
      enterOuterAlt(_localctx, 9);
      setState(164);
      match(SparkySPKParser::Assign_guess_threshhold);
      setState(165);
      match(SparkySPKParser::Float_SP);
      setState(166);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 10: {
      enterOuterAlt(_localctx, 10);
      setState(167);
      match(SparkySPKParser::Assign_relation);
      setState(169); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(168);
        match(SparkySPKParser::Integer_SP);
        setState(171); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Integer_SP);
      setState(173);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 11: {
      enterOuterAlt(_localctx, 11);
      setState(174);
      match(SparkySPKParser::Assign_range);
      setState(175);
      match(SparkySPKParser::Integer_SP);
      setState(176);
      match(SparkySPKParser::Float_SP);
      setState(177);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 12: {
      enterOuterAlt(_localctx, 12);
      setState(178);
      match(SparkySPKParser::Assign_format);
      setState(179);
      match(SparkySPKParser::Format_ex);
      setState(180);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 13: {
      enterOuterAlt(_localctx, 13);
      setState(181);
      match(SparkySPKParser::List_tool);
      setState(182);
      match(SparkySPKParser::Sort_by);
      setState(183);
      match(SparkySPKParser::Simple_name_SP);
      setState(184);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 14: {
      enterOuterAlt(_localctx, 14);
      setState(185);
      match(SparkySPKParser::List_tool);
      setState(186);
      match(SparkySPKParser::Name_type);
      setState(187);
      match(SparkySPKParser::Simple_name_SP);
      setState(188);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 15: {
      enterOuterAlt(_localctx, 15);
      setState(189);
      match(SparkySPKParser::List_tool);
      setState(190);
      match(SparkySPKParser::Sort_axis);
      setState(191);
      match(SparkySPKParser::Simple_name_SP);
      setState(192);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 16: {
      enterOuterAlt(_localctx, 16);
      setState(193);
      match(SparkySPKParser::List_tool);
      setState(194);
      match(SparkySPKParser::Show_flags);
      setState(198);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == SparkySPKParser::Simple_name_SP) {
        setState(195);
        match(SparkySPKParser::Simple_name_SP);
        setState(200);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(201);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 17: {
      enterOuterAlt(_localctx, 17);
      setState(202);
      match(SparkySPKParser::Integrate_overlapped_sep);
      setState(204); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(203);
        match(SparkySPKParser::Float_SP);
        setState(206); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Float_SP);
      setState(208);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 18: {
      enterOuterAlt(_localctx, 18);
      setState(209);
      match(SparkySPKParser::Integrate_methods);
      setState(211); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(210);
        match(SparkySPKParser::Integer_SP);
        setState(213); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Integer_SP);
      setState(215);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 19: {
      enterOuterAlt(_localctx, 19);
      setState(216);
      match(SparkySPKParser::Integrate_allow_motion);
      setState(217);
      match(SparkySPKParser::Integer_SP);
      setState(218);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 20: {
      enterOuterAlt(_localctx, 20);
      setState(219);
      match(SparkySPKParser::Integrate_adjust_linewidths);
      setState(220);
      match(SparkySPKParser::Integer_SP);
      setState(221);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 21: {
      enterOuterAlt(_localctx, 21);
      setState(222);
      match(SparkySPKParser::Integrate_motion_range);
      setState(224); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(223);
        match(SparkySPKParser::Float_SP);
        setState(226); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Float_SP);
      setState(228);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 22: {
      enterOuterAlt(_localctx, 22);
      setState(229);
      match(SparkySPKParser::Integrate_min_linewidth);
      setState(231); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(230);
        match(SparkySPKParser::Float_SP);
        setState(233); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Float_SP);
      setState(235);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 23: {
      enterOuterAlt(_localctx, 23);
      setState(236);
      match(SparkySPKParser::Integrate_max_linewidth);
      setState(238); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(237);
        match(SparkySPKParser::Float_SP);
        setState(240); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Float_SP);
      setState(242);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 24: {
      enterOuterAlt(_localctx, 24);
      setState(243);
      match(SparkySPKParser::Integrate_fit_baseline);
      setState(244);
      match(SparkySPKParser::Integer_SP);
      setState(245);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 25: {
      enterOuterAlt(_localctx, 25);
      setState(246);
      match(SparkySPKParser::Integrate_subtract_peaks);
      setState(247);
      match(SparkySPKParser::Integer_SP);
      setState(248);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 26: {
      enterOuterAlt(_localctx, 26);
      setState(249);
      match(SparkySPKParser::Integrate_contoured_data);
      setState(250);
      match(SparkySPKParser::Integer_SP);
      setState(251);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 27: {
      enterOuterAlt(_localctx, 27);
      setState(252);
      match(SparkySPKParser::Integrate_rectangle_data);
      setState(253);
      match(SparkySPKParser::Integer_SP);
      setState(254);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 28: {
      enterOuterAlt(_localctx, 28);
      setState(255);
      match(SparkySPKParser::Integrate_max_iterations);
      setState(256);
      match(SparkySPKParser::Integer_SP);
      setState(257);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 29: {
      enterOuterAlt(_localctx, 29);
      setState(258);
      match(SparkySPKParser::Integrate_tolerance);
      setState(259);
      match(SparkySPKParser::Float_SP);
      setState(260);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 30: {
      enterOuterAlt(_localctx, 30);
      setState(261);
      match(SparkySPKParser::Peak_pick);
      setState(263); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(262);
        match(SparkySPKParser::Float_SP);
        setState(265); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Float_SP);
      setState(267);
      match(SparkySPKParser::Integer_SP);
      setState(268);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 31: {
      enterOuterAlt(_localctx, 31);
      setState(269);
      match(SparkySPKParser::Peak_pick_minimum_linewidth);
      setState(271); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(270);
        match(SparkySPKParser::Float_SP);
        setState(273); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Float_SP);
      setState(275);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 32: {
      enterOuterAlt(_localctx, 32);
      setState(276);
      match(SparkySPKParser::Peak_pick_minimum_dropoff);
      setState(277);
      match(SparkySPKParser::Float_SP);
      setState(278);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 33: {
      enterOuterAlt(_localctx, 33);
      setState(279);
      match(SparkySPKParser::Noise_sigma);
      setState(280);
      match(SparkySPKParser::Float_SP);
      setState(281);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 34: {
      enterOuterAlt(_localctx, 34);
      setState(282);
      match(SparkySPKParser::Ornament_labe_size);
      setState(283);
      match(SparkySPKParser::Float_SP);
      setState(284);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 35: {
      enterOuterAlt(_localctx, 35);
      setState(285);
      match(SparkySPKParser::Ornament_line_size);
      setState(286);
      match(SparkySPKParser::Float_SP);
      setState(287);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 36: {
      enterOuterAlt(_localctx, 36);
      setState(288);
      match(SparkySPKParser::Ornament_peak_size);
      setState(289);
      match(SparkySPKParser::Float_SP);
      setState(290);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 37: {
      enterOuterAlt(_localctx, 37);
      setState(291);
      match(SparkySPKParser::Ornament_grid_size);
      setState(292);
      match(SparkySPKParser::Float_SP);
      setState(293);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 38: {
      enterOuterAlt(_localctx, 38);
      setState(294);
      match(SparkySPKParser::Ornament_peak_group_size);
      setState(295);
      match(SparkySPKParser::Float_SP);
      setState(296);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 39: {
      enterOuterAlt(_localctx, 39);
      setState(297);
      match(SparkySPKParser::Ornament_select_size);
      setState(298);
      match(SparkySPKParser::Float_SP);
      setState(299);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 40: {
      enterOuterAlt(_localctx, 40);
      setState(300);
      match(SparkySPKParser::Ornament_pointer_size);
      setState(301);
      match(SparkySPKParser::Float_SP);
      setState(302);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 41: {
      enterOuterAlt(_localctx, 41);
      setState(303);
      match(SparkySPKParser::Ornament_line_end_size);
      setState(304);
      match(SparkySPKParser::Float_SP);
      setState(305);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 42: {
      enterOuterAlt(_localctx, 42);
      setState(306);
      attached_data();
      setState(307);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 43: {
      enterOuterAlt(_localctx, 43);
      setState(309);
      view();
      setState(310);
      match(SparkySPKParser::RETURN_SP);
      break;
    }

    case 44: {
      enterOuterAlt(_localctx, 44);
      setState(312);
      ornament();
      setState(313);
      match(SparkySPKParser::RETURN_SP);
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

//----------------- Spectrum_nameContext ------------------------------------------------------------------

SparkySPKParser::Spectrum_nameContext::Spectrum_nameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::Spectrum_nameContext::Integer_SP() {
  return getToken(SparkySPKParser::Integer_SP, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_nameContext::Float_SP() {
  return getToken(SparkySPKParser::Float_SP, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_nameContext::Simple_name_SP() {
  return getToken(SparkySPKParser::Simple_name_SP, 0);
}

tree::TerminalNode* SparkySPKParser::Spectrum_nameContext::Any_name_SP() {
  return getToken(SparkySPKParser::Any_name_SP, 0);
}


size_t SparkySPKParser::Spectrum_nameContext::getRuleIndex() const {
  return SparkySPKParser::RuleSpectrum_name;
}


std::any SparkySPKParser::Spectrum_nameContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitSpectrum_name(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::Spectrum_nameContext* SparkySPKParser::spectrum_name() {
  Spectrum_nameContext *_localctx = _tracker.createInstance<Spectrum_nameContext>(_ctx, getState());
  enterRule(_localctx, 10, SparkySPKParser::RuleSpectrum_name);
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
    setState(317);
    _la = _input->LA(1);
    if (!(((((_la - 75) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 75)) & 15) != 0))) {
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

//----------------- Attached_dataContext ------------------------------------------------------------------

SparkySPKParser::Attached_dataContext::Attached_dataContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::Attached_dataContext::Attached_data() {
  return getToken(SparkySPKParser::Attached_data, 0);
}

tree::TerminalNode* SparkySPKParser::Attached_dataContext::End_attached_data() {
  return getToken(SparkySPKParser::End_attached_data, 0);
}

std::vector<SparkySPKParser::Attached_data_statementContext *> SparkySPKParser::Attached_dataContext::attached_data_statement() {
  return getRuleContexts<SparkySPKParser::Attached_data_statementContext>();
}

SparkySPKParser::Attached_data_statementContext* SparkySPKParser::Attached_dataContext::attached_data_statement(size_t i) {
  return getRuleContext<SparkySPKParser::Attached_data_statementContext>(i);
}


size_t SparkySPKParser::Attached_dataContext::getRuleIndex() const {
  return SparkySPKParser::RuleAttached_data;
}


std::any SparkySPKParser::Attached_dataContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitAttached_data(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::Attached_dataContext* SparkySPKParser::attached_data() {
  Attached_dataContext *_localctx = _tracker.createInstance<Attached_dataContext>(_ctx, getState());
  enterRule(_localctx, 12, SparkySPKParser::RuleAttached_data);
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
    setState(319);
    match(SparkySPKParser::Attached_data);
    setState(323);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == SparkySPKParser::Any_name_AD) {
      setState(320);
      attached_data_statement();
      setState(325);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(326);
    match(SparkySPKParser::End_attached_data);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Attached_data_statementContext ------------------------------------------------------------------

SparkySPKParser::Attached_data_statementContext::Attached_data_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::Attached_data_statementContext::Any_name_AD() {
  return getToken(SparkySPKParser::Any_name_AD, 0);
}


size_t SparkySPKParser::Attached_data_statementContext::getRuleIndex() const {
  return SparkySPKParser::RuleAttached_data_statement;
}


std::any SparkySPKParser::Attached_data_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitAttached_data_statement(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::Attached_data_statementContext* SparkySPKParser::attached_data_statement() {
  Attached_data_statementContext *_localctx = _tracker.createInstance<Attached_data_statementContext>(_ctx, getState());
  enterRule(_localctx, 14, SparkySPKParser::RuleAttached_data_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(328);
    match(SparkySPKParser::Any_name_AD);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ViewContext ------------------------------------------------------------------

SparkySPKParser::ViewContext::ViewContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::ViewContext::View() {
  return getToken(SparkySPKParser::View, 0);
}

tree::TerminalNode* SparkySPKParser::ViewContext::End_view() {
  return getToken(SparkySPKParser::End_view, 0);
}

std::vector<SparkySPKParser::View_statementContext *> SparkySPKParser::ViewContext::view_statement() {
  return getRuleContexts<SparkySPKParser::View_statementContext>();
}

SparkySPKParser::View_statementContext* SparkySPKParser::ViewContext::view_statement(size_t i) {
  return getRuleContext<SparkySPKParser::View_statementContext>(i);
}


size_t SparkySPKParser::ViewContext::getRuleIndex() const {
  return SparkySPKParser::RuleView;
}


std::any SparkySPKParser::ViewContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitView(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::ViewContext* SparkySPKParser::view() {
  ViewContext *_localctx = _tracker.createInstance<ViewContext>(_ctx, getState());
  enterRule(_localctx, 16, SparkySPKParser::RuleView);
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
    setState(330);
    match(SparkySPKParser::View);
    setState(334);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((((_la - 84) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 84)) & 67581) != 0)) {
      setState(331);
      view_statement();
      setState(336);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(337);
    match(SparkySPKParser::End_view);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- View_statementContext ------------------------------------------------------------------

SparkySPKParser::View_statementContext::View_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::View_statementContext::RETURN_VI() {
  return getToken(SparkySPKParser::RETURN_VI, 0);
}

tree::TerminalNode* SparkySPKParser::View_statementContext::Name_VI() {
  return getToken(SparkySPKParser::Name_VI, 0);
}

std::vector<SparkySPKParser::View_nameContext *> SparkySPKParser::View_statementContext::view_name() {
  return getRuleContexts<SparkySPKParser::View_nameContext>();
}

SparkySPKParser::View_nameContext* SparkySPKParser::View_statementContext::view_name(size_t i) {
  return getRuleContext<SparkySPKParser::View_nameContext>(i);
}

tree::TerminalNode* SparkySPKParser::View_statementContext::Precision() {
  return getToken(SparkySPKParser::Precision, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::View_statementContext::Integer_VI() {
  return getTokens(SparkySPKParser::Integer_VI);
}

tree::TerminalNode* SparkySPKParser::View_statementContext::Integer_VI(size_t i) {
  return getToken(SparkySPKParser::Integer_VI, i);
}

tree::TerminalNode* SparkySPKParser::View_statementContext::Precision_by_units() {
  return getToken(SparkySPKParser::Precision_by_units, 0);
}

tree::TerminalNode* SparkySPKParser::View_statementContext::View_mode() {
  return getToken(SparkySPKParser::View_mode, 0);
}

tree::TerminalNode* SparkySPKParser::View_statementContext::Show() {
  return getToken(SparkySPKParser::Show, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::View_statementContext::Simple_name_VI() {
  return getTokens(SparkySPKParser::Simple_name_VI);
}

tree::TerminalNode* SparkySPKParser::View_statementContext::Simple_name_VI(size_t i) {
  return getToken(SparkySPKParser::Simple_name_VI, i);
}

tree::TerminalNode* SparkySPKParser::View_statementContext::Axis_type() {
  return getToken(SparkySPKParser::Axis_type, 0);
}

tree::TerminalNode* SparkySPKParser::View_statementContext::Flags_VI() {
  return getToken(SparkySPKParser::Flags_VI, 0);
}

tree::TerminalNode* SparkySPKParser::View_statementContext::Contour_pos() {
  return getToken(SparkySPKParser::Contour_pos, 0);
}

SparkySPKParser::View_numberContext* SparkySPKParser::View_statementContext::view_number() {
  return getRuleContext<SparkySPKParser::View_numberContext>(0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::View_statementContext::Float_VI() {
  return getTokens(SparkySPKParser::Float_VI);
}

tree::TerminalNode* SparkySPKParser::View_statementContext::Float_VI(size_t i) {
  return getToken(SparkySPKParser::Float_VI, i);
}

tree::TerminalNode* SparkySPKParser::View_statementContext::Contour_neg() {
  return getToken(SparkySPKParser::Contour_neg, 0);
}

SparkySPKParser::ParamsContext* SparkySPKParser::View_statementContext::params() {
  return getRuleContext<SparkySPKParser::ParamsContext>(0);
}


size_t SparkySPKParser::View_statementContext::getRuleIndex() const {
  return SparkySPKParser::RuleView_statement;
}


std::any SparkySPKParser::View_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitView_statement(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::View_statementContext* SparkySPKParser::view_statement() {
  View_statementContext *_localctx = _tracker.createInstance<View_statementContext>(_ctx, getState());
  enterRule(_localctx, 18, SparkySPKParser::RuleView_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(408);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case SparkySPKParser::RETURN_VI: {
        enterOuterAlt(_localctx, 1);
        setState(339);
        match(SparkySPKParser::RETURN_VI);
        break;
      }

      case SparkySPKParser::Name_VI: {
        enterOuterAlt(_localctx, 2);
        setState(340);
        match(SparkySPKParser::Name_VI);
        setState(344);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (((((_la - 95) & ~ 0x3fULL) == 0) &&
          ((1ULL << (_la - 95)) & 15) != 0)) {
          setState(341);
          view_name();
          setState(346);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        setState(347);
        match(SparkySPKParser::RETURN_VI);
        break;
      }

      case SparkySPKParser::Precision: {
        enterOuterAlt(_localctx, 3);
        setState(348);
        match(SparkySPKParser::Precision);
        setState(349);
        match(SparkySPKParser::Integer_VI);
        setState(350);
        match(SparkySPKParser::RETURN_VI);
        break;
      }

      case SparkySPKParser::Precision_by_units: {
        enterOuterAlt(_localctx, 4);
        setState(351);
        match(SparkySPKParser::Precision_by_units);
        setState(353); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(352);
          match(SparkySPKParser::Integer_VI);
          setState(355); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Integer_VI);
        setState(357);
        match(SparkySPKParser::RETURN_VI);
        break;
      }

      case SparkySPKParser::View_mode: {
        enterOuterAlt(_localctx, 5);
        setState(358);
        match(SparkySPKParser::View_mode);
        setState(359);
        match(SparkySPKParser::Integer_VI);
        setState(360);
        match(SparkySPKParser::RETURN_VI);
        break;
      }

      case SparkySPKParser::Show: {
        enterOuterAlt(_localctx, 6);
        setState(361);
        match(SparkySPKParser::Show);
        setState(362);
        match(SparkySPKParser::Integer_VI);
        setState(366);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == SparkySPKParser::Simple_name_VI) {
          setState(363);
          match(SparkySPKParser::Simple_name_VI);
          setState(368);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        setState(369);
        match(SparkySPKParser::RETURN_VI);
        break;
      }

      case SparkySPKParser::Axis_type: {
        enterOuterAlt(_localctx, 7);
        setState(370);
        match(SparkySPKParser::Axis_type);
        setState(371);
        match(SparkySPKParser::Integer_VI);
        setState(372);
        match(SparkySPKParser::RETURN_VI);
        break;
      }

      case SparkySPKParser::Flags_VI: {
        enterOuterAlt(_localctx, 8);
        setState(373);
        match(SparkySPKParser::Flags_VI);
        setState(377);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == SparkySPKParser::Simple_name_VI) {
          setState(374);
          match(SparkySPKParser::Simple_name_VI);
          setState(379);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        setState(380);
        match(SparkySPKParser::RETURN_VI);
        break;
      }

      case SparkySPKParser::Contour_pos: {
        enterOuterAlt(_localctx, 9);
        setState(381);
        match(SparkySPKParser::Contour_pos);
        setState(382);
        match(SparkySPKParser::Integer_VI);
        setState(383);
        view_number();
        setState(384);
        match(SparkySPKParser::Float_VI);
        setState(385);
        match(SparkySPKParser::Float_VI);
        setState(387); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(386);
          match(SparkySPKParser::Simple_name_VI);
          setState(389); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Simple_name_VI);
        setState(391);
        match(SparkySPKParser::RETURN_VI);
        break;
      }

      case SparkySPKParser::Contour_neg: {
        enterOuterAlt(_localctx, 10);
        setState(393);
        match(SparkySPKParser::Contour_neg);
        setState(394);
        match(SparkySPKParser::Integer_VI);
        setState(395);
        view_number();
        setState(396);
        match(SparkySPKParser::Float_VI);
        setState(397);
        match(SparkySPKParser::Float_VI);
        setState(399); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(398);
          match(SparkySPKParser::Simple_name_VI);
          setState(401); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Simple_name_VI);
        setState(403);
        match(SparkySPKParser::RETURN_VI);
        break;
      }

      case SparkySPKParser::Params: {
        enterOuterAlt(_localctx, 11);
        setState(405);
        params();
        setState(406);
        match(SparkySPKParser::RETURN_VI);
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

//----------------- View_nameContext ------------------------------------------------------------------

SparkySPKParser::View_nameContext::View_nameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::View_nameContext::Integer_VI() {
  return getToken(SparkySPKParser::Integer_VI, 0);
}

tree::TerminalNode* SparkySPKParser::View_nameContext::Float_VI() {
  return getToken(SparkySPKParser::Float_VI, 0);
}

tree::TerminalNode* SparkySPKParser::View_nameContext::Real_VI() {
  return getToken(SparkySPKParser::Real_VI, 0);
}

tree::TerminalNode* SparkySPKParser::View_nameContext::Simple_name_VI() {
  return getToken(SparkySPKParser::Simple_name_VI, 0);
}


size_t SparkySPKParser::View_nameContext::getRuleIndex() const {
  return SparkySPKParser::RuleView_name;
}


std::any SparkySPKParser::View_nameContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitView_name(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::View_nameContext* SparkySPKParser::view_name() {
  View_nameContext *_localctx = _tracker.createInstance<View_nameContext>(_ctx, getState());
  enterRule(_localctx, 20, SparkySPKParser::RuleView_name);
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
    setState(410);
    _la = _input->LA(1);
    if (!(((((_la - 95) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 95)) & 15) != 0))) {
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

//----------------- View_numberContext ------------------------------------------------------------------

SparkySPKParser::View_numberContext::View_numberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::View_numberContext::Integer_VI() {
  return getToken(SparkySPKParser::Integer_VI, 0);
}

tree::TerminalNode* SparkySPKParser::View_numberContext::Float_VI() {
  return getToken(SparkySPKParser::Float_VI, 0);
}

tree::TerminalNode* SparkySPKParser::View_numberContext::Real_VI() {
  return getToken(SparkySPKParser::Real_VI, 0);
}


size_t SparkySPKParser::View_numberContext::getRuleIndex() const {
  return SparkySPKParser::RuleView_number;
}


std::any SparkySPKParser::View_numberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitView_number(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::View_numberContext* SparkySPKParser::view_number() {
  View_numberContext *_localctx = _tracker.createInstance<View_numberContext>(_ctx, getState());
  enterRule(_localctx, 22, SparkySPKParser::RuleView_number);
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
    setState(412);
    _la = _input->LA(1);
    if (!(((((_la - 95) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 95)) & 7) != 0))) {
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

//----------------- ParamsContext ------------------------------------------------------------------

SparkySPKParser::ParamsContext::ParamsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::ParamsContext::Params() {
  return getToken(SparkySPKParser::Params, 0);
}

tree::TerminalNode* SparkySPKParser::ParamsContext::End_params() {
  return getToken(SparkySPKParser::End_params, 0);
}

std::vector<SparkySPKParser::Params_statementContext *> SparkySPKParser::ParamsContext::params_statement() {
  return getRuleContexts<SparkySPKParser::Params_statementContext>();
}

SparkySPKParser::Params_statementContext* SparkySPKParser::ParamsContext::params_statement(size_t i) {
  return getRuleContext<SparkySPKParser::Params_statementContext>(i);
}


size_t SparkySPKParser::ParamsContext::getRuleIndex() const {
  return SparkySPKParser::RuleParams;
}


std::any SparkySPKParser::ParamsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitParams(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::ParamsContext* SparkySPKParser::params() {
  ParamsContext *_localctx = _tracker.createInstance<ParamsContext>(_ctx, getState());
  enterRule(_localctx, 24, SparkySPKParser::RuleParams);
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
    setState(414);
    match(SparkySPKParser::Params);
    setState(418);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((((_la - 102) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 102)) & 2175) != 0)) {
      setState(415);
      params_statement();
      setState(420);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(421);
    match(SparkySPKParser::End_params);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Params_statementContext ------------------------------------------------------------------

SparkySPKParser::Params_statementContext::Params_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::Params_statementContext::RETURN_PA() {
  return getToken(SparkySPKParser::RETURN_PA, 0);
}

tree::TerminalNode* SparkySPKParser::Params_statementContext::Orientation() {
  return getToken(SparkySPKParser::Orientation, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Params_statementContext::Integer_PA() {
  return getTokens(SparkySPKParser::Integer_PA);
}

tree::TerminalNode* SparkySPKParser::Params_statementContext::Integer_PA(size_t i) {
  return getToken(SparkySPKParser::Integer_PA, i);
}

tree::TerminalNode* SparkySPKParser::Params_statementContext::Location() {
  return getToken(SparkySPKParser::Location, 0);
}

tree::TerminalNode* SparkySPKParser::Params_statementContext::Size() {
  return getToken(SparkySPKParser::Size, 0);
}

tree::TerminalNode* SparkySPKParser::Params_statementContext::Offset() {
  return getToken(SparkySPKParser::Offset, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Params_statementContext::Float_PA() {
  return getTokens(SparkySPKParser::Float_PA);
}

tree::TerminalNode* SparkySPKParser::Params_statementContext::Float_PA(size_t i) {
  return getToken(SparkySPKParser::Float_PA, i);
}

tree::TerminalNode* SparkySPKParser::Params_statementContext::Scale() {
  return getToken(SparkySPKParser::Scale, 0);
}

tree::TerminalNode* SparkySPKParser::Params_statementContext::Zoom() {
  return getToken(SparkySPKParser::Zoom, 0);
}

tree::TerminalNode* SparkySPKParser::Params_statementContext::Flags_PA() {
  return getToken(SparkySPKParser::Flags_PA, 0);
}


size_t SparkySPKParser::Params_statementContext::getRuleIndex() const {
  return SparkySPKParser::RuleParams_statement;
}


std::any SparkySPKParser::Params_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitParams_statement(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::Params_statementContext* SparkySPKParser::params_statement() {
  Params_statementContext *_localctx = _tracker.createInstance<Params_statementContext>(_ctx, getState());
  enterRule(_localctx, 26, SparkySPKParser::RuleParams_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(465);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case SparkySPKParser::RETURN_PA: {
        enterOuterAlt(_localctx, 1);
        setState(423);
        match(SparkySPKParser::RETURN_PA);
        break;
      }

      case SparkySPKParser::Orientation: {
        enterOuterAlt(_localctx, 2);
        setState(424);
        match(SparkySPKParser::Orientation);
        setState(426); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(425);
          match(SparkySPKParser::Integer_PA);
          setState(428); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Integer_PA);
        setState(430);
        match(SparkySPKParser::RETURN_PA);
        break;
      }

      case SparkySPKParser::Location: {
        enterOuterAlt(_localctx, 3);
        setState(431);
        match(SparkySPKParser::Location);
        setState(433); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(432);
          match(SparkySPKParser::Integer_PA);
          setState(435); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Integer_PA);
        setState(437);
        match(SparkySPKParser::RETURN_PA);
        break;
      }

      case SparkySPKParser::Size: {
        enterOuterAlt(_localctx, 4);
        setState(438);
        match(SparkySPKParser::Size);
        setState(440); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(439);
          match(SparkySPKParser::Integer_PA);
          setState(442); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Integer_PA);
        setState(444);
        match(SparkySPKParser::RETURN_PA);
        break;
      }

      case SparkySPKParser::Offset: {
        enterOuterAlt(_localctx, 5);
        setState(445);
        match(SparkySPKParser::Offset);
        setState(447); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(446);
          match(SparkySPKParser::Float_PA);
          setState(449); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Float_PA);
        setState(451);
        match(SparkySPKParser::RETURN_PA);
        break;
      }

      case SparkySPKParser::Scale: {
        enterOuterAlt(_localctx, 6);
        setState(452);
        match(SparkySPKParser::Scale);
        setState(454); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(453);
          match(SparkySPKParser::Float_PA);
          setState(456); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Float_PA);
        setState(458);
        match(SparkySPKParser::RETURN_PA);
        break;
      }

      case SparkySPKParser::Zoom: {
        enterOuterAlt(_localctx, 7);
        setState(459);
        match(SparkySPKParser::Zoom);
        setState(460);
        match(SparkySPKParser::Float_PA);
        setState(461);
        match(SparkySPKParser::RETURN_PA);
        break;
      }

      case SparkySPKParser::Flags_PA: {
        enterOuterAlt(_localctx, 8);
        setState(462);
        match(SparkySPKParser::Flags_PA);
        setState(463);
        match(SparkySPKParser::Integer_PA);
        setState(464);
        match(SparkySPKParser::RETURN_PA);
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

//----------------- OrnamentContext ------------------------------------------------------------------

SparkySPKParser::OrnamentContext::OrnamentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::OrnamentContext::Ornament() {
  return getToken(SparkySPKParser::Ornament, 0);
}

tree::TerminalNode* SparkySPKParser::OrnamentContext::End_ornament() {
  return getToken(SparkySPKParser::End_ornament, 0);
}

std::vector<SparkySPKParser::Ornament_statementContext *> SparkySPKParser::OrnamentContext::ornament_statement() {
  return getRuleContexts<SparkySPKParser::Ornament_statementContext>();
}

SparkySPKParser::Ornament_statementContext* SparkySPKParser::OrnamentContext::ornament_statement(size_t i) {
  return getRuleContext<SparkySPKParser::Ornament_statementContext>(i);
}


size_t SparkySPKParser::OrnamentContext::getRuleIndex() const {
  return SparkySPKParser::RuleOrnament;
}


std::any SparkySPKParser::OrnamentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitOrnament(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::OrnamentContext* SparkySPKParser::ornament() {
  OrnamentContext *_localctx = _tracker.createInstance<OrnamentContext>(_ctx, getState());
  enterRule(_localctx, 28, SparkySPKParser::RuleOrnament);
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
    setState(467);
    match(SparkySPKParser::Ornament);
    setState(471);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((((_la - 114) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 114)) & 1064933) != 0)) {
      setState(468);
      ornament_statement();
      setState(473);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(474);
    match(SparkySPKParser::End_ornament);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ornament_statementContext ------------------------------------------------------------------

SparkySPKParser::Ornament_statementContext::Ornament_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::RETURN_OR() {
  return getToken(SparkySPKParser::RETURN_OR, 0);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Type_OR() {
  return getToken(SparkySPKParser::Type_OR, 0);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Peak() {
  return getToken(SparkySPKParser::Peak, 0);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Grid() {
  return getToken(SparkySPKParser::Grid, 0);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Color_OR() {
  return getToken(SparkySPKParser::Color_OR, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Ornament_statementContext::Integer_OR() {
  return getTokens(SparkySPKParser::Integer_OR);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Integer_OR(size_t i) {
  return getToken(SparkySPKParser::Integer_OR, i);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Ornament_statementContext::Simple_name_OR() {
  return getTokens(SparkySPKParser::Simple_name_OR);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Simple_name_OR(size_t i) {
  return getToken(SparkySPKParser::Simple_name_OR, i);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Flags_OR() {
  return getToken(SparkySPKParser::Flags_OR, 0);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Id() {
  return getToken(SparkySPKParser::Id, 0);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Pos_OR() {
  return getToken(SparkySPKParser::Pos_OR, 0);
}

std::vector<SparkySPKParser::Ornament_positionContext *> SparkySPKParser::Ornament_statementContext::ornament_position() {
  return getRuleContexts<SparkySPKParser::Ornament_positionContext>();
}

SparkySPKParser::Ornament_positionContext* SparkySPKParser::Ornament_statementContext::ornament_position(size_t i) {
  return getRuleContext<SparkySPKParser::Ornament_positionContext>(i);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Height() {
  return getToken(SparkySPKParser::Height, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Ornament_statementContext::Float_OR() {
  return getTokens(SparkySPKParser::Float_OR);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Float_OR(size_t i) {
  return getToken(SparkySPKParser::Float_OR, i);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Line_width() {
  return getToken(SparkySPKParser::Line_width, 0);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Integral() {
  return getToken(SparkySPKParser::Integral, 0);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Real_OR() {
  return getToken(SparkySPKParser::Real_OR, 0);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Fr() {
  return getToken(SparkySPKParser::Fr, 0);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Rs() {
  return getToken(SparkySPKParser::Rs, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Ornament_statementContext::Rs_ex() {
  return getTokens(SparkySPKParser::Rs_ex);
}

tree::TerminalNode* SparkySPKParser::Ornament_statementContext::Rs_ex(size_t i) {
  return getToken(SparkySPKParser::Rs_ex, i);
}

SparkySPKParser::LabelContext* SparkySPKParser::Ornament_statementContext::label() {
  return getRuleContext<SparkySPKParser::LabelContext>(0);
}


size_t SparkySPKParser::Ornament_statementContext::getRuleIndex() const {
  return SparkySPKParser::RuleOrnament_statement;
}


std::any SparkySPKParser::Ornament_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitOrnament_statement(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::Ornament_statementContext* SparkySPKParser::ornament_statement() {
  Ornament_statementContext *_localctx = _tracker.createInstance<Ornament_statementContext>(_ctx, getState());
  enterRule(_localctx, 30, SparkySPKParser::RuleOrnament_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(549);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 46, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(476);
      match(SparkySPKParser::RETURN_OR);
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(477);
      match(SparkySPKParser::Type_OR);
      setState(478);
      match(SparkySPKParser::Peak);
      setState(479);
      match(SparkySPKParser::RETURN_OR);
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(480);
      match(SparkySPKParser::Type_OR);
      setState(481);
      match(SparkySPKParser::Grid);
      setState(482);
      match(SparkySPKParser::RETURN_OR);
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(483);
      match(SparkySPKParser::Color_OR);
      setState(485); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(484);
        match(SparkySPKParser::Integer_OR);
        setState(487); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Integer_OR);
      setState(490); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(489);
        match(SparkySPKParser::Simple_name_OR);
        setState(492); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Simple_name_OR);
      setState(494);
      match(SparkySPKParser::RETURN_OR);
      break;
    }

    case 5: {
      enterOuterAlt(_localctx, 5);
      setState(495);
      match(SparkySPKParser::Flags_OR);
      setState(497); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(496);
        match(SparkySPKParser::Integer_OR);
        setState(499); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Integer_OR);
      setState(501);
      match(SparkySPKParser::RETURN_OR);
      break;
    }

    case 6: {
      enterOuterAlt(_localctx, 6);
      setState(502);
      match(SparkySPKParser::Id);
      setState(503);
      match(SparkySPKParser::Integer_OR);
      setState(504);
      match(SparkySPKParser::RETURN_OR);
      break;
    }

    case 7: {
      enterOuterAlt(_localctx, 7);
      setState(505);
      match(SparkySPKParser::Pos_OR);
      setState(507); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(506);
        ornament_position();
        setState(509); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Integer_OR

      || _la == SparkySPKParser::Float_OR);
      setState(511);
      match(SparkySPKParser::RETURN_OR);
      break;
    }

    case 8: {
      enterOuterAlt(_localctx, 8);
      setState(513);
      match(SparkySPKParser::Height);
      setState(515); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(514);
        match(SparkySPKParser::Float_OR);
        setState(517); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Float_OR);
      setState(519);
      match(SparkySPKParser::RETURN_OR);
      break;
    }

    case 9: {
      enterOuterAlt(_localctx, 9);
      setState(520);
      match(SparkySPKParser::Line_width);
      setState(522); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(521);
        match(SparkySPKParser::Float_OR);
        setState(524); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Float_OR);
      setState(527);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == SparkySPKParser::Simple_name_OR) {
        setState(526);
        match(SparkySPKParser::Simple_name_OR);
      }
      setState(529);
      match(SparkySPKParser::RETURN_OR);
      break;
    }

    case 10: {
      enterOuterAlt(_localctx, 10);
      setState(530);
      match(SparkySPKParser::Integral);
      setState(531);
      match(SparkySPKParser::Real_OR);
      setState(533);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == SparkySPKParser::Simple_name_OR) {
        setState(532);
        match(SparkySPKParser::Simple_name_OR);
      }
      setState(535);
      match(SparkySPKParser::RETURN_OR);
      break;
    }

    case 11: {
      enterOuterAlt(_localctx, 11);
      setState(536);
      match(SparkySPKParser::Fr);
      setState(537);
      match(SparkySPKParser::Float_OR);
      setState(538);
      match(SparkySPKParser::RETURN_OR);
      break;
    }

    case 12: {
      enterOuterAlt(_localctx, 12);
      setState(539);
      match(SparkySPKParser::Rs);
      setState(541); 
      _errHandler->sync(this);
      _la = _input->LA(1);
      do {
        setState(540);
        match(SparkySPKParser::Rs_ex);
        setState(543); 
        _errHandler->sync(this);
        _la = _input->LA(1);
      } while (_la == SparkySPKParser::Rs_ex);
      setState(545);
      match(SparkySPKParser::RETURN_OR);
      break;
    }

    case 13: {
      enterOuterAlt(_localctx, 13);
      setState(546);
      label();
      setState(547);
      match(SparkySPKParser::RETURN_OR);
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

//----------------- Ornament_positionContext ------------------------------------------------------------------

SparkySPKParser::Ornament_positionContext::Ornament_positionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::Ornament_positionContext::Integer_OR() {
  return getToken(SparkySPKParser::Integer_OR, 0);
}

tree::TerminalNode* SparkySPKParser::Ornament_positionContext::Float_OR() {
  return getToken(SparkySPKParser::Float_OR, 0);
}


size_t SparkySPKParser::Ornament_positionContext::getRuleIndex() const {
  return SparkySPKParser::RuleOrnament_position;
}


std::any SparkySPKParser::Ornament_positionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitOrnament_position(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::Ornament_positionContext* SparkySPKParser::ornament_position() {
  Ornament_positionContext *_localctx = _tracker.createInstance<Ornament_positionContext>(_ctx, getState());
  enterRule(_localctx, 32, SparkySPKParser::RuleOrnament_position);
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
    _la = _input->LA(1);
    if (!(_la == SparkySPKParser::Integer_OR

    || _la == SparkySPKParser::Float_OR)) {
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

//----------------- LabelContext ------------------------------------------------------------------

SparkySPKParser::LabelContext::LabelContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::LabelContext::L_brakt() {
  return getToken(SparkySPKParser::L_brakt, 0);
}

tree::TerminalNode* SparkySPKParser::LabelContext::R_brakt() {
  return getToken(SparkySPKParser::R_brakt, 0);
}

std::vector<SparkySPKParser::Label_statementContext *> SparkySPKParser::LabelContext::label_statement() {
  return getRuleContexts<SparkySPKParser::Label_statementContext>();
}

SparkySPKParser::Label_statementContext* SparkySPKParser::LabelContext::label_statement(size_t i) {
  return getRuleContext<SparkySPKParser::Label_statementContext>(i);
}


size_t SparkySPKParser::LabelContext::getRuleIndex() const {
  return SparkySPKParser::RuleLabel;
}


std::any SparkySPKParser::LabelContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitLabel(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::LabelContext* SparkySPKParser::label() {
  LabelContext *_localctx = _tracker.createInstance<LabelContext>(_ctx, getState());
  enterRule(_localctx, 34, SparkySPKParser::RuleLabel);
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
    setState(553);
    match(SparkySPKParser::L_brakt);
    setState(557);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((((_la - 136) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 136)) & 32895) != 0)) {
      setState(554);
      label_statement();
      setState(559);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(560);
    match(SparkySPKParser::R_brakt);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Label_statementContext ------------------------------------------------------------------

SparkySPKParser::Label_statementContext::Label_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::RETURN_LA() {
  return getToken(SparkySPKParser::RETURN_LA, 0);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Type_LA() {
  return getToken(SparkySPKParser::Type_LA, 0);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Label() {
  return getToken(SparkySPKParser::Label, 0);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Color_LA() {
  return getToken(SparkySPKParser::Color_LA, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Label_statementContext::Integer_LA() {
  return getTokens(SparkySPKParser::Integer_LA);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Integer_LA(size_t i) {
  return getToken(SparkySPKParser::Integer_LA, i);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Label_statementContext::Simple_name_LA() {
  return getTokens(SparkySPKParser::Simple_name_LA);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Simple_name_LA(size_t i) {
  return getToken(SparkySPKParser::Simple_name_LA, i);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Flags_LA() {
  return getToken(SparkySPKParser::Flags_LA, 0);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Mode_LA() {
  return getToken(SparkySPKParser::Mode_LA, 0);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Pos_LA() {
  return getToken(SparkySPKParser::Pos_LA, 0);
}

std::vector<SparkySPKParser::Label_positionContext *> SparkySPKParser::Label_statementContext::label_position() {
  return getRuleContexts<SparkySPKParser::Label_positionContext>();
}

SparkySPKParser::Label_positionContext* SparkySPKParser::Label_statementContext::label_position(size_t i) {
  return getRuleContext<SparkySPKParser::Label_positionContext>(i);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Assignment_2d_ex() {
  return getToken(SparkySPKParser::Assignment_2d_ex, 0);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Assignment_3d_ex() {
  return getToken(SparkySPKParser::Assignment_3d_ex, 0);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Assignment_4d_ex() {
  return getToken(SparkySPKParser::Assignment_4d_ex, 0);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Xy() {
  return getToken(SparkySPKParser::Xy, 0);
}

std::vector<tree::TerminalNode *> SparkySPKParser::Label_statementContext::Xy_pos() {
  return getTokens(SparkySPKParser::Xy_pos);
}

tree::TerminalNode* SparkySPKParser::Label_statementContext::Xy_pos(size_t i) {
  return getToken(SparkySPKParser::Xy_pos, i);
}


size_t SparkySPKParser::Label_statementContext::getRuleIndex() const {
  return SparkySPKParser::RuleLabel_statement;
}


std::any SparkySPKParser::Label_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitLabel_statement(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::Label_statementContext* SparkySPKParser::label_statement() {
  Label_statementContext *_localctx = _tracker.createInstance<Label_statementContext>(_ctx, getState());
  enterRule(_localctx, 36, SparkySPKParser::RuleLabel_statement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(606);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case SparkySPKParser::RETURN_LA: {
        enterOuterAlt(_localctx, 1);
        setState(562);
        match(SparkySPKParser::RETURN_LA);
        break;
      }

      case SparkySPKParser::Type_LA: {
        enterOuterAlt(_localctx, 2);
        setState(563);
        match(SparkySPKParser::Type_LA);
        setState(564);
        match(SparkySPKParser::Label);
        setState(565);
        match(SparkySPKParser::RETURN_LA);
        break;
      }

      case SparkySPKParser::Color_LA: {
        enterOuterAlt(_localctx, 3);
        setState(566);
        match(SparkySPKParser::Color_LA);
        setState(568); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(567);
          match(SparkySPKParser::Integer_LA);
          setState(570); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Integer_LA);
        setState(573); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(572);
          match(SparkySPKParser::Simple_name_LA);
          setState(575); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Simple_name_LA);
        setState(577);
        match(SparkySPKParser::RETURN_LA);
        break;
      }

      case SparkySPKParser::Flags_LA: {
        enterOuterAlt(_localctx, 4);
        setState(578);
        match(SparkySPKParser::Flags_LA);
        setState(580); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(579);
          match(SparkySPKParser::Integer_LA);
          setState(582); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Integer_LA);
        setState(584);
        match(SparkySPKParser::RETURN_LA);
        break;
      }

      case SparkySPKParser::Mode_LA: {
        enterOuterAlt(_localctx, 5);
        setState(585);
        match(SparkySPKParser::Mode_LA);
        setState(586);
        match(SparkySPKParser::Integer_LA);
        setState(587);
        match(SparkySPKParser::RETURN_LA);
        break;
      }

      case SparkySPKParser::Pos_LA: {
        enterOuterAlt(_localctx, 6);
        setState(588);
        match(SparkySPKParser::Pos_LA);
        setState(590); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(589);
          label_position();
          setState(592); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Integer_LA

        || _la == SparkySPKParser::Float_LA);
        setState(594);
        match(SparkySPKParser::RETURN_LA);
        break;
      }

      case SparkySPKParser::Label: {
        enterOuterAlt(_localctx, 7);
        setState(596);
        match(SparkySPKParser::Label);
        setState(597);
        _la = _input->LA(1);
        if (!(((((_la - 143) & ~ 0x3fULL) == 0) &&
          ((1ULL << (_la - 143)) & 7) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(598);
        match(SparkySPKParser::RETURN_LA);
        break;
      }

      case SparkySPKParser::Xy: {
        enterOuterAlt(_localctx, 8);
        setState(599);
        match(SparkySPKParser::Xy);
        setState(601); 
        _errHandler->sync(this);
        _la = _input->LA(1);
        do {
          setState(600);
          match(SparkySPKParser::Xy_pos);
          setState(603); 
          _errHandler->sync(this);
          _la = _input->LA(1);
        } while (_la == SparkySPKParser::Xy_pos);
        setState(605);
        match(SparkySPKParser::RETURN_LA);
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

//----------------- Label_positionContext ------------------------------------------------------------------

SparkySPKParser::Label_positionContext::Label_positionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkySPKParser::Label_positionContext::Integer_LA() {
  return getToken(SparkySPKParser::Integer_LA, 0);
}

tree::TerminalNode* SparkySPKParser::Label_positionContext::Float_LA() {
  return getToken(SparkySPKParser::Float_LA, 0);
}


size_t SparkySPKParser::Label_positionContext::getRuleIndex() const {
  return SparkySPKParser::RuleLabel_position;
}


std::any SparkySPKParser::Label_positionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkySPKParserVisitor*>(visitor))
    return parserVisitor->visitLabel_position(this);
  else
    return visitor->visitChildren(this);
}

SparkySPKParser::Label_positionContext* SparkySPKParser::label_position() {
  Label_positionContext *_localctx = _tracker.createInstance<Label_positionContext>(_ctx, getState());
  enterRule(_localctx, 38, SparkySPKParser::RuleLabel_position);
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
    setState(608);
    _la = _input->LA(1);
    if (!(_la == SparkySPKParser::Integer_LA

    || _la == SparkySPKParser::Float_LA)) {
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

void SparkySPKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  sparkyspkparserParserInitialize();
#else
  ::antlr4::internal::call_once(sparkyspkparserParserOnceFlag, sparkyspkparserParserInitialize);
#endif
}
