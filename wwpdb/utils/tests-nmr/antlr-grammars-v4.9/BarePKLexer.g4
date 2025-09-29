/*
 Bare PK (Spectral peak list) lexer grammar for ANTLR v4.
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

Peak:			[Pp] 'eak' ([ _] ([Nn] 'umber' | [Ii] 'd'))? -> pushMode(PEAK_MODE);

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;
Ambig_float:		(Float | Integer) (( ',' | ';' | '|' | '/') (Float | Integer))+;
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

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' | '-' | '+' | '.' | '*' | '?' | '(' | '{';
fragment NAME_CHAR:	START_CHAR | '\'' | '"' | ',' | ';' | '#' | '%' | '|' | '/' | ')' | '}';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t]+ -> skip;
RETURN:			[\r\n]+;

fragment COMMENT_START_CHAR:	('#' | '!' | '\\' | '&' | '/' | '*' | '=');

//ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	(COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '*'+ | COMMENT_START_CHAR '='+ | [Rr] [Ee] [Mm] [Aa] [Rr] [Kk] [Ss]?) ' '* RETURN -> channel(HIDDEN);
LINE_COMMENT:		(COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '*'+ | COMMENT_START_CHAR '='+ | [Rr] [Ee] [Mm] [Aa] [Rr] [Kk] [Ss]?) ~[\r\n]* RETURN -> channel(HIDDEN);

mode PEAK_MODE;

X_ppm:			[Ff] '1' ([ _] '(ppm)')?;
Y_ppm:			[Ff] '2' ([ _] '(ppm)')?;
Z_ppm:			[Ff] '3' ([ _] '(ppm)')?;
A_ppm:			[Ff] '4' ([ _] '(ppm)')?;
Amplitude:		[Aa] 'mplitude' | [Ii] 'ntensity' | [Hh] 'eight';
Volume:			[Vv] 'olume';

Label:			[Ll] 'abel' | [Aa] 'nnotation' | [Aa] 'ssign' 'ment'?;
Comment:		[Cc] 'omment' | [Nn] 'ote';

SPACE_FO:		[ \t]+ -> skip;
RETURN_FO:		[\r\n]+ -> popMode;

