
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrPipePKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "NmrPipePKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by NmrPipePKParser.
 */
class  NmrPipePKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by NmrPipePKParser.
   */
    virtual std::any visitNmrpipe_pk(NmrPipePKParser::Nmrpipe_pkContext *context) = 0;

    virtual std::any visitData_label(NmrPipePKParser::Data_labelContext *context) = 0;

    virtual std::any visitPeak_list_2d(NmrPipePKParser::Peak_list_2dContext *context) = 0;

    virtual std::any visitPeak_2d(NmrPipePKParser::Peak_2dContext *context) = 0;

    virtual std::any visitPeak_list_3d(NmrPipePKParser::Peak_list_3dContext *context) = 0;

    virtual std::any visitPeak_3d(NmrPipePKParser::Peak_3dContext *context) = 0;

    virtual std::any visitPeak_list_4d(NmrPipePKParser::Peak_list_4dContext *context) = 0;

    virtual std::any visitPeak_4d(NmrPipePKParser::Peak_4dContext *context) = 0;

    virtual std::any visitPipp_label(NmrPipePKParser::Pipp_labelContext *context) = 0;

    virtual std::any visitPipp_axis(NmrPipePKParser::Pipp_axisContext *context) = 0;

    virtual std::any visitPipp_peak_list_2d(NmrPipePKParser::Pipp_peak_list_2dContext *context) = 0;

    virtual std::any visitPipp_peak_2d(NmrPipePKParser::Pipp_peak_2dContext *context) = 0;

    virtual std::any visitPipp_peak_list_3d(NmrPipePKParser::Pipp_peak_list_3dContext *context) = 0;

    virtual std::any visitPipp_peak_3d(NmrPipePKParser::Pipp_peak_3dContext *context) = 0;

    virtual std::any visitPipp_peak_list_4d(NmrPipePKParser::Pipp_peak_list_4dContext *context) = 0;

    virtual std::any visitPipp_peak_4d(NmrPipePKParser::Pipp_peak_4dContext *context) = 0;

    virtual std::any visitPipp_row_peak_list_2d(NmrPipePKParser::Pipp_row_peak_list_2dContext *context) = 0;

    virtual std::any visitPipp_row_peak_2d(NmrPipePKParser::Pipp_row_peak_2dContext *context) = 0;

    virtual std::any visitPipp_row_peak_list_3d(NmrPipePKParser::Pipp_row_peak_list_3dContext *context) = 0;

    virtual std::any visitPipp_row_peak_3d(NmrPipePKParser::Pipp_row_peak_3dContext *context) = 0;

    virtual std::any visitPipp_row_peak_list_4d(NmrPipePKParser::Pipp_row_peak_list_4dContext *context) = 0;

    virtual std::any visitPipp_row_peak_4d(NmrPipePKParser::Pipp_row_peak_4dContext *context) = 0;

    virtual std::any visitNumber(NmrPipePKParser::NumberContext *context) = 0;


};

