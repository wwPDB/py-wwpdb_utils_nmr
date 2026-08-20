
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "NmrViewPKParserVisitor.h"


/**
 * This class provides an empty implementation of NmrViewPKParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  NmrViewPKParserBaseVisitor : public NmrViewPKParserVisitor {
public:

  virtual std::any visitNmrview_pk(NmrViewPKParser::Nmrview_pkContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitData_label(NmrViewPKParser::Data_labelContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLabels(NmrViewPKParser::LabelsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_2d(NmrViewPKParser::Peak_list_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_2d(NmrViewPKParser::Peak_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_3d(NmrViewPKParser::Peak_list_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_3d(NmrViewPKParser::Peak_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_4d(NmrViewPKParser::Peak_list_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_4d(NmrViewPKParser::Peak_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_wo_eju_2d(NmrViewPKParser::Peak_list_wo_eju_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_wo_eju_2d(NmrViewPKParser::Peak_wo_eju_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_wo_eju_3d(NmrViewPKParser::Peak_list_wo_eju_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_wo_eju_3d(NmrViewPKParser::Peak_wo_eju_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_wo_eju_4d(NmrViewPKParser::Peak_list_wo_eju_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_wo_eju_4d(NmrViewPKParser::Peak_wo_eju_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLabel(NmrViewPKParser::LabelContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitJcoupling(NmrViewPKParser::JcouplingContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(NmrViewPKParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitEnclose_data(NmrViewPKParser::Enclose_dataContext *ctx) override {
    return visitChildren(ctx);
  }


};

