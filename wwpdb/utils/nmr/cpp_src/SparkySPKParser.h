
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkySPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  SparkySPKParser : public antlr4::Parser {
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
    RuleSparky_spk = 0, RuleUser_block = 1, RuleUser_statement = 2, RuleSpectrum_block = 3, 
    RuleSpectrum_statement = 4, RuleSpectrum_name = 5, RuleAttached_data = 6, 
    RuleAttached_data_statement = 7, RuleView = 8, RuleView_statement = 9, 
    RuleView_name = 10, RuleView_number = 11, RuleParams = 12, RuleParams_statement = 13, 
    RuleOrnament = 14, RuleOrnament_statement = 15, RuleOrnament_position = 16, 
    RuleLabel = 17, RuleLabel_statement = 18, RuleLabel_position = 19
  };

  explicit SparkySPKParser(antlr4::TokenStream *input);

  SparkySPKParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~SparkySPKParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Sparky_spkContext;
  class User_blockContext;
  class User_statementContext;
  class Spectrum_blockContext;
  class Spectrum_statementContext;
  class Spectrum_nameContext;
  class Attached_dataContext;
  class Attached_data_statementContext;
  class ViewContext;
  class View_statementContext;
  class View_nameContext;
  class View_numberContext;
  class ParamsContext;
  class Params_statementContext;
  class OrnamentContext;
  class Ornament_statementContext;
  class Ornament_positionContext;
  class LabelContext;
  class Label_statementContext;
  class Label_positionContext; 

  class  Sparky_spkContext : public antlr4::ParserRuleContext {
  public:
    Sparky_spkContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Sparky_save_file();
    antlr4::tree::TerminalNode* Sparky_save_file(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Version();
    antlr4::tree::TerminalNode* Version(size_t i);
    std::vector<User_blockContext *> user_block();
    User_blockContext* user_block(size_t i);
    std::vector<Spectrum_blockContext *> spectrum_block();
    Spectrum_blockContext* spectrum_block(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Sparky_spkContext* sparky_spk();

  class  User_blockContext : public antlr4::ParserRuleContext {
  public:
    User_blockContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *User();
    antlr4::tree::TerminalNode *End_user();
    std::vector<User_statementContext *> user_statement();
    User_statementContext* user_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  User_blockContext* user_block();

  class  User_statementContext : public antlr4::ParserRuleContext {
  public:
    User_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN_US();
    antlr4::tree::TerminalNode *Set();
    antlr4::tree::TerminalNode *Mode_US();
    std::vector<antlr4::tree::TerminalNode *> Integer_US();
    antlr4::tree::TerminalNode* Integer_US(size_t i);
    antlr4::tree::TerminalNode *Save_prompt();
    antlr4::tree::TerminalNode *Save_interval();
    antlr4::tree::TerminalNode *Resize_views();
    antlr4::tree::TerminalNode *Key_timeout();
    antlr4::tree::TerminalNode *Cache_size();
    antlr4::tree::TerminalNode *Contour_graying();
    antlr4::tree::TerminalNode *Default();
    std::vector<antlr4::tree::TerminalNode *> Print();
    antlr4::tree::TerminalNode* Print(size_t i);
    antlr4::tree::TerminalNode *Command();
    antlr4::tree::TerminalNode *Simple_name_US();
    antlr4::tree::TerminalNode *File();
    antlr4::tree::TerminalNode *Options();
    std::vector<antlr4::tree::TerminalNode *> Float_US();
    antlr4::tree::TerminalNode* Float_US(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  User_statementContext* user_statement();

  class  Spectrum_blockContext : public antlr4::ParserRuleContext {
  public:
    Spectrum_blockContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Spectrum();
    antlr4::tree::TerminalNode *End_spectrum();
    std::vector<Spectrum_statementContext *> spectrum_statement();
    Spectrum_statementContext* spectrum_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Spectrum_blockContext* spectrum_block();

  class  Spectrum_statementContext : public antlr4::ParserRuleContext {
  public:
    Spectrum_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN_SP();
    antlr4::tree::TerminalNode *Name_SP();
    std::vector<Spectrum_nameContext *> spectrum_name();
    Spectrum_nameContext* spectrum_name(size_t i);
    antlr4::tree::TerminalNode *Path_name();
    antlr4::tree::TerminalNode *Dimension();
    std::vector<antlr4::tree::TerminalNode *> Integer_SP();
    antlr4::tree::TerminalNode* Integer_SP(size_t i);
    antlr4::tree::TerminalNode *Shift();
    std::vector<antlr4::tree::TerminalNode *> Float_SP();
    antlr4::tree::TerminalNode* Float_SP(size_t i);
    antlr4::tree::TerminalNode *Points();
    antlr4::tree::TerminalNode *Extra_peak_planes();
    antlr4::tree::TerminalNode *Assign_multi_axis_guess();
    antlr4::tree::TerminalNode *Assign_guess_threshhold();
    antlr4::tree::TerminalNode *Assign_relation();
    antlr4::tree::TerminalNode *Assign_range();
    antlr4::tree::TerminalNode *Assign_format();
    antlr4::tree::TerminalNode *Format_ex();
    antlr4::tree::TerminalNode *List_tool();
    antlr4::tree::TerminalNode *Sort_by();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_SP();
    antlr4::tree::TerminalNode* Simple_name_SP(size_t i);
    antlr4::tree::TerminalNode *Name_type();
    antlr4::tree::TerminalNode *Sort_axis();
    antlr4::tree::TerminalNode *Show_flags();
    antlr4::tree::TerminalNode *Integrate_overlapped_sep();
    antlr4::tree::TerminalNode *Integrate_methods();
    antlr4::tree::TerminalNode *Integrate_allow_motion();
    antlr4::tree::TerminalNode *Integrate_adjust_linewidths();
    antlr4::tree::TerminalNode *Integrate_motion_range();
    antlr4::tree::TerminalNode *Integrate_min_linewidth();
    antlr4::tree::TerminalNode *Integrate_max_linewidth();
    antlr4::tree::TerminalNode *Integrate_fit_baseline();
    antlr4::tree::TerminalNode *Integrate_subtract_peaks();
    antlr4::tree::TerminalNode *Integrate_contoured_data();
    antlr4::tree::TerminalNode *Integrate_rectangle_data();
    antlr4::tree::TerminalNode *Integrate_max_iterations();
    antlr4::tree::TerminalNode *Integrate_tolerance();
    antlr4::tree::TerminalNode *Peak_pick();
    antlr4::tree::TerminalNode *Peak_pick_minimum_linewidth();
    antlr4::tree::TerminalNode *Peak_pick_minimum_dropoff();
    antlr4::tree::TerminalNode *Noise_sigma();
    antlr4::tree::TerminalNode *Ornament_labe_size();
    antlr4::tree::TerminalNode *Ornament_line_size();
    antlr4::tree::TerminalNode *Ornament_peak_size();
    antlr4::tree::TerminalNode *Ornament_grid_size();
    antlr4::tree::TerminalNode *Ornament_peak_group_size();
    antlr4::tree::TerminalNode *Ornament_select_size();
    antlr4::tree::TerminalNode *Ornament_pointer_size();
    antlr4::tree::TerminalNode *Ornament_line_end_size();
    Attached_dataContext *attached_data();
    ViewContext *view();
    OrnamentContext *ornament();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Spectrum_statementContext* spectrum_statement();

  class  Spectrum_nameContext : public antlr4::ParserRuleContext {
  public:
    Spectrum_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer_SP();
    antlr4::tree::TerminalNode *Float_SP();
    antlr4::tree::TerminalNode *Simple_name_SP();
    antlr4::tree::TerminalNode *Any_name_SP();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Spectrum_nameContext* spectrum_name();

  class  Attached_dataContext : public antlr4::ParserRuleContext {
  public:
    Attached_dataContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Attached_data();
    antlr4::tree::TerminalNode *End_attached_data();
    std::vector<Attached_data_statementContext *> attached_data_statement();
    Attached_data_statementContext* attached_data_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Attached_dataContext* attached_data();

  class  Attached_data_statementContext : public antlr4::ParserRuleContext {
  public:
    Attached_data_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Any_name_AD();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Attached_data_statementContext* attached_data_statement();

  class  ViewContext : public antlr4::ParserRuleContext {
  public:
    ViewContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *View();
    antlr4::tree::TerminalNode *End_view();
    std::vector<View_statementContext *> view_statement();
    View_statementContext* view_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ViewContext* view();

  class  View_statementContext : public antlr4::ParserRuleContext {
  public:
    View_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN_VI();
    antlr4::tree::TerminalNode *Name_VI();
    std::vector<View_nameContext *> view_name();
    View_nameContext* view_name(size_t i);
    antlr4::tree::TerminalNode *Precision();
    std::vector<antlr4::tree::TerminalNode *> Integer_VI();
    antlr4::tree::TerminalNode* Integer_VI(size_t i);
    antlr4::tree::TerminalNode *Precision_by_units();
    antlr4::tree::TerminalNode *View_mode();
    antlr4::tree::TerminalNode *Show();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_VI();
    antlr4::tree::TerminalNode* Simple_name_VI(size_t i);
    antlr4::tree::TerminalNode *Axis_type();
    antlr4::tree::TerminalNode *Flags_VI();
    antlr4::tree::TerminalNode *Contour_pos();
    View_numberContext *view_number();
    std::vector<antlr4::tree::TerminalNode *> Float_VI();
    antlr4::tree::TerminalNode* Float_VI(size_t i);
    antlr4::tree::TerminalNode *Contour_neg();
    ParamsContext *params();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  View_statementContext* view_statement();

  class  View_nameContext : public antlr4::ParserRuleContext {
  public:
    View_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer_VI();
    antlr4::tree::TerminalNode *Float_VI();
    antlr4::tree::TerminalNode *Real_VI();
    antlr4::tree::TerminalNode *Simple_name_VI();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  View_nameContext* view_name();

  class  View_numberContext : public antlr4::ParserRuleContext {
  public:
    View_numberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer_VI();
    antlr4::tree::TerminalNode *Float_VI();
    antlr4::tree::TerminalNode *Real_VI();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  View_numberContext* view_number();

  class  ParamsContext : public antlr4::ParserRuleContext {
  public:
    ParamsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Params();
    antlr4::tree::TerminalNode *End_params();
    std::vector<Params_statementContext *> params_statement();
    Params_statementContext* params_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ParamsContext* params();

  class  Params_statementContext : public antlr4::ParserRuleContext {
  public:
    Params_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN_PA();
    antlr4::tree::TerminalNode *Orientation();
    std::vector<antlr4::tree::TerminalNode *> Integer_PA();
    antlr4::tree::TerminalNode* Integer_PA(size_t i);
    antlr4::tree::TerminalNode *Location();
    antlr4::tree::TerminalNode *Size();
    antlr4::tree::TerminalNode *Offset();
    std::vector<antlr4::tree::TerminalNode *> Float_PA();
    antlr4::tree::TerminalNode* Float_PA(size_t i);
    antlr4::tree::TerminalNode *Scale();
    antlr4::tree::TerminalNode *Zoom();
    antlr4::tree::TerminalNode *Flags_PA();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Params_statementContext* params_statement();

  class  OrnamentContext : public antlr4::ParserRuleContext {
  public:
    OrnamentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Ornament();
    antlr4::tree::TerminalNode *End_ornament();
    std::vector<Ornament_statementContext *> ornament_statement();
    Ornament_statementContext* ornament_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  OrnamentContext* ornament();

  class  Ornament_statementContext : public antlr4::ParserRuleContext {
  public:
    Ornament_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN_OR();
    antlr4::tree::TerminalNode *Type_OR();
    antlr4::tree::TerminalNode *Peak();
    antlr4::tree::TerminalNode *Grid();
    antlr4::tree::TerminalNode *Color_OR();
    std::vector<antlr4::tree::TerminalNode *> Integer_OR();
    antlr4::tree::TerminalNode* Integer_OR(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_OR();
    antlr4::tree::TerminalNode* Simple_name_OR(size_t i);
    antlr4::tree::TerminalNode *Flags_OR();
    antlr4::tree::TerminalNode *Id();
    antlr4::tree::TerminalNode *Pos_OR();
    std::vector<Ornament_positionContext *> ornament_position();
    Ornament_positionContext* ornament_position(size_t i);
    antlr4::tree::TerminalNode *Height();
    std::vector<antlr4::tree::TerminalNode *> Float_OR();
    antlr4::tree::TerminalNode* Float_OR(size_t i);
    antlr4::tree::TerminalNode *Line_width();
    antlr4::tree::TerminalNode *Integral();
    antlr4::tree::TerminalNode *Real_OR();
    antlr4::tree::TerminalNode *Fr();
    antlr4::tree::TerminalNode *Rs();
    std::vector<antlr4::tree::TerminalNode *> Rs_ex();
    antlr4::tree::TerminalNode* Rs_ex(size_t i);
    LabelContext *label();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ornament_statementContext* ornament_statement();

  class  Ornament_positionContext : public antlr4::ParserRuleContext {
  public:
    Ornament_positionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer_OR();
    antlr4::tree::TerminalNode *Float_OR();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ornament_positionContext* ornament_position();

  class  LabelContext : public antlr4::ParserRuleContext {
  public:
    LabelContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brakt();
    antlr4::tree::TerminalNode *R_brakt();
    std::vector<Label_statementContext *> label_statement();
    Label_statementContext* label_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  LabelContext* label();

  class  Label_statementContext : public antlr4::ParserRuleContext {
  public:
    Label_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN_LA();
    antlr4::tree::TerminalNode *Type_LA();
    antlr4::tree::TerminalNode *Label();
    antlr4::tree::TerminalNode *Color_LA();
    std::vector<antlr4::tree::TerminalNode *> Integer_LA();
    antlr4::tree::TerminalNode* Integer_LA(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LA();
    antlr4::tree::TerminalNode* Simple_name_LA(size_t i);
    antlr4::tree::TerminalNode *Flags_LA();
    antlr4::tree::TerminalNode *Mode_LA();
    antlr4::tree::TerminalNode *Pos_LA();
    std::vector<Label_positionContext *> label_position();
    Label_positionContext* label_position(size_t i);
    antlr4::tree::TerminalNode *Assignment_2d_ex();
    antlr4::tree::TerminalNode *Assignment_3d_ex();
    antlr4::tree::TerminalNode *Assignment_4d_ex();
    antlr4::tree::TerminalNode *Xy();
    std::vector<antlr4::tree::TerminalNode *> Xy_pos();
    antlr4::tree::TerminalNode* Xy_pos(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Label_statementContext* label_statement();

  class  Label_positionContext : public antlr4::ParserRuleContext {
  public:
    Label_positionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer_LA();
    antlr4::tree::TerminalNode *Float_LA();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Label_positionContext* label_position();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

