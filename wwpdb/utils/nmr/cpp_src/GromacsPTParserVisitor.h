
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GromacsPTParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "GromacsPTParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by GromacsPTParser.
 */
class  GromacsPTParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by GromacsPTParser.
   */
    virtual std::any visitGromacs_pt(GromacsPTParser::Gromacs_ptContext *context) = 0;

    virtual std::any visitDefault_statement(GromacsPTParser::Default_statementContext *context) = 0;

    virtual std::any visitMoleculetype_statement(GromacsPTParser::Moleculetype_statementContext *context) = 0;

    virtual std::any visitMoleculetype(GromacsPTParser::MoleculetypeContext *context) = 0;

    virtual std::any visitAtomtypes_statement(GromacsPTParser::Atomtypes_statementContext *context) = 0;

    virtual std::any visitAtomtypes(GromacsPTParser::AtomtypesContext *context) = 0;

    virtual std::any visitPairtypes_statement(GromacsPTParser::Pairtypes_statementContext *context) = 0;

    virtual std::any visitPairtypes(GromacsPTParser::PairtypesContext *context) = 0;

    virtual std::any visitBondtypes_statement(GromacsPTParser::Bondtypes_statementContext *context) = 0;

    virtual std::any visitBondtypes(GromacsPTParser::BondtypesContext *context) = 0;

    virtual std::any visitAngletypes_statement(GromacsPTParser::Angletypes_statementContext *context) = 0;

    virtual std::any visitAngletypes(GromacsPTParser::AngletypesContext *context) = 0;

    virtual std::any visitDihedraltypes_statement(GromacsPTParser::Dihedraltypes_statementContext *context) = 0;

    virtual std::any visitDihedraltypes(GromacsPTParser::DihedraltypesContext *context) = 0;

    virtual std::any visitConstrainttypes_statement(GromacsPTParser::Constrainttypes_statementContext *context) = 0;

    virtual std::any visitConstrainttypes(GromacsPTParser::ConstrainttypesContext *context) = 0;

    virtual std::any visitNonbonded_params_statement(GromacsPTParser::Nonbonded_params_statementContext *context) = 0;

    virtual std::any visitNonbonded_params(GromacsPTParser::Nonbonded_paramsContext *context) = 0;

    virtual std::any visitAtoms_statement(GromacsPTParser::Atoms_statementContext *context) = 0;

    virtual std::any visitAtoms(GromacsPTParser::AtomsContext *context) = 0;

    virtual std::any visitBonds_statement(GromacsPTParser::Bonds_statementContext *context) = 0;

    virtual std::any visitBonds(GromacsPTParser::BondsContext *context) = 0;

    virtual std::any visitPairs_statement(GromacsPTParser::Pairs_statementContext *context) = 0;

    virtual std::any visitPairs(GromacsPTParser::PairsContext *context) = 0;

    virtual std::any visitPairs_nb_statement(GromacsPTParser::Pairs_nb_statementContext *context) = 0;

    virtual std::any visitPairs_nb(GromacsPTParser::Pairs_nbContext *context) = 0;

    virtual std::any visitAngles_statement(GromacsPTParser::Angles_statementContext *context) = 0;

    virtual std::any visitAngles(GromacsPTParser::AnglesContext *context) = 0;

    virtual std::any visitDihedrals_statement(GromacsPTParser::Dihedrals_statementContext *context) = 0;

    virtual std::any visitDihedrals(GromacsPTParser::DihedralsContext *context) = 0;

    virtual std::any visitExclusions_statement(GromacsPTParser::Exclusions_statementContext *context) = 0;

    virtual std::any visitExclusions(GromacsPTParser::ExclusionsContext *context) = 0;

    virtual std::any visitConstraints_statement(GromacsPTParser::Constraints_statementContext *context) = 0;

    virtual std::any visitConstraints(GromacsPTParser::ConstraintsContext *context) = 0;

    virtual std::any visitSettles_statement(GromacsPTParser::Settles_statementContext *context) = 0;

    virtual std::any visitSettles(GromacsPTParser::SettlesContext *context) = 0;

    virtual std::any visitVirtual_sites1_statement(GromacsPTParser::Virtual_sites1_statementContext *context) = 0;

    virtual std::any visitVirtual_sites1(GromacsPTParser::Virtual_sites1Context *context) = 0;

    virtual std::any visitVirtual_sites2_statement(GromacsPTParser::Virtual_sites2_statementContext *context) = 0;

    virtual std::any visitVirtual_sites2(GromacsPTParser::Virtual_sites2Context *context) = 0;

    virtual std::any visitVirtual_sites3_statement(GromacsPTParser::Virtual_sites3_statementContext *context) = 0;

    virtual std::any visitVirtual_sites3(GromacsPTParser::Virtual_sites3Context *context) = 0;

    virtual std::any visitVirtual_sites4_statement(GromacsPTParser::Virtual_sites4_statementContext *context) = 0;

    virtual std::any visitVirtual_sites4(GromacsPTParser::Virtual_sites4Context *context) = 0;

    virtual std::any visitVirtual_sitesn_statement(GromacsPTParser::Virtual_sitesn_statementContext *context) = 0;

    virtual std::any visitVirtual_sitesn(GromacsPTParser::Virtual_sitesnContext *context) = 0;

    virtual std::any visitSystem_statement(GromacsPTParser::System_statementContext *context) = 0;

    virtual std::any visitMolecules_statement(GromacsPTParser::Molecules_statementContext *context) = 0;

    virtual std::any visitMolecules(GromacsPTParser::MoleculesContext *context) = 0;

    virtual std::any visitNumber(GromacsPTParser::NumberContext *context) = 0;

    virtual std::any visitPosition_restraints(GromacsPTParser::Position_restraintsContext *context) = 0;

    virtual std::any visitPosition_restraint(GromacsPTParser::Position_restraintContext *context) = 0;


};

