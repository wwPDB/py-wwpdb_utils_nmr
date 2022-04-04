/*
 ROSETTA MR (Magnetic Restraint) parser grammar for ANTLR v4.
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

parser grammar RosettaMRParser;

options { tokenVocab=RosettaMRLexer; }

rosetta_mr:
	(
	atom_pair_restraints |
	angle_restraints |
	dihedral_restraints |
	dihedral_pair_restraints |
	coordinate_restraints |
	local_coordinate_restraints |
	site_restraints |
	site_residues_restraints |
	min_residue_atomic_distance_restraints |
	big_bin_restraints |
	nested_restraints |
	rdc_restraints |			// used only in CS-ROSETTA
	disulfide_bond_linkages			// used only in CS-ROSETTA
	)*
	EOF;

/* Rosetta Constraint File - Constraint Types - Single constraints
 See also https://www.rosettacommons.org/docs/latest/rosetta_basics/file_types/constraint-file
*/
atom_pair_restraints:
	atom_pair_restraint+;

atom_pair_restraint:
	(AtomPair | NamedAtomPair | AmbiguousNMRDistance) Simple_name Integer Simple_name Integer func_type_def;

angle_restraints:
	angle_restraint+;

angle_restraint:
	(Angle | NamedAngle) Simple_name Integer Simple_name Integer Simple_name Integer func_type_def;

dihedral_restraints:
	dihedral_restraint+;

dihedral_restraint:
	Dihedral Simple_name Integer Simple_name Integer Simple_name Integer Simple_name Integer func_type_def;

dihedral_pair_restraints:
	dihedral_pair_restraint+;

dihedral_pair_restraint:
	DihedralPair Simple_name Integer Simple_name Integer Simple_name Integer Simple_name Integer
	Simple_name Integer Simple_name Integer Simple_name Integer Simple_name Integer func_type_def;

coordinate_restraints:
	coordinate_restraint+;

coordinate_restraint:
	CoordinateConstraint Simple_name Simple_name Simple_name Simple_name	// The 2nd and 4th Simple_names represent Residue_num[Chain_ID]
	number number number func_type_def;

local_coordinate_restraints:
	local_coordinate_restraint+;

local_coordinate_restraint:
	LocalCoordinateConstraint Simple_name Integer Simple_name Simple_name Simple_name Integer
	number number number func_type_def;

site_restraints:
	site_restraint+;

site_restraint:
	SiteConstraint Simple_name Integer Simple_name func_type_def;	// the last Simple_name represent Opposing_chain

site_residues_restraints:
	site_residues_restraint+;

site_residues_restraint:
	SiteConstraintResidues Integer Simple_name Integer Integer func_type_def;

min_residue_atomic_distance_restraints:
	min_residue_atomic_distance_restraint+;

min_residue_atomic_distance_restraint:
	MinResidueAtomicDistance Integer Integer number;

big_bin_restraints:
	big_bin_restraint+;

big_bin_restraint:
	BigBin Integer Simple_name number; // Simple_name must be a single uppercase letter selected from 'O', 'G', 'E', 'A', and 'B'

/* Rosetta Constraint File - Constraint Types - Nested constraints
 See also https://www.rosettacommons.org/docs/latest/rosetta_basics/file_types/constraint-file
*/
nested_restraints:
	nested_restraint+;

nested_restraint:
	(MultiConstraint | AmbiguousConstraint | (KofNConstraint Integer)) any_restraint+ END;

any_restraint:
	atom_pair_restraint |
	angle_restraint |
	dihedral_restraint |
	dihedral_pair_restraint |
	coordinate_restraint |
	local_coordinate_restraint |
	site_restraint |
	site_residues_restraint |
	min_residue_atomic_distance_restraint |
	big_bin_restraint;

/* Rosetta Constraint File - Function Types
 See also https://www.rosettacommons.org/docs/latest/rosetta_basics/file_types/constraint-file
*/
func_type_def:
	(CIRCULARHARMONIC | HARMONIC | SIGMOID | SQUARE_WELL) number_f number_f |
	BOUNDED number_f number_f number_f number_f? Simple_name? |
	PERIODICBOUNDED number_f number_f number_f number_f number_f? Simple_name? |
	OFFSETPERIODICBOUNDED number_f number_f number_f number_f number_f number_f? Simple_name? |
	(AMBERPERIODIC | CHARMMPERIODIC | FLAT_HARMONIC | TOPOUT) number_f number_f number_f |
	(CIRCULARSIGMOIDAL | LINEAR_PENALTY) number_f number_f number_f number_f |
	CIRCULARSPLINE number_f+ |
	GAUSSIANFUNC number_f number_f Simple_name (WEIGHT number_f)? |
	SOGFUNC Integer (number_f number_f number_f)+ |
	(MIXTUREFUNC | KARPLUS | SOEDINGFUNC) number_f number_f number_f number_f number_f number_f |
	CONSTANTFUNC number_f |
	IDENTITY |
	SCALARWEIGHTEDFUNC number_f func_type_def |
	SUMFUNC Integer func_type_def+ |
	SPLINE Simple_name (number_f number_f number_f | NONE number_f number_f number_f (Simple_name number_f*)+) | // histogram_file_path can not be evaluated
	FADE number_f number_f number_f number_f number_f? |
	SQUARE_WELL2 number_f number_f number_f DEGREES? |
	ETABLE number_f number_f number_f* |
	USOG Integer (number_f number_f number_f number_f)+ |
	SOG Integer (number_f number_f number_f number_f number_f number_f)+;

/* CS-ROSETTA Installation Files
 See also https://spin.niddk.nih.gov/bax/software/CSROSETTA/#rdc and https://csrosetta.bmrb.io/format_help
*/
rdc_restraints:
	rdc_restraint+;

rdc_restraint:
	Integer Simple_name Integer Simple_name number;

/* CS-ROSETTA Installation Files
 See also https://spin.niddk.nih.gov/bax/software/CSROSETTA/#faq and https://csrosetta.bmrb.io/format_help
*/
disulfide_bond_linkages:
	disulfide_bond_linkage+;

disulfide_bond_linkage:
	Integer Integer;

/* number expression in restrains */
number:	Float | Integer;

/* number expression in functions */
number_f:
	Float | Integer;

