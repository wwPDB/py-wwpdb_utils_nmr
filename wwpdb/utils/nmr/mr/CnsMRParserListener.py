# Generated from CnsMRParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CnsMRParser import CnsMRParser
else:
    from CnsMRParser import CnsMRParser

# This class defines a complete listener for a parse tree produced by CnsMRParser.
class CnsMRParserListener(ParseTreeListener):

    # Enter a parse tree produced by CnsMRParser#cns_mr.
    def enterCns_mr(self, ctx:CnsMRParser.Cns_mrContext):
        pass

    # Exit a parse tree produced by CnsMRParser#cns_mr.
    def exitCns_mr(self, ctx:CnsMRParser.Cns_mrContext):
        pass


    # Enter a parse tree produced by CnsMRParser#distance_restraint.
    def enterDistance_restraint(self, ctx:CnsMRParser.Distance_restraintContext):
        pass

    # Exit a parse tree produced by CnsMRParser#distance_restraint.
    def exitDistance_restraint(self, ctx:CnsMRParser.Distance_restraintContext):
        pass


    # Enter a parse tree produced by CnsMRParser#dihedral_angle_restraint.
    def enterDihedral_angle_restraint(self, ctx:CnsMRParser.Dihedral_angle_restraintContext):
        pass

    # Exit a parse tree produced by CnsMRParser#dihedral_angle_restraint.
    def exitDihedral_angle_restraint(self, ctx:CnsMRParser.Dihedral_angle_restraintContext):
        pass


    # Enter a parse tree produced by CnsMRParser#plane_restraint.
    def enterPlane_restraint(self, ctx:CnsMRParser.Plane_restraintContext):
        pass

    # Exit a parse tree produced by CnsMRParser#plane_restraint.
    def exitPlane_restraint(self, ctx:CnsMRParser.Plane_restraintContext):
        pass


    # Enter a parse tree produced by CnsMRParser#harmonic_restraint.
    def enterHarmonic_restraint(self, ctx:CnsMRParser.Harmonic_restraintContext):
        pass

    # Exit a parse tree produced by CnsMRParser#harmonic_restraint.
    def exitHarmonic_restraint(self, ctx:CnsMRParser.Harmonic_restraintContext):
        pass


    # Enter a parse tree produced by CnsMRParser#rdc_restraint.
    def enterRdc_restraint(self, ctx:CnsMRParser.Rdc_restraintContext):
        pass

    # Exit a parse tree produced by CnsMRParser#rdc_restraint.
    def exitRdc_restraint(self, ctx:CnsMRParser.Rdc_restraintContext):
        pass


    # Enter a parse tree produced by CnsMRParser#coupling_restraint.
    def enterCoupling_restraint(self, ctx:CnsMRParser.Coupling_restraintContext):
        pass

    # Exit a parse tree produced by CnsMRParser#coupling_restraint.
    def exitCoupling_restraint(self, ctx:CnsMRParser.Coupling_restraintContext):
        pass


    # Enter a parse tree produced by CnsMRParser#carbon_shift_restraint.
    def enterCarbon_shift_restraint(self, ctx:CnsMRParser.Carbon_shift_restraintContext):
        pass

    # Exit a parse tree produced by CnsMRParser#carbon_shift_restraint.
    def exitCarbon_shift_restraint(self, ctx:CnsMRParser.Carbon_shift_restraintContext):
        pass


    # Enter a parse tree produced by CnsMRParser#proton_shift_restraint.
    def enterProton_shift_restraint(self, ctx:CnsMRParser.Proton_shift_restraintContext):
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_restraint.
    def exitProton_shift_restraint(self, ctx:CnsMRParser.Proton_shift_restraintContext):
        pass


    # Enter a parse tree produced by CnsMRParser#conformation_db_restraint.
    def enterConformation_db_restraint(self, ctx:CnsMRParser.Conformation_db_restraintContext):
        pass

    # Exit a parse tree produced by CnsMRParser#conformation_db_restraint.
    def exitConformation_db_restraint(self, ctx:CnsMRParser.Conformation_db_restraintContext):
        pass


    # Enter a parse tree produced by CnsMRParser#diffusion_anisotropy_restraint.
    def enterDiffusion_anisotropy_restraint(self, ctx:CnsMRParser.Diffusion_anisotropy_restraintContext):
        pass

    # Exit a parse tree produced by CnsMRParser#diffusion_anisotropy_restraint.
    def exitDiffusion_anisotropy_restraint(self, ctx:CnsMRParser.Diffusion_anisotropy_restraintContext):
        pass


    # Enter a parse tree produced by CnsMRParser#one_bond_coupling_restraint.
    def enterOne_bond_coupling_restraint(self, ctx:CnsMRParser.One_bond_coupling_restraintContext):
        pass

    # Exit a parse tree produced by CnsMRParser#one_bond_coupling_restraint.
    def exitOne_bond_coupling_restraint(self, ctx:CnsMRParser.One_bond_coupling_restraintContext):
        pass


    # Enter a parse tree produced by CnsMRParser#angle_db_restraint.
    def enterAngle_db_restraint(self, ctx:CnsMRParser.Angle_db_restraintContext):
        pass

    # Exit a parse tree produced by CnsMRParser#angle_db_restraint.
    def exitAngle_db_restraint(self, ctx:CnsMRParser.Angle_db_restraintContext):
        pass


    # Enter a parse tree produced by CnsMRParser#noe_statement.
    def enterNoe_statement(self, ctx:CnsMRParser.Noe_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#noe_statement.
    def exitNoe_statement(self, ctx:CnsMRParser.Noe_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#noe_assign.
    def enterNoe_assign(self, ctx:CnsMRParser.Noe_assignContext):
        pass

    # Exit a parse tree produced by CnsMRParser#noe_assign.
    def exitNoe_assign(self, ctx:CnsMRParser.Noe_assignContext):
        pass


    # Enter a parse tree produced by CnsMRParser#predict_statement.
    def enterPredict_statement(self, ctx:CnsMRParser.Predict_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#predict_statement.
    def exitPredict_statement(self, ctx:CnsMRParser.Predict_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#dihedral_statement.
    def enterDihedral_statement(self, ctx:CnsMRParser.Dihedral_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#dihedral_statement.
    def exitDihedral_statement(self, ctx:CnsMRParser.Dihedral_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#dihedral_assign.
    def enterDihedral_assign(self, ctx:CnsMRParser.Dihedral_assignContext):
        pass

    # Exit a parse tree produced by CnsMRParser#dihedral_assign.
    def exitDihedral_assign(self, ctx:CnsMRParser.Dihedral_assignContext):
        pass


    # Enter a parse tree produced by CnsMRParser#plane_statement.
    def enterPlane_statement(self, ctx:CnsMRParser.Plane_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#plane_statement.
    def exitPlane_statement(self, ctx:CnsMRParser.Plane_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#group_statement.
    def enterGroup_statement(self, ctx:CnsMRParser.Group_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#group_statement.
    def exitGroup_statement(self, ctx:CnsMRParser.Group_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#harmonic_statement.
    def enterHarmonic_statement(self, ctx:CnsMRParser.Harmonic_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#harmonic_statement.
    def exitHarmonic_statement(self, ctx:CnsMRParser.Harmonic_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#sani_statement.
    def enterSani_statement(self, ctx:CnsMRParser.Sani_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#sani_statement.
    def exitSani_statement(self, ctx:CnsMRParser.Sani_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#sani_assign.
    def enterSani_assign(self, ctx:CnsMRParser.Sani_assignContext):
        pass

    # Exit a parse tree produced by CnsMRParser#sani_assign.
    def exitSani_assign(self, ctx:CnsMRParser.Sani_assignContext):
        pass


    # Enter a parse tree produced by CnsMRParser#coupling_statement.
    def enterCoupling_statement(self, ctx:CnsMRParser.Coupling_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#coupling_statement.
    def exitCoupling_statement(self, ctx:CnsMRParser.Coupling_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#coup_assign.
    def enterCoup_assign(self, ctx:CnsMRParser.Coup_assignContext):
        pass

    # Exit a parse tree produced by CnsMRParser#coup_assign.
    def exitCoup_assign(self, ctx:CnsMRParser.Coup_assignContext):
        pass


    # Enter a parse tree produced by CnsMRParser#carbon_shift_statement.
    def enterCarbon_shift_statement(self, ctx:CnsMRParser.Carbon_shift_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#carbon_shift_statement.
    def exitCarbon_shift_statement(self, ctx:CnsMRParser.Carbon_shift_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#carbon_shift_assign.
    def enterCarbon_shift_assign(self, ctx:CnsMRParser.Carbon_shift_assignContext):
        pass

    # Exit a parse tree produced by CnsMRParser#carbon_shift_assign.
    def exitCarbon_shift_assign(self, ctx:CnsMRParser.Carbon_shift_assignContext):
        pass


    # Enter a parse tree produced by CnsMRParser#carbon_shift_rcoil.
    def enterCarbon_shift_rcoil(self, ctx:CnsMRParser.Carbon_shift_rcoilContext):
        pass

    # Exit a parse tree produced by CnsMRParser#carbon_shift_rcoil.
    def exitCarbon_shift_rcoil(self, ctx:CnsMRParser.Carbon_shift_rcoilContext):
        pass


    # Enter a parse tree produced by CnsMRParser#proton_shift_statement.
    def enterProton_shift_statement(self, ctx:CnsMRParser.Proton_shift_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_statement.
    def exitProton_shift_statement(self, ctx:CnsMRParser.Proton_shift_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#observed.
    def enterObserved(self, ctx:CnsMRParser.ObservedContext):
        pass

    # Exit a parse tree produced by CnsMRParser#observed.
    def exitObserved(self, ctx:CnsMRParser.ObservedContext):
        pass


    # Enter a parse tree produced by CnsMRParser#proton_shift_rcoil.
    def enterProton_shift_rcoil(self, ctx:CnsMRParser.Proton_shift_rcoilContext):
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_rcoil.
    def exitProton_shift_rcoil(self, ctx:CnsMRParser.Proton_shift_rcoilContext):
        pass


    # Enter a parse tree produced by CnsMRParser#proton_shift_anisotropy.
    def enterProton_shift_anisotropy(self, ctx:CnsMRParser.Proton_shift_anisotropyContext):
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_anisotropy.
    def exitProton_shift_anisotropy(self, ctx:CnsMRParser.Proton_shift_anisotropyContext):
        pass


    # Enter a parse tree produced by CnsMRParser#proton_shift_amides.
    def enterProton_shift_amides(self, ctx:CnsMRParser.Proton_shift_amidesContext):
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_amides.
    def exitProton_shift_amides(self, ctx:CnsMRParser.Proton_shift_amidesContext):
        pass


    # Enter a parse tree produced by CnsMRParser#proton_shift_carbons.
    def enterProton_shift_carbons(self, ctx:CnsMRParser.Proton_shift_carbonsContext):
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_carbons.
    def exitProton_shift_carbons(self, ctx:CnsMRParser.Proton_shift_carbonsContext):
        pass


    # Enter a parse tree produced by CnsMRParser#proton_shift_nitrogens.
    def enterProton_shift_nitrogens(self, ctx:CnsMRParser.Proton_shift_nitrogensContext):
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_nitrogens.
    def exitProton_shift_nitrogens(self, ctx:CnsMRParser.Proton_shift_nitrogensContext):
        pass


    # Enter a parse tree produced by CnsMRParser#proton_shift_oxygens.
    def enterProton_shift_oxygens(self, ctx:CnsMRParser.Proton_shift_oxygensContext):
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_oxygens.
    def exitProton_shift_oxygens(self, ctx:CnsMRParser.Proton_shift_oxygensContext):
        pass


    # Enter a parse tree produced by CnsMRParser#proton_shift_ring_atoms.
    def enterProton_shift_ring_atoms(self, ctx:CnsMRParser.Proton_shift_ring_atomsContext):
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_ring_atoms.
    def exitProton_shift_ring_atoms(self, ctx:CnsMRParser.Proton_shift_ring_atomsContext):
        pass


    # Enter a parse tree produced by CnsMRParser#proton_shift_alphas_and_amides.
    def enterProton_shift_alphas_and_amides(self, ctx:CnsMRParser.Proton_shift_alphas_and_amidesContext):
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_alphas_and_amides.
    def exitProton_shift_alphas_and_amides(self, ctx:CnsMRParser.Proton_shift_alphas_and_amidesContext):
        pass


    # Enter a parse tree produced by CnsMRParser#conformation_statement.
    def enterConformation_statement(self, ctx:CnsMRParser.Conformation_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#conformation_statement.
    def exitConformation_statement(self, ctx:CnsMRParser.Conformation_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#conf_assign.
    def enterConf_assign(self, ctx:CnsMRParser.Conf_assignContext):
        pass

    # Exit a parse tree produced by CnsMRParser#conf_assign.
    def exitConf_assign(self, ctx:CnsMRParser.Conf_assignContext):
        pass


    # Enter a parse tree produced by CnsMRParser#diffusion_statement.
    def enterDiffusion_statement(self, ctx:CnsMRParser.Diffusion_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#diffusion_statement.
    def exitDiffusion_statement(self, ctx:CnsMRParser.Diffusion_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#dani_assign.
    def enterDani_assign(self, ctx:CnsMRParser.Dani_assignContext):
        pass

    # Exit a parse tree produced by CnsMRParser#dani_assign.
    def exitDani_assign(self, ctx:CnsMRParser.Dani_assignContext):
        pass


    # Enter a parse tree produced by CnsMRParser#one_bond_coupling_statement.
    def enterOne_bond_coupling_statement(self, ctx:CnsMRParser.One_bond_coupling_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#one_bond_coupling_statement.
    def exitOne_bond_coupling_statement(self, ctx:CnsMRParser.One_bond_coupling_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#one_bond_assign.
    def enterOne_bond_assign(self, ctx:CnsMRParser.One_bond_assignContext):
        pass

    # Exit a parse tree produced by CnsMRParser#one_bond_assign.
    def exitOne_bond_assign(self, ctx:CnsMRParser.One_bond_assignContext):
        pass


    # Enter a parse tree produced by CnsMRParser#angle_db_statement.
    def enterAngle_db_statement(self, ctx:CnsMRParser.Angle_db_statementContext):
        pass

    # Exit a parse tree produced by CnsMRParser#angle_db_statement.
    def exitAngle_db_statement(self, ctx:CnsMRParser.Angle_db_statementContext):
        pass


    # Enter a parse tree produced by CnsMRParser#angle_db_assign.
    def enterAngle_db_assign(self, ctx:CnsMRParser.Angle_db_assignContext):
        pass

    # Exit a parse tree produced by CnsMRParser#angle_db_assign.
    def exitAngle_db_assign(self, ctx:CnsMRParser.Angle_db_assignContext):
        pass


    # Enter a parse tree produced by CnsMRParser#selection.
    def enterSelection(self, ctx:CnsMRParser.SelectionContext):
        pass

    # Exit a parse tree produced by CnsMRParser#selection.
    def exitSelection(self, ctx:CnsMRParser.SelectionContext):
        pass


    # Enter a parse tree produced by CnsMRParser#selection_expression.
    def enterSelection_expression(self, ctx:CnsMRParser.Selection_expressionContext):
        pass

    # Exit a parse tree produced by CnsMRParser#selection_expression.
    def exitSelection_expression(self, ctx:CnsMRParser.Selection_expressionContext):
        pass


    # Enter a parse tree produced by CnsMRParser#term.
    def enterTerm(self, ctx:CnsMRParser.TermContext):
        pass

    # Exit a parse tree produced by CnsMRParser#term.
    def exitTerm(self, ctx:CnsMRParser.TermContext):
        pass


    # Enter a parse tree produced by CnsMRParser#factor.
    def enterFactor(self, ctx:CnsMRParser.FactorContext):
        pass

    # Exit a parse tree produced by CnsMRParser#factor.
    def exitFactor(self, ctx:CnsMRParser.FactorContext):
        pass


    # Enter a parse tree produced by CnsMRParser#vector_3d.
    def enterVector_3d(self, ctx:CnsMRParser.Vector_3dContext):
        pass

    # Exit a parse tree produced by CnsMRParser#vector_3d.
    def exitVector_3d(self, ctx:CnsMRParser.Vector_3dContext):
        pass



del CnsMRParser