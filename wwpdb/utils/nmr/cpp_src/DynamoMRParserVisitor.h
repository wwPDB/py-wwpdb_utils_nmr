
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/DynamoMRParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "DynamoMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by DynamoMRParser.
 */
class  DynamoMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by DynamoMRParser.
   */
    virtual std::any visitDynamo_mr(DynamoMRParser::Dynamo_mrContext *context) = 0;

    virtual std::any visitSequence(DynamoMRParser::SequenceContext *context) = 0;

    virtual std::any visitDistance_restraints(DynamoMRParser::Distance_restraintsContext *context) = 0;

    virtual std::any visitDistance_restraint(DynamoMRParser::Distance_restraintContext *context) = 0;

    virtual std::any visitDistance_restraints_sw_segid(DynamoMRParser::Distance_restraints_sw_segidContext *context) = 0;

    virtual std::any visitDistance_restraint_sw_segid(DynamoMRParser::Distance_restraint_sw_segidContext *context) = 0;

    virtual std::any visitDistance_restraints_ew_segid(DynamoMRParser::Distance_restraints_ew_segidContext *context) = 0;

    virtual std::any visitDistance_restraint_ew_segid(DynamoMRParser::Distance_restraint_ew_segidContext *context) = 0;

    virtual std::any visitTorsion_angle_restraints(DynamoMRParser::Torsion_angle_restraintsContext *context) = 0;

    virtual std::any visitTorsion_angle_restraint(DynamoMRParser::Torsion_angle_restraintContext *context) = 0;

    virtual std::any visitTorsion_angle_restraints_sw_segid(DynamoMRParser::Torsion_angle_restraints_sw_segidContext *context) = 0;

    virtual std::any visitTorsion_angle_restraint_sw_segid(DynamoMRParser::Torsion_angle_restraint_sw_segidContext *context) = 0;

    virtual std::any visitTorsion_angle_restraints_ew_segid(DynamoMRParser::Torsion_angle_restraints_ew_segidContext *context) = 0;

    virtual std::any visitTorsion_angle_restraint_ew_segid(DynamoMRParser::Torsion_angle_restraint_ew_segidContext *context) = 0;

    virtual std::any visitRdc_restraints(DynamoMRParser::Rdc_restraintsContext *context) = 0;

    virtual std::any visitRdc_restraint(DynamoMRParser::Rdc_restraintContext *context) = 0;

    virtual std::any visitRdc_restraints_sw_segid(DynamoMRParser::Rdc_restraints_sw_segidContext *context) = 0;

    virtual std::any visitRdc_restraint_sw_segid(DynamoMRParser::Rdc_restraint_sw_segidContext *context) = 0;

    virtual std::any visitRdc_restraints_ew_segid(DynamoMRParser::Rdc_restraints_ew_segidContext *context) = 0;

    virtual std::any visitRdc_restraint_ew_segid(DynamoMRParser::Rdc_restraint_ew_segidContext *context) = 0;

    virtual std::any visitPales_meta_outputs(DynamoMRParser::Pales_meta_outputsContext *context) = 0;

    virtual std::any visitPales_rdc_outputs(DynamoMRParser::Pales_rdc_outputsContext *context) = 0;

    virtual std::any visitPales_rdc_output(DynamoMRParser::Pales_rdc_outputContext *context) = 0;

    virtual std::any visitCoupling_restraints(DynamoMRParser::Coupling_restraintsContext *context) = 0;

    virtual std::any visitCoupling_restraint(DynamoMRParser::Coupling_restraintContext *context) = 0;

    virtual std::any visitCoupling_restraints_sw_segid(DynamoMRParser::Coupling_restraints_sw_segidContext *context) = 0;

    virtual std::any visitCoupling_restraint_sw_segid(DynamoMRParser::Coupling_restraint_sw_segidContext *context) = 0;

    virtual std::any visitCoupling_restraints_ew_segid(DynamoMRParser::Coupling_restraints_ew_segidContext *context) = 0;

    virtual std::any visitCoupling_restraint_ew_segid(DynamoMRParser::Coupling_restraint_ew_segidContext *context) = 0;

    virtual std::any visitTalos_restraints(DynamoMRParser::Talos_restraintsContext *context) = 0;

    virtual std::any visitTalos_restraint(DynamoMRParser::Talos_restraintContext *context) = 0;

    virtual std::any visitTalos_restraints_wo_s2(DynamoMRParser::Talos_restraints_wo_s2Context *context) = 0;

    virtual std::any visitTalos_restraint_wo_s2(DynamoMRParser::Talos_restraint_wo_s2Context *context) = 0;

    virtual std::any visitNumber(DynamoMRParser::NumberContext *context) = 0;


};

