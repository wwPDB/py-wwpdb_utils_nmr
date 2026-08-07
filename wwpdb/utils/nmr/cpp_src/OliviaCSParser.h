
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/OliviaCSParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  OliviaCSParser : public antlr4::Parser {
public:
  enum {
    Typedef = 1, Separator = 2, Format = 3, Unformat = 4, Eof = 5, Null_string = 6, 
    Integer = 7, Float = 8, Real = 9, COMMENT = 10, SHARP_COMMENT = 11, 
    EXCLM_COMMENT = 12, Simple_name = 13, SPACE = 14, RETURN = 15, SECTION_COMMENT = 16, 
    LINE_COMMENT = 17, Sequence = 18, Ass_tbl_h2o = 19, Ass_tbl_tro = 20, 
    Ass_tbl_d2o = 21, SPACE_TD = 22, RETURN_TD = 23, Tab = 24, Comma = 25, 
    Space = 26, SPACE_SE = 27, RETURN_SE = 28, Chain = 29, Resname = 30, 
    Seqnum = 31, Atomname = 32, Shift = 33, Stddev = 34, SPACE_FO = 35, 
    RETURN_FO = 36, Printf_string = 37, SPACE_PF = 38, RETURN_PF = 39, Any_name = 40, 
    SPACE_CM = 41, RETURN_CM = 42
  };

  enum {
    RuleOlivia_cs = 0, RuleSequence = 1, RuleResidue = 2, RuleChemical_shifts = 3, 
    RuleChemical_shift = 4, RuleNumber = 5, RuleComment = 6
  };

  explicit OliviaCSParser(antlr4::TokenStream *input);

  OliviaCSParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~OliviaCSParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Olivia_csContext;
  class SequenceContext;
  class ResidueContext;
  class Chemical_shiftsContext;
  class Chemical_shiftContext;
  class NumberContext;
  class CommentContext; 

  class  Olivia_csContext : public antlr4::ParserRuleContext {
  public:
    Olivia_csContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<SequenceContext *> sequence();
    SequenceContext* sequence(size_t i);
    std::vector<Chemical_shiftsContext *> chemical_shifts();
    Chemical_shiftsContext* chemical_shifts(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Olivia_csContext* olivia_cs();

  class  SequenceContext : public antlr4::ParserRuleContext {
  public:
    SequenceContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Typedef();
    antlr4::tree::TerminalNode *Sequence();
    antlr4::tree::TerminalNode *RETURN_TD();
    antlr4::tree::TerminalNode *Separator();
    antlr4::tree::TerminalNode *RETURN_SE();
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *Chain();
    antlr4::tree::TerminalNode *Resname();
    antlr4::tree::TerminalNode *Seqnum();
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<antlr4::tree::TerminalNode *> Printf_string();
    antlr4::tree::TerminalNode* Printf_string(size_t i);
    antlr4::tree::TerminalNode *RETURN_PF();
    antlr4::tree::TerminalNode *Unformat();
    antlr4::tree::TerminalNode *Tab();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *Space();
    std::vector<ResidueContext *> residue();
    ResidueContext* residue(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  SequenceContext* sequence();

  class  ResidueContext : public antlr4::ParserRuleContext {
  public:
    ResidueContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *RETURN();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ResidueContext* residue();

  class  Chemical_shiftsContext : public antlr4::ParserRuleContext {
  public:
    Chemical_shiftsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Typedef();
    antlr4::tree::TerminalNode *RETURN_TD();
    antlr4::tree::TerminalNode *Separator();
    antlr4::tree::TerminalNode *RETURN_SE();
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *Chain();
    antlr4::tree::TerminalNode *Resname();
    antlr4::tree::TerminalNode *Seqnum();
    antlr4::tree::TerminalNode *Atomname();
    antlr4::tree::TerminalNode *Shift();
    antlr4::tree::TerminalNode *Stddev();
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<antlr4::tree::TerminalNode *> Printf_string();
    antlr4::tree::TerminalNode* Printf_string(size_t i);
    antlr4::tree::TerminalNode *RETURN_PF();
    antlr4::tree::TerminalNode *Unformat();
    antlr4::tree::TerminalNode *Ass_tbl_h2o();
    antlr4::tree::TerminalNode *Ass_tbl_tro();
    antlr4::tree::TerminalNode *Ass_tbl_d2o();
    antlr4::tree::TerminalNode *Tab();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *Space();
    std::vector<Chemical_shiftContext *> chemical_shift();
    Chemical_shiftContext* chemical_shift(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chemical_shiftsContext* chemical_shifts();

  class  Chemical_shiftContext : public antlr4::ParserRuleContext {
  public:
    Chemical_shiftContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *Integer();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chemical_shiftContext* chemical_shift();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Real();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  CommentContext : public antlr4::ParserRuleContext {
  public:
    CommentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COMMENT();
    antlr4::tree::TerminalNode *RETURN_CM();
    std::vector<antlr4::tree::TerminalNode *> Any_name();
    antlr4::tree::TerminalNode* Any_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CommentContext* comment();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

