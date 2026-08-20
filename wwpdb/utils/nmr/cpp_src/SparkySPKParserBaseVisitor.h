
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkySPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "SparkySPKParserVisitor.h"


/**
 * This class provides an empty implementation of SparkySPKParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  SparkySPKParserBaseVisitor : public SparkySPKParserVisitor {
public:

  virtual std::any visitSparky_spk(SparkySPKParser::Sparky_spkContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitUser_block(SparkySPKParser::User_blockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitUser_statement(SparkySPKParser::User_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSpectrum_block(SparkySPKParser::Spectrum_blockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSpectrum_statement(SparkySPKParser::Spectrum_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSpectrum_name(SparkySPKParser::Spectrum_nameContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAttached_data(SparkySPKParser::Attached_dataContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAttached_data_statement(SparkySPKParser::Attached_data_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitView(SparkySPKParser::ViewContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitView_statement(SparkySPKParser::View_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitView_name(SparkySPKParser::View_nameContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitView_number(SparkySPKParser::View_numberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitParams(SparkySPKParser::ParamsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitParams_statement(SparkySPKParser::Params_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitOrnament(SparkySPKParser::OrnamentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitOrnament_statement(SparkySPKParser::Ornament_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitOrnament_position(SparkySPKParser::Ornament_positionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLabel(SparkySPKParser::LabelContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLabel_statement(SparkySPKParser::Label_statementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLabel_position(SparkySPKParser::Label_positionContext *ctx) override {
    return visitChildren(ctx);
  }


};

