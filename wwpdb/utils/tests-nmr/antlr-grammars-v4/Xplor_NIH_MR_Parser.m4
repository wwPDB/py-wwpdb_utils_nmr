/*
 Xplor-NIH MR parser grammar for ANTLR v4.
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

parser grammar Xplor_NIH_MR_Parser;

options { tokenVocab=Xplor_NIH_MR_Lexer; }

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

/* Xplor-NIH: Distance restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node377.html
*/
noe_statement:
	noe_assign* |
	Asymptote Class_names Real |
	Averaging Class_names Noe_avr_methods |
	Bhig Class_names Real |
	Ceiling Equ_op Real |
	Classification Class_name |
	CountViol Class_name |
	Distribute Class_name Class_name Real |
	Monomers Class_names Integer |
	Ncount Class_names Integer |
	Nrestraints Equ_op Integer |
	Potential Class_names Noe_potential |
	Predict L_brace predict_statement R_brace End |
	Print Threshold Equ_op? Real |
	Reset |
	Rswitch Class_names Real |
	Scale Class_names Real |
	SoExponent Class_names Real |
	SqConstant Class_names Real |
	SqExponent Class_names Real |
	SqOffset Class_names Real |
	Temperature Equ_op Real;

noe_assign:
	Assign selection selection Real Real Real (Or_op selection selection)*;

predict_statement:
	Cutoff Equ_op Real | Cuton Equ_op Real | From selection | To selection;

/* Xplor-NIH: Dihedral angle restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/cdih_syntax.html
*/
dihedral_statement:
	dihedral_assign* |
	Nassign Equ_op Integer |
	Reset |
	Scale Real;

dihedral_assign:
	Assign selection selection selection selection Real Real Real Integer;

/* Xplor-NIH: RDC - Syntax (SANI - Susceptibility anisotropy)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node418.html
*/
sani_statement:
	sani_assign* |
	Classification Class_name |
	Coefficients Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset;

sani_assign:
	Assign selection selection selection selection selection selection Real Real;

/* Xplor-NIH: RDC - Syntax (XDIP)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node419.html
*/
xdip_statement:
	xdip_assign* |
	Classification Class_name |
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

/* Xplor-NIH: RDC - Syntax (VEAN)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node420.html
*/
vean_statement:
	vean_assign* |
	Cv Equ_op Integer |
	Classification Class_name |
	ForceConstant Real Real |
	Nrestraints Integer |
	Partition Equ_op Integer |
	Print Threshold Real |
	Reset;

vean_assign:
	Assign selection selection selection selection Real Real Real Real;

/* Xplor-NIH: RDC - Syntax (TENS)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node421.html
*/
tens_statement:
	tens_assign* |
	Classification Class_name |
	Coefficients Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset;

tens_assign:
	Assign selection selection Real Real;

/* Xplor-NIH: RDC - Syntax (ANIS)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node422.html
*/
anis_statement:
	anis_assign* |
	Classification Class_name |
	Coefficients Real Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset |
	Type Rdc_anis_types;

anis_assign:
	Assign selection selection selection selection Real Real;

/* Xplor-NIH: Planality restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/plan_syntax.html
*/
planar_statement:
	Group L_brace group_statement R_brace |
	Initialize;

group_statement:
	Selection Equ_op selection |
	Weight Equ_op Real;

/* Xplor-NIH: Antidiatance restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node398.html
*/
antidistance_statement:
	xadc_assign* |
	Classification Class_name |
	Expectation Integer Real |
	ForceConstant Real |
	Nrestraints Integer |
	Print Threshold Real (All | (Classification Class_name)) |
	Reset |
	Size Real Integer |
	Zero;

xadc_assign:
	Assign selection selection;

/* Xplor-NIH: Scalar J-coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node401.html
*/
coupling_statement:
	coup_assign* |
	Classification Class_name |
	Coefficients Real Real Real Real |
	Cv Equ_op Integer |
	DegEnergy Number_of_couplings |
	ForceConstant Real Real? |
	Nrestraints Integer |
	Partition Equ_op Integer |
	Potential Coupling_potential |
	Print Threshold Real (All | (Classification Class_name)) |
	Reset;

