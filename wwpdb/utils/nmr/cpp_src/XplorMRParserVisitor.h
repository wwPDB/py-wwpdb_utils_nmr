
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XplorMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "XplorMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by XplorMRParser.
 */
class  XplorMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by XplorMRParser.
   */
    virtual std::any visitXplor_nih_mr(XplorMRParser::Xplor_nih_mrContext *context) = 0;

    virtual std::any visitDistance_restraint(XplorMRParser::Distance_restraintContext *context) = 0;

    virtual std::any visitDihedral_angle_restraint(XplorMRParser::Dihedral_angle_restraintContext *context) = 0;

    virtual std::any visitRdc_restraint(XplorMRParser::Rdc_restraintContext *context) = 0;

    virtual std::any visitPlanar_restraint(XplorMRParser::Planar_restraintContext *context) = 0;

    virtual std::any visitHarmonic_restraint(XplorMRParser::Harmonic_restraintContext *context) = 0;

    virtual std::any visitAntidistance_restraint(XplorMRParser::Antidistance_restraintContext *context) = 0;

    virtual std::any visitCoupling_restraint(XplorMRParser::Coupling_restraintContext *context) = 0;

    virtual std::any visitCarbon_shift_restraint(XplorMRParser::Carbon_shift_restraintContext *context) = 0;

    virtual std::any visitProton_shift_restraint(XplorMRParser::Proton_shift_restraintContext *context) = 0;

    virtual std::any visitDihedral_angle_db_restraint(XplorMRParser::Dihedral_angle_db_restraintContext *context) = 0;

    virtual std::any visitRadius_of_gyration_restraint(XplorMRParser::Radius_of_gyration_restraintContext *context) = 0;

    virtual std::any visitDiffusion_anisotropy_restraint(XplorMRParser::Diffusion_anisotropy_restraintContext *context) = 0;

    virtual std::any visitOrientation_db_restraint(XplorMRParser::Orientation_db_restraintContext *context) = 0;

    virtual std::any visitCsa_restraint(XplorMRParser::Csa_restraintContext *context) = 0;

    virtual std::any visitPcsa_restraint(XplorMRParser::Pcsa_restraintContext *context) = 0;

    virtual std::any visitOne_bond_coupling_restraint(XplorMRParser::One_bond_coupling_restraintContext *context) = 0;

    virtual std::any visitAngle_db_restraint(XplorMRParser::Angle_db_restraintContext *context) = 0;

    virtual std::any visitPre_restraint(XplorMRParser::Pre_restraintContext *context) = 0;

    virtual std::any visitPcs_restraint(XplorMRParser::Pcs_restraintContext *context) = 0;

    virtual std::any visitPrdc_restraint(XplorMRParser::Prdc_restraintContext *context) = 0;

    virtual std::any visitPorientation_restraint(XplorMRParser::Porientation_restraintContext *context) = 0;

    virtual std::any visitPccr_restraint(XplorMRParser::Pccr_restraintContext *context) = 0;

    virtual std::any visitHbond_restraint(XplorMRParser::Hbond_restraintContext *context) = 0;

    virtual std::any visitHbond_db_restraint(XplorMRParser::Hbond_db_restraintContext *context) = 0;

    virtual std::any visitNoe_statement(XplorMRParser::Noe_statementContext *context) = 0;

    virtual std::any visitNoe_assign(XplorMRParser::Noe_assignContext *context) = 0;

    virtual std::any visitPredict_statement(XplorMRParser::Predict_statementContext *context) = 0;

    virtual std::any visitNoe_annotation(XplorMRParser::Noe_annotationContext *context) = 0;

    virtual std::any visitDihedral_statement(XplorMRParser::Dihedral_statementContext *context) = 0;

    virtual std::any visitDihedral_assign(XplorMRParser::Dihedral_assignContext *context) = 0;

    virtual std::any visitSani_statement(XplorMRParser::Sani_statementContext *context) = 0;

    virtual std::any visitSani_assign(XplorMRParser::Sani_assignContext *context) = 0;

    virtual std::any visitXdip_statement(XplorMRParser::Xdip_statementContext *context) = 0;

    virtual std::any visitXdip_assign(XplorMRParser::Xdip_assignContext *context) = 0;

    virtual std::any visitVean_statement(XplorMRParser::Vean_statementContext *context) = 0;

    virtual std::any visitVean_assign(XplorMRParser::Vean_assignContext *context) = 0;

    virtual std::any visitTenso_statement(XplorMRParser::Tenso_statementContext *context) = 0;

    virtual std::any visitTenso_assign(XplorMRParser::Tenso_assignContext *context) = 0;

    virtual std::any visitAnis_statement(XplorMRParser::Anis_statementContext *context) = 0;

    virtual std::any visitAnis_assign(XplorMRParser::Anis_assignContext *context) = 0;

    virtual std::any visitPlanar_statement(XplorMRParser::Planar_statementContext *context) = 0;

    virtual std::any visitPlanar_group(XplorMRParser::Planar_groupContext *context) = 0;

    virtual std::any visitGroup_statement(XplorMRParser::Group_statementContext *context) = 0;

    virtual std::any visitHarmonic_statement(XplorMRParser::Harmonic_statementContext *context) = 0;

    virtual std::any visitHarmonic_assign(XplorMRParser::Harmonic_assignContext *context) = 0;

    virtual std::any visitAntidistance_statement(XplorMRParser::Antidistance_statementContext *context) = 0;

    virtual std::any visitXadc_assign(XplorMRParser::Xadc_assignContext *context) = 0;

    virtual std::any visitCoupling_statement(XplorMRParser::Coupling_statementContext *context) = 0;

    virtual std::any visitCoup_assign(XplorMRParser::Coup_assignContext *context) = 0;

    virtual std::any visitCarbon_shift_statement(XplorMRParser::Carbon_shift_statementContext *context) = 0;

    virtual std::any visitCarbon_shift_assign(XplorMRParser::Carbon_shift_assignContext *context) = 0;

    virtual std::any visitCarbon_shift_rcoil(XplorMRParser::Carbon_shift_rcoilContext *context) = 0;

    virtual std::any visitProton_shift_statement(XplorMRParser::Proton_shift_statementContext *context) = 0;

    virtual std::any visitObserved(XplorMRParser::ObservedContext *context) = 0;

    virtual std::any visitProton_shift_rcoil(XplorMRParser::Proton_shift_rcoilContext *context) = 0;

    virtual std::any visitProton_shift_anisotropy(XplorMRParser::Proton_shift_anisotropyContext *context) = 0;

    virtual std::any visitProton_shift_amides(XplorMRParser::Proton_shift_amidesContext *context) = 0;

    virtual std::any visitProton_shift_carbons(XplorMRParser::Proton_shift_carbonsContext *context) = 0;

    virtual std::any visitProton_shift_nitrogens(XplorMRParser::Proton_shift_nitrogensContext *context) = 0;

    virtual std::any visitProton_shift_oxygens(XplorMRParser::Proton_shift_oxygensContext *context) = 0;

    virtual std::any visitProton_shift_ring_atoms(XplorMRParser::Proton_shift_ring_atomsContext *context) = 0;

    virtual std::any visitProton_shift_alphas_and_amides(XplorMRParser::Proton_shift_alphas_and_amidesContext *context) = 0;

    virtual std::any visitRamachandran_statement(XplorMRParser::Ramachandran_statementContext *context) = 0;

    virtual std::any visitRama_assign(XplorMRParser::Rama_assignContext *context) = 0;

    virtual std::any visitCollapse_statement(XplorMRParser::Collapse_statementContext *context) = 0;

    virtual std::any visitColl_assign(XplorMRParser::Coll_assignContext *context) = 0;

    virtual std::any visitDiffusion_statement(XplorMRParser::Diffusion_statementContext *context) = 0;

    virtual std::any visitDani_assign(XplorMRParser::Dani_assignContext *context) = 0;

    virtual std::any visitOrientation_statement(XplorMRParser::Orientation_statementContext *context) = 0;

    virtual std::any visitOrie_assign(XplorMRParser::Orie_assignContext *context) = 0;

    virtual std::any visitCsa_statement(XplorMRParser::Csa_statementContext *context) = 0;

    virtual std::any visitCsa_assign(XplorMRParser::Csa_assignContext *context) = 0;

    virtual std::any visitPcsa_statement(XplorMRParser::Pcsa_statementContext *context) = 0;

    virtual std::any visitOne_bond_coupling_statement(XplorMRParser::One_bond_coupling_statementContext *context) = 0;

    virtual std::any visitOne_bond_assign(XplorMRParser::One_bond_assignContext *context) = 0;

    virtual std::any visitAngle_db_statement(XplorMRParser::Angle_db_statementContext *context) = 0;

    virtual std::any visitAngle_db_assign(XplorMRParser::Angle_db_assignContext *context) = 0;

    virtual std::any visitPre_statement(XplorMRParser::Pre_statementContext *context) = 0;

    virtual std::any visitPre_assign(XplorMRParser::Pre_assignContext *context) = 0;

    virtual std::any visitPcs_statement(XplorMRParser::Pcs_statementContext *context) = 0;

    virtual std::any visitPcs_assign(XplorMRParser::Pcs_assignContext *context) = 0;

    virtual std::any visitPrdc_statement(XplorMRParser::Prdc_statementContext *context) = 0;

    virtual std::any visitPrdc_assign(XplorMRParser::Prdc_assignContext *context) = 0;

    virtual std::any visitPorientation_statement(XplorMRParser::Porientation_statementContext *context) = 0;

    virtual std::any visitPorientation_assign(XplorMRParser::Porientation_assignContext *context) = 0;

    virtual std::any visitPccr_statement(XplorMRParser::Pccr_statementContext *context) = 0;

    virtual std::any visitPccr_assign(XplorMRParser::Pccr_assignContext *context) = 0;

    virtual std::any visitHbond_statement(XplorMRParser::Hbond_statementContext *context) = 0;

    virtual std::any visitHbond_assign(XplorMRParser::Hbond_assignContext *context) = 0;

    virtual std::any visitHbond_db_statement(XplorMRParser::Hbond_db_statementContext *context) = 0;

    virtual std::any visitHbond_db_assign(XplorMRParser::Hbond_db_assignContext *context) = 0;

    virtual std::any visitNcs_restraint(XplorMRParser::Ncs_restraintContext *context) = 0;

    virtual std::any visitNcs_statement(XplorMRParser::Ncs_statementContext *context) = 0;

    virtual std::any visitNcs_group_statement(XplorMRParser::Ncs_group_statementContext *context) = 0;

    virtual std::any visitSelection(XplorMRParser::SelectionContext *context) = 0;

    virtual std::any visitSelection_expression(XplorMRParser::Selection_expressionContext *context) = 0;

    virtual std::any visitTerm(XplorMRParser::TermContext *context) = 0;

    virtual std::any visitFactor(XplorMRParser::FactorContext *context) = 0;

    virtual std::any visitNumber(XplorMRParser::NumberContext *context) = 0;

    virtual std::any visitNumber_f(XplorMRParser::Number_fContext *context) = 0;

    virtual std::any visitNumber_s(XplorMRParser::Number_sContext *context) = 0;

    virtual std::any visitNumber_a(XplorMRParser::Number_aContext *context) = 0;

    virtual std::any visitClassification(XplorMRParser::ClassificationContext *context) = 0;

    virtual std::any visitClass_name(XplorMRParser::Class_nameContext *context) = 0;

    virtual std::any visitFlag_statement(XplorMRParser::Flag_statementContext *context) = 0;

    virtual std::any visitVector_statement(XplorMRParser::Vector_statementContext *context) = 0;

    virtual std::any visitVector_mode(XplorMRParser::Vector_modeContext *context) = 0;

    virtual std::any visitVector_expression(XplorMRParser::Vector_expressionContext *context) = 0;

    virtual std::any visitVector_operation(XplorMRParser::Vector_operationContext *context) = 0;

    virtual std::any visitVflc(XplorMRParser::VflcContext *context) = 0;

    virtual std::any visitVector_func_call(XplorMRParser::Vector_func_callContext *context) = 0;

    virtual std::any visitVector_show_property(XplorMRParser::Vector_show_propertyContext *context) = 0;

    virtual std::any visitEvaluate_statement(XplorMRParser::Evaluate_statementContext *context) = 0;

    virtual std::any visitEvaluate_operation(XplorMRParser::Evaluate_operationContext *context) = 0;

    virtual std::any visitPatch_statement(XplorMRParser::Patch_statementContext *context) = 0;

    virtual std::any visitParameter_setting(XplorMRParser::Parameter_settingContext *context) = 0;

    virtual std::any visitParameter_statement(XplorMRParser::Parameter_statementContext *context) = 0;

    virtual std::any visitNoe_assign_loop(XplorMRParser::Noe_assign_loopContext *context) = 0;

    virtual std::any visitDihedral_assign_loop(XplorMRParser::Dihedral_assign_loopContext *context) = 0;

    virtual std::any visitSani_assign_loop(XplorMRParser::Sani_assign_loopContext *context) = 0;

    virtual std::any visitXadc_assign_loop(XplorMRParser::Xadc_assign_loopContext *context) = 0;

    virtual std::any visitCoup_assign_loop(XplorMRParser::Coup_assign_loopContext *context) = 0;

    virtual std::any visitColl_assign_loop(XplorMRParser::Coll_assign_loopContext *context) = 0;

    virtual std::any visitCsa_assign_loop(XplorMRParser::Csa_assign_loopContext *context) = 0;

    virtual std::any visitPre_assign_loop(XplorMRParser::Pre_assign_loopContext *context) = 0;

    virtual std::any visitPcs_assign_loop(XplorMRParser::Pcs_assign_loopContext *context) = 0;

    virtual std::any visitHbond_assign_loop(XplorMRParser::Hbond_assign_loopContext *context) = 0;

    virtual std::any visitHbond_db_assign_loop(XplorMRParser::Hbond_db_assign_loopContext *context) = 0;

    virtual std::any visitPlanar_group_loop(XplorMRParser::Planar_group_loopContext *context) = 0;


};

