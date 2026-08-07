
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/VnmrPKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "VnmrPKParserVisitor.h"


/**
 * This class provides an empty implementation of VnmrPKParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  VnmrPKParserBaseVisitor : public VnmrPKParserVisitor {
public:

  virtual std::any visitVnmr_pk(VnmrPKParser::Vnmr_pkContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComment(VnmrPKParser::CommentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFormat(VnmrPKParser::FormatContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_ll2d(VnmrPKParser::Peak_ll2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_ll3d(VnmrPKParser::Peak_ll3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_ll4d(VnmrPKParser::Peak_ll4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitData_label(VnmrPKParser::Data_labelContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_2d(VnmrPKParser::Peak_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_3d(VnmrPKParser::Peak_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_4d(VnmrPKParser::Peak_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(VnmrPKParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }


};

