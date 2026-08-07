
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AmberPTParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  AmberPTParser : public antlr4::Parser {
public:
  enum {
    VERSION = 1, FLAG = 2, AMBER_ATOM_TYPE = 3, ANGLE_EQUIL_VALUE = 4, ANGLE_FORCE_CONSTANT = 5, 
    ANGLES_INC_HYDROGEN = 6, ANGLES_WITHOUT_HYDROGEN = 7, ATOMIC_NUMBER = 8, 
    ATOM_NAME = 9, ATOM_TYPE_INDEX = 10, ATOMS_PER_MOLECULE = 11, BOND_EQUIL_VALUE = 12, 
    BOND_FORCE_CONSTANT = 13, BONDS_INC_HYDROGEN = 14, BONDS_WITHOUT_HYDROGEN = 15, 
    BOX_DIMENSIONS = 16, CAP_INFO = 17, CAP_INFO2 = 18, CHARGE = 19, CMAP_COUNT = 20, 
    CMAP_RESOLUTION = 21, CMAP_PARAMETER_01 = 22, CMAP_PARAMETER_02 = 23, 
    CMAP_PARAMETER_03 = 24, CMAP_PARAMETER_04 = 25, CMAP_PARAMETER_05 = 26, 
    CMAP_PARAMETER_06 = 27, CMAP_PARAMETER_07 = 28, CMAP_PARAMETER_08 = 29, 
    CMAP_PARAMETER_09 = 30, CMAP_PARAMETER_10 = 31, CMAP_PARAMETER_11 = 32, 
    CMAP_PARAMETER_12 = 33, CMAP_PARAMETER_13 = 34, CMAP_PARAMETER_14 = 35, 
    CMAP_INDEX = 36, DIHEDRAL_FORCE_CONSTANT = 37, DIHEDRAL_PERIODICITY = 38, 
    DIHEDRAL_PHASE = 39, DIHEDRALS_INC_HYDROGEN = 40, DIHEDRALS_WITHOUT_HYDROGEN = 41, 
    EXCLUDED_ATOMS_LIST = 42, HBCUT = 43, HBOND_ACOEF = 44, HBOND_BCOEF = 45, 
    IPOL = 46, IROTAT = 47, JOIN_ARRAY = 48, LENNARD_JONES_ACOEF = 49, LENNARD_JONES_BCOEF = 50, 
    MASS = 51, NONBONDED_PARM_INDEX = 52, NUMBER_EXCLUDED_ATOMS = 53, POINTERS = 54, 
    POLARIZABILITY = 55, RADII = 56, RADIUS_SET = 57, RESIDUE_LABEL = 58, 
    RESIDUE_POINTER = 59, SCEE_SCALE_FACTOR = 60, SCNB_SCALE_FACTOR = 61, 
    SCREEN = 62, SOLTY = 63, SOLVENT_POINTERS = 64, TITLE = 65, TREE_CHAIN_CLASSIFICATION = 66, 
    SHARP_COMMENT = 67, EXCLM_COMMENT = 68, SMCLN_COMMENT = 69, FORMAT = 70, 
    SPACE = 71, LINE_COMMENT = 72, VERSION_STAMP = 73, DATE = 74, Equ_op = 75, 
    Version = 76, Date_time = 77, SPACE_VS = 78, FLAG_VS = 79, Fortran_format_A = 80, 
    Fortran_format_I = 81, Fortran_format_E = 82, Simple_name = 83, SPACE_AA = 84, 
    FLAG_AA = 85, Integer = 86, SPACE_IA = 87, FLAG_IA = 88, Real = 89, 
    SPACE_EA = 90, FLAG_EA = 91
  };

  enum {
    RuleAmber_pt = 0, RuleVersion_statement = 1, RuleAmber_atom_type_statement = 2, 
    RuleAngle_equil_value_statement = 3, RuleAngle_force_constant_statement = 4, 
    RuleAngles_inc_hydrogen_statement = 5, RuleAngles_without_hydrogen_statement = 6, 
    RuleAtomic_number_statement = 7, RuleAtom_name_statement = 8, RuleAtom_type_index_statement = 9, 
    RuleAtoms_per_molecule_statement = 10, RuleBond_equil_value_statement = 11, 
    RuleBond_force_constant_statement = 12, RuleBonds_inc_hydrogen_statement = 13, 
    RuleBonds_without_hydrogen_statement = 14, RuleBox_dimensions_statement = 15, 
    RuleCap_info_statement = 16, RuleCap_info2_statement = 17, RuleCharge_statement = 18, 
    RuleCmap_count_statement = 19, RuleCmap_resolution_statement = 20, RuleCmap_parameter_statement = 21, 
    RuleCmap_index_statement = 22, RuleDihedral_force_constant_statement = 23, 
    RuleDihedral_periodicity_statement = 24, RuleDihedral_phase_statement = 25, 
    RuleDihedrals_inc_hydrogen_statement = 26, RuleDihedrals_without_hydrogen_statement = 27, 
    RuleExcluded_atoms_list_statement = 28, RuleHbcut_statement = 29, RuleHbond_acoef_statement = 30, 
    RuleHbond_bcoef_statement = 31, RuleIpol_statement = 32, RuleIrotat_statement = 33, 
    RuleJoin_array_statement = 34, RuleLennard_jones_acoef_statement = 35, 
    RuleLennard_jones_bcoef_statement = 36, RuleMass_statement = 37, RuleNonbonded_parm_index_statement = 38, 
    RuleNumber_excluded_atoms_statement = 39, RulePointers_statement = 40, 
    RulePolarizability_statement = 41, RuleRadii_statement = 42, RuleRadius_set_statement = 43, 
    RuleResidue_label_statement = 44, RuleResidue_pointer_statement = 45, 
    RuleScee_scale_factor_statement = 46, RuleScnb_scale_factor_statement = 47, 
    RuleScreen_statement = 48, RuleSolty_statement = 49, RuleSolvent_pointers_statement = 50, 
    RuleTitle_statement = 51, RuleTree_chain_classification_statement = 52, 
    RuleFormat_function = 53
  };

  explicit AmberPTParser(antlr4::TokenStream *input);

  AmberPTParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~AmberPTParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Amber_ptContext;
  class Version_statementContext;
  class Amber_atom_type_statementContext;
  class Angle_equil_value_statementContext;
  class Angle_force_constant_statementContext;
  class Angles_inc_hydrogen_statementContext;
  class Angles_without_hydrogen_statementContext;
  class Atomic_number_statementContext;
  class Atom_name_statementContext;
  class Atom_type_index_statementContext;
  class Atoms_per_molecule_statementContext;
  class Bond_equil_value_statementContext;
  class Bond_force_constant_statementContext;
  class Bonds_inc_hydrogen_statementContext;
  class Bonds_without_hydrogen_statementContext;
  class Box_dimensions_statementContext;
  class Cap_info_statementContext;
  class Cap_info2_statementContext;
  class Charge_statementContext;
  class Cmap_count_statementContext;
  class Cmap_resolution_statementContext;
  class Cmap_parameter_statementContext;
  class Cmap_index_statementContext;
  class Dihedral_force_constant_statementContext;
  class Dihedral_periodicity_statementContext;
  class Dihedral_phase_statementContext;
  class Dihedrals_inc_hydrogen_statementContext;
  class Dihedrals_without_hydrogen_statementContext;
  class Excluded_atoms_list_statementContext;
  class Hbcut_statementContext;
  class Hbond_acoef_statementContext;
  class Hbond_bcoef_statementContext;
  class Ipol_statementContext;
  class Irotat_statementContext;
  class Join_array_statementContext;
  class Lennard_jones_acoef_statementContext;
  class Lennard_jones_bcoef_statementContext;
  class Mass_statementContext;
  class Nonbonded_parm_index_statementContext;
  class Number_excluded_atoms_statementContext;
  class Pointers_statementContext;
  class Polarizability_statementContext;
  class Radii_statementContext;
  class Radius_set_statementContext;
  class Residue_label_statementContext;
  class Residue_pointer_statementContext;
  class Scee_scale_factor_statementContext;
  class Scnb_scale_factor_statementContext;
  class Screen_statementContext;
  class Solty_statementContext;
  class Solvent_pointers_statementContext;
  class Title_statementContext;
  class Tree_chain_classification_statementContext;
  class Format_functionContext; 

  class  Amber_ptContext : public antlr4::ParserRuleContext {
  public:
    Amber_ptContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    Version_statementContext *version_statement();
    antlr4::tree::TerminalNode *FLAG();
    std::vector<Amber_atom_type_statementContext *> amber_atom_type_statement();
    Amber_atom_type_statementContext* amber_atom_type_statement(size_t i);
    std::vector<Angle_equil_value_statementContext *> angle_equil_value_statement();
    Angle_equil_value_statementContext* angle_equil_value_statement(size_t i);
    std::vector<Angle_force_constant_statementContext *> angle_force_constant_statement();
    Angle_force_constant_statementContext* angle_force_constant_statement(size_t i);
    std::vector<Angles_inc_hydrogen_statementContext *> angles_inc_hydrogen_statement();
    Angles_inc_hydrogen_statementContext* angles_inc_hydrogen_statement(size_t i);
    std::vector<Angles_without_hydrogen_statementContext *> angles_without_hydrogen_statement();
    Angles_without_hydrogen_statementContext* angles_without_hydrogen_statement(size_t i);
    std::vector<Atomic_number_statementContext *> atomic_number_statement();
    Atomic_number_statementContext* atomic_number_statement(size_t i);
    std::vector<Atom_name_statementContext *> atom_name_statement();
    Atom_name_statementContext* atom_name_statement(size_t i);
    std::vector<Atom_type_index_statementContext *> atom_type_index_statement();
    Atom_type_index_statementContext* atom_type_index_statement(size_t i);
    std::vector<Atoms_per_molecule_statementContext *> atoms_per_molecule_statement();
    Atoms_per_molecule_statementContext* atoms_per_molecule_statement(size_t i);
    std::vector<Bond_equil_value_statementContext *> bond_equil_value_statement();
    Bond_equil_value_statementContext* bond_equil_value_statement(size_t i);
    std::vector<Bond_force_constant_statementContext *> bond_force_constant_statement();
    Bond_force_constant_statementContext* bond_force_constant_statement(size_t i);
    std::vector<Bonds_inc_hydrogen_statementContext *> bonds_inc_hydrogen_statement();
    Bonds_inc_hydrogen_statementContext* bonds_inc_hydrogen_statement(size_t i);
    std::vector<Bonds_without_hydrogen_statementContext *> bonds_without_hydrogen_statement();
    Bonds_without_hydrogen_statementContext* bonds_without_hydrogen_statement(size_t i);
    std::vector<Box_dimensions_statementContext *> box_dimensions_statement();
    Box_dimensions_statementContext* box_dimensions_statement(size_t i);
    std::vector<Cap_info_statementContext *> cap_info_statement();
    Cap_info_statementContext* cap_info_statement(size_t i);
    std::vector<Cap_info2_statementContext *> cap_info2_statement();
    Cap_info2_statementContext* cap_info2_statement(size_t i);
    std::vector<Charge_statementContext *> charge_statement();
    Charge_statementContext* charge_statement(size_t i);
    std::vector<Cmap_count_statementContext *> cmap_count_statement();
    Cmap_count_statementContext* cmap_count_statement(size_t i);
    std::vector<Cmap_resolution_statementContext *> cmap_resolution_statement();
    Cmap_resolution_statementContext* cmap_resolution_statement(size_t i);
    std::vector<Cmap_parameter_statementContext *> cmap_parameter_statement();
    Cmap_parameter_statementContext* cmap_parameter_statement(size_t i);
    std::vector<Cmap_index_statementContext *> cmap_index_statement();
    Cmap_index_statementContext* cmap_index_statement(size_t i);
    std::vector<Dihedral_force_constant_statementContext *> dihedral_force_constant_statement();
    Dihedral_force_constant_statementContext* dihedral_force_constant_statement(size_t i);
    std::vector<Dihedral_periodicity_statementContext *> dihedral_periodicity_statement();
    Dihedral_periodicity_statementContext* dihedral_periodicity_statement(size_t i);
    std::vector<Dihedral_phase_statementContext *> dihedral_phase_statement();
    Dihedral_phase_statementContext* dihedral_phase_statement(size_t i);
    std::vector<Dihedrals_inc_hydrogen_statementContext *> dihedrals_inc_hydrogen_statement();
    Dihedrals_inc_hydrogen_statementContext* dihedrals_inc_hydrogen_statement(size_t i);
    std::vector<Dihedrals_without_hydrogen_statementContext *> dihedrals_without_hydrogen_statement();
    Dihedrals_without_hydrogen_statementContext* dihedrals_without_hydrogen_statement(size_t i);
    std::vector<Excluded_atoms_list_statementContext *> excluded_atoms_list_statement();
    Excluded_atoms_list_statementContext* excluded_atoms_list_statement(size_t i);
    std::vector<Hbcut_statementContext *> hbcut_statement();
    Hbcut_statementContext* hbcut_statement(size_t i);
    std::vector<Hbond_acoef_statementContext *> hbond_acoef_statement();
    Hbond_acoef_statementContext* hbond_acoef_statement(size_t i);
    std::vector<Hbond_bcoef_statementContext *> hbond_bcoef_statement();
    Hbond_bcoef_statementContext* hbond_bcoef_statement(size_t i);
    std::vector<Ipol_statementContext *> ipol_statement();
    Ipol_statementContext* ipol_statement(size_t i);
    std::vector<Irotat_statementContext *> irotat_statement();
    Irotat_statementContext* irotat_statement(size_t i);
    std::vector<Join_array_statementContext *> join_array_statement();
    Join_array_statementContext* join_array_statement(size_t i);
    std::vector<Lennard_jones_acoef_statementContext *> lennard_jones_acoef_statement();
    Lennard_jones_acoef_statementContext* lennard_jones_acoef_statement(size_t i);
    std::vector<Lennard_jones_bcoef_statementContext *> lennard_jones_bcoef_statement();
    Lennard_jones_bcoef_statementContext* lennard_jones_bcoef_statement(size_t i);
    std::vector<Mass_statementContext *> mass_statement();
    Mass_statementContext* mass_statement(size_t i);
    std::vector<Nonbonded_parm_index_statementContext *> nonbonded_parm_index_statement();
    Nonbonded_parm_index_statementContext* nonbonded_parm_index_statement(size_t i);
    std::vector<Number_excluded_atoms_statementContext *> number_excluded_atoms_statement();
    Number_excluded_atoms_statementContext* number_excluded_atoms_statement(size_t i);
    std::vector<Pointers_statementContext *> pointers_statement();
    Pointers_statementContext* pointers_statement(size_t i);
    std::vector<Polarizability_statementContext *> polarizability_statement();
    Polarizability_statementContext* polarizability_statement(size_t i);
    std::vector<Radii_statementContext *> radii_statement();
    Radii_statementContext* radii_statement(size_t i);
    std::vector<Radius_set_statementContext *> radius_set_statement();
    Radius_set_statementContext* radius_set_statement(size_t i);
    std::vector<Residue_label_statementContext *> residue_label_statement();
    Residue_label_statementContext* residue_label_statement(size_t i);
    std::vector<Residue_pointer_statementContext *> residue_pointer_statement();
    Residue_pointer_statementContext* residue_pointer_statement(size_t i);
    std::vector<Scee_scale_factor_statementContext *> scee_scale_factor_statement();
    Scee_scale_factor_statementContext* scee_scale_factor_statement(size_t i);
    std::vector<Scnb_scale_factor_statementContext *> scnb_scale_factor_statement();
    Scnb_scale_factor_statementContext* scnb_scale_factor_statement(size_t i);
    std::vector<Screen_statementContext *> screen_statement();
    Screen_statementContext* screen_statement(size_t i);
    std::vector<Solty_statementContext *> solty_statement();
    Solty_statementContext* solty_statement(size_t i);
    std::vector<Solvent_pointers_statementContext *> solvent_pointers_statement();
    Solvent_pointers_statementContext* solvent_pointers_statement(size_t i);
    std::vector<Title_statementContext *> title_statement();
    Title_statementContext* title_statement(size_t i);
    std::vector<Tree_chain_classification_statementContext *> tree_chain_classification_statement();
    Tree_chain_classification_statementContext* tree_chain_classification_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Amber_ptContext* amber_pt();

  class  Version_statementContext : public antlr4::ParserRuleContext {
  public:
    Version_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *VERSION();
    antlr4::tree::TerminalNode *VERSION_STAMP();
    std::vector<antlr4::tree::TerminalNode *> Equ_op();
    antlr4::tree::TerminalNode* Equ_op(size_t i);
    antlr4::tree::TerminalNode *Version();
    antlr4::tree::TerminalNode *DATE();
    std::vector<antlr4::tree::TerminalNode *> Date_time();
    antlr4::tree::TerminalNode* Date_time(size_t i);
    antlr4::tree::TerminalNode *FLAG_VS();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Version_statementContext* version_statement();

  class  Amber_atom_type_statementContext : public antlr4::ParserRuleContext {
  public:
    Amber_atom_type_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *AMBER_ATOM_TYPE();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_AA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Amber_atom_type_statementContext* amber_atom_type_statement();

  class  Angle_equil_value_statementContext : public antlr4::ParserRuleContext {
  public:
    Angle_equil_value_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ANGLE_EQUIL_VALUE();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_equil_value_statementContext* angle_equil_value_statement();

  class  Angle_force_constant_statementContext : public antlr4::ParserRuleContext {
  public:
    Angle_force_constant_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ANGLE_FORCE_CONSTANT();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_force_constant_statementContext* angle_force_constant_statement();

  class  Angles_inc_hydrogen_statementContext : public antlr4::ParserRuleContext {
  public:
    Angles_inc_hydrogen_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ANGLES_INC_HYDROGEN();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angles_inc_hydrogen_statementContext* angles_inc_hydrogen_statement();

  class  Angles_without_hydrogen_statementContext : public antlr4::ParserRuleContext {
  public:
    Angles_without_hydrogen_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ANGLES_WITHOUT_HYDROGEN();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angles_without_hydrogen_statementContext* angles_without_hydrogen_statement();

  class  Atomic_number_statementContext : public antlr4::ParserRuleContext {
  public:
    Atomic_number_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ATOMIC_NUMBER();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atomic_number_statementContext* atomic_number_statement();

  class  Atom_name_statementContext : public antlr4::ParserRuleContext {
  public:
    Atom_name_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ATOM_NAME();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_AA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_name_statementContext* atom_name_statement();

  class  Atom_type_index_statementContext : public antlr4::ParserRuleContext {
  public:
    Atom_type_index_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ATOM_TYPE_INDEX();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_type_index_statementContext* atom_type_index_statement();

  class  Atoms_per_molecule_statementContext : public antlr4::ParserRuleContext {
  public:
    Atoms_per_molecule_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ATOMS_PER_MOLECULE();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atoms_per_molecule_statementContext* atoms_per_molecule_statement();

  class  Bond_equil_value_statementContext : public antlr4::ParserRuleContext {
  public:
    Bond_equil_value_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *BOND_EQUIL_VALUE();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Bond_equil_value_statementContext* bond_equil_value_statement();

  class  Bond_force_constant_statementContext : public antlr4::ParserRuleContext {
  public:
    Bond_force_constant_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *BOND_FORCE_CONSTANT();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Bond_force_constant_statementContext* bond_force_constant_statement();

  class  Bonds_inc_hydrogen_statementContext : public antlr4::ParserRuleContext {
  public:
    Bonds_inc_hydrogen_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *BONDS_INC_HYDROGEN();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Bonds_inc_hydrogen_statementContext* bonds_inc_hydrogen_statement();

  class  Bonds_without_hydrogen_statementContext : public antlr4::ParserRuleContext {
  public:
    Bonds_without_hydrogen_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *BONDS_WITHOUT_HYDROGEN();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Bonds_without_hydrogen_statementContext* bonds_without_hydrogen_statement();

  class  Box_dimensions_statementContext : public antlr4::ParserRuleContext {
  public:
    Box_dimensions_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *BOX_DIMENSIONS();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Box_dimensions_statementContext* box_dimensions_statement();

  class  Cap_info_statementContext : public antlr4::ParserRuleContext {
  public:
    Cap_info_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *CAP_INFO();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cap_info_statementContext* cap_info_statement();

  class  Cap_info2_statementContext : public antlr4::ParserRuleContext {
  public:
    Cap_info2_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *CAP_INFO2();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cap_info2_statementContext* cap_info2_statement();

  class  Charge_statementContext : public antlr4::ParserRuleContext {
  public:
    Charge_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *CHARGE();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Charge_statementContext* charge_statement();

  class  Cmap_count_statementContext : public antlr4::ParserRuleContext {
  public:
    Cmap_count_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *CMAP_COUNT();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cmap_count_statementContext* cmap_count_statement();

  class  Cmap_resolution_statementContext : public antlr4::ParserRuleContext {
  public:
    Cmap_resolution_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *CMAP_RESOLUTION();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cmap_resolution_statementContext* cmap_resolution_statement();

  class  Cmap_parameter_statementContext : public antlr4::ParserRuleContext {
  public:
    Cmap_parameter_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_01();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_02();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_03();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_04();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_05();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_06();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_07();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_08();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_09();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_10();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_11();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_12();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_13();
    antlr4::tree::TerminalNode *CMAP_PARAMETER_14();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cmap_parameter_statementContext* cmap_parameter_statement();

  class  Cmap_index_statementContext : public antlr4::ParserRuleContext {
  public:
    Cmap_index_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *CMAP_INDEX();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cmap_index_statementContext* cmap_index_statement();

  class  Dihedral_force_constant_statementContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_force_constant_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *DIHEDRAL_FORCE_CONSTANT();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_force_constant_statementContext* dihedral_force_constant_statement();

  class  Dihedral_periodicity_statementContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_periodicity_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *DIHEDRAL_PERIODICITY();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_periodicity_statementContext* dihedral_periodicity_statement();

  class  Dihedral_phase_statementContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_phase_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *DIHEDRAL_PHASE();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_phase_statementContext* dihedral_phase_statement();

  class  Dihedrals_inc_hydrogen_statementContext : public antlr4::ParserRuleContext {
  public:
    Dihedrals_inc_hydrogen_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *DIHEDRALS_INC_HYDROGEN();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedrals_inc_hydrogen_statementContext* dihedrals_inc_hydrogen_statement();

  class  Dihedrals_without_hydrogen_statementContext : public antlr4::ParserRuleContext {
  public:
    Dihedrals_without_hydrogen_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *DIHEDRALS_WITHOUT_HYDROGEN();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedrals_without_hydrogen_statementContext* dihedrals_without_hydrogen_statement();

  class  Excluded_atoms_list_statementContext : public antlr4::ParserRuleContext {
  public:
    Excluded_atoms_list_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EXCLUDED_ATOMS_LIST();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Excluded_atoms_list_statementContext* excluded_atoms_list_statement();

  class  Hbcut_statementContext : public antlr4::ParserRuleContext {
  public:
    Hbcut_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *HBCUT();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Hbcut_statementContext* hbcut_statement();

  class  Hbond_acoef_statementContext : public antlr4::ParserRuleContext {
  public:
    Hbond_acoef_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *HBOND_ACOEF();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Hbond_acoef_statementContext* hbond_acoef_statement();

  class  Hbond_bcoef_statementContext : public antlr4::ParserRuleContext {
  public:
    Hbond_bcoef_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *HBOND_BCOEF();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Hbond_bcoef_statementContext* hbond_bcoef_statement();

  class  Ipol_statementContext : public antlr4::ParserRuleContext {
  public:
    Ipol_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *IPOL();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ipol_statementContext* ipol_statement();

  class  Irotat_statementContext : public antlr4::ParserRuleContext {
  public:
    Irotat_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *IROTAT();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Irotat_statementContext* irotat_statement();

  class  Join_array_statementContext : public antlr4::ParserRuleContext {
  public:
    Join_array_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *JOIN_ARRAY();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Join_array_statementContext* join_array_statement();

  class  Lennard_jones_acoef_statementContext : public antlr4::ParserRuleContext {
  public:
    Lennard_jones_acoef_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *LENNARD_JONES_ACOEF();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Lennard_jones_acoef_statementContext* lennard_jones_acoef_statement();

  class  Lennard_jones_bcoef_statementContext : public antlr4::ParserRuleContext {
  public:
    Lennard_jones_bcoef_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *LENNARD_JONES_BCOEF();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Lennard_jones_bcoef_statementContext* lennard_jones_bcoef_statement();

  class  Mass_statementContext : public antlr4::ParserRuleContext {
  public:
    Mass_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *MASS();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Mass_statementContext* mass_statement();

  class  Nonbonded_parm_index_statementContext : public antlr4::ParserRuleContext {
  public:
    Nonbonded_parm_index_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *NONBONDED_PARM_INDEX();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Nonbonded_parm_index_statementContext* nonbonded_parm_index_statement();

  class  Number_excluded_atoms_statementContext : public antlr4::ParserRuleContext {
  public:
    Number_excluded_atoms_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *NUMBER_EXCLUDED_ATOMS();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Number_excluded_atoms_statementContext* number_excluded_atoms_statement();

  class  Pointers_statementContext : public antlr4::ParserRuleContext {
  public:
    Pointers_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *POINTERS();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pointers_statementContext* pointers_statement();

  class  Polarizability_statementContext : public antlr4::ParserRuleContext {
  public:
    Polarizability_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *POLARIZABILITY();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Polarizability_statementContext* polarizability_statement();

  class  Radii_statementContext : public antlr4::ParserRuleContext {
  public:
    Radii_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RADII();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Radii_statementContext* radii_statement();

  class  Radius_set_statementContext : public antlr4::ParserRuleContext {
  public:
    Radius_set_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RADIUS_SET();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_AA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Radius_set_statementContext* radius_set_statement();

  class  Residue_label_statementContext : public antlr4::ParserRuleContext {
  public:
    Residue_label_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RESIDUE_LABEL();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_AA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Residue_label_statementContext* residue_label_statement();

  class  Residue_pointer_statementContext : public antlr4::ParserRuleContext {
  public:
    Residue_pointer_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RESIDUE_POINTER();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Residue_pointer_statementContext* residue_pointer_statement();

  class  Scee_scale_factor_statementContext : public antlr4::ParserRuleContext {
  public:
    Scee_scale_factor_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *SCEE_SCALE_FACTOR();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Scee_scale_factor_statementContext* scee_scale_factor_statement();

  class  Scnb_scale_factor_statementContext : public antlr4::ParserRuleContext {
  public:
    Scnb_scale_factor_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *SCNB_SCALE_FACTOR();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Scnb_scale_factor_statementContext* scnb_scale_factor_statement();

  class  Screen_statementContext : public antlr4::ParserRuleContext {
  public:
    Screen_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *SCREEN();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Screen_statementContext* screen_statement();

  class  Solty_statementContext : public antlr4::ParserRuleContext {
  public:
    Solty_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *SOLTY();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_EA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Real();
    antlr4::tree::TerminalNode* Real(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Solty_statementContext* solty_statement();

  class  Solvent_pointers_statementContext : public antlr4::ParserRuleContext {
  public:
    Solvent_pointers_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *SOLVENT_POINTERS();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_IA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Solvent_pointers_statementContext* solvent_pointers_statement();

  class  Title_statementContext : public antlr4::ParserRuleContext {
  public:
    Title_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *TITLE();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_AA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Title_statementContext* title_statement();

  class  Tree_chain_classification_statementContext : public antlr4::ParserRuleContext {
  public:
    Tree_chain_classification_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *TREE_CHAIN_CLASSIFICATION();
    Format_functionContext *format_function();
    antlr4::tree::TerminalNode *FLAG_AA();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Tree_chain_classification_statementContext* tree_chain_classification_statement();

  class  Format_functionContext : public antlr4::ParserRuleContext {
  public:
    Format_functionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FORMAT();
    antlr4::tree::TerminalNode *Fortran_format_A();
    antlr4::tree::TerminalNode *Fortran_format_I();
    antlr4::tree::TerminalNode *Fortran_format_E();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Format_functionContext* format_function();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

