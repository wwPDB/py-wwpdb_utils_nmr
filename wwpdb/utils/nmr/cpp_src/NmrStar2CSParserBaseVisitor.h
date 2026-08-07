
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrStar2CSParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "NmrStar2CSParserVisitor.h"


/**
 * This class provides an empty implementation of NmrStar2CSParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  NmrStar2CSParserBaseVisitor : public NmrStar2CSParserVisitor {
public:

  virtual std::any visitNmrstar2_cs(NmrStar2CSParser::Nmrstar2_csContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSeq_loop(NmrStar2CSParser::Seq_loopContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSeq_tags(NmrStar2CSParser::Seq_tagsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSeq_data(NmrStar2CSParser::Seq_dataContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCs_loop(NmrStar2CSParser::Cs_loopContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCs_tags(NmrStar2CSParser::Cs_tagsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCs_data(NmrStar2CSParser::Cs_dataContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAny(NmrStar2CSParser::AnyContext *ctx) override {
    return visitChildren(ctx);
  }


};

