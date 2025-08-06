/*
 SCHRODINGER MR (Magnetic Restraint) parser grammar for ANTLR v4.
 Copyright 2025 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

parser grammar SchrodingerMRParser;

options { tokenVocab=SchrodingerMRLexer; }

schrodinger_mr:
	(
	import_structure |
	distance_restraint |
	dihedral_angle_restraint |
	angle_restraint |
	distance_assign |		// allowing bare assign clauses for Distance restraints
	dihedral_angle_assign |		// allowing bare assign clauses for Dihedral angle restraints
	angle_assign |			// allowing bare assign clauses for angle restraints
	parameter_statement
	)*
	EOF;

import_structure:
	Struct struct_statement+ End_SM;

struct_statement:
	Param_name Equ_op_SM Param_name RETURN_SM;

distance_restraint:
	Dist distance_statement End;

dihedral_angle_restraint:
	Tors dihedral_angle_statement End;

angle_restraint:
	Angle angle_statement End;

distance_statement:
	parameter_statement |
	Atom1 Atom2 Lo Up Fc |
	distance_assign+ |
	distance_assign_unsupported+;

distance_assign:
	selection selection number number number;

distance_assign_unsupported:
	Integer Integer number number number;

dihedral_angle_statement:
	parameter_statement |
	Atom1 Atom2 Atom3 Atom4 Target Fc |
	dihedral_angle_assign+ |
	dihedral_angle_assign_unsupported+;

dihedral_angle_assign:
	selection selection selection selection number number;

dihedral_angle_assign_unsupported:
	Integer Integer Integer Integer number number;

angle_statement:
	parameter_statement |
	Atom1 Atom2 Atom3 Target Fc |
	angle_assign+ |
	angle_assign_unsupported+;

angle_assign:
	selection selection selection number number;

angle_assign_unsupported:
	Integer Integer Integer number number;

/* Atom Selection Language - ASL
  See also https://shaker.umh.es/computing/Schrodinger_suites/maestro_command_reference.pdf
*/
selection:
	L_paren selection_expression R_paren;

selection_expression:
	term (Or_op term)*;

term:
	factor (And_op? factor)*;

factor:
	L_paren selection_expression R_paren |
	(Entry | Entry_name) ((Simple_names | Simple_name) (Comma (Simple_names | Simple_name))*) |
	(Molecule | Molecule_number) (Integers | IntRange | Integer (Comma Integer)*) |
	Molecule_modulo Integer Integer |
	Molecule_entrynum Integer |
	Molecule_atoms (IntRange | Integer | ((Equ_op | Lt_op | Gt_op | Leq_op | Geq_op) Integer)) |
	Molecule_weight (IntRange | Integer | ((Equ_op | Lt_op | Gt_op | Leq_op | Geq_op) Integer)) |
	(Chain | Chain_name) ((Simple_names | Simple_name) (Comma (Simple_names | Simple_name))*) |
	(Residue | Residue_name_or_number) ((IntRange | Integer | (Equ_op | Lt_op | Gt_op | Leq_op | Geq_op) Integer) | ((Simple_names | Simple_name) (Comma (Simple_names | Simple_name))*)) |
	Residue_ptype ((Simple_names | Simple_name) (Comma (Simple_names | Simple_name))*) |
	Residue_mtype ((Simple_names | Simple_name) (Comma (Simple_names | Simple_name))*) |
	Residue_polarity (Hydrophilic | Hydrophobic | Non_polar | Polar | Charged | Positive | Negative) |
	Residue_secondary_structure (Helix_or_strand | Strand_or_loop | Helix_or_loop | Helix | Strand | Loop) |
	Residue_position number_f number_f |
	Residue_inscode Simple_name |
	Atom_ptype ((Simple_names | Simple_name) (Comma (Simple_names | Simple_name))*) |
	Atom_name ((Simple_names | Simple_name) (Comma (Simple_names | Simple_name))*) |
	(Atom | Atom_number) (IntRange | Integer (Comma Integer)*) |
	Atom_molnum (IntRange | Integer (Comma Integer)*) |
	Atom_entrynum (IntRange | Integer (Comma Integer)*) |
	Atom_mtype ((Simple_names | Simple_name) (Comma (Simple_names | Simple_name))*) |
	Atom_element ((Simple_names | Simple_name) (Comma (Simple_names | Simple_name))*) |
	Atom_attachements (IntRange | Integer | ((Equ_op | Lt_op | Gt_op | Leq_op | Geq_op) Integer)) |
	Atom_atomicnumber (IntRange | Integer | ((Equ_op | Lt_op | Gt_op | Leq_op | Geq_op) Integer)) |
	Atom_charge (FloatRange | Float | ((Equ_op | Lt_op | Gt_op | Leq_op | Geq_op) Float)) |
	Atom_formalcharge (IntRange | Integer | ((Equ_op | Lt_op | Gt_op | Leq_op | Geq_op) Integer)) |
	Atom_displayed |
	Atom_selected |
	Fillres_op factor |
	Fillmol_op factor |
	Within_op number_f factor |
	Beyond_op number_f factor |
	Withinbonds_op Integer factor |
	Beyondbonds_op Integer factor |
	Backbone |
	Sidechain |
	Water |
	Methyl |
	Amide |
	Smarts Simple_name |
	Slash_quote_string |
	Not_op factor |
	Simple_name;

/* number expression in assign */
number:	Float | Integer;

/* number expression in factor */
number_f:
	Float | Integer;

parameter_statement:
	Set Simple_name selection_expression;
