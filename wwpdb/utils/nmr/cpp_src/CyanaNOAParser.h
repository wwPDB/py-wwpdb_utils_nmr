
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaNOAParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CyanaNOAParser : public antlr4::Parser {
public:
  enum {
    Peak = 1, From = 2, Ppm_SC = 3, Increased_from = 4, Decreased_from = 5, 
    Diagonal = 6, Out_of = 7, Assignments_used = 8, Quality = 9, Ok = 10, 
    Lone = 11, Poor = 12, Far = 13, Distance_range = 14, Violated_in = 15, 
    Structures_by = 16, Average_quality = 17, Average_number = 18, Peaks_inc_upl = 19, 
    Peaks_dec_upl = 20, Protons_used_in_less = 21, Peak_obs_dist = 22, Atom = 23, 
    Residue = 24, Peaks = 25, Shift = 26, Used = 27, Expect = 28, Selected = 29, 
    Assigned = 30, Unassigned = 31, Without_possibility = 32, With_viol_below = 33, 
    With_viol_between = 34, With_viol_above = 35, With_diagonal = 36, And = 37, 
    Cross_peaks = 38, With_off_diagonal = 39, With_unique = 40, With_short_range = 41, 
    With_medium_range = 42, With_long_range = 43, Short_range_ex = 44, Medium_range_ex = 45, 
    Long_range_ex = 46, L_paren = 47, R_paren = 48, Colon = 49, Period = 50, 
    Comma = 51, Equ_op = 52, Add_op = 53, Sub_op = 54, Div_op = 55, Angstrome = 56, 
    Integer = 57, Float = 58, Numerical_report1 = 59, Numerical_report2 = 60, 
    Numerical_report3 = 61, Numerical_report4 = 62, COMMENT = 63, Simple_name = 64, 
    SPACE = 65, ENCLOSE_COMMENT = 66, SECTION_COMMENT = 67, LINE_COMMENT = 68, 
    File_name = 69, SPACE_FN = 70, Any_name = 71, SPACE_CM = 72, RETURN_CM = 73
  };

  enum {
    RuleCyana_noa = 0, RuleComment = 1, RuleNoe_peaks = 2, RulePeak_header = 3, 
    RulePeak_quality = 4, RuleNoe_assignments = 5, RuleNoe_assignment = 6, 
    RuleNumerical_report = 7, RuleExtended_report = 8, RuleNoe_stat = 9, 
    RuleList_of_proton = 10, RulePeak_stat = 11
  };

  explicit CyanaNOAParser(antlr4::TokenStream *input);

  CyanaNOAParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~CyanaNOAParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Cyana_noaContext;
  class CommentContext;
  class Noe_peaksContext;
  class Peak_headerContext;
  class Peak_qualityContext;
  class Noe_assignmentsContext;
  class Noe_assignmentContext;
  class Numerical_reportContext;
  class Extended_reportContext;
  class Noe_statContext;
  class List_of_protonContext;
  class Peak_statContext; 

  class  Cyana_noaContext : public antlr4::ParserRuleContext {
  public:
    Cyana_noaContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<Noe_peaksContext *> noe_peaks();
    Noe_peaksContext* noe_peaks(size_t i);
    std::vector<Noe_statContext *> noe_stat();
    Noe_statContext* noe_stat(size_t i);
    std::vector<Peak_statContext *> peak_stat();
    Peak_statContext* peak_stat(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cyana_noaContext* cyana_noa();

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

  class  Noe_peaksContext : public antlr4::ParserRuleContext {
  public:
    Noe_peaksContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Peak_headerContext *peak_header();
    Peak_qualityContext *peak_quality();
    Noe_assignmentsContext *noe_assignments();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_peaksContext* noe_peaks();

  class  Peak_headerContext : public antlr4::ParserRuleContext {
  public:
    Peak_headerContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Peak();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *From();
    antlr4::tree::TerminalNode *File_name();
    antlr4::tree::TerminalNode *L_paren();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *Ppm_SC();
    antlr4::tree::TerminalNode *R_paren();
    antlr4::tree::TerminalNode *Colon();
    std::vector<antlr4::tree::TerminalNode *> Angstrome();
    antlr4::tree::TerminalNode* Angstrome(size_t i);
    antlr4::tree::TerminalNode *Diagonal();
    antlr4::tree::TerminalNode *Increased_from();
    antlr4::tree::TerminalNode *Decreased_from();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_headerContext* peak_header();

  class  Peak_qualityContext : public antlr4::ParserRuleContext {
  public:
    Peak_qualityContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Out_of();
    antlr4::tree::TerminalNode *Assignments_used();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *Quality();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Colon();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_qualityContext* peak_quality();

  class  Noe_assignmentsContext : public antlr4::ParserRuleContext {
  public:
    Noe_assignmentsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Noe_assignmentContext *> noe_assignment();
    Noe_assignmentContext* noe_assignment(size_t i);
    antlr4::tree::TerminalNode *Violated_in();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Structures_by();
    antlr4::tree::TerminalNode *Angstrome();
    antlr4::tree::TerminalNode *Period();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_assignmentsContext* noe_assignments();

  class  Noe_assignmentContext : public antlr4::ParserRuleContext {
  public:
    Noe_assignmentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    Numerical_reportContext *numerical_report();
    antlr4::tree::TerminalNode *Add_op();
    antlr4::tree::TerminalNode *Sub_op();
    antlr4::tree::TerminalNode *Ok();
    antlr4::tree::TerminalNode *Lone();
    antlr4::tree::TerminalNode *Poor();
    antlr4::tree::TerminalNode *Far();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_assignmentContext* noe_assignment();

  class  Numerical_reportContext : public antlr4::ParserRuleContext {
  public:
    Numerical_reportContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Sub_op();
    antlr4::tree::TerminalNode* Sub_op(size_t i);
    antlr4::tree::TerminalNode *Distance_range();
    Extended_reportContext *extended_report();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Numerical_reportContext* numerical_report();

  class  Extended_reportContext : public antlr4::ParserRuleContext {
  public:
    Extended_reportContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Numerical_report1();
    antlr4::tree::TerminalNode *Numerical_report2();
    antlr4::tree::TerminalNode *Numerical_report3();
    antlr4::tree::TerminalNode *Numerical_report4();
    Extended_reportContext *extended_report();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Extended_reportContext* extended_report();

  class  Noe_statContext : public antlr4::ParserRuleContext {
  public:
    Noe_statContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Average_quality();
    std::vector<antlr4::tree::TerminalNode *> Colon();
    antlr4::tree::TerminalNode* Colon(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    antlr4::tree::TerminalNode *Average_number();
    antlr4::tree::TerminalNode *Peaks_inc_upl();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Peaks_dec_upl();
    antlr4::tree::TerminalNode *Protons_used_in_less();
    antlr4::tree::TerminalNode *Peak_obs_dist();
    antlr4::tree::TerminalNode *Angstrome();
    antlr4::tree::TerminalNode *Atom();
    antlr4::tree::TerminalNode *Residue();
    antlr4::tree::TerminalNode *Shift();
    antlr4::tree::TerminalNode *Peaks();
    antlr4::tree::TerminalNode *Used();
    antlr4::tree::TerminalNode *Expect();
    std::vector<List_of_protonContext *> list_of_proton();
    List_of_protonContext* list_of_proton(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_statContext* noe_stat();

  class  List_of_protonContext : public antlr4::ParserRuleContext {
  public:
    List_of_protonContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Float();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  List_of_protonContext* list_of_proton();

  class  Peak_statContext : public antlr4::ParserRuleContext {
  public:
    Peak_statContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Peaks();
    std::vector<antlr4::tree::TerminalNode *> Colon();
    antlr4::tree::TerminalNode* Colon(size_t i);
    antlr4::tree::TerminalNode *Selected();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Assigned();
    antlr4::tree::TerminalNode *Unassigned();
    antlr4::tree::TerminalNode *With_diagonal();
    antlr4::tree::TerminalNode *Cross_peaks();
    antlr4::tree::TerminalNode *With_off_diagonal();
    antlr4::tree::TerminalNode *With_unique();
    antlr4::tree::TerminalNode *With_short_range();
    antlr4::tree::TerminalNode *Short_range_ex();
    antlr4::tree::TerminalNode *With_medium_range();
    antlr4::tree::TerminalNode *Medium_range_ex();
    antlr4::tree::TerminalNode *With_long_range();
    antlr4::tree::TerminalNode *Long_range_ex();
    antlr4::tree::TerminalNode *Without_possibility();
    antlr4::tree::TerminalNode *With_viol_below();
    std::vector<antlr4::tree::TerminalNode *> Angstrome();
    antlr4::tree::TerminalNode* Angstrome(size_t i);
    antlr4::tree::TerminalNode *With_viol_between();
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *And();
    antlr4::tree::TerminalNode *With_viol_above();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_statContext* peak_stat();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

