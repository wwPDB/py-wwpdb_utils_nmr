
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrPipeCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "NmrPipeCSParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by NmrPipeCSParser.
 */
class  NmrPipeCSParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by NmrPipeCSParser.
   */
    virtual std::any visitNmrpipe_cs(NmrPipeCSParser::Nmrpipe_csContext *context) = 0;

    virtual std::any visitSequence(NmrPipeCSParser::SequenceContext *context) = 0;

    virtual std::any visitChemical_shifts(NmrPipeCSParser::Chemical_shiftsContext *context) = 0;

    virtual std::any visitChemical_shift(NmrPipeCSParser::Chemical_shiftContext *context) = 0;

    virtual std::any visitChemical_shifts_sw_segid(NmrPipeCSParser::Chemical_shifts_sw_segidContext *context) = 0;

    virtual std::any visitChemical_shift_sw_segid(NmrPipeCSParser::Chemical_shift_sw_segidContext *context) = 0;

    virtual std::any visitChemical_shifts_ew_segid(NmrPipeCSParser::Chemical_shifts_ew_segidContext *context) = 0;

    virtual std::any visitChemical_shift_ew_segid(NmrPipeCSParser::Chemical_shift_ew_segidContext *context) = 0;

    virtual std::any visitNumber(NmrPipeCSParser::NumberContext *context) = 0;


};

