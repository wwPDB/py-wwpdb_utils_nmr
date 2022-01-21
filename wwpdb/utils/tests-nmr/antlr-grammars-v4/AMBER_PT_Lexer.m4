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

lexer grammar AMBER_PT_Lexer;

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
VERSION:		'%VERSION';

VERSION_STAMP:		'VERSION_STAMP';
DATE:			'DATE';

FLAG:			'%FLAG';

AMBER_ATOM_TYPE:	'AMBER_ATOM_TYPE' RETURN;
ANGLE_EQUIL_VALUE:	'ANGLE_EQUIL_VALUE' RETURN;
ANGLE_FORCE_CONSTANT:	'ANGLE_FORCE_CONSTANT' RETURN;
ANGLES_INC_HYDROGEN:	'ANGLES_INC_HYDROGEN' RETURN;
ANGLES_WITHOUT_HYDROGEN:'ANGLES_WITHOUT_HYDROGEN' RETURN;
ATOMIC_NUMBER:		'ATOMIC_NUMBER' RETURN;
ATOM_NAME:		'ATOM_NAME' RETURN;
ATOM_TYPE_INDEX:	'ATOM_TYPE_INDEX' RETURN;
BOND_EQUIL_VALUE:	'BOND_EQUIL_VALUE' RETURN;
BOND_FORCE_CONSTANT:	'BOND_FORCE_CONSTANT' RETURN;
BONDS_INC_HYDROGEN:	'BONDS_INC_HYDROGEN' RETURN;
BONDS_WITHOUT_HYDROGEN:	'BONDS_WITHOUT_HYDROGEN' RETURN;
CHARGE:			'CHARGE' RETURN;
DIHEDRAL_FORCE_CONSTANT:'DIHEDRAL_FORCE_CONSTANT' RETURN;
DIHEDRAL_PERIODICITY:	'DIHEDRAL_PERIODICITY' RETURN;
DIHEDRAL_PHASE:		'DIHEDRAL_PHASE' RETURN;
DIHEDRALS_INC_HYDROGEN:	'DIHEDRALS_INC_HYDROGEN' RETURN;
DIHEDRALS_WITHOUT_HYDROGEN:
			'DIHEDRALS_WITHOUT_HYDROGE' RETURN;
EXCLUDED_ATOMS_LIST:	'EXCLUDED_ATOMS_LIST' RETURN;
HBCUT:			'HBCUT' RETURN;
HBOND_ACOEF:		'HBOND_ACOEF' RETURN;
HBOND_BCOEF:		'HBOND_BCOEF' RETURN;
IPOL:			'IPOL' RETURN;
IROTAT:			'IROTAT' RETURN;
JOIN_ARRAY:		'JOIN_ARRAY' RETURN;
LENNARD_JONES_ACOEF:	'LENNARD_JONES_ACOEF' RETURN;
LENNARD_JONES_BCOEF:	'LENNARD_JONES_BCOEF' RETURN;
MASS:			'MASS' RETURN;
NONBONDED_PARM_INDEX:	'NONBONDED_PARM_INDEX' RETURN;
NUMBER_EXCLUDED_ATOMS:	'NUMBER_EXCLUDED_ATOMS' RETURN;
POINTERS:		'POINTERS' RETURN;
RADII:			'RADII' RETURN;
RADIUS_SET:		'RADIUS_SET' RETURN;
RESIDUE_LABEL:		'RESIDUE_LABEL' RETURN;
RESIDUE_POINTER:	'RESIDUE_POINTER' RETURN;
SCEE_SCALE_FACTOR:	'SCEE_SCALE_FACTOR' RETURN;
SCNB_SCALE_FACTOR:	'SCNB_SCALE_FACTOR' RETURN;
SCREEN:			'SCREEN' RETURN;
SOLTY:			'SOLTY' RETURN;
TITLE:			'TITLE' RETURN;
TREE_CHAIN_CLASSIFICATION:
			'TREE_CHAIN_CLASSIFICATION' RETURN;

FORMAT:			'%FORMAT';

Integer:		('+' | '-')? DECIMAL;
Float:			(DECIMAL | DEC_DOT_DEC);
Real:			(DECIMAL | DEC_DOT_DEC) ((E | D) ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	DECIMAL '.' DECIMAL | DECIMAL '.' | '.' DECIMAL;
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	[A-Za-z0-9];
fragment START_CHAR:	[A-Za-z0-9_];
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.';
fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment ATM_TYPE_CHAR:	ALPHA_NUM | '-' | '+' | '*';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

fragment NAME_FCHR:	NAME_CHAR | ' ';
fragment ATM_NAME_FCHR:	ATM_NAME_CHAR | ' ';
fragment ATM_TYPE_FCHR:	ATM_TYPE_CHAR | ' ';

fragment DEC_DIGIT2:	DEC_DIGIT DEC_DIGIT;
fragment YEAR:		DEC_DIGIT2 DEC_DIGIT2?;
fragment DATE_TIME_SEP:	':' | '/';

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

Residue_number:		Integer;
Residue_name4:		START_CHAR NAME_FCHR NAME_FCHR NAME_FCHR;
Atom_name4:		ALPHA_NUM ATM_NAME_FCHR ATM_NAME_FCHR ATM_NAME_FCHR;
Atom_type4:		ALPHA ATM_TYPE_FCHR ATM_TYPE_FCHR ATM_TYPE_FCHR;
Generic_name4:		START_CHAR NAME_FCHR NAME_FCHR NAME_FCHR;

Version:		V? DECIMAL ('.' DECIMAL)?;
Date:			MONTH DATE_TIME_SEP DEC_DIGIT2 DATE_TIME_SEP YEAR;
Time:			DEC_DIGIT2 (DATE_TIME_SEP DEC_DIGIT2)? (DATE_TIME_SEP DEC_DIGIT2)?;
Line_string:		~[\r\n];

Fortran_format_A:	DECIMAL A DECIMAL;
Fortran_format_A4:	DECIMAL A '4';
Fortran_format_I:	DECIMAL I DECIMAL;
Fortran_format_E:	DECIMAL E DECIMAL ('.' DECIMAL)?;
Fortran_format_F:	DECIMAL F DECIMAL ('.' DECIMAL)?;

L_paren:		'(';
R_paren:		')';
Equ_op:			'=';

RETURN:			[\r\n]+;
SPACE:			[ \t]+ -> skip;
COMMENT:		'{*' (COMMENT | .)*? '*}' -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!') ~[\r\n]* -> channel(HIDDEN);

