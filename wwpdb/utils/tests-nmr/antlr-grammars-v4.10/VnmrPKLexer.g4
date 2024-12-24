/*
 Vnmr PK (Spectral peak list) lexer grammar for ANTLR v4.
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

lexer grammar VnmrPKLexer;

Peak_id:		'peak id.' -> pushMode(LABEL_MODE);
Format:			'# Format:' -> pushMode(FORMAT_MODE);

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

COMMENT:		('#' | '!')+ -> mode(COMMENT_MODE);
Double_quote_string:	'"' ~["\r\n]* '"';

EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

fragment ASS_EACH_AXIS:	SIMPLE_NAME ([:;&/,.] SIMPLE_NAME)*;

Assignment_2d_ex:	ASS_EACH_AXIS '-' ASS_EACH_AXIS;
Assignment_3d_ex:	ASS_EACH_AXIS '-' ASS_EACH_AXIS '-' ASS_EACH_AXIS;
Assignment_4d_ex:	ASS_EACH_AXIS '-' ASS_EACH_AXIS '-' ASS_EACH_AXIS '-' ASS_EACH_AXIS;

//Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' | '+' | '*' | '?';
fragment NAME_CHAR:	START_CHAR | '\'' | '"';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t]+ -> skip;
RETURN:			[\r\n]+;

ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	(';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '=' '='+ | 'REMARK') ' '* RETURN -> channel(HIDDEN);
LINE_COMMENT:		(';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '=' '='+ | 'REMARK') ~[\r\n]* RETURN -> channel(HIDDEN);

/* VNMR: Peak list format
 See also https://sites.google.com/site/ccpnwiki/home/documentation/contributed-software/bruce-d-ray-utility-programs/readme
*/

mode LABEL_MODE;

Dim_0_ppm:		'Dim 0 (ppm)';
Dim_1_ppm:		'Dim 1 (ppm)';
Dim_2_ppm:		'Dim 2 (ppm)';
Dim_3_ppm:		'Dim 3 (ppm)';
Dev_0:			'Dev. 0';
Dev_1:			'Dev. 1';
Dev_2:			'Dev. 2';
Dev_3:			'Dev. 3';
Amplitude:		'Amplitude';
Intensity_LA:		'Intensity';
Volume_LA:		'Volume';
Assignment:		'Assignment';

SPACE_LA:		[ \t]+ -> skip;
RETURN_LA:		[\r\n]+ -> popMode;

/* VNMR: ll2d peak list format */

mode FORMAT_MODE;

Peak_number:		'Peak_Number';
X_ppm:			'X(ppm)';
Y_ppm:			'Y(ppm)';
Z_ppm:			'Z(ppm)';
A_ppm:			'A(ppm)';
Intensity:		'Intensity';
Volume:			'Volume';
Linewidth_X:		'Linewidth_X(Hz)';
Linewidth_Y:		'Linewidth_Y(Hz)';
Linewidth_Z:		'Linewidth_Z(Hz)';
Linewidth_A:		'Linewidth_A(Hz)';
FWHM_X:			'FWHM_X(Hz)';
FWHM_Y:			'FWHM_Y(Hz)';
FWHM_Z:			'FWHM_Z(Hz)';
FWHM_A:			'FWHM_A(Hz)';

Comment:		'Comment';

SPACE_FO:		[ \t]+ -> skip;
RETURN_FO:		[\r\n]+ -> popMode;

mode COMMENT_MODE;

Any_name:		~[ \t\r\n]+;

SPACE_CM:		[ \t]+ -> skip;
RETURN_CM:		[\r\n]+ -> mode(DEFAULT_MODE);

