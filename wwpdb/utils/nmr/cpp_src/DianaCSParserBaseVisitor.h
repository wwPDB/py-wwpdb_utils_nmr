
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/DianaCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "DianaCSParserVisitor.h"


/**
 * This class provides an empty implementation of DianaCSParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  DianaCSParserBaseVisitor : public DianaCSParserVisitor {
public:

  virtual std::any visitDiana_cs(DianaCSParser::Diana_csContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComment(DianaCSParser::CommentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChemical_shifts(DianaCSParser::Chemical_shiftsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChemical_shift(DianaCSParser::Chemical_shiftContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAtom_chemical_shift(DianaCSParser::Atom_chemical_shiftContext *ctx) override {
    return visitChildren(ctx);
  }


};

