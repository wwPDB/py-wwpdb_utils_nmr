/*
 AMBER PT (Parameter Topology) parser grammar for ANTLR v4.
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

parser grammar AMBER_PT_Parser;

options { tokenVocab=AMBER_PT_Lexer; }

amber_pt:
	version_statement |
	amber_atom_type_statement |
	angle_equil_value_statement |
	angle_force_constant_statement |
	angles_inc_hydrogen_statement |
	angles_without_hydrogen_statement |
	atomic_number_statement |
	atom_name_statement |
	atom_type_index_statement |
	atoms_per_molecule_statement |
	bond_equil_value_statement |
	bond_force_constant_statement |
	bonds_inc_hydrogen_statement |
	bonds_without_hydrogen_statement |
	box_dimensions_statement |
	cap_info_statement |
	cap_info2_statement |
	charge_statement |
	dihedral_force_constant_statement |
	dihedral_periodicity_statement |
	dihedral_phase_statement |
	dihedrals_inc_hydrogen_statement |
	dihedrals_without_hydrogen_statement |
	excluded_atoms_list_statement |
	hbcut_statement |
	hbond_acoef_statement |
	hbond_bcoef_statement |
	ipol_statement |
	irotat_statement |
	join_array_statement |
	lennard_jones_acoef_statement |
	lennard_jones_bcoef_statement |
	mass_statement |
	nonbonded_parm_index_statement |
	number_excluded_atoms_statement |
	pointers_statement |
	polarizability_statement |
	radii_statement |
	radius_set_statement |
	residue_label_statement |
	residue_pointer_statement |
	scee_scale_factor_statement |
	scnb_scale_factor_statement |
	screen_statement |
	solty_statement |
	solvent_pointers_statement |
	title_statement |
	tree_chain_classification_statement |
	EOF;

/* Amber file format: parameter/topology file specification (prmtop)
 See also https://ambermd.org/FileFormats.php and https://ambermd.org/Manuals.php
*/
version_statement:
	VERSION	VERSION_STAMP Equ_op Version DATE Equ_op Date Time? RETURN;

/* Amber file format: parameter/topology file specification (prmtop)
 See also https://ambermd.org/prmtop.pdf
*/
amber_atom_type_statement:
	FLAG AMBER_ATOM_TYPE
	string4_format_statement
	atom_type_array*;

angle_equil_value_statement:
	FLAG ANGLE_EQUIL_VALUE
	real_format_statement
	real_array*;

angle_force_constant_statement:
	FLAG ANGLE_FORCE_CONSTANT
	real_format_statement
	real_array*;

angles_inc_hydrogen_statement:
	FLAG ANGLES_INC_HYDROGEN
	integer_format_statement
	integer_array*;

angles_without_hydrogen_statement:
	FLAG ANGLES_WITHOUT_HYDROGEN
	integer_format_statement
	integer_array*;

atomic_number_statement:
	FLAG ATOMIC_NUMBER
	integer_format_statement
	integer_array*;

atom_name_statement:
	FLAG ATOM_NAME
	string4_format_statement
	atom_name_array*;

atom_type_index_statement:
	FLAG ATOM_TYPE_INDEX
	integer_format_statement
	integer_array*;

atoms_per_molecule_statement:
	FLAG ATOMS_PER_MOLECULE
	integer_format_statement
	integer_array*;

bond_equil_value_statement:
	FLAG BOND_EQUIL_VALUE
	real_format_statement
	real_array*;

bond_force_constant_statement:
	FLAG BOND_FORCE_CONSTANT
	real_format_statement
	real_array*;

bonds_inc_hydrogen_statement:
	FLAG BONDS_INC_HYDROGEN
	integer_format_statement
	integer_array*;

bonds_without_hydrogen_statement:
	FLAG BONDS_WITHOUT_HYDROGEN
	integer_format_statement
	integer_array*;

box_dimensions_statement:
	FLAG BOX_DIMENSIONS
	real_format_statement
	real_array*;

cap_info_statement:
	FLAG CAP_INFO
	integer_format_statement
	integer_array*;

cap_info2_statement:
	FLAG CAP_INFO2
	real_format_statement
	real_array*;

charge_statement:
	FLAG CHARGE
	real_format_statement
	real_array*;

