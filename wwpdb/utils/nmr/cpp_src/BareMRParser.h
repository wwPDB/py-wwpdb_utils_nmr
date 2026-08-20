
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BareMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  BareMRParser : public antlr4::Parser {
public:
  enum {
    Integer = 1, Float = 2, SHARP_COMMENT = 3, EXCLM_COMMENT = 4, Number_of_name = 5, 
    Simple_name = 6, Double_quote_string = 7, Double_quote_integer = 8, 
    Double_quote_float = 9, SPACE = 10, RETURN = 11, SECTION_COMMENT = 12, 
    LINE_COMMENT = 13
  };

  enum {
    RuleBare_mr = 0, RuleMr_row_format = 1, RuleHeader = 2, RuleMr_row_list = 3, 
    RuleAny = 4, RuleColumn_name = 5
  };

  explicit BareMRParser(antlr4::TokenStream *input);

  BareMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~BareMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Bare_mrContext;
  class Mr_row_formatContext;
  class HeaderContext;
  class Mr_row_listContext;
  class AnyContext;
  class Column_nameContext; 

  class  Bare_mrContext : public antlr4::ParserRuleContext {
  public:
    Bare_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Mr_row_formatContext *> mr_row_format();
    Mr_row_formatContext* mr_row_format(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Bare_mrContext* bare_mr();

  class  Mr_row_formatContext : public antlr4::ParserRuleContext {
  public:
    Mr_row_formatContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    HeaderContext *header();
    std::vector<Mr_row_listContext *> mr_row_list();
    Mr_row_listContext* mr_row_list(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Mr_row_formatContext* mr_row_format();

  class  HeaderContext : public antlr4::ParserRuleContext {
  public:
    HeaderContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN();
    std::vector<Column_nameContext *> column_name();
    Column_nameContext* column_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  HeaderContext* header();

  class  Mr_row_listContext : public antlr4::ParserRuleContext {
  public:
    Mr_row_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<AnyContext *> any();
    AnyContext* any(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Mr_row_listContext* mr_row_list();

  class  AnyContext : public antlr4::ParserRuleContext {
  public:
    AnyContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Double_quote_float();
    antlr4::tree::TerminalNode *Double_quote_integer();
    antlr4::tree::TerminalNode *Double_quote_string();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  AnyContext* any();

  class  Column_nameContext : public antlr4::ParserRuleContext {
  public:
    Column_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Double_quote_string();
    antlr4::tree::TerminalNode *Number_of_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Column_nameContext* column_name();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

