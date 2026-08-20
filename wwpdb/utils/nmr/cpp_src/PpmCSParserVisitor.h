
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PpmCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "PpmCSParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by PpmCSParser.
 */
class  PpmCSParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by PpmCSParser.
   */
    virtual std::any visitPpm_cs(PpmCSParser::Ppm_csContext *context) = 0;

    virtual std::any visitPpm_list(PpmCSParser::Ppm_listContext *context) = 0;

    virtual std::any visitNumber(PpmCSParser::NumberContext *context) = 0;


};

