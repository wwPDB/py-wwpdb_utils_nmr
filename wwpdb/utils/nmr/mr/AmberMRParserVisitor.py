# Generated from AmberMRParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AmberMRParser import AmberMRParser
else:
    from AmberMRParser import AmberMRParser

# This class defines a complete generic visitor for a parse tree produced by AmberMRParser.

class AmberMRParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AmberMRParser#amber_mr.
    def visitAmber_mr(self, ctx:AmberMRParser.Amber_mrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#nmr_restraint.
    def visitNmr_restraint(self, ctx:AmberMRParser.Nmr_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#noesy_volume_restraint.
    def visitNoesy_volume_restraint(self, ctx:AmberMRParser.Noesy_volume_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#chemical_shift_restraint.
    def visitChemical_shift_restraint(self, ctx:AmberMRParser.Chemical_shift_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#pcs_restraint.
    def visitPcs_restraint(self, ctx:AmberMRParser.Pcs_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#dipolar_coupling_restraint.
    def visitDipolar_coupling_restraint(self, ctx:AmberMRParser.Dipolar_coupling_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#csa_restraint.
    def visitCsa_restraint(self, ctx:AmberMRParser.Csa_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#restraint_statement.
    def visitRestraint_statement(self, ctx:AmberMRParser.Restraint_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#distance_statement.
    def visitDistance_statement(self, ctx:AmberMRParser.Distance_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#angle_statement.
    def visitAngle_statement(self, ctx:AmberMRParser.Angle_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#torsion_statement.
    def visitTorsion_statement(self, ctx:AmberMRParser.Torsion_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#plane_point_angle_statement.
    def visitPlane_point_angle_statement(self, ctx:AmberMRParser.Plane_point_angle_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#plane_plane_angle_statement.
    def visitPlane_plane_angle_statement(self, ctx:AmberMRParser.Plane_plane_angle_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#general_distance2_statement.
    def visitGeneral_distance2_statement(self, ctx:AmberMRParser.General_distance2_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#general_distance3_statement.
    def visitGeneral_distance3_statement(self, ctx:AmberMRParser.General_distance3_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#general_distance4_statement.
    def visitGeneral_distance4_statement(self, ctx:AmberMRParser.General_distance4_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#noeexp_statement.
    def visitNoeexp_statement(self, ctx:AmberMRParser.Noeexp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#shf_statement.
    def visitShf_statement(self, ctx:AmberMRParser.Shf_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#pcshf_statement.
    def visitPcshf_statement(self, ctx:AmberMRParser.Pcshf_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#align_statement.
    def visitAlign_statement(self, ctx:AmberMRParser.Align_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberMRParser#csa_statement.
    def visitCsa_statement(self, ctx:AmberMRParser.Csa_statementContext):
        return self.visitChildren(ctx)



del AmberMRParser