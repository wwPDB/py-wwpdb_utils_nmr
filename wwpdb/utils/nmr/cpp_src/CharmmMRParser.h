
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CharmmMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CharmmMRParser : public antlr4::Parser {
public:
  enum {
    Set = 1, End = 2, Cons = 3, Harmonic = 4, Absolute = 5, Bestfit = 6, 
    Relative = 7, Clear = 8, Force = 9, Mass = 10, Weight = 11, Exponent = 12, 
    XScale = 13, YScale = 14, ZScale = 15, NoRotation = 16, NoTranslation = 17, 
    Main = 18, Comp = 19, Keep = 20, Dihedral = 21, ByNumber = 22, Min = 23, 
    Period = 24, Width = 25, ClDh = 26, IC = 27, Bond = 28, Upper = 29, 
    Angle = 30, Improper = 31, Droplet = 32, NoMass = 33, Fix = 34, Purg = 35, 
    Thet = 36, Phi = 37, Imph = 38, Hmcm = 39, RefX = 40, RefY = 41, RefZ = 42, 
    Shake = 43, Off = 44, NoReset = 45, BonH = 46, Tol = 47, MxIter = 48, 
    AngH = 49, Parameters = 50, ShkScale = 51, Fast = 52, Water = 53, NoFast = 54, 
    Noe = 55, Reset = 56, PNoe = 57, Assign = 58, KMin = 59, KMax = 60, 
    RMin = 61, RMax = 62, FMax = 63, MinDist = 64, RSwi = 65, SExp = 66, 
    SumR = 67, TCon = 68, RExp = 69, CnoX = 70, CnoY = 71, CnoZ = 72, MPNoe = 73, 
    INoe = 74, TnoX = 75, TnoY = 76, TnoZ = 77, NMPNoe = 78, Read = 79, 
    Write = 80, Unit = 81, Print = 82, Anal = 83, Cut = 84, Scale = 85, 
    Temperature = 86, ResDistance = 87, KVal = 88, RVal = 89, EVal = 90, 
    IVal = 91, Positive = 92, Negative = 93, Pull = 94, XDir = 95, YDir = 96, 
    ZDir = 97, EField = 98, List = 99, Switch = 100, SForce = 101, RMSD = 102, 
    MaxN = 103, NPrt = 104, Show = 105, Offset = 106, BOffset = 107, RGyration = 108, 
    Reference = 109, Orient = 110, Output = 111, NSave = 112, DMConstrain = 113, 
    Cutoff = 114, NContact = 115, Selection = 116, Or_op = 117, And_op = 118, 
    Not_op = 119, Around = 120, Subset = 121, Bonded = 122, ByRes = 123, 
    ByGroup = 124, SegIdentifier = 125, ISeg = 126, Residue = 127, IRes = 128, 
    Resname = 129, IGroup = 130, Type = 131, Chemical = 132, Atom = 133, 
    Property = 134, Point = 135, Initial = 136, Lone = 137, Hydrogen = 138, 
    User = 139, Previous = 140, Recall = 141, All = 142, NONE = 143, Integer = 144, 
    Real = 145, Double_quote_string = 146, SMCLN_COMMENT = 147, COMMENT = 148, 
    Simple_name = 149, Simple_names = 150, Integers = 151, L_paren = 152, 
    R_paren = 153, Colon = 154, Equ_op = 155, Lt_op = 156, Gt_op = 157, 
    Leq_op = 158, Geq_op = 159, Neq_op = 160, Aeq_op = 161, Symbol_name = 162, 
    SPACE = 163, CONTINUE = 164, ENCLOSE_COMMENT = 165, SECTION_COMMENT = 166, 
    LINE_COMMENT = 167, Equ_op_VE = 168, Integer_VE = 169, Real_VE = 170, 
    Simple_name_VE = 171, SPACE_VE = 172, RETURN_VE = 173, Any_name = 174, 
    SPACE_CM = 175, RETURN_CM = 176, Abs = 177, Attr_properties = 178, Comparison_ops = 179, 
    SPACE_AP = 180
  };

  enum {
    RuleCharmm_mr = 0, RuleComment = 1, RuleDistance_restraint = 2, RulePoint_distance_restraint = 3, 
    RuleDihedral_angle_restraint = 4, RuleHarmonic_restraint = 5, RuleManipulate_internal_coordinate = 6, 
    RuleDroplet_potential = 7, RuleFix_atom_constraint = 8, RuleCenter_of_mass_constraint = 9, 
    RuleFix_bond_or_angle_constraint = 10, RuleRestrained_distance = 11, 
    RuleExternal_force = 12, RuleRmsd_restraint = 13, RuleGyration_restraint = 14, 
    RuleDistance_matrix_restraint = 15, RuleNoe_statement = 16, RuleNoe_assign = 17, 
    RulePnoe_statement = 18, RulePnoe_assign = 19, RuleDihedral_statement = 20, 
    RuleDihedral_assign = 21, RuleHarmonic_statement = 22, RuleAbsolute_spec = 23, 
    RuleForce_const_spec = 24, RuleBestfit_spec = 25, RuleCoordinate_spec = 26, 
    RuleIc_statement = 27, RuleDroplet_statement = 28, RuleFix_atom_statement = 29, 
    RuleCenter_of_mass_statement = 30, RuleFix_bond_or_angle_statement = 31, 
    RuleShake_opt = 32, RuleFast_opt = 33, RuleRestrained_distance_statement = 34, 
    RuleExternal_force_statement = 35, RuleRmsd_statement = 36, RuleRmsd_orient_spec = 37, 
    RuleRmsd_force_const_spec = 38, RuleRmsd_coordinate_spec = 39, RuleGyration_statement = 40, 
    RuleDistance_matrix_statement = 41, RuleSelection = 42, RuleSelection_expression = 43, 
    RuleTerm = 44, RuleFactor = 45, RuleNumber = 46, RuleNumber_f = 47, 
    RuleNumber_s = 48, RuleSet_statement = 49
  };

  explicit CharmmMRParser(antlr4::TokenStream *input);

  CharmmMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~CharmmMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Charmm_mrContext;
  class CommentContext;
  class Distance_restraintContext;
  class Point_distance_restraintContext;
  class Dihedral_angle_restraintContext;
  class Harmonic_restraintContext;
  class Manipulate_internal_coordinateContext;
  class Droplet_potentialContext;
  class Fix_atom_constraintContext;
  class Center_of_mass_constraintContext;
  class Fix_bond_or_angle_constraintContext;
  class Restrained_distanceContext;
  class External_forceContext;
  class Rmsd_restraintContext;
  class Gyration_restraintContext;
  class Distance_matrix_restraintContext;
  class Noe_statementContext;
  class Noe_assignContext;
  class Pnoe_statementContext;
  class Pnoe_assignContext;
  class Dihedral_statementContext;
  class Dihedral_assignContext;
  class Harmonic_statementContext;
  class Absolute_specContext;
  class Force_const_specContext;
  class Bestfit_specContext;
  class Coordinate_specContext;
  class Ic_statementContext;
  class Droplet_statementContext;
  class Fix_atom_statementContext;
  class Center_of_mass_statementContext;
  class Fix_bond_or_angle_statementContext;
  class Shake_optContext;
  class Fast_optContext;
  class Restrained_distance_statementContext;
  class External_force_statementContext;
  class Rmsd_statementContext;
  class Rmsd_orient_specContext;
  class Rmsd_force_const_specContext;
  class Rmsd_coordinate_specContext;
  class Gyration_statementContext;
  class Distance_matrix_statementContext;
  class SelectionContext;
  class Selection_expressionContext;
  class TermContext;
  class FactorContext;
  class NumberContext;
  class Number_fContext;
  class Number_sContext;
  class Set_statementContext; 

  class  Charmm_mrContext : public antlr4::ParserRuleContext {
  public:
    Charmm_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<Distance_restraintContext *> distance_restraint();
    Distance_restraintContext* distance_restraint(size_t i);
    std::vector<Point_distance_restraintContext *> point_distance_restraint();
    Point_distance_restraintContext* point_distance_restraint(size_t i);
    std::vector<Dihedral_angle_restraintContext *> dihedral_angle_restraint();
    Dihedral_angle_restraintContext* dihedral_angle_restraint(size_t i);
    std::vector<Harmonic_restraintContext *> harmonic_restraint();
    Harmonic_restraintContext* harmonic_restraint(size_t i);
    std::vector<Manipulate_internal_coordinateContext *> manipulate_internal_coordinate();
    Manipulate_internal_coordinateContext* manipulate_internal_coordinate(size_t i);
    std::vector<Droplet_potentialContext *> droplet_potential();
    Droplet_potentialContext* droplet_potential(size_t i);
    std::vector<Fix_atom_constraintContext *> fix_atom_constraint();
    Fix_atom_constraintContext* fix_atom_constraint(size_t i);
    std::vector<Center_of_mass_constraintContext *> center_of_mass_constraint();
    Center_of_mass_constraintContext* center_of_mass_constraint(size_t i);
    std::vector<Fix_bond_or_angle_constraintContext *> fix_bond_or_angle_constraint();
    Fix_bond_or_angle_constraintContext* fix_bond_or_angle_constraint(size_t i);
    std::vector<Restrained_distanceContext *> restrained_distance();
    Restrained_distanceContext* restrained_distance(size_t i);
    std::vector<External_forceContext *> external_force();
    External_forceContext* external_force(size_t i);
    std::vector<Rmsd_restraintContext *> rmsd_restraint();
    Rmsd_restraintContext* rmsd_restraint(size_t i);
    std::vector<Gyration_restraintContext *> gyration_restraint();
    Gyration_restraintContext* gyration_restraint(size_t i);
    std::vector<Distance_matrix_restraintContext *> distance_matrix_restraint();
    Distance_matrix_restraintContext* distance_matrix_restraint(size_t i);
    std::vector<Set_statementContext *> set_statement();
    Set_statementContext* set_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Charmm_mrContext* charmm_mr();

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

  class  Point_distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Point_distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *PNoe();
    antlr4::tree::TerminalNode *End();
    std::vector<Pnoe_statementContext *> pnoe_statement();
    Pnoe_statementContext* pnoe_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Point_distance_restraintContext* point_distance_restraint();

  class  Dihedral_angle_restraintContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Cons();
    antlr4::tree::TerminalNode *Dihedral();
    antlr4::tree::TerminalNode *ClDh();
    std::vector<Dihedral_statementContext *> dihedral_statement();
    Dihedral_statementContext* dihedral_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_restraintContext* dihedral_angle_restraint();

  class  Harmonic_restraintContext : public antlr4::ParserRuleContext {
  public:
    Harmonic_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Cons();
    antlr4::tree::TerminalNode *Harmonic();
    std::vector<Harmonic_statementContext *> harmonic_statement();
    Harmonic_statementContext* harmonic_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Harmonic_restraintContext* harmonic_restraint();

  class  Manipulate_internal_coordinateContext : public antlr4::ParserRuleContext {
  public:
    Manipulate_internal_coordinateContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Cons();
    antlr4::tree::TerminalNode *IC();
    std::vector<Ic_statementContext *> ic_statement();
    Ic_statementContext* ic_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Manipulate_internal_coordinateContext* manipulate_internal_coordinate();

  class  Droplet_potentialContext : public antlr4::ParserRuleContext {
  public:
    Droplet_potentialContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Cons();
    antlr4::tree::TerminalNode *Droplet();
    std::vector<Droplet_statementContext *> droplet_statement();
    Droplet_statementContext* droplet_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Droplet_potentialContext* droplet_potential();

  class  Fix_atom_constraintContext : public antlr4::ParserRuleContext {
  public:
    Fix_atom_constraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Cons();
    antlr4::tree::TerminalNode *Fix();
    std::vector<Fix_atom_statementContext *> fix_atom_statement();
    Fix_atom_statementContext* fix_atom_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fix_atom_constraintContext* fix_atom_constraint();

  class  Center_of_mass_constraintContext : public antlr4::ParserRuleContext {
  public:
    Center_of_mass_constraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Cons();
    antlr4::tree::TerminalNode *Hmcm();
    std::vector<Center_of_mass_statementContext *> center_of_mass_statement();
    Center_of_mass_statementContext* center_of_mass_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Center_of_mass_constraintContext* center_of_mass_constraint();

  class  Fix_bond_or_angle_constraintContext : public antlr4::ParserRuleContext {
  public:
    Fix_bond_or_angle_constraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Shake();
    antlr4::tree::TerminalNode *Off();
    std::vector<Fix_bond_or_angle_statementContext *> fix_bond_or_angle_statement();
    Fix_bond_or_angle_statementContext* fix_bond_or_angle_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fix_bond_or_angle_constraintContext* fix_bond_or_angle_constraint();

  class  Restrained_distanceContext : public antlr4::ParserRuleContext {
  public:
    Restrained_distanceContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ResDistance();
    std::vector<Restrained_distance_statementContext *> restrained_distance_statement();
    Restrained_distance_statementContext* restrained_distance_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Restrained_distanceContext* restrained_distance();

  class  External_forceContext : public antlr4::ParserRuleContext {
  public:
    External_forceContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Pull();
    std::vector<External_force_statementContext *> external_force_statement();
    External_force_statementContext* external_force_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  External_forceContext* external_force();

  class  Rmsd_restraintContext : public antlr4::ParserRuleContext {
  public:
    Rmsd_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Cons();
    antlr4::tree::TerminalNode *RMSD();
    antlr4::tree::TerminalNode *Show();
    antlr4::tree::TerminalNode *Clear();
    std::vector<Rmsd_statementContext *> rmsd_statement();
    Rmsd_statementContext* rmsd_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rmsd_restraintContext* rmsd_restraint();

  class  Gyration_restraintContext : public antlr4::ParserRuleContext {
  public:
    Gyration_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RGyration();
    std::vector<Gyration_statementContext *> gyration_statement();
    Gyration_statementContext* gyration_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Gyration_restraintContext* gyration_restraint();

  class  Distance_matrix_restraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_matrix_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *DMConstrain();
    std::vector<Distance_matrix_statementContext *> distance_matrix_statement();
    Distance_matrix_statementContext* distance_matrix_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_matrix_restraintContext* distance_matrix_restraint();

  class  Noe_statementContext : public antlr4::ParserRuleContext {
  public:
    Noe_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Noe_assignContext *noe_assign();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *KMin();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *RMin();
    antlr4::tree::TerminalNode *KMax();
    antlr4::tree::TerminalNode *RMax();
    antlr4::tree::TerminalNode *FMax();
    antlr4::tree::TerminalNode *MinDist();
    antlr4::tree::TerminalNode *RSwi();
    antlr4::tree::TerminalNode *SExp();
    antlr4::tree::TerminalNode *SumR();
    antlr4::tree::TerminalNode *TCon();
    antlr4::tree::TerminalNode *RExp();
    antlr4::tree::TerminalNode *MPNoe();
    antlr4::tree::TerminalNode *INoe();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *TnoX();
    antlr4::tree::TerminalNode *TnoY();
    antlr4::tree::TerminalNode *TnoZ();
    antlr4::tree::TerminalNode *NMPNoe();
    antlr4::tree::TerminalNode *Read();
    antlr4::tree::TerminalNode *Unit();
    antlr4::tree::TerminalNode *Write();
    antlr4::tree::TerminalNode *Anal();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Cut();
    antlr4::tree::TerminalNode *Scale();
    antlr4::tree::TerminalNode *Temperature();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_statementContext* noe_statement();

  class  Noe_assignContext : public antlr4::ParserRuleContext {
  public:
    Noe_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_assignContext* noe_assign();

  class  Pnoe_statementContext : public antlr4::ParserRuleContext {
  public:
    Pnoe_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Pnoe_assignContext *pnoe_assign();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *KMin();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *RMin();
    antlr4::tree::TerminalNode *KMax();
    antlr4::tree::TerminalNode *RMax();
    antlr4::tree::TerminalNode *FMax();
    antlr4::tree::TerminalNode *CnoX();
    antlr4::tree::TerminalNode *CnoY();
    antlr4::tree::TerminalNode *CnoZ();
    antlr4::tree::TerminalNode *MinDist();
    antlr4::tree::TerminalNode *RSwi();
    antlr4::tree::TerminalNode *SExp();
    antlr4::tree::TerminalNode *SumR();
    antlr4::tree::TerminalNode *TCon();
    antlr4::tree::TerminalNode *RExp();
    antlr4::tree::TerminalNode *MPNoe();
    antlr4::tree::TerminalNode *INoe();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *TnoX();
    antlr4::tree::TerminalNode *TnoY();
    antlr4::tree::TerminalNode *TnoZ();
    antlr4::tree::TerminalNode *NMPNoe();
    antlr4::tree::TerminalNode *Read();
    antlr4::tree::TerminalNode *Unit();
    antlr4::tree::TerminalNode *Write();
    antlr4::tree::TerminalNode *Anal();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Cut();
    antlr4::tree::TerminalNode *Scale();
    antlr4::tree::TerminalNode *Temperature();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pnoe_statementContext* pnoe_statement();

  class  Pnoe_assignContext : public antlr4::ParserRuleContext {
  public:
    Pnoe_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pnoe_assignContext* pnoe_assign();

  class  Dihedral_statementContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Dihedral_assignContext *dihedral_assign();
    antlr4::tree::TerminalNode *Force();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Min();
    antlr4::tree::TerminalNode *Period();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Comp();
    antlr4::tree::TerminalNode *Width();
    antlr4::tree::TerminalNode *Main();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_statementContext* dihedral_statement();

  class  Dihedral_assignContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    antlr4::tree::TerminalNode *ByNumber();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_assignContext* dihedral_assign();

  class  Harmonic_statementContext : public antlr4::ParserRuleContext {
  public:
    Harmonic_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    antlr4::tree::TerminalNode *Absolute();
    std::vector<Absolute_specContext *> absolute_spec();
    Absolute_specContext* absolute_spec(size_t i);
    std::vector<Force_const_specContext *> force_const_spec();
    Force_const_specContext* force_const_spec(size_t i);
    Coordinate_specContext *coordinate_spec();
    antlr4::tree::TerminalNode *Bestfit();
    Bestfit_specContext *bestfit_spec();
    antlr4::tree::TerminalNode *Relative();
    antlr4::tree::TerminalNode *Clear();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Harmonic_statementContext* harmonic_statement();

  class  Absolute_specContext : public antlr4::ParserRuleContext {
  public:
    Absolute_specContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Exponent();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *XScale();
    NumberContext *number();
    antlr4::tree::TerminalNode *YScale();
    antlr4::tree::TerminalNode *ZScale();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Absolute_specContext* absolute_spec();

  class  Force_const_specContext : public antlr4::ParserRuleContext {
  public:
    Force_const_specContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Force();
    NumberContext *number();
    antlr4::tree::TerminalNode *Mass();
    antlr4::tree::TerminalNode *Weight();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Force_const_specContext* force_const_spec();

  class  Bestfit_specContext : public antlr4::ParserRuleContext {
  public:
    Bestfit_specContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *NoRotation();
    antlr4::tree::TerminalNode *NoTranslation();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Bestfit_specContext* bestfit_spec();

  class  Coordinate_specContext : public antlr4::ParserRuleContext {
  public:
    Coordinate_specContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Main();
    antlr4::tree::TerminalNode *Comp();
    antlr4::tree::TerminalNode *Keep();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coordinate_specContext* coordinate_spec();

  class  Ic_statementContext : public antlr4::ParserRuleContext {
  public:
    Ic_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Bond();
    NumberContext *number();
    antlr4::tree::TerminalNode *Exponent();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Upper();
    antlr4::tree::TerminalNode *Angle();
    antlr4::tree::TerminalNode *Dihedral();
    antlr4::tree::TerminalNode *Improper();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ic_statementContext* ic_statement();

  class  Droplet_statementContext : public antlr4::ParserRuleContext {
  public:
    Droplet_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Force();
    NumberContext *number();
    antlr4::tree::TerminalNode *Exponent();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *NoMass();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Droplet_statementContext* droplet_statement();

  class  Fix_atom_statementContext : public antlr4::ParserRuleContext {
  public:
    Fix_atom_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    SelectionContext *selection();
    antlr4::tree::TerminalNode *Purg();
    antlr4::tree::TerminalNode *Bond();
    antlr4::tree::TerminalNode *Thet();
    antlr4::tree::TerminalNode *Phi();
    antlr4::tree::TerminalNode *Imph();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fix_atom_statementContext* fix_atom_statement();

  class  Center_of_mass_statementContext : public antlr4::ParserRuleContext {
  public:
    Center_of_mass_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Force();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RefX();
    antlr4::tree::TerminalNode *RefY();
    antlr4::tree::TerminalNode *RefZ();
    SelectionContext *selection();
    antlr4::tree::TerminalNode *Weight();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Center_of_mass_statementContext* center_of_mass_statement();

  class  Fix_bond_or_angle_statementContext : public antlr4::ParserRuleContext {
  public:
    Fix_bond_or_angle_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    Shake_optContext *shake_opt();
    Fast_optContext *fast_opt();
    antlr4::tree::TerminalNode *NoReset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fix_bond_or_angle_statementContext* fix_bond_or_angle_statement();

  class  Shake_optContext : public antlr4::ParserRuleContext {
  public:
    Shake_optContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *BonH();
    antlr4::tree::TerminalNode *Bond();
    antlr4::tree::TerminalNode *AngH();
    antlr4::tree::TerminalNode *Angle();
    antlr4::tree::TerminalNode *Comp();
    antlr4::tree::TerminalNode *Parameters();
    antlr4::tree::TerminalNode *Tol();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *MxIter();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *ShkScale();
    antlr4::tree::TerminalNode *Main();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Shake_optContext* shake_opt();

  class  Fast_optContext : public antlr4::ParserRuleContext {
  public:
    Fast_optContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Fast();
    antlr4::tree::TerminalNode *Water();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *NoFast();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fast_optContext* fast_opt();

  class  Restrained_distance_statementContext : public antlr4::ParserRuleContext {
  public:
    Restrained_distance_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Reset();
    NumberContext *number();
    antlr4::tree::TerminalNode *Scale();
    antlr4::tree::TerminalNode *KVal();
    antlr4::tree::TerminalNode *RVal();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *EVal();
    antlr4::tree::TerminalNode *IVal();
    antlr4::tree::TerminalNode *Positive();
    antlr4::tree::TerminalNode *Negative();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Restrained_distance_statementContext* restrained_distance_statement();

  class  External_force_statementContext : public antlr4::ParserRuleContext {
  public:
    External_force_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Force();
    NumberContext *number();
    antlr4::tree::TerminalNode *XDir();
    antlr4::tree::TerminalNode *YDir();
    antlr4::tree::TerminalNode *ZDir();
    antlr4::tree::TerminalNode *Period();
    antlr4::tree::TerminalNode *EField();
    antlr4::tree::TerminalNode *SForce();
    antlr4::tree::TerminalNode *Off();
    antlr4::tree::TerminalNode *List();
    antlr4::tree::TerminalNode *Switch();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Weight();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  External_force_statementContext* external_force_statement();

  class  Rmsd_statementContext : public antlr4::ParserRuleContext {
  public:
    Rmsd_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Relative();
    antlr4::tree::TerminalNode *MaxN();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *NPrt();
    Rmsd_orient_specContext *rmsd_orient_spec();
    Rmsd_force_const_specContext *rmsd_force_const_spec();
    Rmsd_coordinate_specContext *rmsd_coordinate_spec();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rmsd_statementContext* rmsd_statement();

  class  Rmsd_orient_specContext : public antlr4::ParserRuleContext {
  public:
    Rmsd_orient_specContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *NoRotation();
    antlr4::tree::TerminalNode *NoTranslation();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rmsd_orient_specContext* rmsd_orient_spec();

  class  Rmsd_force_const_specContext : public antlr4::ParserRuleContext {
  public:
    Rmsd_force_const_specContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Force();
    NumberContext *number();
    antlr4::tree::TerminalNode *Mass();
    antlr4::tree::TerminalNode *Offset();
    antlr4::tree::TerminalNode *BOffset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rmsd_force_const_specContext* rmsd_force_const_spec();

  class  Rmsd_coordinate_specContext : public antlr4::ParserRuleContext {
  public:
    Rmsd_coordinate_specContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Main();
    antlr4::tree::TerminalNode *Comp();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rmsd_coordinate_specContext* rmsd_coordinate_spec();

  class  Gyration_statementContext : public antlr4::ParserRuleContext {
  public:
    Gyration_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Reset();
    NumberContext *number();
    antlr4::tree::TerminalNode *Force();
    antlr4::tree::TerminalNode *Reference();
    antlr4::tree::TerminalNode *RMSD();
    antlr4::tree::TerminalNode *Comp();
    antlr4::tree::TerminalNode *Orient();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Output();
    antlr4::tree::TerminalNode *NSave();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Gyration_statementContext* gyration_statement();

  class  Distance_matrix_statementContext : public antlr4::ParserRuleContext {
  public:
    Distance_matrix_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    NumberContext *number();
    antlr4::tree::TerminalNode *Force();
    antlr4::tree::TerminalNode *Reference();
    antlr4::tree::TerminalNode *Cutoff();
    antlr4::tree::TerminalNode *Weight();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Output();
    antlr4::tree::TerminalNode *NSave();
    antlr4::tree::TerminalNode *NContact();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_matrix_statementContext* distance_matrix_statement();

  class  SelectionContext : public antlr4::ParserRuleContext {
  public:
    SelectionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Selection();
    Selection_expressionContext *selection_expression();
    antlr4::tree::TerminalNode *End();
    antlr4::tree::TerminalNode *Show();


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
    antlr4::tree::TerminalNode *Integers();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Property();
    antlr4::tree::TerminalNode *Attr_properties();
    antlr4::tree::TerminalNode *Comparison_ops();
    std::vector<Number_fContext *> number_f();
    Number_fContext* number_f(size_t i);
    antlr4::tree::TerminalNode *Abs();
    antlr4::tree::TerminalNode *Bonded();
    FactorContext *factor();
    antlr4::tree::TerminalNode *ByGroup();
    antlr4::tree::TerminalNode *ByRes();
    antlr4::tree::TerminalNode *Type();
    antlr4::tree::TerminalNode *Symbol_name();
    antlr4::tree::TerminalNode *Colon();
    antlr4::tree::TerminalNode *Chemical();
    antlr4::tree::TerminalNode *Initial();
    antlr4::tree::TerminalNode *Lone();
    antlr4::tree::TerminalNode *Hydrogen();
    antlr4::tree::TerminalNode *NONE();
    antlr4::tree::TerminalNode *Not_op();
    antlr4::tree::TerminalNode *Point();
    antlr4::tree::TerminalNode *Cut();
    antlr4::tree::TerminalNode *Period();
    antlr4::tree::TerminalNode *User();
    antlr4::tree::TerminalNode *Previous();
    antlr4::tree::TerminalNode *Recall();
    antlr4::tree::TerminalNode *ByNumber();
    antlr4::tree::TerminalNode *Residue();
    antlr4::tree::TerminalNode *Resname();
    antlr4::tree::TerminalNode *SegIdentifier();
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string();
    antlr4::tree::TerminalNode* Double_quote_string(size_t i);
    antlr4::tree::TerminalNode *ISeg();
    antlr4::tree::TerminalNode *IRes();
    antlr4::tree::TerminalNode *IGroup();
    antlr4::tree::TerminalNode *Around();
    antlr4::tree::TerminalNode *Subset();


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

  class  Set_statementContext : public antlr4::ParserRuleContext {
  public:
    Set_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Set();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_VE();
    antlr4::tree::TerminalNode* Simple_name_VE(size_t i);
    antlr4::tree::TerminalNode *RETURN_VE();
    antlr4::tree::TerminalNode *Real_VE();
    antlr4::tree::TerminalNode *Integer_VE();
    antlr4::tree::TerminalNode *Equ_op_VE();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Set_statementContext* set_statement();


  bool sempred(antlr4::RuleContext *_localctx, size_t ruleIndex, size_t predicateIndex) override;

  bool factorSempred(FactorContext *_localctx, size_t predicateIndex);

  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

