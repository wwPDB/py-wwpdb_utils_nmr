
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SybylMRParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  SybylMRParser : public antlr4::Parser {
public:
  enum {
    Atom1 = 1, Atom2 = 2, Lower = 3, Upper = 4, Integer = 5, Float = 6, 
    Float_DecimalComma = 7, SHARP_COMMENT = 8, EXCLM_COMMENT = 9, SMCLN_COMMENT = 10, 
    Atom_selection = 11, SPACE = 12, ENCLOSE_COMMENT = 13, SECTION_COMMENT = 14, 
    LINE_COMMENT = 15
  };

  enum {
    RuleSybyl_mr = 0, RuleDistance_restraints = 1, RuleDistance_restraint = 2, 
    RuleNumber = 3
  };

  explicit SybylMRParser(antlr4::TokenStream *input);

  SybylMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~SybylMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Sybyl_mrContext;
  class Distance_restraintsContext;
  class Distance_restraintContext;
  class NumberContext; 

  class  Sybyl_mrContext : public antlr4::ParserRuleContext {
  public:
    Sybyl_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<Distance_restraintsContext *> distance_restraints();
    Distance_restraintsContext* distance_restraints(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Sybyl_mrContext* sybyl_mr();

  class  Distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Atom1();
    antlr4::tree::TerminalNode *Atom2();
    antlr4::tree::TerminalNode *Lower();
    antlr4::tree::TerminalNode *Upper();
    std::vector<Distance_restraintContext *> distance_restraint();
    Distance_restraintContext* distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintsContext* distance_restraints();

  class  Distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Atom_selection();
    antlr4::tree::TerminalNode* Atom_selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintContext* distance_restraint();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Float_DecimalComma();
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

