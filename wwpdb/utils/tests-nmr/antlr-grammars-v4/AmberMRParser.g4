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
	comment*
	nmr_restraint*
	noesy_volume_restraint*
	chemical_shift_restraint*
	pcs_restraint*
	dipolar_coupling_restraint*
	csa_restraint*
	EOF;

comment:
	COMMENT Simple_name+ RETURN_C;

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
	distance_statement* |
	angle_statement* |
	torsion_statement* |
	plane_point_angle_statement* |
	plane_plane_angle_statement* |
	general_distance2_statement* |
	general_distance3_statement* |
	general_distance4_statement*;

distance_statement:
	(IAT | IGR1 | IGR2) Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	RESTRAINT Equ_op L_QUOT distance_rst_func_call R_QUOT Comma? |
	(ATNAM | GRNAM1 | GRNAM2) Equ_op_QA Qstrings Comma_QA |
	(IRESID | IRSTYP | IALTD | IMULT | OUTXYZ | IR6 | IFNTYP) Equ_op_BP BoolInt Comma? |
	(NSTEP1 | NSTEP2 | IFVARI | NINC | IXPK | NXPK | ICONSTR ) Equ_op_IP Integer Comma? |
	(R1 | R2 | R3 | R4 | RK2 | RK3 | R1A | R2A | R3A | R4A | RK2A | RK3A | R0 | K0 | R0A | K0A) Equ_op_RP Real Comma? |
	FXYZ Equ_op_BA BoolInts Comma_BA |
	IAT L_paren_IP Decimal R_paren_ARG Equ_op_IP Integer Comma? |
	(IGR1 | IGR2) L_paren_IA Decimal R_paren_ARG Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT L_paren_RP Decimal R_paren_ARG Equ_op_RP Real Comma? |
	(ATNAM | GRNAM1 | GRNAM2) L_paren_QA Decimal R_paren_ARG Equ_op_QA Qstrings Comma_QA;

angle_statement:
	(IAT | IGR1 | IGR2 | IGR3) Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	RESTRAINT Equ_op L_QUOT angle_rst_func_call R_QUOT Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3) Equ_op_QA Qstrings Comma_QA |
	(IRESID | IRSTYP | IMULT | IFNTYP) Equ_op_BP BoolInt Comma? |
	(NSTEP1 | NSTEP2 | IFVARI | NINC | IXPK | NXPK) Equ_op_IP Integer Comma? |
	(R1 | R2 | R3 | R4 | RK2 | RK3 | R1A | R2A | R3A | R4A | RK2A | RK3A | R0 | K0 | R0A | K0A) Equ_op_RP Real Comma? |
	IAT L_paren_IP Decimal R_paren_ARG Equ_op_IP Integer Comma? |
	(IGR1 | IGR2 | IGR3) L_paren_IA Decimal R_paren_ARG Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT L_paren_RP Decimal R_paren_ARG Equ_op_RP Real Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3) L_paren_QA Decimal R_paren_ARG Equ_op_QA Qstrings Comma_QA;

torsion_statement:
	(IAT | IGR1 | IGR2 | IGR3 | IGR4) Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	(RSTWT | RJCOEF) Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	RESTRAINT Equ_op L_QUOT torsion_rst_func_call R_QUOT Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4) Equ_op_QA Qstrings Comma_QA |
	(IRESID | IRSTYP | IMULT | IFNTYP) Equ_op_BP BoolInt Comma? |
	(NSTEP1 | NSTEP2 | IFVARI | NINC | IXPK | NXPK) Equ_op_IP Integer Comma? |
	(R1 | R2 | R3 | R4 | RK2 | RK3 | R1A | R2A | R3A | R4A | RK2A | RK3A | R0 | K0 | R0A | K0A) Equ_op_RP Real Comma? |
	IAT L_paren_IP Decimal R_paren_ARG Equ_op_IP Integer Comma? |
	(IGR1 | IGR2 | IGR3 | IGR4) L_paren_IA Decimal R_paren_ARG Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT L_paren_RP Decimal R_paren_ARG Equ_op_RP Real Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4) L_paren_QA Decimal R_paren_ARG Equ_op_QA Qstrings Comma_QA;

