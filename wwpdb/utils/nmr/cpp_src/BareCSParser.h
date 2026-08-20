
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BareCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  BareCSParser : public antlr4::Parser {
public:
  enum {
    Integer = 1, Float = 2, SHARP_COMMENT = 3, EXCLM_COMMENT = 4, Number_of_name = 5, 
    Simple_name = 6, Double_quote_string = 7, Double_quote_integer = 8, 
    Double_quote_float = 9, SPACE = 10, RETURN = 11, SECTION_COMMENT = 12, 
    LINE_COMMENT = 13
  };

  enum {
    RuleBare_cs = 0, RuleCs_row_format = 1, RuleHeader = 2, RuleCs_row_list = 3, 
    RuleAny = 4, RuleColumn_name = 5
  };

  explicit BareCSParser(antlr4::TokenStream *input);

  BareCSParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~BareCSParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Bare_csContext;
  class Cs_row_formatContext;
  class HeaderContext;
  class Cs_row_listContext;
  class AnyContext;
  class Column_nameContext; 

  class  Bare_csContext : public antlr4::ParserRuleContext {
  public:
    Bare_csContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Cs_row_formatContext *> cs_row_format();
    Cs_row_formatContext* cs_row_format(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Bare_csContext* bare_cs();

  class  Cs_row_formatContext : public antlr4::ParserRuleContext {
  public:
    Cs_row_formatContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    HeaderContext *header();
    std::vector<Cs_row_listContext *> cs_row_list();
    Cs_row_listContext* cs_row_list(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cs_row_formatContext* cs_row_format();

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

  class  Cs_row_listContext : public antlr4::ParserRuleContext {
  public:
    Cs_row_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<AnyContext *> any();
    AnyContext* any(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cs_row_listContext* cs_row_list();

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

