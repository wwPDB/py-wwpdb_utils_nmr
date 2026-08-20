
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XeasyPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "XeasyPKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by XeasyPKParser.
 */
class  XeasyPKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by XeasyPKParser.
   */
    virtual std::any visitXeasy_pk(XeasyPKParser::Xeasy_pkContext *context) = 0;

    virtual std::any visitDimension(XeasyPKParser::DimensionContext *context) = 0;

    virtual std::any visitPeak(XeasyPKParser::PeakContext *context) = 0;

    virtual std::any visitFormat(XeasyPKParser::FormatContext *context) = 0;

    virtual std::any visitIname(XeasyPKParser::InameContext *context) = 0;

    virtual std::any visitCyana_format(XeasyPKParser::Cyana_formatContext *context) = 0;

    virtual std::any visitSpectrum(XeasyPKParser::SpectrumContext *context) = 0;

    virtual std::any visitTolerance(XeasyPKParser::ToleranceContext *context) = 0;

    virtual std::any visitPeak_list_2d(XeasyPKParser::Peak_list_2dContext *context) = 0;

    virtual std::any visitPeak_2d(XeasyPKParser::Peak_2dContext *context) = 0;

    virtual std::any visitPeak_list_3d(XeasyPKParser::Peak_list_3dContext *context) = 0;

    virtual std::any visitPeak_3d(XeasyPKParser::Peak_3dContext *context) = 0;

    virtual std::any visitPeak_list_4d(XeasyPKParser::Peak_list_4dContext *context) = 0;

    virtual std::any visitPeak_4d(XeasyPKParser::Peak_4dContext *context) = 0;

    virtual std::any visitPosition(XeasyPKParser::PositionContext *context) = 0;

    virtual std::any visitNumber(XeasyPKParser::NumberContext *context) = 0;

    virtual std::any visitType_code(XeasyPKParser::Type_codeContext *context) = 0;

    virtual std::any visitAssign(XeasyPKParser::AssignContext *context) = 0;

    virtual std::any visitComment(XeasyPKParser::CommentContext *context) = 0;


};

