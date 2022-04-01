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
	(distance_restraint |
	dihedral_angle_restraint |
	rdc_restraint |
	planar_restraint |
	antidistance_restraint |
	coupling_restraint |
	carbon_shift_restraint |
	proton_shift_restraint |
	dihedral_angle_db_restraint |
	radius_of_gyration_restraint |
	diffusion_anisotropy_restraint |
	orientation_db_restraint |
	csa_restraint |
	pcsa_restraint |
	one_bond_coupling_restraint |
	angle_db_restraint |
	pre_restraint |
	pcs_restraint |
	prdc_restraint |
	porientation_restraint |
	pccr_restraint |
	hbond_restraint)*
	noe_assign*			// allowing bare assign clauses for Distance restraints
	dihedral_assign*		// allowing bare assign clauses for Dihedral angle restraints
	sani_assign*			// allowing bare assign clauses for RDC restraints
	planar_statement*		// allowing bare group clauses for Planer restraints
	hbond_assign*			// allowing bare assign clauses for Hydrogen bond restraints
	coup_assign*			// allowing bare assign clauses for Scaler J-coupling restraints
	xadc_assign*			// allowing bare assign clauses for Antidistance restraints
	coll_assign*			// allowing bare assign clauses for Radius of gyration restraints
	csa_assign*			// allowing bare assign clauses for CSA restraints
	pre_assign*			// allowing bare assign clauses for PRE restraints
	pcs_assign*			// allowing bare assign clauses for PCS restraints
	EOF;

distance_restraint:
	Noe noe_statement End;

dihedral_angle_restraint:
	Restraints Dihedral dihedral_statement End;

rdc_restraint:
	Sanisotropy sani_statement End |
	(Xdipolar | Dipolar) xdip_statement End |
	VectorAngle vean_statement End |
	Tensor tenso_statement End |
	Anisotropy anis_statement End;

planar_restraint:
	Restraints Planar planar_statement End;

antidistance_restraint:
	Xadc antidistance_statement End;

coupling_restraint:
	Coupling coupling_statement End;

carbon_shift_restraint:
	Carbon carbon_shift_statement End;

proton_shift_restraint:
	Proton proton_shift_statement End;

dihedral_angle_db_restraint:
	Ramachandran ramachandran_statement End;

radius_of_gyration_restraint:
	Collapse collapse_statement End;

diffusion_anisotropy_restraint:
	Danisotropy diffusion_statement End;

orientation_db_restraint:
	Orient orientation_statement End;

csa_restraint:
	Dcsa csa_statement End;

pcsa_restraint:
	Pcsa pcsa_statement End;

one_bond_coupling_restraint:
	OneBond one_bond_coupling_statement End;

angle_db_restraint:
	AngleDb angle_db_statement End;

pre_restraint:
	Paramagnetic pre_statement End;

pcs_restraint:
	Xpcs pcs_statement End;

prdc_restraint:
	Xrdcoupling prdc_statement End;

porientation_restraint:
	Xangle porientation_statement End;

pccr_restraint:
	Xccr pccr_statement End;

hbond_restraint:
	Hbda hbond_statement End;

/* XPLOR-NIH: Distance restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node377.html
*/
noe_statement:
	noe_assign* |
	Asymptote Simple_names number_s |
	Averaging Simple_names Noe_avr_methods |
	Bhig Simple_names number_s |
	Ceiling Equ_op number_s |
	Classification Simple_name |
	CountViol Simple_name |
	Distribute Simple_name Simple_name number_s |
	Monomers Simple_names Integer |
	Ncount Simple_names Integer |
	Nrestraints Equ_op Integer |
	Potential Simple_names Noe_potential |
	Predict predict_statement End |
	Print Threshold Equ_op? number_s |
	Reset |
	Rswitch Simple_names number_s |
	Scale Simple_names number_s |
	SoExponent Simple_names number_s |
	SqConstant Simple_names number_s |
	SqExponent Simple_names number_s |
	SqOffset Simple_names number_s |
	Temperature Equ_op number_s;

