
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "NmrViewCSParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by NmrViewCSParser.
 */
class  NmrViewCSParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by NmrViewCSParser.
   */
    virtual std::any visitNmrview_cs(NmrViewCSParser::Nmrview_csContext *context) = 0;

    virtual std::any visitRes_def_list(NmrViewCSParser::Res_def_listContext *context) = 0;

    virtual std::any visitRes_id_def(NmrViewCSParser::Res_id_defContext *context) = 0;

    virtual std::any visitRes_type_def(NmrViewCSParser::Res_type_defContext *context) = 0;

    virtual std::any visitPrev_type_def(NmrViewCSParser::Prev_type_defContext *context) = 0;

    virtual std::any visitSpin_system_def(NmrViewCSParser::Spin_system_defContext *context) = 0;

    virtual std::any visitHeterogeneity_def(NmrViewCSParser::Heterogeneity_defContext *context) = 0;

    virtual std::any visitShift_list(NmrViewCSParser::Shift_listContext *context) = 0;


};

