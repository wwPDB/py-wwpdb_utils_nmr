# Generated from CyanaMRParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CyanaMRParser import CyanaMRParser
else:
    from CyanaMRParser import CyanaMRParser

# This class defines a complete generic visitor for a parse tree produced by CyanaMRParser.

class CyanaMRParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CyanaMRParser#cyana_mr.
    def visitCyana_mr(self, ctx:CyanaMRParser.Cyana_mrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyanaMRParser#distance_restraints.
    def visitDistance_restraints(self, ctx:CyanaMRParser.Distance_restraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyanaMRParser#distance_restraint.
    def visitDistance_restraint(self, ctx:CyanaMRParser.Distance_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyanaMRParser#torsion_angle_restraints.
    def visitTorsion_angle_restraints(self, ctx:CyanaMRParser.Torsion_angle_restraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyanaMRParser#torsion_angle_restraint.
    def visitTorsion_angle_restraint(self, ctx:CyanaMRParser.Torsion_angle_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyanaMRParser#rdc_restraints.
    def visitRdc_restraints(self, ctx:CyanaMRParser.Rdc_restraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyanaMRParser#rdc_parameter.
    def visitRdc_parameter(self, ctx:CyanaMRParser.Rdc_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyanaMRParser#rdc_restraint.
    def visitRdc_restraint(self, ctx:CyanaMRParser.Rdc_restraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyanaMRParser#pcs_restraints.
    def visitPcs_restraints(self, ctx:CyanaMRParser.Pcs_restraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyanaMRParser#pcs_parameter.
    def visitPcs_parameter(self, ctx:CyanaMRParser.Pcs_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyanaMRParser#pcs_restraint.
    def visitPcs_restraint(self, ctx:CyanaMRParser.Pcs_restraintContext):
        return self.visitChildren(ctx)



del CyanaMRParser