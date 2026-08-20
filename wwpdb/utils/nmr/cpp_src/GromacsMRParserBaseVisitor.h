
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GromacsMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "GromacsMRParserVisitor.h"


/**
 * This class provides an empty implementation of GromacsMRParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  GromacsMRParserBaseVisitor : public GromacsMRParserVisitor {
public:

  virtual std::any visitGromacs_mr(GromacsMRParser::Gromacs_mrContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_restraints(GromacsMRParser::Distance_restraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_restraint(GromacsMRParser::Distance_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDihedral_restraints(GromacsMRParser::Dihedral_restraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDihedral_restraint(GromacsMRParser::Dihedral_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitOrientation_restraints(GromacsMRParser::Orientation_restraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitOrientation_restraint(GromacsMRParser::Orientation_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAngle_restraints(GromacsMRParser::Angle_restraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAngle_restraint(GromacsMRParser::Angle_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAngle_restraints_z(GromacsMRParser::Angle_restraints_zContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAngle_restraint_z(GromacsMRParser::Angle_restraint_zContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPosition_restraints(GromacsMRParser::Position_restraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPosition_restraint(GromacsMRParser::Position_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(GromacsMRParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }


};

