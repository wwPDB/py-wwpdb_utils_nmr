
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BareMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "BareMRParserVisitor.h"


/**
 * This class provides an empty implementation of BareMRParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  BareMRParserBaseVisitor : public BareMRParserVisitor {
public:

  virtual std::any visitBare_mr(BareMRParser::Bare_mrContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitMr_row_format(BareMRParser::Mr_row_formatContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitHeader(BareMRParser::HeaderContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitMr_row_list(BareMRParser::Mr_row_listContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAny(BareMRParser::AnyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitColumn_name(BareMRParser::Column_nameContext *ctx) override {
    return visitChildren(ctx);
  }


};

