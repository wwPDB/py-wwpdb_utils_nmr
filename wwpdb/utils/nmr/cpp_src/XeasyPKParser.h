
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XeasyPKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  XeasyPKParser : public antlr4::Parser {
public:
  enum {
    Num_of_dim = 1, Num_of_peaks = 2, Format = 3, XEASY_WO_FORMAT = 4, Iname = 5, 
    Cyana_format = 6, Spectrum = 7, Tolerance = 8, Integer = 9, Float = 10, 
    Real = 11, COMMENT = 12, EXCLM_COMMENT = 13, SMCLN_COMMENT = 14, Simple_name = 15, 
    SPACE = 16, RETURN = 17, SECTION_COMMENT = 18, LINE_COMMENT = 19, Integer_ND = 20, 
    SPACE_ND = 21, RETURN_ND = 22, Integer_NP = 23, SPACE_NP = 24, RETURN_NP = 25, 
    Simple_name_FO = 26, SPACE_FO = 27, RETURN_FO = 28, Integer_IN = 29, 
    Simple_name_IN = 30, SPACE_IN = 31, RETURN_IN = 32, Simple_name_CY = 33, 
    SPACE_CY = 34, RETURN_CY = 35, Simple_name_SP = 36, SPACE_SP = 37, RETURN_SP = 38, 
    Float_TO = 39, TOACE_TO = 40, RETURN_TO = 41, Any_name = 42, SPACE_CM = 43, 
    RETURN_CM = 44
  };

  enum {
    RuleXeasy_pk = 0, RuleDimension = 1, RulePeak = 2, RuleFormat = 3, RuleIname = 4, 
    RuleCyana_format = 5, RuleSpectrum = 6, RuleTolerance = 7, RulePeak_list_2d = 8, 
    RulePeak_2d = 9, RulePeak_list_3d = 10, RulePeak_3d = 11, RulePeak_list_4d = 12, 
    RulePeak_4d = 13, RulePosition = 14, RuleNumber = 15, RuleType_code = 16, 
    RuleAssign = 17, RuleComment = 18
  };

  explicit XeasyPKParser(antlr4::TokenStream *input);

  XeasyPKParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~XeasyPKParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Xeasy_pkContext;
  class DimensionContext;
  class PeakContext;
  class FormatContext;
  class InameContext;
  class Cyana_formatContext;
  class SpectrumContext;
  class ToleranceContext;
  class Peak_list_2dContext;
  class Peak_2dContext;
  class Peak_list_3dContext;
  class Peak_3dContext;
  class Peak_list_4dContext;
  class Peak_4dContext;
  class PositionContext;
  class NumberContext;
  class Type_codeContext;
  class AssignContext;
  class CommentContext; 

  class  Xeasy_pkContext : public antlr4::ParserRuleContext {
  public:
    Xeasy_pkContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<DimensionContext *> dimension();
    DimensionContext* dimension(size_t i);
    std::vector<PeakContext *> peak();
    PeakContext* peak(size_t i);
    std::vector<FormatContext *> format();
    FormatContext* format(size_t i);
    std::vector<InameContext *> iname();
    InameContext* iname(size_t i);
    std::vector<Cyana_formatContext *> cyana_format();
    Cyana_formatContext* cyana_format(size_t i);
    std::vector<SpectrumContext *> spectrum();
    SpectrumContext* spectrum(size_t i);
    std::vector<ToleranceContext *> tolerance();
    ToleranceContext* tolerance(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<Peak_list_2dContext *> peak_list_2d();
    Peak_list_2dContext* peak_list_2d(size_t i);
    std::vector<Peak_list_3dContext *> peak_list_3d();
    Peak_list_3dContext* peak_list_3d(size_t i);
    std::vector<Peak_list_4dContext *> peak_list_4d();
    Peak_list_4dContext* peak_list_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Xeasy_pkContext* xeasy_pk();

  class  DimensionContext : public antlr4::ParserRuleContext {
  public:
    DimensionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Num_of_dim();
    antlr4::tree::TerminalNode *Integer_ND();
    antlr4::tree::TerminalNode *RETURN_ND();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  DimensionContext* dimension();

  class  PeakContext : public antlr4::ParserRuleContext {
  public:
    PeakContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Num_of_peaks();
    antlr4::tree::TerminalNode *Integer_NP();
    antlr4::tree::TerminalNode *RETURN_NP();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  PeakContext* peak();

  class  FormatContext : public antlr4::ParserRuleContext {
  public:
    FormatContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_FO();
    antlr4::tree::TerminalNode* Simple_name_FO(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  FormatContext* format();

  class  InameContext : public antlr4::ParserRuleContext {
  public:
    InameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Iname();
    antlr4::tree::TerminalNode *Integer_IN();
    antlr4::tree::TerminalNode *Simple_name_IN();
    antlr4::tree::TerminalNode *RETURN_IN();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  InameContext* iname();

  class  Cyana_formatContext : public antlr4::ParserRuleContext {
  public:
    Cyana_formatContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Cyana_format();
    antlr4::tree::TerminalNode *Simple_name_CY();
    antlr4::tree::TerminalNode *RETURN_CY();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cyana_formatContext* cyana_format();

  class  SpectrumContext : public antlr4::ParserRuleContext {
  public:
    SpectrumContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Spectrum();
    antlr4::tree::TerminalNode *RETURN_SP();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_SP();
    antlr4::tree::TerminalNode* Simple_name_SP(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  SpectrumContext* spectrum();

  class  ToleranceContext : public antlr4::ParserRuleContext {
  public:
    ToleranceContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Tolerance();
    antlr4::tree::TerminalNode *RETURN_TO();
    std::vector<antlr4::tree::TerminalNode *> Float_TO();
    antlr4::tree::TerminalNode* Float_TO(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ToleranceContext* tolerance();

  class  Peak_list_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Peak_2dContext *> peak_2d();
    Peak_2dContext* peak_2d(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_2dContext* peak_list_2d();

  class  Peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    Type_codeContext *type_code();
    std::vector<AssignContext *> assign();
    AssignContext* assign(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<antlr4::tree::TerminalNode *> EOF();
    antlr4::tree::TerminalNode* EOF(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_2dContext* peak_2d();

  class  Peak_list_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Peak_3dContext *> peak_3d();
    Peak_3dContext* peak_3d(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_3dContext* peak_list_3d();

  class  Peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    Type_codeContext *type_code();
    std::vector<AssignContext *> assign();
    AssignContext* assign(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<antlr4::tree::TerminalNode *> EOF();
    antlr4::tree::TerminalNode* EOF(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_3dContext* peak_3d();

  class  Peak_list_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Peak_4dContext *> peak_4d();
    Peak_4dContext* peak_4d(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_4dContext* peak_list_4d();

  class  Peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    Type_codeContext *type_code();
    std::vector<AssignContext *> assign();
    AssignContext* assign(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<antlr4::tree::TerminalNode *> EOF();
    antlr4::tree::TerminalNode* EOF(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_4dContext* peak_4d();

  class  PositionContext : public antlr4::ParserRuleContext {
  public:
    PositionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  PositionContext* position();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  Type_codeContext : public antlr4::ParserRuleContext {
  public:
    Type_codeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Type_codeContext* type_code();

  class  AssignContext : public antlr4::ParserRuleContext {
  public:
    AssignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  AssignContext* assign();

  class  CommentContext : public antlr4::ParserRuleContext {
  public:
    CommentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COMMENT();
    antlr4::tree::TerminalNode *RETURN_CM();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Any_name();
    antlr4::tree::TerminalNode* Any_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CommentContext* comment();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

