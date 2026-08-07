
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/OliviaCSParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "OliviaCSParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by OliviaCSParser.
 */
class  OliviaCSParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by OliviaCSParser.
   */
    virtual std::any visitOlivia_cs(OliviaCSParser::Olivia_csContext *context) = 0;

    virtual std::any visitSequence(OliviaCSParser::SequenceContext *context) = 0;

    virtual std::any visitResidue(OliviaCSParser::ResidueContext *context) = 0;

    virtual std::any visitChemical_shifts(OliviaCSParser::Chemical_shiftsContext *context) = 0;

    virtual std::any visitChemical_shift(OliviaCSParser::Chemical_shiftContext *context) = 0;

    virtual std::any visitNumber(OliviaCSParser::NumberContext *context) = 0;

    virtual std::any visitComment(OliviaCSParser::CommentContext *context) = 0;


};

