
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BarePKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "BarePKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by BarePKParser.
 */
class  BarePKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by BarePKParser.
   */
    virtual std::any visitBare_pk(BarePKParser::Bare_pkContext *context) = 0;

    virtual std::any visitPeak_list_2d(BarePKParser::Peak_list_2dContext *context) = 0;

    virtual std::any visitPeak_2d(BarePKParser::Peak_2dContext *context) = 0;

    virtual std::any visitPeak_list_3d(BarePKParser::Peak_list_3dContext *context) = 0;

    virtual std::any visitPeak_3d(BarePKParser::Peak_3dContext *context) = 0;

    virtual std::any visitPeak_list_4d(BarePKParser::Peak_list_4dContext *context) = 0;

    virtual std::any visitPeak_4d(BarePKParser::Peak_4dContext *context) = 0;

    virtual std::any visitPeak_list_wo_chain_2d(BarePKParser::Peak_list_wo_chain_2dContext *context) = 0;

    virtual std::any visitPeak_wo_chain_2d(BarePKParser::Peak_wo_chain_2dContext *context) = 0;

    virtual std::any visitPeak_list_wo_chain_3d(BarePKParser::Peak_list_wo_chain_3dContext *context) = 0;

    virtual std::any visitPeak_wo_chain_3d(BarePKParser::Peak_wo_chain_3dContext *context) = 0;

    virtual std::any visitPeak_list_wo_chain_4d(BarePKParser::Peak_list_wo_chain_4dContext *context) = 0;

    virtual std::any visitPeak_wo_chain_4d(BarePKParser::Peak_wo_chain_4dContext *context) = 0;

    virtual std::any visitRow_format_2d(BarePKParser::Row_format_2dContext *context) = 0;

    virtual std::any visitRow_format_3d(BarePKParser::Row_format_3dContext *context) = 0;

    virtual std::any visitRow_format_4d(BarePKParser::Row_format_4dContext *context) = 0;

    virtual std::any visitRev_row_format_2d(BarePKParser::Rev_row_format_2dContext *context) = 0;

    virtual std::any visitRev_row_format_3d(BarePKParser::Rev_row_format_3dContext *context) = 0;

    virtual std::any visitRev_row_format_4d(BarePKParser::Rev_row_format_4dContext *context) = 0;

    virtual std::any visitRow_format_wo_label_2d(BarePKParser::Row_format_wo_label_2dContext *context) = 0;

    virtual std::any visitRow_format_wo_label_3d(BarePKParser::Row_format_wo_label_3dContext *context) = 0;

    virtual std::any visitRow_format_wo_label_4d(BarePKParser::Row_format_wo_label_4dContext *context) = 0;

    virtual std::any visitPeak_list_row_2d(BarePKParser::Peak_list_row_2dContext *context) = 0;

    virtual std::any visitPeak_list_row_3d(BarePKParser::Peak_list_row_3dContext *context) = 0;

    virtual std::any visitPeak_list_row_4d(BarePKParser::Peak_list_row_4dContext *context) = 0;

    virtual std::any visitPosition(BarePKParser::PositionContext *context) = 0;

    virtual std::any visitNumber(BarePKParser::NumberContext *context) = 0;


};

