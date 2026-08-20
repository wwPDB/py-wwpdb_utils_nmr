
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BarePDBParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "BarePDBParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by BarePDBParser.
 */
class  BarePDBParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by BarePDBParser.
   */
    virtual std::any visitBare_pdb(BarePDBParser::Bare_pdbContext *context) = 0;

    virtual std::any visitComment(BarePDBParser::CommentContext *context) = 0;

    virtual std::any visitCoordinates(BarePDBParser::CoordinatesContext *context) = 0;

    virtual std::any visitAtom_coordinate(BarePDBParser::Atom_coordinateContext *context) = 0;

    virtual std::any visitAtom_num(BarePDBParser::Atom_numContext *context) = 0;

    virtual std::any visitAtom_name(BarePDBParser::Atom_nameContext *context) = 0;

    virtual std::any visitXyz(BarePDBParser::XyzContext *context) = 0;

    virtual std::any visitX_yz(BarePDBParser::X_yzContext *context) = 0;

    virtual std::any visitXy_z(BarePDBParser::Xy_zContext *context) = 0;

    virtual std::any visitX_y_z(BarePDBParser::X_y_zContext *context) = 0;

    virtual std::any visitUndefined(BarePDBParser::UndefinedContext *context) = 0;

    virtual std::any visitNumber(BarePDBParser::NumberContext *context) = 0;

    virtual std::any visitTerminal(BarePDBParser::TerminalContext *context) = 0;

    virtual std::any visitEnd(BarePDBParser::EndContext *context) = 0;


};