dihedral_force_constant_statement:
	FLAG DIHEDRAL_FORCE_CONSTANT
	real_format_statement
	real_array*;

dihedral_periodicity_statement:
	FLAG DIHEDRAL_PERIODICITY
	real_format_statement
	real_array*;

dihedral_phase_statement:
	FLAG DIHEDRAL_PHASE
	real_format_statement
	real_array*;

dihedrals_inc_hydrogen_statement:
	FLAG DIHEDRALS_INC_HYDROGEN
	integer_format_statement
	integer_array*;

dihedrals_without_hydrogen_statement:
	FLAG DIHEDRALS_WITHOUT_HYDROGEN
	integer_format_statement
	integer_array*;

excluded_atoms_list_statement:
	FLAG EXCLUDED_ATOMS_LIST
	integer_format_statement
	integer_array*;

hbcut_statement:
	FLAG HBCUT
	real_format_statement
	real_array*;

hbond_acoef_statement:
	FLAG HBOND_ACOEF
	real_format_statement
	real_array*;

hbond_bcoef_statement:
	FLAG HBOND_BCOEF
	real_format_statement
	real_array*;

ipol_statement:
	FLAG IPOL
	integer_format_statement
	integer_array*;

irotat_statement:
	FLAG IROTAT
	integer_format_statement
	integer_array*;

join_array_statement:
	FLAG JOIN_ARRAY
	integer_format_statement
	integer_array*;

lennard_jones_acoef_statement:
	FLAG LENNARD_JONES_ACOEF
	real_format_statement
	real_array*;

lennard_jones_bcoef_statement:
	FLAG LENNARD_JONES_BCOEF
	real_format_statement
	real_array*;
	
mass_statement:
	FLAG MASS
	real_format_statement
	real_array*;

nonbonded_parm_index_statement:
	NONBONDED_PARM_INDEX
	integer_format_statement
	integer_array*;

number_excluded_atoms_statement:
	FLAG NUMBER_EXCLUDED_ATOMS
	integer_format_statement
	integer_array*;

pointers_statement:
	FLAG POINTERS
	integer_format_statement
	integer_array*;

polarizability_statement:
	FLAG POLARIZABILITY
	real_format_statement
	real_array*;

radii_statement:
	FLAG RADII
	real_format_statement
	real_array*;

radius_set_statement:
	FLAG RADIUS_SET
	integer_format_statement
	integer_array*;

residue_label_statement:
	FLAG RESIDUE_LABEL
	string4_format_statement
	residue_name_array*;

residue_pointer_statement:
	FLAG RESIDUE_POINTER
	integer_format_statement
	integer_array*;

scee_scale_factor_statement:
	FLAG SCEE_SCALE_FACTOR
	real_format_statement
	real_array*;

scnb_scale_factor_statement:
	FLAG SCNB_SCALE_FACTOR
	real_format_statement
	real_array*;

screen_statement:
	FLAG SCREEN
	real_format_statement
	real_array*;

solty_statement:
	FLAG SOLTY
	real_format_statement
	real_array*;

solvent_pointers_statement:
	FLAG SOLVENT_POINTERS
	integer_format_statement
	integer_array*;

title_statement:
	FLAG TITLE
	string_format_statement
	line_string_array*;

tree_chain_classification_statement:
	FLAG TREE_CHAIN_CLASSIFICATION
	string4_format_statement
	generic_name_array*;

string_format_statement:
	FORMAT L_paren Fortran_format_A R_paren RETURN;

string4_format_statement:
	FORMAT L_paren Fortran_format_A4 R_paren RETURN;

integer_format_statement:
	FORMAT L_paren Fortran_format_I R_paren RETURN;

real_format_statement:
	FORMAT L_paren Fortran_format_E R_paren RETURN;

float_format_statement:
	FORMAT L_paren Fortran_format_F R_paren RETURN;

atom_type_array:
	Atom_type4* RETURN;

atom_name_array:
	Atom_name4* RETURN;

residue_name_array:
	Residue_name4* RETURN;

generic_name_array:
	Generic_name4* RETURN;

line_string_array:
	Line_string RETURN;

integer_array:
	Integer* RETURN;

float_array:
	Float* RETURN;

real_array:
	Real* RETURN;

