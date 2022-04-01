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
	(distance_restraint |
	dihedral_angle_restraint |
	plane_restraint |
	harmonic_restraint |
	rdc_restraint |
	coupling_restraint |
	carbon_shift_restraint |
	proton_shift_restraint |
	conformation_db_restraint |
	diffusion_anisotropy_restraint |
	one_bond_coupling_restraint |
	angle_db_restraint)*
	noe_assign*			// allowing bare assign clauses for Distance restraints
	dihedral_assign*		// allowing bare assign clauses for Dihedral angle restraints
	sani_assign*			// allowing bare assign clauses for RDC restraints
	plane_statement*		// allowing bare group clauses for Plane restraints
	coup_assign*			// allowing bare assign clauses for Scaler J-coupling restraints
	EOF;

distance_restraint:
	Noe noe_statement End;

dihedral_angle_restraint:
	Restraints Dihedral dihedral_statement End;

plane_restraint:
	Restraints Plane plane_statement End;

harmonic_restraint:
	Restraints Harmonic harmonic_statement End;

rdc_restraint:
	Sanisotropy sani_statement End;

coupling_restraint:
	Coupling coupling_statement End;

carbon_shift_restraint:
	Carbon carbon_shift_statement End;

proton_shift_restraint:
	Proton proton_shift_statement End;

conformation_db_restraint:
	Conformation conformation_statement End;

diffusion_anisotropy_restraint:
	Danisotropy diffusion_statement End;

one_bond_coupling_restraint:
	OneBond one_bond_coupling_statement End;

angle_db_restraint:
	AngleDb angle_db_statement End;

