
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BareMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "BareMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by BareMRParser.
 */
class  BareMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by BareMRParser.
   */
    virtual std::any visitBare_mr(BareMRParser::Bare_mrContext *context) = 0;

    virtual std::any visitMr_row_format(BareMRParser::Mr_row_formatContext *context) = 0;

    virtual std::any visitHeader(BareMRParser::HeaderContext *context) = 0;

    virtual std::any visitMr_row_list(BareMRParser::Mr_row_listContext *context) = 0;

    virtual std::any visitAny(BareMRParser::AnyContext *context) = 0;

    virtual std::any visitColumn_name(BareMRParser::Column_nameContext *context) = 0;


};

