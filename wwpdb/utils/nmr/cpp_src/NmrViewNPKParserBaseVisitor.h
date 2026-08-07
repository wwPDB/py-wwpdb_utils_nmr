
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewNPKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "NmrViewNPKParserVisitor.h"


/**
 * This class provides an empty implementation of NmrViewNPKParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  NmrViewNPKParserBaseVisitor : public NmrViewNPKParserVisitor {
public:

  virtual std::any visitNmrview_npk(NmrViewNPKParser::Nmrview_npkContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitData_label(NmrViewNPKParser::Data_labelContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLabels(NmrViewNPKParser::LabelsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_2d(NmrViewNPKParser::Peak_list_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_2d(NmrViewNPKParser::Peak_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_3d(NmrViewNPKParser::Peak_list_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_3d(NmrViewNPKParser::Peak_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_4d(NmrViewNPKParser::Peak_list_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_4d(NmrViewNPKParser::Peak_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_wo_eju_2d(NmrViewNPKParser::Peak_list_wo_eju_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_wo_eju_2d(NmrViewNPKParser::Peak_wo_eju_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_wo_eju_3d(NmrViewNPKParser::Peak_list_wo_eju_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_wo_eju_3d(NmrViewNPKParser::Peak_wo_eju_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_wo_eju_4d(NmrViewNPKParser::Peak_list_wo_eju_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_wo_eju_4d(NmrViewNPKParser::Peak_wo_eju_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLabel(NmrViewNPKParser::LabelContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitJcoupling(NmrViewNPKParser::JcouplingContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(NmrViewNPKParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }


};

