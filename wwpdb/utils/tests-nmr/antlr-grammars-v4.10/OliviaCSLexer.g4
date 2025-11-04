/*
 Olivia CS (Assigned chemical shift) lexer grammar for ANTLR v4.
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

lexer grammar OliviaCSLexer;

Typedef:		'TYPEDEF' -> pushMode(TYPEDEF_MODE);

Separator:		'SEPARATOR' -> pushMode(SEPARATOR_MODE);

Format:			'FORMAT\n' -> pushMode(FORMAT_MODE);

Unformat:		'UNFORMAT';

Eof:			'EOF' -> skip;

Null_string:		'-' '-'+;

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

COMMENT:		'REMARK' -> mode(COMMENT_MODE);

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
//SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

Simple_name:		SIMPLE_NAME;

//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' | '-' | '+' | '.' | '*' | '?' | '(' | '{' | '[';
fragment NAME_CHAR:	START_CHAR | '\'' | '"' | ',' | ';' | '#' | '%' | '|' | '/' | ')' | '}' | ']';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t,]+ -> skip;
RETURN:			[\r\n]+;

fragment COMMENT_START_CHAR:	('!' | '\\' | '&' | '/' | '=');

//ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '='+) ' '* RETURN -> channel(HIDDEN);
LINE_COMMENT:		(('#' (' ' | ALPHA_NUM)) | COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '='+) ~[\r\n]* RETURN -> channel(HIDDEN);

mode TYPEDEF_MODE;

Sequence:		'SEQUENCE';
Ass_tbl_h2o:		'ASS_TBL_H2O';
Ass_tbl_tro:		'ASS_TBL_TRO';
Ass_tbl_d2o:		'ASS_TBL_D2O';

SPACE_TD:		[ \t]+ -> skip;
RETURN_TD:		[\r\n]+ -> popMode;

mode SEPARATOR_MODE;

Tab:			'TAB';
Comma:			'COMMA';
Space:			'SPACE';

SPACE_SE:		[ \t]+ -> skip;
RETURN_SE:		[\r\n]+ -> popMode;

mode FORMAT_MODE;

Chain:			'CHAIN';
Resname:		'RESNAME';
Seqnum:			'SEQNUM';
Atomname:		'ATOMNAME';
Shift:			'SHIFT';
Stddev:			'STDDEV';

SPACE_FO:		[ \t,] -> skip;

RETURN_FO:		[\r\n]+ -> pushMode(PRINTF_MODE);

mode PRINTF_MODE;

Printf_string:		'%' ('+' | '-')? DECIMAL? '.'? DECIMAL? ('d' | 'e' | 'f' | 's');

SPACE_PF:		[ \t,] -> skip;

RETURN_PF:		[\r\n]+ -> mode(DEFAULT_MODE);

mode COMMENT_MODE;

Any_name:		~[ \t\r\n]+;

SPACE_CM:		[ \t]+ -> skip;
RETURN_CM:		[\r\n]+ -> mode(DEFAULT_MODE);

