
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/OliviaCSParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "OliviaCSParserVisitor.h"


/**
 * This class provides an empty implementation of OliviaCSParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  OliviaCSParserBaseVisitor : public OliviaCSParserVisitor {
public:

  virtual std::any visitOlivia_cs(OliviaCSParser::Olivia_csContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSequence(OliviaCSParser::SequenceContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitResidue(OliviaCSParser::ResidueContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChemical_shifts(OliviaCSParser::Chemical_shiftsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChemical_shift(OliviaCSParser::Chemical_shiftContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(OliviaCSParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComment(OliviaCSParser::CommentContext *ctx) override {
    return visitChildren(ctx);
  }


};

