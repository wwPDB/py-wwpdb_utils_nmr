/*
 AMBER MR (Magnetic Restraint) parser grammar for ANTLR v4.
 Copyright 2021 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

parser grammar AmberMRParser;

options { tokenVocab=AmberMRLexer; }

amber_mr:
	nmr_restraint*
	noesy_volume_restraint*
	chemical_shift_restraint*
	pcs_restraint*
	dipolar_coupling_restraint*
	csa_restraint*
	EOF;

nmr_restraint:
	RST restraint_statement END;

noesy_volume_restraint:
	NOEEXP noeexp_statement END;

chemical_shift_restraint:
	SHF shf_statement END;

pcs_restraint:
	PCSHF pcshf_statement END;

dipolar_coupling_restraint:
	ALIGN align_statement END;

csa_restraint:
	CSA csa_statement END;

/* Amber: NMR restraints - 29.1 Distance, angle and torsional restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
restraint_statement:
	distance_statement |
	angle_statement |
	torsion_statement |
	plane_point_angle_statement |
	plane_plane_angle_statement |
	general_distance2_statement |
	general_distance3_statement |
	general_distance4_statement;

distance_statement:
	IAT Equ_op Integer Comma Integer Comma? |
	RSTWT Equ_op Real Comma? |
	RESTRAINT Equ_op QUOT DistanceRstFunctionCall QUOT Comma? |
	ATNAM Equ_op Quoted_atom_name Comma Quoted_atom_name Comma? |
	IRESID Equ_op Integer Comma? |
	NSTEP1 Equ_op Integer Comma? |
	NSTEP2 Equ_op Integer Comma? |
	IRSTYP Equ_op Integer Comma? |
	IALTD Equ_op Integer Comma? |
	IFVARI Equ_op Integer Comma? |
	NINC Equ_op Integer Comma? |
	IMULT Equ_op Integer Comma? |
	R1 Equ_op Real Comma? |
	R2 Equ_op Real Comma? |
	R3 Equ_op Real Comma? |
	R4 Equ_op Real Comma? |
	RK2 Equ_op Real Comma? |
	RK3 Equ_op Real Comma? |
	R1A Equ_op Real Comma? |
	R2A Equ_op Real Comma? |
	R3A Equ_op Real Comma? |
	R4A Equ_op Real Comma? |
	RK2A Equ_op Real Comma? |
	RK3A Equ_op Real Comma? |
	R0 Equ_op Real Comma? |
	K0 Equ_op Real Comma? |
	R0A Equ_op Real Comma? |
	K0A Equ_op Real Comma? |
	DISTANCE_IGR Equ_op Integer (Comma Integer)* Comma? |
	FXYZ Equ_op Integer Comma Integer Comma Integer Comma? |
	OUTXYZ Equ_op Integer Comma? |
	DISTANCE_GRNAM Equ_op Quoted_atom_name (Comma Quoted_atom_name)* Comma? |
	IR6 Equ_op Integer Comma? |
	IFNTYP Equ_op Integer Comma? |
	IXPK Equ_op Integer Comma? |
	NXPK Equ_op Integer Comma? |
	ICONSTR Equ_op Integer Comma? |
	DistanceIFunctionCall Equ_op Integer Comma? |
	DistanceIGFunctionCall Equ_op IntegerArray Comma? |
	DistanceRFunctionCall Equ_op Real Comma? |
	DistanceNFunctionCall Equ_op Quoted_atom_name Comma?;

angle_statement:
	IAT Equ_op Integer Comma Integer Comma Integer Comma? |
	RSTWT Equ_op Real Comma? |
	RESTRAINT Equ_op QUOT AngleRstFunctionCall QUOT Comma? |
	ATNAM Equ_op Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma? |
	IRESID Equ_op Integer Comma? |
	NSTEP1 Equ_op Integer Comma? |
	NSTEP2 Equ_op Integer Comma? |
	IRSTYP Equ_op Integer Comma? |
	IFVARI Equ_op Integer Comma? |
	NINC Equ_op Integer Comma? |
	IMULT Equ_op Integer Comma? |
	R1 Equ_op Real Comma? |
	R2 Equ_op Real Comma? |
	R3 Equ_op Real Comma? |
	R4 Equ_op Real Comma? |
	RK2 Equ_op Real Comma? |
	RK3 Equ_op Real Comma? |
	R1A Equ_op Real Comma? |
	R2A Equ_op Real Comma? |
	R3A Equ_op Real Comma? |
	R4A Equ_op Real Comma? |
	RK2A Equ_op Real Comma? |
	RK3A Equ_op Real Comma? |
	R0 Equ_op Real Comma? |
	K0 Equ_op Real Comma? |
	R0A Equ_op Real Comma? |
	K0A Equ_op Real Comma? |
	ANGLE_IGR Equ_op Integer (Comma Integer)* Comma? |
	ANGLE_GRNAM Equ_op Quoted_atom_name (Comma Quoted_atom_name)* Comma? |
	IFNTYP Equ_op Integer Comma? |
	IXPK Equ_op Integer Comma? |
	NXPK Equ_op Integer Comma? |
	AngleIFunctionCall Equ_op Integer Comma? |
	AngleIGFunctionCall Equ_op IntegerArray Comma? |
	AngleRFunctionCall Equ_op Real Comma? |
	AngleNFunctionCall Equ_op Quoted_atom_name Comma?;

torsion_statement:
	IAT Equ_op Integer Comma Integer Comma Integer Comma Integer Comma? |
	RSTWT Equ_op Real Comma? |
	RESTRAINT Equ_op QUOT TorsionRstFunctionCall QUOT Comma? |
	ATNAM Equ_op Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma? |
	IRESID Equ_op Integer Comma? |
	NSTEP1 Equ_op Integer Comma? |
	NSTEP2 Equ_op Integer Comma? |
	IRSTYP Equ_op Integer Comma? |
	IFVARI Equ_op Integer Comma? |
	NINC Equ_op Integer Comma? |
	IMULT Equ_op Integer Comma? |
	R1 Equ_op Real Comma? |
	R2 Equ_op Real Comma? |
	R3 Equ_op Real Comma? |
	R4 Equ_op Real Comma? |
	RK2 Equ_op Real Comma? |
	RK3 Equ_op Real Comma? |
	R1A Equ_op Real Comma? |
	R2A Equ_op Real Comma? |
	R3A Equ_op Real Comma? |
	R4A Equ_op Real Comma? |
	RK2A Equ_op Real Comma? |
	RK3A Equ_op Real Comma? |
	R0 Equ_op Real Comma? |
	K0 Equ_op Real Comma? |
	R0A Equ_op Real Comma? |
	K0A Equ_op Real Comma? |
	TORSION_IGR Equ_op Integer (Comma Integer)* Comma? |
	TORSION_GRNAM Equ_op Quoted_atom_name (Comma Quoted_atom_name)* Comma? |
	RJCOEF Equ_op Real Comma Real Comma Real Comma? |
	IFNTYP Equ_op Integer Comma? |
	IXPK Equ_op Integer Comma? |
	NXPK Equ_op Integer Comma? |
	TorsionIFunctionCall Equ_op Integer Comma? |
	TorsionIGFunctionCall Equ_op IntegerArray Comma? |
	TorsionRFunctionCall Equ_op Real Comma? |
	TorsionNFunctionCall Equ_op Quoted_atom_name Comma?;

plane_point_angle_statement:
	IAT Equ_op Integer Comma Integer Comma Integer Comma Integer Comma Integer Comma? |
	RSTWT Equ_op Real Comma? |
	ATNAM Equ_op Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma?
	IRESID Equ_op Integer Comma? |
	NSTEP1 Equ_op Integer Comma? |
	NSTEP2 Equ_op Integer Comma? |
	IRSTYP Equ_op Integer Comma? |
	IFVARI Equ_op Integer Comma? |
	NINC Equ_op Integer Comma? |
	IMULT Equ_op Integer Comma? |
	R1 Equ_op Real Comma? |
	R2 Equ_op Real Comma? |
	R3 Equ_op Real Comma? |
	R4 Equ_op Real Comma? |
	RK2 Equ_op Real Comma? |
	RK3 Equ_op Real Comma? |
	R1A Equ_op Real Comma? |
	R2A Equ_op Real Comma? |
	R3A Equ_op Real Comma? |
	R4A Equ_op Real Comma? |
	RK2A Equ_op Real Comma? |
	RK3A Equ_op Real Comma? |
	R0 Equ_op Real Comma? |
	K0 Equ_op Real Comma? |
	R0A Equ_op Real Comma? |
	K0A Equ_op Real Comma? |
	PLANEPOINTANG_IGR Equ_op Integer (Comma Integer)* Comma? |
	PLANEPOINTANG_GRNAM Equ_op Quoted_atom_name (Comma Quoted_atom_name)* Comma? |
	IXPK Equ_op Integer Comma? |
	NXPK Equ_op Integer Comma? |
	PlanePointAngleIFunctionCall Equ_op Integer Comma? |
	PlanePointAngleIGFunctionCall Equ_op IntegerArray Comma? |
	PlanePointAngleRFunctionCall Equ_op Real Comma? |
	PlanePointAngleNFunctionCall Equ_op Quoted_atom_name Comma?;
	
plane_plane_angle_statement:
	IAT Equ_op Integer Comma Integer Comma Integer Comma Integer Comma Integer Comma Integer Comma Integer Comma Integer Comma? |
	RSTWT Equ_op Real Comma? |
	ATNAM Equ_op Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma?
	IRESID Equ_op Integer Comma? |
	NSTEP1 Equ_op Integer Comma? |
	NSTEP2 Equ_op Integer Comma? |
	IRSTYP Equ_op Integer Comma? |
	IFVARI Equ_op Integer Comma? |
	NINC Equ_op Integer Comma? |
	IMULT Equ_op Integer Comma? |
	R1 Equ_op Real Comma? |
	R2 Equ_op Real Comma? |
	R3 Equ_op Real Comma? |
	R4 Equ_op Real Comma? |
	RK2 Equ_op Real Comma? |
	RK3 Equ_op Real Comma? |
	R1A Equ_op Real Comma? |
	R2A Equ_op Real Comma? |
	R3A Equ_op Real Comma? |
	R4A Equ_op Real Comma? |
	RK2A Equ_op Real Comma? |
	RK3A Equ_op Real Comma? |
	R0 Equ_op Real Comma? |
	K0 Equ_op Real Comma? |
	R0A Equ_op Real Comma? |
	K0A Equ_op Real Comma? |
	PLANEPLANEANG_IGR Equ_op Integer (Comma Integer)* Comma? |
	PLANEPLANEANG_GRNAM Equ_op Quoted_atom_name (Comma Quoted_atom_name)* Comma? |
	IXPK Equ_op Integer Comma? |
	NXPK Equ_op Integer Comma? |
	PlanePlaneAngleIFunctionCall Equ_op Integer Comma? |
	PlanePlaneAngleIGFunctionCall Equ_op IntegerArray Comma? |
	PlanePlaneAngleRFunctionCall Equ_op Real Comma? |
	PlanePlaneAngleNFunctionCall Equ_op Quoted_atom_name Comma?;

general_distance2_statement:
	IAT Equ_op Integer Comma Integer Comma Integer Comma Integer Comma? |
	RSTWT Equ_op Real Comma Real Comma? |
	RESTRAINT Equ_op QUOT Coordinate2RstFunctionCall QUOT Comma? |
	ATNAM Equ_op Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma? |
	IRESID Equ_op Integer Comma? |
	NSTEP1 Equ_op Integer Comma? |
	NSTEP2 Equ_op Integer Comma? |
	IRSTYP Equ_op Integer Comma? |
	IALTD Equ_op Integer Comma? |
	IFVARI Equ_op Integer Comma? |
	NINC Equ_op Integer Comma? |
	IMULT Equ_op Integer Comma? |
	R1 Equ_op Real Comma? |
	R2 Equ_op Real Comma? |
	R3 Equ_op Real Comma? |
	R4 Equ_op Real Comma? |
	RK2 Equ_op Real Comma? |
	RK3 Equ_op Real Comma? |
	R1A Equ_op Real Comma? |
	R2A Equ_op Real Comma? |
	R3A Equ_op Real Comma? |
	R4A Equ_op Real Comma? |
	RK2A Equ_op Real Comma? |
	RK3A Equ_op Real Comma? |
	R0 Equ_op Real Comma? |
	K0 Equ_op Real Comma? |
	R0A Equ_op Real Comma? |
	K0A Equ_op Real Comma? |
	GENDISTANCE2_IGR Equ_op Integer (Comma Integer)* Comma? |
	GENDISTANCE2_GRNAM Equ_op Quoted_atom_name (Comma Quoted_atom_name)* Comma? |
	IFNTYP Equ_op Integer Comma? |
	IXPK Equ_op Integer Comma? |
	NXPK Equ_op Integer Comma? |
	GeneralDistance2IFunctionCall Equ_op Integer Comma? |
	GeneralDistance2IGFunctionCall Equ_op IntegerArray Comma? |
	GeneralDistance2RFunctionCall Equ_op Real Comma? |
	GeneralDistance2NFunctionCall Equ_op Quoted_atom_name Comma?;

general_distance3_statement:
	IAT Equ_op Integer Comma Integer Comma Integer Comma Integer Comma Integer Comma Integer Comma? |
	RSTWT Equ_op Real Comma Real Comma Real Comma? |
	RESTRAINT Equ_op QUOT Coordinate3RstFunctionCall QUOT Comma? |
	ATNAM Equ_op Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma? |
	IRESID Equ_op Integer Comma? |
	NSTEP1 Equ_op Integer Comma? |
	NSTEP2 Equ_op Integer Comma? |
	IRSTYP Equ_op Integer Comma? |
	IALTD Equ_op Integer Comma? |
	IFVARI Equ_op Integer Comma? |
	NINC Equ_op Integer Comma? |
	IMULT Equ_op Integer Comma? |
	R1 Equ_op Real Comma? |
	R2 Equ_op Real Comma? |
	R3 Equ_op Real Comma? |
	R4 Equ_op Real Comma? |
	RK2 Equ_op Real Comma? |
	RK3 Equ_op Real Comma? |
	R1A Equ_op Real Comma? |
	R2A Equ_op Real Comma? |
	R3A Equ_op Real Comma? |
	R4A Equ_op Real Comma? |
	RK2A Equ_op Real Comma? |
	RK3A Equ_op Real Comma? |
	R0 Equ_op Real Comma? |
	K0 Equ_op Real Comma? |
	R0A Equ_op Real Comma? |
	K0A Equ_op Real Comma? |
	GENDISTANCE3_IGR Equ_op Integer (Comma Integer)* Comma? |
	GENDISTANCE3_GRNAM Equ_op Quoted_atom_name (Comma Quoted_atom_name)* Comma? |
	IFNTYP Equ_op Integer Comma? |
	IXPK Equ_op Integer Comma? |
	NXPK Equ_op Integer Comma? |
	GeneralDistance3IFunctionCall Equ_op Integer Comma? |
	GeneralDistance3IGFunctionCall Equ_op IntegerArray Comma? |
	GeneralDistance3RFunctionCall Equ_op Real Comma? |
	GeneralDistance3NFunctionCall Equ_op Quoted_atom_name Comma?;

general_distance4_statement:
	IAT Equ_op Integer Comma Integer Comma Integer Comma Integer Comma Integer Comma Integer Comma Integer Comma Integer Comma? |
	RSTWT Equ_op Real Comma Real Comma Real Comma Real Comma? |
	RESTRAINT Equ_op QUOT Coordinate4RstFunctionCall QUOT Comma? |
	ATNAM Equ_op Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma Quoted_atom_name Comma? |
	IRESID Equ_op Integer Comma? |
	NSTEP1 Equ_op Integer Comma? |
	NSTEP2 Equ_op Integer Comma? |
	IRSTYP Equ_op Integer Comma? |
	IALTD Equ_op Integer Comma? |
	IFVARI Equ_op Integer Comma? |
	NINC Equ_op Integer Comma? |
	IMULT Equ_op Integer Comma? |
	R1 Equ_op Real Comma? |
	R2 Equ_op Real Comma? |
	R3 Equ_op Real Comma? |
	R4 Equ_op Real Comma? |
	RK2 Equ_op Real Comma? |
	RK3 Equ_op Real Comma? |
	R1A Equ_op Real Comma? |
	R2A Equ_op Real Comma? |
	R3A Equ_op Real Comma? |
	R4A Equ_op Real Comma? |
	RK2A Equ_op Real Comma? |
	RK3A Equ_op Real Comma? |
	R0 Equ_op Real Comma? |
	K0 Equ_op Real Comma? |
	R0A Equ_op Real Comma? |
	K0A Equ_op Real Comma? |
	GENDISTANCE4_IGR Equ_op Integer (Comma Integer)* Comma? |
	GENDISTANCE4_GRNAM Equ_op Quoted_atom_name (Comma Quoted_atom_name)* Comma? |
	IFNTYP Equ_op Integer Comma? |
	IXPK Equ_op Integer Comma? |
	NXPK Equ_op Integer Comma? |
	GeneralDistance4IFunctionCall Equ_op Integer Comma? |
	GeneralDistance4IGFunctionCall Equ_op IntegerArray Comma? |
	GeneralDistance4RFunctionCall Equ_op Real Comma? |
	GeneralDistance4NFunctionCall Equ_op Quoted_atom_name Comma?;

/* Amber: NMR restraints - 29.2. NOESY volume restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
noeexp_statement:
	NPEAK Equ_op IntegerArray Comma? |
	EMIX Equ_op Real (Comma Real)* Comma? |
	NoeExpIGFunctionCall Equ_op IntegerArray Comma? |
	NoeExpRGFunctionCall Equ_op RealArray Comma? |
	INVWT1 Equ_op Real Comma? |
	INVWT2 Equ_op Real Comma? |
	OMEGA Equ_op Real Comma? |
	TAUROT Equ_op Real Comma? |
	TAUMET Equ_op Real Comma? |
	ID2O Equ_op Integer Comma? |
	OSCALE Equ_op Real Comma?;

/* Amber: NMR restraints - 29.3. Chemical shift restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
shf_statement:
	NRING Equ_op Integer Comma? |
	SftIFunctionCall Equ_op Integer Comma? |
	SftIFunctionCall2 Equ_op Integer Comma? |
	SftRFunctionCall Equ_op Real Comma? |
	SftRGFunctionCall Equ_op RealArray Comma? |
	SftNFunctionCall Equ_op Quoted_atom_name Comma? |
	NPROT Equ_op Integer Comma? |
	SHCUT Equ_op Real Comma? |
	NTER Equ_op Integer Comma? |
	CTER Equ_op Integer Comma?;

/* Amber: NMR restraints - 29.4. Psuedocontact shift restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
pcshf_statement:
	NPROT Equ_op Integer Comma? |
	NME Equ_op Integer Comma? |
	NMPMC Equ_op Quoted_atom_name (Comma Quoted_atom_name)* Comma? |
	PcshfIFunctionCall Equ_op Integer Comma? |
	PcshfIGFunctionCall Equ_op IntegerArray Comma? |
	PcshfRFunctionCall Equ_op Real Comma? |
	PcshfRGFunctionCall Equ_op RealArray Comma? |
	OPTKON Equ_op Real Comma?;

/* Amber: NMR restraints - 29.5. Direct dipolar coupling restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
align_statement:
	NDIP Equ_op Integer Comma? |
	AlignIFunctionCall Equ_op Integer Comma? |
	AlignRFunctionCall Equ_op Real Comma? |
	DWT Equ_op RealArray Comma? |
	DATASET Equ_op Integer Comma? |
	NUM_DATASET Equ_op Integer Comma? |
	SNN Equ_op Real Comma? |
	GIGJ Equ_op RealArray Comma? |
	DIJ Equ_op Real Comma? |
	DCUT Equ_op Real Comma? |
	FREEZEMOL Equ_op Logical Comma?;

/* Amber: NMR restraints - 29.6. Residual CSA or pseudo-CSA restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
csa_statement:
	NCSA Equ_op Integer Comma? |
	CsaIFunctionCall Equ_op Integer Comma? |
	CsaRFunctionCall Equ_op Real Comma? |
	CWT Equ_op RealArray Comma? |
	DATASETC Equ_op Integer Comma? |
	FIELD Equ_op Real Comma? |
	SIGMANN Equ_op Real Comma? |
	CCUT Equ_op Real Comma?;

