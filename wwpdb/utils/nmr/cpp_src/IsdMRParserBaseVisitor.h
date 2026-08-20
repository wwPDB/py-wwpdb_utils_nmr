
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/IsdMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "IsdMRParserVisitor.h"


/**
 * This class provides an empty implementation of IsdMRParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  IsdMRParserBaseVisitor : public IsdMRParserVisitor {
public:

  virtual std::any visitIsd_mr(IsdMRParser::Isd_mrContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_restraints(IsdMRParser::Distance_restraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_restraint(IsdMRParser::Distance_restraintContext *ctx) override {
    return visitChildren(ctx);
  }


};

