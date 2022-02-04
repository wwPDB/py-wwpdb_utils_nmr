/*
 XPLOR-NIH MR (Magnetic Restraint) parser grammar for ANTLR v4.
 Copyright 2022 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

parser grammar XplorMRParser;

options { tokenVocab=XplorMRLexer; }

xplor_nih_mr:
	distance_restraint*
	dihedral_angle_restraint*
	rdc_restraint*
	planar_restraint*
	antidistance_restraint*
	coupling_restraint*
	carbon_shift_restraint*
	proton_shift_restraint*
	dihedral_angle_db_restraint*
	radius_of_gyration_restraint*
	diffusion_anisotropy_restraint*
	orientation_db_restraint*
	csa_restraint*
	pcsa_restraint*
	one_bond_coupling_restraint*
	angle_db_restraint*
	pre_restraint*
	pcs_restraint*
	prdc_restraint*
	porientation_restraint*
	pccr_restraint*
	hbond_restraint*
	noe_assign*			// allowing bare assign clauses for distance restraints
	dihedral_assign*		// allowing bare assign clauses for dihedral angle restraints
	sani_assign*			// allowing bare assign clauses for RDC restraints
	planar_statement*		// allowing bare group clauses for planer restraints
	hbond_assign*			// allowing bare assign clauses for Hydrogen bond restraints
	EOF;

distance_restraint:
	Noe L_brace noe_statement R_brace End;

dihedral_angle_restraint:
	Restraints Dihedral L_brace dihedral_statement R_brace End;

rdc_restraint:
	Sanisotropy L_brace sani_statement R_brace End |
	(Xdipolar | Dipolar) L_brace xdip_statement R_brace End |
	VectorAngle L_brace vean_statement R_brace End |
	Tensor L_brace tens_statement R_brace End |
	Anisotropy L_brace anis_statement R_brace End;

planar_restraint:
	Restraints Planar L_brace planar_statement R_brace End;

antidistance_restraint:
	Xadc L_brace antidistance_statement R_brace End;

coupling_restraint:
	Coupling L_brace coupling_statement R_brace End;

carbon_shift_restraint:
	Carbon L_brace carbon_shift_statement R_brace End;

proton_shift_restraint:
	Proton L_brace proton_shift_statement R_brace End;

dihedral_angle_db_restraint:
	Ramachandran L_brace ramachandran_statement R_brace End;

radius_of_gyration_restraint:
	Collapse L_brace collapse_statement R_brace End;

diffusion_anisotropy_restraint:
	Danisotropy L_brace diffusion_statement R_brace End;

orientation_db_restraint:
	Orient L_brace orientation_statement R_brace End;

csa_restraint:
	Dcsa L_brace csa_statement R_brace End;

pcsa_restraint:
	Pcsa L_brace pcsa_statement R_brace End;

one_bond_coupling_restraint:
	OneBond L_brace one_bond_coupling_statement R_brace End;

angle_db_restraint:
	AngleDb L_brace angle_db_statement R_brace End;

pre_restraint:
	Paramagnetic L_brace pre_statement R_brace End;

pcs_restraint:
	Xpcs L_brace pcs_statement R_brace End;

prdc_restraint:
	Xrdcoupling L_brace prdc_statement R_brace End;

porientation_restraint:
	Xangle L_brace porientation_statement R_brace End;

pccr_restraint:
	Xccr L_brace pccr_statement R_brace End;

hbond_restraint:
	Hbda L_brace hbond_statement R_brace End;

/* XPLOR-NIH: Distance restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node377.html
*/
noe_statement:
	noe_assign* |
	Asymptote Simple_names Real |
	Averaging Simple_names Noe_avr_methods |
	Bhig Simple_names Real |
	Ceiling Equ_op Real |
	Classification Simple_name |
	CountViol Simple_name |
	Distribute Simple_name Simple_name Real |
	Monomers Simple_names Integer |
	Ncount Simple_names Integer |
	Nrestraints Equ_op Integer |
	Potential Simple_names Noe_potential |
	Predict L_brace predict_statement R_brace End |
	Print Threshold Equ_op? Real |
	Reset |
	Rswitch Simple_names Real |
	Scale Simple_names Real |
	SoExponent Simple_names Real |
	SqConstant Simple_names Real |
	SqExponent Simple_names Real |
	SqOffset Simple_names Real |
	Temperature Equ_op Real;

