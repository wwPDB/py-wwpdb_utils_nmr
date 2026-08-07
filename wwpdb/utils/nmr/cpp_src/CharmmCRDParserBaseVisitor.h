
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CharmmCRDParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "CharmmCRDParserVisitor.h"


/**
 * This class provides an empty implementation of CharmmCRDParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  CharmmCRDParserBaseVisitor : public CharmmCRDParserVisitor {
public:

  virtual std::any visitCharmm_crd(CharmmCRDParser::Charmm_crdContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComment(CharmmCRDParser::CommentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCoordinates(CharmmCRDParser::CoordinatesContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAtom_coordinate(CharmmCRDParser::Atom_coordinateContext *ctx) override {
    return visitChildren(ctx);
  }


};

