
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GromacsPTParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  GromacsPTParser : public antlr4::Parser {
public:
  enum {
    L_brkt = 1, R_brkt = 2, Default = 3, Moleculetype = 4, Atomtypes = 5, 
    Pairtypes = 6, Bondtypes = 7, Angletypes = 8, Dihedraltypes = 9, Constrainttypes = 10, 
    Nonbond_params = 11, Atoms = 12, Bonds = 13, Pairs = 14, Pairs_nb = 15, 
    Angles = 16, Dihedrals = 17, Exclusions = 18, Constraints = 19, Settles = 20, 
    Virtual_sites1 = 21, Virtual_sites2 = 22, Virtual_sites3 = 23, Virtual_sites4 = 24, 
    Virtual_sitesn = 25, System = 26, Molecules = 27, Position_restraints = 28, 
    Intermolecular_interactions = 29, Integer = 30, Real = 31, SHARP_COMMENT = 32, 
    EXCLM_COMMENT = 33, SMCLN_COMMENT = 34, Simple_name = 35, SPACE = 36, 
    ENCLOSE_COMMENT = 37, SECTION_COMMENT = 38, LINE_COMMENT = 39, R_brkt_AA = 40, 
    SECTION_COMMENT_AA = 41, LINE_COMMENT_AA = 42, Simple_name_AA = 43, 
    SPACE_AA = 44, RETURN_AA = 45
  };

  enum {
    RuleGromacs_pt = 0, RuleDefault_statement = 1, RuleMoleculetype_statement = 2, 
    RuleMoleculetype = 3, RuleAtomtypes_statement = 4, RuleAtomtypes = 5, 
    RulePairtypes_statement = 6, RulePairtypes = 7, RuleBondtypes_statement = 8, 
    RuleBondtypes = 9, RuleAngletypes_statement = 10, RuleAngletypes = 11, 
    RuleDihedraltypes_statement = 12, RuleDihedraltypes = 13, RuleConstrainttypes_statement = 14, 
    RuleConstrainttypes = 15, RuleNonbonded_params_statement = 16, RuleNonbonded_params = 17, 
    RuleAtoms_statement = 18, RuleAtoms = 19, RuleBonds_statement = 20, 
    RuleBonds = 21, RulePairs_statement = 22, RulePairs = 23, RulePairs_nb_statement = 24, 
    RulePairs_nb = 25, RuleAngles_statement = 26, RuleAngles = 27, RuleDihedrals_statement = 28, 
    RuleDihedrals = 29, RuleExclusions_statement = 30, RuleExclusions = 31, 
    RuleConstraints_statement = 32, RuleConstraints = 33, RuleSettles_statement = 34, 
    RuleSettles = 35, RuleVirtual_sites1_statement = 36, RuleVirtual_sites1 = 37, 
    RuleVirtual_sites2_statement = 38, RuleVirtual_sites2 = 39, RuleVirtual_sites3_statement = 40, 
    RuleVirtual_sites3 = 41, RuleVirtual_sites4_statement = 42, RuleVirtual_sites4 = 43, 
    RuleVirtual_sitesn_statement = 44, RuleVirtual_sitesn = 45, RuleSystem_statement = 46, 
    RuleMolecules_statement = 47, RuleMolecules = 48, RuleNumber = 49, RulePosition_restraints = 50, 
    RulePosition_restraint = 51
  };

  explicit GromacsPTParser(antlr4::TokenStream *input);

  GromacsPTParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~GromacsPTParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Gromacs_ptContext;
  class Default_statementContext;
  class Moleculetype_statementContext;
  class MoleculetypeContext;
  class Atomtypes_statementContext;
  class AtomtypesContext;
  class Pairtypes_statementContext;
  class PairtypesContext;
  class Bondtypes_statementContext;
  class BondtypesContext;
  class Angletypes_statementContext;
  class AngletypesContext;
  class Dihedraltypes_statementContext;
  class DihedraltypesContext;
  class Constrainttypes_statementContext;
  class ConstrainttypesContext;
  class Nonbonded_params_statementContext;
  class Nonbonded_paramsContext;
  class Atoms_statementContext;
  class AtomsContext;
  class Bonds_statementContext;
  class BondsContext;
  class Pairs_statementContext;
  class PairsContext;
  class Pairs_nb_statementContext;
  class Pairs_nbContext;
  class Angles_statementContext;
  class AnglesContext;
  class Dihedrals_statementContext;
  class DihedralsContext;
  class Exclusions_statementContext;
  class ExclusionsContext;
  class Constraints_statementContext;
  class ConstraintsContext;
  class Settles_statementContext;
  class SettlesContext;
  class Virtual_sites1_statementContext;
  class Virtual_sites1Context;
  class Virtual_sites2_statementContext;
  class Virtual_sites2Context;
  class Virtual_sites3_statementContext;
  class Virtual_sites3Context;
  class Virtual_sites4_statementContext;
  class Virtual_sites4Context;
  class Virtual_sitesn_statementContext;
  class Virtual_sitesnContext;
  class System_statementContext;
  class Molecules_statementContext;
  class MoleculesContext;
  class NumberContext;
  class Position_restraintsContext;
  class Position_restraintContext; 

  class  Gromacs_ptContext : public antlr4::ParserRuleContext {
  public:
    Gromacs_ptContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<Default_statementContext *> default_statement();
    Default_statementContext* default_statement(size_t i);
    std::vector<Moleculetype_statementContext *> moleculetype_statement();
    Moleculetype_statementContext* moleculetype_statement(size_t i);
    std::vector<Atomtypes_statementContext *> atomtypes_statement();
    Atomtypes_statementContext* atomtypes_statement(size_t i);
    std::vector<Pairtypes_statementContext *> pairtypes_statement();
    Pairtypes_statementContext* pairtypes_statement(size_t i);
    std::vector<Bondtypes_statementContext *> bondtypes_statement();
    Bondtypes_statementContext* bondtypes_statement(size_t i);
    std::vector<Angletypes_statementContext *> angletypes_statement();
    Angletypes_statementContext* angletypes_statement(size_t i);
    std::vector<Dihedraltypes_statementContext *> dihedraltypes_statement();
    Dihedraltypes_statementContext* dihedraltypes_statement(size_t i);
    std::vector<Constrainttypes_statementContext *> constrainttypes_statement();
    Constrainttypes_statementContext* constrainttypes_statement(size_t i);
    std::vector<Nonbonded_params_statementContext *> nonbonded_params_statement();
    Nonbonded_params_statementContext* nonbonded_params_statement(size_t i);
    std::vector<Atoms_statementContext *> atoms_statement();
    Atoms_statementContext* atoms_statement(size_t i);
    std::vector<Bonds_statementContext *> bonds_statement();
    Bonds_statementContext* bonds_statement(size_t i);
    std::vector<Pairs_statementContext *> pairs_statement();
    Pairs_statementContext* pairs_statement(size_t i);
    std::vector<Pairs_nb_statementContext *> pairs_nb_statement();
    Pairs_nb_statementContext* pairs_nb_statement(size_t i);
    std::vector<Angles_statementContext *> angles_statement();
    Angles_statementContext* angles_statement(size_t i);
    std::vector<Dihedrals_statementContext *> dihedrals_statement();
    Dihedrals_statementContext* dihedrals_statement(size_t i);
    std::vector<Exclusions_statementContext *> exclusions_statement();
    Exclusions_statementContext* exclusions_statement(size_t i);
    std::vector<Constraints_statementContext *> constraints_statement();
    Constraints_statementContext* constraints_statement(size_t i);
    std::vector<Settles_statementContext *> settles_statement();
    Settles_statementContext* settles_statement(size_t i);
    std::vector<Virtual_sites1_statementContext *> virtual_sites1_statement();
    Virtual_sites1_statementContext* virtual_sites1_statement(size_t i);
    std::vector<Virtual_sites2_statementContext *> virtual_sites2_statement();
    Virtual_sites2_statementContext* virtual_sites2_statement(size_t i);
    std::vector<Virtual_sites3_statementContext *> virtual_sites3_statement();
    Virtual_sites3_statementContext* virtual_sites3_statement(size_t i);
    std::vector<Virtual_sites4_statementContext *> virtual_sites4_statement();
    Virtual_sites4_statementContext* virtual_sites4_statement(size_t i);
    std::vector<Virtual_sitesn_statementContext *> virtual_sitesn_statement();
    Virtual_sitesn_statementContext* virtual_sitesn_statement(size_t i);
    std::vector<System_statementContext *> system_statement();
    System_statementContext* system_statement(size_t i);
    std::vector<Molecules_statementContext *> molecules_statement();
    Molecules_statementContext* molecules_statement(size_t i);
    std::vector<Position_restraintsContext *> position_restraints();
    Position_restraintsContext* position_restraints(size_t i);
    std::vector<antlr4::tree::TerminalNode *> L_brkt();
    antlr4::tree::TerminalNode* L_brkt(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Intermolecular_interactions();
    antlr4::tree::TerminalNode* Intermolecular_interactions(size_t i);
    std::vector<antlr4::tree::TerminalNode *> R_brkt();
    antlr4::tree::TerminalNode* R_brkt(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Gromacs_ptContext* gromacs_pt();

  class  Default_statementContext : public antlr4::ParserRuleContext {
  public:
    Default_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Default();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Default_statementContext* default_statement();

  class  Moleculetype_statementContext : public antlr4::ParserRuleContext {
  public:
    Moleculetype_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Moleculetype();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<MoleculetypeContext *> moleculetype();
    MoleculetypeContext* moleculetype(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Moleculetype_statementContext* moleculetype_statement();

  class  MoleculetypeContext : public antlr4::ParserRuleContext {
  public:
    MoleculetypeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  MoleculetypeContext* moleculetype();

  class  Atomtypes_statementContext : public antlr4::ParserRuleContext {
  public:
    Atomtypes_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Atomtypes();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<AtomtypesContext *> atomtypes();
    AtomtypesContext* atomtypes(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atomtypes_statementContext* atomtypes_statement();

  class  AtomtypesContext : public antlr4::ParserRuleContext {
  public:
    AtomtypesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  AtomtypesContext* atomtypes();

  class  Pairtypes_statementContext : public antlr4::ParserRuleContext {
  public:
    Pairtypes_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Pairtypes();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<PairtypesContext *> pairtypes();
    PairtypesContext* pairtypes(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pairtypes_statementContext* pairtypes_statement();

  class  PairtypesContext : public antlr4::ParserRuleContext {
  public:
    PairtypesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  PairtypesContext* pairtypes();

  class  Bondtypes_statementContext : public antlr4::ParserRuleContext {
  public:
    Bondtypes_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Bondtypes();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<BondtypesContext *> bondtypes();
    BondtypesContext* bondtypes(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Bondtypes_statementContext* bondtypes_statement();

  class  BondtypesContext : public antlr4::ParserRuleContext {
  public:
    BondtypesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  BondtypesContext* bondtypes();

  class  Angletypes_statementContext : public antlr4::ParserRuleContext {
  public:
    Angletypes_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Angletypes();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<AngletypesContext *> angletypes();
    AngletypesContext* angletypes(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angletypes_statementContext* angletypes_statement();

  class  AngletypesContext : public antlr4::ParserRuleContext {
  public:
    AngletypesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  AngletypesContext* angletypes();

  class  Dihedraltypes_statementContext : public antlr4::ParserRuleContext {
  public:
    Dihedraltypes_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Dihedraltypes();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<DihedraltypesContext *> dihedraltypes();
    DihedraltypesContext* dihedraltypes(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedraltypes_statementContext* dihedraltypes_statement();

  class  DihedraltypesContext : public antlr4::ParserRuleContext {
  public:
    DihedraltypesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  DihedraltypesContext* dihedraltypes();

  class  Constrainttypes_statementContext : public antlr4::ParserRuleContext {
  public:
    Constrainttypes_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Constrainttypes();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<ConstrainttypesContext *> constrainttypes();
    ConstrainttypesContext* constrainttypes(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Constrainttypes_statementContext* constrainttypes_statement();

  class  ConstrainttypesContext : public antlr4::ParserRuleContext {
  public:
    ConstrainttypesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ConstrainttypesContext* constrainttypes();

  class  Nonbonded_params_statementContext : public antlr4::ParserRuleContext {
  public:
    Nonbonded_params_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Nonbond_params();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Nonbonded_paramsContext *> nonbonded_params();
    Nonbonded_paramsContext* nonbonded_params(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Nonbonded_params_statementContext* nonbonded_params_statement();

  class  Nonbonded_paramsContext : public antlr4::ParserRuleContext {
  public:
    Nonbonded_paramsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Nonbonded_paramsContext* nonbonded_params();

  class  Atoms_statementContext : public antlr4::ParserRuleContext {
  public:
    Atoms_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Atoms();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<AtomsContext *> atoms();
    AtomsContext* atoms(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atoms_statementContext* atoms_statement();

  class  AtomsContext : public antlr4::ParserRuleContext {
  public:
    AtomsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  AtomsContext* atoms();

  class  Bonds_statementContext : public antlr4::ParserRuleContext {
  public:
    Bonds_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Bonds();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<BondsContext *> bonds();
    BondsContext* bonds(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Bonds_statementContext* bonds_statement();

  class  BondsContext : public antlr4::ParserRuleContext {
  public:
    BondsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  BondsContext* bonds();

  class  Pairs_statementContext : public antlr4::ParserRuleContext {
  public:
    Pairs_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Pairs();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<PairsContext *> pairs();
    PairsContext* pairs(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pairs_statementContext* pairs_statement();

  class  PairsContext : public antlr4::ParserRuleContext {
  public:
    PairsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  PairsContext* pairs();

  class  Pairs_nb_statementContext : public antlr4::ParserRuleContext {
  public:
    Pairs_nb_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Pairs_nb();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Pairs_nbContext *> pairs_nb();
    Pairs_nbContext* pairs_nb(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pairs_nb_statementContext* pairs_nb_statement();

  class  Pairs_nbContext : public antlr4::ParserRuleContext {
  public:
    Pairs_nbContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pairs_nbContext* pairs_nb();

  class  Angles_statementContext : public antlr4::ParserRuleContext {
  public:
    Angles_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Angles();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<AnglesContext *> angles();
    AnglesContext* angles(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angles_statementContext* angles_statement();

  class  AnglesContext : public antlr4::ParserRuleContext {
  public:
    AnglesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  AnglesContext* angles();

  class  Dihedrals_statementContext : public antlr4::ParserRuleContext {
  public:
    Dihedrals_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Dihedrals();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<DihedralsContext *> dihedrals();
    DihedralsContext* dihedrals(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedrals_statementContext* dihedrals_statement();

  class  DihedralsContext : public antlr4::ParserRuleContext {
  public:
    DihedralsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  DihedralsContext* dihedrals();

  class  Exclusions_statementContext : public antlr4::ParserRuleContext {
  public:
    Exclusions_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Exclusions();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<ExclusionsContext *> exclusions();
    ExclusionsContext* exclusions(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Exclusions_statementContext* exclusions_statement();

  class  ExclusionsContext : public antlr4::ParserRuleContext {
  public:
    ExclusionsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ExclusionsContext* exclusions();

  class  Constraints_statementContext : public antlr4::ParserRuleContext {
  public:
    Constraints_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Constraints();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<ConstraintsContext *> constraints();
    ConstraintsContext* constraints(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Constraints_statementContext* constraints_statement();

  class  ConstraintsContext : public antlr4::ParserRuleContext {
  public:
    ConstraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    NumberContext *number();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ConstraintsContext* constraints();

  class  Settles_statementContext : public antlr4::ParserRuleContext {
  public:
    Settles_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Settles();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<SettlesContext *> settles();
    SettlesContext* settles(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Settles_statementContext* settles_statement();

  class  SettlesContext : public antlr4::ParserRuleContext {
  public:
    SettlesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  SettlesContext* settles();

  class  Virtual_sites1_statementContext : public antlr4::ParserRuleContext {
  public:
    Virtual_sites1_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Virtual_sites1();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Virtual_sites1Context *> virtual_sites1();
    Virtual_sites1Context* virtual_sites1(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Virtual_sites1_statementContext* virtual_sites1_statement();

  class  Virtual_sites1Context : public antlr4::ParserRuleContext {
  public:
    Virtual_sites1Context(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Virtual_sites1Context* virtual_sites1();

  class  Virtual_sites2_statementContext : public antlr4::ParserRuleContext {
  public:
    Virtual_sites2_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Virtual_sites2();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Virtual_sites2Context *> virtual_sites2();
    Virtual_sites2Context* virtual_sites2(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Virtual_sites2_statementContext* virtual_sites2_statement();

  class  Virtual_sites2Context : public antlr4::ParserRuleContext {
  public:
    Virtual_sites2Context(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    NumberContext *number();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Virtual_sites2Context* virtual_sites2();

  class  Virtual_sites3_statementContext : public antlr4::ParserRuleContext {
  public:
    Virtual_sites3_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Virtual_sites3();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Virtual_sites3Context *> virtual_sites3();
    Virtual_sites3Context* virtual_sites3(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Virtual_sites3_statementContext* virtual_sites3_statement();

  class  Virtual_sites3Context : public antlr4::ParserRuleContext {
  public:
    Virtual_sites3Context(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Virtual_sites3Context* virtual_sites3();

  class  Virtual_sites4_statementContext : public antlr4::ParserRuleContext {
  public:
    Virtual_sites4_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Virtual_sites4();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Virtual_sites4Context *> virtual_sites4();
    Virtual_sites4Context* virtual_sites4(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Virtual_sites4_statementContext* virtual_sites4_statement();

  class  Virtual_sites4Context : public antlr4::ParserRuleContext {
  public:
    Virtual_sites4Context(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Virtual_sites4Context* virtual_sites4();

  class  Virtual_sitesn_statementContext : public antlr4::ParserRuleContext {
  public:
    Virtual_sitesn_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Virtual_sitesn();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Virtual_sitesnContext *> virtual_sitesn();
    Virtual_sitesnContext* virtual_sitesn(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Virtual_sitesn_statementContext* virtual_sitesn_statement();

  class  Virtual_sitesnContext : public antlr4::ParserRuleContext {
  public:
    Virtual_sitesnContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    NumberContext *number();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Virtual_sitesnContext* virtual_sitesn();

  class  System_statementContext : public antlr4::ParserRuleContext {
  public:
    System_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *System();
    antlr4::tree::TerminalNode *R_brkt_AA();
    antlr4::tree::TerminalNode *RETURN_AA();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_AA();
    antlr4::tree::TerminalNode* Simple_name_AA(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  System_statementContext* system_statement();

  class  Molecules_statementContext : public antlr4::ParserRuleContext {
  public:
    Molecules_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Molecules();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<MoleculesContext *> molecules();
    MoleculesContext* molecules(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Molecules_statementContext* molecules_statement();

  class  MoleculesContext : public antlr4::ParserRuleContext {
  public:
    MoleculesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  MoleculesContext* molecules();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  Position_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Position_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brkt();
    antlr4::tree::TerminalNode *Position_restraints();
    antlr4::tree::TerminalNode *R_brkt();
    std::vector<Position_restraintContext *> position_restraint();
    Position_restraintContext* position_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Position_restraintsContext* position_restraints();

  class  Position_restraintContext : public antlr4::ParserRuleContext {
  public:
    Position_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Position_restraintContext* position_restraint();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

