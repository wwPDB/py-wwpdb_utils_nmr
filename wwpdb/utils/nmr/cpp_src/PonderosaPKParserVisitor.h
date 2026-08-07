
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PonderosaPKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "PonderosaPKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by PonderosaPKParser.
 */
class  PonderosaPKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by PonderosaPKParser.
   */
    virtual std::any visitPonderosa_pk(PonderosaPKParser::Ponderosa_pkContext *context) = 0;

    virtual std::any visitPeak_list_2d(PonderosaPKParser::Peak_list_2dContext *context) = 0;

    virtual std::any visitPeak_2d(PonderosaPKParser::Peak_2dContext *context) = 0;

    virtual std::any visitPeak_list_3d(PonderosaPKParser::Peak_list_3dContext *context) = 0;

    virtual std::any visitPeak_3d(PonderosaPKParser::Peak_3dContext *context) = 0;

    virtual std::any visitPeak_list_4d(PonderosaPKParser::Peak_list_4dContext *context) = 0;

    virtual std::any visitPeak_4d(PonderosaPKParser::Peak_4dContext *context) = 0;

    virtual std::any visitNumber(PonderosaPKParser::NumberContext *context) = 0;


};

