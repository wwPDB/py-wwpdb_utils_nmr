
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaNOAParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "CyanaNOAParserVisitor.h"


/**
 * This class provides an empty implementation of CyanaNOAParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  CyanaNOAParserBaseVisitor : public CyanaNOAParserVisitor {
public:

  virtual std::any visitCyana_noa(CyanaNOAParser::Cyana_noaContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComment(CyanaNOAParser::CommentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNoe_peaks(CyanaNOAParser::Noe_peaksContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_header(CyanaNOAParser::Peak_headerContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_quality(CyanaNOAParser::Peak_qualityContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNoe_assignments(CyanaNOAParser::Noe_assignmentsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNoe_assignment(CyanaNOAParser::Noe_assignmentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumerical_report(CyanaNOAParser::Numerical_reportContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExtended_report(CyanaNOAParser::Extended_reportContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNoe_stat(CyanaNOAParser::Noe_statContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitList_of_proton(CyanaNOAParser::List_of_protonContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_stat(CyanaNOAParser::Peak_statContext *ctx) override {
    return visitChildren(ctx);
  }


};

