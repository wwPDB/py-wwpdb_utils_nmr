/*
 CNS MR (Magnetic Restraint) parser grammar for ANTLR v4.
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

parser grammar CnsMRParser;

options { tokenVocab=CnsMRLexer; }

cns_mr:
	distance_restraint*
	dihedral_angle_restraint*
	plane_restraint*
	harmonic_restraint*
	rdc_restraint*
	coupling_restraint*
	carbon_shift_restraint*
	proton_shift_restraint*
	conformation_db_restraint*
	diffusion_anisotropy_restraint*
	one_bond_coupling_restraint*
	angle_db_restraint*
	noe_assign*			// allowing bare assign clauses for distance restraints
	dihedral_assign*		// allowing bare assign clauses for dihedral angle restraints
	sani_assign*			// allowing bare assign clauses for RDC restraints
	plane_statement*		// allowing bare group clauses for plane restraints
	EOF;

distance_restraint:
	Noe L_brace noe_statement R_brace End;

dihedral_angle_restraint:
	Restraints Dihedral L_brace dihedral_statement R_brace End;

plane_restraint:
	Restraints Plane L_brace plane_statement R_brace End;

harmonic_restraint:
	Restraints Harmonic L_brace harmonic_statement R_brace End;

rdc_restraint:
	Sanisotropy L_brace sani_statement R_brace End;

coupling_restraint:
	Coupling L_brace coupling_statement R_brace End;

carbon_shift_restraint:
	Carbon L_brace carbon_shift_statement R_brace End;

proton_shift_restraint:
	Proton L_brace proton_shift_statement R_brace End;

conformation_db_restraint:
	Conformation L_brace conformation_statement R_brace End;

diffusion_anisotropy_restraint:
	Danisotropy L_brace diffusion_statement R_brace End;

one_bond_coupling_restraint:
	OneBond L_brace one_bond_coupling_statement R_brace End;

angle_db_restraint:
	AngleDb L_brace angle_db_statement R_brace End;

/* CNS: Distance restraints - Syntax - noe
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
noe_statement:
	Analysis Equ_op Noe_analysis |
	noe_assign* |
	Asymptote Simple_names Real |
	Averaging Simple_names Noe_avr_methods |
	Bgig Simple_names Real |
	Ceiling Equ_op Real |
	Classification Equ_op Simple_name |
	CountViol Simple_name |
	Cv Equ_op Integer |
	Den Initialize |
	Den Update Gamma Equ_op Real Kappa Equ_op Real |
	Distribute Simple_name Simple_name Real |
	Ensemble L_brace *? R_brace End |
	Monomers Simple_names Integer |
	Ncount Simple_names Integer |
	Nrestraints Equ_op Integer |
	Outd |
	Partition Equ_op Integer |
	Potential Simple_names Noe_potential |
	Predict L_brace predict_statement R_brace End |
	Print Threshold Equ_op Real |
	Raverage Simple_name L_brace *? R_brace End |
	Reset |
	Rswitch Simple_names Real |
	Scale Simple_names Real |
	SoExponent Simple_names Real |
	SqConstant Simple_names Real |
	SqExponent Simple_names Real |
	SqOffset Simple_names Real |
	Taverage Simple_name L_brace *? R_brace End |
	Temperature Equ_op Real;

noe_assign:
	Assign selection selection Real Real Real (Or_op selection selection)*;

predict_statement:
	Cutoff Equ_op Real | Cuton Equ_op Real | From selection | To selection;

/* CNS: Dihedral angle restraints - Syntax - restranits/dihedral
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
dihedral_statement:
	dihedral_assign* |
	Cv Equ_op Integer |
	Nassign Equ_op Integer |
	Partition Equ_op Integer |
	Reset |
	Scale Equ_op Real |
	Print_any;

dihedral_assign:
	Assign selection selection selection selection Real Real Real Integer;

/* CNS: Plane restraints - Syntax - restraints/plane
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
plane_statement:
	Group L_brace group_statement R_brace |
	Initialize |
	Print_any;

group_statement:
	Selection Equ_op selection |
	Weight Equ_op Real;

/* CNS: Plane restraints - Syntax - restraints/harmonic
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
harmonic_statement:
	Exponent Equ_op Integer |
	Normal Equ_op vector_3d;

/* CNS: Suscetibility anisotropy restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
sani_statement:
	sani_assign* |
	Classification Equ_op Simple_name |
	Coefficients Real Real Real |
	ForceConstant Equ_op Real |
	Nrestraints Equ_op Integer |
	Potential Equ_op Rdc_potential |
	Print Threshold Real |
	Reset;

sani_assign:
	Assign selection selection selection selection selection selection Real Real;

/* CNS: Scalar J-coupling restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
coupling_statement:
	coup_assign* |
	Classification Equ_op Simple_name |
	Coefficients Real Real Real Real |
	Cv Equ_op Integer |
	ForceConstant Real Real? |
	Nrestraints Equ_op Integer |
	Partition Equ_op Integer |
	Potential Equ_op Coupling_potential |
	Print Threshold Real (All | (Classification Equ_op Simple_name)) |
	Reset;

coup_assign:
	Assign selection selection selection selection (selection selection selection selection)? Real Real (Real Real)?;

/* CNS: Carbon chemical shift restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
carbon_shift_statement:
	carbon_shift_assign* |
	Classification Equ_op Simple_name |
	Expectation Integer Integer Real Real Real |
	ForceConstant Equ_op Real |
	Nrestraints Equ_op Integer |
	PhiStep Equ_op Real |
	PsiStep Equ_op Real |
	Potential Equ_op Rdc_potential |
	Print Threshold Real |
	carbon_shift_rcoil* |
	Reset |
	Zero;

carbon_shift_assign:
	Assign selection selection selection selection selection Real Real;

carbon_shift_rcoil:
	Rcoil selection Real Real;

/* CNS: Proton chemical shift restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
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
	Classification Equ_op Simple_name |
	Error Equ_op? Real |
	ForceConstant Real Real? |
	Potential Coupling_potential |
	Print Threshold Real (All | (Classification Equ_op Simple_name)) Simple_name |
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

/* CNS: Conformation database restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
conformation_statement:
	conf_assign* |
	Classification Equ_op Simple_name |
	Compressed |
	Expectation Integer Integer? Integer? Integer? Real |
	Error Equ_op Real |
	ForceConstant Equ_op Real |
	Nrestraints Equ_op Integer |
	Phase Integer Integer Integer (Integer Integer Integer)? (Integer Integer Integer)? (Integer Integer Integer)? |
	Potential Equ_op Rdc_potential |
	Print Threshold Real (All | (Classification Equ_op Simple_name)) |
	Reset |
	Size Dimensions Integer Integer? Integer? Integer? |
	Zero;

conf_assign:
	Assign selection selection selection selection (selection selection selection selection)? (selection selection selection selection)? (selection selection selection selection)?;

/* CNS: Diffusion anisotropy restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
diffusion_statement:
	dani_assign* |
	Classification Equ_op Simple_name |
	Coefficients Real Real Real Real Real |
	ForceConstant Equ_op Real |
	Nrestraints Equ_op Integer |
	Potential Equ_op Rdc_potential |
	Print Threshold Real |
	Reset;

dani_assign:
	Assign selection selection selection selection selection selection Real Real;

/* CNS: One-bond coupling restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
one_bond_coupling_statement:
	one_bond_assign* |
	Classification Equ_op Simple_name |
	Coefficients Real Real Real Real Real Real Real |
	ForceConstant Equ_op Real |
	Nrestraints Equ_op Integer |
	Potential Equ_op Rdc_potential |
	Print Threshold Real |
	Reset;

one_bond_assign:
	Assign selection selection selection selection selection selection selection selection Real Real;

/* CNS: Angle database restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
angle_db_statement:
	angle_db_assign* |
	Classification Equ_op Simple_name |
	DerivFlag Equ_op Simple_name |
	Expectation Integer Integer Real |
	Error Equ_op Real |
	ForceConstant Equ_op Real |
	Nrestraints Equ_op Integer |
	Potential Equ_op Rdc_potential |
	Print Threshold Real (All | (Classification Equ_op Simple_name)) |
	Reset |
	Size Angle_dihedral Integer Integer |
	Zero;

angle_db_assign:
	Assign selection selection selection selection selection selection selection selection selection selection selection selection?;

/* Atom selection - Syntax - identity/atom-selection
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
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
	Atom Simple_names Integers Simple_names |
	Attribute Abs? Simple_name Comparison_ops Real |
	Attribute Chemical String_comp_ops Simple_name |
	Attribute Name String_comp_ops Simple_name |
	Attribute Abs? Residue Comparison_ops Integer |
	Attribute Resname String_comp_ops Simple_name |
	Attribute SegIdentifier String_comp_ops Simple_name |
	BondedTo factor |
	ByGroup factor |
	ByRes factor |
	Chemical (Simple_names | Simple_name (Colon Simple_name)*) |
	Fbox Real Real Real Real Real Real |
	Hydrogen |
	Id Integer |
	Known |
	Name (Simple_names | Simple_name (Colon Simple_name)*) |
	Not_op factor |
	Point vector_3d Cut Real |
	Previous |
	Pseudo |
	Residue (Integers | Integer (Colon Integer)*) |
	Resname (Simple_names | Simple_name (Colon Simple_name)*) |
	factor Saround Real |
	SegIdentifier (Simple_names | Simple_name (Colon Simple_name)* | Double_quote_string) |
	Sfbox Real Real Real Real Real Real |
	Store_1 | Store_2 | Store_3 | Store_4 | Store_5 | Store_6 | Store_7 | Store_8 | Store_9 |
	Tag;

/* Three-dimentional vectors - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
vector_3d:
	L_paren Real Comma? Real Comma? Real R_paren |
	L_paren Tail Equ_op selection Comma? (Head Equ_op selection)? R_paren;

