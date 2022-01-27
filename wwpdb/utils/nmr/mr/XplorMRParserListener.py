##
# File: XplorMRParserListener.py
# Date: 27-Jan-2022
#
# Updates:
# Generated from XplorMRParser.g4 by ANTLR 4.9
""" ParserLister class for XPLOR-NIH MR files.
    @author: Masashi Yokochi
"""
from antlr4 import ParseTreeListener

from wwpdb.utils.nmr.mr.XplorMRParser import XplorMRParser


# This class defines a complete listener for a parse tree produced by XplorMRParser.
class XplorMRParserListener(ParseTreeListener):

    distRestraints = 0      # XPLOR-NIH: Distance restraints
    dihedRestraints = 0     # XPLOR-NIH: Dihedral angle restraints
    rdcRestraints = 0       # XPLOR-NIH: Residual Dipolar Couplings
    planeRestraints = 0     # XPLOR-NIH: Planality restraints
    adistRestraints = 0     # XPLOR-NIH: Antidiatance restraints
    jcoupRestraints = 0     # XPLOR-NIH: Scalar J-coupling restraints
    hvycsRestraints = 0     # XPLOR-NIH: Carbon chemical shift restraints
    procsRestraints = 0     # XPLOR-NIH: Proton chemical shift restraints
    ramaRestraints = 0      # XPLOR-NIH: Dihedral angle database restraints
    radiRestraints = 0      # XPLOR-NIH: Radius of gyration restraints
    diffRestraints = 0      # XPLOR-NIH: Diffusion anisotropy restraints
    nbaseRestraints = 0     # XPLOR-NIH: Residue-residue position/orientation database restraints
    csaRestraints = 0       # XPLOR-NIH: (Pseudo) Chemical shift anisotropy restraints
    angRestraints = 0       # XPLOR-NIH: Angle database restraints
    preRestraints = 0       # XPLOR-NIH: Paramagnetic relaxation enhancement restraints
    pcsRestraints = 0       # XPLOR-NIH: Paramagnetic pseudocontact shift restraints
    prdcRestraints = 0      # XPLOR-NIH: Paramagnetic residual dipolar coupling restraints
    pangRestraints = 0      # XPLOR-NIH: Paramagnetic orientation restraints
    pccrRestraints = 0      # XPLOR-NIH: Paramagnetic cross-correlation rate restraints
    hbondRestraints = 0     # XPLOR-NIH: Hydrogen bond geometry restraints

    distStatements = 0      # XPLOR-NIH: Distance restraints
    dihedStatements = 0     # XPLOR-NIH: Dihedral angle restraints
    rdcStatements = 0       # XPLOR-NIH: Residual Dipolar Couplings
    planeStatements = 0     # XPLOR-NIH: Planality restraints
    adistStatements = 0     # XPLOR-NIH: Antidiatance restraints
    jcoupStatements = 0     # XPLOR-NIH: Scalar J-coupling restraints
    hvycsStatements = 0     # XPLOR-NIH: Carbon chemical shift restraints
    procsStatements = 0     # XPLOR-NIH: Proton chemical shift restraints
    ramaStatements = 0      # XPLOR-NIH: Dihedral angle database restraints
    radiStatements = 0      # XPLOR-NIH: Radius of gyration restraints
    diffStatements = 0      # XPLOR-NIH: Diffusion anisotropy restraints
    nbaseStatements = 0     # XPLOR-NIH: Residue-residue position/orientation database restraints
    csaStatements = 0       # XPLOR-NIH: (Pseudo) Chemical shift anisotropy restraints
    angStatements = 0       # XPLOR-NIH: Angle database restraints
    preStatements = 0       # XPLOR-NIH: Paramagnetic relaxation enhancement restraints
    pcsStatements = 0       # XPLOR-NIH: Paramagnetic pseudocontact shift restraints
    prdcStatements = 0      # XPLOR-NIH: Paramagnetic residual dipolar coupling restraints
    pangStatements = 0      # XPLOR-NIH: Paramagnetic orientation restraints
    pccrStatements = 0      # XPLOR-NIH: Paramagnetic cross-correlation rate restraints
    hbondStatements = 0     # XPLOR-NIH: Hydrogen bond geometry restraints

    # Enter a parse tree produced by XplorMRParser#xplor_nih_mr.
    def enterXplor_nih_mr(self, ctx: XplorMRParser.Xplor_nih_mrContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#xplor_nih_mr.
    def exitXplor_nih_mr(self, ctx: XplorMRParser.Xplor_nih_mrContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#distance_restraint.
    def enterDistance_restraint(self, ctx: XplorMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        self.distStatements += 1

    # Exit a parse tree produced by XplorMRParser#distance_restraint.
    def exitDistance_restraint(self, ctx: XplorMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dihedral_angle_restraint.
    def enterDihedral_angle_restraint(self, ctx: XplorMRParser.Dihedral_angle_restraintContext):  # pylint: disable=unused-argument
        self.dihedStatements += 1

    # Exit a parse tree produced by XplorMRParser#dihedral_angle_restraint.
    def exitDihedral_angle_restraint(self, ctx: XplorMRParser.Dihedral_angle_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#rdc_restraint.
    def enterRdc_restraint(self, ctx: XplorMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        self.rdcStatements += 1

    # Exit a parse tree produced by XplorMRParser#rdc_restraint.
    def exitRdc_restraint(self, ctx: XplorMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#planar_restraint.
    def enterPlanar_restraint(self, ctx: XplorMRParser.Planar_restraintContext):  # pylint: disable=unused-argument
        self.planeStatements += 1

    # Exit a parse tree produced by XplorMRParser#planar_restraint.
    def exitPlanar_restraint(self, ctx: XplorMRParser.Planar_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#antidistance_restraint.
    def enterAntidistance_restraint(self, ctx: XplorMRParser.Antidistance_restraintContext):  # pylint: disable=unused-argument
        self.adistStatements += 1

    # Exit a parse tree produced by XplorMRParser#antidistance_restraint.
    def exitAntidistance_restraint(self, ctx: XplorMRParser.Antidistance_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#coupling_restraint.
    def enterCoupling_restraint(self, ctx: XplorMRParser.Coupling_restraintContext):  # pylint: disable=unused-argument
        self.jcoupStatements += 1

    # Exit a parse tree produced by XplorMRParser#coupling_restraint.
    def exitCoupling_restraint(self, ctx: XplorMRParser.Coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#carbon_shift_restraint.
    def enterCarbon_shift_restraint(self, ctx: XplorMRParser.Carbon_shift_restraintContext):  # pylint: disable=unused-argument
        self.hvycsStatements += 1

    # Exit a parse tree produced by XplorMRParser#carbon_shift_restraint.
    def exitCarbon_shift_restraint(self, ctx: XplorMRParser.Carbon_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_restraint.
    def enterProton_shift_restraint(self, ctx: XplorMRParser.Proton_shift_restraintContext):  # pylint: disable=unused-argument
        self.procsStatements += 1

    # Exit a parse tree produced by XplorMRParser#proton_shift_restraint.
    def exitProton_shift_restraint(self, ctx: XplorMRParser.Proton_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dihedral_angle_db_restraint.
    def enterDihedral_angle_db_restraint(self, ctx: XplorMRParser.Dihedral_angle_db_restraintContext):  # pylint: disable=unused-argument
        self.angStatements += 1

    # Exit a parse tree produced by XplorMRParser#dihedral_angle_db_restraint.
    def exitDihedral_angle_db_restraint(self, ctx: XplorMRParser.Dihedral_angle_db_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#radius_of_gyration_restraint.
    def enterRadius_of_gyration_restraint(self, ctx: XplorMRParser.Radius_of_gyration_restraintContext):  # pylint: disable=unused-argument
        self.radiStatements += 1

    # Exit a parse tree produced by XplorMRParser#radius_of_gyration_restraint.
    def exitRadius_of_gyration_restraint(self, ctx: XplorMRParser.Radius_of_gyration_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#diffusion_anisotropy_restraint.
    def enterDiffusion_anisotropy_restraint(self, ctx: XplorMRParser.Diffusion_anisotropy_restraintContext):  # pylint: disable=unused-argument
        self.diffStatements += 1

    # Exit a parse tree produced by XplorMRParser#diffusion_anisotropy_restraint.
    def exitDiffusion_anisotropy_restraint(self, ctx: XplorMRParser.Diffusion_anisotropy_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#orientation_db_restraint.
    def enterOrientation_db_restraint(self, ctx: XplorMRParser.Orientation_db_restraintContext):  # pylint: disable=unused-argument
        self.nbaseStatements += 1

    # Exit a parse tree produced by XplorMRParser#orientation_db_restraint.
    def exitOrientation_db_restraint(self, ctx: XplorMRParser.Orientation_db_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#csa_restraint.
    def enterCsa_restraint(self, ctx: XplorMRParser.Csa_restraintContext):  # pylint: disable=unused-argument
        self.csaStatements += 1  # either CSA or pseudo CSA

    # Exit a parse tree produced by XplorMRParser#csa_restraint.
    def exitCsa_restraint(self, ctx: XplorMRParser.Csa_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pcsa_restraint.
    def enterPcsa_restraint(self, ctx: XplorMRParser.Pcsa_restraintContext):  # pylint: disable=unused-argument
        self.csaStatements += 1  # either CSA or pseudo CSA

    # Exit a parse tree produced by XplorMRParser#pcsa_restraint.
    def exitPcsa_restraint(self, ctx: XplorMRParser.Pcsa_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#one_bond_coupling_restraint.
    def enterOne_bond_coupling_restraint(self, ctx: XplorMRParser.One_bond_coupling_restraintContext):  # pylint: disable=unused-argument
        """
        @deprecated: This restraint has not been useful in practice, but has been preserved for historical reasons.
        """

    # Exit a parse tree produced by XplorMRParser#one_bond_coupling_restraint.
    def exitOne_bond_coupling_restraint(self, ctx: XplorMRParser.One_bond_coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#angle_db_restraint.
    def enterAngle_db_restraint(self, ctx: XplorMRParser.Angle_db_restraintContext):  # pylint: disable=unused-argument
        self.angStatements += 1

    # Exit a parse tree produced by XplorMRParser#angle_db_restraint.
    def exitAngle_db_restraint(self, ctx: XplorMRParser.Angle_db_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pre_restraint.
    def enterPre_restraint(self, ctx: XplorMRParser.Pre_restraintContext):  # pylint: disable=unused-argument
        self.preStatements += 1

    # Exit a parse tree produced by XplorMRParser#pre_restraint.
    def exitPre_restraint(self, ctx: XplorMRParser.Pre_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pcs_restraint.
    def enterPcs_restraint(self, ctx: XplorMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        self.pcsStatements += 1

    # Exit a parse tree produced by XplorMRParser#pcs_restraint.
    def exitPcs_restraint(self, ctx: XplorMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#prdc_restraint.
    def enterPrdc_restraint(self, ctx: XplorMRParser.Prdc_restraintContext):  # pylint: disable=unused-argument
        self.prdcStatements += 1

    # Exit a parse tree produced by XplorMRParser#prdc_restraint.
    def exitPrdc_restraint(self, ctx: XplorMRParser.Prdc_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#porientation_restraint.
    def enterPorientation_restraint(self, ctx: XplorMRParser.Porientation_restraintContext):  # pylint: disable=unused-argument
        self.prdcStatements += 1

    # Exit a parse tree produced by XplorMRParser#porientation_restraint.
    def exitPorientation_restraint(self, ctx: XplorMRParser.Porientation_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pccr_restraint.
    def enterPccr_restraint(self, ctx: XplorMRParser.Pccr_restraintContext):  # pylint: disable=unused-argument
        self.pccrStatements += 1

    # Exit a parse tree produced by XplorMRParser#pccr_restraint.
    def exitPccr_restraint(self, ctx: XplorMRParser.Pccr_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#hbond_restraint.
    def enterHbond_restraint(self, ctx: XplorMRParser.Hbond_restraintContext):  # pylint: disable=unused-argument
        self.hbondStatements += 1

    # Exit a parse tree produced by XplorMRParser#hbond_restraint.
    def exitHbond_restraint(self, ctx: XplorMRParser.Hbond_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#noe_statement.
    def enterNoe_statement(self, ctx: XplorMRParser.Noe_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#noe_statement.
    def exitNoe_statement(self, ctx: XplorMRParser.Noe_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#noe_assign.
    def enterNoe_assign(self, ctx: XplorMRParser.Noe_assignContext):  # pylint: disable=unused-argument
        self.distRestraints += 1

    # Exit a parse tree produced by XplorMRParser#noe_assign.
    def exitNoe_assign(self, ctx: XplorMRParser.Noe_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#predict_statement.
    def enterPredict_statement(self, ctx: XplorMRParser.Predict_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#predict_statement.
    def exitPredict_statement(self, ctx: XplorMRParser.Predict_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dihedral_statement.
    def enterDihedral_statement(self, ctx: XplorMRParser.Dihedral_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#dihedral_statement.
    def exitDihedral_statement(self, ctx: XplorMRParser.Dihedral_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dihedral_assign.
    def enterDihedral_assign(self, ctx: XplorMRParser.Dihedral_assignContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

    # Exit a parse tree produced by XplorMRParser#dihedral_assign.
    def exitDihedral_assign(self, ctx: XplorMRParser.Dihedral_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#sani_statement.
    def enterSani_statement(self, ctx: XplorMRParser.Sani_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#sani_statement.
    def exitSani_statement(self, ctx: XplorMRParser.Sani_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#sani_assign.
    def enterSani_assign(self, ctx: XplorMRParser.Sani_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

    # Exit a parse tree produced by XplorMRParser#sani_assign.
    def exitSani_assign(self, ctx: XplorMRParser.Sani_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#xdip_statement.
    def enterXdip_statement(self, ctx: XplorMRParser.Xdip_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#xdip_statement.
    def exitXdip_statement(self, ctx: XplorMRParser.Xdip_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#xdip_assign.
    def enterXdip_assign(self, ctx: XplorMRParser.Xdip_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

    # Exit a parse tree produced by XplorMRParser#xdip_assign.
    def exitXdip_assign(self, ctx: XplorMRParser.Xdip_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#vean_statement.
    def enterVean_statement(self, ctx: XplorMRParser.Vean_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#vean_statement.
    def exitVean_statement(self, ctx: XplorMRParser.Vean_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#vean_assign.
    def enterVean_assign(self, ctx: XplorMRParser.Vean_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

    # Exit a parse tree produced by XplorMRParser#vean_assign.
    def exitVean_assign(self, ctx: XplorMRParser.Vean_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#tens_statement.
    def enterTens_statement(self, ctx: XplorMRParser.Tens_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#tens_statement.
    def exitTens_statement(self, ctx: XplorMRParser.Tens_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#tens_assign.
    def enterTens_assign(self, ctx: XplorMRParser.Tens_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

    # Exit a parse tree produced by XplorMRParser#tens_assign.
    def exitTens_assign(self, ctx: XplorMRParser.Tens_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#anis_statement.
    def enterAnis_statement(self, ctx: XplorMRParser.Anis_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#anis_statement.
    def exitAnis_statement(self, ctx: XplorMRParser.Anis_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#anis_assign.
    def enterAnis_assign(self, ctx: XplorMRParser.Anis_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

    # Exit a parse tree produced by XplorMRParser#anis_assign.
    def exitAnis_assign(self, ctx: XplorMRParser.Anis_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#planar_statement.
    def enterPlanar_statement(self, ctx: XplorMRParser.Planar_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#planar_statement.
    def exitPlanar_statement(self, ctx: XplorMRParser.Planar_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#group_statement.
    def enterGroup_statement(self, ctx: XplorMRParser.Group_statementContext):  # pylint: disable=unused-argument
        self.planeRestraints += 1

    # Exit a parse tree produced by XplorMRParser#group_statement.
    def exitGroup_statement(self, ctx: XplorMRParser.Group_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#antidistance_statement.
    def enterAntidistance_statement(self, ctx: XplorMRParser.Antidistance_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#antidistance_statement.
    def exitAntidistance_statement(self, ctx: XplorMRParser.Antidistance_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#xadc_assign.
    def enterXadc_assign(self, ctx: XplorMRParser.Xadc_assignContext):  # pylint: disable=unused-argument
        self.adistRestraints += 1

    # Exit a parse tree produced by XplorMRParser#xadc_assign.
    def exitXadc_assign(self, ctx: XplorMRParser.Xadc_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#coupling_statement.
    def enterCoupling_statement(self, ctx: XplorMRParser.Coupling_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#coupling_statement.
    def exitCoupling_statement(self, ctx: XplorMRParser.Coupling_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#coup_assign.
    def enterCoup_assign(self, ctx: XplorMRParser.Coup_assignContext):  # pylint: disable=unused-argument
        self.jcoupRestraints += 1

    # Exit a parse tree produced by XplorMRParser#coup_assign.
    def exitCoup_assign(self, ctx: XplorMRParser.Coup_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#carbon_shift_statement.
    def enterCarbon_shift_statement(self, ctx: XplorMRParser.Carbon_shift_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#carbon_shift_statement.
    def exitCarbon_shift_statement(self, ctx: XplorMRParser.Carbon_shift_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#carbon_shift_assign.
    def enterCarbon_shift_assign(self, ctx: XplorMRParser.Carbon_shift_assignContext):  # pylint: disable=unused-argument
        self.hvycsRestraints += 1

    # Exit a parse tree produced by XplorMRParser#carbon_shift_assign.
    def exitCarbon_shift_assign(self, ctx: XplorMRParser.Carbon_shift_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#carbon_shift_rcoil.
    def enterCarbon_shift_rcoil(self, ctx: XplorMRParser.Carbon_shift_rcoilContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#carbon_shift_rcoil.
    def exitCarbon_shift_rcoil(self, ctx: XplorMRParser.Carbon_shift_rcoilContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_statement.
    def enterProton_shift_statement(self, ctx: XplorMRParser.Proton_shift_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_statement.
    def exitProton_shift_statement(self, ctx: XplorMRParser.Proton_shift_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#observed.
    def enterObserved(self, ctx: XplorMRParser.ObservedContext):  # pylint: disable=unused-argument
        self.procsRestraints += 1

    # Exit a parse tree produced by XplorMRParser#observed.
    def exitObserved(self, ctx: XplorMRParser.ObservedContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_rcoil.
    def enterProton_shift_rcoil(self, ctx: XplorMRParser.Proton_shift_rcoilContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_rcoil.
    def exitProton_shift_rcoil(self, ctx: XplorMRParser.Proton_shift_rcoilContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_anisotropy.
    def enterProton_shift_anisotropy(self, ctx: XplorMRParser.Proton_shift_anisotropyContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_anisotropy.
    def exitProton_shift_anisotropy(self, ctx: XplorMRParser.Proton_shift_anisotropyContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_amides.
    def enterProton_shift_amides(self, ctx: XplorMRParser.Proton_shift_amidesContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_amides.
    def exitProton_shift_amides(self, ctx: XplorMRParser.Proton_shift_amidesContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_carbons.
    def enterProton_shift_carbons(self, ctx: XplorMRParser.Proton_shift_carbonsContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_carbons.
    def exitProton_shift_carbons(self, ctx: XplorMRParser.Proton_shift_carbonsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_nitrogens.
    def enterProton_shift_nitrogens(self, ctx: XplorMRParser.Proton_shift_nitrogensContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_nitrogens.
    def exitProton_shift_nitrogens(self, ctx: XplorMRParser.Proton_shift_nitrogensContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_oxygens.
    def enterProton_shift_oxygens(self, ctx: XplorMRParser.Proton_shift_oxygensContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_oxygens.
    def exitProton_shift_oxygens(self, ctx: XplorMRParser.Proton_shift_oxygensContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_ring_atoms.
    def enterProton_shift_ring_atoms(self, ctx: XplorMRParser.Proton_shift_ring_atomsContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_ring_atoms.
    def exitProton_shift_ring_atoms(self, ctx: XplorMRParser.Proton_shift_ring_atomsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_alphas_and_amides.
    def enterProton_shift_alphas_and_amides(self, ctx: XplorMRParser.Proton_shift_alphas_and_amidesContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_alphas_and_amides.
    def exitProton_shift_alphas_and_amides(self, ctx: XplorMRParser.Proton_shift_alphas_and_amidesContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#ramachandran_statement.
    def enterRamachandran_statement(self, ctx: XplorMRParser.Ramachandran_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#ramachandran_statement.
    def exitRamachandran_statement(self, ctx: XplorMRParser.Ramachandran_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#rama_assign.
    def enterRama_assign(self, ctx: XplorMRParser.Rama_assignContext):  # pylint: disable=unused-argument
        self.ramaRestraints += 1

    # Exit a parse tree produced by XplorMRParser#rama_assign.
    def exitRama_assign(self, ctx: XplorMRParser.Rama_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#collapse_statement.
    def enterCollapse_statement(self, ctx: XplorMRParser.Collapse_statementContext):  # pylint: disable=unused-argument
        self.radiRestraints += 1

    # Exit a parse tree produced by XplorMRParser#collapse_statement.
    def exitCollapse_statement(self, ctx: XplorMRParser.Collapse_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#diffusion_statement.
    def enterDiffusion_statement(self, ctx: XplorMRParser.Diffusion_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#diffusion_statement.
    def exitDiffusion_statement(self, ctx: XplorMRParser.Diffusion_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dani_assign.
    def enterDani_assign(self, ctx: XplorMRParser.Dani_assignContext):  # pylint: disable=unused-argument
        self.diffRestraints += 1

    # Exit a parse tree produced by XplorMRParser#dani_assign.
    def exitDani_assign(self, ctx: XplorMRParser.Dani_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#orientation_statement.
    def enterOrientation_statement(self, ctx: XplorMRParser.Orientation_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#orientation_statement.
    def exitOrientation_statement(self, ctx: XplorMRParser.Orientation_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#orie_assign.
    def enterOrie_assign(self, ctx: XplorMRParser.Orie_assignContext):  # pylint: disable=unused-argument
        self.nbaseRestraints += 1

    # Exit a parse tree produced by XplorMRParser#orie_assign.
    def exitOrie_assign(self, ctx: XplorMRParser.Orie_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#csa_statement.
    def enterCsa_statement(self, ctx: XplorMRParser.Csa_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#csa_statement.
    def exitCsa_statement(self, ctx: XplorMRParser.Csa_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#csa_assign.
    def enterCsa_assign(self, ctx: XplorMRParser.Csa_assignContext):  # pylint: disable=unused-argument
        self.csaRestraints += 1

    # Exit a parse tree produced by XplorMRParser#csa_assign.
    def exitCsa_assign(self, ctx: XplorMRParser.Csa_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pcsa_statement.
    def enterPcsa_statement(self, ctx: XplorMRParser.Pcsa_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#pcsa_statement.
    def exitPcsa_statement(self, ctx: XplorMRParser.Pcsa_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#one_bond_coupling_statement.
    def enterOne_bond_coupling_statement(self, ctx: XplorMRParser.One_bond_coupling_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#one_bond_coupling_statement.
    def exitOne_bond_coupling_statement(self, ctx: XplorMRParser.One_bond_coupling_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#one_bond_assign.
    def enterOne_bond_assign(self, ctx: XplorMRParser.One_bond_assignContext):  # pylint: disable=unused-argument
        """
        @deprecated: This restraint has not been useful in practice, but has been preserved for historical reasons.
        """

    # Exit a parse tree produced by XplorMRParser#one_bond_assign.
    def exitOne_bond_assign(self, ctx: XplorMRParser.One_bond_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#angle_db_statement.
    def enterAngle_db_statement(self, ctx: XplorMRParser.Angle_db_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#angle_db_statement.
    def exitAngle_db_statement(self, ctx: XplorMRParser.Angle_db_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#angle_db_assign.
    def enterAngle_db_assign(self, ctx: XplorMRParser.Angle_db_assignContext):  # pylint: disable=unused-argument
        self.angRestraints += 1

    # Exit a parse tree produced by XplorMRParser#angle_db_assign.
    def exitAngle_db_assign(self, ctx: XplorMRParser.Angle_db_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pre_statement.
    def enterPre_statement(self, ctx: XplorMRParser.Pre_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#pre_statement.
    def exitPre_statement(self, ctx: XplorMRParser.Pre_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pre_assign.
    def enterPre_assign(self, ctx: XplorMRParser.Pre_assignContext):  # pylint: disable=unused-argument
        self.preRestraints += 1

    # Exit a parse tree produced by XplorMRParser#pre_assign.
    def exitPre_assign(self, ctx: XplorMRParser.Pre_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pcs_statement.
    def enterPcs_statement(self, ctx: XplorMRParser.Pcs_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#pcs_statement.
    def exitPcs_statement(self, ctx: XplorMRParser.Pcs_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pcs_assign.
    def enterPcs_assign(self, ctx: XplorMRParser.Pcs_assignContext):  # pylint: disable=unused-argument
        self.pcsRestraints += 1

    # Exit a parse tree produced by XplorMRParser#pcs_assign.
    def exitPcs_assign(self, ctx: XplorMRParser.Pcs_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#prdc_statement.
    def enterPrdc_statement(self, ctx: XplorMRParser.Prdc_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#prdc_statement.
    def exitPrdc_statement(self, ctx: XplorMRParser.Prdc_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#prdc_assign.
    def enterPrdc_assign(self, ctx: XplorMRParser.Prdc_assignContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#prdc_assign.
    def exitPrdc_assign(self, ctx: XplorMRParser.Prdc_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#porientation_statement.
    def enterPorientation_statement(self, ctx: XplorMRParser.Porientation_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#porientation_statement.
    def exitPorientation_statement(self, ctx: XplorMRParser.Porientation_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#porientation_assign.
    def enterPorientation_assign(self, ctx: XplorMRParser.Porientation_assignContext):  # pylint: disable=unused-argument
        self.pangRestraints += 1

    # Exit a parse tree produced by XplorMRParser#porientation_assign.
    def exitPorientation_assign(self, ctx: XplorMRParser.Porientation_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pccr_statement.
    def enterPccr_statement(self, ctx: XplorMRParser.Pccr_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#pccr_statement.
    def exitPccr_statement(self, ctx: XplorMRParser.Pccr_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pccr_assign.
    def enterPccr_assign(self, ctx: XplorMRParser.Pccr_assignContext):  # pylint: disable=unused-argument
        self.pccrRestraints += 1

    # Exit a parse tree produced by XplorMRParser#pccr_assign.
    def exitPccr_assign(self, ctx: XplorMRParser.Pccr_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#hbond_statement.
    def enterHbond_statement(self, ctx: XplorMRParser.Hbond_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#hbond_statement.
    def exitHbond_statement(self, ctx: XplorMRParser.Hbond_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#hbond_assign.
    def enterHbond_assign(self, ctx: XplorMRParser.Hbond_assignContext):  # pylint: disable=unused-argument
        self.hbondRestraints += 1

    # Exit a parse tree produced by XplorMRParser#hbond_assign.
    def exitHbond_assign(self, ctx: XplorMRParser.Hbond_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#selection.
    def enterSelection(self, ctx: XplorMRParser.SelectionContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#selection.
    def exitSelection(self, ctx: XplorMRParser.SelectionContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#selection_expression.
    def enterSelection_expression(self, ctx: XplorMRParser.Selection_expressionContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#selection_expression.
    def exitSelection_expression(self, ctx: XplorMRParser.Selection_expressionContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#term.
    def enterTerm(self, ctx: XplorMRParser.TermContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#term.
    def exitTerm(self, ctx: XplorMRParser.TermContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#factor.
    def enterFactor(self, ctx: XplorMRParser.FactorContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#factor.
    def exitFactor(self, ctx: XplorMRParser.FactorContext):  # pylint: disable=unused-argument
        # """
        # if ctx.Name():  # pylint: disable=unused-argument
        #     print(f"name={ctx.Simple_name(0)}")
        # if ctx.Residue():  # pylint: disable=unused-argument
        #     print(f"resid={ctx.Integer(0)}")
        # if ctx.SegIdentifier():  # pylint: disable=unused-argument
        #     print(f"segid={ctx.Simple_name(0)}")
        # """
        pass

    # Enter a parse tree produced by XplorMRParser#vector_3d.
    def enterVector_3d(self, ctx: XplorMRParser.Vector_3dContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#vector_3d.
    def exitVector_3d(self, ctx: XplorMRParser.Vector_3dContext):  # pylint: disable=unused-argument
        pass

    # The followings are extensions.
    def getContentSubtype(self):
        """ Return content subtype of XPLOR-NIH MR file.
        """

        if self.distStatements == 0 and self.distRestraints > 0:
            self.distStatements = 1

        if self.dihedStatements == 0 and self.dihedRestraints > 0:
            self.dihedStatements = 1

        if self.rdcStatements == 0 and self.rdcRestraints > 0:
            self.rdcStatements = 1

        if self.planeStatements == 0 and self.planeRestraints > 0:
            self.planeStatements = 1

        if self.adistStatements == 0 and self.adistRestraints > 0:
            self.adistStatements = 1

        if self.jcoupStatements == 0 and self.jcoupRestraints > 0:
            self.jcoupStatements = 1

        if self.hvycsStatements == 0 and self.hvycsRestraints > 0:
            self.hvycsStatements = 1

        if self.procsStatements == 0 and self.procsRestraints > 0:
            self.procsStatements = 1

        if self.ramaStatements == 0 and self.ramaRestraints > 0:
            self.ramaStatements = 1

        if self.radiStatements == 0 and self.radiRestraints > 0:
            self.radiStatements = 1

        if self.diffStatements == 0 and self.diffRestraints > 0:
            self.diffStatements = 1

        if self.nbaseStatements == 0 and self.nbaseRestraints > 0:
            self.nbaseStatements = 1

        if self.csaStatements == 0 and self.csaRestraints > 0:
            self.csaStatements = 1

        if self.angStatements == 0 and self.angRestraints > 0:
            self.angStatements = 1

        if self.preStatements == 0 and self.preRestraints > 0:
            self.preStatements = 1

        if self.pcsStatements == 0 and self.pcsRestraints > 0:
            self.pcsStatements = 1

        if self.prdcStatements == 0 and self.prdcRestraints > 0:
            self.prdcStatements = 1

        if self.pangStatements == 0 and self.pangRestraints > 0:
            self.pangStatements = 1

        if self.pccrStatements == 0 and self.pccrRestraints > 0:
            self.pccrStatements = 1

        if self.hbondStatements == 0 and self.hbondRestraints > 0:
            self.hbondStatements = 1

        content_subtype = {'dist_restraint': self.distStatements,
                           'dihed_restraint': self.dihedStatements,
                           'rdc_restraint': self.rdcStatements,
                           'plane_restraint': self.planeStatements,
                           'adist_restraint': self.adistStatements,
                           'jcoup_restraint': self.jcoupStatements,
                           'hvycs_restraint': self.hvycsStatements,
                           'procs_restraint': self.procsStatements,
                           'rama_restraint': self.ramaStatements,
                           'radi_restraint': self.radiStatements,
                           'diff_restraint': self.diffStatements,
                           'nbase_restraint': self.nbaseStatements,
                           'csa_restraint': self.csaStatements,
                           'ang_restraint': self.angStatements,
                           'pre_restraint': self.preStatements,
                           'pcs_restraint': self.pcsStatements,
                           'prdc_restraint': self.prdcStatements,
                           'pang_restraint': self.pangStatements,
                           'pccr_restraint': self.pccrStatements,
                           'hbond_restraint': self.hbondStatements
                           }

        return {k: v for k, v in content_subtype.items() if v > 0}

# del XplorMRParser
