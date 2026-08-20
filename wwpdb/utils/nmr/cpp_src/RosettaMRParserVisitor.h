
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/RosettaMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "RosettaMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by RosettaMRParser.
 */
class  RosettaMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by RosettaMRParser.
   */
    virtual std::any visitRosetta_mr(RosettaMRParser::Rosetta_mrContext *context) = 0;

    virtual std::any visitComment(RosettaMRParser::CommentContext *context) = 0;

    virtual std::any visitAtom_pair_restraints(RosettaMRParser::Atom_pair_restraintsContext *context) = 0;

    virtual std::any visitAtom_pair_restraint(RosettaMRParser::Atom_pair_restraintContext *context) = 0;

    virtual std::any visitAngle_restraints(RosettaMRParser::Angle_restraintsContext *context) = 0;

    virtual std::any visitAngle_restraint(RosettaMRParser::Angle_restraintContext *context) = 0;

    virtual std::any visitDihedral_restraints(RosettaMRParser::Dihedral_restraintsContext *context) = 0;

    virtual std::any visitDihedral_restraint(RosettaMRParser::Dihedral_restraintContext *context) = 0;

    virtual std::any visitDihedral_pair_restraints(RosettaMRParser::Dihedral_pair_restraintsContext *context) = 0;

    virtual std::any visitDihedral_pair_restraint(RosettaMRParser::Dihedral_pair_restraintContext *context) = 0;

    virtual std::any visitCoordinate_restraints(RosettaMRParser::Coordinate_restraintsContext *context) = 0;

    virtual std::any visitCoordinate_restraint(RosettaMRParser::Coordinate_restraintContext *context) = 0;

    virtual std::any visitLocal_coordinate_restraints(RosettaMRParser::Local_coordinate_restraintsContext *context) = 0;

    virtual std::any visitLocal_coordinate_restraint(RosettaMRParser::Local_coordinate_restraintContext *context) = 0;

    virtual std::any visitSite_restraints(RosettaMRParser::Site_restraintsContext *context) = 0;

    virtual std::any visitSite_restraint(RosettaMRParser::Site_restraintContext *context) = 0;

    virtual std::any visitSite_residues_restraints(RosettaMRParser::Site_residues_restraintsContext *context) = 0;

    virtual std::any visitSite_residues_restraint(RosettaMRParser::Site_residues_restraintContext *context) = 0;

    virtual std::any visitMin_residue_atomic_distance_restraints(RosettaMRParser::Min_residue_atomic_distance_restraintsContext *context) = 0;

    virtual std::any visitMin_residue_atomic_distance_restraint(RosettaMRParser::Min_residue_atomic_distance_restraintContext *context) = 0;

    virtual std::any visitBig_bin_restraints(RosettaMRParser::Big_bin_restraintsContext *context) = 0;

    virtual std::any visitBig_bin_restraint(RosettaMRParser::Big_bin_restraintContext *context) = 0;

    virtual std::any visitNested_restraints(RosettaMRParser::Nested_restraintsContext *context) = 0;

    virtual std::any visitNested_restraint(RosettaMRParser::Nested_restraintContext *context) = 0;

    virtual std::any visitAny_restraint(RosettaMRParser::Any_restraintContext *context) = 0;

    virtual std::any visitFunc_type_def(RosettaMRParser::Func_type_defContext *context) = 0;

    virtual std::any visitRdc_restraints(RosettaMRParser::Rdc_restraintsContext *context) = 0;

    virtual std::any visitRdc_restraint(RosettaMRParser::Rdc_restraintContext *context) = 0;

    virtual std::any visitDisulfide_bond_linkages(RosettaMRParser::Disulfide_bond_linkagesContext *context) = 0;

    virtual std::any visitDisulfide_bond_linkage(RosettaMRParser::Disulfide_bond_linkageContext *context) = 0;

    virtual std::any visitAtom_pair_w_chain_restraints(RosettaMRParser::Atom_pair_w_chain_restraintsContext *context) = 0;

    virtual std::any visitAtom_pair_w_chain_restraint(RosettaMRParser::Atom_pair_w_chain_restraintContext *context) = 0;

    virtual std::any visitNumber(RosettaMRParser::NumberContext *context) = 0;

    virtual std::any visitNumber_f(RosettaMRParser::Number_fContext *context) = 0;

    virtual std::any visitGen_res_num(RosettaMRParser::Gen_res_numContext *context) = 0;

    virtual std::any visitGen_simple_name(RosettaMRParser::Gen_simple_nameContext *context) = 0;


};

