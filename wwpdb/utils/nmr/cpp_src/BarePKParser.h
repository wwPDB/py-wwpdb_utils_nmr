
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BarePKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  BarePKParser : public antlr4::Parser {
public:
  enum {
    Peak = 1, X_PPM = 2, Y_PPM = 3, Z_PPM = 4, A_PPM = 5, Integer = 6, Float = 7, 
    Real = 8, Ambig_float = 9, SHARP_COMMENT = 10, EXCLM_COMMENT = 11, Simple_name = 12, 
    SPACE = 13, RETURN = 14, SECTION_COMMENT = 15, LINE_COMMENT = 16, X_ppm = 17, 
    Y_ppm = 18, Z_ppm = 19, A_ppm = 20, X_width = 21, Y_width = 22, Z_width = 23, 
    A_width = 24, Amplitude = 25, Volume = 26, Label = 27, Comment = 28, 
    SPACE_FO = 29, RETURN_FO = 30
  };

  enum {
    RuleBare_pk = 0, RulePeak_list_2d = 1, RulePeak_2d = 2, RulePeak_list_3d = 3, 
    RulePeak_3d = 4, RulePeak_list_4d = 5, RulePeak_4d = 6, RulePeak_list_wo_chain_2d = 7, 
    RulePeak_wo_chain_2d = 8, RulePeak_list_wo_chain_3d = 9, RulePeak_wo_chain_3d = 10, 
    RulePeak_list_wo_chain_4d = 11, RulePeak_wo_chain_4d = 12, RuleRow_format_2d = 13, 
    RuleRow_format_3d = 14, RuleRow_format_4d = 15, RuleRev_row_format_2d = 16, 
    RuleRev_row_format_3d = 17, RuleRev_row_format_4d = 18, RuleRow_format_wo_label_2d = 19, 
    RuleRow_format_wo_label_3d = 20, RuleRow_format_wo_label_4d = 21, RulePeak_list_row_2d = 22, 
    RulePeak_list_row_3d = 23, RulePeak_list_row_4d = 24, RulePosition = 25, 
    RuleNumber = 26
  };

  explicit BarePKParser(antlr4::TokenStream *input);

  BarePKParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~BarePKParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Bare_pkContext;
  class Peak_list_2dContext;
  class Peak_2dContext;
  class Peak_list_3dContext;
  class Peak_3dContext;
  class Peak_list_4dContext;
  class Peak_4dContext;
  class Peak_list_wo_chain_2dContext;
  class Peak_wo_chain_2dContext;
  class Peak_list_wo_chain_3dContext;
  class Peak_wo_chain_3dContext;
  class Peak_list_wo_chain_4dContext;
  class Peak_wo_chain_4dContext;
  class Row_format_2dContext;
  class Row_format_3dContext;
  class Row_format_4dContext;
  class Rev_row_format_2dContext;
  class Rev_row_format_3dContext;
  class Rev_row_format_4dContext;
  class Row_format_wo_label_2dContext;
  class Row_format_wo_label_3dContext;
  class Row_format_wo_label_4dContext;
  class Peak_list_row_2dContext;
  class Peak_list_row_3dContext;
  class Peak_list_row_4dContext;
  class PositionContext;
  class NumberContext; 

  class  Bare_pkContext : public antlr4::ParserRuleContext {
  public:
    Bare_pkContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Peak_list_2dContext *> peak_list_2d();
    Peak_list_2dContext* peak_list_2d(size_t i);
    std::vector<Peak_list_3dContext *> peak_list_3d();
    Peak_list_3dContext* peak_list_3d(size_t i);
    std::vector<Peak_list_4dContext *> peak_list_4d();
    Peak_list_4dContext* peak_list_4d(size_t i);
    std::vector<Peak_list_wo_chain_2dContext *> peak_list_wo_chain_2d();
    Peak_list_wo_chain_2dContext* peak_list_wo_chain_2d(size_t i);
    std::vector<Peak_list_wo_chain_3dContext *> peak_list_wo_chain_3d();
    Peak_list_wo_chain_3dContext* peak_list_wo_chain_3d(size_t i);
    std::vector<Peak_list_wo_chain_4dContext *> peak_list_wo_chain_4d();
    Peak_list_wo_chain_4dContext* peak_list_wo_chain_4d(size_t i);
    std::vector<Row_format_2dContext *> row_format_2d();
    Row_format_2dContext* row_format_2d(size_t i);
    std::vector<Row_format_3dContext *> row_format_3d();
    Row_format_3dContext* row_format_3d(size_t i);
    std::vector<Row_format_4dContext *> row_format_4d();
    Row_format_4dContext* row_format_4d(size_t i);
    std::vector<Rev_row_format_2dContext *> rev_row_format_2d();
    Rev_row_format_2dContext* rev_row_format_2d(size_t i);
    std::vector<Rev_row_format_3dContext *> rev_row_format_3d();
    Rev_row_format_3dContext* rev_row_format_3d(size_t i);
    std::vector<Rev_row_format_4dContext *> rev_row_format_4d();
    Rev_row_format_4dContext* rev_row_format_4d(size_t i);
    std::vector<Row_format_wo_label_2dContext *> row_format_wo_label_2d();
    Row_format_wo_label_2dContext* row_format_wo_label_2d(size_t i);
    std::vector<Row_format_wo_label_3dContext *> row_format_wo_label_3d();
    Row_format_wo_label_3dContext* row_format_wo_label_3d(size_t i);
    std::vector<Row_format_wo_label_4dContext *> row_format_wo_label_4d();
    Row_format_wo_label_4dContext* row_format_wo_label_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Bare_pkContext* bare_pk();

  class  Peak_list_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Peak_2dContext *> peak_2d();
    Peak_2dContext* peak_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_2dContext* peak_list_2d();

  class  Peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_2dContext* peak_2d();

  class  Peak_list_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Peak_3dContext *> peak_3d();
    Peak_3dContext* peak_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_3dContext* peak_list_3d();

  class  Peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_3dContext* peak_3d();

  class  Peak_list_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Peak_4dContext *> peak_4d();
    Peak_4dContext* peak_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_4dContext* peak_list_4d();

  class  Peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_4dContext* peak_4d();

  class  Peak_list_wo_chain_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_wo_chain_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Peak_wo_chain_2dContext *> peak_wo_chain_2d();
    Peak_wo_chain_2dContext* peak_wo_chain_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_wo_chain_2dContext* peak_list_wo_chain_2d();

  class  Peak_wo_chain_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_wo_chain_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_wo_chain_2dContext* peak_wo_chain_2d();

  class  Peak_list_wo_chain_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_wo_chain_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Peak_wo_chain_3dContext *> peak_wo_chain_3d();
    Peak_wo_chain_3dContext* peak_wo_chain_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_wo_chain_3dContext* peak_list_wo_chain_3d();

  class  Peak_wo_chain_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_wo_chain_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_wo_chain_3dContext* peak_wo_chain_3d();

  class  Peak_list_wo_chain_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_wo_chain_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Peak_wo_chain_4dContext *> peak_wo_chain_4d();
    Peak_wo_chain_4dContext* peak_wo_chain_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_wo_chain_4dContext* peak_list_wo_chain_4d();

  class  Peak_wo_chain_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_wo_chain_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_wo_chain_4dContext* peak_wo_chain_4d();

  class  Row_format_2dContext : public antlr4::ParserRuleContext {
  public:
    Row_format_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Peak();
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *X_PPM();
    antlr4::tree::TerminalNode *X_width();
    antlr4::tree::TerminalNode *Y_width();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Label();
    antlr4::tree::TerminalNode *Comment();
    std::vector<Peak_list_row_2dContext *> peak_list_row_2d();
    Peak_list_row_2dContext* peak_list_row_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Row_format_2dContext* row_format_2d();

  class  Row_format_3dContext : public antlr4::ParserRuleContext {
  public:
    Row_format_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *Z_ppm();
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Peak();
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *X_PPM();
    antlr4::tree::TerminalNode *X_width();
    antlr4::tree::TerminalNode *Y_width();
    antlr4::tree::TerminalNode *Z_width();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Label();
    antlr4::tree::TerminalNode *Comment();
    std::vector<Peak_list_row_3dContext *> peak_list_row_3d();
    Peak_list_row_3dContext* peak_list_row_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Row_format_3dContext* row_format_3d();

  class  Row_format_4dContext : public antlr4::ParserRuleContext {
  public:
    Row_format_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *Z_ppm();
    antlr4::tree::TerminalNode *A_ppm();
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Peak();
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *X_PPM();
    antlr4::tree::TerminalNode *X_width();
    antlr4::tree::TerminalNode *Y_width();
    antlr4::tree::TerminalNode *Z_width();
    antlr4::tree::TerminalNode *A_width();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Label();
    antlr4::tree::TerminalNode *Comment();
    std::vector<Peak_list_row_4dContext *> peak_list_row_4d();
    Peak_list_row_4dContext* peak_list_row_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Row_format_4dContext* row_format_4d();

  class  Rev_row_format_2dContext : public antlr4::ParserRuleContext {
  public:
    Rev_row_format_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Peak();
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *Y_PPM();
    antlr4::tree::TerminalNode *Y_width();
    antlr4::tree::TerminalNode *X_width();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Label();
    antlr4::tree::TerminalNode *Comment();
    std::vector<Peak_list_row_2dContext *> peak_list_row_2d();
    Peak_list_row_2dContext* peak_list_row_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rev_row_format_2dContext* rev_row_format_2d();

  class  Rev_row_format_3dContext : public antlr4::ParserRuleContext {
  public:
    Rev_row_format_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Peak();
    antlr4::tree::TerminalNode *Z_ppm();
    antlr4::tree::TerminalNode *Z_PPM();
    antlr4::tree::TerminalNode *Z_width();
    antlr4::tree::TerminalNode *Y_width();
    antlr4::tree::TerminalNode *X_width();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Label();
    antlr4::tree::TerminalNode *Comment();
    std::vector<Peak_list_row_3dContext *> peak_list_row_3d();
    Peak_list_row_3dContext* peak_list_row_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rev_row_format_3dContext* rev_row_format_3d();

  class  Rev_row_format_4dContext : public antlr4::ParserRuleContext {
  public:
    Rev_row_format_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Z_ppm();
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Peak();
    antlr4::tree::TerminalNode *A_ppm();
    antlr4::tree::TerminalNode *A_PPM();
    antlr4::tree::TerminalNode *A_width();
    antlr4::tree::TerminalNode *Z_width();
    antlr4::tree::TerminalNode *Y_width();
    antlr4::tree::TerminalNode *X_width();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Label();
    antlr4::tree::TerminalNode *Comment();
    std::vector<Peak_list_row_4dContext *> peak_list_row_4d();
    Peak_list_row_4dContext* peak_list_row_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rev_row_format_4dContext* rev_row_format_4d();

  class  Row_format_wo_label_2dContext : public antlr4::ParserRuleContext {
  public:
    Row_format_wo_label_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Peak_list_row_2dContext *> peak_list_row_2d();
    Peak_list_row_2dContext* peak_list_row_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Row_format_wo_label_2dContext* row_format_wo_label_2d();

  class  Row_format_wo_label_3dContext : public antlr4::ParserRuleContext {
  public:
    Row_format_wo_label_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Peak_list_row_3dContext *> peak_list_row_3d();
    Peak_list_row_3dContext* peak_list_row_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Row_format_wo_label_3dContext* row_format_wo_label_3d();

  class  Row_format_wo_label_4dContext : public antlr4::ParserRuleContext {
  public:
    Row_format_wo_label_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Peak_list_row_4dContext *> peak_list_row_4d();
    Peak_list_row_4dContext* peak_list_row_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Row_format_wo_label_4dContext* row_format_wo_label_4d();

  class  Peak_list_row_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_row_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_row_2dContext* peak_list_row_2d();

  class  Peak_list_row_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_row_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_row_3dContext* peak_list_row_3d();

  class  Peak_list_row_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_row_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_row_4dContext* peak_list_row_4d();

  class  PositionContext : public antlr4::ParserRuleContext {
  public:
    PositionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Ambig_float();


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


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

