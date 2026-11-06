
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/DianaCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  DianaCSParser : public antlr4::Parser {
public:
  enum {
    Integer = 1, Float = 2, SMCLN_COMMENT = 3, COMMENT = 4, Shifts = 5, 
    Simple_name = 6, SPACE = 7, ENCLOSE_COMMENT = 8, SECTION_COMMENT = 9, 
    LINE_COMMENT = 10, Any_name = 11, SPACE_CM = 12, RETURN_CM = 13
  };

  enum {
    RuleDiana_cs = 0, RuleComment = 1, RuleChemical_shifts = 2, RuleChemical_shift = 3, 
    RuleAtom_chemical_shift = 4
  };

  explicit DianaCSParser(antlr4::TokenStream *input);

  DianaCSParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~DianaCSParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Diana_csContext;
  class CommentContext;
  class Chemical_shiftsContext;
  class Chemical_shiftContext;
  class Atom_chemical_shiftContext; 

  class  Diana_csContext : public antlr4::ParserRuleContext {
  public:
    Diana_csContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<Chemical_shiftsContext *> chemical_shifts();
    Chemical_shiftsContext* chemical_shifts(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_csContext* diana_cs();

  class  CommentContext : public antlr4::ParserRuleContext {
  public:
    CommentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COMMENT();
    antlr4::tree::TerminalNode *RETURN_CM();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Any_name();
    antlr4::tree::TerminalNode* Any_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CommentContext* comment();

  class  Chemical_shiftsContext : public antlr4::ParserRuleContext {
  public:
    Chemical_shiftsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Chemical_shiftContext *> chemical_shift();
    Chemical_shiftContext* chemical_shift(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chemical_shiftsContext* chemical_shifts();

  class  Chemical_shiftContext : public antlr4::ParserRuleContext {
  public:
    Chemical_shiftContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Shifts();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<Atom_chemical_shiftContext *> atom_chemical_shift();
    Atom_chemical_shiftContext* atom_chemical_shift(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chemical_shiftContext* chemical_shift();

  class  Atom_chemical_shiftContext : public antlr4::ParserRuleContext {
  public:
    Atom_chemical_shiftContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_chemical_shiftContext* atom_chemical_shift();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

