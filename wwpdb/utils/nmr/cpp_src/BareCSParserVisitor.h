
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BareCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "BareCSParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by BareCSParser.
 */
class  BareCSParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by BareCSParser.
   */
    virtual std::any visitBare_cs(BareCSParser::Bare_csContext *context) = 0;

    virtual std::any visitCs_row_format(BareCSParser::Cs_row_formatContext *context) = 0;

    virtual std::any visitHeader(BareCSParser::HeaderContext *context) = 0;

    virtual std::any visitCs_row_list(BareCSParser::Cs_row_listContext *context) = 0;

    virtual std::any visitAny(BareCSParser::AnyContext *context) = 0;

    virtual std::any visitColumn_name(BareCSParser::Column_nameContext *context) = 0;


};