plane_point_angle_statement:
	(IAT | IGR1 | IGR2 | IGR3 | IGR4 | IGR5) Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5) Equ_op_QA Qstrings Comma_QA |
	(IRESID | IRSTYP | IMULT) Equ_op_BP BoolInt Comma? |
	(NSTEP1 | NSTEP2 | IFVARI | NINC | IXPK | NXPK) Equ_op_IP Integer Comma? |
	(R1 | R2 | R3 | R4 | RK2 | RK3 | R1A | R2A | R3A | R4A | RK2A | RK3A | R0 | K0 | R0A | K0A) Equ_op_RP Real Comma? |
	IAT L_paren_IP Decimal R_paren_ARG Equ_op_IP Integer Comma? |
	(IGR1 | IGR2 | IGR3 | IGR4 | IGR5) L_paren_IA Decimal R_paren_ARG Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT L_paren_RP Decimal R_paren_ARG Equ_op_RP Real Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5) L_paren_QA Decimal R_paren_ARG Equ_op_QA Qstrings Comma_QA;

plane_plane_angle_statement:
	(IAT | IGR1 | IGR2 | IGR3 | IGR4 | IGR5 | IGR6 | IGR7 | IGR8) Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5 | GRNAM6 | GRNAM7 | GRNAM8) Equ_op_QA Qstrings Comma_QA |
	(IRESID | IRSTYP | IMULT) Equ_op_BP BoolInt Comma? |
	(NSTEP1 | NSTEP2 | IFVARI | NINC | IXPK | NXPK) Equ_op_IP Integer Comma? |
	(R1 | R2 | R3 | R4 | RK2 | RK3 | R1A | R2A | R3A | R4A | RK2A | RK3A | R0 | K0 | R0A | K0A) Equ_op_RP Real Comma? |
	IAT L_paren_IP Decimal R_paren_ARG Equ_op_IP Integer Comma? |
	(IGR1 | IGR2 | IGR3 | IGR4 | IGR5 | IGR6 | IGR7 | IGR8) L_paren_IA Decimal R_paren_ARG Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT L_paren_RP Decimal R_paren_ARG Equ_op_RP Real Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5 | GRNAM6 | GRNAM7 | GRNAM8) L_paren_QA Decimal R_paren_ARG Equ_op_QA Qstrings Comma_QA;

general_distance2_statement:
	(IAT | IGR1 | IGR2 | IGR3 | IGR4) Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	RESTRAINT Equ_op L_QUOT coordinate2_rst_func_call R_QUOT Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4) Equ_op_QA Qstrings Comma_QA |
	(IRESID | IRSTYP | IALTD | IMULT | IFNTYP) Equ_op_BP BoolInt Comma? |
	(NSTEP1 | NSTEP2 | IFVARI | NINC | IXPK | NXPK) Equ_op_IP Integer Comma? |
	(R1 | R2 | R3 | R4 | RK2 | RK3 | R1A | R2A | R3A | R4A | RK2A | RK3A | R0 | K0 | R0A | K0A) Equ_op_RP Real Comma? |
	IAT L_paren_IP Decimal R_paren_ARG Equ_op_IP Integer Comma? |
	(IGR1 | IGR2 | IGR3 | IGR4) L_paren_IA Decimal R_paren_ARG Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT L_paren_RP Decimal R_paren_ARG Equ_op_RP Real Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4) L_paren_QA Decimal R_paren_ARG Equ_op_QA Qstrings Comma_QA;

