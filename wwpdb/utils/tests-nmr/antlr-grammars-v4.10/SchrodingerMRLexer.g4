/*
 SCHRODINGER MR (Magnetic Restraint) lexer grammar for ANTLR v4.10 or later
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

lexer grammar SchrodingerMRLexer;

options { caseInsensitive=true; }

Set:			'set';

Struct:			'&STRUCT' -> mode(STRUCT_MODE);
Dist:			'&DIST';
Tors:			'&TROS';
Angle:			'&ANGLE';
End:			'&END';

Atom1:			'atom1';
Atom2:			'atom2';
Atom3:			'atom3';
Atom4:			'atom4';

Lo:			'lo';
Up:			'up';
Fc:			'fc';
Target:			'target';

Comma:			',';

/* MacroModel command
  See also https://shaker.umh.es/computing/Schrodinger_suites/macromodel_reference_manual.pdf
*/

FXDI:			'FXDI';
FXBA:			'FXBA';
FXTA:			'FXTA';
FXHB:			'FXHB';

/* Atom Selection Language - ASL
  See also https://shaker.umh.es/computing/Schrodinger_suites/maestro_command_reference.pdf
*/

// token
Entry:			'e' 'n'? 't'? 'r'? 'y'? '.';
Molecule:		'm' 'o'? 'l'? 'e'? 'c'? 'u'? 'l'? 'e'? '.';
Chain:			'c' 'h'? 'a'? 'i'? 'n'? '.';
Residue:		'r' 'e'? 's'? 'i'? 'd'? 'u'? 'e'? '.';
Atom:			'a' 't'? 'o'? 'm'? '.';
Backbone:		'backbone';
Sidechain:		'sidechain';
Water:			'water' | '/H2-O3-H2/';
Methyl:			'/C3(-H1)(-H1)(-H1)/';
Amide:			'/C2(=O2)-N2-H2/';
Smarts:			'smarts.';

Entry_name:		Entry 'n' 'a'? 'm'? 'e'?;

Molecule_number:	Molecule 'n' 'u'? 'm'? 'b'? 'e'? 'r'?;
Molecule_modulo:	Molecule 'm' 'o'? 'd'? 'u'? 'l'? 'o'?;
Molecule_entrynum:	Molecule 'e' 'n'? 't'? 'r'? 'y'? 'n'? 'u'? 'm'?;
Molecule_atoms:		Molecule 'a' 't'? 'o'? 'm'? 's'?;
Molecule_weight:	Molecule 'w' 'e'? 'i'? 'g'? 'h'? 't'?;

Chain_name:		Chain 'n' 'a'? 'm'? 'e'?;

Residue_name_or_number:	Residue 'n' ('a'? 'm'? 'e'? | 'u'? 'm'? 'b'? 'e'? 'r'?);
Residue_ptype:		Residue 'pt' 'y'? 'p'? 'e'?;
Residue_mtype:		Residue 'm' 't'? 'y'? 'p'? 'e'?;
Residue_polarity:	Residue 'pol' 'a'? 'r'? 'i'? 't'? 'y'? -> mode(POLARITY_MODE);
Residue_secondary_structure:	Residue 'sec' 'o'? 'n'? 'd'? 'a'? 'r'? 'y'? '_'? 's'? 't'? 'r'? 'c'? 't'? 'u'? 'r'? 'e'? -> mode(SECONDARY_STRUCT_MODE);
Residue_position:		Residue 'pos' 'i'? 't'? 'i'? 'o'? 'n'?;
Residue_inscode:		Residue 'i' 'n'? 's'? 'c'? 'o'? 'd'? 'e'?;

Atom_ptype:		Atom 'pt' 'y'? 'p'? 'e'?;
Atom_name:		Atom 'na' 'm'? 'e'?;
Atom_number:		Atom 'n' 'u'? 'm'? 'b'? 'e'? 'r'?;
Atom_molnum:		Atom 'mo' 'l'? 'n'? 'u'? 'm'?;
Atom_entrynum:		Atom 'en' 't'? 'r'? 'y'? 'n'? 'u'? 'm'?;
Atom_mtype:		Atom 'm' 't'? 'y'? 'p'? 'e'?;
Atom_element:		Atom 'e' 'l'? 'e'? 'm'? 'e'? 'n'? 'nt'?;
Atom_attachements:	Atom 'att' 'a'? 'c'? 'h'? 'e'? 'm'? 'e'? 'n'? 't'? 's'?;
Atom_atomicnumber:	Atom 'ato' 'm'? 'i'? 'c'? 'n'? 'u'? 'm'? 'b'? 'e'? 'r'?;
Atom_charge:		Atom 'c' 'h'? 'a'? 'r'? 'g'? 'e'?;
Atom_formalcharge:	Atom 'f' 'o'? 'r'? 'm'? 'a'? 'l'? 'c'? 'h'? 'a'? 'r'? 'g'? 'e'?;
Atom_displayed:		Atom 'd' 'i'? 's'? 'p'? 'l'? 'a'? 'y'? 'e'? 'd'?;
Atom_selected:		Atom 's' 'e'? 'l'? 'e'? 'c'? 't'? 'e'? 'd'?;

