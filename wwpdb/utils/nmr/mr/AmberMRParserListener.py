##
# File: AmberMRParserListener.py
# Date: 27-Jan-2022
#
# Updates:
# Generated from AmberMRParser.g4 by ANTLR 4.9
""" ParserLister class for AMBER MR files.
    @author: Masashi Yokochi
"""
from antlr4 import ParseTreeListener

from wwpdb.utils.nmr.mr.AmberMRParser import AmberMRParser


# This class defines a complete listener for a parse tree produced by AmberMRParser.
class AmberMRParserListener(ParseTreeListener):

    distRestraints = 0      # AMBER: Distance restraints
    angRestraints = 0       # AMBER: Angle restraints
    dihedRestraints = 0     # AMBER: Torsional restraints
    planeRestraints = 0     # AMBER: Plane-point/plane angle restraints
    noepkRestraints = 0     # AMBER: NOESY volume restraints
    hvycsRestraints = 0     # AMBER: Chemical shift restraints
    pcsRestraints = 0       # AMBER: Psuedocontact shift restraints
    rdcRestraints = 0       # AMBER: Direct dipolar coupling restraints
    csaRestraints = 0       # AMBER: Residual CSA or pseudo-CSA restraints

    # current restraint subtype
    __cur_subtype = None

    # collection of atom selection
    atomSelectionSet = None

    warningMessage = ''

    # Enter a parse tree produced by AmberMRParser#amber_mr.
    def enterAmber_mr(self, ctx: AmberMRParser.Amber_mrContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#amber_mr.
    def exitAmber_mr(self, ctx: AmberMRParser.Amber_mrContext):  # pylint: disable=unused-argument
        if len(self.warningMessage) == 0:
            self.warningMessage = None
        else:
            self.warningMessage = self.warningMessage[0:-1]
            self.warningMessage = '\n'.join(set(self.warningMessage.split('\n')))

    # Enter a parse tree produced by AmberMRParser#nmr_restraint.
    def enterNmr_restraint(self, ctx: AmberMRParser.Nmr_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#nmr_restraint.
    def exitNmr_restraint(self, ctx: AmberMRParser.Nmr_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#noesy_volume_restraint.
    def enterNoesy_volume_restraint(self, ctx: AmberMRParser.Noesy_volume_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#noesy_volume_restraint.
    def exitNoesy_volume_restraint(self, ctx: AmberMRParser.Noesy_volume_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#chemical_shift_restraint.
    def enterChemical_shift_restraint(self, ctx: AmberMRParser.Chemical_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#chemical_shift_restraint.
    def exitChemical_shift_restraint(self, ctx: AmberMRParser.Chemical_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#pcs_restraint.
    def enterPcs_restraint(self, ctx: AmberMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#pcs_restraint.
    def exitPcs_restraint(self, ctx: AmberMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#dipolar_coupling_restraint.
    def enterDipolar_coupling_restraint(self, ctx: AmberMRParser.Dipolar_coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#dipolar_coupling_restraint.
    def exitDipolar_coupling_restraint(self, ctx: AmberMRParser.Dipolar_coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#csa_restraint.
    def enterCsa_restraint(self, ctx: AmberMRParser.Csa_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#csa_restraint.
    def exitCsa_restraint(self, ctx: AmberMRParser.Csa_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#restraint_statement.
    def enterRestraint_statement(self, ctx: AmberMRParser.Restraint_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#restraint_statement.
    def exitRestraint_statement(self, ctx: AmberMRParser.Restraint_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#distance_statement.
    def enterDistance_statement(self, ctx: AmberMRParser.Distance_statementContext):  # pylint: disable=unused-argument
        self.distRestraints += 1
        self.__cur_subtype = 'dist'

    # Exit a parse tree produced by AmberMRParser#distance_statement.
    def exitDistance_statement(self, ctx: AmberMRParser.Distance_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#angle_statement.
    def enterAngle_statement(self, ctx: AmberMRParser.Angle_statementContext):  # pylint: disable=unused-argument
        self.angRestraints += 1
        self.__cur_subtype = 'ang'

    # Exit a parse tree produced by AmberMRParser#angle_statement.
    def exitAngle_statement(self, ctx: AmberMRParser.Angle_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#torsion_statement.
    def enterTorsion_statement(self, ctx: AmberMRParser.Torsion_statementContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1
        self.__cur_subtype = 'dihed'

    # Exit a parse tree produced by AmberMRParser#torsion_statement.
    def exitTorsion_statement(self, ctx: AmberMRParser.Torsion_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#plane_point_angle_statement.
    def enterPlane_point_angle_statement(self, ctx: AmberMRParser.Plane_point_angle_statementContext):  # pylint: disable=unused-argument
        self.planeRestraints += 1
        self.__cur_subtype = 'plane'

    # Exit a parse tree produced by AmberMRParser#plane_point_angle_statement.
    def exitPlane_point_angle_statement(self, ctx: AmberMRParser.Plane_point_angle_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#plane_plane_angle_statement.
    def enterPlane_plane_angle_statement(self, ctx: AmberMRParser.Plane_plane_angle_statementContext):  # pylint: disable=unused-argument
        self.planeRestraints += 1
        self.__cur_subtype = 'plane'

    # Exit a parse tree produced by AmberMRParser#plane_plane_angle_statement.
    def exitPlane_plane_angle_statement(self, ctx: AmberMRParser.Plane_plane_angle_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#general_distance2_statement.
    def enterGeneral_distance2_statement(self, ctx: AmberMRParser.General_distance2_statementContext):  # pylint: disable=unused-argument
        self.distRestraints += 1
        self.__cur_subtype = 'dist'

    # Exit a parse tree produced by AmberMRParser#general_distance2_statement.
    def exitGeneral_distance2_statement(self, ctx: AmberMRParser.General_distance2_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#general_distance3_statement.
    def enterGeneral_distance3_statement(self, ctx: AmberMRParser.General_distance3_statementContext):  # pylint: disable=unused-argument
        self.distRestraints += 1
        self.__cur_subtype = 'dist'

    # Exit a parse tree produced by AmberMRParser#general_distance3_statement.
    def exitGeneral_distance3_statement(self, ctx: AmberMRParser.General_distance3_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#general_distance4_statement.
    def enterGeneral_distance4_statement(self, ctx: AmberMRParser.General_distance4_statementContext):  # pylint: disable=unused-argument
        self.distRestraints += 1
        self.__cur_subtype = 'dist'

    # Exit a parse tree produced by AmberMRParser#general_distance4_statement.
    def exitGeneral_distance4_statement(self, ctx: AmberMRParser.General_distance4_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#noeexp_statement.
    def enterNoeexp_statement(self, ctx: AmberMRParser.Noeexp_statementContext):  # pylint: disable=unused-argument
        self.noepkRestraints += 1
        self.__cur_subtype = 'noepk'

    # Exit a parse tree produced by AmberMRParser#noeexp_statement.
    def exitNoeexp_statement(self, ctx: AmberMRParser.Noeexp_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#shf_statement.
    def enterShf_statement(self, ctx: AmberMRParser.Shf_statementContext):  # pylint: disable=unused-argument
        self.hvycsRestraints += 1
        self.__cur_subtype = 'hvycs'

    # Exit a parse tree produced by AmberMRParser#shf_statement.
    def exitShf_statement(self, ctx: AmberMRParser.Shf_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#pcshf_statement.
    def enterPcshf_statement(self, ctx: AmberMRParser.Pcshf_statementContext):  # pylint: disable=unused-argument
        self.pcsRestraints += 1
        self.__cur_subtype = 'pcs'

    # Exit a parse tree produced by AmberMRParser#pcshf_statement.
    def exitPcshf_statement(self, ctx: AmberMRParser.Pcshf_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#align_statement.
    def enterAlign_statement(self, ctx: AmberMRParser.Align_statementContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1
        self.__cur_subtype = 'rdc'

    # Exit a parse tree produced by AmberMRParser#align_statement.
    def exitAlign_statement(self, ctx: AmberMRParser.Align_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#csa_statement.
    def enterCsa_statement(self, ctx: AmberMRParser.Csa_statementContext):  # pylint: disable=unused-argument
        self.csaRestraints += 1
        self.__cur_subtype = 'csa'

    # Exit a parse tree produced by AmberMRParser#csa_statement.
    def exitCsa_statement(self, ctx: AmberMRParser.Csa_statementContext):  # pylint: disable=unused-argument
        pass

    def __getCurrentRestraint(self):
        if self.__cur_subtype == 'dist':
            return f"[Check the {self.distRestraints}th row of distance restraints] "
        if self.__cur_subtype == 'dihed':
            return f"[Check the {self.dihedRestraints}th row of torsional angle restraints] "
        if self.__cur_subtype == 'rdc':
            return f"[Check the {self.rdcRestraints}th row of residual dipolar coupling restraints] "
        if self.__cur_subtype == 'plane':
            return f"[Check the {self.planeRestraints}th row of plane-point/plane angle restraints] "
        if self.__cur_subtype == 'noepk':
            return f"[Check the {self.noepkRestraints}th row of NOESY volume restraints] "
        if self.__cur_subtype == 'hvycs':
            return f"[Check the {self.hvycsRestraints}th row of chemical shift restraints] "
        if self.__cur_subtype == 'pcs':
            return f"[Check the {self.pcsRestraints}th row of pseudocontact shift restraints] "
        if self.__cur_subtype == 'csa':
            return f"[Check the {self.csaRestraints}th row of residual CSA or pseudo-CSA restraints] "
        return ''

    def getContentSubtype(self):
        """ Return content subtype of AMBER MR file.
        """

        contentSubtype = {'dist_restraint': self.distRestraints,
                          'dihed_restraint': self.dihedRestraints,
                          'rdc_restraint': self.rdcRestraints,
                          'plane_restraint': self.planeRestraints,
                          'noepk_resraint': self.noepkRestraints,
                          'hvycs_restraint': self.hvycsRestraints,
                          'pcs_restraint': self.pcsRestraints,
                          'csa_restraint': self.csaRestraints
                          }

        return {k: 1 for k, v in contentSubtype.items() if v > 0}

# del AmberMRParser
