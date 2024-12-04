/*
 Xeasy PK (Spectral peak list) lexer grammar for ANTLR v4.
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

lexer grammar XeasyPKLexer;

Num_of_dim:		'#' ~[\t\r\n]* 'Number of dimensions' -> pushMode(NUM_OF_DIM_MODE);

Format:			'#FORMAT' -> pushMode(FORMAT_MODE);

Iname:			'#INAME' -> pushMode(INAME_MODE);

Cyana_format:		'#CYANAFORMAT' -> pushMode(CYANA_FORMAT_MODE);

Spectrum:		'#SPECTRUM' -> pushMode(SPECTRUM_MODE);

Tolerance:		'#TOLERANCE' -> pushMode(TOLERANCE_MODE);

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;
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

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' | '-' | '+' | '.' | '*' | '#' | '?';
fragment NAME_CHAR:	START_CHAR | '\'' | '"';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t\r\n]+ -> skip;
RETURN:			[\r\n]+;

ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '=' '='+ | 'REMARK') ' '* RETURN -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '=' '='+ | 'REMARK') ~[\r\n]* RETURN -> channel(HIDDEN);

mode NUM_OF_DIM_MODE;

Integer_ND:		('+' | '-')? DECIMAL;

SPACE_ND:		[ \t]+ -> skip;
RETURN_ND:		[\r\n]+ -> popMode;

mode FORMAT_MODE;

Simple_name_FO:		SIMPLE_NAME;

SPACE_FO:		[ \t]+ -> skip;
RETURN_FO:		[\r\n]+ -> popMode;

mode INAME_MODE;

Integer_IN:		('+' | '-')? DECIMAL;
Simple_name_IN:		SIMPLE_NAME;

SPACE_IN:		[ \t]+ -> skip;
RETURN_IN:		[\r\n]+ -> popMode;

mode CYANA_FORMAT_MODE;

Simple_name_CY:		SIMPLE_NAME;

SPACE_CY:		[ \t]+ -> skip;
RETURN_CY:		[\r\n]+ -> popMode;

mode SPECTRUM_MODE;

Simple_name_SP:		SIMPLE_NAME;

SPACE_SP:		[ \t]+ -> skip;
RETURN_SP:		[\r\n]+ -> popMode;

mode TOLERANCE_MODE;

Float_TO:		Float;

TOACE_TO:		[ \t]+ -> skip;
RETURN_TO:		[\r\n]+ -> popMode;

