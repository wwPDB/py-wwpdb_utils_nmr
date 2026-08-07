
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PpmCSParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  PpmCSParser : public antlr4::Parser {
public:
  enum {
    Integer = 1, Float = 2, SHARP_COMMENT = 3, EXCLM_COMMENT = 4, Atom_selection_2d_ex = 5, 
    Atom_selection_3d_ex = 6, Simple_name = 7, SPACE = 8, RETURN = 9, SECTION_COMMENT = 10, 
    LINE_COMMENT = 11
  };

  enum {
    RulePpm_cs = 0, RulePpm_list = 1, RuleNumber = 2
  };

  explicit PpmCSParser(antlr4::TokenStream *input);

  PpmCSParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~PpmCSParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Ppm_csContext;
  class Ppm_listContext;
  class NumberContext; 

  class  Ppm_csContext : public antlr4::ParserRuleContext {
  public:
    Ppm_csContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Ppm_listContext *> ppm_list();
    Ppm_listContext* ppm_list(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ppm_csContext* ppm_cs();

  class  Ppm_listContext : public antlr4::ParserRuleContext {
  public:
    Ppm_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    NumberContext *number();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Atom_selection_2d_ex();
    antlr4::tree::TerminalNode *Atom_selection_3d_ex();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ppm_listContext* ppm_list();

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

