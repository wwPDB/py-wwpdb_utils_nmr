
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AriaMRParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "AriaMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by AriaMRParser.
 */
class  AriaMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by AriaMRParser.
   */
    virtual std::any visitAria_mr(AriaMRParser::Aria_mrContext *context) = 0;

    virtual std::any visitDistance_restraints(AriaMRParser::Distance_restraintsContext *context) = 0;

    virtual std::any visitDistance_restraint(AriaMRParser::Distance_restraintContext *context) = 0;

    virtual std::any visitContribution(AriaMRParser::ContributionContext *context) = 0;

    virtual std::any visitAtom_pair(AriaMRParser::Atom_pairContext *context) = 0;

    virtual std::any visitAtom_selection(AriaMRParser::Atom_selectionContext *context) = 0;

    virtual std::any visitOld_distance_restraints(AriaMRParser::Old_distance_restraintsContext *context) = 0;

    virtual std::any visitOld_distance_restraint(AriaMRParser::Old_distance_restraintContext *context) = 0;

    virtual std::any visitP_row(AriaMRParser::P_rowContext *context) = 0;

    virtual std::any visitA_row(AriaMRParser::A_rowContext *context) = 0;

    virtual std::any visitC_row(AriaMRParser::C_rowContext *context) = 0;

    virtual std::any visitNumber(AriaMRParser::NumberContext *context) = 0;

    virtual std::any visitNumber_c(AriaMRParser::Number_cContext *context) = 0;


};

