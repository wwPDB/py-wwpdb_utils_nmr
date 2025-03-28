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
Ambig_code:		(DECIMAL '-' DECIMAL ':' DECIMAL | (ALPHA | '_') SIMPLE_NAME '.' DECIMAL);
Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ('E' ('+' | '-')? DECIMAL)?;
Float_DecimalComma:	('+' | '-')? (DEC_COM_DEC) ('E' ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_COM_DEC:	(DECIMAL ',' DECIMAL?) | (',' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

Orientation_header:	'#' [ \t]* 'ORIENTATION' [ \t]+ 'MAGNITUDE' [ \t]+ 'RHOMBICITY' [ \t]+ 'ORI' [ \t]+ 'RESIDUE' [ \t]+ 'NUMBER' [ \t]* [\r\n]+;
Tensor_header:		'#' [ \t]* 'TENSOR' [ \t]+ 'MAGNITUDE' [ \t]+ 'RHOMBICITY' [ \t]+ 'RESIDUE' [ \t]* [\r\n]+;

SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

COMMENT:		('#' | '!')+ -> mode(COMMENT_MODE);

/* DIANA distance restraint generated by 'qconvert' script */
NoeUpp:			'NOEUPP';
NoeLow:			'NOELOW';

/* extensions for torsion angle restraints */
Type:			'TYPE';		// = Integer
Equ_op:			'=';
Or:			'OR';

/* CYANA 3.0 Reference Manual - ssbond macro
 See also http://www.cyana.org/wiki/index.php/CYANA_Macro:_ssbond
*/
Ssbond:			'SSBOND';
Ssbond_resids:		DECIMAL '-' DECIMAL;

/* CYANA 3.0 Reference Manual - hbond macro
 See also http://www.cyana.org/wiki/index.php/CYANA_Macro:_hbond
*/
Hbond:			'HBOND' -> pushMode(HBOND_MODE);

/* CYANA 3.0 Reference Manual - link statement
 See also http://www.cyana.org/wiki/index.php/Sequence_file
*/
Link:			'LINK';

/* CYANA 3.0 Reference Macnual - stereoassign macro
 See also http://www.cyana.org/wiki/index.php/CYANA_Macro:_stereoassign
*/
Atom_stereo:		'ATOM' ' '+ 'STEREO' -> mode(PRINT_MODE);

Var:			'VAR' -> mode(VARIABLE_MODE);
Unset:			'UNSET' -> mode(VARIABLE_MODE);

SetVar:			SIMPLE_NAME ':=' (SIMPLE_NAME | Float | Float_DecimalComma | Integer);

Print:			'PRINT' -> mode(PRINT_MODE);

/* AMBER atom nomenclature mapping generated by makeDIST_RST */
Residue:		'RESIDUE';
Mapping:		'MAPPING' -> pushMode(MAP_MODE);
Ambig:			'AMBIG' -> pushMode(MAP_MODE);

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"' | '*' | '#';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t\r\n]+ -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		(';' | '\\' | '&' | '<' | '>' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

mode COMMENT_MODE;

Any_name:		~[ \t\r\n]+;

SPACE_CM:		[ \t]+ -> skip;
RETURN_CM:		[\r\n]+ -> mode(DEFAULT_MODE);

mode HBOND_MODE;

Atom1:			'ATOM1';
Atom2:			'ATOM2';
Residue1:		'RESIDUE1';
Residue2:		'RESIDUE2';

Equ_op_HB:		'=';

Integer_HB:		('+' | '-')? DECIMAL;
Simple_name_HB:		SIMPLE_NAME;

SPACE_HB:		[ \t]+ -> skip;
RETURN_HB:		[\r\n]+ -> mode(DEFAULT_MODE);

//SECTION_COMMENT_HB:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_HB:	('#' | '!' | ';' | '\\' | '&' | '<' | '>' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

mode PRINT_MODE;

Double_quote_string:	'"' ~["\r\n]* '"';

SPACE_PR:		[ \t]+ -> skip;
RETURN_PR:		[\r\n]+ -> mode(DEFAULT_MODE);

//SECTION_COMMENT_PR:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_PR:	('#' | '!' | ';' | '\\' | '&' | '<' | '>' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

mode VARIABLE_MODE;

Simple_name_VA:		SIMPLE_NAME;

SPACE_VA:		[ \t]+ -> skip;
RETURN_VA:		[\r\n]+ -> mode(DEFAULT_MODE);

//SECTION_COMMENT_VA:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_VA:	('#' | '!' | ';' | '\\' | '&' | '<' | '>' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

mode MAP_MODE;

Ambig_code_MP:		(DECIMAL '-' DECIMAL ':' DECIMAL | (ALPHA | '_') SIMPLE_NAME '.' DECIMAL);
Integer_MP:		('+' | '-')? DECIMAL;
Simple_name_MP:		SIMPLE_NAME;

Equ_op_MP:		'=';

SPACE_MP:		[ \t]+ -> skip;
RETURN_MP:		[\r\n]+ -> mode(DEFAULT_MODE);

//SECTION_COMMENT_MP:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_MP:	('#' | '!' | ';' | '\\' | '&' | '<' | '>' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

