
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XwinNmrPKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "XwinNmrPKParserVisitor.h"


/**
 * This class provides an empty implementation of XwinNmrPKParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  XwinNmrPKParserBaseVisitor : public XwinNmrPKParserVisitor {
public:

  virtual std::any visitXwinnmr_pk(XwinNmrPKParser::Xwinnmr_pkContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComment(XwinNmrPKParser::CommentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDimension(XwinNmrPKParser::DimensionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_2d(XwinNmrPKParser::Peak_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_3d(XwinNmrPKParser::Peak_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_4d(XwinNmrPKParser::Peak_4dContext *ctx) override {
    return visitChildren(ctx);
  }


};

