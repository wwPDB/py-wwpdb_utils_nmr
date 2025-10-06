/*
 ARIA MR (Magnetic Restraint) lexer grammar for ANTLR v4.9 or later
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

lexer grammar AriaMRLexer;

COMMA:			',' -> skip;

Integer:		('+' | '-')? DECIMAL COMMA?;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) COMMA?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

RefSpec:		'ref_spec:' -> pushMode(REF_SPEC_MODE);
RefPeak:		'ref_peak:';
Id:			'id:';
D:			'd:';
U:			'u:';
UViol:			'u_viol:';
PViol:			'%_viol:';
Viol:			'viol:' -> pushMode(VIOL_MODE);
Reliable:		'reliable:' -> pushMode(RELIABLE_MODE);
AType:			'a_type:' -> pushMode(ATYPE_MODE);
Weight:			'weight:';

PlusMinus:		'+/-';
Hyphen:			'-';

fragment YesNo:		('yes' | 'no') COMMA?;
fragment ATypeCode:	('M' | 'S' | 'A') COMMA?;

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"' | '*' | '#';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR* COMMA?;

SPACE:			[ \t\r\n]+ -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ~[\r\n]* -> channel(HIDDEN);

mode REF_SPEC_MODE;

SPACE_RS:		[\t]+ -> skip;

RefSpecName:		~[,\t\r\n]+ ','? -> popMode;

RETURN_RS:		[\r\n]+ -> popMode;

mode VIOL_MODE;

SPACE_V:		[, \t]+ -> skip;

ViolFlag:		YesNo ','? -> popMode;

RETURN_V:		[\r\n]+ -> popMode;

mode RELIABLE_MODE;

SPACE_R:		[, \t]+ -> skip;

ReliableFlag:		YesNo ','? -> popMode;

RETURN_R:		[\r\n]+ -> popMode;

mode ATYPE_MODE;

SPACE_A:		[, \t]+ -> skip;

ATypeFlag:		ATypeCode ','? -> popMode;

RETURN_A:		[\r\n]+ -> popMode;

