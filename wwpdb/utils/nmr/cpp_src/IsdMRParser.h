
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/IsdMRParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  IsdMRParser : public antlr4::Parser {
public:
  enum {
    Distance = 1, Integer = 2, Float = 3, SHARP_COMMENT = 4, EXCLM_COMMENT = 5, 
    SMCLN_COMMENT = 6, Atom_selection = 7, SPACE = 8, ENCLOSE_COMMENT = 9, 
    SECTION_COMMENT = 10, LINE_COMMENT = 11
  };

  enum {
    RuleIsd_mr = 0, RuleDistance_restraints = 1, RuleDistance_restraint = 2
  };

  explicit IsdMRParser(antlr4::TokenStream *input);

  IsdMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~IsdMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Isd_mrContext;
  class Distance_restraintsContext;
  class Distance_restraintContext; 

  class  Isd_mrContext : public antlr4::ParserRuleContext {
  public:
    Isd_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<Distance_restraintsContext *> distance_restraints();
    Distance_restraintsContext* distance_restraints(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Isd_mrContext* isd_mr();

  class  Distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Distance();
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


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintContext* distance_restraint();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

