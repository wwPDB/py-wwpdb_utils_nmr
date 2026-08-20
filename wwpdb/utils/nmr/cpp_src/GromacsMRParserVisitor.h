
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GromacsMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "GromacsMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by GromacsMRParser.
 */
class  GromacsMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by GromacsMRParser.
   */
    virtual std::any visitGromacs_mr(GromacsMRParser::Gromacs_mrContext *context) = 0;

    virtual std::any visitDistance_restraints(GromacsMRParser::Distance_restraintsContext *context) = 0;

    virtual std::any visitDistance_restraint(GromacsMRParser::Distance_restraintContext *context) = 0;

    virtual std::any visitDihedral_restraints(GromacsMRParser::Dihedral_restraintsContext *context) = 0;

    virtual std::any visitDihedral_restraint(GromacsMRParser::Dihedral_restraintContext *context) = 0;

    virtual std::any visitOrientation_restraints(GromacsMRParser::Orientation_restraintsContext *context) = 0;

    virtual std::any visitOrientation_restraint(GromacsMRParser::Orientation_restraintContext *context) = 0;

    virtual std::any visitAngle_restraints(GromacsMRParser::Angle_restraintsContext *context) = 0;

    virtual std::any visitAngle_restraint(GromacsMRParser::Angle_restraintContext *context) = 0;

    virtual std::any visitAngle_restraints_z(GromacsMRParser::Angle_restraints_zContext *context) = 0;

    virtual std::any visitAngle_restraint_z(GromacsMRParser::Angle_restraint_zContext *context) = 0;

    virtual std::any visitPosition_restraints(GromacsMRParser::Position_restraintsContext *context) = 0;

    virtual std::any visitPosition_restraint(GromacsMRParser::Position_restraintContext *context) = 0;

    virtual std::any visitNumber(GromacsMRParser::NumberContext *context) = 0;


};

