
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkySPKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "SparkySPKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by SparkySPKParser.
 */
class  SparkySPKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by SparkySPKParser.
   */
    virtual std::any visitSparky_spk(SparkySPKParser::Sparky_spkContext *context) = 0;

    virtual std::any visitUser_block(SparkySPKParser::User_blockContext *context) = 0;

    virtual std::any visitUser_statement(SparkySPKParser::User_statementContext *context) = 0;

    virtual std::any visitSpectrum_block(SparkySPKParser::Spectrum_blockContext *context) = 0;

    virtual std::any visitSpectrum_statement(SparkySPKParser::Spectrum_statementContext *context) = 0;

    virtual std::any visitSpectrum_name(SparkySPKParser::Spectrum_nameContext *context) = 0;

    virtual std::any visitAttached_data(SparkySPKParser::Attached_dataContext *context) = 0;

    virtual std::any visitAttached_data_statement(SparkySPKParser::Attached_data_statementContext *context) = 0;

    virtual std::any visitView(SparkySPKParser::ViewContext *context) = 0;

    virtual std::any visitView_statement(SparkySPKParser::View_statementContext *context) = 0;

    virtual std::any visitView_name(SparkySPKParser::View_nameContext *context) = 0;

    virtual std::any visitView_number(SparkySPKParser::View_numberContext *context) = 0;

    virtual std::any visitParams(SparkySPKParser::ParamsContext *context) = 0;

    virtual std::any visitParams_statement(SparkySPKParser::Params_statementContext *context) = 0;

    virtual std::any visitOrnament(SparkySPKParser::OrnamentContext *context) = 0;

    virtual std::any visitOrnament_statement(SparkySPKParser::Ornament_statementContext *context) = 0;

    virtual std::any visitOrnament_position(SparkySPKParser::Ornament_positionContext *context) = 0;

    virtual std::any visitLabel(SparkySPKParser::LabelContext *context) = 0;

    virtual std::any visitLabel_statement(SparkySPKParser::Label_statementContext *context) = 0;

    virtual std::any visitLabel_position(SparkySPKParser::Label_positionContext *context) = 0;


};