noe_assign:
	Assign selection selection Real Real Real (Or_op selection selection)*;

predict_statement:
	Cutoff Equ_op Real | Cuton Equ_op Real | From selection | To selection;

/* XPLOR-NIH: Dihedral angle restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/cdih_syntax.html
*/
dihedral_statement:
	dihedral_assign* |
	Nassign Equ_op Integer |
	Reset |
	Scale Real;

dihedral_assign:
	Assign selection selection selection selection Real Real Real Integer;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (SANI - Susceptibility anisotropy)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node418.html
*/
sani_statement:
	sani_assign* |
	Classification Simple_name |
	Coefficients Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset;

sani_assign:
	Assign selection selection selection selection selection selection Real Real;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (XDIP)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node419.html
*/
xdip_statement:
	xdip_assign* |
	Classification Simple_name |
	Type Rdc_dist_fix_types |
	Scale Real |
	Sign Logical |
	Average Rdc_avr_methods |
	Coefficients Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset;

xdip_assign:
	Assign selection selection selection selection selection selection Real Real Real (Real Real Real)?;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (VEAN)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node420.html
*/
vean_statement:
	vean_assign* |
	Cv Equ_op Integer |
	Classification Simple_name |
	ForceConstant Real Real |
	Nrestraints Integer |
	Partition Equ_op Integer |
	Print Threshold Real |
	Reset;

vean_assign:
	Assign selection selection selection selection Real Real Real Real;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (TENS)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node421.html
*/
tens_statement:
	tens_assign* |
	Classification Simple_name |
	Coefficients Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset;

tens_assign:
	Assign selection selection Real Real;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (ANIS)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node422.html
*/
anis_statement:
	anis_assign* |
	Classification Simple_name |
	Coefficients Real Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset |
	Type Rdc_anis_types;

anis_assign:
	Assign selection selection selection selection Real Real;

/* XPLOR-NIH: Planality restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/plan_syntax.html
*/
planar_statement:
	Group L_brace group_statement R_brace |
	Initialize;

group_statement:
	Selection Equ_op selection |
	Weight Equ_op Real;

/* XPLOR-NIH: Antidiatance restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node398.html
*/
antidistance_statement:
	xadc_assign* |
	Classification Simple_name |
	Expectation Integer Real |
	ForceConstant Real |
	Nrestraints Integer |
	Print Threshold Real (All | (Classification Simple_name)) |
	Reset |
	Size Real Integer |
	Zero;

xadc_assign:
	Assign selection selection;

/* XPLOR-NIH: Scalar J-coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node401.html
*/
coupling_statement:
	coup_assign* |
	Classification Simple_name |
	Coefficients Real Real Real Real |
	Cv Equ_op Integer |
	DegEnergy Integer |
	ForceConstant Real Real? |
	Nrestraints Integer |
	Partition Equ_op Integer |
	Potential Coupling_potential |
	Print Threshold Real (All | (Classification Simple_name)) |
	Reset;

coup_assign:
	Assign selection selection selection selection (selection selection selection selection)? Real Real (Real Real)?;

/* XPLOR-NIH: Carbon chemical shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node404.html
*/
carbon_shift_statement:
	carbon_shift_assign* |
	Classification Simple_name |
	Expectation Integer Integer Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	PhiStep Real |
	PsiStep Real |
	Potential Coupling_potential |
	Print Threshold Real |
	carbon_shift_rcoil* |
	Reset |
	Zero;

carbon_shift_assign:
	Assign selection selection selection selection selection Real Real;

carbon_shift_rcoil:
	Rcoil selection Real Real;

/* XPLOR-NIH: Proton chemical shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node407.html
*/
proton_shift_statement:
	observed* |
	proton_shift_rcoil* |
	proton_shift_anisotropy* |
	proton_shift_amides* |
	proton_shift_carbons* |
	proton_shift_nitrogens* |
	proton_shift_oxygens* |
	proton_shift_ring_atoms* |
	proton_shift_alphas_and_amides* |
	Classification Simple_name |
	Error Real |
	DegEnergy Integer |
	ForceConstant Real Real? |
	Potential Coupling_potential |
	Print Threshold Real (All | (Classification Simple_name)) Simple_name |
	Reset;

