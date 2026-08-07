
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AmberMRParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "AmberMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by AmberMRParser.
 */
class  AmberMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by AmberMRParser.
   */
    virtual std::any visitAmber_mr(AmberMRParser::Amber_mrContext *context) = 0;

    virtual std::any visitComment(AmberMRParser::CommentContext *context) = 0;

    virtual std::any visitNmr_restraint(AmberMRParser::Nmr_restraintContext *context) = 0;

    virtual std::any visitNoesy_volume_restraint(AmberMRParser::Noesy_volume_restraintContext *context) = 0;

    virtual std::any visitChemical_shift_restraint(AmberMRParser::Chemical_shift_restraintContext *context) = 0;

    virtual std::any visitPcs_restraint(AmberMRParser::Pcs_restraintContext *context) = 0;

    virtual std::any visitDipolar_coupling_restraint(AmberMRParser::Dipolar_coupling_restraintContext *context) = 0;

    virtual std::any visitCsa_restraint(AmberMRParser::Csa_restraintContext *context) = 0;

    virtual std::any visitRestraint_statement(AmberMRParser::Restraint_statementContext *context) = 0;

    virtual std::any visitRestraint_factor(AmberMRParser::Restraint_factorContext *context) = 0;

    virtual std::any visitNoeexp_statement(AmberMRParser::Noeexp_statementContext *context) = 0;

    virtual std::any visitNoeexp_factor(AmberMRParser::Noeexp_factorContext *context) = 0;

    virtual std::any visitShf_statement(AmberMRParser::Shf_statementContext *context) = 0;

    virtual std::any visitShf_factor(AmberMRParser::Shf_factorContext *context) = 0;

    virtual std::any visitPcshf_statement(AmberMRParser::Pcshf_statementContext *context) = 0;

    virtual std::any visitPcshf_factor(AmberMRParser::Pcshf_factorContext *context) = 0;

    virtual std::any visitAlign_statement(AmberMRParser::Align_statementContext *context) = 0;

    virtual std::any visitAlign_factor(AmberMRParser::Align_factorContext *context) = 0;

    virtual std::any visitCsa_statement(AmberMRParser::Csa_statementContext *context) = 0;

    virtual std::any visitCsa_factor(AmberMRParser::Csa_factorContext *context) = 0;

    virtual std::any visitDistance_rst_func_call(AmberMRParser::Distance_rst_func_callContext *context) = 0;

    virtual std::any visitAngle_rst_func_call(AmberMRParser::Angle_rst_func_callContext *context) = 0;

    virtual std::any visitPlane_point_angle_rst_func_call(AmberMRParser::Plane_point_angle_rst_func_callContext *context) = 0;

    virtual std::any visitPlane_plane_angle_rst_func_call(AmberMRParser::Plane_plane_angle_rst_func_callContext *context) = 0;

    virtual std::any visitTorsion_rst_func_call(AmberMRParser::Torsion_rst_func_callContext *context) = 0;

    virtual std::any visitCoordinate2_rst_func_call(AmberMRParser::Coordinate2_rst_func_callContext *context) = 0;

    virtual std::any visitCoordinate3_rst_func_call(AmberMRParser::Coordinate3_rst_func_callContext *context) = 0;

    virtual std::any visitCoordinate4_rst_func_call(AmberMRParser::Coordinate4_rst_func_callContext *context) = 0;

    virtual std::any visitRestraint_func_expr(AmberMRParser::Restraint_func_exprContext *context) = 0;

    virtual std::any visitPlane_rst_func_call(AmberMRParser::Plane_rst_func_callContext *context) = 0;

    virtual std::any visitCom_rst_func_call(AmberMRParser::Com_rst_func_callContext *context) = 0;

    virtual std::any visitUnambig_atom_name_mapping(AmberMRParser::Unambig_atom_name_mappingContext *context) = 0;

    virtual std::any visitMapping_list(AmberMRParser::Mapping_listContext *context) = 0;

    virtual std::any visitAmbig_atom_name_mapping(AmberMRParser::Ambig_atom_name_mappingContext *context) = 0;

    virtual std::any visitAmbig_list(AmberMRParser::Ambig_listContext *context) = 0;


};

