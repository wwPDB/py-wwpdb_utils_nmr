
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CharmmCRDParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "CharmmCRDParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by CharmmCRDParser.
 */
class  CharmmCRDParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by CharmmCRDParser.
   */
    virtual std::any visitCharmm_crd(CharmmCRDParser::Charmm_crdContext *context) = 0;

    virtual std::any visitComment(CharmmCRDParser::CommentContext *context) = 0;

    virtual std::any visitCoordinates(CharmmCRDParser::CoordinatesContext *context) = 0;

    virtual std::any visitAtom_coordinate(CharmmCRDParser::Atom_coordinateContext *context) = 0;


};

