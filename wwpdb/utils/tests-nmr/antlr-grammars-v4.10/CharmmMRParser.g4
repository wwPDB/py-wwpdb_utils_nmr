/*
 CHARMM MR (Magnetic Restraint) parser grammar for ANTLR v4.
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

parser grammar CharmmMRParser;

options { tokenVocab=CharmmMRLexer; }

charmm_mr:
	(
	comment |
	distance_restraint |
	point_distance_restraint |
	dihedral_angle_restraint |
	harmonic_restraint |
	manipulate_internal_coordinate |
	droplet_potential |
	fix_atom_constraint |
	center_of_mass_constraint |
	fix_bond_or_angle_constraint |
	restrained_distance |
	external_force |
	rmsd_restraint |
	gyration_restraint |
	distance_matrix_restraint |
	set_statement
	)*
	EOF;

comment:
	COMMENT Any_name* (RETURN_CM | EOF);

distance_restraint:
	Noe noe_statement* End;

point_distance_restraint:
	PNoe pnoe_statement* End;

dihedral_angle_restraint:
	Cons (Dihedral dihedral_statement* | ClDh);

harmonic_restraint:
	Cons Harmonic harmonic_statement*;

manipulate_internal_coordinate:
	Cons IC ic_statement*;

droplet_potential:
	Cons Droplet droplet_statement*;

fix_atom_constraint:
	Cons Fix fix_atom_statement*;

center_of_mass_constraint:
	Cons Hmcm center_of_mass_statement*;

fix_bond_or_angle_constraint:
	Shake (fix_bond_or_angle_statement* | Off);

restrained_distance:
	ResDistance restrained_distance_statement*;

external_force:
	Pull external_force_statement*;

rmsd_restraint:
	Cons RMSD (rmsd_statement* | Show | Clear);

gyration_restraint:
	RGyration gyration_statement*;

distance_matrix_restraint:
	DMConstrain distance_matrix_statement*;

/* CHARMM: CONSTRAINTS - Fixing bond lengths or angles during dynamics
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
noe_statement:
	noe_assign |
	Reset |
	KMin number_s |
	RMin number_s |
	KMax number_s |
	RMax number_s |
	FMax number_s |
	MinDist |
	RSwi number_s |
	SExp number_s |
	SumR |
	TCon number_s |
	RExp number_s |
	MPNoe INoe Integer TnoX number_s TnoY number_s TnoZ number_s |
	NMPNoe Integer |
	Read Unit Integer |
	Write Unit Integer Anal? |
	Print (Anal (Cut number_s)?)? |
	Scale number_s |
	Temperature number_s;

noe_assign:
	Assign selection selection;

pnoe_statement:
	pnoe_assign |
	Reset |
	KMin number_s |
	RMin number_s |
	KMax number_s |
	RMax number_s |
	FMax number_s |
	CnoX number_s |
	CnoY number_s |
	CnoZ number_s |
	MinDist |
	RSwi number_s |
	SExp number_s |
	SumR |
	TCon number_s |
	RExp number_s |
	MPNoe INoe Integer TnoX number_s TnoY number_s TnoZ number_s |
	NMPNoe Integer |
	Read Unit Integer |
	Write Unit Integer Anal? |
	Print (Anal (Cut number_s)?)? |
	Scale number_s |
	Temperature number_s;

pnoe_assign:
	Assign selection;

/* CHARMM: CONSTRAINTS - Holding dihedrals near selected values
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
dihedral_statement:
	dihedral_assign |
	Force number_s |
	Min number_s |
	Period Integer |
	Comp |
	Width number_s |
	Main;

dihedral_assign:
	(selection selection selection selection) |
	(ByNumber Integer Integer Integer Integer) |
	(Integer Simple_name Integer Simple_name Integer Simple_name Integer Simple_name) |
	(Simple_name? Integer Simple_name Simple_name? Integer Simple_name Simple_name? Integer Simple_name Simple_name? Integer Simple_name);

/* CHARMM: CONSTRAINTS - Holding atoms in place
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
harmonic_statement:
	(Absolute? absolute_spec* force_const_spec* selection force_const_spec* coordinate_spec?) |
	(Bestfit bestfit_spec? force_const_spec* coordinate_spec?) |
	(Relative bestfit_spec? force_const_spec* selection force_const_spec* selection) |
	Clear;

absolute_spec:
	(Exponent Integer) |
	(XScale number) |
	(YScale number) |
	(ZScale number);

force_const_spec:
	Force number |
	Mass |
	Weight;

bestfit_spec:
	NoRotation |
	NoTranslation;

coordinate_spec:
	Main |
	Comp |
	Keep;

/* CHARMM: CONSTRAINTS - Holding Internal Coordinates near selected values
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
ic_statement:
	Bond number (Exponent Integer)? Upper? |
	Angle number |
	Dihedral number |
	Improper number;

/* CHARMM: CONSTRAINTS - The Quartic Droplet Potential
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
droplet_statement:
	Force number |
	Exponent Integer |
	NoMass;

/* CHARMM: CONSTRAINTS - How to fix atoms rigidly in place
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
fix_atom_statement:
	selection Purg? Bond? Thet? Phi? Imph?;

/* CHARMM: CONSTRAINTS - Constrain centers of mass for selected atoms
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
center_of_mass_statement:
	Force number Weight?
	RefX number
	RefY number
	RefZ number
	selection;

/* CHARMM: CONSTRAINTS - Fixing bond lengths or angles during dynamics
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
fix_bond_or_angle_statement:
	selection selection
	shake_opt |
	fast_opt |
	NoReset;

shake_opt:
	(BonH | Bond | AngH | Angle)
	(Main? | Comp | Parameters)
	(Tol number)?
	(MxIter Integer)?
	(ShkScale number)?;

fast_opt:
	Fast (Water Simple_name)? |
	NoFast;

/* CHARMM: CONSTRAINTS - Restrained Distances
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
restrained_distance_statement:
	Reset |
	(Scale | KVal | RVal) number |
	(EVal | IVal) Integer |
	Positive |
	Negative |
	selection selection;

/* CHARMM: CONSTRAINTS - External Forces
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
external_force_statement:
	Force number |
	(XDir | YDir | ZDir | Period | EField | SForce) number |
	Off |
	List |
	Switch Integer |
	Weight |
	selection;

/* CHAMM: CONSTRAINTS - RMSD Restraints
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
rmsd_statement:
	Relative |
	MaxN Integer |
	NPrt |
	rmsd_orient_spec |
	rmsd_force_const_spec |
	rmsd_coordinate_spec |
	selection;

rmsd_orient_spec:
	NoRotation |
	NoTranslation;

rmsd_force_const_spec:
	Force number |
	Mass |
	Offset number |
	BOffset number;

rmsd_coordinate_spec:
	Main |
	Comp;

/* CHARMM: CONSTRAINTS - Rg/RMSD Restraint
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
gyration_statement:
	Reset |
	(Force | Reference ) number |
	RMSD |
	Comp |
	Orient |
	(Output | NSave) Integer |
	selection;

/* CHARMM: CONSTRAINTS - Distance Matrix Restraint
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
distance_matrix_statement:
	(Force | Reference | Cutoff | Weight) number |
	(Output | NSave | NContact) Integer |
	selection;

/* CHARMM: Atom selection
 See also https://charmm-gui.org/charmmdoc/select.html
*/
selection:
	Selection selection_expression Show? End;

