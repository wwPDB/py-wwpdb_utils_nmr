
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PonderosaPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  PonderosaPKParser : public antlr4::Parser {
public:
  enum {
    Noesy_type = 1, Axis_order = 2, Integer = 3, Float = 4, Real = 5, SHARP_COMMENT = 6, 
    EXCLM_COMMENT = 7, SMCLN_COMMENT = 8, Simple_name = 9, SPACE = 10, RETURN = 11, 
    SECTION_COMMENT = 12, LINE_COMMENT = 13, Integer_NT = 14, Simple_name_NT = 15, 
    SPACE_NT = 16, RETURN_NT = 17, Integer_AO = 18, Simple_name_AO = 19, 
    SPACE_AO = 20, RETURN_AO = 21
  };

  enum {
    RulePonderosa_pk = 0, RulePeak_list_2d = 1, RulePeak_2d = 2, RulePeak_list_3d = 3, 
    RulePeak_3d = 4, RulePeak_list_4d = 5, RulePeak_4d = 6, RuleNumber = 7
  };

  explicit PonderosaPKParser(antlr4::TokenStream *input);

  PonderosaPKParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~PonderosaPKParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Ponderosa_pkContext;
  class Peak_list_2dContext;
  class Peak_2dContext;
  class Peak_list_3dContext;
  class Peak_3dContext;
  class Peak_list_4dContext;
  class Peak_4dContext;
  class NumberContext; 

  class  Ponderosa_pkContext : public antlr4::ParserRuleContext {
  public:
    Ponderosa_pkContext(antlr4::ParserRuleContext *parent, size_t invokingState);
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


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ponderosa_pkContext* ponderosa_pk();

  class  Peak_list_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Noesy_type();
    antlr4::tree::TerminalNode *Integer_NT();
    antlr4::tree::TerminalNode *Simple_name_NT();
    antlr4::tree::TerminalNode *RETURN_NT();
    antlr4::tree::TerminalNode *Axis_order();
    antlr4::tree::TerminalNode *Integer_AO();
    antlr4::tree::TerminalNode *Simple_name_AO();
    antlr4::tree::TerminalNode *RETURN_AO();
    std::vector<Peak_2dContext *> peak_2d();
    Peak_2dContext* peak_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_2dContext* peak_list_2d();

  class  Peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    NumberContext *number();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_2dContext* peak_2d();

  class  Peak_list_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Noesy_type();
    antlr4::tree::TerminalNode *Integer_NT();
    antlr4::tree::TerminalNode *Simple_name_NT();
    antlr4::tree::TerminalNode *RETURN_NT();
    antlr4::tree::TerminalNode *Axis_order();
    antlr4::tree::TerminalNode *Integer_AO();
    antlr4::tree::TerminalNode *Simple_name_AO();
    antlr4::tree::TerminalNode *RETURN_AO();
    std::vector<Peak_3dContext *> peak_3d();
    Peak_3dContext* peak_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_3dContext* peak_list_3d();

  class  Peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    NumberContext *number();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_3dContext* peak_3d();

  class  Peak_list_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Noesy_type();
    antlr4::tree::TerminalNode *Integer_NT();
    antlr4::tree::TerminalNode *Simple_name_NT();
    antlr4::tree::TerminalNode *RETURN_NT();
    antlr4::tree::TerminalNode *Axis_order();
    antlr4::tree::TerminalNode *Integer_AO();
    antlr4::tree::TerminalNode *Simple_name_AO();
    antlr4::tree::TerminalNode *RETURN_AO();
    std::vector<Peak_4dContext *> peak_4d();
    Peak_4dContext* peak_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_4dContext* peak_list_4d();

  class  Peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    NumberContext *number();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_4dContext* peak_4d();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Real();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

