
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkySPKLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  SparkySPKLexer : public antlr4::Lexer {
public:
  enum {
    Sparky_save_file = 1, Version = 2, User = 3, Spectrum = 4, Integer = 5, 
    Float = 6, Real = 7, Simple_name = 8, SPACE = 9, End_user = 10, Set = 11, 
    Mode_US = 12, Save_prompt = 13, Save_interval = 14, Resize_views = 15, 
    Key_timeout = 16, Cache_size = 17, Contour_graying = 18, Default = 19, 
    Print = 20, Command = 21, File = 22, Options = 23, Integer_US = 24, 
    Float_US = 25, Simple_name_US = 26, SPACE_US = 27, RETURN_US = 28, Attached_data = 29, 
    View = 30, Ornament = 31, End_spectrum = 32, Name_SP = 33, Path_name = 34, 
    Dimension = 35, Shift = 36, Points = 37, Extra_peak_planes = 38, Assign_multi_axis_guess = 39, 
    Assign_guess_threshhold = 40, Assign_relation = 41, Assign_range = 42, 
    Assign_format = 43, List_tool = 44, Sort_by = 45, Name_type = 46, Sort_axis = 47, 
    Show_flags = 48, Integrate_overlapped_sep = 49, Integrate_methods = 50, 
    Integrate_allow_motion = 51, Integrate_adjust_linewidths = 52, Integrate_motion_range = 53, 
    Integrate_min_linewidth = 54, Integrate_max_linewidth = 55, Integrate_fit_baseline = 56, 
    Integrate_subtract_peaks = 57, Integrate_contoured_data = 58, Integrate_rectangle_data = 59, 
    Integrate_max_iterations = 60, Integrate_tolerance = 61, Peak_pick = 62, 
    Peak_pick_minimum_linewidth = 63, Peak_pick_minimum_dropoff = 64, Noise_sigma = 65, 
    Ornament_labe_size = 66, Ornament_line_size = 67, Ornament_peak_size = 68, 
    Ornament_grid_size = 69, Ornament_peak_group_size = 70, Ornament_select_size = 71, 
    Ornament_pointer_size = 72, Ornament_line_end_size = 73, Format_ex = 74, 
    Integer_SP = 75, Float_SP = 76, Simple_name_SP = 77, Any_name_SP = 78, 
    SPACE_SP = 79, RETURN_SP = 80, End_attached_data = 81, Any_name_AD = 82, 
    SPACE_AD = 83, Params = 84, End_view = 85, Name_VI = 86, Precision = 87, 
    Precision_by_units = 88, View_mode = 89, Show = 90, Axis_type = 91, 
    Flags_VI = 92, Contour_pos = 93, Contour_neg = 94, Integer_VI = 95, 
    Float_VI = 96, Real_VI = 97, Simple_name_VI = 98, SPACE_VI = 99, RETURN_VI = 100, 
    End_params = 101, Orientation = 102, Location = 103, Size = 104, Offset = 105, 
    Scale = 106, Zoom = 107, Flags_PA = 108, Integer_PA = 109, Float_PA = 110, 
    Simple_name_PA = 111, SPACE_PA = 112, RETURN_PA = 113, L_brakt = 114, 
    End_ornament = 115, Type_OR = 116, Peak = 117, Grid = 118, Color_OR = 119, 
    Flags_OR = 120, Id = 121, Pos_OR = 122, Height = 123, Line_width = 124, 
    Integral = 125, Fr = 126, Rs = 127, Rs_ex = 128, Integer_OR = 129, Float_OR = 130, 
    Real_OR = 131, Simple_name_OR = 132, SPACE_OR = 133, RETURN_OR = 134, 
    R_brakt = 135, Type_LA = 136, Label = 137, Color_LA = 138, Flags_LA = 139, 
    Mode_LA = 140, Pos_LA = 141, Xy = 142, Assignment_2d_ex = 143, Assignment_3d_ex = 144, 
    Assignment_4d_ex = 145, Xy_pos = 146, Integer_LA = 147, Float_LA = 148, 
    Simple_name_LA = 149, SPACE_LA = 150, RETURN_LA = 151
  };

  enum {
    USER_MODE = 1, SPECTRUM_MODE = 2, ATTACHED_DATA_MODE = 3, VIEW_MODE = 4, 
    PARAMS_MODE = 5, ORNAMENT_MODE = 6, LABEL_MODE = 7
  };

  explicit SparkySPKLexer(antlr4::CharStream *input);

  ~SparkySPKLexer() override;


  std::string getGrammarFileName() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const std::vector<std::string>& getChannelNames() const override;

  const std::vector<std::string>& getModeNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;

  const antlr4::atn::ATN& getATN() const override;

  // By default the static state used to implement the lexer is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:

  // Individual action functions triggered by action() above.

  // Individual semantic predicate functions triggered by sempred() above.

};

