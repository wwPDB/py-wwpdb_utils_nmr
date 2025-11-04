/*
 Olivia PK (Spectral peak list) lexer grammar for ANTLR v4.
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

lexer grammar OliviaPKLexer;

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

Double_quote_string:	'"' SIMPLE_NAME? (' ' SIMPLE_NAME)* '"';
Single_quote_string:	'\'' SIMPLE_NAME? (' ' SIMPLE_NAME)* '\'';
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

Idx_tbl_2d:		'IDX_TBL_2D';
Idx_tbl_3d:		'IDX_TBL_3D';
Idx_tbl_4d:		'IDX_TBL_4D';
Ass_tbl_2d:		'ASS_TBL_2D';
Ass_tbl_3d:		'ASS_TBL_3D';
Ass_tbl_4d:		'ASS_TBL_4D';

SPACE_TD:		[ \t]+ -> skip;
RETURN_TD:		[\r\n]+ -> popMode;

mode SEPARATOR_MODE;

Tab:			'TAB';
Comma:			'COMMA';
Space:			'SPACE';

SPACE_SE:		[ \t]+ -> skip;
RETURN_SE:		[\r\n]+ -> popMode;

mode FORMAT_MODE;

Index:			'INDEX';
X_ppm:			'X_PPM';
Y_ppm:			'Y_PPM';
Z_ppm:			'Z_PPM';
A_ppm:			'A_PPM';
X_hz:			'X_HZ';
Y_hz:			'Y_HZ';
Z_hz:			'Z_HZ';
A_hz:			'A_HZ';
Amplitude:		'AMPLITUDE';
Volume:			'VOLUME';
Vol_err:		'VOL_ERR';
X_chain:		'X_CHAIN';
Y_chain:		'Y_CHAIN';
Z_chain:		'Z_CHAIN';
A_chain:		'A_CHAIN';
X_resname:		'X_RESNAME';
Y_resname:		'Y_RESNAME';
Z_resname:		'Z_RESNAME';
A_resname:		'A_RESNAME';
X_seqnum:		'X_SEQNUM';
Y_seqnum:		'Y_SEQNUM';
Z_seqnum:		'Z_SEQNUM';
A_seqnum:		'A_SEQNUM';
X_assign:		'X_ASSIGN';
Y_assign:		'Y_ASSIGN';
Z_assign:		'Z_ASSIGN';
A_assign:		'A_ASSIGN';
Eval:			'EVAL';
Status:			'STATUS';
User_memo:		'USER_MEMO';
Update_time:		'UPDATE_TIME';

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

