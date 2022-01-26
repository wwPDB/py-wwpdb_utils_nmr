# Generated from XplorMRParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XplorMRParser import XplorMRParser
else:
    from XplorMRParser import XplorMRParser

# This class defines a complete generic visitor for a parse tree produced by XplorMRParser.

class XplorMRParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XplorMRParser#xplor_nih_mr.
    def visitXplor_nih_mr(self, ctx:XplorMRParser.Xplor_nih_mrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#distance_restraint.
    def visitDistance_restraint(self, ctx:XplorMRParser.Distance_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#dihedral_angle_restraint.
    def visitDihedral_angle_restraint(self, ctx:XplorMRParser.Dihedral_angle_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#rdc_restraint.
    def visitRdc_restraint(self, ctx:XplorMRParser.Rdc_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#planar_restraint.
    def visitPlanar_restraint(self, ctx:XplorMRParser.Planar_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#antidistance_restraint.
    def visitAntidistance_restraint(self, ctx:XplorMRParser.Antidistance_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#coupling_restraint.
    def visitCoupling_restraint(self, ctx:XplorMRParser.Coupling_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#carbon_shift_restraint.
    def visitCarbon_shift_restraint(self, ctx:XplorMRParser.Carbon_shift_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#proton_shift_restraint.
    def visitProton_shift_restraint(self, ctx:XplorMRParser.Proton_shift_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#dihedral_angle_db_restraint.
    def visitDihedral_angle_db_restraint(self, ctx:XplorMRParser.Dihedral_angle_db_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#radius_of_gyration_restraint.
    def visitRadius_of_gyration_restraint(self, ctx:XplorMRParser.Radius_of_gyration_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#diffusion_anisotropy_restraint.
    def visitDiffusion_anisotropy_restraint(self, ctx:XplorMRParser.Diffusion_anisotropy_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#orientation_db_restraint.
    def visitOrientation_db_restraint(self, ctx:XplorMRParser.Orientation_db_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#csa_restraint.
    def visitCsa_restraint(self, ctx:XplorMRParser.Csa_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#pcsa_restraint.
    def visitPcsa_restraint(self, ctx:XplorMRParser.Pcsa_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#one_bond_coupling_restraint.
    def visitOne_bond_coupling_restraint(self, ctx:XplorMRParser.One_bond_coupling_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#angle_db_restraint.
    def visitAngle_db_restraint(self, ctx:XplorMRParser.Angle_db_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#pre_restraint.
    def visitPre_restraint(self, ctx:XplorMRParser.Pre_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#pcs_restraint.
    def visitPcs_restraint(self, ctx:XplorMRParser.Pcs_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#prdc_restraint.
    def visitPrdc_restraint(self, ctx:XplorMRParser.Prdc_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#porientation_restraint.
    def visitPorientation_restraint(self, ctx:XplorMRParser.Porientation_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#pccr_restraint.
    def visitPccr_restraint(self, ctx:XplorMRParser.Pccr_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#hbond_restraint.
    def visitHbond_restraint(self, ctx:XplorMRParser.Hbond_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#noe_statement.
    def visitNoe_statement(self, ctx:XplorMRParser.Noe_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#noe_assign.
    def visitNoe_assign(self, ctx:XplorMRParser.Noe_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#predict_statement.
    def visitPredict_statement(self, ctx:XplorMRParser.Predict_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#dihedral_statement.
    def visitDihedral_statement(self, ctx:XplorMRParser.Dihedral_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#dihedral_assign.
    def visitDihedral_assign(self, ctx:XplorMRParser.Dihedral_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#sani_statement.
    def visitSani_statement(self, ctx:XplorMRParser.Sani_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#sani_assign.
    def visitSani_assign(self, ctx:XplorMRParser.Sani_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#xdip_statement.
    def visitXdip_statement(self, ctx:XplorMRParser.Xdip_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#xdip_assign.
    def visitXdip_assign(self, ctx:XplorMRParser.Xdip_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#vean_statement.
    def visitVean_statement(self, ctx:XplorMRParser.Vean_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#vean_assign.
    def visitVean_assign(self, ctx:XplorMRParser.Vean_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#tens_statement.
    def visitTens_statement(self, ctx:XplorMRParser.Tens_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#tens_assign.
    def visitTens_assign(self, ctx:XplorMRParser.Tens_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#anis_statement.
    def visitAnis_statement(self, ctx:XplorMRParser.Anis_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#anis_assign.
    def visitAnis_assign(self, ctx:XplorMRParser.Anis_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#planar_statement.
    def visitPlanar_statement(self, ctx:XplorMRParser.Planar_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#group_statement.
    def visitGroup_statement(self, ctx:XplorMRParser.Group_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#antidistance_statement.
    def visitAntidistance_statement(self, ctx:XplorMRParser.Antidistance_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#xadc_assign.
    def visitXadc_assign(self, ctx:XplorMRParser.Xadc_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#coupling_statement.
    def visitCoupling_statement(self, ctx:XplorMRParser.Coupling_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#coup_assign.
    def visitCoup_assign(self, ctx:XplorMRParser.Coup_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#carbon_shift_statement.
    def visitCarbon_shift_statement(self, ctx:XplorMRParser.Carbon_shift_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#carbon_shift_assign.
    def visitCarbon_shift_assign(self, ctx:XplorMRParser.Carbon_shift_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#carbon_shift_rcoil.
    def visitCarbon_shift_rcoil(self, ctx:XplorMRParser.Carbon_shift_rcoilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#proton_shift_statement.
    def visitProton_shift_statement(self, ctx:XplorMRParser.Proton_shift_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#observed.
    def visitObserved(self, ctx:XplorMRParser.ObservedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#proton_shift_rcoil.
    def visitProton_shift_rcoil(self, ctx:XplorMRParser.Proton_shift_rcoilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#proton_shift_anisotropy.
    def visitProton_shift_anisotropy(self, ctx:XplorMRParser.Proton_shift_anisotropyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#proton_shift_amides.
    def visitProton_shift_amides(self, ctx:XplorMRParser.Proton_shift_amidesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#proton_shift_carbons.
    def visitProton_shift_carbons(self, ctx:XplorMRParser.Proton_shift_carbonsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#proton_shift_nitrogens.
    def visitProton_shift_nitrogens(self, ctx:XplorMRParser.Proton_shift_nitrogensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#proton_shift_oxygens.
    def visitProton_shift_oxygens(self, ctx:XplorMRParser.Proton_shift_oxygensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#proton_shift_ring_atoms.
    def visitProton_shift_ring_atoms(self, ctx:XplorMRParser.Proton_shift_ring_atomsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#proton_shift_alphas_and_amides.
    def visitProton_shift_alphas_and_amides(self, ctx:XplorMRParser.Proton_shift_alphas_and_amidesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#ramachandran_statement.
    def visitRamachandran_statement(self, ctx:XplorMRParser.Ramachandran_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#rama_assign.
    def visitRama_assign(self, ctx:XplorMRParser.Rama_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#collapse_statement.
    def visitCollapse_statement(self, ctx:XplorMRParser.Collapse_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#diffusion_statement.
    def visitDiffusion_statement(self, ctx:XplorMRParser.Diffusion_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#dani_assign.
    def visitDani_assign(self, ctx:XplorMRParser.Dani_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#orientation_statement.
    def visitOrientation_statement(self, ctx:XplorMRParser.Orientation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#orie_assign.
    def visitOrie_assign(self, ctx:XplorMRParser.Orie_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#csa_statement.
    def visitCsa_statement(self, ctx:XplorMRParser.Csa_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#csa_assign.
    def visitCsa_assign(self, ctx:XplorMRParser.Csa_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#pcsa_statement.
    def visitPcsa_statement(self, ctx:XplorMRParser.Pcsa_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#one_bond_coupling_statement.
    def visitOne_bond_coupling_statement(self, ctx:XplorMRParser.One_bond_coupling_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#one_bond_assign.
    def visitOne_bond_assign(self, ctx:XplorMRParser.One_bond_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#angle_db_statement.
    def visitAngle_db_statement(self, ctx:XplorMRParser.Angle_db_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#angle_db_assign.
    def visitAngle_db_assign(self, ctx:XplorMRParser.Angle_db_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#pre_statement.
    def visitPre_statement(self, ctx:XplorMRParser.Pre_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#pre_assign.
    def visitPre_assign(self, ctx:XplorMRParser.Pre_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#pcs_statement.
    def visitPcs_statement(self, ctx:XplorMRParser.Pcs_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#pcs_assign.
    def visitPcs_assign(self, ctx:XplorMRParser.Pcs_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#prdc_statement.
    def visitPrdc_statement(self, ctx:XplorMRParser.Prdc_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#prdc_assign.
    def visitPrdc_assign(self, ctx:XplorMRParser.Prdc_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#porientation_statement.
    def visitPorientation_statement(self, ctx:XplorMRParser.Porientation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#porientation_assign.
    def visitPorientation_assign(self, ctx:XplorMRParser.Porientation_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#pccr_statement.
    def visitPccr_statement(self, ctx:XplorMRParser.Pccr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#pccr_assign.
    def visitPccr_assign(self, ctx:XplorMRParser.Pccr_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#hbond_statement.
    def visitHbond_statement(self, ctx:XplorMRParser.Hbond_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#hbond_assign.
    def visitHbond_assign(self, ctx:XplorMRParser.Hbond_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#selection.
    def visitSelection(self, ctx:XplorMRParser.SelectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#selection_expression.
    def visitSelection_expression(self, ctx:XplorMRParser.Selection_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#term.
    def visitTerm(self, ctx:XplorMRParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#factor.
    def visitFactor(self, ctx:XplorMRParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorMRParser#vector_3d.
    def visitVector_3d(self, ctx:XplorMRParser.Vector_3dContext):
        return self.visitChildren(ctx)



del XplorMRParser