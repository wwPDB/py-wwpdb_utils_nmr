
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewPKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "NmrViewPKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by NmrViewPKParser.
 */
class  NmrViewPKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by NmrViewPKParser.
   */
    virtual std::any visitNmrview_pk(NmrViewPKParser::Nmrview_pkContext *context) = 0;

    virtual std::any visitData_label(NmrViewPKParser::Data_labelContext *context) = 0;

    virtual std::any visitLabels(NmrViewPKParser::LabelsContext *context) = 0;

    virtual std::any visitPeak_list_2d(NmrViewPKParser::Peak_list_2dContext *context) = 0;

    virtual std::any visitPeak_2d(NmrViewPKParser::Peak_2dContext *context) = 0;

    virtual std::any visitPeak_list_3d(NmrViewPKParser::Peak_list_3dContext *context) = 0;

    virtual std::any visitPeak_3d(NmrViewPKParser::Peak_3dContext *context) = 0;

    virtual std::any visitPeak_list_4d(NmrViewPKParser::Peak_list_4dContext *context) = 0;

    virtual std::any visitPeak_4d(NmrViewPKParser::Peak_4dContext *context) = 0;

    virtual std::any visitPeak_list_wo_eju_2d(NmrViewPKParser::Peak_list_wo_eju_2dContext *context) = 0;

    virtual std::any visitPeak_wo_eju_2d(NmrViewPKParser::Peak_wo_eju_2dContext *context) = 0;

    virtual std::any visitPeak_list_wo_eju_3d(NmrViewPKParser::Peak_list_wo_eju_3dContext *context) = 0;

    virtual std::any visitPeak_wo_eju_3d(NmrViewPKParser::Peak_wo_eju_3dContext *context) = 0;

    virtual std::any visitPeak_list_wo_eju_4d(NmrViewPKParser::Peak_list_wo_eju_4dContext *context) = 0;

    virtual std::any visitPeak_wo_eju_4d(NmrViewPKParser::Peak_wo_eju_4dContext *context) = 0;

    virtual std::any visitLabel(NmrViewPKParser::LabelContext *context) = 0;

    virtual std::any visitJcoupling(NmrViewPKParser::JcouplingContext *context) = 0;

    virtual std::any visitNumber(NmrViewPKParser::NumberContext *context) = 0;

    virtual std::any visitEnclose_data(NmrViewPKParser::Enclose_dataContext *context) = 0;


};

