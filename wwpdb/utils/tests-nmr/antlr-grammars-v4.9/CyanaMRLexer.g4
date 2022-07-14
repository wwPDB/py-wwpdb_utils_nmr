/*
 CYANA MR (Magnetic Restraint) lexer grammar for ANTLR v4.
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

/* CYANA 3.0 Reference Manual
 See also http://www.cyana.org/wiki/index.php/CYANA_3.0_Reference_Manual
*/
Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) (E ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

ORI_HEADER:		'#' [ \t]* O R I E N T A T I O N [ \t]+ M A G N I T U D E [ \t]+ R H O M B I C I T Y [ \t]+ O R I [ \t]+ R E S I D U E [ \t]+ N U M B E R [ \t]* [\r\n]+;
TEN_HEADER:		'#' [ \t]* T E N S O R [ \t]+ M A G N I T U D E [ \t]+ R H O M B I C I T Y [ \t]+ R E S I D U E [ \t]* [\r\n]+;

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

/* extensions for torsion angle restraints */
Type:			T Y P E;		// = Integer
Equ_op:			'=';
Or:			O R;

/* CYANA 3.0 Reference Manual - ssbond macro
 See also http://www.cyana.org/wiki/index.php/CYANA_Macro:_ssbond
*/
Ssbond:			S S B O N D;
Ssbond_resids:		DECIMAL '-' DECIMAL;

/* CYANA 3.0 Reference Manual - hbond macro
 See also http://www.cyana.org/wiki/index.php/CYANA_Macro:_hbond
*/
Hbond:			H B O N D -> pushMode(HBOND_MODE);

/* CYANA 3.0 Reference Manual - link statement
 See also http://www.cyana.org/wiki/index.php/Sequence_file
*/
Link:			L I N K;

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;
//Atom_type:		ALPHA ATM_TYPE_CHAR*;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"' | '*' | '#';
fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment ATM_TYPE_CHAR:	ALPHA_NUM | '-' | '+';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t\r\n]+ -> skip;
COMMENT:		'{' (COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | R E M A R K) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | R E M A R K) ~[\r\n]* -> channel(HIDDEN);

mode HBOND_MODE;

Atom1:			A T O M '1';
Atom2:			A T O M '2';
Residue1:		R E S I D U E '1';
Residue2:		R E S I D U E '2';

Equ_op_HB:		'=';

Integer_HB:		('+' | '-')? DECIMAL;
Simple_name_HB:		SIMPLE_NAME;

SPACE_HB:		[ \t]+ -> skip;
RETURN_HB:		[\r\n]+ -> popMode;

SECTION_COMMENT_HB:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | R E M A R K) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_HB:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | R E M A R K) ~[\r\n]* -> channel(HIDDEN);

