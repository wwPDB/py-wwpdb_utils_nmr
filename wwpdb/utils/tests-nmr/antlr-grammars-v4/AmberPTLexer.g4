/*
 AMBER PT (Parameter Topology) lexer grammar for ANTLR v4.
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

lexer grammar AmberPTLexer;

/* Case-Insensitive Lexing
 See also https://github.com/antlr/antlr4/blob/master/doc/case-insensitive-lexing.md
*/
fragment A:		[aA]; // match either an 'a' or 'A'
fragment B:		[bB];
fragment C:		[cC];
fragment D:		[dD];
fragment E:		[eE];
fragment F:		[fF];
fragment G:		[gG];
fragment H:		[hH];
fragment I:		[iI];
fragment J:		[jJ];
fragment K:		[kK];
fragment L:		[lL];
fragment M:		[mM];
fragment N:		[nN];
fragment O:		[oO];
fragment P:		[pP];
fragment Q:		[qQ];
fragment R:		[rR];
fragment S:		[sS];
fragment T:		[tT];
fragment U:		[uU];
fragment V:		[vV];
fragment W:		[wW];
fragment X:		[xX];
fragment Y:		[yY];
fragment Z:		[zZ];

/* Amber file format: parameter/topology file specification (prmtop)
 See also https://ambermd.org/FileFormats.php and https://ambermd.org/Manuals.php
*/
VERSION:		'%VERSION'
			-> pushMode(VERSION_MODE);

/* Amber file format: parameter/topology file specification (prmtop)
 See also https://ambermd.org/prmtop.pdf
*/
FLAG:			'%FLAG';

AMBER_ATOM_TYPE:	'AMBER_ATOM_TYPE';
ANGLE_EQUIL_VALUE:	'ANGLE_EQUIL_VALUE';
ANGLE_FORCE_CONSTANT:	'ANGLE_FORCE_CONSTANT';
ANGLES_INC_HYDROGEN:	'ANGLES_INC_HYDROGEN';
ANGLES_WITHOUT_HYDROGEN:'ANGLES_WITHOUT_HYDROGEN';
ATOMIC_NUMBER:		'ATOMIC_NUMBER';
ATOM_NAME:		'ATOM_NAME';
ATOM_TYPE_INDEX:	'ATOM_TYPE_INDEX';
ATOMS_PER_MOLECULE:	'ATOMS_PER_MOLECULE';
BOND_EQUIL_VALUE:	'BOND_EQUIL_VALUE';
BOND_FORCE_CONSTANT:	'BOND_FORCE_CONSTANT';
BONDS_INC_HYDROGEN:	'BONDS_INC_HYDROGEN';
BONDS_WITHOUT_HYDROGEN:	'BONDS_WITHOUT_HYDROGEN';
BOX_DIMENSIONS:		'BOX_DIMENSIONS';
CAP_INFO:		'CAP_INFO';
CAP_INFO2:		'CAP_INFO2';
CHARGE:			'CHARGE';
DIHEDRAL_FORCE_CONSTANT:'DIHEDRAL_FORCE_CONSTANT';
DIHEDRAL_PERIODICITY:	'DIHEDRAL_PERIODICITY';
DIHEDRAL_PHASE:		'DIHEDRAL_PHASE';
DIHEDRALS_INC_HYDROGEN:	'DIHEDRALS_INC_HYDROGEN';
DIHEDRALS_WITHOUT_HYDROGEN:
			'DIHEDRALS_WITHOUT_HYDROGEN';
