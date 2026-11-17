
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CnsMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CnsMRParser : public antlr4::Parser {
public:
  enum {
    Set = 1, End = 2, Noe = 3, Analysis = 4, Assign = 5, Asymptote = 6, 
    Average = 7, Bhig = 8, Ceiling = 9, Classification = 10, CountViol = 11, 
    Cv = 12, Den = 13, Distribute = 14, Ensemble = 15, Monomers = 16, Ncount = 17, 
    Nrestraints = 18, Outd = 19, Partition = 20, Potential = 21, Predict = 22, 
    Print = 23, Raverage = 24, Threshold = 25, Reset = 26, Rswitch = 27, 
    Scale = 28, SoExponent = 29, SqConstant = 30, SqExponent = 31, SqOffset = 32, 
    Taverage = 33, Temperature = 34, Initialize = 35, Update = 36, Gamma = 37, 
    Kappa = 38, Cutoff = 39, Cuton = 40, From = 41, To = 42, Peak = 43, 
    Spectrum = 44, Volume = 45, Vol = 46, Hpm1 = 47, Ppm1 = 48, Ppm2 = 49, 
    Restraints = 50, Dihedral = 51, Nassign = 52, Print_any = 53, Plane = 54, 
    Group = 55, Selection = 56, Weight = 57, Harmonic = 58, Exponent = 59, 
    Normal = 60, Sanisotropy = 61, Coefficients = 62, ForceConstant = 63, 
    Coupling = 64, Carbon = 65, Expectation = 66, PhiStep = 67, PsiStep = 68, 
    Rcoil = 69, Zero = 70, Proton = 71, Observed = 72, Anisotropy = 73, 
    Amides = 74, Nitrogens = 75, Oxygens = 76, RingAtoms = 77, AlphasAndAmides = 78, 
    Error = 79, Conformation = 80, Compressed = 81, Phase = 82, Size = 83, 
    Dimensions = 84, Danisotropy = 85, OneBond = 86, AngleDb = 87, DerivFlag = 88, 
    Ncs = 89, Equivalence = 90, Sigb = 91, Flags = 92, All = 93, Around = 94, 
    Atom = 95, Attribute = 96, BondedTo = 97, ByGroup = 98, ByRes = 99, 
    Chemical = 100, Fbox = 101, Hydrogen = 102, Id = 103, Known = 104, Name = 105, 
    NONE = 106, Point = 107, Cut = 108, Previous = 109, Pseudo = 110, Residue = 111, 
    Resname = 112, Saround = 113, SegIdentifier = 114, Sfbox = 115, Store1 = 116, 
    Store2 = 117, Store3 = 118, Store4 = 119, Store5 = 120, Store6 = 121, 
    Store7 = 122, Store8 = 123, Store9 = 124, Tag = 125, Vector = 126, Do_Lp = 127, 
    Identity_Lp = 128, Show = 129, Evaluate_Lp = 130, Patch = 131, Reference = 132, 
    Nil = 133, Parameter = 134, UB = 135, Mult = 136, HBonded = 137, Improper = 138, 
    NBFix = 139, NonB = 140, VDWOff = 141, Verbose = 142, For = 143, Loop = 144, 
    Tail = 145, Head = 146, Or_op = 147, And_op = 148, Not_op = 149, Comma = 150, 
    Complex = 151, Integer = 152, Logical = 153, Real = 154, Double_quote_string = 155, 
    SHARP_COMMENT = 156, EXCLM_COMMENT = 157, SMCLN_COMMENT = 158, Simple_name = 159, 
    Simple_names = 160, Integers = 161, L_paren = 162, R_paren = 163, Colon = 164, 
    Equ_op = 165, Lt_op = 166, Gt_op = 167, Leq_op = 168, Geq_op = 169, 
    Neq_op = 170, Symbol_name = 171, SPACE = 172, ENCLOSE_COMMENT = 173, 
    SECTION_COMMENT = 174, LINE_COMMENT = 175, SET_VARIABLE = 176, Abs = 177, 
    Attr_properties = 178, Comparison_ops = 179, SPACE_AP = 180, Averaging_methods = 181, 
    Equ_op_CL = 182, Class_name = 183, SPACE_CL = 184, Class_name_AM = 185, 
    SPACE_AM = 186, Equ_op_PT = 187, Potential_types = 188, Class_name_PT = 189, 
    SPACE_PT = 190, Noe_analysis = 191, SPACE_NA = 192, Exclude = 193, Include = 194, 
    End_FL = 195, Class_name_FL = 196, Any_class = 197, SPACE_FL = 198, 
    R_paren_VE = 199, Equ_op_VE = 200, Add_op_VE = 201, Sub_op_VE = 202, 
    Mul_op_VE = 203, Div_op_VE = 204, Exp_op_VE = 205, Comma_VE = 206, Integer_VE = 207, 
    Real_VE = 208, Atom_properties_VE = 209, Abs_VE = 210, Acos_VE = 211, 
    Asin_VE = 212, Cos_VE = 213, Decode_VE = 214, Encode_VE = 215, Exp_VE = 216, 
    Gauss_VE = 217, Heavy_VE = 218, Int_VE = 219, Log10_VE = 220, Log_VE = 221, 
    Max_VE = 222, Maxw_VE = 223, Min_VE = 224, Mod_VE = 225, Norm_VE = 226, 
    Random_VE = 227, Sign_VE = 228, Sin_VE = 229, Sqrt_VE = 230, Tan_VE = 231, 
    Symbol_name_VE = 232, Simple_name_VE = 233, Double_quote_string_VE = 234, 
    SPACE_VE = 235, L_paren_VF = 236, SPACE_VF = 237, L_paren_VS = 238, 
    R_paren_VS = 239, Average_VS = 240, Element_VS = 241, Max_VS = 242, 
    Min_VS = 243, Norm_VS = 244, Rms_VS = 245, Sum_VS = 246, Atom_properties_VS = 247, 
    SPACE_VS = 248, L_paren_CF = 249, R_paren_CF = 250, In_CF = 251, Integer_CF = 252, 
    Real_CF = 253, Symbol_name_CF = 254, Simple_name_CF = 255, Double_quote_string_CF = 256, 
    SPACE_CF = 257, COMMENT_CF = 258, Simple_name_LL = 259, SPACE_LL = 260
  };

  enum {
    RuleCns_mr = 0, RuleDistance_restraint = 1, RuleDihedral_angle_restraint = 2, 
    RulePlane_restraint = 3, RuleHarmonic_restraint = 4, RuleRdc_restraint = 5, 
    RuleCoupling_restraint = 6, RuleCarbon_shift_restraint = 7, RuleProton_shift_restraint = 8, 
    RuleConformation_db_restraint = 9, RuleDiffusion_anisotropy_restraint = 10, 
    RuleOne_bond_coupling_restraint = 11, RuleAngle_db_restraint = 12, RuleNoe_statement = 13, 
    RuleNoe_assign = 14, RulePredict_statement = 15, RuleNoe_annotation = 16, 
    RuleDihedral_statement = 17, RuleDihedral_assign = 18, RulePlane_statement = 19, 
    RulePlane_group = 20, RuleGroup_statement = 21, RuleHarmonic_statement = 22, 
    RuleHarmonic_assign = 23, RuleSani_statement = 24, RuleSani_assign = 25, 
    RuleCoupling_statement = 26, RuleCoup_assign = 27, RuleCarbon_shift_statement = 28, 
    RuleCarbon_shift_assign = 29, RuleCarbon_shift_rcoil = 30, RuleProton_shift_statement = 31, 
    RuleObserved = 32, RuleProton_shift_rcoil = 33, RuleProton_shift_anisotropy = 34, 
    RuleProton_shift_amides = 35, RuleProton_shift_carbons = 36, RuleProton_shift_nitrogens = 37, 
    RuleProton_shift_oxygens = 38, RuleProton_shift_ring_atoms = 39, RuleProton_shift_alphas_and_amides = 40, 
    RuleConformation_statement = 41, RuleConf_assign = 42, RuleDiffusion_statement = 43, 
    RuleDani_assign = 44, RuleOne_bond_coupling_statement = 45, RuleOne_bond_assign = 46, 
    RuleAngle_db_statement = 47, RuleAngle_db_assign = 48, RuleNcs_restraint = 49, 
    RuleNcs_statement = 50, RuleNcs_group_statement = 51, RuleSelection = 52, 
    RuleSelection_expression = 53, RuleTerm = 54, RuleFactor = 55, RuleNumber = 56, 
    RuleNumber_f = 57, RuleNumber_s = 58, RuleNumber_a = 59, RuleClassification = 60, 
    RuleClass_name = 61, RuleFlag_statement = 62, RuleVector_statement = 63, 
    RuleVector_mode = 64, RuleVector_expression = 65, RuleVector_operation = 66, 
    RuleVflc = 67, RuleVector_func_call = 68, RuleVector_show_property = 69, 
    RuleEvaluate_statement = 70, RuleEvaluate_operation = 71, RulePatch_statement = 72, 
    RuleParameter_setting = 73, RuleParameter_statement = 74, RuleNoe_assign_loop = 75, 
    RuleDihedral_assign_loop = 76, RuleSani_assign_loop = 77, RuleCoup_assign_loop = 78, 
    RuleCarbon_shift_assign_loop = 79, RulePlane_group_loop = 80
  };

  explicit CnsMRParser(antlr4::TokenStream *input);

  CnsMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~CnsMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Cns_mrContext;
  class Distance_restraintContext;
  class Dihedral_angle_restraintContext;
  class Plane_restraintContext;
  class Harmonic_restraintContext;
  class Rdc_restraintContext;
  class Coupling_restraintContext;
  class Carbon_shift_restraintContext;
  class Proton_shift_restraintContext;
  class Conformation_db_restraintContext;
  class Diffusion_anisotropy_restraintContext;
  class One_bond_coupling_restraintContext;
  class Angle_db_restraintContext;
  class Noe_statementContext;
  class Noe_assignContext;
  class Predict_statementContext;
  class Noe_annotationContext;
  class Dihedral_statementContext;
  class Dihedral_assignContext;
  class Plane_statementContext;
  class Plane_groupContext;
  class Group_statementContext;
  class Harmonic_statementContext;
  class Harmonic_assignContext;
  class Sani_statementContext;
  class Sani_assignContext;
  class Coupling_statementContext;
  class Coup_assignContext;
  class Carbon_shift_statementContext;
  class Carbon_shift_assignContext;
  class Carbon_shift_rcoilContext;
  class Proton_shift_statementContext;
  class ObservedContext;
  class Proton_shift_rcoilContext;
  class Proton_shift_anisotropyContext;
  class Proton_shift_amidesContext;
  class Proton_shift_carbonsContext;
  class Proton_shift_nitrogensContext;
  class Proton_shift_oxygensContext;
  class Proton_shift_ring_atomsContext;
  class Proton_shift_alphas_and_amidesContext;
  class Conformation_statementContext;
  class Conf_assignContext;
  class Diffusion_statementContext;
  class Dani_assignContext;
  class One_bond_coupling_statementContext;
  class One_bond_assignContext;
  class Angle_db_statementContext;
  class Angle_db_assignContext;
  class Ncs_restraintContext;
  class Ncs_statementContext;
  class Ncs_group_statementContext;
  class SelectionContext;
  class Selection_expressionContext;
  class TermContext;
  class FactorContext;
  class NumberContext;
  class Number_fContext;
  class Number_sContext;
  class Number_aContext;
  class ClassificationContext;
  class Class_nameContext;
  class Flag_statementContext;
  class Vector_statementContext;
  class Vector_modeContext;
  class Vector_expressionContext;
  class Vector_operationContext;
  class VflcContext;
  class Vector_func_callContext;
  class Vector_show_propertyContext;
  class Evaluate_statementContext;
  class Evaluate_operationContext;
  class Patch_statementContext;
  class Parameter_settingContext;
  class Parameter_statementContext;
  class Noe_assign_loopContext;
  class Dihedral_assign_loopContext;
  class Sani_assign_loopContext;
  class Coup_assign_loopContext;
  class Carbon_shift_assign_loopContext;
  class Plane_group_loopContext; 

  class  Cns_mrContext : public antlr4::ParserRuleContext {
  public:
    Cns_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<Distance_restraintContext *> distance_restraint();
    Distance_restraintContext* distance_restraint(size_t i);
    std::vector<Dihedral_angle_restraintContext *> dihedral_angle_restraint();
    Dihedral_angle_restraintContext* dihedral_angle_restraint(size_t i);
    std::vector<Plane_restraintContext *> plane_restraint();
    Plane_restraintContext* plane_restraint(size_t i);
    std::vector<Harmonic_restraintContext *> harmonic_restraint();
    Harmonic_restraintContext* harmonic_restraint(size_t i);
    std::vector<Rdc_restraintContext *> rdc_restraint();
    Rdc_restraintContext* rdc_restraint(size_t i);
    std::vector<Coupling_restraintContext *> coupling_restraint();
    Coupling_restraintContext* coupling_restraint(size_t i);
    std::vector<Carbon_shift_restraintContext *> carbon_shift_restraint();
    Carbon_shift_restraintContext* carbon_shift_restraint(size_t i);
    std::vector<Proton_shift_restraintContext *> proton_shift_restraint();
    Proton_shift_restraintContext* proton_shift_restraint(size_t i);
    std::vector<Conformation_db_restraintContext *> conformation_db_restraint();
    Conformation_db_restraintContext* conformation_db_restraint(size_t i);
    std::vector<Diffusion_anisotropy_restraintContext *> diffusion_anisotropy_restraint();
    Diffusion_anisotropy_restraintContext* diffusion_anisotropy_restraint(size_t i);
    std::vector<One_bond_coupling_restraintContext *> one_bond_coupling_restraint();
    One_bond_coupling_restraintContext* one_bond_coupling_restraint(size_t i);
    std::vector<Angle_db_restraintContext *> angle_db_restraint();
    Angle_db_restraintContext* angle_db_restraint(size_t i);
    std::vector<Ncs_restraintContext *> ncs_restraint();
    Ncs_restraintContext* ncs_restraint(size_t i);
    std::vector<ClassificationContext *> classification();
    ClassificationContext* classification(size_t i);
    std::vector<Flag_statementContext *> flag_statement();
    Flag_statementContext* flag_statement(size_t i);
    std::vector<Vector_statementContext *> vector_statement();
    Vector_statementContext* vector_statement(size_t i);
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Patch_statementContext *> patch_statement();
    Patch_statementContext* patch_statement(size_t i);
    std::vector<Parameter_settingContext *> parameter_setting();
    Parameter_settingContext* parameter_setting(size_t i);
    std::vector<Noe_assign_loopContext *> noe_assign_loop();
    Noe_assign_loopContext* noe_assign_loop(size_t i);
    std::vector<Dihedral_assign_loopContext *> dihedral_assign_loop();
    Dihedral_assign_loopContext* dihedral_assign_loop(size_t i);
    std::vector<Sani_assign_loopContext *> sani_assign_loop();
    Sani_assign_loopContext* sani_assign_loop(size_t i);
    std::vector<Coup_assign_loopContext *> coup_assign_loop();
    Coup_assign_loopContext* coup_assign_loop(size_t i);
    std::vector<Carbon_shift_assign_loopContext *> carbon_shift_assign_loop();
    Carbon_shift_assign_loopContext* carbon_shift_assign_loop(size_t i);
    std::vector<Noe_assignContext *> noe_assign();
    Noe_assignContext* noe_assign(size_t i);
    std::vector<Dihedral_assignContext *> dihedral_assign();
    Dihedral_assignContext* dihedral_assign(size_t i);
    std::vector<Sani_assignContext *> sani_assign();
    Sani_assignContext* sani_assign(size_t i);
    std::vector<Plane_statementContext *> plane_statement();
    Plane_statementContext* plane_statement(size_t i);
    std::vector<Harmonic_assignContext *> harmonic_assign();
    Harmonic_assignContext* harmonic_assign(size_t i);
    std::vector<Coup_assignContext *> coup_assign();
    Coup_assignContext* coup_assign(size_t i);
    std::vector<Carbon_shift_assignContext *> carbon_shift_assign();
    Carbon_shift_assignContext* carbon_shift_assign(size_t i);
    std::vector<ObservedContext *> observed();
    ObservedContext* observed(size_t i);
    std::vector<Parameter_statementContext *> parameter_statement();
    Parameter_statementContext* parameter_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cns_mrContext* cns_mr();

  class  Distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Noe();
    antlr4::tree::TerminalNode *End();
    std::vector<Noe_statementContext *> noe_statement();
    Noe_statementContext* noe_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintContext* distance_restraint();

  class  Dihedral_angle_restraintContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Dihedral();
    antlr4::tree::TerminalNode *End();
    antlr4::tree::TerminalNode *Restraints();
    std::vector<Dihedral_statementContext *> dihedral_statement();
    Dihedral_statementContext* dihedral_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_restraintContext* dihedral_angle_restraint();

  class  Plane_restraintContext : public antlr4::ParserRuleContext {
  public:
    Plane_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Plane();
    antlr4::tree::TerminalNode *End();
    antlr4::tree::TerminalNode *Restraints();
    std::vector<Plane_statementContext *> plane_statement();
    Plane_statementContext* plane_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Plane_restraintContext* plane_restraint();

  class  Harmonic_restraintContext : public antlr4::ParserRuleContext {
  public:
    Harmonic_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Harmonic();
    antlr4::tree::TerminalNode *End();
    antlr4::tree::TerminalNode *Restraints();
    std::vector<Harmonic_statementContext *> harmonic_statement();
    Harmonic_statementContext* harmonic_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Harmonic_restraintContext* harmonic_restraint();

  class  Rdc_restraintContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Sanisotropy();
    antlr4::tree::TerminalNode *End();
    std::vector<Sani_statementContext *> sani_statement();
    Sani_statementContext* sani_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraintContext* rdc_restraint();

  class  Coupling_restraintContext : public antlr4::ParserRuleContext {
  public:
    Coupling_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Coupling();
    antlr4::tree::TerminalNode *End();
    std::vector<Coupling_statementContext *> coupling_statement();
    Coupling_statementContext* coupling_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coupling_restraintContext* coupling_restraint();

  class  Carbon_shift_restraintContext : public antlr4::ParserRuleContext {
  public:
    Carbon_shift_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Carbon();
    antlr4::tree::TerminalNode *End();
    std::vector<Carbon_shift_statementContext *> carbon_shift_statement();
    Carbon_shift_statementContext* carbon_shift_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Carbon_shift_restraintContext* carbon_shift_restraint();

  class  Proton_shift_restraintContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Proton();
    antlr4::tree::TerminalNode *End();
    std::vector<Proton_shift_statementContext *> proton_shift_statement();
    Proton_shift_statementContext* proton_shift_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_restraintContext* proton_shift_restraint();

  class  Conformation_db_restraintContext : public antlr4::ParserRuleContext {
  public:
    Conformation_db_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Conformation();
    antlr4::tree::TerminalNode *End();
    std::vector<Conformation_statementContext *> conformation_statement();
    Conformation_statementContext* conformation_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Conformation_db_restraintContext* conformation_db_restraint();

  class  Diffusion_anisotropy_restraintContext : public antlr4::ParserRuleContext {
  public:
    Diffusion_anisotropy_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Danisotropy();
    antlr4::tree::TerminalNode *End();
    std::vector<Diffusion_statementContext *> diffusion_statement();
    Diffusion_statementContext* diffusion_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diffusion_anisotropy_restraintContext* diffusion_anisotropy_restraint();

  class  One_bond_coupling_restraintContext : public antlr4::ParserRuleContext {
  public:
    One_bond_coupling_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *OneBond();
    antlr4::tree::TerminalNode *End();
    std::vector<One_bond_coupling_statementContext *> one_bond_coupling_statement();
    One_bond_coupling_statementContext* one_bond_coupling_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  One_bond_coupling_restraintContext* one_bond_coupling_restraint();

  class  Angle_db_restraintContext : public antlr4::ParserRuleContext {
  public:
    Angle_db_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *AngleDb();
    antlr4::tree::TerminalNode *End();
    std::vector<Angle_db_statementContext *> angle_db_statement();
    Angle_db_statementContext* angle_db_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_db_restraintContext* angle_db_restraint();

  class  Noe_statementContext : public antlr4::ParserRuleContext {
  public:
    Noe_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Analysis();
    antlr4::tree::TerminalNode *Noe_analysis();
    std::vector<antlr4::tree::TerminalNode *> Equ_op();
    antlr4::tree::TerminalNode* Equ_op(size_t i);
    Noe_assignContext *noe_assign();
    Noe_assign_loopContext *noe_assign_loop();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Asymptote();
    std::vector<Class_nameContext *> class_name();
    Class_nameContext* class_name(size_t i);
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Average();
    antlr4::tree::TerminalNode *Class_name_AM();
    antlr4::tree::TerminalNode *Averaging_methods();
    antlr4::tree::TerminalNode *Bhig();
    antlr4::tree::TerminalNode *Ceiling();
    antlr4::tree::TerminalNode *CountViol();
    antlr4::tree::TerminalNode *Cv();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Den();
    antlr4::tree::TerminalNode *Initialize();
    antlr4::tree::TerminalNode *Update();
    antlr4::tree::TerminalNode *Gamma();
    antlr4::tree::TerminalNode *Kappa();
    antlr4::tree::TerminalNode *Distribute();
    antlr4::tree::TerminalNode *End();
    std::vector<antlr4::tree::TerminalNode *> Ensemble();
    antlr4::tree::TerminalNode* Ensemble(size_t i);
    antlr4::tree::TerminalNode *Monomers();
    antlr4::tree::TerminalNode *Ncount();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Outd();
    antlr4::tree::TerminalNode *Partition();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Class_name_PT();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Predict();
    Predict_statementContext *predict_statement();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Raverage();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Rswitch();
    antlr4::tree::TerminalNode *Scale();
    antlr4::tree::TerminalNode *SoExponent();
    antlr4::tree::TerminalNode *SqConstant();
    antlr4::tree::TerminalNode *SqExponent();
    antlr4::tree::TerminalNode *SqOffset();
    antlr4::tree::TerminalNode *Taverage();
    antlr4::tree::TerminalNode *Temperature();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_statementContext* noe_statement();

  class  Noe_assignContext : public antlr4::ParserRuleContext {
  public:
    Noe_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Assign();
    antlr4::tree::TerminalNode* Assign(size_t i);
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<Noe_annotationContext *> noe_annotation();
    Noe_annotationContext* noe_annotation(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Or_op();
    antlr4::tree::TerminalNode* Or_op(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_assignContext* noe_assign();

  class  Predict_statementContext : public antlr4::ParserRuleContext {
  public:
    Predict_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Cutoff();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Cuton();
    antlr4::tree::TerminalNode *From();
    SelectionContext *selection();
    antlr4::tree::TerminalNode *To();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Predict_statementContext* predict_statement();

  class  Noe_annotationContext : public antlr4::ParserRuleContext {
  public:
    Noe_annotationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Peak();
    Number_aContext *number_a();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Spectrum();
    antlr4::tree::TerminalNode *Weight();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Vol();
    antlr4::tree::TerminalNode *Hpm1();
    antlr4::tree::TerminalNode *Ppm1();
    antlr4::tree::TerminalNode *Ppm2();
    antlr4::tree::TerminalNode *Cv();
    antlr4::tree::TerminalNode *Comma();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_annotationContext* noe_annotation();

  class  Dihedral_statementContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Vector_statementContext *vector_statement();
    Evaluate_statementContext *evaluate_statement();
    Dihedral_assignContext *dihedral_assign();
    Dihedral_assign_loopContext *dihedral_assign_loop();
    antlr4::tree::TerminalNode *Cv();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nassign();
    antlr4::tree::TerminalNode *Partition();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Scale();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Print_any();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_statementContext* dihedral_statement();

  class  Dihedral_assignContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_assignContext* dihedral_assign();

  class  Plane_statementContext : public antlr4::ParserRuleContext {
  public:
    Plane_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Vector_statementContext *vector_statement();
    Evaluate_statementContext *evaluate_statement();
    Plane_groupContext *plane_group();
    Plane_group_loopContext *plane_group_loop();
    antlr4::tree::TerminalNode *Initialize();
    antlr4::tree::TerminalNode *Print_any();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Plane_statementContext* plane_statement();

  class  Plane_groupContext : public antlr4::ParserRuleContext {
  public:
    Plane_groupContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Group();
    antlr4::tree::TerminalNode *End();
    std::vector<Group_statementContext *> group_statement();
    Group_statementContext* group_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Plane_groupContext* plane_group();

  class  Group_statementContext : public antlr4::ParserRuleContext {
  public:
    Group_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Selection();
    SelectionContext *selection();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Weight();
    Number_sContext *number_s();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Group_statementContext* group_statement();

  class  Harmonic_statementContext : public antlr4::ParserRuleContext {
  public:
    Harmonic_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Vector_statementContext *vector_statement();
    Evaluate_statementContext *evaluate_statement();
    antlr4::tree::TerminalNode *Exponent();
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Equ_op();
    antlr4::tree::TerminalNode* Equ_op(size_t i);
    antlr4::tree::TerminalNode *Normal();
    antlr4::tree::TerminalNode *L_paren();
    antlr4::tree::TerminalNode *R_paren();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Tail();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);
    antlr4::tree::TerminalNode *Head();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Harmonic_statementContext* harmonic_statement();

  class  Harmonic_assignContext : public antlr4::ParserRuleContext {
  public:
    Harmonic_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    SelectionContext *selection();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Harmonic_assignContext* harmonic_assign();

  class  Sani_statementContext : public antlr4::ParserRuleContext {
  public:
    Sani_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Sani_assignContext *sani_assign();
    Sani_assign_loopContext *sani_assign_loop();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Coefficients();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Sani_statementContext* sani_statement();

  class  Sani_assignContext : public antlr4::ParserRuleContext {
  public:
    Sani_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Sani_assignContext* sani_assign();

  class  Coupling_statementContext : public antlr4::ParserRuleContext {
  public:
    Coupling_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Coup_assignContext *coup_assign();
    Coup_assign_loopContext *coup_assign_loop();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Coefficients();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Cv();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Partition();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coupling_statementContext* coupling_statement();

  class  Coup_assignContext : public antlr4::ParserRuleContext {
  public:
    Coup_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coup_assignContext* coup_assign();

  class  Carbon_shift_statementContext : public antlr4::ParserRuleContext {
  public:
    Carbon_shift_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Carbon_shift_assignContext *carbon_shift_assign();
    Carbon_shift_assign_loopContext *carbon_shift_assign_loop();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Expectation();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *PhiStep();
    antlr4::tree::TerminalNode *PsiStep();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    Carbon_shift_rcoilContext *carbon_shift_rcoil();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Zero();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Carbon_shift_statementContext* carbon_shift_statement();

  class  Carbon_shift_assignContext : public antlr4::ParserRuleContext {
  public:
    Carbon_shift_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Carbon_shift_assignContext* carbon_shift_assign();

  class  Carbon_shift_rcoilContext : public antlr4::ParserRuleContext {
  public:
    Carbon_shift_rcoilContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Rcoil();
    SelectionContext *selection();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Carbon_shift_rcoilContext* carbon_shift_rcoil();

  class  Proton_shift_statementContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    ObservedContext *observed();
    Proton_shift_rcoilContext *proton_shift_rcoil();
    Proton_shift_anisotropyContext *proton_shift_anisotropy();
    Proton_shift_amidesContext *proton_shift_amides();
    Proton_shift_carbonsContext *proton_shift_carbons();
    Proton_shift_nitrogensContext *proton_shift_nitrogens();
    Proton_shift_oxygensContext *proton_shift_oxygens();
    Proton_shift_ring_atomsContext *proton_shift_ring_atoms();
    Proton_shift_alphas_and_amidesContext *proton_shift_alphas_and_amides();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Error();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_statementContext* proton_shift_statement();

  class  ObservedContext : public antlr4::ParserRuleContext {
  public:
    ObservedContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Observed();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ObservedContext* observed();

  class  Proton_shift_rcoilContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_rcoilContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Rcoil();
    SelectionContext *selection();
    NumberContext *number();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_rcoilContext* proton_shift_rcoil();

  class  Proton_shift_anisotropyContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_anisotropyContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Anisotropy();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *Logical();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_anisotropyContext* proton_shift_anisotropy();

  class  Proton_shift_amidesContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_amidesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Amides();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_amidesContext* proton_shift_amides();

  class  Proton_shift_carbonsContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_carbonsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Carbon();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_carbonsContext* proton_shift_carbons();

  class  Proton_shift_nitrogensContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_nitrogensContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Nitrogens();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_nitrogensContext* proton_shift_nitrogens();

  class  Proton_shift_oxygensContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_oxygensContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Oxygens();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_oxygensContext* proton_shift_oxygens();

  class  Proton_shift_ring_atomsContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_ring_atomsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RingAtoms();
    antlr4::tree::TerminalNode *Simple_name();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_ring_atomsContext* proton_shift_ring_atoms();

  class  Proton_shift_alphas_and_amidesContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_alphas_and_amidesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *AlphasAndAmides();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_alphas_and_amidesContext* proton_shift_alphas_and_amides();

  class  Conformation_statementContext : public antlr4::ParserRuleContext {
  public:
    Conformation_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Conf_assignContext *conf_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Compressed();
    antlr4::tree::TerminalNode *Expectation();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Error();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Phase();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Size();
    antlr4::tree::TerminalNode *Dimensions();
    antlr4::tree::TerminalNode *Zero();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Conformation_statementContext* conformation_statement();

  class  Conf_assignContext : public antlr4::ParserRuleContext {
  public:
    Conf_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Conf_assignContext* conf_assign();

  class  Diffusion_statementContext : public antlr4::ParserRuleContext {
  public:
    Diffusion_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Dani_assignContext *dani_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Coefficients();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diffusion_statementContext* diffusion_statement();

  class  Dani_assignContext : public antlr4::ParserRuleContext {
  public:
    Dani_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dani_assignContext* dani_assign();

  class  One_bond_coupling_statementContext : public antlr4::ParserRuleContext {
  public:
    One_bond_coupling_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    One_bond_assignContext *one_bond_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Coefficients();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  One_bond_coupling_statementContext* one_bond_coupling_statement();

  class  One_bond_assignContext : public antlr4::ParserRuleContext {
  public:
    One_bond_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  One_bond_assignContext* one_bond_assign();

  class  Angle_db_statementContext : public antlr4::ParserRuleContext {
  public:
    Angle_db_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Angle_db_assignContext *angle_db_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *DerivFlag();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Expectation();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Error();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Size();
    antlr4::tree::TerminalNode *AngleDb();
    antlr4::tree::TerminalNode *Dihedral();
    antlr4::tree::TerminalNode *Zero();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_db_statementContext* angle_db_statement();

  class  Angle_db_assignContext : public antlr4::ParserRuleContext {
  public:
    Angle_db_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_db_assignContext* angle_db_assign();

  class  Ncs_restraintContext : public antlr4::ParserRuleContext {
  public:
    Ncs_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Ncs();
    antlr4::tree::TerminalNode *Restraints();
    antlr4::tree::TerminalNode *End();
    std::vector<Ncs_statementContext *> ncs_statement();
    Ncs_statementContext* ncs_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ncs_restraintContext* ncs_restraint();

  class  Ncs_statementContext : public antlr4::ParserRuleContext {
  public:
    Ncs_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Group();
    antlr4::tree::TerminalNode *End();
    std::vector<Ncs_group_statementContext *> ncs_group_statement();
    Ncs_group_statementContext* ncs_group_statement(size_t i);
    antlr4::tree::TerminalNode *Initialize();
    antlr4::tree::TerminalNode *Print_any();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ncs_statementContext* ncs_statement();

  class  Ncs_group_statementContext : public antlr4::ParserRuleContext {
  public:
    Ncs_group_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Equivalence();
    SelectionContext *selection();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Sigb();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Weight();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ncs_group_statementContext* ncs_group_statement();

  class  SelectionContext : public antlr4::ParserRuleContext {
  public:
    SelectionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_paren();
    Selection_expressionContext *selection_expression();
    antlr4::tree::TerminalNode *R_paren();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  SelectionContext* selection();

  class  Selection_expressionContext : public antlr4::ParserRuleContext {
  public:
    Selection_expressionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<TermContext *> term();
    TermContext* term(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Or_op();
    antlr4::tree::TerminalNode* Or_op(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Selection_expressionContext* selection_expression();

  class  TermContext : public antlr4::ParserRuleContext {
  public:
    TermContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<FactorContext *> factor();
    FactorContext* factor(size_t i);
    std::vector<antlr4::tree::TerminalNode *> And_op();
    antlr4::tree::TerminalNode* And_op(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  TermContext* term();

  class  FactorContext : public antlr4::ParserRuleContext {
  public:
    FactorContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_paren();
    Selection_expressionContext *selection_expression();
    antlr4::tree::TerminalNode *R_paren();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Atom();
    std::vector<antlr4::tree::TerminalNode *> Simple_names();
    antlr4::tree::TerminalNode* Simple_names(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string();
    antlr4::tree::TerminalNode* Double_quote_string(size_t i);
    antlr4::tree::TerminalNode *Integers();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Logical();
    antlr4::tree::TerminalNode *Attribute();
    antlr4::tree::TerminalNode *Attr_properties();
    antlr4::tree::TerminalNode *Comparison_ops();
    std::vector<Number_fContext *> number_f();
    Number_fContext* number_f(size_t i);
    antlr4::tree::TerminalNode *Abs();
    antlr4::tree::TerminalNode *BondedTo();
    FactorContext *factor();
    antlr4::tree::TerminalNode *ByGroup();
    antlr4::tree::TerminalNode *ByRes();
    antlr4::tree::TerminalNode *Chemical();
    antlr4::tree::TerminalNode *Symbol_name();
    antlr4::tree::TerminalNode *Colon();
    antlr4::tree::TerminalNode *Fbox();
    antlr4::tree::TerminalNode *Hydrogen();
    antlr4::tree::TerminalNode *Id();
    antlr4::tree::TerminalNode *Known();
    antlr4::tree::TerminalNode *Name();
    antlr4::tree::TerminalNode *NONE();
    antlr4::tree::TerminalNode *Not_op();
    antlr4::tree::TerminalNode *Point();
    antlr4::tree::TerminalNode *Cut();
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);
    antlr4::tree::TerminalNode *Tail();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Equ_op();
    antlr4::tree::TerminalNode* Equ_op(size_t i);
    antlr4::tree::TerminalNode *Head();
    antlr4::tree::TerminalNode *Previous();
    antlr4::tree::TerminalNode *Pseudo();
    antlr4::tree::TerminalNode *Residue();
    antlr4::tree::TerminalNode *Resname();
    antlr4::tree::TerminalNode *SegIdentifier();
    antlr4::tree::TerminalNode *Sfbox();
    antlr4::tree::TerminalNode *Store1();
    antlr4::tree::TerminalNode *Store2();
    antlr4::tree::TerminalNode *Store3();
    antlr4::tree::TerminalNode *Store4();
    antlr4::tree::TerminalNode *Store5();
    antlr4::tree::TerminalNode *Store6();
    antlr4::tree::TerminalNode *Store7();
    antlr4::tree::TerminalNode *Store8();
    antlr4::tree::TerminalNode *Store9();
    antlr4::tree::TerminalNode *Tag();
    antlr4::tree::TerminalNode *Around();
    antlr4::tree::TerminalNode *Saround();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  FactorContext* factor();
  FactorContext* factor(int precedence);
  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Symbol_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  Number_fContext : public antlr4::ParserRuleContext {
  public:
    Number_fContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Number_fContext* number_f();

  class  Number_sContext : public antlr4::ParserRuleContext {
  public:
    Number_sContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Symbol_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Number_sContext* number_s();

  class  Number_aContext : public antlr4::ParserRuleContext {
  public:
    Number_aContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Number_aContext* number_a();

  class  ClassificationContext : public antlr4::ParserRuleContext {
  public:
    ClassificationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Classification();
    antlr4::tree::TerminalNode *Class_name();
    antlr4::tree::TerminalNode *Equ_op_CL();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ClassificationContext* classification();

  class  Class_nameContext : public antlr4::ParserRuleContext {
  public:
    Class_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Noe();
    antlr4::tree::TerminalNode *Restraints();
    antlr4::tree::TerminalNode *AngleDb();
    antlr4::tree::TerminalNode *HBonded();
    antlr4::tree::TerminalNode *Dihedral();
    antlr4::tree::TerminalNode *Improper();
    antlr4::tree::TerminalNode *Average();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Class_nameContext* class_name();

  class  Flag_statementContext : public antlr4::ParserRuleContext {
  public:
    Flag_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Flags();
    antlr4::tree::TerminalNode *Include();
    antlr4::tree::TerminalNode *End_FL();
    antlr4::tree::TerminalNode *Exclude();
    std::vector<antlr4::tree::TerminalNode *> Class_name_FL();
    antlr4::tree::TerminalNode* Class_name_FL(size_t i);
    antlr4::tree::TerminalNode *Any_class();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Flag_statementContext* flag_statement();

  class  Vector_statementContext : public antlr4::ParserRuleContext {
  public:
    Vector_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vector();
    Vector_modeContext *vector_mode();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vector_statementContext* vector_statement();

  class  Vector_modeContext : public antlr4::ParserRuleContext {
  public:
    Vector_modeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Vector_expressionContext *vector_expression();
    antlr4::tree::TerminalNode *R_paren_VE();
    antlr4::tree::TerminalNode *Do_Lp();
    antlr4::tree::TerminalNode *Identity_Lp();
    antlr4::tree::TerminalNode *Show();
    Vector_show_propertyContext *vector_show_property();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vector_modeContext* vector_mode();

  class  Vector_expressionContext : public antlr4::ParserRuleContext {
  public:
    Vector_expressionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Atom_properties_VE();
    antlr4::tree::TerminalNode *Equ_op_VE();
    Vector_operationContext *vector_operation();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vector_expressionContext* vector_expression();

  class  Vector_operationContext : public antlr4::ParserRuleContext {
  public:
    Vector_operationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VflcContext *vflc();
    Vector_operationContext *vector_operation();
    antlr4::tree::TerminalNode *Add_op_VE();
    antlr4::tree::TerminalNode *Sub_op_VE();
    antlr4::tree::TerminalNode *Mul_op_VE();
    antlr4::tree::TerminalNode *Div_op_VE();
    antlr4::tree::TerminalNode *Exp_op_VE();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vector_operationContext* vector_operation();

  class  VflcContext : public antlr4::ParserRuleContext {
  public:
    VflcContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Atom_properties_VE();
    Vector_func_callContext *vector_func_call();
    antlr4::tree::TerminalNode *Integer_VE();
    antlr4::tree::TerminalNode *Real_VE();
    antlr4::tree::TerminalNode *Simple_name_VE();
    antlr4::tree::TerminalNode *Symbol_name_VE();
    antlr4::tree::TerminalNode *Double_quote_string_VE();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  VflcContext* vflc();

  class  Vector_func_callContext : public antlr4::ParserRuleContext {
  public:
    Vector_func_callContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Abs_VE();
    antlr4::tree::TerminalNode *L_paren_VF();
    std::vector<VflcContext *> vflc();
    VflcContext* vflc(size_t i);
    antlr4::tree::TerminalNode *R_paren_VE();
    antlr4::tree::TerminalNode *Acos_VE();
    antlr4::tree::TerminalNode *Cos_VE();
    antlr4::tree::TerminalNode *Decode_VE();
    antlr4::tree::TerminalNode *Encode_VE();
    antlr4::tree::TerminalNode *Exp_VE();
    antlr4::tree::TerminalNode *Gauss_VE();
    antlr4::tree::TerminalNode *Heavy_VE();
    antlr4::tree::TerminalNode *Int_VE();
    antlr4::tree::TerminalNode *Log10_VE();
    antlr4::tree::TerminalNode *Log_VE();
    antlr4::tree::TerminalNode *Max_VE();
    std::vector<antlr4::tree::TerminalNode *> Comma_VE();
    antlr4::tree::TerminalNode* Comma_VE(size_t i);
    antlr4::tree::TerminalNode *Maxw_VE();
    antlr4::tree::TerminalNode *Min_VE();
    antlr4::tree::TerminalNode *Mod_VE();
    antlr4::tree::TerminalNode *Norm_VE();
    antlr4::tree::TerminalNode *Random_VE();
    antlr4::tree::TerminalNode *Sign_VE();
    antlr4::tree::TerminalNode *Sin_VE();
    antlr4::tree::TerminalNode *Sqrt_VE();
    antlr4::tree::TerminalNode *Tan_VE();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vector_func_callContext* vector_func_call();

  class  Vector_show_propertyContext : public antlr4::ParserRuleContext {
  public:
    Vector_show_propertyContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_paren_VS();
    antlr4::tree::TerminalNode *Atom_properties_VS();
    antlr4::tree::TerminalNode *R_paren_VS();
    antlr4::tree::TerminalNode *Average_VS();
    antlr4::tree::TerminalNode *Element_VS();
    antlr4::tree::TerminalNode *Max_VS();
    antlr4::tree::TerminalNode *Min_VS();
    antlr4::tree::TerminalNode *Norm_VS();
    antlr4::tree::TerminalNode *Rms_VS();
    antlr4::tree::TerminalNode *Sum_VS();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vector_show_propertyContext* vector_show_property();

  class  Evaluate_statementContext : public antlr4::ParserRuleContext {
  public:
    Evaluate_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Evaluate_Lp();
    antlr4::tree::TerminalNode *Symbol_name_VE();
    antlr4::tree::TerminalNode *Equ_op_VE();
    Evaluate_operationContext *evaluate_operation();
    antlr4::tree::TerminalNode *R_paren_VE();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Evaluate_statementContext* evaluate_statement();

  class  Evaluate_operationContext : public antlr4::ParserRuleContext {
  public:
    Evaluate_operationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VflcContext *vflc();
    Evaluate_operationContext *evaluate_operation();
    antlr4::tree::TerminalNode *Add_op_VE();
    antlr4::tree::TerminalNode *Sub_op_VE();
    antlr4::tree::TerminalNode *Mul_op_VE();
    antlr4::tree::TerminalNode *Div_op_VE();
    antlr4::tree::TerminalNode *Exp_op_VE();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Evaluate_operationContext* evaluate_operation();

  class  Patch_statementContext : public antlr4::ParserRuleContext {
  public:
    Patch_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Patch();
    std::vector<antlr4::tree::TerminalNode *> Reference();
    antlr4::tree::TerminalNode* Reference(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Equ_op();
    antlr4::tree::TerminalNode* Equ_op(size_t i);
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<antlr4::tree::TerminalNode *> Nil();
    antlr4::tree::TerminalNode* Nil(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    Class_nameContext *class_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Patch_statementContext* patch_statement();

  class  Parameter_settingContext : public antlr4::ParserRuleContext {
  public:
    Parameter_settingContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Parameter();
    antlr4::tree::TerminalNode *End();
    std::vector<Parameter_statementContext *> parameter_statement();
    Parameter_statementContext* parameter_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Parameter_settingContext* parameter_setting();

  class  Parameter_statementContext : public antlr4::ParserRuleContext {
  public:
    Parameter_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *AngleDb();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *UB();
    antlr4::tree::TerminalNode *BondedTo();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Dihedral();
    antlr4::tree::TerminalNode *Improper();
    antlr4::tree::TerminalNode *Mult();
    antlr4::tree::TerminalNode *HBonded();
    std::vector<antlr4::tree::TerminalNode *> Simple_names();
    antlr4::tree::TerminalNode* Simple_names(size_t i);
    antlr4::tree::TerminalNode *NBFix();
    antlr4::tree::TerminalNode *NonB();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *VDWOff();
    antlr4::tree::TerminalNode *Verbose();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Parameter_statementContext* parameter_statement();

  class  Noe_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Noe_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Noe_assignContext *> noe_assign();
    Noe_assignContext* noe_assign(size_t i);
    std::vector<Noe_assign_loopContext *> noe_assign_loop();
    Noe_assign_loopContext* noe_assign_loop(size_t i);
    std::vector<Distance_restraintContext *> distance_restraint();
    Distance_restraintContext* distance_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string_CF();
    antlr4::tree::TerminalNode* Double_quote_string_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_assign_loopContext* noe_assign_loop();

  class  Dihedral_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Dihedral_assignContext *> dihedral_assign();
    Dihedral_assignContext* dihedral_assign(size_t i);
    std::vector<Dihedral_assign_loopContext *> dihedral_assign_loop();
    Dihedral_assign_loopContext* dihedral_assign_loop(size_t i);
    std::vector<Dihedral_angle_restraintContext *> dihedral_angle_restraint();
    Dihedral_angle_restraintContext* dihedral_angle_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string_CF();
    antlr4::tree::TerminalNode* Double_quote_string_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_assign_loopContext* dihedral_assign_loop();

  class  Sani_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Sani_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Sani_assignContext *> sani_assign();
    Sani_assignContext* sani_assign(size_t i);
    std::vector<Sani_assign_loopContext *> sani_assign_loop();
    Sani_assign_loopContext* sani_assign_loop(size_t i);
    std::vector<Rdc_restraintContext *> rdc_restraint();
    Rdc_restraintContext* rdc_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string_CF();
    antlr4::tree::TerminalNode* Double_quote_string_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Sani_assign_loopContext* sani_assign_loop();

  class  Coup_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Coup_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Coup_assignContext *> coup_assign();
    Coup_assignContext* coup_assign(size_t i);
    std::vector<Coup_assign_loopContext *> coup_assign_loop();
    Coup_assign_loopContext* coup_assign_loop(size_t i);
    std::vector<Coupling_restraintContext *> coupling_restraint();
    Coupling_restraintContext* coupling_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string_CF();
    antlr4::tree::TerminalNode* Double_quote_string_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coup_assign_loopContext* coup_assign_loop();

  class  Carbon_shift_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Carbon_shift_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Carbon_shift_assignContext *> carbon_shift_assign();
    Carbon_shift_assignContext* carbon_shift_assign(size_t i);
    std::vector<Carbon_shift_assign_loopContext *> carbon_shift_assign_loop();
    Carbon_shift_assign_loopContext* carbon_shift_assign_loop(size_t i);
    std::vector<Carbon_shift_restraintContext *> carbon_shift_restraint();
    Carbon_shift_restraintContext* carbon_shift_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string_CF();
    antlr4::tree::TerminalNode* Double_quote_string_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Carbon_shift_assign_loopContext* carbon_shift_assign_loop();

  class  Plane_group_loopContext : public antlr4::ParserRuleContext {
  public:
    Plane_group_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Plane_groupContext *> plane_group();
    Plane_groupContext* plane_group(size_t i);
    std::vector<Plane_group_loopContext *> plane_group_loop();
    Plane_group_loopContext* plane_group_loop(size_t i);
    std::vector<Plane_restraintContext *> plane_restraint();
    Plane_restraintContext* plane_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string_CF();
    antlr4::tree::TerminalNode* Double_quote_string_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Plane_group_loopContext* plane_group_loop();


  bool sempred(antlr4::RuleContext *_localctx, size_t ruleIndex, size_t predicateIndex) override;

  bool factorSempred(FactorContext *_localctx, size_t predicateIndex);

  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