/* CNS: Distance restraints - Syntax - noe
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
noe_statement:
	Analysis Equ_op Noe_analysis |
	noe_assign* |
	Asymptote Simple_names number_s |
	Averaging Simple_names Noe_avr_methods |
	Bgig Simple_names number_s |
	Ceiling Equ_op number_s |
	Classification Equ_op Simple_name |
	CountViol Simple_name |
	Cv Equ_op Integer |
	Den Initialize |
	Den Update Gamma Equ_op number_s Kappa Equ_op number_s |
	Distribute Simple_name Simple_name number_s |
	Ensemble *? End |
	Monomers Simple_names Integer |
	Ncount Simple_names Integer |
	Nrestraints Equ_op Integer |
	Outd |
	Partition Equ_op Integer |
	Potential Simple_names Noe_potential |
	Predict predict_statement End |
	Print Threshold Equ_op number_s |
	Raverage Simple_name *? End |
	Reset |
	Rswitch Simple_names number_s |
	Scale Simple_names number_s |
	SoExponent Simple_names number_s |
	SqConstant Simple_names number_s |
	SqExponent Simple_names number_s |
	SqOffset Simple_names number_s |
	Taverage Simple_name *? End |
	Temperature Equ_op number_s;

noe_assign:
	Assign selection selection number number number (Or_op selection selection)*;

predict_statement:
	Cutoff Equ_op number_s | Cuton Equ_op number_s | From selection | To selection;

/* CNS: Dihedral angle restraints - Syntax - restranits/dihedral
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
dihedral_statement:
	dihedral_assign* |
	Cv Equ_op Integer |
	Nassign Equ_op Integer |
	Partition Equ_op Integer |
	Reset |
	Scale Equ_op number_s |
	Print_any;

dihedral_assign:
	Assign selection selection selection selection number number number Integer;

/* CNS: Plane restraints - Syntax - restraints/plane
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
plane_statement:
	Group group_statement |
	Initialize |
	Print_any;

group_statement:
	Selection Equ_op selection |
	Weight Equ_op number_s;

/* CNS: Plane restraints - Syntax - restraints/harmonic
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
harmonic_statement:
	Exponent Equ_op Integer |
	Normal Equ_op L_paren (number_s Comma? number_s Comma? number_s | Tail Equ_op selection Comma? (Head Equ_op selection)?) R_paren;

/* CNS: Suscetibility anisotropy restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
sani_statement:
	sani_assign* |
	Classification Equ_op Simple_name |
	Coefficients number_s number_s number_s |
	ForceConstant Equ_op number_s |
	Nrestraints Equ_op Integer |
	Potential Equ_op Rdc_potential |
	Print Threshold number_s |
	Reset;

sani_assign:
	Assign selection selection selection selection selection selection number number number?;

/* CNS: Scalar J-coupling restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
coupling_statement:
	coup_assign* |
	Classification Equ_op Simple_name |
	Coefficients number_s number_s number_s number_s |
	Cv Equ_op Integer |
	ForceConstant number_s number_s? |
	Nrestraints Equ_op Integer |
	Partition Equ_op Integer |
	Potential Equ_op Coupling_potential |
	Print Threshold number_s (All | (Classification Equ_op Simple_name)) |
	Reset;

coup_assign:
	Assign selection selection selection selection (selection selection selection selection)? number number (number number)?;

/* CNS: Carbon chemical shift restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
carbon_shift_statement:
	carbon_shift_assign* |
	Classification Equ_op Simple_name |
	Expectation Integer Integer number_s number_s number_s |
	ForceConstant Equ_op number_s |
	Nrestraints Equ_op Integer |
	PhiStep Equ_op number_s |
	PsiStep Equ_op number_s |
	Potential Equ_op Rdc_potential |
	Print Threshold number_s |
	carbon_shift_rcoil* |
	Reset |
	Zero;

carbon_shift_assign:
	Assign selection selection selection selection selection number number;

carbon_shift_rcoil:
	Rcoil selection number_s number_s;

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
	Error Equ_op? number_s |
	ForceConstant number_s number_s? |
	Potential Coupling_potential |
	Print Threshold number_s (All | (Classification Equ_op Simple_name)) Simple_name |
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

/* CNS: Conformation database restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
conformation_statement:
	conf_assign* |
	Classification Equ_op Simple_name |
	Compressed |
	Expectation Integer Integer? Integer? Integer? number_s |
	Error Equ_op number_s |
	ForceConstant Equ_op number_s |
	Nrestraints Equ_op Integer |
	Phase Integer Integer Integer (Integer Integer Integer)? (Integer Integer Integer)? (Integer Integer Integer)? |
	Potential Equ_op Rdc_potential |
	Print Threshold number_s (All | (Classification Equ_op Simple_name)) |
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
	Coefficients number_s number_s number_s number_s number_s |
	ForceConstant Equ_op number_s |
	Nrestraints Equ_op Integer |
	Potential Equ_op Rdc_potential |
	Print Threshold number_s |
	Reset;

dani_assign:
	Assign selection selection selection selection selection selection number number;

/* CNS: One-bond coupling restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
one_bond_coupling_statement:
	one_bond_assign* |
	Classification Equ_op Simple_name |
	Coefficients number_s number_s number_s number_s number_s number_s number_s |
	ForceConstant Equ_op number_s |
	Nrestraints Equ_op Integer |
	Potential Equ_op Rdc_potential |
	Print Threshold number_s |
	Reset;

one_bond_assign:
	Assign selection selection selection selection selection selection selection selection number number;

/* CNS: Angle database restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
angle_db_statement:
	angle_db_assign* |
	Classification Equ_op Simple_name |
	DerivFlag Equ_op Simple_name |
	Expectation Integer Integer number_s |
	Error Equ_op number_s |
	ForceConstant Equ_op number_s |
	Nrestraints Equ_op Integer |
	Potential Equ_op Rdc_potential |
	Print Threshold number_s (All | (Classification Equ_op Simple_name)) |
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
	factor Around number_f |
	Atom (Simple_names | Simple_name) (Integers | Integer) (Simple_names | Simple_name) |
	Attribute Abs? Attr_properties Comparison_ops number_f |
	BondedTo factor |
	ByGroup factor |
	ByRes factor |
	Chemical (Simple_names | Simple_name (Colon Simple_name)?) |
	Fbox number_f number_f number_f number_f number_f number_f |
	Hydrogen |
	Id Integer |
	Known |
	Name (Simple_names | Simple_name (Colon Simple_name)?) |
	NONE |
	Not_op factor |
	Point L_paren number_f Comma? number_f Comma? number_f R_paren Cut number_f |
	Point L_paren Tail Equ_op selection Comma? (Head Equ_op selection)? R_paren Cut number_f |
	Previous |
	Pseudo |
	Residue (Integers | Integer (Colon Integer)?) |
	Resname (Simple_names | Simple_name (Colon Simple_name)?) |
	factor Saround number_f |
	SegIdentifier (Simple_names | Simple_name (Colon Simple_name)? | Double_quote_string (Colon Double_quote_string)?) |
	Sfbox number_f number_f number_f number_f number_f number_f |
	Store_1 | Store_2 | Store_3 | Store_4 | Store_5 | Store_6 | Store_7 | Store_8 | Store_9 |
	Tag;

/* Three-dimentional vectors - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html

vector_3d:
	L_paren number_f Comma? number_f Comma? number_f R_paren |
	L_paren Tail Equ_op selection Comma? (Head Equ_op selection)? R_paren;
*/

/* number expression in assign */
number: Real | Integer;

/* number expression in factor */
number_f:
	Real | Integer;

/* number expression in statement */
number_s:
	Real | Integer;