noe_assign:
	Assign selection selection number number number (Or_op selection selection)*;

predict_statement:
	Cutoff Equ_op number_s | Cuton Equ_op number_s | From selection | To selection;

/* XPLOR-NIH: Dihedral angle restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/cdih_syntax.html
*/
dihedral_statement:
	dihedral_assign* |
	Nassign Equ_op Integer |
	Reset |
	Scale number_s;

dihedral_assign:
	Assign selection selection selection selection number number number Integer;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (SANI - Susceptibility anisotropy)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node418.html
*/
sani_statement:
	sani_assign* |
	Classification Simple_name |
	Coefficients number_s number_s number_s |
	ForceConstant number_s |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold number_s |
	Reset;

sani_assign:
	Assign selection selection selection selection selection selection number number number?;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (XDIP)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node419.html
*/
xdip_statement:
	xdip_assign* |
	Classification Simple_name |
	Type Rdc_dist_fix_types |
	Scale number_s |
	Sign Logical |
	Average Rdc_avr_methods |
	Coefficients number_s number_s number_s |
	ForceConstant number_s |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold number_s |
	Reset;

xdip_assign:
	Assign selection selection selection selection selection selection number number (number | number number number number)?;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (VEAN)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node420.html
*/
vean_statement:
	vean_assign* |
	Cv Equ_op Integer |
	Classification Simple_name |
	ForceConstant number_s number_s |
	Nrestraints Integer |
	Partition Equ_op Integer |
	Print Threshold number_s |
	Reset;

vean_assign:
	Assign selection selection selection selection number number number number;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (TENSO)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node421.html
*/
tenso_statement:
	tenso_assign* |
	Classification Simple_name |
	Coefficients number_s |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold number_s |
	Reset;

tenso_assign:
	Assign selection selection number number;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (ANIS)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node422.html
*/
anis_statement:
	anis_assign* |
	Classification Simple_name |
	Coefficients number_s number_s number_s number_s |
	ForceConstant number_s |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold number_s |
	Reset |
	Type Rdc_anis_types;

anis_assign:
	Assign selection selection selection selection number number;

/* XPLOR-NIH: Planality restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/plan_syntax.html
*/
planar_statement:
	Group group_statement |
	Initialize;

group_statement:
	Selection Equ_op selection |
	Weight Equ_op number_s;

/* XPLOR-NIH: Antidiatance restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node398.html
*/
antidistance_statement:
	xadc_assign* |
	Classification Simple_name |
	Expectation Integer number_s |
	ForceConstant number_s |
	Nrestraints Integer |
	Print Threshold number_s (All | (Classification Simple_name)) |
	Reset |
	Size number_s Integer |
	Zero;

xadc_assign:
	Assign selection selection;

/* XPLOR-NIH: Scalar J-coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node401.html
*/
coupling_statement:
	coup_assign* |
	Classification Simple_name |
	Coefficients number_s number_s number_s number_s |
	Cv Equ_op Integer |
	DegEnergy Integer |
	ForceConstant number_s number_s? |
	Nrestraints Integer |
	Partition Equ_op Integer |
	Potential Coupling_potential |
	Print Threshold number_s (All | (Classification Simple_name)) |
	Reset;

coup_assign:
	Assign selection selection selection selection (selection selection selection selection)? number number (number number)?;

/* XPLOR-NIH: Carbon chemical shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node404.html
*/
carbon_shift_statement:
	carbon_shift_assign* |
	Classification Simple_name |
	Expectation Integer Integer number_s number_s number_s |
	ForceConstant number_s |
	Nrestraints Integer |
	PhiStep number_s |
	PsiStep number_s |
	Potential Rdc_potential |
	Print Threshold number_s |
	carbon_shift_rcoil* |
	Reset |
	Zero;

carbon_shift_assign:
	Assign selection selection selection selection selection number number;

