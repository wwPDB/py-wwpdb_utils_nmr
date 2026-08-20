
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/OliviaPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "OliviaPKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by OliviaPKParser.
 */
class  OliviaPKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by OliviaPKParser.
   */
    virtual std::any visitOlivia_pk(OliviaPKParser::Olivia_pkContext *context) = 0;

    virtual std::any visitComment(OliviaPKParser::CommentContext *context) = 0;

    virtual std::any visitIdx_peak_list_2d(OliviaPKParser::Idx_peak_list_2dContext *context) = 0;

    virtual std::any visitIdx_peak_2d(OliviaPKParser::Idx_peak_2dContext *context) = 0;

    virtual std::any visitIdx_peak_list_3d(OliviaPKParser::Idx_peak_list_3dContext *context) = 0;

    virtual std::any visitIdx_peak_3d(OliviaPKParser::Idx_peak_3dContext *context) = 0;

    virtual std::any visitIdx_peak_list_4d(OliviaPKParser::Idx_peak_list_4dContext *context) = 0;

    virtual std::any visitIdx_peak_4d(OliviaPKParser::Idx_peak_4dContext *context) = 0;

    virtual std::any visitAss_peak_list_2d(OliviaPKParser::Ass_peak_list_2dContext *context) = 0;

    virtual std::any visitAss_peak_2d(OliviaPKParser::Ass_peak_2dContext *context) = 0;

    virtual std::any visitAss_peak_list_3d(OliviaPKParser::Ass_peak_list_3dContext *context) = 0;

    virtual std::any visitAss_peak_3d(OliviaPKParser::Ass_peak_3dContext *context) = 0;

    virtual std::any visitAss_peak_list_4d(OliviaPKParser::Ass_peak_list_4dContext *context) = 0;

    virtual std::any visitAss_peak_4d(OliviaPKParser::Ass_peak_4dContext *context) = 0;

    virtual std::any visitDef_2d_axis_order_ppm(OliviaPKParser::Def_2d_axis_order_ppmContext *context) = 0;

    virtual std::any visitTp_2d_axis_order_ppm(OliviaPKParser::Tp_2d_axis_order_ppmContext *context) = 0;

    virtual std::any visitDef_2d_axis_order_hz(OliviaPKParser::Def_2d_axis_order_hzContext *context) = 0;

    virtual std::any visitTp_2d_axis_order_hz(OliviaPKParser::Tp_2d_axis_order_hzContext *context) = 0;

    virtual std::any visitDef_3d_axis_order_ppm(OliviaPKParser::Def_3d_axis_order_ppmContext *context) = 0;

    virtual std::any visitTp_3d_axis_order_ppm(OliviaPKParser::Tp_3d_axis_order_ppmContext *context) = 0;

    virtual std::any visitDef_3d_axis_order_hz(OliviaPKParser::Def_3d_axis_order_hzContext *context) = 0;

    virtual std::any visitTp_3d_axis_order_hz(OliviaPKParser::Tp_3d_axis_order_hzContext *context) = 0;

    virtual std::any visitDef_4d_axis_order_ppm(OliviaPKParser::Def_4d_axis_order_ppmContext *context) = 0;

    virtual std::any visitTp_4d_axis_order_ppm(OliviaPKParser::Tp_4d_axis_order_ppmContext *context) = 0;

    virtual std::any visitDef_4d_axis_order_hz(OliviaPKParser::Def_4d_axis_order_hzContext *context) = 0;

    virtual std::any visitTp_4d_axis_order_hz(OliviaPKParser::Tp_4d_axis_order_hzContext *context) = 0;

    virtual std::any visitString(OliviaPKParser::StringContext *context) = 0;

    virtual std::any visitInteger(OliviaPKParser::IntegerContext *context) = 0;

    virtual std::any visitNumber(OliviaPKParser::NumberContext *context) = 0;

    virtual std::any visitMemo(OliviaPKParser::MemoContext *context) = 0;


};

