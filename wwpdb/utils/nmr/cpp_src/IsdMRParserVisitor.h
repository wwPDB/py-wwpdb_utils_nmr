
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/IsdMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "IsdMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by IsdMRParser.
 */
class  IsdMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by IsdMRParser.
   */
    virtual std::any visitIsd_mr(IsdMRParser::Isd_mrContext *context) = 0;

    virtual std::any visitDistance_restraints(IsdMRParser::Distance_restraintsContext *context) = 0;

    virtual std::any visitDistance_restraint(IsdMRParser::Distance_restraintContext *context) = 0;


};

