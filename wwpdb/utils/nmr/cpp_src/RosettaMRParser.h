
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/RosettaMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  RosettaMRParser : public antlr4::Parser {
public:
  enum {
    AtomPair = 1, NamedAtomPair = 2, Angle = 3, NamedAngle = 4, Dihedral = 5, 
    DihedralPair = 6, CoordinateConstraint = 7, LocalCoordinateConstraint = 8, 
    AmbiguousNMRDistance = 9, SiteConstraint = 10, SiteConstraintResidues = 11, 
    MinResidueAtomicDistance = 12, BigBin = 13, MultiConstraint = 14, AmbiguousConstraint = 15, 
    KofNConstraint = 16, END = 17, CIRCULARHARMONIC = 18, PERIODICBOUNDED = 19, 
    OFFSETPERIODICBOUNDED = 20, AMBERPERIODIC = 21, CHARMMPERIODIC = 22, 
    CIRCULARSIGMOIDAL = 23, CIRCULARSPLINE = 24, HARMONIC = 25, FLAT_HARMONIC = 26, 
    BOUNDED = 27, GAUSSIANFUNC = 28, WEIGHT = 29, SOGFUNC = 30, MIXTUREFUNC = 31, 
    CONSTANTFUNC = 32, IDENTITY = 33, SCALARWEIGHTEDFUNC = 34, SUMFUNC = 35, 
    SPLINE = 36, NONE = 37, FADE = 38, SIGMOID = 39, SQUARE_WELL = 40, SQUARE_WELL2 = 41, 
    DEGREES = 42, LINEAR_PENALTY = 43, KARPLUS = 44, SOEDINGFUNC = 45, TOPOUT = 46, 
    ETABLE = 47, USOG = 48, SOG = 49, Integer = 50, Float = 51, SHARP_COMMENT = 52, 
    EXCLM_COMMENT = 53, COMMENT = 54, Capital_integer = 55, Integer_capital = 56, 
    Simple_name = 57, SPACE = 58, ENCLOSE_COMMENT = 59, SECTION_COMMENT = 60, 
    LINE_COMMENT = 61, Atom_pair_selection = 62, Atom_selection = 63, Any_name = 64, 
    SPACE_CM = 65, RETURN_CM = 66
  };

  enum {
    RuleRosetta_mr = 0, RuleComment = 1, RuleAtom_pair_restraints = 2, RuleAtom_pair_restraint = 3, 
    RuleAngle_restraints = 4, RuleAngle_restraint = 5, RuleDihedral_restraints = 6, 
    RuleDihedral_restraint = 7, RuleDihedral_pair_restraints = 8, RuleDihedral_pair_restraint = 9, 
    RuleCoordinate_restraints = 10, RuleCoordinate_restraint = 11, RuleLocal_coordinate_restraints = 12, 
    RuleLocal_coordinate_restraint = 13, RuleSite_restraints = 14, RuleSite_restraint = 15, 
    RuleSite_residues_restraints = 16, RuleSite_residues_restraint = 17, 
    RuleMin_residue_atomic_distance_restraints = 18, RuleMin_residue_atomic_distance_restraint = 19, 
    RuleBig_bin_restraints = 20, RuleBig_bin_restraint = 21, RuleNested_restraints = 22, 
    RuleNested_restraint = 23, RuleAny_restraint = 24, RuleFunc_type_def = 25, 
    RuleRdc_restraints = 26, RuleRdc_restraint = 27, RuleDisulfide_bond_linkages = 28, 
    RuleDisulfide_bond_linkage = 29, RuleAtom_pair_w_chain_restraints = 30, 
    RuleAtom_pair_w_chain_restraint = 31, RuleNumber = 32, RuleNumber_f = 33, 
    RuleGen_res_num = 34, RuleGen_simple_name = 35
  };

  explicit RosettaMRParser(antlr4::TokenStream *input);

  RosettaMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~RosettaMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Rosetta_mrContext;
  class CommentContext;
  class Atom_pair_restraintsContext;
  class Atom_pair_restraintContext;
  class Angle_restraintsContext;
  class Angle_restraintContext;
  class Dihedral_restraintsContext;
  class Dihedral_restraintContext;
  class Dihedral_pair_restraintsContext;
  class Dihedral_pair_restraintContext;
  class Coordinate_restraintsContext;
  class Coordinate_restraintContext;
  class Local_coordinate_restraintsContext;
  class Local_coordinate_restraintContext;
  class Site_restraintsContext;
  class Site_restraintContext;
  class Site_residues_restraintsContext;
  class Site_residues_restraintContext;
  class Min_residue_atomic_distance_restraintsContext;
  class Min_residue_atomic_distance_restraintContext;
  class Big_bin_restraintsContext;
  class Big_bin_restraintContext;
  class Nested_restraintsContext;
  class Nested_restraintContext;
  class Any_restraintContext;
  class Func_type_defContext;
  class Rdc_restraintsContext;
  class Rdc_restraintContext;
  class Disulfide_bond_linkagesContext;
  class Disulfide_bond_linkageContext;
  class Atom_pair_w_chain_restraintsContext;
  class Atom_pair_w_chain_restraintContext;
  class NumberContext;
  class Number_fContext;
  class Gen_res_numContext;
  class Gen_simple_nameContext; 

  class  Rosetta_mrContext : public antlr4::ParserRuleContext {
  public:
    Rosetta_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<Atom_pair_restraintsContext *> atom_pair_restraints();
    Atom_pair_restraintsContext* atom_pair_restraints(size_t i);
    std::vector<Angle_restraintsContext *> angle_restraints();
    Angle_restraintsContext* angle_restraints(size_t i);
    std::vector<Dihedral_restraintsContext *> dihedral_restraints();
    Dihedral_restraintsContext* dihedral_restraints(size_t i);
    std::vector<Dihedral_pair_restraintsContext *> dihedral_pair_restraints();
    Dihedral_pair_restraintsContext* dihedral_pair_restraints(size_t i);
    std::vector<Coordinate_restraintsContext *> coordinate_restraints();
    Coordinate_restraintsContext* coordinate_restraints(size_t i);
    std::vector<Local_coordinate_restraintsContext *> local_coordinate_restraints();
    Local_coordinate_restraintsContext* local_coordinate_restraints(size_t i);
    std::vector<Site_restraintsContext *> site_restraints();
    Site_restraintsContext* site_restraints(size_t i);
    std::vector<Site_residues_restraintsContext *> site_residues_restraints();
    Site_residues_restraintsContext* site_residues_restraints(size_t i);
    std::vector<Min_residue_atomic_distance_restraintsContext *> min_residue_atomic_distance_restraints();
    Min_residue_atomic_distance_restraintsContext* min_residue_atomic_distance_restraints(size_t i);
    std::vector<Big_bin_restraintsContext *> big_bin_restraints();
    Big_bin_restraintsContext* big_bin_restraints(size_t i);
    std::vector<Nested_restraintsContext *> nested_restraints();
    Nested_restraintsContext* nested_restraints(size_t i);
    std::vector<Rdc_restraintsContext *> rdc_restraints();
    Rdc_restraintsContext* rdc_restraints(size_t i);
    std::vector<Disulfide_bond_linkagesContext *> disulfide_bond_linkages();
    Disulfide_bond_linkagesContext* disulfide_bond_linkages(size_t i);
    std::vector<Atom_pair_w_chain_restraintsContext *> atom_pair_w_chain_restraints();
    Atom_pair_w_chain_restraintsContext* atom_pair_w_chain_restraints(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rosetta_mrContext* rosetta_mr();

  class  CommentContext : public antlr4::ParserRuleContext {
  public:
    CommentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COMMENT();
    antlr4::tree::TerminalNode *RETURN_CM();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Atom_pair_selection();
    antlr4::tree::TerminalNode* Atom_pair_selection(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Atom_selection();
    antlr4::tree::TerminalNode* Atom_selection(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Any_name();
    antlr4::tree::TerminalNode* Any_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CommentContext* comment();

  class  Atom_pair_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Atom_pair_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Atom_pair_restraintContext *> atom_pair_restraint();
    Atom_pair_restraintContext* atom_pair_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_pair_restraintsContext* atom_pair_restraints();

  class  Atom_pair_restraintContext : public antlr4::ParserRuleContext {
  public:
    Atom_pair_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    Func_type_defContext *func_type_def();
    antlr4::tree::TerminalNode *AtomPair();
    antlr4::tree::TerminalNode *NamedAtomPair();
    antlr4::tree::TerminalNode *AmbiguousNMRDistance();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_pair_restraintContext* atom_pair_restraint();

  class  Angle_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Angle_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Angle_restraintContext *> angle_restraint();
    Angle_restraintContext* angle_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_restraintsContext* angle_restraints();

  class  Angle_restraintContext : public antlr4::ParserRuleContext {
  public:
    Angle_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    Func_type_defContext *func_type_def();
    antlr4::tree::TerminalNode *Angle();
    antlr4::tree::TerminalNode *NamedAngle();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_restraintContext* angle_restraint();

  class  Dihedral_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Dihedral_restraintContext *> dihedral_restraint();
    Dihedral_restraintContext* dihedral_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_restraintsContext* dihedral_restraints();

  class  Dihedral_restraintContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Dihedral();
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    Func_type_defContext *func_type_def();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_restraintContext* dihedral_restraint();

  class  Dihedral_pair_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_pair_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Dihedral_pair_restraintContext *> dihedral_pair_restraint();
    Dihedral_pair_restraintContext* dihedral_pair_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_pair_restraintsContext* dihedral_pair_restraints();

  class  Dihedral_pair_restraintContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_pair_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *DihedralPair();
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    Func_type_defContext *func_type_def();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_pair_restraintContext* dihedral_pair_restraint();

  class  Coordinate_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Coordinate_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Coordinate_restraintContext *> coordinate_restraint();
    Coordinate_restraintContext* coordinate_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coordinate_restraintsContext* coordinate_restraints();

  class  Coordinate_restraintContext : public antlr4::ParserRuleContext {
  public:
    Coordinate_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *CoordinateConstraint();
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    Func_type_defContext *func_type_def();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coordinate_restraintContext* coordinate_restraint();

  class  Local_coordinate_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Local_coordinate_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Local_coordinate_restraintContext *> local_coordinate_restraint();
    Local_coordinate_restraintContext* local_coordinate_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Local_coordinate_restraintsContext* local_coordinate_restraints();

  class  Local_coordinate_restraintContext : public antlr4::ParserRuleContext {
  public:
    Local_coordinate_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *LocalCoordinateConstraint();
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    Gen_res_numContext *gen_res_num();
    antlr4::tree::TerminalNode *Integer();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    Func_type_defContext *func_type_def();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Local_coordinate_restraintContext* local_coordinate_restraint();

  class  Site_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Site_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Site_restraintContext *> site_restraint();
    Site_restraintContext* site_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Site_restraintsContext* site_restraints();

  class  Site_restraintContext : public antlr4::ParserRuleContext {
  public:
    Site_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *SiteConstraint();
    Gen_simple_nameContext *gen_simple_name();
    Gen_res_numContext *gen_res_num();
    antlr4::tree::TerminalNode *Simple_name();
    Func_type_defContext *func_type_def();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Site_restraintContext* site_restraint();

  class  Site_residues_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Site_residues_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Site_residues_restraintContext *> site_residues_restraint();
    Site_residues_restraintContext* site_residues_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Site_residues_restraintsContext* site_residues_restraints();

  class  Site_residues_restraintContext : public antlr4::ParserRuleContext {
  public:
    Site_residues_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *SiteConstraintResidues();
    Gen_res_numContext *gen_res_num();
    Gen_simple_nameContext *gen_simple_name();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    Func_type_defContext *func_type_def();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Site_residues_restraintContext* site_residues_restraint();

  class  Min_residue_atomic_distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Min_residue_atomic_distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Min_residue_atomic_distance_restraintContext *> min_residue_atomic_distance_restraint();
    Min_residue_atomic_distance_restraintContext* min_residue_atomic_distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Min_residue_atomic_distance_restraintsContext* min_residue_atomic_distance_restraints();

  class  Min_residue_atomic_distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Min_residue_atomic_distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *MinResidueAtomicDistance();
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    NumberContext *number();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Min_residue_atomic_distance_restraintContext* min_residue_atomic_distance_restraint();

  class  Big_bin_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Big_bin_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Big_bin_restraintContext *> big_bin_restraint();
    Big_bin_restraintContext* big_bin_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Big_bin_restraintsContext* big_bin_restraints();

  class  Big_bin_restraintContext : public antlr4::ParserRuleContext {
  public:
    Big_bin_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *BigBin();
    Gen_res_numContext *gen_res_num();
    antlr4::tree::TerminalNode *Simple_name();
    NumberContext *number();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Big_bin_restraintContext* big_bin_restraint();

  class  Nested_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Nested_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Nested_restraintContext *> nested_restraint();
    Nested_restraintContext* nested_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Nested_restraintsContext* nested_restraints();

  class  Nested_restraintContext : public antlr4::ParserRuleContext {
  public:
    Nested_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *END();
    antlr4::tree::TerminalNode *MultiConstraint();
    antlr4::tree::TerminalNode *AmbiguousConstraint();
    std::vector<Any_restraintContext *> any_restraint();
    Any_restraintContext* any_restraint(size_t i);
    std::vector<Nested_restraintContext *> nested_restraint();
    Nested_restraintContext* nested_restraint(size_t i);
    antlr4::tree::TerminalNode *KofNConstraint();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Nested_restraintContext* nested_restraint();

  class  Any_restraintContext : public antlr4::ParserRuleContext {
  public:
    Any_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Atom_pair_restraintContext *atom_pair_restraint();
    Angle_restraintContext *angle_restraint();
    Dihedral_restraintContext *dihedral_restraint();
    Dihedral_pair_restraintContext *dihedral_pair_restraint();
    Coordinate_restraintContext *coordinate_restraint();
    Local_coordinate_restraintContext *local_coordinate_restraint();
    Site_restraintContext *site_restraint();
    Site_residues_restraintContext *site_residues_restraint();
    Min_residue_atomic_distance_restraintContext *min_residue_atomic_distance_restraint();
    Big_bin_restraintContext *big_bin_restraint();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Any_restraintContext* any_restraint();

  class  Func_type_defContext : public antlr4::ParserRuleContext {
  public:
    Func_type_defContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Number_fContext *> number_f();
    Number_fContext* number_f(size_t i);
    antlr4::tree::TerminalNode *BOUNDED();
    antlr4::tree::TerminalNode *PERIODICBOUNDED();
    antlr4::tree::TerminalNode *OFFSETPERIODICBOUNDED();
    antlr4::tree::TerminalNode *CIRCULARSPLINE();
    antlr4::tree::TerminalNode *GAUSSIANFUNC();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *SOGFUNC();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *CONSTANTFUNC();
    antlr4::tree::TerminalNode *IDENTITY();
    antlr4::tree::TerminalNode *SCALARWEIGHTEDFUNC();
    std::vector<Func_type_defContext *> func_type_def();
    Func_type_defContext* func_type_def(size_t i);
    antlr4::tree::TerminalNode *SUMFUNC();
    antlr4::tree::TerminalNode *SPLINE();
    antlr4::tree::TerminalNode *FADE();
    antlr4::tree::TerminalNode *SQUARE_WELL2();
    antlr4::tree::TerminalNode *ETABLE();
    antlr4::tree::TerminalNode *USOG();
    antlr4::tree::TerminalNode *SOG();
    antlr4::tree::TerminalNode *CIRCULARHARMONIC();
    antlr4::tree::TerminalNode *HARMONIC();
    antlr4::tree::TerminalNode *SIGMOID();
    antlr4::tree::TerminalNode *SQUARE_WELL();
    antlr4::tree::TerminalNode *AMBERPERIODIC();
    antlr4::tree::TerminalNode *CHARMMPERIODIC();
    antlr4::tree::TerminalNode *FLAT_HARMONIC();
    antlr4::tree::TerminalNode *TOPOUT();
    antlr4::tree::TerminalNode *CIRCULARSIGMOIDAL();
    antlr4::tree::TerminalNode *LINEAR_PENALTY();
    antlr4::tree::TerminalNode *MIXTUREFUNC();
    antlr4::tree::TerminalNode *KARPLUS();
    antlr4::tree::TerminalNode *SOEDINGFUNC();
    CommentContext *comment();
    antlr4::tree::TerminalNode *NONE();
    antlr4::tree::TerminalNode *WEIGHT();
    antlr4::tree::TerminalNode *DEGREES();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Func_type_defContext* func_type_def();

  class  Rdc_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Rdc_restraintContext *> rdc_restraint();
    Rdc_restraintContext* rdc_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraintsContext* rdc_restraints();

  class  Rdc_restraintContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    NumberContext *number();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraintContext* rdc_restraint();

  class  Disulfide_bond_linkagesContext : public antlr4::ParserRuleContext {
  public:
    Disulfide_bond_linkagesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Disulfide_bond_linkageContext *> disulfide_bond_linkage();
    Disulfide_bond_linkageContext* disulfide_bond_linkage(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Disulfide_bond_linkagesContext* disulfide_bond_linkages();

  class  Disulfide_bond_linkageContext : public antlr4::ParserRuleContext {
  public:
    Disulfide_bond_linkageContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Disulfide_bond_linkageContext* disulfide_bond_linkage();

  class  Atom_pair_w_chain_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Atom_pair_w_chain_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Atom_pair_w_chain_restraintContext *> atom_pair_w_chain_restraint();
    Atom_pair_w_chain_restraintContext* atom_pair_w_chain_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_pair_w_chain_restraintsContext* atom_pair_w_chain_restraints();

  class  Atom_pair_w_chain_restraintContext : public antlr4::ParserRuleContext {
  public:
    Atom_pair_w_chain_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    Func_type_defContext *func_type_def();
    antlr4::tree::TerminalNode *AtomPair();
    antlr4::tree::TerminalNode *NamedAtomPair();
    antlr4::tree::TerminalNode *AmbiguousNMRDistance();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_pair_w_chain_restraintContext* atom_pair_w_chain_restraint();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  Number_fContext : public antlr4::ParserRuleContext {
  public:
    Number_fContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Number_fContext* number_f();

  class  Gen_res_numContext : public antlr4::ParserRuleContext {
  public:
    Gen_res_numContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Integer_capital();
    antlr4::tree::TerminalNode *Capital_integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Gen_res_numContext* gen_res_num();

  class  Gen_simple_nameContext : public antlr4::ParserRuleContext {
  public:
    Gen_simple_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer_capital();
    antlr4::tree::TerminalNode *Capital_integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Gen_simple_nameContext* gen_simple_name();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

