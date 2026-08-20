
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/VnmrPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "VnmrPKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by VnmrPKParser.
 */
class  VnmrPKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by VnmrPKParser.
   */
    virtual std::any visitVnmr_pk(VnmrPKParser::Vnmr_pkContext *context) = 0;

    virtual std::any visitComment(VnmrPKParser::CommentContext *context) = 0;

    virtual std::any visitFormat(VnmrPKParser::FormatContext *context) = 0;

    virtual std::any visitPeak_ll2d(VnmrPKParser::Peak_ll2dContext *context) = 0;

    virtual std::any visitPeak_ll3d(VnmrPKParser::Peak_ll3dContext *context) = 0;

    virtual std::any visitPeak_ll4d(VnmrPKParser::Peak_ll4dContext *context) = 0;

    virtual std::any visitData_label(VnmrPKParser::Data_labelContext *context) = 0;

    virtual std::any visitPeak_2d(VnmrPKParser::Peak_2dContext *context) = 0;

    virtual std::any visitPeak_3d(VnmrPKParser::Peak_3dContext *context) = 0;

    virtual std::any visitPeak_4d(VnmrPKParser::Peak_4dContext *context) = 0;

    virtual std::any visitNumber(VnmrPKParser::NumberContext *context) = 0;


};

