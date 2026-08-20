
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrPipePKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  NmrPipePKParser : public antlr4::Parser {
public:
  enum {
    Data = 1, Vars = 2, Format = 3, Null_value = 4, Null_string = 5, L_paren = 6, 
    Integer = 7, Float = 8, Real = 9, SHARP_COMMENT = 10, EXCLM_COMMENT = 11, 
    Any_name = 12, SPACE = 13, RETURN = 14, SECTION_COMMENT = 15, LINE_COMMENT = 16, 
    X_axis_DA = 17, Y_axis_DA = 18, Z_axis_DA = 19, A_axis_DA = 20, Ppm_value_DA = 21, 
    Dim_count_DA = 22, Ppm_DA = 23, Hz_DA = 24, Integer_DA = 25, Float_DA = 26, 
    Real_DA = 27, Simple_name_DA = 28, SPACE_DA = 29, RETURN_DA = 30, LINE_COMMENT_DA = 31, 
    Index = 32, X_axis = 33, Y_axis = 34, Z_axis = 35, A_axis = 36, Dx = 37, 
    Dy = 38, Dz = 39, Da = 40, X_ppm = 41, Y_ppm = 42, Z_ppm = 43, A_ppm = 44, 
    X_hz = 45, Y_hz = 46, Z_hz = 47, A_hz = 48, Xw = 49, Yw = 50, Zw = 51, 
    Aw = 52, Xw_hz = 53, Yw_hz = 54, Zw_hz = 55, Aw_hz = 56, X1 = 57, X3 = 58, 
    Y1 = 59, Y3 = 60, Z1 = 61, Z3 = 62, A1 = 63, A3 = 64, Height = 65, DHeight = 66, 
    Vol = 67, Pchi2 = 68, Type = 69, Ass = 70, ClustId = 71, Memcnt = 72, 
    Trouble = 73, PkID = 74, Sl_Z = 75, Sl_A = 76, X = 77, Y = 78, Z = 79, 
    A = 80, Intensity = 81, Assign = 82, Assign1 = 83, Assign2 = 84, Integer_VA = 85, 
    Float_VA = 86, Real_VA = 87, Simple_name_VA = 88, SPACE_VA = 89, RETURN_VA = 90, 
    LINE_COMMENT_VA = 91, Format_code = 92, SPACE_FO = 93, RETURN_FO = 94, 
    LINE_COMMENT_FO = 95, Any_name_NV = 96, SPACE_NV = 97, RETURN_NV = 98, 
    Any_name_NS = 99, SPACE_NS = 100, RETURN_NS = 101, R_paren = 102, L_brkt = 103, 
    R_brkt = 104, Comma = 105, Semicolon = 106, Number_sign = 107, Percent_sign = 108, 
    Caret = 109, Integer_PR = 110, Float_PR = 111, Real_PR = 112, Assignments_PR = 113, 
    SPACE_PR = 114, RETURN_PR = 115
  };

  enum {
    RuleNmrpipe_pk = 0, RuleData_label = 1, RulePeak_list_2d = 2, RulePeak_2d = 3, 
    RulePeak_list_3d = 4, RulePeak_3d = 5, RulePeak_list_4d = 6, RulePeak_4d = 7, 
    RulePipp_label = 8, RulePipp_axis = 9, RulePipp_peak_list_2d = 10, RulePipp_peak_2d = 11, 
    RulePipp_peak_list_3d = 12, RulePipp_peak_3d = 13, RulePipp_peak_list_4d = 14, 
    RulePipp_peak_4d = 15, RulePipp_row_peak_list_2d = 16, RulePipp_row_peak_2d = 17, 
    RulePipp_row_peak_list_3d = 18, RulePipp_row_peak_3d = 19, RulePipp_row_peak_list_4d = 20, 
    RulePipp_row_peak_4d = 21, RuleNumber = 22
  };

  explicit NmrPipePKParser(antlr4::TokenStream *input);

  NmrPipePKParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~NmrPipePKParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Nmrpipe_pkContext;
  class Data_labelContext;
  class Peak_list_2dContext;
  class Peak_2dContext;
  class Peak_list_3dContext;
  class Peak_3dContext;
  class Peak_list_4dContext;
  class Peak_4dContext;
  class Pipp_labelContext;
  class Pipp_axisContext;
  class Pipp_peak_list_2dContext;
  class Pipp_peak_2dContext;
  class Pipp_peak_list_3dContext;
  class Pipp_peak_3dContext;
  class Pipp_peak_list_4dContext;
  class Pipp_peak_4dContext;
  class Pipp_row_peak_list_2dContext;
  class Pipp_row_peak_2dContext;
  class Pipp_row_peak_list_3dContext;
  class Pipp_row_peak_3dContext;
  class Pipp_row_peak_list_4dContext;
  class Pipp_row_peak_4dContext;
  class NumberContext; 

  class  Nmrpipe_pkContext : public antlr4::ParserRuleContext {
  public:
    Nmrpipe_pkContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Data_labelContext *> data_label();
    Data_labelContext* data_label(size_t i);
    std::vector<Peak_list_2dContext *> peak_list_2d();
    Peak_list_2dContext* peak_list_2d(size_t i);
    std::vector<Peak_list_3dContext *> peak_list_3d();
    Peak_list_3dContext* peak_list_3d(size_t i);
    std::vector<Peak_list_4dContext *> peak_list_4d();
    Peak_list_4dContext* peak_list_4d(size_t i);
    std::vector<Pipp_labelContext *> pipp_label();
    Pipp_labelContext* pipp_label(size_t i);
    std::vector<Pipp_peak_list_2dContext *> pipp_peak_list_2d();
    Pipp_peak_list_2dContext* pipp_peak_list_2d(size_t i);
    std::vector<Pipp_peak_list_3dContext *> pipp_peak_list_3d();
    Pipp_peak_list_3dContext* pipp_peak_list_3d(size_t i);
    std::vector<Pipp_peak_list_4dContext *> pipp_peak_list_4d();
    Pipp_peak_list_4dContext* pipp_peak_list_4d(size_t i);
    std::vector<Pipp_row_peak_list_2dContext *> pipp_row_peak_list_2d();
    Pipp_row_peak_list_2dContext* pipp_row_peak_list_2d(size_t i);
    std::vector<Pipp_row_peak_list_3dContext *> pipp_row_peak_list_3d();
    Pipp_row_peak_list_3dContext* pipp_row_peak_list_3d(size_t i);
    std::vector<Pipp_row_peak_list_4dContext *> pipp_row_peak_list_4d();
    Pipp_row_peak_list_4dContext* pipp_row_peak_list_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Nmrpipe_pkContext* nmrpipe_pk();

  class  Data_labelContext : public antlr4::ParserRuleContext {
  public:
    Data_labelContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Data();
    antlr4::tree::TerminalNode *Simple_name_DA();
    std::vector<antlr4::tree::TerminalNode *> Integer_DA();
    antlr4::tree::TerminalNode* Integer_DA(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Ppm_value_DA();
    antlr4::tree::TerminalNode* Ppm_value_DA(size_t i);
    antlr4::tree::TerminalNode *RETURN_DA();
    antlr4::tree::TerminalNode *X_axis_DA();
    antlr4::tree::TerminalNode *Y_axis_DA();
    antlr4::tree::TerminalNode *Z_axis_DA();
    antlr4::tree::TerminalNode *A_axis_DA();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Data_labelContext* data_label();

  class  Peak_list_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *X_axis();
    antlr4::tree::TerminalNode *Y_axis();
    antlr4::tree::TerminalNode *Dx();
    antlr4::tree::TerminalNode *Dy();
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *X_hz();
    antlr4::tree::TerminalNode *Y_hz();
    antlr4::tree::TerminalNode *Xw();
    antlr4::tree::TerminalNode *Yw();
    antlr4::tree::TerminalNode *Xw_hz();
    antlr4::tree::TerminalNode *Yw_hz();
    antlr4::tree::TerminalNode *X1();
    antlr4::tree::TerminalNode *X3();
    antlr4::tree::TerminalNode *Y1();
    antlr4::tree::TerminalNode *Y3();
    antlr4::tree::TerminalNode *Height();
    antlr4::tree::TerminalNode *DHeight();
    antlr4::tree::TerminalNode *Vol();
    antlr4::tree::TerminalNode *Pchi2();
    antlr4::tree::TerminalNode *Type();
    antlr4::tree::TerminalNode *ClustId();
    antlr4::tree::TerminalNode *Memcnt();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Ass();
    antlr4::tree::TerminalNode *Trouble();
    antlr4::tree::TerminalNode *Null_value();
    antlr4::tree::TerminalNode *Any_name_NV();
    antlr4::tree::TerminalNode *RETURN_NV();
    antlr4::tree::TerminalNode *Null_string();
    antlr4::tree::TerminalNode *Any_name_NS();
    antlr4::tree::TerminalNode *RETURN_NS();
    std::vector<Peak_2dContext *> peak_2d();
    Peak_2dContext* peak_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_2dContext* peak_list_2d();

  class  Peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    antlr4::tree::TerminalNode *Any_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_2dContext* peak_2d();

  class  Peak_list_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *X_axis();
    antlr4::tree::TerminalNode *Y_axis();
    antlr4::tree::TerminalNode *Z_axis();
    antlr4::tree::TerminalNode *Dx();
    antlr4::tree::TerminalNode *Dy();
    antlr4::tree::TerminalNode *Dz();
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *Z_ppm();
    antlr4::tree::TerminalNode *X_hz();
    antlr4::tree::TerminalNode *Y_hz();
    antlr4::tree::TerminalNode *Z_hz();
    antlr4::tree::TerminalNode *Xw();
    antlr4::tree::TerminalNode *Yw();
    antlr4::tree::TerminalNode *Zw();
    antlr4::tree::TerminalNode *Xw_hz();
    antlr4::tree::TerminalNode *Yw_hz();
    antlr4::tree::TerminalNode *Zw_hz();
    antlr4::tree::TerminalNode *X1();
    antlr4::tree::TerminalNode *X3();
    antlr4::tree::TerminalNode *Y1();
    antlr4::tree::TerminalNode *Y3();
    antlr4::tree::TerminalNode *Z1();
    antlr4::tree::TerminalNode *Z3();
    antlr4::tree::TerminalNode *Height();
    antlr4::tree::TerminalNode *DHeight();
    antlr4::tree::TerminalNode *Vol();
    antlr4::tree::TerminalNode *Pchi2();
    antlr4::tree::TerminalNode *Type();
    antlr4::tree::TerminalNode *ClustId();
    antlr4::tree::TerminalNode *Memcnt();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Ass();
    antlr4::tree::TerminalNode *Trouble();
    antlr4::tree::TerminalNode *Null_value();
    antlr4::tree::TerminalNode *Any_name_NV();
    antlr4::tree::TerminalNode *RETURN_NV();
    antlr4::tree::TerminalNode *Null_string();
    antlr4::tree::TerminalNode *Any_name_NS();
    antlr4::tree::TerminalNode *RETURN_NS();
    std::vector<Peak_3dContext *> peak_3d();
    Peak_3dContext* peak_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_3dContext* peak_list_3d();

  class  Peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    antlr4::tree::TerminalNode *Any_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_3dContext* peak_3d();

  class  Peak_list_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *X_axis();
    antlr4::tree::TerminalNode *Y_axis();
    antlr4::tree::TerminalNode *Z_axis();
    antlr4::tree::TerminalNode *A_axis();
    antlr4::tree::TerminalNode *Dx();
    antlr4::tree::TerminalNode *Dy();
    std::vector<antlr4::tree::TerminalNode *> Dz();
    antlr4::tree::TerminalNode* Dz(size_t i);
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *Z_ppm();
    antlr4::tree::TerminalNode *A_ppm();
    antlr4::tree::TerminalNode *X_hz();
    antlr4::tree::TerminalNode *Y_hz();
    antlr4::tree::TerminalNode *Z_hz();
    antlr4::tree::TerminalNode *A_hz();
    antlr4::tree::TerminalNode *Xw();
    antlr4::tree::TerminalNode *Yw();
    antlr4::tree::TerminalNode *Zw();
    antlr4::tree::TerminalNode *Aw();
    antlr4::tree::TerminalNode *Xw_hz();
    antlr4::tree::TerminalNode *Yw_hz();
    antlr4::tree::TerminalNode *Zw_hz();
    antlr4::tree::TerminalNode *Aw_hz();
    antlr4::tree::TerminalNode *X1();
    antlr4::tree::TerminalNode *X3();
    antlr4::tree::TerminalNode *Y1();
    antlr4::tree::TerminalNode *Y3();
    antlr4::tree::TerminalNode *Z1();
    antlr4::tree::TerminalNode *Z3();
    antlr4::tree::TerminalNode *A1();
    antlr4::tree::TerminalNode *A3();
    antlr4::tree::TerminalNode *Height();
    antlr4::tree::TerminalNode *DHeight();
    antlr4::tree::TerminalNode *Vol();
    antlr4::tree::TerminalNode *Pchi2();
    antlr4::tree::TerminalNode *Type();
    antlr4::tree::TerminalNode *ClustId();
    antlr4::tree::TerminalNode *Memcnt();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Ass();
    antlr4::tree::TerminalNode *Trouble();
    antlr4::tree::TerminalNode *Null_value();
    antlr4::tree::TerminalNode *Any_name_NV();
    antlr4::tree::TerminalNode *RETURN_NV();
    antlr4::tree::TerminalNode *Null_string();
    antlr4::tree::TerminalNode *Any_name_NS();
    antlr4::tree::TerminalNode *RETURN_NS();
    std::vector<Peak_4dContext *> peak_4d();
    Peak_4dContext* peak_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_4dContext* peak_list_4d();

  class  Peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    antlr4::tree::TerminalNode *Any_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_4dContext* peak_4d();

  class  Pipp_labelContext : public antlr4::ParserRuleContext {
  public:
    Pipp_labelContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Data();
    antlr4::tree::TerminalNode *Dim_count_DA();
    antlr4::tree::TerminalNode *Integer_DA();
    antlr4::tree::TerminalNode *RETURN_DA();
    std::vector<Pipp_axisContext *> pipp_axis();
    Pipp_axisContext* pipp_axis(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_labelContext* pipp_label();

  class  Pipp_axisContext : public antlr4::ParserRuleContext {
  public:
    Pipp_axisContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Data();
    antlr4::tree::TerminalNode *Integer_DA();
    std::vector<antlr4::tree::TerminalNode *> Float_DA();
    antlr4::tree::TerminalNode* Float_DA(size_t i);
    antlr4::tree::TerminalNode *RETURN_DA();
    antlr4::tree::TerminalNode *X_axis_DA();
    antlr4::tree::TerminalNode *Y_axis_DA();
    antlr4::tree::TerminalNode *Z_axis_DA();
    antlr4::tree::TerminalNode *A_axis_DA();
    antlr4::tree::TerminalNode *Ppm_DA();
    antlr4::tree::TerminalNode *Hz_DA();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_axisContext* pipp_axis();

  class  Pipp_peak_list_2dContext : public antlr4::ParserRuleContext {
  public:
    Pipp_peak_list_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *PkID();
    antlr4::tree::TerminalNode *X();
    antlr4::tree::TerminalNode *Y();
    antlr4::tree::TerminalNode *Intensity();
    antlr4::tree::TerminalNode *RETURN_VA();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *Assign();
    antlr4::tree::TerminalNode *Assign1();
    antlr4::tree::TerminalNode *Assign2();
    std::vector<Pipp_peak_2dContext *> pipp_peak_2d();
    Pipp_peak_2dContext* pipp_peak_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_peak_list_2dContext* pipp_peak_list_2d();

  class  Pipp_peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Pipp_peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_peak_2dContext* pipp_peak_2d();

  class  Pipp_peak_list_3dContext : public antlr4::ParserRuleContext {
  public:
    Pipp_peak_list_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *PkID();
    antlr4::tree::TerminalNode *X();
    antlr4::tree::TerminalNode *Y();
    antlr4::tree::TerminalNode *Z();
    antlr4::tree::TerminalNode *Intensity();
    antlr4::tree::TerminalNode *RETURN_VA();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *Sl_Z();
    antlr4::tree::TerminalNode *Assign();
    antlr4::tree::TerminalNode *Assign1();
    antlr4::tree::TerminalNode *Assign2();
    std::vector<Pipp_peak_3dContext *> pipp_peak_3d();
    Pipp_peak_3dContext* pipp_peak_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_peak_list_3dContext* pipp_peak_list_3d();

  class  Pipp_peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Pipp_peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_peak_3dContext* pipp_peak_3d();

  class  Pipp_peak_list_4dContext : public antlr4::ParserRuleContext {
  public:
    Pipp_peak_list_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *PkID();
    antlr4::tree::TerminalNode *X();
    antlr4::tree::TerminalNode *Y();
    antlr4::tree::TerminalNode *Z();
    antlr4::tree::TerminalNode *A();
    antlr4::tree::TerminalNode *Intensity();
    antlr4::tree::TerminalNode *RETURN_VA();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *Sl_A();
    antlr4::tree::TerminalNode *Sl_Z();
    antlr4::tree::TerminalNode *Assign();
    antlr4::tree::TerminalNode *Assign1();
    antlr4::tree::TerminalNode *Assign2();
    std::vector<Pipp_peak_4dContext *> pipp_peak_4d();
    Pipp_peak_4dContext* pipp_peak_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_peak_list_4dContext* pipp_peak_list_4d();

  class  Pipp_peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Pipp_peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_peak_4dContext* pipp_peak_4d();

  class  Pipp_row_peak_list_2dContext : public antlr4::ParserRuleContext {
  public:
    Pipp_row_peak_list_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Pipp_row_peak_2dContext *> pipp_row_peak_2d();
    Pipp_row_peak_2dContext* pipp_row_peak_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_row_peak_list_2dContext* pipp_row_peak_list_2d();

  class  Pipp_row_peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Pipp_row_peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_paren();
    std::vector<antlr4::tree::TerminalNode *> Float_PR();
    antlr4::tree::TerminalNode* Float_PR(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Semicolon();
    antlr4::tree::TerminalNode* Semicolon(size_t i);
    antlr4::tree::TerminalNode *Number_sign();
    std::vector<antlr4::tree::TerminalNode *> Integer_PR();
    antlr4::tree::TerminalNode* Integer_PR(size_t i);
    antlr4::tree::TerminalNode *Caret();
    antlr4::tree::TerminalNode *Real_PR();
    antlr4::tree::TerminalNode *Percent_sign();
    antlr4::tree::TerminalNode *R_paren();
    antlr4::tree::TerminalNode *RETURN_PR();
    antlr4::tree::TerminalNode *EOF();
    antlr4::tree::TerminalNode *Assignments_PR();
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *R_brkt();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_row_peak_2dContext* pipp_row_peak_2d();

  class  Pipp_row_peak_list_3dContext : public antlr4::ParserRuleContext {
  public:
    Pipp_row_peak_list_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Pipp_row_peak_3dContext *> pipp_row_peak_3d();
    Pipp_row_peak_3dContext* pipp_row_peak_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_row_peak_list_3dContext* pipp_row_peak_list_3d();

  class  Pipp_row_peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Pipp_row_peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_paren();
    std::vector<antlr4::tree::TerminalNode *> Float_PR();
    antlr4::tree::TerminalNode* Float_PR(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Semicolon();
    antlr4::tree::TerminalNode* Semicolon(size_t i);
    antlr4::tree::TerminalNode *Number_sign();
    std::vector<antlr4::tree::TerminalNode *> Integer_PR();
    antlr4::tree::TerminalNode* Integer_PR(size_t i);
    antlr4::tree::TerminalNode *Caret();
    antlr4::tree::TerminalNode *Real_PR();
    antlr4::tree::TerminalNode *Percent_sign();
    antlr4::tree::TerminalNode *R_paren();
    antlr4::tree::TerminalNode *RETURN_PR();
    antlr4::tree::TerminalNode *EOF();
    antlr4::tree::TerminalNode *Assignments_PR();
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *R_brkt();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_row_peak_3dContext* pipp_row_peak_3d();

  class  Pipp_row_peak_list_4dContext : public antlr4::ParserRuleContext {
  public:
    Pipp_row_peak_list_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Pipp_row_peak_4dContext *> pipp_row_peak_4d();
    Pipp_row_peak_4dContext* pipp_row_peak_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_row_peak_list_4dContext* pipp_row_peak_list_4d();

  class  Pipp_row_peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Pipp_row_peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_paren();
    std::vector<antlr4::tree::TerminalNode *> Float_PR();
    antlr4::tree::TerminalNode* Float_PR(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Semicolon();
    antlr4::tree::TerminalNode* Semicolon(size_t i);
    antlr4::tree::TerminalNode *Number_sign();
    std::vector<antlr4::tree::TerminalNode *> Integer_PR();
    antlr4::tree::TerminalNode* Integer_PR(size_t i);
    antlr4::tree::TerminalNode *Caret();
    antlr4::tree::TerminalNode *Real_PR();
    antlr4::tree::TerminalNode *Percent_sign();
    antlr4::tree::TerminalNode *R_paren();
    antlr4::tree::TerminalNode *RETURN_PR();
    antlr4::tree::TerminalNode *EOF();
    antlr4::tree::TerminalNode *Assignments_PR();
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *R_brkt();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_row_peak_4dContext* pipp_row_peak_4d();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Any_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

