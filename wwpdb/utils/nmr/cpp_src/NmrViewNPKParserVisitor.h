
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewNPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "NmrViewNPKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by NmrViewNPKParser.
 */
class  NmrViewNPKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by NmrViewNPKParser.
   */
    virtual std::any visitNmrview_npk(NmrViewNPKParser::Nmrview_npkContext *context) = 0;

    virtual std::any visitData_label(NmrViewNPKParser::Data_labelContext *context) = 0;

    virtual std::any visitLabels(NmrViewNPKParser::LabelsContext *context) = 0;

    virtual std::any visitPeak_list_2d(NmrViewNPKParser::Peak_list_2dContext *context) = 0;

    virtual std::any visitPeak_2d(NmrViewNPKParser::Peak_2dContext *context) = 0;

    virtual std::any visitPeak_list_3d(NmrViewNPKParser::Peak_list_3dContext *context) = 0;

    virtual std::any visitPeak_3d(NmrViewNPKParser::Peak_3dContext *context) = 0;

    virtual std::any visitPeak_list_4d(NmrViewNPKParser::Peak_list_4dContext *context) = 0;

    virtual std::any visitPeak_4d(NmrViewNPKParser::Peak_4dContext *context) = 0;

    virtual std::any visitPeak_list_wo_eju_2d(NmrViewNPKParser::Peak_list_wo_eju_2dContext *context) = 0;

    virtual std::any visitPeak_wo_eju_2d(NmrViewNPKParser::Peak_wo_eju_2dContext *context) = 0;

    virtual std::any visitPeak_list_wo_eju_3d(NmrViewNPKParser::Peak_list_wo_eju_3dContext *context) = 0;

    virtual std::any visitPeak_wo_eju_3d(NmrViewNPKParser::Peak_wo_eju_3dContext *context) = 0;

    virtual std::any visitPeak_list_wo_eju_4d(NmrViewNPKParser::Peak_list_wo_eju_4dContext *context) = 0;

    virtual std::any visitPeak_wo_eju_4d(NmrViewNPKParser::Peak_wo_eju_4dContext *context) = 0;

    virtual std::any visitLabel(NmrViewNPKParser::LabelContext *context) = 0;

    virtual std::any visitJcoupling(NmrViewNPKParser::JcouplingContext *context) = 0;

    virtual std::any visitNumber(NmrViewNPKParser::NumberContext *context) = 0;


};

