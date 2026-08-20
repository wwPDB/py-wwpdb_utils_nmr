
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XeasyPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "XeasyPKParserVisitor.h"


/**
 * This class provides an empty implementation of XeasyPKParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  XeasyPKParserBaseVisitor : public XeasyPKParserVisitor {
public:

  virtual std::any visitXeasy_pk(XeasyPKParser::Xeasy_pkContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDimension(XeasyPKParser::DimensionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak(XeasyPKParser::PeakContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFormat(XeasyPKParser::FormatContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitIname(XeasyPKParser::InameContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCyana_format(XeasyPKParser::Cyana_formatContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSpectrum(XeasyPKParser::SpectrumContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTolerance(XeasyPKParser::ToleranceContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_2d(XeasyPKParser::Peak_list_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_2d(XeasyPKParser::Peak_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_3d(XeasyPKParser::Peak_list_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_3d(XeasyPKParser::Peak_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_4d(XeasyPKParser::Peak_list_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_4d(XeasyPKParser::Peak_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPosition(XeasyPKParser::PositionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(XeasyPKParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitType_code(XeasyPKParser::Type_codeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAssign(XeasyPKParser::AssignContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComment(XeasyPKParser::CommentContext *ctx) override {
    return visitChildren(ctx);
  }


};

