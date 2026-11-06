
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  NmrViewCSParser : public antlr4::Parser {
public:
  enum {
    Integer = 1, Float = 2, SHARP_COMMENT = 3, EXCLM_COMMENT = 4, Res_ID = 5, 
    Res_Type = 6, Prev_Type = 7, Spin_System_ID = 8, Heterogeneity = 9, 
    End_Res_Def = 10, Type_pred = 11, Single_note = 12, Note_begin = 13, 
    Simple_name = 14, SPACE = 15, RETURN = 16, SECTION_COMMENT = 17, LINE_COMMENT = 18, 
    Note_middle = 19, Note_end = 20, SPACE_MN = 21
  };

  enum {
    RuleNmrview_cs = 0, RuleRes_def_list = 1, RuleRes_id_def = 2, RuleRes_type_def = 3, 
    RulePrev_type_def = 4, RuleSpin_system_def = 5, RuleHeterogeneity_def = 6, 
    RuleShift_list = 7
  };

  explicit NmrViewCSParser(antlr4::TokenStream *input);

  NmrViewCSParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~NmrViewCSParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Nmrview_csContext;
  class Res_def_listContext;
  class Res_id_defContext;
  class Res_type_defContext;
  class Prev_type_defContext;
  class Spin_system_defContext;
  class Heterogeneity_defContext;
  class Shift_listContext; 

  class  Nmrview_csContext : public antlr4::ParserRuleContext {
  public:
    Nmrview_csContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Res_def_listContext *> res_def_list();
    Res_def_listContext* res_def_list(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Nmrview_csContext* nmrview_cs();

  class  Res_def_listContext : public antlr4::ParserRuleContext {
  public:
    Res_def_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Res_id_defContext *res_id_def();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    Res_type_defContext *res_type_def();
    Spin_system_defContext *spin_system_def();
    Heterogeneity_defContext *heterogeneity_def();
    antlr4::tree::TerminalNode *End_Res_Def();
    Prev_type_defContext *prev_type_def();
    std::vector<Shift_listContext *> shift_list();
    Shift_listContext* shift_list(size_t i);
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Res_def_listContext* res_def_list();

  class  Res_id_defContext : public antlr4::ParserRuleContext {
  public:
    Res_id_defContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Res_ID();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Res_id_defContext* res_id_def();

  class  Res_type_defContext : public antlr4::ParserRuleContext {
  public:
    Res_type_defContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Res_Type();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Res_type_defContext* res_type_def();

  class  Prev_type_defContext : public antlr4::ParserRuleContext {
  public:
    Prev_type_defContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Prev_Type();
    std::vector<antlr4::tree::TerminalNode *> Type_pred();
    antlr4::tree::TerminalNode* Type_pred(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Prev_type_defContext* prev_type_def();

  class  Spin_system_defContext : public antlr4::ParserRuleContext {
  public:
    Spin_system_defContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Spin_System_ID();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Spin_system_defContext* spin_system_def();

  class  Heterogeneity_defContext : public antlr4::ParserRuleContext {
  public:
    Heterogeneity_defContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Heterogeneity();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Heterogeneity_defContext* heterogeneity_def();

  class  Shift_listContext : public antlr4::ParserRuleContext {
  public:
    Shift_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    antlr4::tree::TerminalNode *Single_note();
    antlr4::tree::TerminalNode *Note_begin();
    antlr4::tree::TerminalNode *Note_end();
    std::vector<antlr4::tree::TerminalNode *> Note_middle();
    antlr4::tree::TerminalNode* Note_middle(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Shift_listContext* shift_list();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