carbon_shift_rcoil:
	Rcoil selection number_s number_s;

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
	Error number_s |
	DegEnergy Integer |
	ForceConstant number_s number_s? |
	Potential Coupling_potential |
	Print Threshold number_s (All | (Classification Simple_name)) Simple_name |
	Reset;

observed:
	Observed selection selection? number_s number_s?;

proton_shift_rcoil:
	Rcoil selection number_s;

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
	Cutoff number_s |
	ForceConstant number_s |
	Gaussian number_s number_s number_s (number_s number_s number_s)? (number_s number_s number_s)? (number_s number_s number_s)? |
	Nrestraints Integer |
	Phase number_s number_s number_s (number_s number_s number_s)? (number_s number_s number_s)? (number_s number_s number_s)? |
	Print Threshold number_s (All | (Classification Simple_name)) |
	Quartic number_s number_s number_s (number_s number_s number_s)? (number_s number_s number_s)? (number_s number_s number_s)? |
	Reset |
	Scale number_s |
	Shape Gauss_or_Quart |
	Size Dimensions number_s number_s? number_s? number_s? |
	Sort |
	Zero;

rama_assign:
	Assign selection selection selection selection (selection selection selection selection)? (selection selection selection selection)? (selection selection selection selection)?;

/* XPLOR-NIH: Radius of gyration restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node413.html
*/
collapse_statement:
	coll_assign* |
	Scale number_s |
	Print |
	Reset;

coll_assign:
	Assign selection number number;

/* XPLOR-NIH: Diffusion anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node415.html
*/
diffusion_statement:
	dani_assign* |
	Classification Simple_name |
	Coefficients number_s number_s number_s number_s number_s |
	ForceConstant number_s |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold number_s |
	Reset |
	Type Diff_anis_types;

dani_assign:
	Assign selection selection selection selection selection selection number number;

/* XPLOR-NIH: Residue-residue position/orientation database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node425.html
*/
orientation_statement:
	orie_assign* |
	Classification Simple_name |
	Cutoff number_s |
	Height number_s |
	ForceConstant number_s |
	Gaussian number_s number_s number_s number_s number_s number_s number_s |
	MaxGaussians Integer |
	NewGaussian number_s number_s number_s number_s number_s number_s number_s number_s |
	Nrestraints Integer |
	Print Threshold number_s (All | (Classification Simple_name)) |
	Quartic number_s number_s number_s number_s number_s number_s number_s |
	Reset |
	Residue Integer |
	Size number_s number_s |
	Zero;

orie_assign:
	Assign selection selection selection selection;

/* XPLOR-NIH: Chemical shift anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node427.html
*/
csa_statement:
	csa_assign* |
	Classification Simple_name |
	Scale number_s |
	Type Csa_types |
	Coefficients number_s number_s number_s |
	Sigma number_s number_s number_s |
	ForceConstant number_s |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold number_s |
	Reset;

csa_assign:
	Assign selection selection selection selection selection selection selection number number number;

/* XPLOR-NIH: Pseudo chemical shift anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node430.html
*/
pcsa_statement:
	csa_assign* |
	Classification Simple_name |
	Scale number_s |
	Coefficients number_s number_s number_s |
	Sigma number_s number_s number_s number_s |
	ForceConstant number_s |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold number_s |
	Reset;

/* XPLOR-NIH: One-bond coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node433.html
*/
one_bond_coupling_statement:
	one_bond_assign* |
	Classification Simple_name |
	Coefficients number_s number_s number_s number_s number_s number_s number_s |
	ForceConstant number_s |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold number_s |
	Reset;

one_bond_assign:
	Assign selection selection selection selection selection selection selection selection number number;

