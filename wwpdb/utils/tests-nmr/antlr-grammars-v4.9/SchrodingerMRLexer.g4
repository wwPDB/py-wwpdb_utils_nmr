/*
 SCHRODINGER MR (Magnetic Restraint) lexer grammar for ANTLR v4.9
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

/* Case-Insensitive Lexing
 See also https://github.com/antlr/antlr4/blob/master/doc/case-insensitive-lexing.md
*/
fragment A:		[aA]; // match either an A or 'A'
fragment B:		[bB];
fragment C:		[cC];
fragment D:		[dD];
fragment E:		[eE];
fragment F:		[fF];
fragment G:		[gG];
fragment H:		[hH];
fragment I:		[iI];
fragment J:		[jJ];
fragment K:		[kK];
fragment L:		[lL];
fragment M:		[mM];
fragment N:		[nN];
fragment O:		[oO];
fragment P:		[pP];
fragment Q:		[qQ];
fragment R:		[rR];
fragment S:		[sS];
fragment T:		[tT];
fragment U:		[uU];
fragment V:		[vV];
fragment W:		[wW];
fragment X:		[xX];
fragment Y:		[yY];
fragment Z:		[zZ];

Set:			S E T;

Struct:			'&' S T R U C T -> mode(STRUCT_MODE);
Dist:			'&' D I S T;
Tors:			'&' T R O S;
Angle:			'&' A N G L E;
End:			'&' E N D;

Atom1:			A T O M '1';
Atom2:			A T O M '2';
Atom3:			A T O M '3';
Atom4:			A T O M '4';

Lo:			L O;
Up:			U P;
Fc:			F C;
Target:			T A R G E T;

Comma:			',';

/* Atom Selection Language - ASL
  See also https://shaker.umh.es/computing/Schrodinger_suites/maestro_command_reference.pdf
*/

// token
Entry:			E N? T? T? Y? '.';
Molecule:		M O? L? E? C? U? L? E? '.';
Chain:			C H? A? I? N? '.';
Residue:		R E? S? I? D? U? E? '.';
Atom:			A T? O? M? '.';
Backbone:		B A C K B O N E;
Sidechain:		S I D E C H A I N;
Water:			W A T E R | '/H2-O3-H2/';
Methyl:			'/C3(-H1)(-H1)(-H1)/';
Amide:			'/C2(=O2)-N2-H2/';
Smarts:			S M A R T S '.';

Entry_name:		Entry N A? M? E?;

Molecule_number:	Molecule N U? M? B? E? R?;
Molecule_modulo:	Molecule M O? D? U? L? O?;
Molecule_entrynum:	Molecule E N? T? R? Y? N? U? M?;
Molecule_atoms:		Molecule A T? O? M? S?;
Molecule_weight:	Molecule W E? I? G? H? T?;

Chain_name:		Chain N A? M? E?;

Residue_name_or_number:	Residue N (A? M? E? | U? M? B? E? R?);
Residue_ptype:		Residue P T Y? P? E?;
Residue_mtype:		Residue M T? Y? P? E?;
Residue_polarity:	Residue P O L A? R? I? T? Y? -> mode(POLARITY_MODE);
Residue_secondary_structure:	Residue S E C O? N? D? A? R? Y? '_'? S? T? R? C? T? U? R? E? -> mode(SECONDARY_STRUCT_MODE);
Residue_position:		Residue P O S I? T? I? O? N?;
Residue_inscode:		Residue I N? S? C? O? D? E?;

Atom_ptype:		Atom P T Y? P? E?;
Atom_name:		Atom N A M? E?;
Atom_number:		Atom N U? M? B? E? R?;
Atom_molnum:		Atom M O L? N? U? M?;
Atom_entrynum:		Atom E N T? R? Y? N? U? M?;
Atom_mtype:		Atom M T? Y? P? E?;
Atom_element:		Atom E L? E? M? E? N? 'nt'?;
Atom_attachements:	Atom A T T A? C? H? E? M? E? N? T? S?;
Atom_atomicnumber:	Atom A T O M? I? C? N? U? M? B? E? R?;
Atom_charge:		Atom C H? A? R? G? E?;
Atom_formalcharge:	Atom F O? R? M? A? L? C? H? A? R? G? E?;
Atom_displayed:		Atom D I? S? P? L? A? Y? E? D?;
Atom_selected:		Atom S E? L? E? C? T? E? D?;

// factor
Or_op:			(O R | '|' | U N I O N);
And_op:			(A N D | '&' | I N T E R S E C T I O N);
Not_op:			(N O T | '!');

Fillres_op:		F I L L R E S;
Fillmol_op:		F I L L M O L;

Within_op:		W I T H I N;
Beyond_op:		B E Y O N D;

Withinbonds_op:		W I T H I N B O N D S;
Beyondbonds_op:		B E Y O N D B O N D S;

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

COMMENT:		'#'+ -> mode(COMMENT_MODE);

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
SECTION_COMMENT:	('#' | ';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+ | R E M A R K) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		(';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+ | R E M A R K) ~[\r\n]* -> channel(HIDDEN);

mode STRUCT_MODE;

Param_name:		~[ \t\r\n]+;
Equ_op_SM:		'=';

SPACE_SM:		[ \t]+ -> skip;
RETURN_SM:		[\r\n]+;

End_SM:			'&' E N D -> popMode;

mode COMMENT_MODE;

Any_name:		~[ \t\r\n]+;

SPACE_CM:		[ \t]+ -> skip;
RETURN_CM:		[\r\n]+ -> popMode;

mode POLARITY_MODE;

Hydrophilic:		(N O T | '!') SPACE_PM+ Hydrophobic -> popMode;
Hydrophobic:		H Y? D? R? O? P? H? B? I? C? -> popMode;
Non_polar:		(N O T | '!') SPACE_PM+ Polar -> popMode;
Polar:			P O L A? R? -> popMode;
Charged:		((Positive CONTINUE_PM Negative) | (Negative CONTINUE_PM Positive)) -> popMode;
Positive:		P O S I? T? I? V? E? -> popMode;
Negative:		N E? G? A? T? I? V? E? -> popMode;

fragment SPACE_PM:	[ \t\r\n];
fragment CONTINUE_PM:	SPACE_PM* (O R | '|' | ',' | U N I O N) SPACE_PM*;

IGNORE_SPACE_PM:	SPACE_PM -> skip;

mode SECONDARY_STRUCT_MODE;

Helix_or_strand:	((Helix CONTINUE_SSM Strand) | (Strand CONTINUE_SSM Helix)) -> popMode;
Strand_or_loop:		((Strand CONTINUE_SSM Loop) | (Loop CONTINUE_SSM Strand)) -> popMode;
Helix_or_loop:		((Helix CONTINUE_SSM Loop) | (Loop CONTINUE_SSM Helix)) -> popMode;

Helix:			H E? L? I? X? -> popMode;
Strand:			S T? R? A? N? D? -> popMode;
Loop:			L O? O? P? -> popMode;

fragment SPACE_SSM:	[ \t\r\n];
fragment CONTINUE_SSM:	SPACE_SSM* (O R | '|' | ',') SPACE_SSM*;

IGNORE_SPACE_SSM:	SPACE_SSM -> skip;

