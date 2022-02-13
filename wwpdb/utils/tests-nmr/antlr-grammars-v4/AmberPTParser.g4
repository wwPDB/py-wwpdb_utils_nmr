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

parser grammar AmberPTParser;

options { tokenVocab=AmberPTLexer; }

amber_pt:
	(version_statement | FLAG) (
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
	tree_chain_classification_statement)*;

/* Amber file format: parameter/topology file specification (prmtop)
 See also https://ambermd.org/FileFormats.php and https://ambermd.org/Manuals.php
*/
version_statement:
	VERSION VERSION_STAMP Equ_op Version DATE Equ_op Date_time Date_time?
	(FLAG_V | EOF);

/* Amber file format: parameter/topology file specification (prmtop)
 See also https://ambermd.org/prmtop.pdf
*/
amber_atom_type_statement:
	AMBER_ATOM_TYPE
	format_function
	Simple_name* (FLAG_A | EOF);

angle_equil_value_statement:
	ANGLE_EQUIL_VALUE
	format_function
	Real* (FLAG_E | EOF);

angle_force_constant_statement:
	ANGLE_FORCE_CONSTANT
	format_function
	Real* (FLAG_E | EOF);

angles_inc_hydrogen_statement:
	ANGLES_INC_HYDROGEN
	format_function
	Integer* (FLAG_I | EOF);

angles_without_hydrogen_statement:
	ANGLES_WITHOUT_HYDROGEN
	format_function
	Integer* (FLAG_I | EOF);

atomic_number_statement:
	ATOMIC_NUMBER
	format_function
	Integer* (FLAG_I | EOF);

atom_name_statement:
	ATOM_NAME
	format_function
	Simple_name* (FLAG_A | EOF);

atom_type_index_statement:
	ATOM_TYPE_INDEX
	format_function
	Integer* (FLAG_I | EOF);

atoms_per_molecule_statement:
	ATOMS_PER_MOLECULE
	format_function
	Integer* (FLAG_I | EOF);

bond_equil_value_statement:
	BOND_EQUIL_VALUE
	format_function
	Real* (FLAG_E | EOF);

bond_force_constant_statement:
	BOND_FORCE_CONSTANT
	format_function
	Real* (FLAG_E | EOF);

bonds_inc_hydrogen_statement:
	BONDS_INC_HYDROGEN
	format_function
	Integer* (FLAG_I | EOF);

bonds_without_hydrogen_statement:
	BONDS_WITHOUT_HYDROGEN
	format_function
	Integer* (FLAG_I | EOF);

box_dimensions_statement:
	BOX_DIMENSIONS
	format_function
	Real* (FLAG_E | EOF);

cap_info_statement:
	CAP_INFO
	format_function
	Integer* (FLAG_I | EOF);

cap_info2_statement:
	CAP_INFO2
	format_function
	Real* (FLAG_E | EOF);

charge_statement:
	CHARGE
	format_function
	Real* (FLAG_E | EOF);

dihedral_force_constant_statement:
	DIHEDRAL_FORCE_CONSTANT
	format_function
	Real* (FLAG_E | EOF);

dihedral_periodicity_statement:
	DIHEDRAL_PERIODICITY
	format_function
	Real* (FLAG_E | EOF);

dihedral_phase_statement:
	DIHEDRAL_PHASE
	format_function
	Real* (FLAG_E | EOF);

dihedrals_inc_hydrogen_statement:
	DIHEDRALS_INC_HYDROGEN
	format_function
	Integer* (FLAG_I | EOF);

dihedrals_without_hydrogen_statement:
	DIHEDRALS_WITHOUT_HYDROGEN
	format_function
	Integer* (FLAG_I | EOF);

excluded_atoms_list_statement:
	EXCLUDED_ATOMS_LIST
	format_function
	Integer* (FLAG_I | EOF);

hbcut_statement:
	HBCUT
	format_function
	Real* (FLAG_E | EOF);

hbond_acoef_statement:
	HBOND_ACOEF
	format_function
	Real* (FLAG_E | EOF);

hbond_bcoef_statement:
	HBOND_BCOEF
	format_function
	Real* (FLAG_E | EOF);

ipol_statement:
	IPOL
	format_function
	Integer* (FLAG_I | EOF);

irotat_statement:
	IROTAT
	format_function
	Integer* (FLAG_I | EOF);

join_array_statement:
	JOIN_ARRAY
	format_function
	Integer* (FLAG_I | EOF);

lennard_jones_acoef_statement:
	LENNARD_JONES_ACOEF
	format_function
	Real* (FLAG_E | EOF);

lennard_jones_bcoef_statement:
	LENNARD_JONES_BCOEF
	format_function
	Real* (FLAG_E | EOF);

mass_statement:
	MASS
	format_function
	Real* (FLAG_E | EOF);

nonbonded_parm_index_statement:
	NONBONDED_PARM_INDEX
	format_function
	Integer* (FLAG_I | EOF);

number_excluded_atoms_statement:
	NUMBER_EXCLUDED_ATOMS
	format_function
	Integer* (FLAG_I | EOF);

pointers_statement:
	POINTERS
	format_function
	Integer* (FLAG_I | EOF);

polarizability_statement:
	POLARIZABILITY
	format_function
	Real* (FLAG_E | EOF);

radii_statement:
	RADII
	format_function
	Real* (FLAG_E | EOF);

radius_set_statement:
	RADIUS_SET
	format_function
	Simple_name* (FLAG_A | EOF);

residue_label_statement:
	RESIDUE_LABEL
	format_function
	Simple_name* (FLAG_A | EOF);

residue_pointer_statement:
	RESIDUE_POINTER
	format_function
	Integer+ (FLAG_I | EOF);

scee_scale_factor_statement:
	SCEE_SCALE_FACTOR
	format_function
	Real* (FLAG_E | EOF);

scnb_scale_factor_statement:
	SCNB_SCALE_FACTOR
	format_function
	Real* (FLAG_E | EOF);

screen_statement:
	SCREEN
	format_function
	Real* (FLAG_E | EOF);

solty_statement:
	SOLTY
	format_function
	Real* (FLAG_E | EOF);

solvent_pointers_statement:
	SOLVENT_POINTERS
	format_function
	Integer* (FLAG_I | EOF);

title_statement:
	TITLE
	format_function
	Simple_name* (FLAG_A | EOF);

tree_chain_classification_statement:
	TREE_CHAIN_CLASSIFICATION
	format_function
	Simple_name* (FLAG_A | EOF);

format_function:
	FORMAT (Fortran_format_A | Fortran_format_I | Fortran_format_E);

