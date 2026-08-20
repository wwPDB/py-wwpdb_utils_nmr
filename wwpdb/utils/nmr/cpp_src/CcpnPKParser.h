
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CcpnPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CcpnPKParser : public antlr4::Parser {
public:
  enum {
    Num = 1, Id = 2, Assign_F1 = 3, Position_F1 = 4, Shift_F1 = 5, Integer = 6, 
    Float = 7, Real = 8, EXCLM_COMMENT = 9, SMCLN_COMMENT = 10, Simple_name = 11, 
    Any_name = 12, SPACE = 13, RETURN = 14, SECTION_COMMENT = 15, LINE_COMMENT = 16, 
    Id_ = 17, Position_F1_ = 18, Position_F2 = 19, Position_F3 = 20, Position_F4 = 21, 
    Shift_F1_ = 22, Shift_F2 = 23, Shift_F3 = 24, Shift_F4 = 25, Assign_F1_ = 26, 
    Assign_F2 = 27, Assign_F3 = 28, Assign_F4 = 29, Height = 30, Volume = 31, 
    Line_width_F1 = 32, Line_width_F2 = 33, Line_width_F3 = 34, Line_width_F4 = 35, 
    Merit = 36, Details = 37, Fit_method = 38, Vol_method = 39, SPACE_VARS = 40, 
    RETURN_VARS = 41
  };

  enum {
    RuleCcpn_pk = 0, RulePeak_list_2d = 1, RulePeak_2d = 2, RulePeak_list_3d = 3, 
    RulePeak_3d = 4, RulePeak_list_4d = 5, RulePeak_4d = 6, RulePeak_list_wo_assign_2d = 7, 
    RulePeak_wo_assign_2d = 8, RulePeak_list_wo_assign_3d = 9, RulePeak_wo_assign_3d = 10, 
    RulePeak_list_wo_assign_4d = 11, RulePeak_wo_assign_4d = 12, RulePosition = 13, 
    RuleNumber = 14, RuleNote = 15
  };

  explicit CcpnPKParser(antlr4::TokenStream *input);

  CcpnPKParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~CcpnPKParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Ccpn_pkContext;
  class Peak_list_2dContext;
  class Peak_2dContext;
  class Peak_list_3dContext;
  class Peak_3dContext;
  class Peak_list_4dContext;
  class Peak_4dContext;
  class Peak_list_wo_assign_2dContext;
  class Peak_wo_assign_2dContext;
  class Peak_list_wo_assign_3dContext;
  class Peak_wo_assign_3dContext;
  class Peak_list_wo_assign_4dContext;
  class Peak_wo_assign_4dContext;
  class PositionContext;
  class NumberContext;
  class NoteContext; 

  class  Ccpn_pkContext : public antlr4::ParserRuleContext {
  public:
    Ccpn_pkContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Peak_list_2dContext *> peak_list_2d();
    Peak_list_2dContext* peak_list_2d(size_t i);
    std::vector<Peak_list_3dContext *> peak_list_3d();
    Peak_list_3dContext* peak_list_3d(size_t i);
    std::vector<Peak_list_4dContext *> peak_list_4d();
    Peak_list_4dContext* peak_list_4d(size_t i);
    std::vector<Peak_list_wo_assign_2dContext *> peak_list_wo_assign_2d();
    Peak_list_wo_assign_2dContext* peak_list_wo_assign_2d(size_t i);
    std::vector<Peak_list_wo_assign_3dContext *> peak_list_wo_assign_3d();
    Peak_list_wo_assign_3dContext* peak_list_wo_assign_3d(size_t i);
    std::vector<Peak_list_wo_assign_4dContext *> peak_list_wo_assign_4d();
    Peak_list_wo_assign_4dContext* peak_list_wo_assign_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ccpn_pkContext* ccpn_pk();

  class  Peak_list_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN_VARS();
    antlr4::tree::TerminalNode *Num();
    antlr4::tree::TerminalNode *Height();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Line_width_F1();
    antlr4::tree::TerminalNode *Line_width_F2();
    antlr4::tree::TerminalNode *Merit();
    antlr4::tree::TerminalNode *Details();
    antlr4::tree::TerminalNode *Fit_method();
    antlr4::tree::TerminalNode *Vol_method();
    std::vector<Peak_2dContext *> peak_2d();
    Peak_2dContext* peak_2d(size_t i);
    antlr4::tree::TerminalNode *Id();
    antlr4::tree::TerminalNode *Id_();
    antlr4::tree::TerminalNode *Assign_F1_();
    antlr4::tree::TerminalNode *Assign_F2();
    antlr4::tree::TerminalNode *Position_F1();
    antlr4::tree::TerminalNode *Shift_F1();
    antlr4::tree::TerminalNode *Position_F1_();
    antlr4::tree::TerminalNode *Shift_F1_();
    antlr4::tree::TerminalNode *Position_F2();
    antlr4::tree::TerminalNode *Shift_F2();
    antlr4::tree::TerminalNode *Assign_F1();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_2dContext* peak_list_2d();

  class  Peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    std::vector<NoteContext *> note();
    NoteContext* note(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_2dContext* peak_2d();

  class  Peak_list_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN_VARS();
    antlr4::tree::TerminalNode *Num();
    antlr4::tree::TerminalNode *Height();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Line_width_F1();
    antlr4::tree::TerminalNode *Line_width_F2();
    antlr4::tree::TerminalNode *Line_width_F3();
    antlr4::tree::TerminalNode *Merit();
    antlr4::tree::TerminalNode *Details();
    antlr4::tree::TerminalNode *Fit_method();
    antlr4::tree::TerminalNode *Vol_method();
    std::vector<Peak_3dContext *> peak_3d();
    Peak_3dContext* peak_3d(size_t i);
    antlr4::tree::TerminalNode *Id();
    antlr4::tree::TerminalNode *Id_();
    antlr4::tree::TerminalNode *Assign_F1_();
    antlr4::tree::TerminalNode *Assign_F2();
    antlr4::tree::TerminalNode *Assign_F3();
    antlr4::tree::TerminalNode *Position_F1();
    antlr4::tree::TerminalNode *Shift_F1();
    antlr4::tree::TerminalNode *Position_F1_();
    antlr4::tree::TerminalNode *Shift_F1_();
    antlr4::tree::TerminalNode *Position_F2();
    antlr4::tree::TerminalNode *Shift_F2();
    antlr4::tree::TerminalNode *Position_F3();
    antlr4::tree::TerminalNode *Shift_F3();
    antlr4::tree::TerminalNode *Assign_F1();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_3dContext* peak_list_3d();

  class  Peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    std::vector<NoteContext *> note();
    NoteContext* note(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_3dContext* peak_3d();

  class  Peak_list_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN_VARS();
    antlr4::tree::TerminalNode *Num();
    antlr4::tree::TerminalNode *Height();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Line_width_F1();
    antlr4::tree::TerminalNode *Line_width_F2();
    antlr4::tree::TerminalNode *Line_width_F3();
    antlr4::tree::TerminalNode *Line_width_F4();
    antlr4::tree::TerminalNode *Merit();
    antlr4::tree::TerminalNode *Details();
    antlr4::tree::TerminalNode *Fit_method();
    antlr4::tree::TerminalNode *Vol_method();
    std::vector<Peak_4dContext *> peak_4d();
    Peak_4dContext* peak_4d(size_t i);
    antlr4::tree::TerminalNode *Id();
    antlr4::tree::TerminalNode *Id_();
    antlr4::tree::TerminalNode *Assign_F1_();
    antlr4::tree::TerminalNode *Assign_F2();
    antlr4::tree::TerminalNode *Assign_F3();
    antlr4::tree::TerminalNode *Assign_F4();
    antlr4::tree::TerminalNode *Position_F1();
    antlr4::tree::TerminalNode *Shift_F1();
    antlr4::tree::TerminalNode *Position_F1_();
    antlr4::tree::TerminalNode *Shift_F1_();
    antlr4::tree::TerminalNode *Position_F2();
    antlr4::tree::TerminalNode *Shift_F2();
    antlr4::tree::TerminalNode *Position_F3();
    antlr4::tree::TerminalNode *Shift_F3();
    antlr4::tree::TerminalNode *Position_F4();
    antlr4::tree::TerminalNode *Shift_F4();
    antlr4::tree::TerminalNode *Assign_F1();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_4dContext* peak_list_4d();

  class  Peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    std::vector<NoteContext *> note();
    NoteContext* note(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_4dContext* peak_4d();

  class  Peak_list_wo_assign_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_wo_assign_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN_VARS();
    antlr4::tree::TerminalNode *Position_F1();
    antlr4::tree::TerminalNode *Shift_F1();
    antlr4::tree::TerminalNode *Position_F1_();
    antlr4::tree::TerminalNode *Shift_F1_();
    antlr4::tree::TerminalNode *Position_F2();
    antlr4::tree::TerminalNode *Shift_F2();
    antlr4::tree::TerminalNode *Num();
    antlr4::tree::TerminalNode *Height();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Line_width_F1();
    antlr4::tree::TerminalNode *Line_width_F2();
    antlr4::tree::TerminalNode *Merit();
    antlr4::tree::TerminalNode *Details();
    antlr4::tree::TerminalNode *Fit_method();
    antlr4::tree::TerminalNode *Vol_method();
    std::vector<Peak_wo_assign_2dContext *> peak_wo_assign_2d();
    Peak_wo_assign_2dContext* peak_wo_assign_2d(size_t i);
    antlr4::tree::TerminalNode *Id();
    antlr4::tree::TerminalNode *Id_();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_wo_assign_2dContext* peak_list_wo_assign_2d();

  class  Peak_wo_assign_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_wo_assign_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<NoteContext *> note();
    NoteContext* note(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_wo_assign_2dContext* peak_wo_assign_2d();

  class  Peak_list_wo_assign_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_wo_assign_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN_VARS();
    antlr4::tree::TerminalNode *Position_F1();
    antlr4::tree::TerminalNode *Shift_F1();
    antlr4::tree::TerminalNode *Position_F1_();
    antlr4::tree::TerminalNode *Shift_F1_();
    antlr4::tree::TerminalNode *Position_F2();
    antlr4::tree::TerminalNode *Shift_F2();
    antlr4::tree::TerminalNode *Position_F3();
    antlr4::tree::TerminalNode *Shift_F3();
    antlr4::tree::TerminalNode *Num();
    antlr4::tree::TerminalNode *Height();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Line_width_F1();
    antlr4::tree::TerminalNode *Line_width_F2();
    antlr4::tree::TerminalNode *Line_width_F3();
    antlr4::tree::TerminalNode *Merit();
    antlr4::tree::TerminalNode *Details();
    antlr4::tree::TerminalNode *Fit_method();
    antlr4::tree::TerminalNode *Vol_method();
    std::vector<Peak_wo_assign_3dContext *> peak_wo_assign_3d();
    Peak_wo_assign_3dContext* peak_wo_assign_3d(size_t i);
    antlr4::tree::TerminalNode *Id();
    antlr4::tree::TerminalNode *Id_();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_wo_assign_3dContext* peak_list_wo_assign_3d();

  class  Peak_wo_assign_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_wo_assign_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<NoteContext *> note();
    NoteContext* note(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_wo_assign_3dContext* peak_wo_assign_3d();

  class  Peak_list_wo_assign_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_wo_assign_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN_VARS();
    antlr4::tree::TerminalNode *Position_F1();
    antlr4::tree::TerminalNode *Shift_F1();
    antlr4::tree::TerminalNode *Position_F1_();
    antlr4::tree::TerminalNode *Shift_F1_();
    antlr4::tree::TerminalNode *Position_F2();
    antlr4::tree::TerminalNode *Shift_F2();
    antlr4::tree::TerminalNode *Position_F3();
    antlr4::tree::TerminalNode *Shift_F3();
    antlr4::tree::TerminalNode *Position_F4();
    antlr4::tree::TerminalNode *Shift_F4();
    antlr4::tree::TerminalNode *Num();
    antlr4::tree::TerminalNode *Height();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Line_width_F1();
    antlr4::tree::TerminalNode *Line_width_F2();
    antlr4::tree::TerminalNode *Line_width_F3();
    antlr4::tree::TerminalNode *Line_width_F4();
    antlr4::tree::TerminalNode *Merit();
    antlr4::tree::TerminalNode *Details();
    antlr4::tree::TerminalNode *Fit_method();
    antlr4::tree::TerminalNode *Vol_method();
    std::vector<Peak_wo_assign_4dContext *> peak_wo_assign_4d();
    Peak_wo_assign_4dContext* peak_wo_assign_4d(size_t i);
    antlr4::tree::TerminalNode *Id();
    antlr4::tree::TerminalNode *Id_();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_wo_assign_4dContext* peak_list_wo_assign_4d();

  class  Peak_wo_assign_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_wo_assign_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<PositionContext *> position();
    PositionContext* position(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<NoteContext *> note();
    NoteContext* note(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_wo_assign_4dContext* peak_wo_assign_4d();

  class  PositionContext : public antlr4::ParserRuleContext {
  public:
    PositionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  PositionContext* position();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  NoteContext : public antlr4::ParserRuleContext {
  public:
    NoteContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Any_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NoteContext* note();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

