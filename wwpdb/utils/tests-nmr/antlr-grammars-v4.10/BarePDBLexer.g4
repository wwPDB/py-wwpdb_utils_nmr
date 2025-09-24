/*
 Bare PDB lexer grammar for ANTLR v4.10 or later
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

lexer grammar BarePDBLexer;

/* Numbers and Strings - Syntax
*/
Integer:		'-'? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

fragment PDB_IGNORED:	'HEADER' | 'OBSLTE' | 'TITLE' | 'SPLIT' | 'CAVEAT' | 'COMPND' | 'SOURCE' | 'KEYWDS' | 'EXPDTA' | 'NUMMDL' | 'MDLTYP' |
			'AUTHOR' | 'REVDAT' | 'SPRSDE' | 'JRNL' | 'REMARK' | 'DBREF' | 'DBREF1' | 'DBREF2' | 'SEQADV' | 'SEQRES' | 'MODRES' |
			'HET' | 'HETNAM' | 'HETSYN' | 'FORMUL' | 'HELIX' | 'SHEET' | 'SSBOND' | 'TURN' | 'LINK' | 'CISPEP' | 'SITE' |
			'CRYST1' | 'ORIGX1' | 'ORIGX2' | 'ORIGX3' | 'SCALE1' | 'SCALE2' | 'SCALE3' | 'MTRIX1' | 'MTRIX2' | 'MTRIX3' | 'MODEL'
			| 'ANISOU' | 'ENDMDL' | 'CONECT' | 'MASTER';

COMMENT:		('#'+ | '!'+ | PDB_IGNORED) -> mode(COMMENT_MODE);

Hetatm_decimal:		'HETATM' DECIMAL;
Float_concat_2:		('+' | '-')? (DECIMAL | DEC_DOT_DEC) '-' DEC_DOT_DEC;
Float_concat_3:		('+' | '-')? (DECIMAL | DEC_DOT_DEC) '-' DEC_DOT_DEC '-' DEC_DOT_DEC;

Atom:			'ATOM';
Hetatm:			'HETATM';
Ter:			'TER' -> mode(COMMENT_MODE);
End:			'END';

Simple_name:		SIMPLE_NAME;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '/' | '-' | '+' | '.' | ',' | ':' | '"' | '*';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t\r\n]+ -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	(';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		(';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+) ~[\r\n]* -> channel(HIDDEN);

mode COMMENT_MODE;

Any_name:		~[ \t\r\n]+;

SPACE_CM:		[ \t]+ -> skip;
RETURN_CM:		[\r\n]+ -> mode(DEFAULT_MODE);