coup_assign:
	Assign selection selection selection selection (selection selection selection selection)? Real Real (Real Real)?;

/* Xplor-NIH: Carbon chemical shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node404.html
*/
carbon_shift_statement:
	carbon_shift_assign* |
	Classification Class_name |
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

/* Xplor-NIH: Proton chemical shift restraints - Syntax
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
	Classification Class_name |
	Error Real |
	DegEnergy Number_of_shifts |
	ForceConstant Real Real? |
	Potential Coupling_potential |
	Print Threshold Real (All | (Classification Class_name)) Rmsd_or_Not |
	Reset;

observed:
	Observed selection selection? Real Real?;

proton_shift_rcoil:
	Rcoil selection Real;

proton_shift_anisotropy:
	Anisotropy selection selection selection CO_or_CN Logical? SC_or_BB;

proton_shift_amides:
	Amides selection;

proton_shift_carbons:
	Carbons selection;

proton_shift_nitrogens:
	Nitrogens selection;

proton_shift_oxygens:
	Oxygens selection;

proton_shift_ring_atoms:
	RingAtoms Ring_resname selection selection selection selection selection selection?;

proton_shift_alphas_and_amides:
	AlphasAndAmides selection;

/* Xplor-NIH: Dihedral angle database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node410.html
*/
ramachandran_statement:
	rama_assign* |
	Classification Class_name |
	Cutoff Real |
	ForceConstant Real |
	Gaussian Real Real Real (Real Real Real)? (Real Real Real)? (Real Real Real)? |
	Nrestraints Integer |
	Phase Real Real Real (Real Real Real)? (Real Real Real)? (Real Real Real)? |
	Print Threshold Real (All | (Classification Class_name)) |
	Quartic Real Real Real (Real Real Real)? (Real Real Real)? (Real Real Real)? |
	Reset |
	Scale Real |
	Shape Gauss_or_Quart |
	Size Dimensions Real Real? Real? Real? |
	Sort |
	Zero;

rama_assign:
	Assign selection selection selection selection (selection selection selection selection)? (selection selection selection selection)? (selection selection selection selection)?;

/* Xplor-NIH: Radius of gyration restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node413.html
*/
collapse_statement:
	Scale Real |
	Assign selection Real Real |
	Print |
	Reset;

/* Xplor-NIH: Diffusion anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node415.html
*/
diffusion_statement:
	dani_assign* |
	Classification Class_name |
	Coefficients Real Real Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset |
	Type Diff_anis_types;

dani_assign:
	Assign selection selection selection selection selection selection Real Real;

/* Xplor-NIH: Residue-residue position/orientation database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node425.html
*/
orientation_statement:
	orie_assign* |
	Classification Class_name |
	Cutoff Real |
	Height Real |
	ForceConstant Real |
	Gaussian Real Real Real Real Real Real Real |
	MaxGaussians Integer |
	NewGaussian Real Real Real Real Real Real Real Real |
	Nrestraints Integer |
	Print Threshold Real (All | (Classification Class_name)) |
	Quartic Real Real Real Real Real Real Real |
	Reset |
	Residues Integer |
	Size Real Real |
	Zero;

orie_assign:
	Assign selection selection selection selection;

/* Xplor-NIH: Chemical shift anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node427.html
*/
csa_statement:
	csa_assign* |
	Classification Class_name |
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

/* Xplor-NIH: Pseudo chemical shift anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node430.html
*/
pcsa_statement:
	csa_assign* |
	Classification Class_name |
	Scale Real |
	Coefficients Real Real Real |
	Sigma Real Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset;

/* Xplor-NIH: One-bond coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node433.html
*/
one_bond_coupling_statement:
	one_bond_assign* |
	Classification Class_name |
	Coefficients Real Real Real Real Real Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real |
	Reset;

one_bond_assign:
	Assign selection selection selection selection selection selection selection selection Real Real;

