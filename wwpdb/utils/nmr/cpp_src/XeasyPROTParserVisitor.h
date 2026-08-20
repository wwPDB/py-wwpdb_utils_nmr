
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XeasyPROTParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "XeasyPROTParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by XeasyPROTParser.
 */
class  XeasyPROTParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by XeasyPROTParser.
   */
    virtual std::any visitXeasy_prot(XeasyPROTParser::Xeasy_protContext *context) = 0;

    virtual std::any visitProt(XeasyPROTParser::ProtContext *context) = 0;

    virtual std::any visitResidue(XeasyPROTParser::ResidueContext *context) = 0;


};

