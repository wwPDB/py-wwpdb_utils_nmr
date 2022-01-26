# Generated from CnsMRParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CnsMRParser import CnsMRParser
else:
    from CnsMRParser import CnsMRParser

# This class defines a complete generic visitor for a parse tree produced by CnsMRParser.

class CnsMRParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CnsMRParser#cns_mr.
    def visitCns_mr(self, ctx:CnsMRParser.Cns_mrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#distance_restraint.
    def visitDistance_restraint(self, ctx:CnsMRParser.Distance_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#dihedral_angle_restraint.
    def visitDihedral_angle_restraint(self, ctx:CnsMRParser.Dihedral_angle_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#plane_restraint.
    def visitPlane_restraint(self, ctx:CnsMRParser.Plane_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#harmonic_restraint.
    def visitHarmonic_restraint(self, ctx:CnsMRParser.Harmonic_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#rdc_restraint.
    def visitRdc_restraint(self, ctx:CnsMRParser.Rdc_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#coupling_restraint.
    def visitCoupling_restraint(self, ctx:CnsMRParser.Coupling_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#carbon_shift_restraint.
    def visitCarbon_shift_restraint(self, ctx:CnsMRParser.Carbon_shift_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#proton_shift_restraint.
    def visitProton_shift_restraint(self, ctx:CnsMRParser.Proton_shift_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#conformation_db_restraint.
    def visitConformation_db_restraint(self, ctx:CnsMRParser.Conformation_db_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#diffusion_anisotropy_restraint.
    def visitDiffusion_anisotropy_restraint(self, ctx:CnsMRParser.Diffusion_anisotropy_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#one_bond_coupling_restraint.
    def visitOne_bond_coupling_restraint(self, ctx:CnsMRParser.One_bond_coupling_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#angle_db_restraint.
    def visitAngle_db_restraint(self, ctx:CnsMRParser.Angle_db_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#noe_statement.
    def visitNoe_statement(self, ctx:CnsMRParser.Noe_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#noe_assign.
    def visitNoe_assign(self, ctx:CnsMRParser.Noe_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#predict_statement.
    def visitPredict_statement(self, ctx:CnsMRParser.Predict_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#dihedral_statement.
    def visitDihedral_statement(self, ctx:CnsMRParser.Dihedral_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#dihedral_assign.
    def visitDihedral_assign(self, ctx:CnsMRParser.Dihedral_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#plane_statement.
    def visitPlane_statement(self, ctx:CnsMRParser.Plane_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#group_statement.
    def visitGroup_statement(self, ctx:CnsMRParser.Group_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#harmonic_statement.
    def visitHarmonic_statement(self, ctx:CnsMRParser.Harmonic_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#sani_statement.
    def visitSani_statement(self, ctx:CnsMRParser.Sani_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#sani_assign.
    def visitSani_assign(self, ctx:CnsMRParser.Sani_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#coupling_statement.
    def visitCoupling_statement(self, ctx:CnsMRParser.Coupling_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#coup_assign.
    def visitCoup_assign(self, ctx:CnsMRParser.Coup_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#carbon_shift_statement.
    def visitCarbon_shift_statement(self, ctx:CnsMRParser.Carbon_shift_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#carbon_shift_assign.
    def visitCarbon_shift_assign(self, ctx:CnsMRParser.Carbon_shift_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#carbon_shift_rcoil.
    def visitCarbon_shift_rcoil(self, ctx:CnsMRParser.Carbon_shift_rcoilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#proton_shift_statement.
    def visitProton_shift_statement(self, ctx:CnsMRParser.Proton_shift_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#observed.
    def visitObserved(self, ctx:CnsMRParser.ObservedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#proton_shift_rcoil.
    def visitProton_shift_rcoil(self, ctx:CnsMRParser.Proton_shift_rcoilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#proton_shift_anisotropy.
    def visitProton_shift_anisotropy(self, ctx:CnsMRParser.Proton_shift_anisotropyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#proton_shift_amides.
    def visitProton_shift_amides(self, ctx:CnsMRParser.Proton_shift_amidesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#proton_shift_carbons.
    def visitProton_shift_carbons(self, ctx:CnsMRParser.Proton_shift_carbonsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#proton_shift_nitrogens.
    def visitProton_shift_nitrogens(self, ctx:CnsMRParser.Proton_shift_nitrogensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#proton_shift_oxygens.
    def visitProton_shift_oxygens(self, ctx:CnsMRParser.Proton_shift_oxygensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#proton_shift_ring_atoms.
    def visitProton_shift_ring_atoms(self, ctx:CnsMRParser.Proton_shift_ring_atomsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#proton_shift_alphas_and_amides.
    def visitProton_shift_alphas_and_amides(self, ctx:CnsMRParser.Proton_shift_alphas_and_amidesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#conformation_statement.
    def visitConformation_statement(self, ctx:CnsMRParser.Conformation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#conf_assign.
    def visitConf_assign(self, ctx:CnsMRParser.Conf_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#diffusion_statement.
    def visitDiffusion_statement(self, ctx:CnsMRParser.Diffusion_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#dani_assign.
    def visitDani_assign(self, ctx:CnsMRParser.Dani_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#one_bond_coupling_statement.
    def visitOne_bond_coupling_statement(self, ctx:CnsMRParser.One_bond_coupling_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#one_bond_assign.
    def visitOne_bond_assign(self, ctx:CnsMRParser.One_bond_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#angle_db_statement.
    def visitAngle_db_statement(self, ctx:CnsMRParser.Angle_db_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#angle_db_assign.
    def visitAngle_db_assign(self, ctx:CnsMRParser.Angle_db_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#selection.
    def visitSelection(self, ctx:CnsMRParser.SelectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#selection_expression.
    def visitSelection_expression(self, ctx:CnsMRParser.Selection_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#term.
    def visitTerm(self, ctx:CnsMRParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#factor.
    def visitFactor(self, ctx:CnsMRParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CnsMRParser#vector_3d.
    def visitVector_3d(self, ctx:CnsMRParser.Vector_3dContext):
        return self.visitChildren(ctx)



del CnsMRParser