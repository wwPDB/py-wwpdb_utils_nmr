
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BarePDBParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "BarePDBParserVisitor.h"


/**
 * This class provides an empty implementation of BarePDBParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  BarePDBParserBaseVisitor : public BarePDBParserVisitor {
public:

  virtual std::any visitBare_pdb(BarePDBParser::Bare_pdbContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComment(BarePDBParser::CommentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCoordinates(BarePDBParser::CoordinatesContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAtom_coordinate(BarePDBParser::Atom_coordinateContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAtom_num(BarePDBParser::Atom_numContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAtom_name(BarePDBParser::Atom_nameContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitXyz(BarePDBParser::XyzContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitX_yz(BarePDBParser::X_yzContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitXy_z(BarePDBParser::Xy_zContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitX_y_z(BarePDBParser::X_y_zContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitUndefined(BarePDBParser::UndefinedContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(BarePDBParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTerminal(BarePDBParser::TerminalContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitEnd(BarePDBParser::EndContext *ctx) override {
    return visitChildren(ctx);
  }


};