// factor
Or_op:			('or' | '|' | 'union');
And_op:			('and' | '&' | 'intersection');
Not_op:			('not' | '!');

Fillres_op:		'fillres';
Fillmol_op:		'fillmol';

Within_op:		'within';
Beyond_op:		'beyond';

Withinbonds_op:		'withinbonds';
Beyondbonds_op:		'beyondbonds';

/* Numbers and Strings */
Integer:		'-'? DECIMAL;
IntRange:		DECIMAL '-' DECIMAL;
//Logical:		'TRUE' | 'FALSE' | 'ON' | 'OFF';
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
FloatRange:		Float '-' Float;
Slash_quote_string:	'/' ~["\r\n]* '/';
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

COMMENT:		'#'+ -> channel(HIDDEN);

Simple_name:		SIMPLE_NAME;
Simple_names:		(WILDCARD | WILDCARD* SIMPLE_NAME WILDCARD+) POST_WC_CHAR*;
Integers:		(WILDCARD | WILDCARD* Integer WILDCARD+) DEC_DIGIT*;
//Class_name:		SIMPLE_NAME;
//Class_names:		(WILDCARD | WILDCARD* SIMPLE_NAME WILDCARD+) POST_WC_CHAR*;
//Segment_name:		SIMPLE_NAME;
//Segment_names:	(WILDCARD | WILDCARD* SIMPLE_NAME WILDCARD+) POST_WC_CHAR*;
//Residue_number:	Integer;
//Residue_numbers:	(WILDCARD | WILDCARD* Residue_number WILDCARD+) DEC_DIGIT*;
//Residue_name:		SIMPLE_NAME;
//Residue_names:	(WILDCARD | WILDCARD* SIMPLE_NAME WILDCARD+) POST_WC_CHAR*;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;
//Atom_names:		(WILDCARD | WILDCARD* Atom_name WILDCARD+) POST_WC_CHAR*;

fragment WILDCARD:	'*' | '?' | '#';

fragment ALPHA:		[A-Z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"';
fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;
fragment POST_WC_CHAR:	DEC_DIGIT | '\'' | 'P';

L_paren:		'(';
R_paren:		')';
Lt_op:			'<';
Gt_op:			'>';
Leq_op:			'<=';
Geq_op:			'>=';
Equ_op:			'=';

SPACE:			[ \t\r\n]+ -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | ';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		(';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

mode STRUCT_MODE;

Param_name:		~[ \t\r\n]+;
Equ_op_SM:		'=';

SPACE_SM:		[ \t]+ -> skip;
RETURN_SM:		[\r\n]+;

End_SM:			'&END' -> popMode;

mode POLARITY_MODE;

fragment HYDROPHOBIC:	'h' 'y'? 'd'? 'r'? 'o'? 'p'? 'h'? 'b'? 'i'? 'c'?;
fragment POLAR:		'pol' 'a'? 'r'?;
fragment POSITIVE:	'pos' 'i'? 't'? 'i'? 'v'? 'e'?;
fragment NEGATIVE:	'n' 'e'? 'g'? 'a'? 't'? 'i'? 'v'? 'e'?;

Hydrophilic:		('not' | '!') SPACE_PM+ HYDROPHOBIC -> popMode;
Hydrophobic:		HYDROPHOBIC -> popMode;
Non_polar:		('not' | '!') SPACE_PM+ POLAR -> popMode;
Polar:			POLAR -> popMode;
Charged:		((POSITIVE CONTINUE_PM NEGATIVE) | (NEGATIVE CONTINUE_PM POSITIVE)) -> popMode;
Positive:		POSITIVE -> popMode;
Negative:		NEGATIVE -> popMode;

fragment SPACE_PM:	[ \t\r\n];
fragment CONTINUE_PM:	SPACE_PM* ('or' | '|' | ',' | 'union') SPACE_PM*;

IGNORE_SPACE_PM:	SPACE_PM -> skip;

mode SECONDARY_STRUCT_MODE;

fragment HELIX:		'h' 'e'? 'l'? 'i'? 'x'?;
fragment STRAND:	's' 't'? 'r'? 'a'? 'n'? 'd'?;
fragment LOOP:		'l' 'o'? 'o'? 'p'?;

Helix_or_strand:	((HELIX CONTINUE_SSM STRAND) | (STRAND CONTINUE_SSM HELIX)) -> popMode;
Strand_or_loop:		((STRAND CONTINUE_SSM LOOP) | (LOOP CONTINUE_SSM STRAND)) -> popMode;
Helix_or_loop:		((HELIX CONTINUE_SSM LOOP) | (LOOP CONTINUE_SSM HELIX)) -> popMode;

Helix:			HELIX -> popMode;
Strand:			STRAND -> popMode;
Loop:			LOOP -> popMode;

fragment SPACE_SSM:	[ \t\r\n];
fragment CONTINUE_SSM:	SPACE_SSM* ('or' | '|' | ',') SPACE_SSM*;

IGNORE_SPACE_SSM:	SPACE_SSM -> skip;

