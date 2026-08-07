
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XwinNmrPKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "XwinNmrPKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by XwinNmrPKParser.
 */
class  XwinNmrPKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by XwinNmrPKParser.
   */
    virtual std::any visitXwinnmr_pk(XwinNmrPKParser::Xwinnmr_pkContext *context) = 0;

    virtual std::any visitComment(XwinNmrPKParser::CommentContext *context) = 0;

    virtual std::any visitDimension(XwinNmrPKParser::DimensionContext *context) = 0;

    virtual std::any visitPeak_2d(XwinNmrPKParser::Peak_2dContext *context) = 0;

    virtual std::any visitPeak_3d(XwinNmrPKParser::Peak_3dContext *context) = 0;

    virtual std::any visitPeak_4d(XwinNmrPKParser::Peak_4dContext *context) = 0;


};