observed:
	Observed selection selection? Real Real?;

proton_shift_rcoil:
	Rcoil selection Real;

proton_shift_anisotropy:
	Anisotropy selection selection selection Simple_name Logical? Simple_name;

proton_shift_amides:
	Amides selection;

proton_shift_carbons:
	Carbons selection;

proton_shift_nitrogens:
	Nitrogens selection;

proton_shift_oxygens:
	Oxygens selection;

proton_shift_ring_atoms:
	RingAtoms Simple_name selection selection selection selection selection selection?;

proton_shift_alphas_and_amides:
	AlphasAndAmides selection;

/* XPLOR-NIH: Dihedral angle database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node410.html
*/
ramachandran_statement:
	rama_assign* |
	Classification Simple_name |
	Cutoff Real |
	ForceConstant Real |
	Gaussian Real Real Real (Real Real Real)? (Real Real Real)? (Real Real Real)? |
	Nrestraints Integer |
	Phase Real Real Real (Real Real Real)? (Real Real Real)? (Real Real Real)? |
	Print Threshold Real (All | (Classification Simple_name)) |
	Quartic Real Real Real (Real Real Real)? (Real Real Real)? (Real Real Real)? |
	Reset |
	Scale Real |
	Shape Gauss_or_Quart |
	Size Dimensions Real Real? Real? Real? |
	Sort |
	Zero;

rama_assign:
	Assign selection selection selection selection (selection selection selection selection)? (selection selection selection selection)? (selection selection selection selection)?;

/* XPLOR-NIH: Radius of gyration restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node413.html
*/
collapse_statement:
	Scale Real |
	Assign selection Real Real |
	Print |
	Reset;

/* XPLOR-NIH: Diffusion anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node415.html
*/
diffusion_statement:
	dani_assign* |
	Classification Simple_name |
	Coefficients Real Real Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset |
	Type Diff_anis_types;

dani_assign:
	Assign selection selection selection selection selection selection Real Real;

/* XPLOR-NIH: Residue-residue position/orientation database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node425.html
*/
orientation_statement:
	orie_assign* |
	Classification Simple_name |
	Cutoff Real |
	Height Real |
	ForceConstant Real |
	Gaussian Real Real Real Real Real Real Real |
	MaxGaussians Integer |
	NewGaussian Real Real Real Real Real Real Real Real |
	Nrestraints Integer |
	Print Threshold Real (All | (Classification Simple_name)) |
	Quartic Real Real Real Real Real Real Real |
	Reset |
	Residue Integer |
	Size Real Real |
	Zero;

orie_assign:
	Assign selection selection selection selection;

/* XPLOR-NIH: Chemical shift anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node427.html
*/
csa_statement:
	csa_assign* |
	Classification Simple_name |
	Scale Real |
	Type Csa_types |
	Coefficients Real Real Real |
	Sigma Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset;

csa_assign:
	Assign selection selection selection selection selection selection selection Real Real Real;

/* XPLOR-NIH: Pseudo chemical shift anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node430.html
*/
pcsa_statement:
	csa_assign* |
	Classification Simple_name |
	Scale Real |
	Coefficients Real Real Real |
	Sigma Real Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset;

/* XPLOR-NIH: One-bond coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node433.html
*/
one_bond_coupling_statement:
	one_bond_assign* |
	Classification Simple_name |
	Coefficients Real Real Real Real Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset;

one_bond_assign:
	Assign selection selection selection selection selection selection selection selection Real Real;

/* XPLOR-NIH: Angle database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node435.html
*/
angle_db_statement:
	angle_db_assign* |
	Classification Simple_name |
	DerivFlag Simple_name |
	Expectation Integer Integer Real |
	Error Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real (All | (Classification Simple_name)) |
	Reset |
	Size Angle_dihedral Integer Integer |
	Zero;

angle_db_assign:
	Assign selection selection selection selection selection selection selection selection selection selection selection selection?;

