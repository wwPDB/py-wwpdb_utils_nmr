
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CharmmMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "CharmmMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by CharmmMRParser.
 */
class  CharmmMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by CharmmMRParser.
   */
    virtual std::any visitCharmm_mr(CharmmMRParser::Charmm_mrContext *context) = 0;

    virtual std::any visitComment(CharmmMRParser::CommentContext *context) = 0;

    virtual std::any visitDistance_restraint(CharmmMRParser::Distance_restraintContext *context) = 0;

    virtual std::any visitPoint_distance_restraint(CharmmMRParser::Point_distance_restraintContext *context) = 0;

    virtual std::any visitDihedral_angle_restraint(CharmmMRParser::Dihedral_angle_restraintContext *context) = 0;

    virtual std::any visitHarmonic_restraint(CharmmMRParser::Harmonic_restraintContext *context) = 0;

    virtual std::any visitManipulate_internal_coordinate(CharmmMRParser::Manipulate_internal_coordinateContext *context) = 0;

    virtual std::any visitDroplet_potential(CharmmMRParser::Droplet_potentialContext *context) = 0;

    virtual std::any visitFix_atom_constraint(CharmmMRParser::Fix_atom_constraintContext *context) = 0;

    virtual std::any visitCenter_of_mass_constraint(CharmmMRParser::Center_of_mass_constraintContext *context) = 0;

    virtual std::any visitFix_bond_or_angle_constraint(CharmmMRParser::Fix_bond_or_angle_constraintContext *context) = 0;

    virtual std::any visitRestrained_distance(CharmmMRParser::Restrained_distanceContext *context) = 0;

    virtual std::any visitExternal_force(CharmmMRParser::External_forceContext *context) = 0;

    virtual std::any visitRmsd_restraint(CharmmMRParser::Rmsd_restraintContext *context) = 0;

    virtual std::any visitGyration_restraint(CharmmMRParser::Gyration_restraintContext *context) = 0;

    virtual std::any visitDistance_matrix_restraint(CharmmMRParser::Distance_matrix_restraintContext *context) = 0;

    virtual std::any visitNoe_statement(CharmmMRParser::Noe_statementContext *context) = 0;

    virtual std::any visitNoe_assign(CharmmMRParser::Noe_assignContext *context) = 0;

    virtual std::any visitPnoe_statement(CharmmMRParser::Pnoe_statementContext *context) = 0;

    virtual std::any visitPnoe_assign(CharmmMRParser::Pnoe_assignContext *context) = 0;

    virtual std::any visitDihedral_statement(CharmmMRParser::Dihedral_statementContext *context) = 0;

    virtual std::any visitDihedral_assign(CharmmMRParser::Dihedral_assignContext *context) = 0;

    virtual std::any visitHarmonic_statement(CharmmMRParser::Harmonic_statementContext *context) = 0;

    virtual std::any visitAbsolute_spec(CharmmMRParser::Absolute_specContext *context) = 0;

    virtual std::any visitForce_const_spec(CharmmMRParser::Force_const_specContext *context) = 0;

    virtual std::any visitBestfit_spec(CharmmMRParser::Bestfit_specContext *context) = 0;

    virtual std::any visitCoordinate_spec(CharmmMRParser::Coordinate_specContext *context) = 0;

    virtual std::any visitIc_statement(CharmmMRParser::Ic_statementContext *context) = 0;

    virtual std::any visitDroplet_statement(CharmmMRParser::Droplet_statementContext *context) = 0;

    virtual std::any visitFix_atom_statement(CharmmMRParser::Fix_atom_statementContext *context) = 0;

    virtual std::any visitCenter_of_mass_statement(CharmmMRParser::Center_of_mass_statementContext *context) = 0;

    virtual std::any visitFix_bond_or_angle_statement(CharmmMRParser::Fix_bond_or_angle_statementContext *context) = 0;

    virtual std::any visitShake_opt(CharmmMRParser::Shake_optContext *context) = 0;

    virtual std::any visitFast_opt(CharmmMRParser::Fast_optContext *context) = 0;

    virtual std::any visitRestrained_distance_statement(CharmmMRParser::Restrained_distance_statementContext *context) = 0;

    virtual std::any visitExternal_force_statement(CharmmMRParser::External_force_statementContext *context) = 0;

    virtual std::any visitRmsd_statement(CharmmMRParser::Rmsd_statementContext *context) = 0;

    virtual std::any visitRmsd_orient_spec(CharmmMRParser::Rmsd_orient_specContext *context) = 0;

    virtual std::any visitRmsd_force_const_spec(CharmmMRParser::Rmsd_force_const_specContext *context) = 0;

    virtual std::any visitRmsd_coordinate_spec(CharmmMRParser::Rmsd_coordinate_specContext *context) = 0;

    virtual std::any visitGyration_statement(CharmmMRParser::Gyration_statementContext *context) = 0;

    virtual std::any visitDistance_matrix_statement(CharmmMRParser::Distance_matrix_statementContext *context) = 0;

    virtual std::any visitSelection(CharmmMRParser::SelectionContext *context) = 0;

    virtual std::any visitSelection_expression(CharmmMRParser::Selection_expressionContext *context) = 0;

    virtual std::any visitTerm(CharmmMRParser::TermContext *context) = 0;

    virtual std::any visitFactor(CharmmMRParser::FactorContext *context) = 0;

    virtual std::any visitNumber(CharmmMRParser::NumberContext *context) = 0;

    virtual std::any visitNumber_f(CharmmMRParser::Number_fContext *context) = 0;

    virtual std::any visitNumber_s(CharmmMRParser::Number_sContext *context) = 0;

    virtual std::any visitSet_statement(CharmmMRParser::Set_statementContext *context) = 0;


};

