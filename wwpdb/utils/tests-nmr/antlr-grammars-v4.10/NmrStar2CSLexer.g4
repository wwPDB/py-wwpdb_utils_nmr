/*
 NMR-STAR V2.1 (Assigned chemical shift) lexer grammar for ANTLR v4.
 Copyright 2025 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

lexer grammar NmrStar2CSLexer;

Loop:			'loop_';
Stop:			'stop_';

Residue_seq_code:	'_Residue_seq_code';
Residue_label:		'_Residue_label';

Atom_shift_assign_ID:	'_Atom_shift_assign_ID';
Residue_author_seq_code:	'_Residue_author_seq_code';
Atom_name:		'_Atom_name';
Atom_type:		'_Atom_type';
Chem_shift_value:	'_Chem_shift_value';
Chem_shift_value_error:	'_Chem_shift_value_error';
Chem_shift_ambiguity_code:	'_Chem_shift_ambiguity_code';

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
// Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;
// Ambig_float:		(Float | Integer) (( ',' | ';' | '|' | '/') (Float | Integer))+;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;
fragment SEPARATOR:	[,:|/];

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' | '-' | '+' | '.' | '*' | '?' | '(' | '{';
fragment NAME_CHAR:	START_CHAR | '\'' | '"' | ',' | ';' | '#' | '%' | '|' | '/' | ')' | '}';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

Double_quote_string:	'"' SIMPLE_NAME '"';
Single_quote_string:	'\'' SIMPLE_NAME '\'';

SPACE:			[ \t]+ -> skip;
RETURN:			[\r\n]+;

fragment COMMENT_START_CHAR:	('#' | '!' | '\\' | '&' | '/' | '=');

//ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	(COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '*'+ | COMMENT_START_CHAR '='+ | 'REMARK') ' '* RETURN -> channel(HIDDEN);
LINE_COMMENT:		(COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '*'+ | COMMENT_START_CHAR '='+ | 'REMARK') ~[\r\n]* RETURN -> channel(HIDDEN);

