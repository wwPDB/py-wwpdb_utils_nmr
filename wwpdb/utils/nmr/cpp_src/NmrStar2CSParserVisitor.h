
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrStar2CSParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "NmrStar2CSParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by NmrStar2CSParser.
 */
class  NmrStar2CSParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by NmrStar2CSParser.
   */
    virtual std::any visitNmrstar2_cs(NmrStar2CSParser::Nmrstar2_csContext *context) = 0;

    virtual std::any visitSeq_loop(NmrStar2CSParser::Seq_loopContext *context) = 0;

    virtual std::any visitSeq_tags(NmrStar2CSParser::Seq_tagsContext *context) = 0;

    virtual std::any visitSeq_data(NmrStar2CSParser::Seq_dataContext *context) = 0;

    virtual std::any visitCs_loop(NmrStar2CSParser::Cs_loopContext *context) = 0;

    virtual std::any visitCs_tags(NmrStar2CSParser::Cs_tagsContext *context) = 0;

    virtual std::any visitCs_data(NmrStar2CSParser::Cs_dataContext *context) = 0;

    virtual std::any visitAny(NmrStar2CSParser::AnyContext *context) = 0;


};

