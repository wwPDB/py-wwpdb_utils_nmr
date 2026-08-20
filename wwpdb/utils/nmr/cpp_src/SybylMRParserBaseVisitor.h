
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SybylMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "SybylMRParserVisitor.h"


/**
 * This class provides an empty implementation of SybylMRParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  SybylMRParserBaseVisitor : public SybylMRParserVisitor {
public:

  virtual std::any visitSybyl_mr(SybylMRParser::Sybyl_mrContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_restraints(SybylMRParser::Distance_restraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_restraint(SybylMRParser::Distance_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(SybylMRParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }


};

