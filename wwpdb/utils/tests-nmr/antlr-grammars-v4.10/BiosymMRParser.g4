/*
 BIOSYM MR (Magnetic Restraint) parser grammar for ANTLR v4.
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

parser grammar BiosymMRParser;

options { tokenVocab=BiosymMRLexer; }

biosym_mr:
	(
	distance_restraints |
	distance_constraints |
	dihedral_angle_restraints |
	dihedral_angle_constraints |
	chirality_constraints |
	prochirality_constraints |
	mixing_time
	)*
	EOF;

/* BIOSYM - Distance restraints
 See also https://www.chem.uzh.ch/robinson/felixman/felix-restraints.html
*/
distance_restraints:
	distance_restraint+;

distance_restraint:
	Atom_selection Atom_selection
	number number number					// lower limit, upper limit, observation
	number number number					// weights for lower bound, upper bound, maximum penalty
	number?;

/* BIOSYM - Distance constraints
*/
distance_constraints:
	distance_constraint+;

distance_constraint:
	Atom_selection Atom_selection
	number number						// lower limit, upper limit
	number number number;					// weights for lower bound, upper bound, maximum penalty

/* BIOSYM - Dihedral angle restraints
 See also https://www.chem.uzh.ch/robinson/felixman/habas.html
*/
dihedral_angle_restraints:
	dihedral_angle_restraint+;

dihedral_angle_restraint:
	Atom_selection Atom_selection Atom_selection Atom_selection
	number number						// coupling constant, uncertainty of coupling constant
	number number number					// weights for lower bound, upper bound, maximum penalty
	number number						// range for lower bound, upper bound
	(number number)? (number number)? (number number)?;	// 2nd, 3rd, 4th ranges

/* BIOSYM - Dihedral angle constraints
*/
dihedral_angle_constraints:
	dihedral_angle_constraint+;

dihedral_angle_constraint:
	Atom_selection Atom_selection Atom_selection Atom_selection
	number number						// range for lower bound, upper bound
	number number number;					// weights for lower bound, upper bound, maximum penalty

/* BIOSYM - Chirality constraints
 See also https://www.chem.uzh.ch/robinson/felixman/felix-restraints.html
*/
chirality_constraints:
	chirality_constraint+;

chirality_constraint:
	Atom_selection
	Chiral_code;

/* BIOSYM - Prochirality constraints
*/
prochirality_constraints:
	prochirality_constraint+;

prochirality_constraint:
	Atom_selection
	Atom_selection
	Atom_selection
	Atom_selection
	Atom_selection;

mixing_time:
	Real;

/* number expression in restrains */
number:	Float | Integer;