/* Xplor-NIH: Angle database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node435.html
*/
angle_db_statement:
	angle_db_assign* |
	Classification Class_name |
	DerivFlag On_or_Off |
	Expectation Integer Integer Real |
	Error Real |
	ForceConstant Real |
	Nrestraints Integer |
	Potential Rdc_potential |
	Print Threshold Real (All | (Classification Class_name)) |
	Reset |
	Size Angle_dihedral Integer Integer |
	Zero;

angle_db_assign:
	Assign selection selection selection selection selection selection selection selection selection selection selection selection?;

/* Xplor-NIH: Paramagnetic relaxation enhancement restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node438.html
*/
pre_statement:
	pre_assign* |
	Classification Equ_op Class_name |
	ForceConstant Equ_op Class_name Real |
	Nrestraints Equ_op Integer |
	Potential Equ_op Class_name Rdc_potential |
	Kconst Equ_op Class_name Real |
	Omega Equ_op Class_name Real |
	Tauc Equ_op Class_name Real Real |
	Print Threshold Real (All | (Classification Class_name)) |
	Reset |
	Debug;

pre_assign:
	Assign selection selection Real Real;

/* Xplor-NIH: Paramagnetic pseudocontact shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node442.html
*/
pcs_statement:
	pcs_assign* |
	Classification Class_name |
	Tolerance One_or_Zero |
	Coefficients Real Real |
	ForceConstant Real |
	Nrestraints Integer |
	Print Threshold Real (All | (Classification Class_name)) |
	Reset |
	Save Class_name |
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

/* Xplor-NIH: Paramagnetic residual dipolar coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node445.html
*/
prdc_statement:
	prdc_assign* |
	Classification Class_name |
	Tolerance One_or_Zero |
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
	Save Class_name |
	Son |
	Soff;

prdc_assign:
	Assign selection selection selection selection selection selection Real Real;

/* Xplor-NIH: Paramagnetic orientation restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node448.html
*/
porientation_statement:
	porientation_assign* |
	Classification Class_name |
	ForceConstant Real |
	Nrestraints Integer |
	Print Threshold Real |
	Reset;

porientation_assign:
	Assign selection selection Real Real Real;

/* Xplor-NIH: Paramagnetic cross-correlation rate restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node450.html
*/
pccr_statement:
	pccr_assign* |
	Classification Class_name |
	Weip One_or_Zero |
	Coefficients Real |
	ForceConstant Real |
	Nrestraints Integer |
	Print Threshold Real |
	Reset |
	Frun Integer;

pccr_assign:
	Assign selection selection selection Real Real;

/* Xplor-NIH: Hydrogen bond geometry restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node452.html
*/
hbond_statement:
	hbond_assign* |
	Classification Class_name |
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
	term (L_brace Or_op term R_brace)*;

term:
	factor (L_brace And_op factor R_brace)*;

factor:
	L_paren selection_expression R_paren |
	All |
	factor Around Real |
	Atom Segment_names Residue_numbers Atom_names |
	Attribute Abs? Attr_properties Comparison_ops Real |
	BondedTo factor |
	ByGroup factor |
	ByRes factor |
	Chemical (Atom_types | Atom_type (Colon Atom_type)*) |
	Hydrogen |
	Id Integer |
	Known |
	Name (Atom_names | Atom_name (Colon Atom_name)*) |
	Not_op factor |
	Point vector_3d Cut Real |
	Previous |
	Pseudo |
	Residue (Residue_numbers | Residue_number (Colon Residue_number)*) |
	Resname (Residue_names | Residue_name (Colon Residue_name)*) |
	factor Saround Real |
	SegIdentifier (Segment_names | Segment_name (Colon Segment_name)* | Double_quote_string) |
	Store_1 | Store_2 | Store_3 | Store_4 | Store_5 | Store_6 | Store_7 | Store_8 | Store_9 |
	Tag;

/* Three-dimentional vectors - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node15.html
*/
vector_3d:
	L_paren Real Real Real R_paren |
	L_paren Tail Equ_op selection (Head Equ_op selection)? R_paren;

