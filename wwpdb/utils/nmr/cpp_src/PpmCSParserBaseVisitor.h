
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PpmCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "PpmCSParserVisitor.h"


/**
 * This class provides an empty implementation of PpmCSParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  PpmCSParserBaseVisitor : public PpmCSParserVisitor {
public:

  virtual std::any visitPpm_cs(PpmCSParser::Ppm_csContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPpm_list(PpmCSParser::Ppm_listContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(PpmCSParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }


};

