/*
 CYANA MR (Magnetic Restraint) lexer grammar for ANTLR v4.10 or later
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

lexer grammar CyanaMRLexer;

options { caseInsensitive=true; }

/* CYANA 3.0 Reference Manual
 See also http://www.cyana.org/wiki/index.php/CYANA_3.0_Reference_Manual
*/
Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ('E' ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

ORI_HEADER:		'#' [ \t]* 'ORIENTATION' [ \t]+ 'MAGNITUDE' [ \t]+ 'RHOMBICITY' [ \t]+ 'ORI' [ \t]+ 'RESIDUE' [ \t]+ 'NUMBER' [ \t]* [\r\n]+;
TEN_HEADER:		'#' [ \t]* 'TENSOR' [ \t]+ 'MAGNITUDE' [ \t]+ 'RHOMBICITY' [ \t]+ 'RESIDUE' [ \t]* [\r\n]+;

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

/* extensions for torsion angle restraints */
Type:			'TYPE';		// = Integer
Equ_op:			'=';
Or:			'OR';

/* ssbond macro */
Ssbond:			'SSBOND';
Ssbond_resids:		DECIMAL '-' DECIMAL;

/* hbond macro */
Hbond:			'HBOND' -> pushMode(HBOND_MODE);

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;
//Atom_type:		ALPHA ATM_TYPE_CHAR*;

fragment ALPHA:		[A-Z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"' | '*' | '#';
fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment ATM_TYPE_CHAR:	ALPHA_NUM | '-' | '+';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t\r\n]+ -> skip;
COMMENT:		'{' (COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

mode HBOND_MODE;

Atom1:			'ATOM1';
Atom2:			'ATOM2';
Residue1:		'RESIDUE1';
Residue2:		'RESIDUE2';

Equ_op_HB:		'=';

Integer_HB:		('+' | '-')? DECIMAL;
Simple_name_HB:		SIMPLE_NAME;

SPACE_HB:		[ \t]+ -> skip;
RETURN_HB:		[\r\n]+ -> popMode;

SECTION_COMMENT_HB:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_HB:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

