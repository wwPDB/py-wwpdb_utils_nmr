
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CcpnPKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "CcpnPKParserVisitor.h"


/**
 * This class provides an empty implementation of CcpnPKParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  CcpnPKParserBaseVisitor : public CcpnPKParserVisitor {
public:

  virtual std::any visitCcpn_pk(CcpnPKParser::Ccpn_pkContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_2d(CcpnPKParser::Peak_list_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_2d(CcpnPKParser::Peak_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_3d(CcpnPKParser::Peak_list_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_3d(CcpnPKParser::Peak_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_4d(CcpnPKParser::Peak_list_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_4d(CcpnPKParser::Peak_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_wo_assign_2d(CcpnPKParser::Peak_list_wo_assign_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_wo_assign_2d(CcpnPKParser::Peak_wo_assign_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_wo_assign_3d(CcpnPKParser::Peak_list_wo_assign_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_wo_assign_3d(CcpnPKParser::Peak_wo_assign_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_list_wo_assign_4d(CcpnPKParser::Peak_list_wo_assign_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_wo_assign_4d(CcpnPKParser::Peak_wo_assign_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPosition(CcpnPKParser::PositionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(CcpnPKParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNote(CcpnPKParser::NoteContext *ctx) override {
    return visitChildren(ctx);
  }


};

