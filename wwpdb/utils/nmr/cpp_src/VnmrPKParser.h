
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/VnmrPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  VnmrPKParser : public antlr4::Parser {
public:
  enum {
    Peak_id = 1, Format = 2, Integer = 3, Float = 4, Real = 5, COMMENT = 6, 
    Double_quote_string = 7, EXCLM_COMMENT = 8, SMCLN_COMMENT = 9, Assignment_2d_ex = 10, 
    Assignment_3d_ex = 11, Assignment_4d_ex = 12, SPACE = 13, RETURN = 14, 
    SECTION_COMMENT = 15, LINE_COMMENT = 16, Dim_0_ppm = 17, Dim_1_ppm = 18, 
    Dim_2_ppm = 19, Dim_3_ppm = 20, Dev_0 = 21, Dev_1 = 22, Dev_2 = 23, 
    Dev_3 = 24, Amplitude_LA = 25, Volume_LA = 26, Assignment = 27, SPACE_LA = 28, 
    RETURN_LA = 29, Peak_number = 30, X_ppm = 31, Y_ppm = 32, Z_ppm = 33, 
    A_ppm = 34, Amplitude = 35, Volume = 36, Linewidth_X = 37, Linewidth_Y = 38, 
    Linewidth_Z = 39, Linewidth_A = 40, FWHM_X = 41, FWHM_Y = 42, FWHM_Z = 43, 
    FWHM_A = 44, Label = 45, Comment = 46, SPACE_FO = 47, RETURN_FO = 48, 
    Any_name = 49, SPACE_CM = 50, RETURN_CM = 51
  };

  enum {
    RuleVnmr_pk = 0, RuleComment = 1, RuleFormat = 2, RulePeak_ll2d = 3, 
    RulePeak_ll3d = 4, RulePeak_ll4d = 5, RuleData_label = 6, RulePeak_2d = 7, 
    RulePeak_3d = 8, RulePeak_4d = 9, RuleNumber = 10
  };

  explicit VnmrPKParser(antlr4::TokenStream *input);

  VnmrPKParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~VnmrPKParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Vnmr_pkContext;
  class CommentContext;
  class FormatContext;
  class Peak_ll2dContext;
  class Peak_ll3dContext;
  class Peak_ll4dContext;
  class Data_labelContext;
  class Peak_2dContext;
  class Peak_3dContext;
  class Peak_4dContext;
  class NumberContext; 

  class  Vnmr_pkContext : public antlr4::ParserRuleContext {
  public:
    Vnmr_pkContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<FormatContext *> format();
    FormatContext* format(size_t i);
    std::vector<Data_labelContext *> data_label();
    Data_labelContext* data_label(size_t i);
    std::vector<Peak_2dContext *> peak_2d();
    Peak_2dContext* peak_2d(size_t i);
    std::vector<Peak_3dContext *> peak_3d();
    Peak_3dContext* peak_3d(size_t i);
    std::vector<Peak_4dContext *> peak_4d();
    Peak_4dContext* peak_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vnmr_pkContext* vnmr_pk();

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

  class  FormatContext : public antlr4::ParserRuleContext {
  public:
    FormatContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *Peak_number();
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *RETURN_FO();
    antlr4::tree::TerminalNode *Z_ppm();
    antlr4::tree::TerminalNode *A_ppm();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Label();
    antlr4::tree::TerminalNode *Comment();
    antlr4::tree::TerminalNode *Linewidth_X();
    antlr4::tree::TerminalNode *FWHM_X();
    antlr4::tree::TerminalNode *Linewidth_Y();
    antlr4::tree::TerminalNode *FWHM_Y();
    antlr4::tree::TerminalNode *Linewidth_Z();
    antlr4::tree::TerminalNode *FWHM_Z();
    antlr4::tree::TerminalNode *Linewidth_A();
    antlr4::tree::TerminalNode *FWHM_A();
    std::vector<Peak_ll2dContext *> peak_ll2d();
    Peak_ll2dContext* peak_ll2d(size_t i);
    std::vector<Peak_ll3dContext *> peak_ll3d();
    Peak_ll3dContext* peak_ll3d(size_t i);
    std::vector<Peak_ll4dContext *> peak_ll4d();
    Peak_ll4dContext* peak_ll4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  FormatContext* format();

  class  Peak_ll2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_ll2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string();
    antlr4::tree::TerminalNode* Double_quote_string(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_ll2dContext* peak_ll2d();

  class  Peak_ll3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_ll3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string();
    antlr4::tree::TerminalNode* Double_quote_string(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_ll3dContext* peak_ll3d();

  class  Peak_ll4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_ll4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string();
    antlr4::tree::TerminalNode* Double_quote_string(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_ll4dContext* peak_ll4d();

  class  Data_labelContext : public antlr4::ParserRuleContext {
  public:
    Data_labelContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Peak_id();
    antlr4::tree::TerminalNode *Dim_0_ppm();
    antlr4::tree::TerminalNode *Dev_0();
    antlr4::tree::TerminalNode *Dim_1_ppm();
    antlr4::tree::TerminalNode *Dev_1();
    antlr4::tree::TerminalNode *Amplitude_LA();
    antlr4::tree::TerminalNode *RETURN_LA();
    antlr4::tree::TerminalNode *Dim_2_ppm();
    antlr4::tree::TerminalNode *Dev_2();
    antlr4::tree::TerminalNode *Volume_LA();
    antlr4::tree::TerminalNode *Assignment();
    antlr4::tree::TerminalNode *Dim_3_ppm();
    antlr4::tree::TerminalNode *Dev_3();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Data_labelContext* data_label();

  class  Peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    NumberContext *number();
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    antlr4::tree::TerminalNode *Assignment_2d_ex();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_2dContext* peak_2d();

  class  Peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    NumberContext *number();
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    antlr4::tree::TerminalNode *Assignment_3d_ex();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_3dContext* peak_3d();

  class  Peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    NumberContext *number();
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    antlr4::tree::TerminalNode *Assignment_4d_ex();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_4dContext* peak_4d();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Float();
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

