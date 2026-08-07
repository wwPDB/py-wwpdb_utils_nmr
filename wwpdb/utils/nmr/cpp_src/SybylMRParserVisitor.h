
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SybylMRParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "SybylMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by SybylMRParser.
 */
class  SybylMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by SybylMRParser.
   */
    virtual std::any visitSybyl_mr(SybylMRParser::Sybyl_mrContext *context) = 0;

    virtual std::any visitDistance_restraints(SybylMRParser::Distance_restraintsContext *context) = 0;

    virtual std::any visitDistance_restraint(SybylMRParser::Distance_restraintContext *context) = 0;

    virtual std::any visitNumber(SybylMRParser::NumberContext *context) = 0;


};

