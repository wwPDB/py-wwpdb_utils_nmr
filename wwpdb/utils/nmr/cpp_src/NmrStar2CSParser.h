
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrStar2CSParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  NmrStar2CSParser : public antlr4::Parser {
public:
  enum {
    Loop = 1, Stop = 2, Residue_seq_code = 3, Residue_label = 4, Atom_shift_assign_ID = 5, 
    Residue_author_seq_code = 6, Atom_name = 7, Atom_type = 8, Chem_shift_value = 9, 
    Chem_shift_value_error = 10, Chem_shift_ambiguity_code = 11, Integer = 12, 
    Float = 13, SHARP_COMMENT = 14, EXCLM_COMMENT = 15, SMCLN_COMMENT = 16, 
    Simple_name = 17, Double_quote_string = 18, Single_quote_string = 19, 
    SPACE = 20, RETURN = 21, SECTION_COMMENT = 22, LINE_COMMENT = 23
  };

  enum {
    RuleNmrstar2_cs = 0, RuleSeq_loop = 1, RuleSeq_tags = 2, RuleSeq_data = 3, 
    RuleCs_loop = 4, RuleCs_tags = 5, RuleCs_data = 6, RuleAny = 7
  };

  explicit NmrStar2CSParser(antlr4::TokenStream *input);

  NmrStar2CSParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~NmrStar2CSParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Nmrstar2_csContext;
  class Seq_loopContext;
  class Seq_tagsContext;
  class Seq_dataContext;
  class Cs_loopContext;
  class Cs_tagsContext;
  class Cs_dataContext;
  class AnyContext; 

  class  Nmrstar2_csContext : public antlr4::ParserRuleContext {
  public:
    Nmrstar2_csContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Seq_loopContext *> seq_loop();
    Seq_loopContext* seq_loop(size_t i);
    std::vector<Cs_loopContext *> cs_loop();
    Cs_loopContext* cs_loop(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Nmrstar2_csContext* nmrstar2_cs();

  class  Seq_loopContext : public antlr4::ParserRuleContext {
  public:
    Seq_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Loop();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    antlr4::tree::TerminalNode *Stop();
    std::vector<Seq_tagsContext *> seq_tags();
    Seq_tagsContext* seq_tags(size_t i);
    std::vector<Seq_dataContext *> seq_data();
    Seq_dataContext* seq_data(size_t i);
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Seq_loopContext* seq_loop();

  class  Seq_tagsContext : public antlr4::ParserRuleContext {
  public:
    Seq_tagsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *Residue_seq_code();
    antlr4::tree::TerminalNode *Residue_label();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Seq_tagsContext* seq_tags();

  class  Seq_dataContext : public antlr4::ParserRuleContext {
  public:
    Seq_dataContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN();
    std::vector<AnyContext *> any();
    AnyContext* any(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Seq_dataContext* seq_data();

  class  Cs_loopContext : public antlr4::ParserRuleContext {
  public:
    Cs_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Loop();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    antlr4::tree::TerminalNode *Stop();
    std::vector<Cs_tagsContext *> cs_tags();
    Cs_tagsContext* cs_tags(size_t i);
    std::vector<Cs_dataContext *> cs_data();
    Cs_dataContext* cs_data(size_t i);
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cs_loopContext* cs_loop();

  class  Cs_tagsContext : public antlr4::ParserRuleContext {
  public:
    Cs_tagsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *Atom_shift_assign_ID();
    antlr4::tree::TerminalNode *Residue_author_seq_code();
    antlr4::tree::TerminalNode *Residue_seq_code();
    antlr4::tree::TerminalNode *Residue_label();
    antlr4::tree::TerminalNode *Atom_name();
    antlr4::tree::TerminalNode *Atom_type();
    antlr4::tree::TerminalNode *Chem_shift_value();
    antlr4::tree::TerminalNode *Chem_shift_value_error();
    antlr4::tree::TerminalNode *Chem_shift_ambiguity_code();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cs_tagsContext* cs_tags();

  class  Cs_dataContext : public antlr4::ParserRuleContext {
  public:
    Cs_dataContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN();
    std::vector<AnyContext *> any();
    AnyContext* any(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cs_dataContext* cs_data();

  class  AnyContext : public antlr4::ParserRuleContext {
  public:
    AnyContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Double_quote_string();
    antlr4::tree::TerminalNode *Single_quote_string();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  AnyContext* any();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

