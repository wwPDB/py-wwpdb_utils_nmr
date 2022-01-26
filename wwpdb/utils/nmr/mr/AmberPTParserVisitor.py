# Generated from AmberPTParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AmberPTParser import AmberPTParser
else:
    from AmberPTParser import AmberPTParser

# This class defines a complete generic visitor for a parse tree produced by AmberPTParser.

class AmberPTParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AmberPTParser#amber_pt.
    def visitAmber_pt(self, ctx:AmberPTParser.Amber_ptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#version_statement.
    def visitVersion_statement(self, ctx:AmberPTParser.Version_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#amber_atom_type_statement.
    def visitAmber_atom_type_statement(self, ctx:AmberPTParser.Amber_atom_type_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#angle_equil_value_statement.
    def visitAngle_equil_value_statement(self, ctx:AmberPTParser.Angle_equil_value_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#angle_force_constant_statement.
    def visitAngle_force_constant_statement(self, ctx:AmberPTParser.Angle_force_constant_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#angles_inc_hydrogen_statement.
    def visitAngles_inc_hydrogen_statement(self, ctx:AmberPTParser.Angles_inc_hydrogen_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#angles_without_hydrogen_statement.
    def visitAngles_without_hydrogen_statement(self, ctx:AmberPTParser.Angles_without_hydrogen_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#atomic_number_statement.
    def visitAtomic_number_statement(self, ctx:AmberPTParser.Atomic_number_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#atom_name_statement.
    def visitAtom_name_statement(self, ctx:AmberPTParser.Atom_name_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#atom_type_index_statement.
    def visitAtom_type_index_statement(self, ctx:AmberPTParser.Atom_type_index_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#atoms_per_molecule_statement.
    def visitAtoms_per_molecule_statement(self, ctx:AmberPTParser.Atoms_per_molecule_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#bond_equil_value_statement.
    def visitBond_equil_value_statement(self, ctx:AmberPTParser.Bond_equil_value_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#bond_force_constant_statement.
    def visitBond_force_constant_statement(self, ctx:AmberPTParser.Bond_force_constant_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#bonds_inc_hydrogen_statement.
    def visitBonds_inc_hydrogen_statement(self, ctx:AmberPTParser.Bonds_inc_hydrogen_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#bonds_without_hydrogen_statement.
    def visitBonds_without_hydrogen_statement(self, ctx:AmberPTParser.Bonds_without_hydrogen_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#box_dimensions_statement.
    def visitBox_dimensions_statement(self, ctx:AmberPTParser.Box_dimensions_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#cap_info_statement.
    def visitCap_info_statement(self, ctx:AmberPTParser.Cap_info_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#cap_info2_statement.
    def visitCap_info2_statement(self, ctx:AmberPTParser.Cap_info2_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#charge_statement.
    def visitCharge_statement(self, ctx:AmberPTParser.Charge_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#dihedral_force_constant_statement.
    def visitDihedral_force_constant_statement(self, ctx:AmberPTParser.Dihedral_force_constant_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#dihedral_periodicity_statement.
    def visitDihedral_periodicity_statement(self, ctx:AmberPTParser.Dihedral_periodicity_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#dihedral_phase_statement.
    def visitDihedral_phase_statement(self, ctx:AmberPTParser.Dihedral_phase_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#dihedrals_inc_hydrogen_statement.
    def visitDihedrals_inc_hydrogen_statement(self, ctx:AmberPTParser.Dihedrals_inc_hydrogen_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#dihedrals_without_hydrogen_statement.
    def visitDihedrals_without_hydrogen_statement(self, ctx:AmberPTParser.Dihedrals_without_hydrogen_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#excluded_atoms_list_statement.
    def visitExcluded_atoms_list_statement(self, ctx:AmberPTParser.Excluded_atoms_list_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#hbcut_statement.
    def visitHbcut_statement(self, ctx:AmberPTParser.Hbcut_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#hbond_acoef_statement.
    def visitHbond_acoef_statement(self, ctx:AmberPTParser.Hbond_acoef_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#hbond_bcoef_statement.
    def visitHbond_bcoef_statement(self, ctx:AmberPTParser.Hbond_bcoef_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#ipol_statement.
    def visitIpol_statement(self, ctx:AmberPTParser.Ipol_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#irotat_statement.
    def visitIrotat_statement(self, ctx:AmberPTParser.Irotat_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#join_array_statement.
    def visitJoin_array_statement(self, ctx:AmberPTParser.Join_array_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#lennard_jones_acoef_statement.
    def visitLennard_jones_acoef_statement(self, ctx:AmberPTParser.Lennard_jones_acoef_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#lennard_jones_bcoef_statement.
    def visitLennard_jones_bcoef_statement(self, ctx:AmberPTParser.Lennard_jones_bcoef_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#mass_statement.
    def visitMass_statement(self, ctx:AmberPTParser.Mass_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#nonbonded_parm_index_statement.
    def visitNonbonded_parm_index_statement(self, ctx:AmberPTParser.Nonbonded_parm_index_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#number_excluded_atoms_statement.
    def visitNumber_excluded_atoms_statement(self, ctx:AmberPTParser.Number_excluded_atoms_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#pointers_statement.
    def visitPointers_statement(self, ctx:AmberPTParser.Pointers_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#polarizability_statement.
    def visitPolarizability_statement(self, ctx:AmberPTParser.Polarizability_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#radii_statement.
    def visitRadii_statement(self, ctx:AmberPTParser.Radii_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#radius_set_statement.
    def visitRadius_set_statement(self, ctx:AmberPTParser.Radius_set_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#residue_label_statement.
    def visitResidue_label_statement(self, ctx:AmberPTParser.Residue_label_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#residue_pointer_statement.
    def visitResidue_pointer_statement(self, ctx:AmberPTParser.Residue_pointer_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#scee_scale_factor_statement.
    def visitScee_scale_factor_statement(self, ctx:AmberPTParser.Scee_scale_factor_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#scnb_scale_factor_statement.
    def visitScnb_scale_factor_statement(self, ctx:AmberPTParser.Scnb_scale_factor_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#screen_statement.
    def visitScreen_statement(self, ctx:AmberPTParser.Screen_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#solty_statement.
    def visitSolty_statement(self, ctx:AmberPTParser.Solty_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#solvent_pointers_statement.
    def visitSolvent_pointers_statement(self, ctx:AmberPTParser.Solvent_pointers_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#title_statement.
    def visitTitle_statement(self, ctx:AmberPTParser.Title_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#tree_chain_classification_statement.
    def visitTree_chain_classification_statement(self, ctx:AmberPTParser.Tree_chain_classification_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#string_format_statement.
    def visitString_format_statement(self, ctx:AmberPTParser.String_format_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#string4_format_statement.
    def visitString4_format_statement(self, ctx:AmberPTParser.String4_format_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#integer_format_statement.
    def visitInteger_format_statement(self, ctx:AmberPTParser.Integer_format_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#real_format_statement.
    def visitReal_format_statement(self, ctx:AmberPTParser.Real_format_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#float_format_statement.
    def visitFloat_format_statement(self, ctx:AmberPTParser.Float_format_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#simple_name_array.
    def visitSimple_name_array(self, ctx:AmberPTParser.Simple_name_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#line_string_array.
    def visitLine_string_array(self, ctx:AmberPTParser.Line_string_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#integer_array.
    def visitInteger_array(self, ctx:AmberPTParser.Integer_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#float_array.
    def visitFloat_array(self, ctx:AmberPTParser.Float_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmberPTParser#real_array.
    def visitReal_array(self, ctx:AmberPTParser.Real_arrayContext):
        return self.visitChildren(ctx)



del AmberPTParser