EXCLUDED_ATOMS_LIST:	'EXCLUDED_ATOMS_LIST';
HBCUT:			'HBCUT';
HBOND_ACOEF:		'HBOND_ACOEF';
HBOND_BCOEF:		'HBOND_BCOEF';
IPOL:			'IPOL';
IROTAT:			'IROTAT';
JOIN_ARRAY:		'JOIN_ARRAY';
LENNARD_JONES_ACOEF:	'LENNARD_JONES_ACOEF';
LENNARD_JONES_BCOEF:	'LENNARD_JONES_BCOEF';
MASS:			'MASS';
NONBONDED_PARM_INDEX:	'NONBONDED_PARM_INDEX';
NUMBER_EXCLUDED_ATOMS:	'NUMBER_EXCLUDED_ATOMS';
POINTERS:		'POINTERS';
POLARIZABILITY:		'POLARIZABILITY';
RADII:			'RADII';
RADIUS_SET:		'RADIUS_SET';
RESIDUE_LABEL:		'RESIDUE_LABEL';
RESIDUE_POINTER:	'RESIDUE_POINTER';
SCEE_SCALE_FACTOR:	'SCEE_SCALE_FACTOR';
SCNB_SCALE_FACTOR:	'SCNB_SCALE_FACTOR';
SCREEN:			'SCREEN';
SOLTY:			'SOLTY';
SOLVENT_POINTERS:	'SOLVENT_POINTERS';
TITLE:			'TITLE';
TREE_CHAIN_CLASSIFICATION:
			'TREE_CHAIN_CLASSIFICATION';

fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' |
			'(' | '{' | '[' | '<' |
			'=' | '~' |
			'"' | '\'' | '`' |
			'+' | '-' | '*' | '/' |
			'.' | '?' | ':' |
			'&' | '$' | '@';
fragment ANY_CHAR:	~[ \t\r\n];
fragment SIMPLE_NAME:	START_CHAR ANY_CHAR*;

FORMAT:			'%FORMAT'
			-> pushMode(FORMAT_MODE);

SPACE:			[ \t\r\n]+ -> skip;
//COMMENT:		'{*' (COMMENT | .)*? '*}' -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | '*' | ';' | '/') ~[\r\n]* -> channel(HIDDEN);

mode VERSION_MODE;

fragment DEC_DIGIT2:	DEC_DIGIT DEC_DIGIT;
fragment YEAR:		DEC_DIGIT2 DEC_DIGIT2?;
fragment DATE_TIME_SEP:	'/' | ':' | '-' | '.';

fragment JAN:		J A N;
fragment FEB:		F E B;
fragment MAR:		M A R;
fragment APR:		A P R;
fragment MAY:		M A Y;
fragment JUN:		J U N;
fragment JUL:		J U L;
fragment AUG:		A U G;
fragment SEP:		S E P;
fragment OCT:		O C T;
fragment NOV:		N O V;
fragment DEC:		D E C;

fragment MONTH:		JAN | FEB | MAR | APR | MAY | JUN | JUL | AUG | SEP | OCT | NOV | DEC | DEC_DIGIT2;

VERSION_STAMP:		'VERSION_STAMP';
DATE:			'DATE';
Equ_op:			'=';
Version:		V? DECIMAL ('.' DECIMAL);
Date_time:		MONTH (DATE_TIME_SEP DEC_DIGIT2)? (DATE_TIME_SEP YEAR)?;

SPACE_V:		[ \t\r\n]+ -> skip;
FLAG_V:			'%FLAG' -> popMode;

mode FORMAT_MODE;

Fortran_format_A:	'(' DECIMAL A DECIMAL ')'
			-> pushMode(STR_ARRAY_MODE);
Fortran_format_I:	'(' DECIMAL I DECIMAL ')'
			-> pushMode(INT_ARRAY_MODE);
Fortran_format_E:	'(' DECIMAL E DECIMAL ('.' DECIMAL)? ')'
			-> pushMode(REAL_ARRAY_MODE);

mode STR_ARRAY_MODE;

Simple_name:		SIMPLE_NAME;

SPACE_A:		[ \t\r\n]+ -> skip;
FLAG_A:			'%FLAG' -> mode(DEFAULT_MODE);

mode INT_ARRAY_MODE;

Integer:		('+' | '-')? DECIMAL;

SPACE_I:		[ \t\r\n]+ -> skip;
FLAG_I:			'%FLAG' -> mode(DEFAULT_MODE);

mode REAL_ARRAY_MODE;

Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) (E ('+' | '-')? DECIMAL)?;

SPACE_E:		[ \t\r\n]+ -> skip;
FLAG_E:			'%FLAG' -> mode(DEFAULT_MODE);

