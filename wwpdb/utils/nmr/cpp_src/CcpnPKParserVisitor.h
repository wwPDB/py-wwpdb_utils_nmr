
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CcpnPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "CcpnPKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by CcpnPKParser.
 */
class  CcpnPKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by CcpnPKParser.
   */
    virtual std::any visitCcpn_pk(CcpnPKParser::Ccpn_pkContext *context) = 0;

    virtual std::any visitPeak_list_2d(CcpnPKParser::Peak_list_2dContext *context) = 0;

    virtual std::any visitPeak_2d(CcpnPKParser::Peak_2dContext *context) = 0;

    virtual std::any visitPeak_list_3d(CcpnPKParser::Peak_list_3dContext *context) = 0;

    virtual std::any visitPeak_3d(CcpnPKParser::Peak_3dContext *context) = 0;

    virtual std::any visitPeak_list_4d(CcpnPKParser::Peak_list_4dContext *context) = 0;

    virtual std::any visitPeak_4d(CcpnPKParser::Peak_4dContext *context) = 0;

    virtual std::any visitPeak_list_wo_assign_2d(CcpnPKParser::Peak_list_wo_assign_2dContext *context) = 0;

    virtual std::any visitPeak_wo_assign_2d(CcpnPKParser::Peak_wo_assign_2dContext *context) = 0;

    virtual std::any visitPeak_list_wo_assign_3d(CcpnPKParser::Peak_list_wo_assign_3dContext *context) = 0;

    virtual std::any visitPeak_wo_assign_3d(CcpnPKParser::Peak_wo_assign_3dContext *context) = 0;

    virtual std::any visitPeak_list_wo_assign_4d(CcpnPKParser::Peak_list_wo_assign_4dContext *context) = 0;

    virtual std::any visitPeak_wo_assign_4d(CcpnPKParser::Peak_wo_assign_4dContext *context) = 0;

    virtual std::any visitPosition(CcpnPKParser::PositionContext *context) = 0;

    virtual std::any visitNumber(CcpnPKParser::NumberContext *context) = 0;

    virtual std::any visitNote(CcpnPKParser::NoteContext *context) = 0;


};

