
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AriaMRParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  AriaMRParser : public antlr4::Parser {
public:
  enum {
    COMMA = 1, Integer = 2, Float = 3, Real = 4, SHARP_COMMENT = 5, EXCLM_COMMENT = 6, 
    SMCLN_COMMENT = 7, RefSpec = 8, RefPeak = 9, Id = 10, D = 11, U = 12, 
    UViol = 13, PViol = 14, Viol = 15, Reliable = 16, AType = 17, Weight = 18, 
    PlusMinus = 19, Hyphen = 20, P_code = 21, A_code = 22, C_code = 23, 
    Simple_name = 24, SPACE = 25, ENCLOSE_COMMENT = 26, SECTION_COMMENT = 27, 
    LINE_COMMENT = 28, SPACE_RS = 29, RefSpecName = 30, RETURN_RS = 31, 
    SPACE_V = 32, ViolFlag = 33, RETURN_V = 34, SPACE_R = 35, ReliableFlag = 36, 
    RETURN_R = 37, SPACE_A = 38, ATypeFlag = 39, RETURN_A = 40
  };

  enum {
    RuleAria_mr = 0, RuleDistance_restraints = 1, RuleDistance_restraint = 2, 
    RuleContribution = 3, RuleAtom_pair = 4, RuleAtom_selection = 5, RuleOld_distance_restraints = 6, 
    RuleOld_distance_restraint = 7, RuleP_row = 8, RuleA_row = 9, RuleC_row = 10, 
    RuleNumber = 11, RuleNumber_c = 12
  };

  explicit AriaMRParser(antlr4::TokenStream *input);

  AriaMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~AriaMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Aria_mrContext;
  class Distance_restraintsContext;
  class Distance_restraintContext;
  class ContributionContext;
  class Atom_pairContext;
  class Atom_selectionContext;
  class Old_distance_restraintsContext;
  class Old_distance_restraintContext;
  class P_rowContext;
  class A_rowContext;
  class C_rowContext;
  class NumberContext;
  class Number_cContext; 

  class  Aria_mrContext : public antlr4::ParserRuleContext {
  public:
    Aria_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<Distance_restraintsContext *> distance_restraints();
    Distance_restraintsContext* distance_restraints(size_t i);
    std::vector<Old_distance_restraintsContext *> old_distance_restraints();
    Old_distance_restraintsContext* old_distance_restraints(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Aria_mrContext* aria_mr();

  class  Distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Distance_restraintContext *> distance_restraint();
    Distance_restraintContext* distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintsContext* distance_restraints();

  class  Distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RefSpec();
    antlr4::tree::TerminalNode *RefSpecName();
    antlr4::tree::TerminalNode *RefPeak();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Id();
    antlr4::tree::TerminalNode *D();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *U();
    antlr4::tree::TerminalNode *UViol();
    antlr4::tree::TerminalNode *PViol();
    antlr4::tree::TerminalNode *Viol();
    antlr4::tree::TerminalNode *ViolFlag();
    antlr4::tree::TerminalNode *Reliable();
    antlr4::tree::TerminalNode *ReliableFlag();
    antlr4::tree::TerminalNode *AType();
    antlr4::tree::TerminalNode *ATypeFlag();
    std::vector<ContributionContext *> contribution();
    ContributionContext* contribution(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintContext* distance_restraint();

  class  ContributionContext : public antlr4::ParserRuleContext {
  public:
    ContributionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Atom_pairContext *atom_pair();
    antlr4::tree::TerminalNode *D();
    std::vector<Number_cContext *> number_c();
    Number_cContext* number_c(size_t i);
    antlr4::tree::TerminalNode *PlusMinus();
    antlr4::tree::TerminalNode *Weight();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ContributionContext* contribution();

  class  Atom_pairContext : public antlr4::ParserRuleContext {
  public:
    Atom_pairContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Atom_selectionContext *> atom_selection();
    Atom_selectionContext* atom_selection(size_t i);
    antlr4::tree::TerminalNode *Hyphen();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_pairContext* atom_pair();

  class  Atom_selectionContext : public antlr4::ParserRuleContext {
  public:
    Atom_selectionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_selectionContext* atom_selection();

  class  Old_distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Old_distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Old_distance_restraintContext *> old_distance_restraint();
    Old_distance_restraintContext* old_distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Old_distance_restraintsContext* old_distance_restraints();

  class  Old_distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Old_distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    P_rowContext *p_row();
    A_rowContext *a_row();
    std::vector<C_rowContext *> c_row();
    C_rowContext* c_row(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Old_distance_restraintContext* old_distance_restraint();

  class  P_rowContext : public antlr4::ParserRuleContext {
  public:
    P_rowContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *P_code();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    antlr4::tree::TerminalNode *Real();
    std::vector<antlr4::tree::TerminalNode *> Hyphen();
    antlr4::tree::TerminalNode* Hyphen(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  P_rowContext* p_row();

  class  A_rowContext : public antlr4::ParserRuleContext {
  public:
    A_rowContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *A_code();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  A_rowContext* a_row();

  class  C_rowContext : public antlr4::ParserRuleContext {
  public:
    C_rowContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *C_code();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Hyphen();
    antlr4::tree::TerminalNode* Hyphen(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  C_rowContext* c_row();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  Number_cContext : public antlr4::ParserRuleContext {
  public:
    Number_cContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Number_cContext* number_c();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

