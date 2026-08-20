
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrPipeCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  NmrPipeCSParser : public antlr4::Parser {
public:
  enum {
    Data = 1, Vars = 2, Format = 3, Integer = 4, Float = 5, Float_DecimalComma = 6, 
    SHARP_COMMENT = 7, EXCLM_COMMENT = 8, SMCLN_COMMENT = 9, Simple_name = 10, 
    SPACE = 11, ENCLOSE_COMMENT = 12, SECTION_COMMENT = 13, LINE_COMMENT = 14, 
    First_resid = 15, Sequence = 16, Db_name = 17, Tab_name = 18, Tab_id = 19, 
    Integer_DA = 20, Simple_name_DA = 21, SPACE_DA = 22, RETURN_DA = 23, 
    LINE_COMMENT_DA = 24, One_letter_code = 25, SPACE_SQ = 26, RETURN_SQ = 27, 
    LINE_COMMENT_SQ = 28, Segname = 29, Resid = 30, Resname = 31, Atomname = 32, 
    Shift = 33, SPACE_VA = 34, RETURN_VA = 35, LINE_COMMENT_VA = 36, Format_code = 37, 
    SPACE_FO = 38, RETURN_FO = 39, LINE_COMMENT_FO = 40
  };

  enum {
    RuleNmrpipe_cs = 0, RuleSequence = 1, RuleChemical_shifts = 2, RuleChemical_shift = 3, 
    RuleChemical_shifts_sw_segid = 4, RuleChemical_shift_sw_segid = 5, RuleChemical_shifts_ew_segid = 6, 
    RuleChemical_shift_ew_segid = 7, RuleNumber = 8
  };

  explicit NmrPipeCSParser(antlr4::TokenStream *input);

  NmrPipeCSParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~NmrPipeCSParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Nmrpipe_csContext;
  class SequenceContext;
  class Chemical_shiftsContext;
  class Chemical_shiftContext;
  class Chemical_shifts_sw_segidContext;
  class Chemical_shift_sw_segidContext;
  class Chemical_shifts_ew_segidContext;
  class Chemical_shift_ew_segidContext;
  class NumberContext; 

  class  Nmrpipe_csContext : public antlr4::ParserRuleContext {
  public:
    Nmrpipe_csContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<SequenceContext *> sequence();
    SequenceContext* sequence(size_t i);
    std::vector<Chemical_shiftsContext *> chemical_shifts();
    Chemical_shiftsContext* chemical_shifts(size_t i);
    std::vector<Chemical_shifts_sw_segidContext *> chemical_shifts_sw_segid();
    Chemical_shifts_sw_segidContext* chemical_shifts_sw_segid(size_t i);
    std::vector<Chemical_shifts_ew_segidContext *> chemical_shifts_ew_segid();
    Chemical_shifts_ew_segidContext* chemical_shifts_ew_segid(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Nmrpipe_csContext* nmrpipe_cs();

  class  SequenceContext : public antlr4::ParserRuleContext {
  public:
    SequenceContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Data();
    antlr4::tree::TerminalNode *First_resid();
    antlr4::tree::TerminalNode *Integer_DA();
    antlr4::tree::TerminalNode *RETURN_DA();
    antlr4::tree::TerminalNode *Sequence();
    antlr4::tree::TerminalNode *RETURN_SQ();
    antlr4::tree::TerminalNode *Db_name();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_DA();
    antlr4::tree::TerminalNode* Simple_name_DA(size_t i);
    antlr4::tree::TerminalNode *Tab_name();
    antlr4::tree::TerminalNode *Tab_id();
    std::vector<antlr4::tree::TerminalNode *> One_letter_code();
    antlr4::tree::TerminalNode* One_letter_code(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  SequenceContext* sequence();

  class  Chemical_shiftsContext : public antlr4::ParserRuleContext {
  public:
    Chemical_shiftsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Resid();
    antlr4::tree::TerminalNode *Resname();
    antlr4::tree::TerminalNode *Atomname();
    antlr4::tree::TerminalNode *Shift();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Chemical_shiftContext *> chemical_shift();
    Chemical_shiftContext* chemical_shift(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chemical_shiftsContext* chemical_shifts();

  class  Chemical_shiftContext : public antlr4::ParserRuleContext {
  public:
    Chemical_shiftContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    NumberContext *number();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chemical_shiftContext* chemical_shift();

  class  Chemical_shifts_sw_segidContext : public antlr4::ParserRuleContext {
  public:
    Chemical_shifts_sw_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Segname();
    antlr4::tree::TerminalNode *Resid();
    antlr4::tree::TerminalNode *Resname();
    antlr4::tree::TerminalNode *Atomname();
    antlr4::tree::TerminalNode *Shift();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Chemical_shift_sw_segidContext *> chemical_shift_sw_segid();
    Chemical_shift_sw_segidContext* chemical_shift_sw_segid(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chemical_shifts_sw_segidContext* chemical_shifts_sw_segid();

  class  Chemical_shift_sw_segidContext : public antlr4::ParserRuleContext {
  public:
    Chemical_shift_sw_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *Integer();
    NumberContext *number();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chemical_shift_sw_segidContext* chemical_shift_sw_segid();

  class  Chemical_shifts_ew_segidContext : public antlr4::ParserRuleContext {
  public:
    Chemical_shifts_ew_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Resid();
    antlr4::tree::TerminalNode *Resname();
    antlr4::tree::TerminalNode *Atomname();
    antlr4::tree::TerminalNode *Segname();
    antlr4::tree::TerminalNode *Shift();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Chemical_shift_ew_segidContext *> chemical_shift_ew_segid();
    Chemical_shift_ew_segidContext* chemical_shift_ew_segid(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chemical_shifts_ew_segidContext* chemical_shifts_ew_segid();

  class  Chemical_shift_ew_segidContext : public antlr4::ParserRuleContext {
  public:
    Chemical_shift_ew_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    NumberContext *number();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chemical_shift_ew_segidContext* chemical_shift_ew_segid();

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

