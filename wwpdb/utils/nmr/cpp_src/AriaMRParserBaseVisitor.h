
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AriaMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "AriaMRParserVisitor.h"


/**
 * This class provides an empty implementation of AriaMRParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  AriaMRParserBaseVisitor : public AriaMRParserVisitor {
public:

  virtual std::any visitAria_mr(AriaMRParser::Aria_mrContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_restraints(AriaMRParser::Distance_restraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_restraint(AriaMRParser::Distance_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitContribution(AriaMRParser::ContributionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAtom_pair(AriaMRParser::Atom_pairContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAtom_selection(AriaMRParser::Atom_selectionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitOld_distance_restraints(AriaMRParser::Old_distance_restraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitOld_distance_restraint(AriaMRParser::Old_distance_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitP_row(AriaMRParser::P_rowContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitA_row(AriaMRParser::A_rowContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitC_row(AriaMRParser::C_rowContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(AriaMRParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber_c(AriaMRParser::Number_cContext *ctx) override {
    return visitChildren(ctx);
  }


};

