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
fragment DEC_DOT_DEC:	(DECIMAL '.' PRECISION?) | ('.' PRECISION);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;
fragment PRECISION:	DEC_DIGIT DEC_DIGIT? DEC_DIGIT?;

fragment PDB_IGNORED:	'HEADER' DECIMAL? | 'OBSLTE' DECIMAL? | 'TITLE' DECIMAL? | 'SPLIT' DECIMAL? | 'CAVEAT' DECIMAL? | 'COMPND' DECIMAL? |
			'SOURCE' DECIMAL? | 'KEYWDS' DECIMAL? | 'EXPDTA' DECIMAL? | 'NUMMDL' DECIMAL? | 'MDLTYP' DECIMAL? |
			'AUTHOR' DECIMAL? | 'REVDAT' DECIMAL? | 'SPRSDE' DECIMAL? | 'JRNL' | 'REMARK' DECIMAL? | 'DBREF' | 'DBREF1' DECIMAL? |
			'DBREF2' DECIMAL? | 'SEQADV' DECIMAL? | 'SEQRES' DECIMAL? | 'MODRES' DECIMAL? | 'HET' | 'HETNAM' DECIMAL? |
			'HETSYN' DECIMAL? | 'FORMUL' DECIMAL? | 'HELIX' | 'SHEET' | 'SSBOND' DECIMAL? | 'TURN' | 'LINK' | 'CISPEP' DECIMAL? |
			'SITE' | 'CRYST1' DECIMAL? | 'ORIGX1' DECIMAL? | 'ORIGX2' DECIMAL? | 'ORIGX3' DECIMAL? | 'SCALE1' DECIMAL?
			| 'SCALE2' DECIMAL? | 'SCALE3' DECIMAL? | 'MTRIX1' DECIMAL? | 'MTRIX2' DECIMAL? | 'MTRIX3' DECIMAL? | 'MODEL'
			| 'ANISOU' DECIMAL? | 'ENDMDL' DECIMAL? | 'CONECT' DECIMAL? | 'MASTER' DECIMAL?;

COMMENT:		('#'+ | '!'+ | PDB_IGNORED) -> mode(COMMENT_MODE);

Hetatm_decimal:		'HETATM' DECIMAL;

Integer_concat_alt:	'-'? DECIMAL [A-Z];

Float_concat_2:		('+' | '-')? (DECIMAL | DEC_DOT_DEC) ('-' | '1') DEC_DOT_DEC;
Float_concat_3:		('+' | '-')? (DECIMAL | DEC_DOT_DEC) ('-' | '1') DEC_DOT_DEC ('-' | '1') DEC_DOT_DEC;

Float_100_concat:	(DECIMAL | DEC_DOT_DEC) '100.' '0'+;

Atom:			'ATOM';
Hetatm:			'HETATM';
Ter:			'TER' -> mode(COMMENT_MODE);
End:			'END' -> mode(COMMENT_MODE);

Simple_name:		SIMPLE_NAME;
Null_value:		'?' | '-' | '.';

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' | '\'';
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

