
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CharmmMRParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "CharmmMRParserVisitor.h"


/**
 * This class provides an empty implementation of CharmmMRParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  CharmmMRParserBaseVisitor : public CharmmMRParserVisitor {
public:

  virtual std::any visitCharmm_mr(CharmmMRParser::Charmm_mrContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComment(CharmmMRParser::CommentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_restraint(CharmmMRParser::Distance_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPoint_distance_restraint(CharmmMRParser::Point_distance_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDihedral_angle_restraint(CharmmMRParser::Dihedral_angle_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitHarmonic_restraint(CharmmMRParser::Harmonic_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitManipulate_internal_coordinate(CharmmMRParser::Manipulate_internal_coordinateContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDroplet_potential(CharmmMRParser::Droplet_potentialContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFix_atom_constraint(CharmmMRParser::Fix_atom_constraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCenter_of_mass_constraint(CharmmMRParser::Center_of_mass_constraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFix_bond_or_angle_constraint(CharmmMRParser::Fix_bond_or_angle_constraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRestrained_distance(CharmmMRParser::Restrained_distanceContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExternal_force(CharmmMRParser::External_forceContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRmsd_restraint(CharmmMRParser::Rmsd_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitGyration_restraint(CharmmMRParser::Gyration_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_matrix_restraint(CharmmMRParser::Distance_matrix_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNoe_statement(CharmmMRParser::Noe_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNoe_assign(CharmmMRParser::Noe_assignContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPnoe_statement(CharmmMRParser::Pnoe_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPnoe_assign(CharmmMRParser::Pnoe_assignContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDihedral_statement(CharmmMRParser::Dihedral_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDihedral_assign(CharmmMRParser::Dihedral_assignContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitHarmonic_statement(CharmmMRParser::Harmonic_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAbsolute_spec(CharmmMRParser::Absolute_specContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitForce_const_spec(CharmmMRParser::Force_const_specContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitBestfit_spec(CharmmMRParser::Bestfit_specContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCoordinate_spec(CharmmMRParser::Coordinate_specContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitIc_statement(CharmmMRParser::Ic_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDroplet_statement(CharmmMRParser::Droplet_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFix_atom_statement(CharmmMRParser::Fix_atom_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCenter_of_mass_statement(CharmmMRParser::Center_of_mass_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFix_bond_or_angle_statement(CharmmMRParser::Fix_bond_or_angle_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitShake_opt(CharmmMRParser::Shake_optContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFast_opt(CharmmMRParser::Fast_optContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRestrained_distance_statement(CharmmMRParser::Restrained_distance_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExternal_force_statement(CharmmMRParser::External_force_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRmsd_statement(CharmmMRParser::Rmsd_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRmsd_orient_spec(CharmmMRParser::Rmsd_orient_specContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRmsd_force_const_spec(CharmmMRParser::Rmsd_force_const_specContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRmsd_coordinate_spec(CharmmMRParser::Rmsd_coordinate_specContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitGyration_statement(CharmmMRParser::Gyration_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_matrix_statement(CharmmMRParser::Distance_matrix_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSelection(CharmmMRParser::SelectionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSelection_expression(CharmmMRParser::Selection_expressionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTerm(CharmmMRParser::TermContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFactor(CharmmMRParser::FactorContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(CharmmMRParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber_f(CharmmMRParser::Number_fContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber_s(CharmmMRParser::Number_sContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSet_statement(CharmmMRParser::Set_statementContext *ctx) override {
    return visitChildren(ctx);
  }


};

