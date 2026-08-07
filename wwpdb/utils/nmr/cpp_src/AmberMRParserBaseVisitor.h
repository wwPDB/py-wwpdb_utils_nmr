
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AmberMRParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "AmberMRParserVisitor.h"


/**
 * This class provides an empty implementation of AmberMRParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  AmberMRParserBaseVisitor : public AmberMRParserVisitor {
public:

  virtual std::any visitAmber_mr(AmberMRParser::Amber_mrContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComment(AmberMRParser::CommentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNmr_restraint(AmberMRParser::Nmr_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNoesy_volume_restraint(AmberMRParser::Noesy_volume_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChemical_shift_restraint(AmberMRParser::Chemical_shift_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPcs_restraint(AmberMRParser::Pcs_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDipolar_coupling_restraint(AmberMRParser::Dipolar_coupling_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCsa_restraint(AmberMRParser::Csa_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRestraint_statement(AmberMRParser::Restraint_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRestraint_factor(AmberMRParser::Restraint_factorContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNoeexp_statement(AmberMRParser::Noeexp_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNoeexp_factor(AmberMRParser::Noeexp_factorContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitShf_statement(AmberMRParser::Shf_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitShf_factor(AmberMRParser::Shf_factorContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPcshf_statement(AmberMRParser::Pcshf_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPcshf_factor(AmberMRParser::Pcshf_factorContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAlign_statement(AmberMRParser::Align_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAlign_factor(AmberMRParser::Align_factorContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCsa_statement(AmberMRParser::Csa_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCsa_factor(AmberMRParser::Csa_factorContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_rst_func_call(AmberMRParser::Distance_rst_func_callContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAngle_rst_func_call(AmberMRParser::Angle_rst_func_callContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPlane_point_angle_rst_func_call(AmberMRParser::Plane_point_angle_rst_func_callContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPlane_plane_angle_rst_func_call(AmberMRParser::Plane_plane_angle_rst_func_callContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTorsion_rst_func_call(AmberMRParser::Torsion_rst_func_callContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCoordinate2_rst_func_call(AmberMRParser::Coordinate2_rst_func_callContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCoordinate3_rst_func_call(AmberMRParser::Coordinate3_rst_func_callContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCoordinate4_rst_func_call(AmberMRParser::Coordinate4_rst_func_callContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRestraint_func_expr(AmberMRParser::Restraint_func_exprContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPlane_rst_func_call(AmberMRParser::Plane_rst_func_callContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCom_rst_func_call(AmberMRParser::Com_rst_func_callContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitUnambig_atom_name_mapping(AmberMRParser::Unambig_atom_name_mappingContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitMapping_list(AmberMRParser::Mapping_listContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAmbig_atom_name_mapping(AmberMRParser::Ambig_atom_name_mappingContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAmbig_list(AmberMRParser::Ambig_listContext *ctx) override {
    return visitChildren(ctx);
  }


};

