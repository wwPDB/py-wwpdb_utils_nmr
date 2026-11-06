
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/DianaCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "DianaCSParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by DianaCSParser.
 */
class  DianaCSParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by DianaCSParser.
   */
    virtual std::any visitDiana_cs(DianaCSParser::Diana_csContext *context) = 0;

    virtual std::any visitComment(DianaCSParser::CommentContext *context) = 0;

    virtual std::any visitChemical_shifts(DianaCSParser::Chemical_shiftsContext *context) = 0;

    virtual std::any visitChemical_shift(DianaCSParser::Chemical_shiftContext *context) = 0;

    virtual std::any visitAtom_chemical_shift(DianaCSParser::Atom_chemical_shiftContext *context) = 0;


};

