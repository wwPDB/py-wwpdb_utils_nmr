/*
 DIANA (Assigned chemical shift) lexer grammar for ANTLR v4.10 or later
 Copyright 2026 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

lexer grammar DianaCSLexer;

options { caseInsensitive=true; }

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ('E' ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

COMMENT:		('#' | '!')+ -> mode(COMMENT_MODE);

Shifts:			'SHIFTS';

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"' | '*' | '#' | '|';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t\r\n]+ -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ |
			 'REMARK' 'S'? | 'COORDS' | 'QCONVR' | 'COUNT' | 'JNRL' | 'NOEUPP' | 'NOELOW' | 'HBUPP' | 'HBLOW' | 'SSUPP' | 'SSLOW' | 'JCOUPL' | 'ANGLE' | 'STEREO' | 'MASTER' | 'END') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		(';' | '\\' | '&' | '<' | '>' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ |
			 'REMARK' 'S'? | 'COORDS' | 'QCONVR' | 'COUNT' | 'JNRL' | 'NOEUPP' | 'NOELOW' | 'HBUPP' | 'HBLOW' | 'SSUPP' | 'SSLOW' | 'JCOUPL' | 'ANGLE' | 'STEREO' | 'MASTER' | 'END') ~[\r\n]* -> channel(HIDDEN);

mode COMMENT_MODE;

Any_name:		~[ \t\r\n]+;

SPACE_CM:		[ \t]+ -> skip;
RETURN_CM:		[\r\n]+ -> mode(DEFAULT_MODE);
