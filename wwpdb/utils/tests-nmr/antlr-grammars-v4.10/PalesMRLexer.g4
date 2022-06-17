/*
 PALES (DYNAMO) MR (Magnetic Restraint) lexer grammar for ANTLR v4.
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

lexer grammar PalesMRLexer;

/* PALES: Syntax
 See also https://spin.niddk.nih.gov/bax/software/PALES/
*/

/* DYNAMO: Syntax
 See also https://spin.niddk.nih.gov/NMRPipe/dynamo/
*/

Data:			'DATA' -> pushMode(DATA_MODE);

Vars:			'VARS' -> pushMode(VARS_MODE);

Format:			'FORMAT' -> pushMode(FORMAT_MODE);

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
//Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ('E' ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

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
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

mode DATA_MODE;

Sequence:		'SEQUENCE';

One_letter_code:	[ABCDEFGHIKLMNPQRSTVWYZ]+;

SPACE_D:		[ \t]+ -> skip;
RETURN_D:		[\r\n]+ -> popMode;

SECTION_COMMENT_D:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_D:		('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

mode VARS_MODE;

Index:			'INDEX';
Group:			'GROUP';

Segname_I:		'SEGNAME_I';
Resid_I:		'RESID_I';
Resname_I:		'RESNAME_I';
Atomname_I:		'ATOMNAME_I';

Segname_J:		'SEGNAME_J';
Resid_J:		'RESID_J';
Resname_J:		'RESNAME_J';
Atomname_J:		'ATOMNAME_J';

Segname_K:		'SEGNAME_K';
Resid_K:		'RESID_K';
Resname_K:		'RESNAME_K';
Atomname_K:		'ATOMNAME_K';

Segname_L:		'SEGNAME_L';
Resid_L:		'RESID_L';
Resname_L:		'RESNAME_L';
Atomname_L:		'ATOMNAME_L';

A:			[Aa];
B:			[Bb];
C:			[Cc];
D:			[Dd];
DD:			[Dd] [Dd];
FC:			[Ff] [Cc];
S:			[Ss];
W:			[Ww];

D_Lo:			'D_LO';
D_Hi:			'D_HI';
Angle_Lo:		'ANGLE_LO';
Angle_Hi:		'ANGLE_HI';
Phase:			'PHASE';
ObsJ:			'OBSJ';

SPACE_V:		[ \t]+ -> skip;
RETURN_V:		[\r\n]+ -> popMode;

SECTION_COMMENT_V:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_V:		('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

mode FORMAT_MODE;

Format_code:		'%' (DECIMAL 's' | DECIMAL 'd' | (DECIMAL)? '.' DECIMAL 'f');

SPACE_F:		[ \t]+ -> skip;
RETURN_F:		[\r\n]+ -> popMode;

SECTION_COMMENT_F:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_F:		('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