selection_expression:
	term (Or_op term)*;

term:
	factor (And_op factor)*;

factor:
	L_paren selection_expression R_paren |
	All |
	factor Around number_f |
	factor Subset (Integers | Integer (Colon Integer)? | Symbol_name) |
	Atom (Simple_names | Simple_name) (Integers | Integer) (Simple_names | Simple_name) |
	Property Abs? Attr_properties Comparison_ops number_f |
	Bonded factor |
	ByGroup factor |
	ByRes factor |
	Type (Simple_names | Simple_name (Colon Simple_name)? | Symbol_name) |
	Chemical (Simple_names | Simple_name (Colon Simple_name)? | Symbol_name) |
	Initial |
	Lone |
	Hydrogen |
	NONE |
	Not_op factor |
	Point number_f number_f number_f (Cut number_f)? Period? |
	User |
	Previous |
	Recall Integer |
	(ByNumber | Residue) (Integers | Integer (Colon Integer)? | Symbol_name) |
	Resname (Simple_names | Simple_name (Colon Simple_name)? | Symbol_name) |
	SegIdentifier (Simple_names | Simple_name (Colon Simple_name)? | Double_quote_string (Colon Double_quote_string)? | Symbol_name | Integer) |
	(ISeg | IRes | IGroup) Integer Colon Integer;

/* number expression in assign */
number:	Real | Integer | Symbol_name;

/* number expression in factor */
number_f:
	Real | Integer;

/* number expression in statement */
number_s:
	Real | Integer | Symbol_name;

set_statement:
	Set Simple_name_VE Equ_op_VE? (Real_VE | Integer_VE | Simple_name_VE) RETURN_VE;

