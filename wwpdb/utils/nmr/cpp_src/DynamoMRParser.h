
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/DynamoMRParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  DynamoMRParser : public antlr4::Parser {
public:
  enum {
    Data = 1, Vars = 2, Format = 3, Integer = 4, Float = 5, Float_DecimalComma = 6, 
    SHARP_COMMENT = 7, EXCLM_COMMENT = 8, SMCLN_COMMENT = 9, Simple_name = 10, 
    SPACE = 11, ENCLOSE_COMMENT = 12, SECTION_COMMENT = 13, LINE_COMMENT = 14, 
    First_resid = 15, Sequence = 16, Db_name = 17, Tab_name = 18, Tab_id = 19, 
    Pales_mode = 20, Tensor_mode = 21, Saupe_matrix = 22, S_DA = 23, Saupe = 24, 
    Irreducible_rep = 25, Irreducible = 26, General_magnitude = 27, Mapping_corr = 28, 
    Mapping = 29, Inv = 30, Eigenvalues = 31, Eigenvectors = 32, X_axis = 33, 
    Y_axis = 34, Z_axis = 35, Q_euler_solutions = 36, Q_euler_angles = 37, 
    Euler_solutions = 38, Euler_angles = 39, Da = 40, Dr = 41, Aa = 42, 
    Ar = 43, Da_hn = 44, Rhombicity = 45, N = 46, Rms = 47, Chi2 = 48, Corr = 49, 
    R = 50, Q = 51, Regression = 52, Offset = 53, Slope = 54, Bax = 55, 
    Plus_minus = 56, Hz = 57, Comma_DA = 58, L_paren_DA = 59, R_paren_DA = 60, 
    L_brkt_DA = 61, R_brkt_DA = 62, Integer_DA = 63, Float_DA = 64, Real_DA = 65, 
    Simple_name_DA = 66, SPACE_DA = 67, RETURN_DA = 68, LINE_COMMENT_DA = 69, 
    One_letter_code = 70, SPACE_SQ = 71, RETURN_SQ = 72, LINE_COMMENT_SQ = 73, 
    Index = 74, Group = 75, Segname_I = 76, Resid_I = 77, Resname_I = 78, 
    Atomname_I = 79, Segname_J = 80, Resid_J = 81, Resname_J = 82, Atomname_J = 83, 
    Segname_K = 84, Resid_K = 85, Resname_K = 86, Atomname_K = 87, Segname_L = 88, 
    Resid_L = 89, Resname_L = 90, Atomname_L = 91, Resid = 92, Resname = 93, 
    A = 94, B = 95, C = 96, D = 97, DD = 98, DI = 99, D_diff = 100, D_obs = 101, 
    FC = 102, S = 103, W = 104, D_Lo = 105, D_Hi = 106, Angle_Lo = 107, 
    Angle_Hi = 108, Phase = 109, ObsJ = 110, Phi = 111, Psi = 112, Dphi = 113, 
    Dpsi = 114, Dist = 115, S2 = 116, Count = 117, Cs_count = 118, Class = 119, 
    SPACE_VA = 120, RETURN_VA = 121, LINE_COMMENT_VA = 122, Format_code = 123, 
    SPACE_FO = 124, RETURN_FO = 125, LINE_COMMENT_FO = 126
  };

  enum {
    RuleDynamo_mr = 0, RuleSequence = 1, RuleDistance_restraints = 2, RuleDistance_restraint = 3, 
    RuleDistance_restraints_sw_segid = 4, RuleDistance_restraint_sw_segid = 5, 
    RuleDistance_restraints_ew_segid = 6, RuleDistance_restraint_ew_segid = 7, 
    RuleTorsion_angle_restraints = 8, RuleTorsion_angle_restraint = 9, RuleTorsion_angle_restraints_sw_segid = 10, 
    RuleTorsion_angle_restraint_sw_segid = 11, RuleTorsion_angle_restraints_ew_segid = 12, 
    RuleTorsion_angle_restraint_ew_segid = 13, RuleRdc_restraints = 14, 
    RuleRdc_restraint = 15, RuleRdc_restraints_sw_segid = 16, RuleRdc_restraint_sw_segid = 17, 
    RuleRdc_restraints_ew_segid = 18, RuleRdc_restraint_ew_segid = 19, RulePales_meta_outputs = 20, 
    RulePales_rdc_outputs = 21, RulePales_rdc_output = 22, RuleCoupling_restraints = 23, 
    RuleCoupling_restraint = 24, RuleCoupling_restraints_sw_segid = 25, 
    RuleCoupling_restraint_sw_segid = 26, RuleCoupling_restraints_ew_segid = 27, 
    RuleCoupling_restraint_ew_segid = 28, RuleTalos_restraints = 29, RuleTalos_restraint = 30, 
    RuleTalos_restraints_wo_s2 = 31, RuleTalos_restraint_wo_s2 = 32, RuleNumber = 33
  };

  explicit DynamoMRParser(antlr4::TokenStream *input);

  DynamoMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~DynamoMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Dynamo_mrContext;
  class SequenceContext;
  class Distance_restraintsContext;
  class Distance_restraintContext;
  class Distance_restraints_sw_segidContext;
  class Distance_restraint_sw_segidContext;
  class Distance_restraints_ew_segidContext;
  class Distance_restraint_ew_segidContext;
  class Torsion_angle_restraintsContext;
  class Torsion_angle_restraintContext;
  class Torsion_angle_restraints_sw_segidContext;
  class Torsion_angle_restraint_sw_segidContext;
  class Torsion_angle_restraints_ew_segidContext;
  class Torsion_angle_restraint_ew_segidContext;
  class Rdc_restraintsContext;
  class Rdc_restraintContext;
  class Rdc_restraints_sw_segidContext;
  class Rdc_restraint_sw_segidContext;
  class Rdc_restraints_ew_segidContext;
  class Rdc_restraint_ew_segidContext;
  class Pales_meta_outputsContext;
  class Pales_rdc_outputsContext;
  class Pales_rdc_outputContext;
  class Coupling_restraintsContext;
  class Coupling_restraintContext;
  class Coupling_restraints_sw_segidContext;
  class Coupling_restraint_sw_segidContext;
  class Coupling_restraints_ew_segidContext;
  class Coupling_restraint_ew_segidContext;
  class Talos_restraintsContext;
  class Talos_restraintContext;
  class Talos_restraints_wo_s2Context;
  class Talos_restraint_wo_s2Context;
  class NumberContext; 

  class  Dynamo_mrContext : public antlr4::ParserRuleContext {
  public:
    Dynamo_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<SequenceContext *> sequence();
    SequenceContext* sequence(size_t i);
    std::vector<Distance_restraintsContext *> distance_restraints();
    Distance_restraintsContext* distance_restraints(size_t i);
    std::vector<Distance_restraints_sw_segidContext *> distance_restraints_sw_segid();
    Distance_restraints_sw_segidContext* distance_restraints_sw_segid(size_t i);
    std::vector<Distance_restraints_ew_segidContext *> distance_restraints_ew_segid();
    Distance_restraints_ew_segidContext* distance_restraints_ew_segid(size_t i);
    std::vector<Torsion_angle_restraintsContext *> torsion_angle_restraints();
    Torsion_angle_restraintsContext* torsion_angle_restraints(size_t i);
    std::vector<Torsion_angle_restraints_sw_segidContext *> torsion_angle_restraints_sw_segid();
    Torsion_angle_restraints_sw_segidContext* torsion_angle_restraints_sw_segid(size_t i);
    std::vector<Torsion_angle_restraints_ew_segidContext *> torsion_angle_restraints_ew_segid();
    Torsion_angle_restraints_ew_segidContext* torsion_angle_restraints_ew_segid(size_t i);
    std::vector<Rdc_restraintsContext *> rdc_restraints();
    Rdc_restraintsContext* rdc_restraints(size_t i);
    std::vector<Rdc_restraints_sw_segidContext *> rdc_restraints_sw_segid();
    Rdc_restraints_sw_segidContext* rdc_restraints_sw_segid(size_t i);
    std::vector<Rdc_restraints_ew_segidContext *> rdc_restraints_ew_segid();
    Rdc_restraints_ew_segidContext* rdc_restraints_ew_segid(size_t i);
    std::vector<Pales_meta_outputsContext *> pales_meta_outputs();
    Pales_meta_outputsContext* pales_meta_outputs(size_t i);
    std::vector<Pales_rdc_outputsContext *> pales_rdc_outputs();
    Pales_rdc_outputsContext* pales_rdc_outputs(size_t i);
    std::vector<Coupling_restraintsContext *> coupling_restraints();
    Coupling_restraintsContext* coupling_restraints(size_t i);
    std::vector<Coupling_restraints_sw_segidContext *> coupling_restraints_sw_segid();
    Coupling_restraints_sw_segidContext* coupling_restraints_sw_segid(size_t i);
    std::vector<Coupling_restraints_ew_segidContext *> coupling_restraints_ew_segid();
    Coupling_restraints_ew_segidContext* coupling_restraints_ew_segid(size_t i);
    std::vector<Talos_restraintsContext *> talos_restraints();
    Talos_restraintsContext* talos_restraints(size_t i);
    std::vector<Talos_restraints_wo_s2Context *> talos_restraints_wo_s2();
    Talos_restraints_wo_s2Context* talos_restraints_wo_s2(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dynamo_mrContext* dynamo_mr();

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

  class  Distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Group();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *D_Lo();
    antlr4::tree::TerminalNode *D_Hi();
    antlr4::tree::TerminalNode *FC();
    antlr4::tree::TerminalNode *W();
    antlr4::tree::TerminalNode *S();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
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
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintContext* distance_restraint();

  class  Distance_restraints_sw_segidContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraints_sw_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Group();
    antlr4::tree::TerminalNode *Segname_I();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Segname_J();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *D_Lo();
    antlr4::tree::TerminalNode *D_Hi();
    antlr4::tree::TerminalNode *FC();
    antlr4::tree::TerminalNode *W();
    antlr4::tree::TerminalNode *S();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Distance_restraint_sw_segidContext *> distance_restraint_sw_segid();
    Distance_restraint_sw_segidContext* distance_restraint_sw_segid(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraints_sw_segidContext* distance_restraints_sw_segid();

  class  Distance_restraint_sw_segidContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraint_sw_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraint_sw_segidContext* distance_restraint_sw_segid();

  class  Distance_restraints_ew_segidContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraints_ew_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Group();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Segname_I();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *Segname_J();
    antlr4::tree::TerminalNode *D_Lo();
    antlr4::tree::TerminalNode *D_Hi();
    antlr4::tree::TerminalNode *FC();
    antlr4::tree::TerminalNode *W();
    antlr4::tree::TerminalNode *S();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Distance_restraint_ew_segidContext *> distance_restraint_ew_segid();
    Distance_restraint_ew_segidContext* distance_restraint_ew_segid(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraints_ew_segidContext* distance_restraints_ew_segid();

  class  Distance_restraint_ew_segidContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraint_ew_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraint_ew_segidContext* distance_restraint_ew_segid();

  class  Torsion_angle_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Torsion_angle_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *Resid_K();
    antlr4::tree::TerminalNode *Resname_K();
    antlr4::tree::TerminalNode *Atomname_K();
    antlr4::tree::TerminalNode *Resid_L();
    antlr4::tree::TerminalNode *Resname_L();
    antlr4::tree::TerminalNode *Atomname_L();
    antlr4::tree::TerminalNode *Angle_Lo();
    antlr4::tree::TerminalNode *Angle_Hi();
    antlr4::tree::TerminalNode *FC();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Torsion_angle_restraintContext *> torsion_angle_restraint();
    Torsion_angle_restraintContext* torsion_angle_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Torsion_angle_restraintsContext* torsion_angle_restraints();

  class  Torsion_angle_restraintContext : public antlr4::ParserRuleContext {
  public:
    Torsion_angle_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Torsion_angle_restraintContext* torsion_angle_restraint();

  class  Torsion_angle_restraints_sw_segidContext : public antlr4::ParserRuleContext {
  public:
    Torsion_angle_restraints_sw_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Segname_I();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Segname_J();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *Segname_K();
    antlr4::tree::TerminalNode *Resid_K();
    antlr4::tree::TerminalNode *Resname_K();
    antlr4::tree::TerminalNode *Atomname_K();
    antlr4::tree::TerminalNode *Segname_L();
    antlr4::tree::TerminalNode *Resid_L();
    antlr4::tree::TerminalNode *Resname_L();
    antlr4::tree::TerminalNode *Atomname_L();
    antlr4::tree::TerminalNode *Angle_Lo();
    antlr4::tree::TerminalNode *Angle_Hi();
    antlr4::tree::TerminalNode *FC();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Torsion_angle_restraint_sw_segidContext *> torsion_angle_restraint_sw_segid();
    Torsion_angle_restraint_sw_segidContext* torsion_angle_restraint_sw_segid(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Torsion_angle_restraints_sw_segidContext* torsion_angle_restraints_sw_segid();

  class  Torsion_angle_restraint_sw_segidContext : public antlr4::ParserRuleContext {
  public:
    Torsion_angle_restraint_sw_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Torsion_angle_restraint_sw_segidContext* torsion_angle_restraint_sw_segid();

  class  Torsion_angle_restraints_ew_segidContext : public antlr4::ParserRuleContext {
  public:
    Torsion_angle_restraints_ew_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Segname_I();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *Segname_J();
    antlr4::tree::TerminalNode *Resid_K();
    antlr4::tree::TerminalNode *Resname_K();
    antlr4::tree::TerminalNode *Atomname_K();
    antlr4::tree::TerminalNode *Segname_K();
    antlr4::tree::TerminalNode *Resid_L();
    antlr4::tree::TerminalNode *Resname_L();
    antlr4::tree::TerminalNode *Atomname_L();
    antlr4::tree::TerminalNode *Segname_L();
    antlr4::tree::TerminalNode *Angle_Lo();
    antlr4::tree::TerminalNode *Angle_Hi();
    antlr4::tree::TerminalNode *FC();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Torsion_angle_restraint_ew_segidContext *> torsion_angle_restraint_ew_segid();
    Torsion_angle_restraint_ew_segidContext* torsion_angle_restraint_ew_segid(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Torsion_angle_restraints_ew_segidContext* torsion_angle_restraints_ew_segid();

  class  Torsion_angle_restraint_ew_segidContext : public antlr4::ParserRuleContext {
  public:
    Torsion_angle_restraint_ew_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Torsion_angle_restraint_ew_segidContext* torsion_angle_restraint_ew_segid();

  class  Rdc_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *D();
    antlr4::tree::TerminalNode *DD();
    antlr4::tree::TerminalNode *W();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Rdc_restraintContext *> rdc_restraint();
    Rdc_restraintContext* rdc_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraintsContext* rdc_restraints();

  class  Rdc_restraintContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraintContext* rdc_restraint();

  class  Rdc_restraints_sw_segidContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraints_sw_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Segname_I();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Segname_J();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *D();
    antlr4::tree::TerminalNode *DD();
    antlr4::tree::TerminalNode *W();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Rdc_restraint_sw_segidContext *> rdc_restraint_sw_segid();
    Rdc_restraint_sw_segidContext* rdc_restraint_sw_segid(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraints_sw_segidContext* rdc_restraints_sw_segid();

  class  Rdc_restraint_sw_segidContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraint_sw_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraint_sw_segidContext* rdc_restraint_sw_segid();

  class  Rdc_restraints_ew_segidContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraints_ew_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Segname_I();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *Segname_J();
    antlr4::tree::TerminalNode *D();
    antlr4::tree::TerminalNode *DD();
    antlr4::tree::TerminalNode *W();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Rdc_restraint_ew_segidContext *> rdc_restraint_ew_segid();
    Rdc_restraint_ew_segidContext* rdc_restraint_ew_segid(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraints_ew_segidContext* rdc_restraints_ew_segid();

  class  Rdc_restraint_ew_segidContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraint_ew_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraint_ew_segidContext* rdc_restraint_ew_segid();

  class  Pales_meta_outputsContext : public antlr4::ParserRuleContext {
  public:
    Pales_meta_outputsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Data();
    antlr4::tree::TerminalNode *RETURN_DA();
    antlr4::tree::TerminalNode *Pales_mode();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_DA();
    antlr4::tree::TerminalNode* Simple_name_DA(size_t i);
    antlr4::tree::TerminalNode *Tensor_mode();
    antlr4::tree::TerminalNode *Saupe_matrix();
    std::vector<antlr4::tree::TerminalNode *> S_DA();
    antlr4::tree::TerminalNode* S_DA(size_t i);
    std::vector<antlr4::tree::TerminalNode *> L_paren_DA();
    antlr4::tree::TerminalNode* L_paren_DA(size_t i);
    std::vector<antlr4::tree::TerminalNode *> R_paren_DA();
    antlr4::tree::TerminalNode* R_paren_DA(size_t i);
    antlr4::tree::TerminalNode *Saupe();
    std::vector<antlr4::tree::TerminalNode *> Real_DA();
    antlr4::tree::TerminalNode* Real_DA(size_t i);
    antlr4::tree::TerminalNode *Irreducible_rep();
    antlr4::tree::TerminalNode *Irreducible();
    antlr4::tree::TerminalNode *Mapping_corr();
    antlr4::tree::TerminalNode *Mapping();
    std::vector<antlr4::tree::TerminalNode *> Float_DA();
    antlr4::tree::TerminalNode* Float_DA(size_t i);
    antlr4::tree::TerminalNode *Eigenvalues();
    std::vector<antlr4::tree::TerminalNode *> Comma_DA();
    antlr4::tree::TerminalNode* Comma_DA(size_t i);
    antlr4::tree::TerminalNode *Eigenvectors();
    antlr4::tree::TerminalNode *Q_euler_solutions();
    antlr4::tree::TerminalNode *Q_euler_angles();
    antlr4::tree::TerminalNode *Integer_DA();
    antlr4::tree::TerminalNode *Euler_solutions();
    antlr4::tree::TerminalNode *Euler_angles();
    antlr4::tree::TerminalNode *N();
    antlr4::tree::TerminalNode *Regression();
    antlr4::tree::TerminalNode *Plus_minus();
    antlr4::tree::TerminalNode *L_brkt_DA();
    antlr4::tree::TerminalNode *Hz();
    antlr4::tree::TerminalNode *R_brkt_DA();
    antlr4::tree::TerminalNode *Da();
    antlr4::tree::TerminalNode *Dr();
    antlr4::tree::TerminalNode *Aa();
    antlr4::tree::TerminalNode *Ar();
    antlr4::tree::TerminalNode *Da_hn();
    antlr4::tree::TerminalNode *Rhombicity();
    antlr4::tree::TerminalNode *General_magnitude();
    antlr4::tree::TerminalNode *Rms();
    antlr4::tree::TerminalNode *Chi2();
    antlr4::tree::TerminalNode *Corr();
    antlr4::tree::TerminalNode *R();
    antlr4::tree::TerminalNode *Q();
    antlr4::tree::TerminalNode *Offset();
    antlr4::tree::TerminalNode *Slope();
    antlr4::tree::TerminalNode *Inv();
    antlr4::tree::TerminalNode *X_axis();
    antlr4::tree::TerminalNode *Y_axis();
    antlr4::tree::TerminalNode *Z_axis();
    antlr4::tree::TerminalNode *Bax();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pales_meta_outputsContext* pales_meta_outputs();

  class  Pales_rdc_outputsContext : public antlr4::ParserRuleContext {
  public:
    Pales_rdc_outputsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *DI();
    antlr4::tree::TerminalNode *D_obs();
    antlr4::tree::TerminalNode *D();
    antlr4::tree::TerminalNode *D_diff();
    antlr4::tree::TerminalNode *DD();
    antlr4::tree::TerminalNode *W();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Pales_rdc_outputContext *> pales_rdc_output();
    Pales_rdc_outputContext* pales_rdc_output(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pales_rdc_outputsContext* pales_rdc_outputs();

  class  Pales_rdc_outputContext : public antlr4::ParserRuleContext {
  public:
    Pales_rdc_outputContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pales_rdc_outputContext* pales_rdc_output();

  class  Coupling_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Coupling_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *Resid_K();
    antlr4::tree::TerminalNode *Resname_K();
    antlr4::tree::TerminalNode *Atomname_K();
    antlr4::tree::TerminalNode *Resid_L();
    antlr4::tree::TerminalNode *Resname_L();
    antlr4::tree::TerminalNode *Atomname_L();
    antlr4::tree::TerminalNode *A();
    antlr4::tree::TerminalNode *B();
    antlr4::tree::TerminalNode *C();
    antlr4::tree::TerminalNode *Phase();
    antlr4::tree::TerminalNode *ObsJ();
    antlr4::tree::TerminalNode *FC();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Coupling_restraintContext *> coupling_restraint();
    Coupling_restraintContext* coupling_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coupling_restraintsContext* coupling_restraints();

  class  Coupling_restraintContext : public antlr4::ParserRuleContext {
  public:
    Coupling_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coupling_restraintContext* coupling_restraint();

  class  Coupling_restraints_sw_segidContext : public antlr4::ParserRuleContext {
  public:
    Coupling_restraints_sw_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Segname_I();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Segname_J();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *Segname_K();
    antlr4::tree::TerminalNode *Resid_K();
    antlr4::tree::TerminalNode *Resname_K();
    antlr4::tree::TerminalNode *Atomname_K();
    antlr4::tree::TerminalNode *Segname_L();
    antlr4::tree::TerminalNode *Resid_L();
    antlr4::tree::TerminalNode *Resname_L();
    antlr4::tree::TerminalNode *Atomname_L();
    antlr4::tree::TerminalNode *A();
    antlr4::tree::TerminalNode *B();
    antlr4::tree::TerminalNode *C();
    antlr4::tree::TerminalNode *Phase();
    antlr4::tree::TerminalNode *ObsJ();
    antlr4::tree::TerminalNode *FC();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Coupling_restraint_sw_segidContext *> coupling_restraint_sw_segid();
    Coupling_restraint_sw_segidContext* coupling_restraint_sw_segid(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coupling_restraints_sw_segidContext* coupling_restraints_sw_segid();

  class  Coupling_restraint_sw_segidContext : public antlr4::ParserRuleContext {
  public:
    Coupling_restraint_sw_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coupling_restraint_sw_segidContext* coupling_restraint_sw_segid();

  class  Coupling_restraints_ew_segidContext : public antlr4::ParserRuleContext {
  public:
    Coupling_restraints_ew_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Resid_I();
    antlr4::tree::TerminalNode *Resname_I();
    antlr4::tree::TerminalNode *Atomname_I();
    antlr4::tree::TerminalNode *Segname_I();
    antlr4::tree::TerminalNode *Resid_J();
    antlr4::tree::TerminalNode *Resname_J();
    antlr4::tree::TerminalNode *Atomname_J();
    antlr4::tree::TerminalNode *Segname_J();
    antlr4::tree::TerminalNode *Resid_K();
    antlr4::tree::TerminalNode *Resname_K();
    antlr4::tree::TerminalNode *Atomname_K();
    antlr4::tree::TerminalNode *Segname_K();
    antlr4::tree::TerminalNode *Resid_L();
    antlr4::tree::TerminalNode *Resname_L();
    antlr4::tree::TerminalNode *Atomname_L();
    antlr4::tree::TerminalNode *Segname_L();
    antlr4::tree::TerminalNode *A();
    antlr4::tree::TerminalNode *B();
    antlr4::tree::TerminalNode *C();
    antlr4::tree::TerminalNode *Phase();
    antlr4::tree::TerminalNode *ObsJ();
    antlr4::tree::TerminalNode *FC();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Coupling_restraint_ew_segidContext *> coupling_restraint_ew_segid();
    Coupling_restraint_ew_segidContext* coupling_restraint_ew_segid(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coupling_restraints_ew_segidContext* coupling_restraints_ew_segid();

  class  Coupling_restraint_ew_segidContext : public antlr4::ParserRuleContext {
  public:
    Coupling_restraint_ew_segidContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coupling_restraint_ew_segidContext* coupling_restraint_ew_segid();

  class  Talos_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Talos_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Resid();
    antlr4::tree::TerminalNode *Resname();
    antlr4::tree::TerminalNode *Phi();
    antlr4::tree::TerminalNode *Psi();
    antlr4::tree::TerminalNode *Dphi();
    antlr4::tree::TerminalNode *Dpsi();
    antlr4::tree::TerminalNode *Dist();
    antlr4::tree::TerminalNode *S2();
    antlr4::tree::TerminalNode *Count();
    antlr4::tree::TerminalNode *Cs_count();
    antlr4::tree::TerminalNode *Class();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Talos_restraintContext *> talos_restraint();
    Talos_restraintContext* talos_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Talos_restraintsContext* talos_restraints();

  class  Talos_restraintContext : public antlr4::ParserRuleContext {
  public:
    Talos_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Talos_restraintContext* talos_restraint();

  class  Talos_restraints_wo_s2Context : public antlr4::ParserRuleContext {
  public:
    Talos_restraints_wo_s2Context(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vars();
    antlr4::tree::TerminalNode *Resid();
    antlr4::tree::TerminalNode *Resname();
    antlr4::tree::TerminalNode *Phi();
    antlr4::tree::TerminalNode *Psi();
    antlr4::tree::TerminalNode *Dphi();
    antlr4::tree::TerminalNode *Dpsi();
    antlr4::tree::TerminalNode *Dist();
    antlr4::tree::TerminalNode *Count();
    antlr4::tree::TerminalNode *Class();
    antlr4::tree::TerminalNode *RETURN_VA();
    antlr4::tree::TerminalNode *Format();
    std::vector<antlr4::tree::TerminalNode *> Format_code();
    antlr4::tree::TerminalNode* Format_code(size_t i);
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<Talos_restraint_wo_s2Context *> talos_restraint_wo_s2();
    Talos_restraint_wo_s2Context* talos_restraint_wo_s2(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Talos_restraints_wo_s2Context* talos_restraints_wo_s2();

  class  Talos_restraint_wo_s2Context : public antlr4::ParserRuleContext {
  public:
    Talos_restraint_wo_s2Context(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Talos_restraint_wo_s2Context* talos_restraint_wo_s2();

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

