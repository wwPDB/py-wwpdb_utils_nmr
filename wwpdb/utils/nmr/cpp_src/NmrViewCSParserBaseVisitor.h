
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "NmrViewCSParserVisitor.h"


/**
 * This class provides an empty implementation of NmrViewCSParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  NmrViewCSParserBaseVisitor : public NmrViewCSParserVisitor {
public:

  virtual std::any visitNmrview_cs(NmrViewCSParser::Nmrview_csContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRes_def_list(NmrViewCSParser::Res_def_listContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRes_id_def(NmrViewCSParser::Res_id_defContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRes_type_def(NmrViewCSParser::Res_type_defContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPrev_type_def(NmrViewCSParser::Prev_type_defContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSpin_system_def(NmrViewCSParser::Spin_system_defContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitHeterogeneity_def(NmrViewCSParser::Heterogeneity_defContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitShift_list(NmrViewCSParser::Shift_listContext *ctx) override {
    return visitChildren(ctx);
  }


};

