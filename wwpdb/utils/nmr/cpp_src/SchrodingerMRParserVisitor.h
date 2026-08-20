
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SchrodingerMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "SchrodingerMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by SchrodingerMRParser.
 */
class  SchrodingerMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by SchrodingerMRParser.
   */
    virtual std::any visitSchrodinger_mr(SchrodingerMRParser::Schrodinger_mrContext *context) = 0;

    virtual std::any visitImport_structure(SchrodingerMRParser::Import_structureContext *context) = 0;

    virtual std::any visitStruct_statement(SchrodingerMRParser::Struct_statementContext *context) = 0;

    virtual std::any visitDistance_restraint(SchrodingerMRParser::Distance_restraintContext *context) = 0;

    virtual std::any visitDihedral_angle_restraint(SchrodingerMRParser::Dihedral_angle_restraintContext *context) = 0;

    virtual std::any visitAngle_restraint(SchrodingerMRParser::Angle_restraintContext *context) = 0;

    virtual std::any visitDistance_statement(SchrodingerMRParser::Distance_statementContext *context) = 0;

    virtual std::any visitDistance_assign(SchrodingerMRParser::Distance_assignContext *context) = 0;

    virtual std::any visitDistance_assign_by_number(SchrodingerMRParser::Distance_assign_by_numberContext *context) = 0;

    virtual std::any visitDihedral_angle_statement(SchrodingerMRParser::Dihedral_angle_statementContext *context) = 0;

    virtual std::any visitDihedral_angle_assign(SchrodingerMRParser::Dihedral_angle_assignContext *context) = 0;

    virtual std::any visitDihedral_angle_assign_by_number(SchrodingerMRParser::Dihedral_angle_assign_by_numberContext *context) = 0;

    virtual std::any visitAngle_statement(SchrodingerMRParser::Angle_statementContext *context) = 0;

    virtual std::any visitAngle_assign(SchrodingerMRParser::Angle_assignContext *context) = 0;

    virtual std::any visitAngle_assign_by_number(SchrodingerMRParser::Angle_assign_by_numberContext *context) = 0;

    virtual std::any visitFxdi_statement(SchrodingerMRParser::Fxdi_statementContext *context) = 0;

    virtual std::any visitFxdi_assign(SchrodingerMRParser::Fxdi_assignContext *context) = 0;

    virtual std::any visitFxdi_assign_by_number(SchrodingerMRParser::Fxdi_assign_by_numberContext *context) = 0;

    virtual std::any visitFxta_statement(SchrodingerMRParser::Fxta_statementContext *context) = 0;

    virtual std::any visitFxta_assign(SchrodingerMRParser::Fxta_assignContext *context) = 0;

    virtual std::any visitFxta_assign_by_number(SchrodingerMRParser::Fxta_assign_by_numberContext *context) = 0;

    virtual std::any visitFxba_statement(SchrodingerMRParser::Fxba_statementContext *context) = 0;

    virtual std::any visitFxba_assign(SchrodingerMRParser::Fxba_assignContext *context) = 0;

    virtual std::any visitFxba_assign_by_number(SchrodingerMRParser::Fxba_assign_by_numberContext *context) = 0;

    virtual std::any visitFxhb_statement(SchrodingerMRParser::Fxhb_statementContext *context) = 0;

    virtual std::any visitFxhb_assign(SchrodingerMRParser::Fxhb_assignContext *context) = 0;

    virtual std::any visitFxhb_assign_by_number(SchrodingerMRParser::Fxhb_assign_by_numberContext *context) = 0;

    virtual std::any visitSelection(SchrodingerMRParser::SelectionContext *context) = 0;

    virtual std::any visitSelection_expression(SchrodingerMRParser::Selection_expressionContext *context) = 0;

    virtual std::any visitTerm(SchrodingerMRParser::TermContext *context) = 0;

    virtual std::any visitFactor(SchrodingerMRParser::FactorContext *context) = 0;

    virtual std::any visitNumber(SchrodingerMRParser::NumberContext *context) = 0;

    virtual std::any visitNumber_f(SchrodingerMRParser::Number_fContext *context) = 0;

    virtual std::any visitParameter_statement(SchrodingerMRParser::Parameter_statementContext *context) = 0;


};

