
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AmberPTParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "AmberPTParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by AmberPTParser.
 */
class  AmberPTParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by AmberPTParser.
   */
    virtual std::any visitAmber_pt(AmberPTParser::Amber_ptContext *context) = 0;

    virtual std::any visitVersion_statement(AmberPTParser::Version_statementContext *context) = 0;

    virtual std::any visitAmber_atom_type_statement(AmberPTParser::Amber_atom_type_statementContext *context) = 0;

    virtual std::any visitAngle_equil_value_statement(AmberPTParser::Angle_equil_value_statementContext *context) = 0;

    virtual std::any visitAngle_force_constant_statement(AmberPTParser::Angle_force_constant_statementContext *context) = 0;

    virtual std::any visitAngles_inc_hydrogen_statement(AmberPTParser::Angles_inc_hydrogen_statementContext *context) = 0;

    virtual std::any visitAngles_without_hydrogen_statement(AmberPTParser::Angles_without_hydrogen_statementContext *context) = 0;

    virtual std::any visitAtomic_number_statement(AmberPTParser::Atomic_number_statementContext *context) = 0;

    virtual std::any visitAtom_name_statement(AmberPTParser::Atom_name_statementContext *context) = 0;

    virtual std::any visitAtom_type_index_statement(AmberPTParser::Atom_type_index_statementContext *context) = 0;

    virtual std::any visitAtoms_per_molecule_statement(AmberPTParser::Atoms_per_molecule_statementContext *context) = 0;

    virtual std::any visitBond_equil_value_statement(AmberPTParser::Bond_equil_value_statementContext *context) = 0;

    virtual std::any visitBond_force_constant_statement(AmberPTParser::Bond_force_constant_statementContext *context) = 0;

    virtual std::any visitBonds_inc_hydrogen_statement(AmberPTParser::Bonds_inc_hydrogen_statementContext *context) = 0;

    virtual std::any visitBonds_without_hydrogen_statement(AmberPTParser::Bonds_without_hydrogen_statementContext *context) = 0;

    virtual std::any visitBox_dimensions_statement(AmberPTParser::Box_dimensions_statementContext *context) = 0;

    virtual std::any visitCap_info_statement(AmberPTParser::Cap_info_statementContext *context) = 0;

    virtual std::any visitCap_info2_statement(AmberPTParser::Cap_info2_statementContext *context) = 0;

    virtual std::any visitCharge_statement(AmberPTParser::Charge_statementContext *context) = 0;

    virtual std::any visitCmap_count_statement(AmberPTParser::Cmap_count_statementContext *context) = 0;

    virtual std::any visitCmap_resolution_statement(AmberPTParser::Cmap_resolution_statementContext *context) = 0;

    virtual std::any visitCmap_parameter_statement(AmberPTParser::Cmap_parameter_statementContext *context) = 0;

    virtual std::any visitCmap_index_statement(AmberPTParser::Cmap_index_statementContext *context) = 0;

    virtual std::any visitDihedral_force_constant_statement(AmberPTParser::Dihedral_force_constant_statementContext *context) = 0;

    virtual std::any visitDihedral_periodicity_statement(AmberPTParser::Dihedral_periodicity_statementContext *context) = 0;

    virtual std::any visitDihedral_phase_statement(AmberPTParser::Dihedral_phase_statementContext *context) = 0;

    virtual std::any visitDihedrals_inc_hydrogen_statement(AmberPTParser::Dihedrals_inc_hydrogen_statementContext *context) = 0;

    virtual std::any visitDihedrals_without_hydrogen_statement(AmberPTParser::Dihedrals_without_hydrogen_statementContext *context) = 0;

    virtual std::any visitExcluded_atoms_list_statement(AmberPTParser::Excluded_atoms_list_statementContext *context) = 0;

    virtual std::any visitHbcut_statement(AmberPTParser::Hbcut_statementContext *context) = 0;

    virtual std::any visitHbond_acoef_statement(AmberPTParser::Hbond_acoef_statementContext *context) = 0;

    virtual std::any visitHbond_bcoef_statement(AmberPTParser::Hbond_bcoef_statementContext *context) = 0;

    virtual std::any visitIpol_statement(AmberPTParser::Ipol_statementContext *context) = 0;

    virtual std::any visitIrotat_statement(AmberPTParser::Irotat_statementContext *context) = 0;

    virtual std::any visitJoin_array_statement(AmberPTParser::Join_array_statementContext *context) = 0;

    virtual std::any visitLennard_jones_acoef_statement(AmberPTParser::Lennard_jones_acoef_statementContext *context) = 0;

    virtual std::any visitLennard_jones_bcoef_statement(AmberPTParser::Lennard_jones_bcoef_statementContext *context) = 0;

    virtual std::any visitMass_statement(AmberPTParser::Mass_statementContext *context) = 0;

    virtual std::any visitNonbonded_parm_index_statement(AmberPTParser::Nonbonded_parm_index_statementContext *context) = 0;

    virtual std::any visitNumber_excluded_atoms_statement(AmberPTParser::Number_excluded_atoms_statementContext *context) = 0;

    virtual std::any visitPointers_statement(AmberPTParser::Pointers_statementContext *context) = 0;

    virtual std::any visitPolarizability_statement(AmberPTParser::Polarizability_statementContext *context) = 0;

    virtual std::any visitRadii_statement(AmberPTParser::Radii_statementContext *context) = 0;

    virtual std::any visitRadius_set_statement(AmberPTParser::Radius_set_statementContext *context) = 0;

    virtual std::any visitResidue_label_statement(AmberPTParser::Residue_label_statementContext *context) = 0;

    virtual std::any visitResidue_pointer_statement(AmberPTParser::Residue_pointer_statementContext *context) = 0;

    virtual std::any visitScee_scale_factor_statement(AmberPTParser::Scee_scale_factor_statementContext *context) = 0;

    virtual std::any visitScnb_scale_factor_statement(AmberPTParser::Scnb_scale_factor_statementContext *context) = 0;

    virtual std::any visitScreen_statement(AmberPTParser::Screen_statementContext *context) = 0;

    virtual std::any visitSolty_statement(AmberPTParser::Solty_statementContext *context) = 0;

    virtual std::any visitSolvent_pointers_statement(AmberPTParser::Solvent_pointers_statementContext *context) = 0;

    virtual std::any visitTitle_statement(AmberPTParser::Title_statementContext *context) = 0;

    virtual std::any visitTree_chain_classification_statement(AmberPTParser::Tree_chain_classification_statementContext *context) = 0;

    virtual std::any visitFormat_function(AmberPTParser::Format_functionContext *context) = 0;


};

