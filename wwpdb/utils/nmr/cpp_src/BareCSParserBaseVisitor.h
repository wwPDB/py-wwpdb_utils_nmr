
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BareCSParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "BareCSParserVisitor.h"


/**
 * This class provides an empty implementation of BareCSParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  BareCSParserBaseVisitor : public BareCSParserVisitor {
public:

  virtual std::any visitBare_cs(BareCSParser::Bare_csContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCs_row_format(BareCSParser::Cs_row_formatContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitHeader(BareCSParser::HeaderContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCs_row_list(BareCSParser::Cs_row_listContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAny(BareCSParser::AnyContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitColumn_name(BareCSParser::Column_nameContext *ctx) override {
    return visitChildren(ctx);
  }


};

