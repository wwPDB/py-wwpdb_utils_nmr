/*
 Bare PK (Spectral peak list - WSV/TSV with a header) lexer grammar for ANTLR v4.
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

lexer grammar BarePKLexer;

options { caseInsensitive=true; }

Peak:			'Peak' ([ _] ('Number' | 'Id'))? -> pushMode(PEAK_MODE);
X_PPM:			'F1' ([ _] '(ppm)')? -> pushMode(PEAK_MODE);
Y_PPM:			'F2' ([ _] '(ppm)')? -> pushMode(PEAK_MODE);
Z_PPM:			'F3' ([ _] '(ppm)')? -> pushMode(PEAK_MODE);
A_PPM:			'F4' ([ _] '(ppm)')? -> pushMode(PEAK_MODE);

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ('E' ('+' | '-')? DECIMAL)?;
Ambig_float:		(Float | Integer) ((',' | ';' | '|' | '/') (Float | Integer))+;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
//SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' | '-' | '+' | '.' | '*' | '?' | '(' | '{' | '[';
fragment NAME_CHAR:	START_CHAR | '\'' | '"' | ',' | ';' | '#' | '%' | '|' | '/' | ')' | '}' | ']';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t]+ -> skip;
RETURN:			[\r\n]+;

fragment COMMENT_START_CHAR:	('#' | '!' | '\\' | '&' | '/' | '*' | '=');

//ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	(COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '*'+ | COMMENT_START_CHAR '='+ | 'REMARK' 'S'?) ' '* RETURN -> channel(HIDDEN);
LINE_COMMENT:		(COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '*'+ | COMMENT_START_CHAR '='+ | 'REMARK' 'S'?) ~[\r\n]* RETURN -> channel(HIDDEN);

mode PEAK_MODE;

X_ppm:			'F1' ([ _] '(ppm)')?;
Y_ppm:			'F2' ([ _] '(ppm)')?;
Z_ppm:			'F3' ([ _] '(ppm)')?;
A_ppm:			'F4' ([ _] '(ppm)')?;

X_width:		'Line '? 'Width F1' ([ _] '(Hz)')?;
Y_width:		'Line '? 'Width F2' ([ _] '(Hz)')?;
Z_width:		'Line '? 'Width F3' ([ _] '(Hz)')?;
A_width:		'Line '? 'Width F4' ([ _] '(Hz)')?;

Amplitude:		'Amplitude' | 'Intensity' | 'Height';
Volume:			'Volume';

Label:			'Label' | 'Annotation' | 'Assign' 'ment'?;
Comment:		'Comment' | 'Note';

SPACE_FO:		[ \t]+ -> skip;
RETURN_FO:		[\r\n]+ -> popMode;

