
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaNOAParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "CyanaNOAParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by CyanaNOAParser.
 */
class  CyanaNOAParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by CyanaNOAParser.
   */
    virtual std::any visitCyana_noa(CyanaNOAParser::Cyana_noaContext *context) = 0;

    virtual std::any visitComment(CyanaNOAParser::CommentContext *context) = 0;

    virtual std::any visitNoe_peaks(CyanaNOAParser::Noe_peaksContext *context) = 0;

    virtual std::any visitPeak_header(CyanaNOAParser::Peak_headerContext *context) = 0;

    virtual std::any visitPeak_quality(CyanaNOAParser::Peak_qualityContext *context) = 0;

    virtual std::any visitNoe_assignments(CyanaNOAParser::Noe_assignmentsContext *context) = 0;

    virtual std::any visitNoe_assignment(CyanaNOAParser::Noe_assignmentContext *context) = 0;

    virtual std::any visitNumerical_report(CyanaNOAParser::Numerical_reportContext *context) = 0;

    virtual std::any visitExtended_report(CyanaNOAParser::Extended_reportContext *context) = 0;

    virtual std::any visitNoe_stat(CyanaNOAParser::Noe_statContext *context) = 0;

    virtual std::any visitList_of_proton(CyanaNOAParser::List_of_protonContext *context) = 0;

    virtual std::any visitPeak_stat(CyanaNOAParser::Peak_statContext *context) = 0;


};

