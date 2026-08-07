
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PippCSParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  PippCSParser : public antlr4::Parser {
public:
  enum {
    Shift_fl_frmt = 1, Res_siad = 2, First_res_in_seq = 3, Exp_peak_pick_tbl = 4, 
    Res_ID = 5, Res_type = 6, Spin_system_ID = 7, Heterogeneity = 8, End_res_def = 9, 
    L_paren = 10, R_paren = 11, Integer = 12, Float = 13, SHARP_COMMENT = 14, 
    EXCLM_COMMENT = 15, Simple_name = 16, SPACE = 17, RETURN = 18, SECTION_COMMENT = 19, 
    LINE_COMMENT = 20, Res_ID_ = 21, Label = 22, Exp_par_fl = 23, Peak_pick_fl = 24, 
    Cross_ref = 25, Simple_name_ET = 26, SPACE_ET = 27, RETURN_ET = 28
  };

  enum {
    RulePipp_cs = 0, RulePipp_format = 1, RuleExt_peak_pick_tbl = 2, RuleExt_peak_pick_tbl_row = 3, 
    RuleResidue_list = 4, RuleShift_list = 5, RuleNumber = 6
  };

  explicit PippCSParser(antlr4::TokenStream *input);

  PippCSParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~PippCSParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Pipp_csContext;
  class Pipp_formatContext;
  class Ext_peak_pick_tblContext;
  class Ext_peak_pick_tbl_rowContext;
  class Residue_listContext;
  class Shift_listContext;
  class NumberContext; 

  class  Pipp_csContext : public antlr4::ParserRuleContext {
  public:
    Pipp_csContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Pipp_formatContext *> pipp_format();
    Pipp_formatContext* pipp_format(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_csContext* pipp_cs();

  class  Pipp_formatContext : public antlr4::ParserRuleContext {
  public:
    Pipp_formatContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Shift_fl_frmt();
    antlr4::tree::TerminalNode *Res_siad();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    antlr4::tree::TerminalNode *First_res_in_seq();
    antlr4::tree::TerminalNode *Integer();
    Ext_peak_pick_tblContext *ext_peak_pick_tbl();
    std::vector<Residue_listContext *> residue_list();
    Residue_listContext* residue_list(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pipp_formatContext* pipp_format();

  class  Ext_peak_pick_tblContext : public antlr4::ParserRuleContext {
  public:
    Ext_peak_pick_tblContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Exp_peak_pick_tbl();
    std::vector<antlr4::tree::TerminalNode *> RETURN_ET();
    antlr4::tree::TerminalNode* RETURN_ET(size_t i);
    antlr4::tree::TerminalNode *Label();
    antlr4::tree::TerminalNode *Exp_par_fl();
    antlr4::tree::TerminalNode *Peak_pick_fl();
    antlr4::tree::TerminalNode *Cross_ref();
    std::vector<Ext_peak_pick_tbl_rowContext *> ext_peak_pick_tbl_row();
    Ext_peak_pick_tbl_rowContext* ext_peak_pick_tbl_row(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ext_peak_pick_tblContext* ext_peak_pick_tbl();

  class  Ext_peak_pick_tbl_rowContext : public antlr4::ParserRuleContext {
  public:
    Ext_peak_pick_tbl_rowContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name_ET();
    antlr4::tree::TerminalNode* Simple_name_ET(size_t i);
    antlr4::tree::TerminalNode *RETURN_ET();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ext_peak_pick_tbl_rowContext* ext_peak_pick_tbl_row();

  class  Residue_listContext : public antlr4::ParserRuleContext {
  public:
    Residue_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    antlr4::tree::TerminalNode *Res_type();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Spin_system_ID();
    antlr4::tree::TerminalNode *Heterogeneity();
    antlr4::tree::TerminalNode *End_res_def();
    antlr4::tree::TerminalNode *Res_ID();
    antlr4::tree::TerminalNode *Res_ID_();
    antlr4::tree::TerminalNode *EOF();
    std::vector<Shift_listContext *> shift_list();
    Shift_listContext* shift_list(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Residue_listContext* residue_list();

  class  Shift_listContext : public antlr4::ParserRuleContext {
  public:
    Shift_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    NumberContext *number();
    antlr4::tree::TerminalNode *L_paren();
    antlr4::tree::TerminalNode *R_paren();
    antlr4::tree::TerminalNode *RETURN();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Shift_listContext* shift_list();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

