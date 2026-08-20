
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XeasyPROTParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "XeasyPROTParserVisitor.h"


/**
 * This class provides an empty implementation of XeasyPROTParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  XeasyPROTParserBaseVisitor : public XeasyPROTParserVisitor {
public:

  virtual std::any visitXeasy_prot(XeasyPROTParser::Xeasy_protContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitProt(XeasyPROTParser::ProtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitResidue(XeasyPROTParser::ResidueContext *ctx) override {
    return visitChildren(ctx);
  }


};