general_distance3_statement:
	(IAT | IGR1 | IGR2 | IGR3 | IGR4 | IGR5 | IGR6) Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	RESTRAINT Equ_op L_QUOT coordinate3_rst_func_call R_QUOT Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5 | GRNAM6) Equ_op_QA Qstrings Comma_QA |
	(IRESID | IRSTYP | IALTD | IMULT | IFNTYP) Equ_op_BP BoolInt Comma? |
	(NSTEP1 | NSTEP2 | IFVARI | NINC | IXPK | NXPK) Equ_op_IP Integer Comma? |
	(R1 | R2 | R3 | R4 | RK2 | RK3 | R1A | R2A | R3A | R4A | RK2A | RK3A | R0 | K0 | R0A | K0A) Equ_op_RP Real Comma? |
	IAT L_paren_IP Decimal R_paren_ARG Equ_op_IP Integer Comma? |
	(IGR1 | IGR2 | IGR3 | IGR4 | IGR5 | IGR6) L_paren_IA Decimal R_paren_ARG Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT L_paren_RP Decimal R_paren_ARG Equ_op_RP Real Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5 | GRNAM6) L_paren_QA Decimal R_paren_ARG Equ_op_QA Qstrings Comma_QA;

general_distance4_statement:
	(IAT | IGR1 | IGR2 | IGR3 | IGR4 | IGR5 | IGR6 | IGR7 | IGR8) Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	RESTRAINT Equ_op L_QUOT coordinate4_rst_func_call R_QUOT Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5 | GRNAM6 | GRNAM7 | GRNAM8) Equ_op_QA Qstrings Comma_QA |
	(IRESID | IRSTYP | IALTD | IMULT | IFNTYP) Equ_op_BP BoolInt Comma? |
	(NSTEP1 | NSTEP2 | IFVARI | NINC | IXPK | NXPK) Equ_op_IP Integer Comma? |
	(R1 | R2 | R3 | R4 | RK2 | RK3 | R1A | R2A | R3A | R4A | RK2A | RK3A | R0 | K0 | R0A | K0A) Equ_op_RP Real Comma? |
	IAT L_paren_IP Decimal R_paren_ARG Equ_op_IP Integer Comma? |
	(IGR1 | IGR2 | IGR3 | IGR4 | IGR5 | IGR6 | IGR7 | IGR8) L_paren_IA Decimal R_paren_ARG Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	RSTWT L_paren_RP Decimal R_paren_ARG Equ_op_RP Real Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5 | GRNAM6 | GRNAM7 | GRNAM8) L_paren_QA Decimal R_paren_ARG Equ_op_QA Qstrings Comma_QA;

