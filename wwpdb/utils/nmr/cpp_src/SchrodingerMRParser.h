
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SchrodingerMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  SchrodingerMRParser : public antlr4::Parser {
public:
  enum {
    Set = 1, Struct = 2, Dist = 3, Tors = 4, Angle = 5, End = 6, Atom1 = 7, 
    Atom2 = 8, Atom3 = 9, Atom4 = 10, Lo = 11, Up = 12, Fc = 13, Target = 14, 
    Comma = 15, FXDI = 16, FXBA = 17, FXTA = 18, FXHB = 19, Entry = 20, 
    Molecule = 21, Chain = 22, Residue = 23, Atom = 24, Backbone = 25, Sidechain = 26, 
    Water = 27, Methyl = 28, Amide = 29, Smarts = 30, Entry_name = 31, Molecule_number = 32, 
    Molecule_modulo = 33, Molecule_entrynum = 34, Molecule_atoms = 35, Molecule_weight = 36, 
    Chain_name = 37, Residue_name_or_number = 38, Residue_ptype = 39, Residue_mtype = 40, 
    Residue_polarity = 41, Residue_secondary_structure = 42, Residue_position = 43, 
    Residue_inscode = 44, Atom_ptype = 45, Atom_name = 46, Atom_number = 47, 
    Atom_molnum = 48, Atom_entrynum = 49, Atom_mtype = 50, Atom_element = 51, 
    Atom_attachements = 52, Atom_atomicnumber = 53, Atom_charge = 54, Atom_formalcharge = 55, 
    Atom_displayed = 56, Atom_selected = 57, Or_op = 58, And_op = 59, Not_op = 60, 
    Fillres_op = 61, Fillmol_op = 62, Within_op = 63, Beyond_op = 64, Withinbonds_op = 65, 
    Beyondbonds_op = 66, Integer = 67, IntRange = 68, Float = 69, FloatRange = 70, 
    Slash_quote_string = 71, SMCLN_COMMENT = 72, COMMENT = 73, Simple_name = 74, 
    Simple_names = 75, Integers = 76, L_paren = 77, R_paren = 78, Lt_op = 79, 
    Gt_op = 80, Leq_op = 81, Geq_op = 82, Equ_op = 83, SPACE = 84, ENCLOSE_COMMENT = 85, 
    SECTION_COMMENT = 86, LINE_COMMENT = 87, Param_name = 88, Equ_op_SM = 89, 
    SPACE_SM = 90, RETURN_SM = 91, End_SM = 92, Hydrophilic = 93, Hydrophobic = 94, 
    Non_polar = 95, Polar = 96, Charged = 97, Positive = 98, Negative = 99, 
    IGNORE_SPACE_PM = 100, Helix_or_strand = 101, Strand_or_loop = 102, 
    Helix_or_loop = 103, Helix = 104, Strand = 105, Loop = 106, IGNORE_SPACE_SSM = 107
  };

  enum {
    RuleSchrodinger_mr = 0, RuleImport_structure = 1, RuleStruct_statement = 2, 
    RuleDistance_restraint = 3, RuleDihedral_angle_restraint = 4, RuleAngle_restraint = 5, 
    RuleDistance_statement = 6, RuleDistance_assign = 7, RuleDistance_assign_by_number = 8, 
    RuleDihedral_angle_statement = 9, RuleDihedral_angle_assign = 10, RuleDihedral_angle_assign_by_number = 11, 
    RuleAngle_statement = 12, RuleAngle_assign = 13, RuleAngle_assign_by_number = 14, 
    RuleFxdi_statement = 15, RuleFxdi_assign = 16, RuleFxdi_assign_by_number = 17, 
    RuleFxta_statement = 18, RuleFxta_assign = 19, RuleFxta_assign_by_number = 20, 
    RuleFxba_statement = 21, RuleFxba_assign = 22, RuleFxba_assign_by_number = 23, 
    RuleFxhb_statement = 24, RuleFxhb_assign = 25, RuleFxhb_assign_by_number = 26, 
    RuleSelection = 27, RuleSelection_expression = 28, RuleTerm = 29, RuleFactor = 30, 
    RuleNumber = 31, RuleNumber_f = 32, RuleParameter_statement = 33
  };

  explicit SchrodingerMRParser(antlr4::TokenStream *input);

  SchrodingerMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~SchrodingerMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Schrodinger_mrContext;
  class Import_structureContext;
  class Struct_statementContext;
  class Distance_restraintContext;
  class Dihedral_angle_restraintContext;
  class Angle_restraintContext;
  class Distance_statementContext;
  class Distance_assignContext;
  class Distance_assign_by_numberContext;
  class Dihedral_angle_statementContext;
  class Dihedral_angle_assignContext;
  class Dihedral_angle_assign_by_numberContext;
  class Angle_statementContext;
  class Angle_assignContext;
  class Angle_assign_by_numberContext;
  class Fxdi_statementContext;
  class Fxdi_assignContext;
  class Fxdi_assign_by_numberContext;
  class Fxta_statementContext;
  class Fxta_assignContext;
  class Fxta_assign_by_numberContext;
  class Fxba_statementContext;
  class Fxba_assignContext;
  class Fxba_assign_by_numberContext;
  class Fxhb_statementContext;
  class Fxhb_assignContext;
  class Fxhb_assign_by_numberContext;
  class SelectionContext;
  class Selection_expressionContext;
  class TermContext;
  class FactorContext;
  class NumberContext;
  class Number_fContext;
  class Parameter_statementContext; 

  class  Schrodinger_mrContext : public antlr4::ParserRuleContext {
  public:
    Schrodinger_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<Import_structureContext *> import_structure();
    Import_structureContext* import_structure(size_t i);
    std::vector<Distance_restraintContext *> distance_restraint();
    Distance_restraintContext* distance_restraint(size_t i);
    std::vector<Dihedral_angle_restraintContext *> dihedral_angle_restraint();
    Dihedral_angle_restraintContext* dihedral_angle_restraint(size_t i);
    std::vector<Angle_restraintContext *> angle_restraint();
    Angle_restraintContext* angle_restraint(size_t i);
    std::vector<Distance_assignContext *> distance_assign();
    Distance_assignContext* distance_assign(size_t i);
    std::vector<Dihedral_angle_assignContext *> dihedral_angle_assign();
    Dihedral_angle_assignContext* dihedral_angle_assign(size_t i);
    std::vector<Angle_assignContext *> angle_assign();
    Angle_assignContext* angle_assign(size_t i);
    std::vector<Parameter_statementContext *> parameter_statement();
    Parameter_statementContext* parameter_statement(size_t i);
    std::vector<Fxdi_statementContext *> fxdi_statement();
    Fxdi_statementContext* fxdi_statement(size_t i);
    std::vector<Fxta_statementContext *> fxta_statement();
    Fxta_statementContext* fxta_statement(size_t i);
    std::vector<Fxba_statementContext *> fxba_statement();
    Fxba_statementContext* fxba_statement(size_t i);
    std::vector<Fxhb_statementContext *> fxhb_statement();
    Fxhb_statementContext* fxhb_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Schrodinger_mrContext* schrodinger_mr();

  class  Import_structureContext : public antlr4::ParserRuleContext {
  public:
    Import_structureContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Struct();
    antlr4::tree::TerminalNode *End_SM();
    std::vector<Struct_statementContext *> struct_statement();
    Struct_statementContext* struct_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Import_structureContext* import_structure();

  class  Struct_statementContext : public antlr4::ParserRuleContext {
  public:
    Struct_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Param_name();
    antlr4::tree::TerminalNode* Param_name(size_t i);
    antlr4::tree::TerminalNode *Equ_op_SM();
    antlr4::tree::TerminalNode *RETURN_SM();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Struct_statementContext* struct_statement();

  class  Distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Dist();
    Distance_statementContext *distance_statement();
    antlr4::tree::TerminalNode *End();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintContext* distance_restraint();

  class  Dihedral_angle_restraintContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Tors();
    Dihedral_angle_statementContext *dihedral_angle_statement();
    antlr4::tree::TerminalNode *End();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_restraintContext* dihedral_angle_restraint();

  class  Angle_restraintContext : public antlr4::ParserRuleContext {
  public:
    Angle_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Angle();
    Angle_statementContext *angle_statement();
    antlr4::tree::TerminalNode *End();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_restraintContext* angle_restraint();

  class  Distance_statementContext : public antlr4::ParserRuleContext {
  public:
    Distance_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Parameter_statementContext *parameter_statement();
    antlr4::tree::TerminalNode *Atom1();
    antlr4::tree::TerminalNode *Atom2();
    antlr4::tree::TerminalNode *Lo();
    antlr4::tree::TerminalNode *Up();
    antlr4::tree::TerminalNode *Fc();
    std::vector<Distance_assignContext *> distance_assign();
    Distance_assignContext* distance_assign(size_t i);
    std::vector<Distance_assign_by_numberContext *> distance_assign_by_number();
    Distance_assign_by_numberContext* distance_assign_by_number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_statementContext* distance_statement();

  class  Distance_assignContext : public antlr4::ParserRuleContext {
  public:
    Distance_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_assignContext* distance_assign();

  class  Distance_assign_by_numberContext : public antlr4::ParserRuleContext {
  public:
    Distance_assign_by_numberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_assign_by_numberContext* distance_assign_by_number();

  class  Dihedral_angle_statementContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Parameter_statementContext *parameter_statement();
    antlr4::tree::TerminalNode *Atom1();
    antlr4::tree::TerminalNode *Atom2();
    antlr4::tree::TerminalNode *Atom3();
    antlr4::tree::TerminalNode *Atom4();
    antlr4::tree::TerminalNode *Target();
    antlr4::tree::TerminalNode *Fc();
    std::vector<Dihedral_angle_assignContext *> dihedral_angle_assign();
    Dihedral_angle_assignContext* dihedral_angle_assign(size_t i);
    std::vector<Dihedral_angle_assign_by_numberContext *> dihedral_angle_assign_by_number();
    Dihedral_angle_assign_by_numberContext* dihedral_angle_assign_by_number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_statementContext* dihedral_angle_statement();

  class  Dihedral_angle_assignContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_assignContext* dihedral_angle_assign();

  class  Dihedral_angle_assign_by_numberContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_assign_by_numberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_assign_by_numberContext* dihedral_angle_assign_by_number();

  class  Angle_statementContext : public antlr4::ParserRuleContext {
  public:
    Angle_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Parameter_statementContext *parameter_statement();
    antlr4::tree::TerminalNode *Atom1();
    antlr4::tree::TerminalNode *Atom2();
    antlr4::tree::TerminalNode *Atom3();
    antlr4::tree::TerminalNode *Target();
    antlr4::tree::TerminalNode *Fc();
    std::vector<Angle_assignContext *> angle_assign();
    Angle_assignContext* angle_assign(size_t i);
    std::vector<Angle_assign_by_numberContext *> angle_assign_by_number();
    Angle_assign_by_numberContext* angle_assign_by_number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_statementContext* angle_statement();

  class  Angle_assignContext : public antlr4::ParserRuleContext {
  public:
    Angle_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_assignContext* angle_assign();

  class  Angle_assign_by_numberContext : public antlr4::ParserRuleContext {
  public:
    Angle_assign_by_numberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_assign_by_numberContext* angle_assign_by_number();

  class  Fxdi_statementContext : public antlr4::ParserRuleContext {
  public:
    Fxdi_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Fxdi_assignContext *> fxdi_assign();
    Fxdi_assignContext* fxdi_assign(size_t i);
    std::vector<Fxdi_assign_by_numberContext *> fxdi_assign_by_number();
    Fxdi_assign_by_numberContext* fxdi_assign_by_number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fxdi_statementContext* fxdi_statement();

  class  Fxdi_assignContext : public antlr4::ParserRuleContext {
  public:
    Fxdi_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FXDI();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fxdi_assignContext* fxdi_assign();

  class  Fxdi_assign_by_numberContext : public antlr4::ParserRuleContext {
  public:
    Fxdi_assign_by_numberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FXDI();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fxdi_assign_by_numberContext* fxdi_assign_by_number();

  class  Fxta_statementContext : public antlr4::ParserRuleContext {
  public:
    Fxta_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Fxta_assignContext *> fxta_assign();
    Fxta_assignContext* fxta_assign(size_t i);
    std::vector<Fxta_assign_by_numberContext *> fxta_assign_by_number();
    Fxta_assign_by_numberContext* fxta_assign_by_number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fxta_statementContext* fxta_statement();

  class  Fxta_assignContext : public antlr4::ParserRuleContext {
  public:
    Fxta_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FXTA();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fxta_assignContext* fxta_assign();

  class  Fxta_assign_by_numberContext : public antlr4::ParserRuleContext {
  public:
    Fxta_assign_by_numberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FXTA();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fxta_assign_by_numberContext* fxta_assign_by_number();

  class  Fxba_statementContext : public antlr4::ParserRuleContext {
  public:
    Fxba_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Fxba_assignContext *> fxba_assign();
    Fxba_assignContext* fxba_assign(size_t i);
    std::vector<Fxba_assign_by_numberContext *> fxba_assign_by_number();
    Fxba_assign_by_numberContext* fxba_assign_by_number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fxba_statementContext* fxba_statement();

  class  Fxba_assignContext : public antlr4::ParserRuleContext {
  public:
    Fxba_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FXBA();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    antlr4::tree::TerminalNode *Integer();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fxba_assignContext* fxba_assign();

  class  Fxba_assign_by_numberContext : public antlr4::ParserRuleContext {
  public:
    Fxba_assign_by_numberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FXBA();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fxba_assign_by_numberContext* fxba_assign_by_number();

  class  Fxhb_statementContext : public antlr4::ParserRuleContext {
  public:
    Fxhb_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Fxhb_assignContext *> fxhb_assign();
    Fxhb_assignContext* fxhb_assign(size_t i);
    std::vector<Fxhb_assign_by_numberContext *> fxhb_assign_by_number();
    Fxhb_assign_by_numberContext* fxhb_assign_by_number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fxhb_statementContext* fxhb_statement();

  class  Fxhb_assignContext : public antlr4::ParserRuleContext {
  public:
    Fxhb_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FXHB();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    antlr4::tree::TerminalNode *Integer();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fxhb_assignContext* fxhb_assign();

  class  Fxhb_assign_by_numberContext : public antlr4::ParserRuleContext {
  public:
    Fxhb_assign_by_numberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FXHB();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fxhb_assign_by_numberContext* fxhb_assign_by_number();

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
    antlr4::tree::TerminalNode *Entry();
    antlr4::tree::TerminalNode *Entry_name();
    std::vector<antlr4::tree::TerminalNode *> Simple_names();
    antlr4::tree::TerminalNode* Simple_names(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);
    antlr4::tree::TerminalNode *Molecule();
    antlr4::tree::TerminalNode *Molecule_number();
    antlr4::tree::TerminalNode *Integers();
    antlr4::tree::TerminalNode *IntRange();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Molecule_modulo();
    antlr4::tree::TerminalNode *Molecule_entrynum();
    antlr4::tree::TerminalNode *Molecule_atoms();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Lt_op();
    antlr4::tree::TerminalNode *Gt_op();
    antlr4::tree::TerminalNode *Leq_op();
    antlr4::tree::TerminalNode *Geq_op();
    antlr4::tree::TerminalNode *Molecule_weight();
    antlr4::tree::TerminalNode *Chain();
    antlr4::tree::TerminalNode *Chain_name();
    antlr4::tree::TerminalNode *Residue();
    antlr4::tree::TerminalNode *Residue_name_or_number();
    antlr4::tree::TerminalNode *Residue_ptype();
    antlr4::tree::TerminalNode *Residue_mtype();
    antlr4::tree::TerminalNode *Residue_polarity();
    antlr4::tree::TerminalNode *Hydrophilic();
    antlr4::tree::TerminalNode *Hydrophobic();
    antlr4::tree::TerminalNode *Non_polar();
    antlr4::tree::TerminalNode *Polar();
    antlr4::tree::TerminalNode *Charged();
    antlr4::tree::TerminalNode *Positive();
    antlr4::tree::TerminalNode *Negative();
    antlr4::tree::TerminalNode *Residue_secondary_structure();
    antlr4::tree::TerminalNode *Helix_or_strand();
    antlr4::tree::TerminalNode *Strand_or_loop();
    antlr4::tree::TerminalNode *Helix_or_loop();
    antlr4::tree::TerminalNode *Helix();
    antlr4::tree::TerminalNode *Strand();
    antlr4::tree::TerminalNode *Loop();
    antlr4::tree::TerminalNode *Residue_position();
    std::vector<Number_fContext *> number_f();
    Number_fContext* number_f(size_t i);
    antlr4::tree::TerminalNode *Residue_inscode();
    antlr4::tree::TerminalNode *Atom_ptype();
    antlr4::tree::TerminalNode *Atom_name();
    antlr4::tree::TerminalNode *Atom();
    antlr4::tree::TerminalNode *Atom_number();
    antlr4::tree::TerminalNode *Atom_molnum();
    antlr4::tree::TerminalNode *Atom_entrynum();
    antlr4::tree::TerminalNode *Atom_mtype();
    antlr4::tree::TerminalNode *Atom_element();
    antlr4::tree::TerminalNode *Atom_attachements();
    antlr4::tree::TerminalNode *Atom_atomicnumber();
    antlr4::tree::TerminalNode *Atom_charge();
    antlr4::tree::TerminalNode *FloatRange();
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Atom_formalcharge();
    antlr4::tree::TerminalNode *Atom_displayed();
    antlr4::tree::TerminalNode *Atom_selected();
    antlr4::tree::TerminalNode *Fillres_op();
    FactorContext *factor();
    antlr4::tree::TerminalNode *Fillmol_op();
    antlr4::tree::TerminalNode *Within_op();
    antlr4::tree::TerminalNode *Beyond_op();
    antlr4::tree::TerminalNode *Withinbonds_op();
    antlr4::tree::TerminalNode *Beyondbonds_op();
    antlr4::tree::TerminalNode *Backbone();
    antlr4::tree::TerminalNode *Sidechain();
    antlr4::tree::TerminalNode *Water();
    antlr4::tree::TerminalNode *Methyl();
    antlr4::tree::TerminalNode *Amide();
    antlr4::tree::TerminalNode *Smarts();
    antlr4::tree::TerminalNode *Slash_quote_string();
    antlr4::tree::TerminalNode *Not_op();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  FactorContext* factor();

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

  class  Parameter_statementContext : public antlr4::ParserRuleContext {
  public:
    Parameter_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Set();
    antlr4::tree::TerminalNode *Simple_name();
    Selection_expressionContext *selection_expression();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Parameter_statementContext* parameter_statement();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

