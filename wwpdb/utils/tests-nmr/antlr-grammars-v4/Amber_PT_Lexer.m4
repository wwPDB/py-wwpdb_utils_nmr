/*
 Amber PT (Parameter Topology) lexer grammar for ANTLR v4.
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

lexer grammar Amber_PT_Lexer;

/* Amber file format: parameter/topology file specification (prmtop)
 See also https://ambermd.org/FileFormats.php and https://ambermd.org/Manuals.php
*/
VERSION:			'VERSION';

VERSION_STAMP:			'VERSION_STAMP';
DATE:				'DATE';

FLAG:				'FLAG';

AMBER_ATOM_TYPE:		'AMBER_ATOM_TYPE';
ANGLE_EQUIL_VALUE:		'ANGLE_EQUIL_VALUE';
ANGLE_FORCE_CONSTANT:		'ANGLE_FORCE_CONSTANT';
ANGLES_INC_HYDROGEN:		'ANGLES_INC_HYDROGEN';
ANGLES_WITHOUT_HYDROGEN:	'ANGLES_WITHOUT_HYDROGEN';
ATOMIC_NUMBER:			'ATOMIC_NUMBER';
ATOM_NAME:			'ATOM_NAME';
ATOM_TYPE_INDEX:		'ATOM_TYPE_INDEX';
BOND_EQUIL_VALUE:		'BOND_EQUIL_VALUE';
BOND_FORCE_CONSTANT:		'BOND_FORCE_CONSTANT';
BONDS_INC_HYDROGEN:		'BONDS_INC_HYDROGEN';
BONDS_WITHOUT_HYDROGEN:		'BONDS_WITHOUT_HYDROGEN';
CHARGE:				'CHARGE';
DIHEDRAL_FORCE_CONSTANT:	'DIHEDRAL_FORCE_CONSTANT';
DIHEDRAL_PERIODICITY:		'DIHEDRAL_PERIODICITY';
DIHEDRAL_PHASE:			'DIHEDRAL_PHASE';
DIHEDRALS_INC_HYDROGEN:		'DIHEDRALS_INC_HYDROGEN';
DIHEDRALS_WITHOUT_HYDROGEN:	'DIHEDRALS_WITHOUT_HYDROGE';
EXCLUDED_ATOMS_LIST:		'EXCLUDED_ATOMS_LIST';
HBCUT:				'HBCUT';
HBOND_ACOEF:			'HBOND_ACOEF';
HBOND_BCOEF:			'HBOND_BCOEF';
IPOL:				'IPOL';
IROTAT:				'IROTAT';
JOIN_ARRAY:			'JOIN_ARRAY';
LENNARD_JONES_ACOEF:		'LENNARD_JONES_ACOEF';
LENNARD_JONES_BCOEF:		'LENNARD_JONES_BCOEF';
MASS:				'MASS';
NONBONDED_PARM_INDEX:		'NONBONDED_PARM_INDEX';
NUMBER_EXCLUDED_ATOMS:		'NUMBER_EXCLUDED_ATOMS';
POINTERS:			'POINTERS';
RADII:				'RADII';
RADIUS_SET:			'RADIUS_SET';
RESIDUE_LABEL:			'RESIDUE_LABEL';
RESIDUE_POINTER:		'RESIDUE_POINTER';
SCEE_SCALE_FACTOR:		'SCEE_SCALE_FACTOR';
SCNB_SCALE_FACTOR:		'SCNB_SCALE_FACTOR';
SCREEN:				'SCREEN';
SOLTY:				'SOLTY';
TITLE:				'TITLE';
TREE_CHAIN_CLASSIFICATION:	'TREE_CHAIN_CLASSIFICATION';

FORMAT:			'FORMAT';

Percent:		'%';
Comma:			',';
Ampersand:		'&';

Integer:		('+' | '-')? DECIMAL;
Real:			(DECIMAL | DEC_DOT_DEC) ('E' ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	DECIMAL '.' DECIMAL | DECIMAL '.' | '.' DECIMAL;
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	[A-Za-z0-9];
fragment START_CHAR:	[A-Za-z0-9_];
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.';
fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment ATM_TYPE_CHAR:	ALPHA_NUM | '-' | '+';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

Class_name:		SIMPLE_NAME;
Segment_name:		SIMPLE_NAME;
Residue_number:		Integer;
Residue_name:		SIMPLE_NAME;
Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;
Atom_type:		ALPHA ATM_TYPE_CHAR*;

Quoted_atom_name:	('\'' | '"')? Atom_name Atom_name* ('\'' | '"')?;

L_paren:		'(';
R_paren:		')';
L_brace:		'{';
R_brace:		'}';
L_brakt:		'[';
R_brakt:		']';
Equ_op:			'=';
Lt_op:			'<';
Gt_op:			'>';
Leq_op:			'<=';
Geq_op:			'>=';

QUOT:			'"';
SPACE:			[ \t\r\n]+ -> skip;
COMMENT:		'{*' (COMMENT | .)*? '*}' -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!') ~[\r\n]* -> channel(HIDDEN);

