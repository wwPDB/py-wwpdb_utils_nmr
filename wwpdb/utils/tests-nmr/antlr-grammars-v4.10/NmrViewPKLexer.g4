/*
 NmrView PK (Spectral peak list) lexer grammar for ANTLR v4.
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

lexer grammar NmrViewPKLexer;

Label:			'label' -> pushMode(LABEL_MODE);

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
fragment START_CHAR:	ALPHA_NUM | '_' | '-' | '+' | '.' | '*' | '?' | '(';
fragment NAME_CHAR:	START_CHAR | '\'' | '"' | ',' | ';' | '#' | '%' | '|' | '/' | ')';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t]+ -> skip;
RETURN:			[\r\n]+;

fragment COMMENT_START_CHAR:	('#' | '!' | ';' | '\\' | '&' | '/' | '*' | '=');

L_brace:		'{'+ -> pushMode(ENCLOSE_DATA_MODE);

SECTION_COMMENT:	(COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '*'+ | COMMENT_START_CHAR '='+ | 'REMARK' 'S'?) ' '* RETURN -> channel(HIDDEN);
LINE_COMMENT:		(COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '*'+ | COMMENT_START_CHAR '='+ | 'REMARK' 'S'?) ~[\r\n]* RETURN -> channel(HIDDEN);

/* NMRView: Peak list format
 See also https://github.com/onemoonsci/nmrfxprocessordocs/blob/master/pages/02.viewer/08.refcmds/01.ref/docs.md
*/

mode LABEL_MODE;

Dataset:		'dataset';
Sw:			'sw';
Sf:			'sf';
Condition:		'condition';

L_name:			Simple_name '.L';
P_name:			Simple_name '.P';
W_name:			Simple_name '.W';
B_name:			Simple_name '.B';
E_name:			Simple_name '.E';
J_name:			Simple_name '.J';
U_name:			Simple_name '.U';

Vol:			'vol';
Int:			'int';
Stat:			'stat';
Comment:		'comment';
Flag0:			'flag0' ' '* ('flag' [1-9] ' '*)* [\r\n]+ -> popMode;

Simple_name_LA:		SIMPLE_NAME;
Float_LA:		Float;

SPACE_LA:		[ \t\r]+ -> skip;

SINGLE_NL_LA:		'\n';

ENCLOSE_DATA_LA:	'{' ' '* (Float | (SIMPLE_NAME | ' ')*?) ' '* '}';

mode ENCLOSE_DATA_MODE;

Any_name:		~[{} \t\r\n]+;

SPACE_CM:		[ \t]+ -> skip;
R_brace:		'}'+ -> popMode;