/* XPLOR-NIH: Angle database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node435.html
*/
angle_db_statement:
	angle_db_assign* |
	Classification Simple_name |
	DerivFlag Simple_name |
	Expectation Integer Integer number_s |
	Error number_s |
	ForceConstant number_s |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold number_s (All | (Classification Simple_name)) |
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
	ForceConstant Equ_op Simple_name number_s |
	Nrestraints Equ_op Integer |
	Potential Equ_op Simple_name Rdc_potential |
	Kconst Equ_op Simple_name number_s |
	Omega Equ_op Simple_name number_s |
	Tauc Equ_op Simple_name number_s number_s |
	Print Threshold number_s (All | (Classification Simple_name)) |
	Reset |
	Debug;

pre_assign:
	Assign selection selection number number;

/* XPLOR-NIH: Paramagnetic pseudocontact shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node442.html
*/
pcs_statement:
	pcs_assign* |
	Classification Simple_name |
	Tolerance Integer |
	Coefficients number_s number_s |
	ForceConstant number_s |
	Nrestraints Integer |
	Print Threshold number_s (All | (Classification Simple_name)) |
	Reset |
	Save Simple_name |
	Fmed number_s Integer |
	ErrOn |
	ErrOff |
	Fon |
	Foff |
	Son |
	Soff |
	Frun Integer;

pcs_assign:
	Assign selection selection selection selection selection number number;

/* XPLOR-NIH: Paramagnetic residual dipolar coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node445.html
*/
prdc_statement:
	prdc_assign* |
	Classification Simple_name |
	Tolerance Integer |
	Coefficients number_s number_s |
	ForceConstant number_s |
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
	Assign selection selection selection selection selection selection number number;

/* XPLOR-NIH: Paramagnetic orientation restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node448.html
*/
porientation_statement:
	porientation_assign* |
	Classification Simple_name |
	ForceConstant number_s |
	Nrestraints Integer |
	Print Threshold number_s |
	Reset;

porientation_assign:
	Assign selection selection number number number;

/* XPLOR-NIH: Paramagnetic cross-correlation rate restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node450.html
*/
pccr_statement:
	pccr_assign* |
	Classification Simple_name |
	Weip Integer |
	Coefficients number_s |
	ForceConstant number_s |
	Nrestraints Integer |
	Print Threshold number_s |
	Reset |
	Frun Integer;

pccr_assign:
	Assign selection selection selection number number;

/* XPLOR-NIH: Hydrogen bond geometry restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node452.html
*/
hbond_statement:
	hbond_assign* |
	Classification Simple_name |
	ForceConstant number_s |
	Nrestraints Integer |
	Print Threshold number_s |
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
	factor Around number_f |
	Atom (Simple_names | Simple_name) (Integers | Integer) (Simple_names | Simple_name) |
	Attribute Abs? Attr_properties Comparison_ops number_f |
	BondedTo factor |
	ByGroup factor |
	ByRes factor |
	Chemical (Simple_names | Simple_name (Colon Simple_name)?) |
	Hydrogen |
	Id Integer |
	Known |
	Name (Simple_names | Simple_name (Colon Simple_name)?) |
	Not_op factor |
	Point L_paren number_f Comma? number_f Comma? number_f R_paren Cut number_f |
	Point L_paren Tail Equ_op selection Comma? (Head Equ_op selection)? R_paren Cut number_f |
	Previous |
	Pseudo |
	Residue (Integers | Integer (Colon Integer)?) |
	Resname (Simple_names | Simple_name (Colon Simple_name)?) |
	factor Saround number_f |
	SegIdentifier (Simple_names | Simple_name (Colon Simple_name)? | Double_quote_string (Colon Double_quote_string)?) |
	Store_1 | Store_2 | Store_3 | Store_4 | Store_5 | Store_6 | Store_7 | Store_8 | Store_9 |
	Tag;

/* Three-dimentional vectors - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node15.html

vector_3d:
	L_paren number_f Comma? number_f Comma? number_f R_paren |
	L_paren Tail Equ_op selection Comma? (Head Equ_op selection)? R_paren;
*/

/* number expression in assign */
number:	Real | Integer;

/* number expression in factor */
number_f:
	Real | Integer;

number_s:
	Real | Integer;