/* XPLOR-NIH: Paramagnetic relaxation enhancement restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node438.html
*/
pre_statement:
	pre_assign* |
	Classification Equ_op Simple_name |
	ForceConstant Equ_op Simple_name Real |
	Nrestraints Equ_op Integer |
	Potential Equ_op Simple_name Rdc_potential |
	Kconst Equ_op Simple_name Real |
	Omega Equ_op Simple_name Real |
	Tauc Equ_op Simple_name Real Real |
	Print Threshold Real (All | (Classification Simple_name)) |
	Reset |
	Debug;

pre_assign:
	Assign selection selection Real Real;

/* XPLOR-NIH: Paramagnetic pseudocontact shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node442.html
*/
pcs_statement:
	pcs_assign* |
	Classification Simple_name |
	Tolerance Integer |
	Coefficients Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Print Threshold Real (All | (Classification Simple_name)) |
	Reset |
	Save Simple_name |
	Fmed Real Integer |
	ErrOn |
	ErrOff |
	Fon |
	Foff |
	Son |
	Soff |
	Frun Integer;

pcs_assign:
	Assign selection selection selection selection selection Real Real;

/* XPLOR-NIH: Paramagnetic residual dipolar coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node445.html
*/
prdc_statement:
	prdc_assign* |
	Classification Simple_name |
	Tolerance Integer |
	Coefficients Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	ErrOn |
	ErrOff |
	Fmed |
	Fon |
	Foff |
	Frun |
	Print Threshold |
	Reset |
	Save Simple_name |
	Son |
	Soff;

prdc_assign:
	Assign selection selection selection selection selection selection Real Real;

/* XPLOR-NIH: Paramagnetic orientation restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node448.html
*/
porientation_statement:
	porientation_assign* |
	Classification Simple_name |
	ForceConstant Real |
	Nrestraints Integer |
	Print Threshold Real |
	Reset;

porientation_assign:
	Assign selection selection Real Real Real;

/* XPLOR-NIH: Paramagnetic cross-correlation rate restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node450.html
*/
pccr_statement:
	pccr_assign* |
	Classification Simple_name |
	Weip Integer |
	Coefficients Real |
	ForceConstant Real |
	Nrestraints Integer |
	Print Threshold Real |
	Reset |
	Frun Integer;

pccr_assign:
	Assign selection selection selection Real Real;

/* XPLOR-NIH: Hydrogen bond geometry restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node452.html
*/
hbond_statement:
	hbond_assign* |
	Classification Simple_name |
	ForceConstant Real |
	Nrestraints Integer |
	Print Threshold Real |
	Reset;

hbond_assign:
	Assign selection selection selection;

/* Atom selection - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node39.html
*/
selection:
	L_paren selection_expression R_paren;

selection_expression:
	term (Or_op term)*;

term:
	factor (And_op factor)*;

factor:
	L_paren selection_expression R_paren |
	All |
	factor Around Real |
	Atom (Simple_names | Simple_name) (Integers | Integer) (Simple_names | Simple_name) |
	Attribute Abs? Attr_properties Comparison_ops Real |
	BondedTo factor |
	ByGroup factor |
	ByRes factor |
	Chemical (Simple_names | Simple_name (Colon Simple_name)?) |
	Hydrogen |
	Id Integer |
	Known |
	Name (Simple_names | Simple_name (Colon Simple_name)?) |
	Not_op factor |
	Point L_paren Real Comma? Real Comma? Real R_paren Cut Real |
	Point L_paren Tail Equ_op selection Comma? (Head Equ_op selection)? R_paren Cut Real |
	Previous |
	Pseudo |
	Residue (Integers | Integer (Colon Integer)?) |
	Resname (Simple_names | Simple_name (Colon Simple_name)?) |
	factor Saround Real |
	SegIdentifier (Simple_names | Simple_name (Colon Simple_name)? | Double_quote_string (Colon Double_quote_string)?) |
	Store_1 | Store_2 | Store_3 | Store_4 | Store_5 | Store_6 | Store_7 | Store_8 | Store_9 |
	Tag;

/* Three-dimentional vectors - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node15.html

vector_3d:
	L_paren Real Comma? Real Comma? Real R_paren |
	L_paren Tail Equ_op selection Comma? (Head Equ_op selection)? R_paren;
*/
