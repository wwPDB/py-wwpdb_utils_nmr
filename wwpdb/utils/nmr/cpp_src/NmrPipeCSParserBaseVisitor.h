
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrPipeCSParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "NmrPipeCSParserVisitor.h"


/**
 * This class provides an empty implementation of NmrPipeCSParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  NmrPipeCSParserBaseVisitor : public NmrPipeCSParserVisitor {
public:

  virtual std::any visitNmrpipe_cs(NmrPipeCSParser::Nmrpipe_csContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSequence(NmrPipeCSParser::SequenceContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChemical_shifts(NmrPipeCSParser::Chemical_shiftsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChemical_shift(NmrPipeCSParser::Chemical_shiftContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChemical_shifts_sw_segid(NmrPipeCSParser::Chemical_shifts_sw_segidContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChemical_shift_sw_segid(NmrPipeCSParser::Chemical_shift_sw_segidContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChemical_shifts_ew_segid(NmrPipeCSParser::Chemical_shifts_ew_segidContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChemical_shift_ew_segid(NmrPipeCSParser::Chemical_shift_ew_segidContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(NmrPipeCSParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }


};

