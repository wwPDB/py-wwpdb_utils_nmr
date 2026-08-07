
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PonderosaPKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "PonderosaPKParserVisitor.h"


/**
 * This class provides an empty implementation of PonderosaPKParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  PonderosaPKParserBaseVisitor : public PonderosaPKParserVisitor {
public:

  virtual std::any visitPonderosa_pk(PonderosaPKParser::Ponderosa_pkContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_2d(PonderosaPKParser::Peak_list_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_2d(PonderosaPKParser::Peak_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_3d(PonderosaPKParser::Peak_list_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_3d(PonderosaPKParser::Peak_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_4d(PonderosaPKParser::Peak_list_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_4d(PonderosaPKParser::Peak_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(PonderosaPKParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }


};

