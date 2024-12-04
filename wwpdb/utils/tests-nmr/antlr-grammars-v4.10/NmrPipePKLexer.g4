/*
 NmrPipe PK (Spectral peak list) lexer grammar for ANTLR v4.
 Copyright 2024 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

lexer grammar NmrPipePKLexer;

/* NmrPipe: Syntax
 See also https://spin.niddk.nih.gov/NMRPipe/
*/

Data:			'DATA' -> pushMode(DATA_MODE);

Vars:			'VARS' -> pushMode(VARS_MODE);

Format:			'FORMAT' -> pushMode(FORMAT_MODE);

Null_value:		'NULLVALUE' -> pushMode(NULL_VALUE_MODE);
Null_string:		'NULLSTRING' -> pushMode(NULL_STRING_MODE);

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

Any_name:		~[ \t\r\n]+;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' | '-' | '+' | '.' | '*' | '#' | '?';
fragment NAME_CHAR:	START_CHAR | '\'' | '"';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t]+ -> skip;
RETURN:			[\r\n]+;

ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '=' '='+ | 'REMARK') ' '* RETURN -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '=' '='+ | 'REMARK') ~[\r\n]* RETURN -> channel(HIDDEN);

mode DATA_MODE;

X_axis_DA:		'X_AXIS';
Y_axis_DA:		'Y_AXIS';
Z_axis_DA:		'Z_AXIS';
A_axis_DA:		'A_AXIS';

Ppm_value_DA:		Float 'ppm';

Integer_DA:		('+' | '-')? DECIMAL;
Float_DA:		('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Real_DA:		('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;

Simple_name_DA:		SIMPLE_NAME;

SPACE_DA:		[ \t]+ -> skip;
RETURN_DA:		[\r\n]+ -> popMode;

//SECTION_COMMENT_DA:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* RETURN_DA -> channel(HIDDEN);
LINE_COMMENT_DA:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* RETURN_DA -> channel(HIDDEN);

mode VARS_MODE;

Index:			'INDEX';
X_axis:			'X_AXIS';
Y_axis:			'Y_AXIS';
Z_axis:			'Z_AXIS';
A_axis:			'A_AXIS';

Dx:			'DX';
Dy:			'DY';
Dz:			'DZ';
Da:			'DA';

X_ppm:			'X_PPM';
Y_ppm:			'Y_PPM';
Z_ppm:			'Z_PPM';
A_ppm:			'A_PPM';

X_hz:			'X_HZ';
Y_hz:			'Y_HZ';
Z_hz:			'Z_HZ';
A_hz:			'A_HZ';

Xw:			'XW';
Yw:			'YW';
Zw:			'ZW';
Aw:			'AW';

Xw_hz:			'XW_HZ';
Yw_hz:			'YW_HZ';
Zw_hz:			'ZW_HZ';
Aw_hz:			'AW_HZ';

X1:			'X1';
X3:			'X3';
Y1:			'Y1';
Y3:			'Y3';
Z1:			'Z1';
Z3:			'Z3';
A1:			'A1';
A3:			'A3';

Height:			'HEIGHT';
DHeight:		'DHEIGHT';
Vol:			'VOL';
Pchi2:			'PCHI2';
Type:			'TYPE';
Ass:			'ASS';
ClustId:		'CLUSTID';
Memcnt:			'MEMCNT';
Trouble:		'TROUBLE';

Integer_VA:		('+' | '-')? DECIMAL;
Float_VA:		('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Real_VA:		('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;

Simple_name_VA:		SIMPLE_NAME;

SPACE_VA:		[ \t]+ -> skip;
RETURN_VA:		[\r\n]+ -> popMode;

//SECTION_COMMENT_VA:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* RETURN_VA -> channel(HIDDEN);
LINE_COMMENT_VA:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* RETURN_VA -> channel(HIDDEN);

mode FORMAT_MODE;

Format_code:		'%' DECIMAL? ('s' | 'd' | '.' DECIMAL 'f' | '+'? 'e');

SPACE_FO:		[ \t]+ -> skip;
RETURN_FO:		[\r\n]+ -> popMode;

//SECTION_COMMENT_FO:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* RETURN_FO -> channel(HIDDEN);
LINE_COMMENT_FO:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* RETURN_FO -> channel(HIDDEN);

mode NULL_VALUE_MODE;

Any_name_NV:		~[ \t\r\n]+;

SPACE_NV:		[ \t]+ -> skip;
RETURN_NV:		[\r\n]+ -> popMode;

mode NULL_STRING_MODE;

Any_name_NS:		~[ \t\r\n]+;

SPACE_NS:		[ \t]+ -> skip;
RETURN_NS:		[\r\n]+ -> popMode;

