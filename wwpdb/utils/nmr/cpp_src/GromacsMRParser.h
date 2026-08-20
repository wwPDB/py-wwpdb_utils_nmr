
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GromacsMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  GromacsMRParser : public antlr4::Parser {
public:
  enum {
    L_brkt = 1, R_brkt = 2, Distance_restraints = 3, Dihedral_restraints = 4, 
    Orientation_restraints = 5, Angle_restraints = 6, Angle_restraints_z = 7, 
    Position_restraints = 8, Intermolecular_interactions = 9, Integer = 10, 
    Float = 11, SHARP_COMMENT = 12, EXCLM_COMMENT = 13, SMCLN_COMMENT = 14, 
    Simple_name = 15, SPACE = 16, ENCLOSE_COMMENT = 17, SECTION_COMMENT = 18, 
    LINE_COMMENT = 19
  };

  enum {
    RuleGromacs_mr = 0, RuleDistance_restraints = 1, RuleDistance_restraint = 2, 
    RuleDihedral_restraints = 3, RuleDihedral_restraint = 4, RuleOrientation_restraints = 5, 
    RuleOrientation_restraint = 6, RuleAngle_restraints = 7, RuleAngle_restraint = 8, 
    RuleAngle_restraints_z = 9, RuleAngle_restraint_z = 10, RulePosition_restraints = 11, 
    RulePosition_restraint = 12, RuleNumber = 13
  };

  explicit GromacsMRParser(antlr4::TokenStream *input);

  GromacsMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~GromacsMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Gromacs_mrContext;
  class Distance_restraintsContext;
  class Distance_restraintContext;
  class Dihedral_restraintsContext;
  class Dihedral_restraintContext;
  class Orientation_restraintsContext;
  class Orientation_restraintContext;
  class Angle_restraintsContext;
  class Angle_restraintContext;
  class Angle_restraints_zContext;
  class Angle_restraint_zContext;
  class Position_restraintsContext;
  class Position_restraintContext;
  class NumberContext; 

  class  Gromacs_mrContext : public antlr4::ParserRuleContext {
  public:
    Gromacs_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<Distance_restraintsContext *> distance_restraints();
    Distance_restraintsContext* distance_restraints(size_t i);
    std::vector<Dihedral_restraintsContext *> dihedral_restraints();
    Dihedral_restraintsContext* dihedral_restraints(size_t i);
    std::vector<Orientation_restraintsContext *> orientation_restraints();
    Orientation_restraintsContext* orientation_restraints(size_t i);
    std::vector<Angle_restraintsContext *> angle_restraints();
    Angle_restraintsContext* angle_restraints(size_t i);
    std::vector<Angle_restraints_zContext *> angle_restraints_z();
    Angle_restraints_zContext* angle_restraints_z(size_t i);
    std::vector<Position_restraintsContext *> position_restraints();
    Position_restraintsContext* position_restraints(size_t i);
    std::vector<antlr4::tree::TerminalNode *> L_brkt();
    antlr4::tree::TerminalNode* L_brkt(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Intermolecular_interactions();
    antlr4::tree::TerminalNode* Intermolecular_interactions(size_t i);
    std::vector<antlr4::tree::TerminalNode *> R_brkt();
    antlr4::tree::TerminalNode* R_brkt(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Gromacs_mrContext* gromacs_mr();

  class  Distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Distance_restraints();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Distance_restraintContext *> distance_restraint();
    Distance_restraintContext* distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintsContext* distance_restraints();

  class  Distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintContext* distance_restraint();

  class  Dihedral_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Dihedral_restraints();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Dihedral_restraintContext *> dihedral_restraint();
    Dihedral_restraintContext* dihedral_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_restraintsContext* dihedral_restraints();

  class  Dihedral_restraintContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_restraintContext* dihedral_restraint();

  class  Orientation_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Orientation_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Orientation_restraints();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Orientation_restraintContext *> orientation_restraint();
    Orientation_restraintContext* orientation_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Orientation_restraintsContext* orientation_restraints();

  class  Orientation_restraintContext : public antlr4::ParserRuleContext {
  public:
    Orientation_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Orientation_restraintContext* orientation_restraint();

  class  Angle_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Angle_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Angle_restraints();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Angle_restraintContext *> angle_restraint();
    Angle_restraintContext* angle_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_restraintsContext* angle_restraints();

  class  Angle_restraintContext : public antlr4::ParserRuleContext {
  public:
    Angle_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_restraintContext* angle_restraint();

  class  Angle_restraints_zContext : public antlr4::ParserRuleContext {
  public:
    Angle_restraints_zContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Angle_restraints_z();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Angle_restraint_zContext *> angle_restraint_z();
    Angle_restraint_zContext* angle_restraint_z(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_restraints_zContext* angle_restraints_z();

  class  Angle_restraint_zContext : public antlr4::ParserRuleContext {
  public:
    Angle_restraint_zContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_restraint_zContext* angle_restraint_z();

  class  Position_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Position_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Position_restraints();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Position_restraintContext *> position_restraint();
    Position_restraintContext* position_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Position_restraintsContext* position_restraints();

  class  Position_restraintContext : public antlr4::ParserRuleContext {
  public:
    Position_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Position_restraintContext* position_restraint();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
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