/* Amber: NMR restraints - 29.2. NOESY volume restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
noeexp_statement:
	NPEAK Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	EMIX Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	(IHP | JHP) L_paren_IA Decimal Comma_ARG Decimal R_paren_ARG Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	(AEXP | ARANGE | AWT) L_paren_RA Decimal Comma_ARG Decimal R_paren_ARG Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	(INVWT1 | INVWT2 | OMEGA | TAUROT | TAUMET | OSCALE) Equ_op_RP Real Comma? |
	ID2O Equ_op_BP BoolInt Comma?;

/* Amber: NMR restraints - 29.3. Chemical shift restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
shf_statement:
	(NRING | NPROT | NTER | CTER) Equ_op_IP Integer Comma? |
	(NATR | IPROT) L_paren_IA Decimal R_paren_ARG Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	IATR L_paren_IP Decimal Comma_ARG Decimal R_paren_ARG Equ_op_IP Integer Comma? |
	OBS L_paren_RP Decimal R_paren_ARG Equ_op_RP Real Comma? |
	(STR | SHRANG | WT) L_paren_RA Decimal R_paren_ARG Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	NAMR L_paren_QA Decimal R_paren_ARG Equ_op_QA Qstrings Comma_QA |
	SHCUT Equ_op_RP Real Comma?;

/* Amber: NMR restraints - 29.4. Psuedocontact shift restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
pcshf_statement:
	(NPROT | NME) Equ_op_IP Integer Comma? |
	NMPMC Equ_op_QA Qstrings Comma_QA |
	(IPROT | MLTPRO) L_paren_IA Decimal R_paren_ARG Equ_op_IA (Integers | MultiplicativeInt) Comma_IA |
	(OPTPHI | OPTTET | OPTOMG | OPTA1 | OPTA2 | OBS) L_paren_RP Decimal R_paren_ARG Equ_op_RP Real Comma? |
	(WT | TOLPRO) L_paren_RA Decimal R_paren_ARG Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	OPTKON Equ_op_RP Real Comma?;

/* Amber: NMR restraints - 29.5. Direct dipolar coupling restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
align_statement:
	(NDIP | DATASET | NUM_DATASET) Equ_op_IP Integer Comma? |
	(ID | JD) L_paren_IP Decimal R_paren_ARG Equ_op_IP Integer Comma? |
	(DOBSL | DOBSU) L_paren_RP Decimal R_paren_ARG Equ_op_RP Real Comma? |
	(DWT | GIGJ) Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	(S11 | S12 | S13 | S22 | S23 | DIJ | DCUT) Equ_op_RP Real Comma? |
	FREEZEMOL Equ_op Logical Comma?;

/* Amber: NMR restraints - 29.6. Residual CSA or pseudo-CSA restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
csa_statement:
	(NCSA | DATASETC) Equ_op_IP Integer Comma? |
	(ICSA | JCSA | KCSA) L_paren_IP Decimal R_paren_ARG Equ_op_IP Integer Comma? |
	(COBSL | COBSU) L_paren_RP Decimal R_paren_ARG Equ_op_RP Real Comma? |
	CWT Equ_op_RA (Reals | MultiplicativeReal) Comma_RA |
	(SIGMA11 | SIGMA12 | SIGMA13 | SIGMA22 | SIGMA23 | FIELD | CCUT) Equ_op_RP Real Comma?;

/* Amber 10 (ambmask): NMR restraints - 29.1 Distance, angle and torsional restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
distance_rst_func_call:
	DISTANCE_F L_paren_F restraint_func_expr Comma_F? restraint_func_expr R_paren_F |
	DISTANCE_F L_brace_F restraint_func_expr Comma_F? restraint_func_expr R_brace_F |
	DISTANCE_F L_brakt_F restraint_func_expr Comma_F? restraint_func_expr R_brakt_F;

angle_rst_func_call:
	ANGLE_F L_paren_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_paren_F |
	ANGLE_F L_brace_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_brace_F |
	ANGLE_F L_brakt_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_brakt_F;

torsion_rst_func_call:
	TORSION_F L_paren_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_paren_F |
	TORSION_F L_brace_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_brace_F |
	TORSION_F L_brakt_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_brakt_F;

coordinate2_rst_func_call:
	COORDINATE_F L_paren_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F R_paren_F |
	COORDINATE_F L_brace_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F R_brace_F |
	COORDINATE_F L_brakt_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F R_brakt_F;

coordinate3_rst_func_call:
	COORDINATE_F L_paren_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F Comma_F?
				distance_rst_func_call Comma_F? Real_F R_paren_F |
	COORDINATE_F L_brace_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F Comma_F?
				distance_rst_func_call Comma_F? Real_F R_brace_F |
	COORDINATE_F L_brakt_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F Comma_F?
				distance_rst_func_call Comma_F? Real_F R_brakt_F;

coordinate4_rst_func_call:
	COORDINATE_F L_paren_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F Comma_F?
				distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F R_paren_F |
	COORDINATE_F L_brace_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F Comma_F?
				distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F R_brace_F |
	COORDINATE_F L_brakt_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F Comma_F?
				distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F R_brakt_F;

restraint_func_expr:
	Int_F |
	L_paren_F Int_F R_paren_F |
	L_brace_F Int_F R_brace_F |
	L_brakt_F Int_F R_brakt_F |
	Ambmask_F |
	L_paren_F Ambmask_F R_paren_F |
	L_brace_F Ambmask_F R_brace_F |
	L_brakt_F Ambmask_F R_brakt_F |
	plane_rst_func_call |
	com_rst_fun_call;

plane_rst_func_call:
	PLANE_F L_paren_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_paren_F |
	PLANE_F L_brace_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_brace_F |
	PLANE_F L_brakt_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_brakt_F;

com_rst_fun_call:
	COM_F L_paren_F restraint_func_expr (Comma_F? restraint_func_expr)* R_paren_F |
	COM_F L_brace_F restraint_func_expr (Comma_F? restraint_func_expr)* R_brace_F |
	COM_F L_brakt_F restraint_func_expr (Comma_F? restraint_func_expr)* R_brakt_F;
