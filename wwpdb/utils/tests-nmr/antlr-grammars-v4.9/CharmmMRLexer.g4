/*
 CHARMM MR (Magnetic Restraint) lexer grammar for ANTLR v4.
 Copyright 2022 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

lexer grammar CharmmMRLexer;

/* Case-Insensitive Lexing
 See also https://github.com/antlr/antlr4/blob/master/doc/case-insensitive-lexing.md
*/
fragment A:		[aA]; // match either an 'a' or 'A'
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

Set:			S E T -> pushMode(VECTOR_EXPR_MODE);
End:			E N D;

/* CHARMM: CONSTRAINTS - Holding atoms in place
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
Cons:			C O N S T? R? A? I? N? T?;

Harmonic:		H A R M O? N? I? C?;
Absolute:		A B S O L? U? T? E?;
Bestfit:		B E S T F? I? T?;
Relative:		R E L A T? I? V? E?;
Clear:			C L E A R?;

// force-const-spec
Force:			F O R C E?;
Mass:			M A S S;
Weight:			W E I G H? T? I? N? G?;

// absolute-specs
Exponent:		E X P O N? E? N? T?;
XScale:			X S C A L? E?;
YScale:			Y S C A L? E?;
ZScale:			Z S C A L? E?;

// bestfit-specs
NoRotation:		N O R O T? A? T? I? O? N?;
NoTranslation:		N O T R A? N? S? L? A? T? I? O? N?;

// coordinate-spec
Main:			M A I N;
Comp:			C O M P;
Keep:			K E E P;

/* CHARMM: CONSTRAINTS - Holding dihedrals near selected values
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
//Cons:			C O N S T? R? A? I? N? T?;

Dihedral:		D I H E D? R? A? L?;
ByNumber:		B Y N U M? B? E? R?;
//Force:		F O R C E?;
Min:			M I N;
Period:			P E R I O? D?;
//Comp:			C O M P;
Width:			W I D T H?;
//Main:			M A I N;

ClDh:			C L D H;

/* CHARMM: CONSTRAINTS - Holding Internal Coordinates near selected values
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
//Cons:			C O N S T? R? A? I? N? T?;

IC:			I C;
Bond:			B O N D;
//Exponent:		E X P O N? E? N? T?;
Upper:			U P P E R?;
Angle:			A N G L E?;
//Dihedral:		D I H E D? R? A? L?;
Improper:		I M P R O? P? E? R?;

/* CHARMM: CONSTRAINTS - The Quartic Droplet Potential
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
//Cons:			C O N S T? R? A? I? N? T?;
Droplet:		D R O P L? E? T?;
//Force:		F O R C E?;
//Exponent:		E X P O N? E? N? T?;
NoMass:			N O M A S? S?;

/* CHARMM: CONSTRAINTS - How to fix atoms rigidly in place
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
//Cons:			C O N S T? R? A? I? N? T?;
Fix:			F I X;
Purg:			P U R G;
//Bond:			B O N D;
Thet:			T H E T;
Phi:			P H I;
Imph:			I M P H;

/* CHARMM: CONSTRAINTS - Constrain centers of mass for selected atoms
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
//Cons:			C O N S T? R? A? I? N? T?;
Hmcm:			H M C M;
//Force:		F O R C E?;
//Weighting:		W E I G H? T? I? N? G?;

// reference-spec
RefX:			R E F X;
RefY:			R E F Y;
RefZ:			R E F Z;

/* CHARMM: CONSTRAINTS - Fixing bond lengths or angles during dynamics
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
Shake:			S H A K E?;
Off:			O F F;
NoReset:		N O R E S? E? T?;

// shake-opt
BonH:			B O N H;
//Main:			M A N I;
Tol:			T O L;
MxIter:			M X I T E? R?;
//Bond:			B O N D;
//Comp:			C O M P;
AngH:			A N G H;
Parameters:		P A R A M? E? T? E? R? S?;
ShkScale:		S H K S C? A? L? E?;
//Angl:			A N G L;

// fast-opt
Fast:			F A S T;
Water:			W A T E R?;
NoFast:			N O F A S? T?;

Noe:			N O E;

// noe_statement
Reset:			R E S E T?;
PNoe:			P N O E;

Assign:			A S S I G? N?;
KMin:			K M I N;
KMax:			K M A X;
RMin:			R M I N;
RMax:			R M A X;
FMax:			F M A X;
MinDist:		M I N D I S T;
RSwi:			R S W I;
SExp:			S E X P;
SumR:			S U M R;
TCon:			T C O N;
RExp:			R E X P;
CnoX:			C N O X;
CnoY:			C N O Y;
CnoZ:			C N O Z;

MPNoe:			M P N O E?;
INoe:			I N O E;
TnoX:			T N O X;
TnoY:			T N O Y;
TnoZ:			T N O Z;

NMPNoe:			N M P N O? E?;

Read:			R E A D;
Write:			W R I T E?;
Unit:			U N I T;

Print:			P R I N T?;
Anal:			A N A L;
Cut:			C U T;

Scale:			S C A L E?;
Temperature:		T E M P R? A? T? U? R? E?;

/* CHARMM: CONSTRAINTS - Restrained Distances
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
ResDistance:		R E S D I? S? T? A? N? C? E?;
//Reset:		R E S E T?;
//Scale:		S C A L E?;
KVal:			K V A L;
RVal:			R V A L;
EVal:			E V A L;
IVal:			I V A L;
Positive:		P O S I T? I? V? E?;
Negative:		N E G A T? I? V? E?;

/* CHARMM: CONSTRAINTS - External Forces
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
Pull:			P U L L;
//Force:		F O R C E?;
XDir:			X D I R;
YDir:			Y D I R;
ZDir:			Z D I R;
//Period:		P E R I O? D?;
EField:			E F I E L? D?;
//Off:			O F F;
List:			L I S T;
Switch:			S W I T C? H?;
SForce:			S F O R C? E?;
//Weight:		W E I G H? T?;


/* CHAMM: CONSTRAINTS - RMSD Restraints
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
//Cons:			C O N S T? R? A? I? N? T?;
RMSD:			R M S D;
//Relative:		R E L A T? I? V? E?;
MaxN:			M A X N;
NPrt:			N P R T;
Show:			S H O W;
//Clear:		C L E A R?;

// orient-specs
//NoRotation:		N O R O T? A? T? I? O? N?;
//NoTranslation:	N O T R A? N? S? L? A? T? I? O? N?;

// force-const-spec
//Force:		F O R C E?;
//Mass:			M A S S;
Offset:			O F F S E? T?;
BOffset:		B O F F S? E? T?;

// coordinate-spec
//Main:			M A I N;
//Comp:			C O M P;

/* CHARMM: CONSTRAINTS - Rg/RMSD Restraint
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
RGyration:		R G Y R A? T? I? O? N?;
//Force:		F O R C E?;
Reference:		R E F E R? E? N? C? E?;
//RMSD:			R M S D;
//Comparison:		C O M P;
Orient:			O R I E N? T?;
Output:			O U T P U? T?;
NSave:			N S A V E?;
//Reset:		R E S E T?;

/* CHARMM: CONSTRAINTS - Distance Matrix Restraint
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
DMConstrain:		D M C O N? S? T? R? A? I? N?;
//Force:		F O R C E?;
//Reference:		R E F E R? E? N? C? E?;
//Output:		O U T P U? T?;
//NSave:		N S A V E?;
Cutoff:			C U T O F? F?;
NContact:		N C O N T? A? C? T?;
//Weight:		W E I G H? T?;

/* CHARMM: Atom selection
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
Selection:		S E L E C? T? I? O? N?;
//Show:			S H O W;
//End:			E N D;

// factor
Or_op:			'.' O R '.';
And_op:			'.' A N D '.';
Not_op:			'.' N O T '.';

Around:			'.' A R O U N D '.';
Subset:			'.' S U B S E T '.';
Bonded:			'.' B O N D E D '.';
ByRes:			'.' B Y R E S '.';
ByGroup:		'.' B Y G R O U P '.';

// token
SegIdentifier:		S E G I D?;
ISeg:			I S E G;
Residue:		R E S I D;
IRes:			I R E S;
Resname:		R E S N A? M? E?;
IGroup:			I G R O U? P?;
Type:			T Y P E;
Chemical:		C H E M I? C? A? L?;
Atom:			A T O M;
Property:		P R O P E? R? T? Y? -> pushMode(ATTR_MODE);
Point:			P O I N T?;
//Cut:			C U T;
//Periodic:		P E R I O? D? I? C?;
//ByNumber:		B Y N U M? B? E? R?;
Initial:		I N I T I? A? L?;
Lone:			L O N E;
Hydrogen:		H Y D R O? G? E? N?;
User:			U S E R;
Previous:		P R E V I? O? U? S?;
Recall:			R E C A L? L?;
All:			A L L;
NONE:			N O N E;

/* Numbers and Strings - Syntax
*/
Integer:		'-'? DECIMAL;
//Logical:		T R U E | F A L S E | O N | O F F;
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) (E ('+' | '-')? DECIMAL)?;
Double_quote_string:	'"' ~["\r\n]* '"';
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

COMMENT:		('#' | '!')+ -> mode(COMMENT_MODE);

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

/* Wildcard - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
fragment WILDCARD:	'*' | '%' | '#' | '+';

fragment ALPHA:		[A-Z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;
fragment POST_WC_CHAR:	DEC_DIGIT | '\'' | 'P';
fragment SYMBOL_NAME:	'@' START_CHAR+;

L_paren:		'(';
R_paren:		')';
Colon:			':';
Equ_op:			'.' E Q '.';
Lt_op:			'.' L T '.';
Gt_op:			'.' G T '.';
Leq_op:			'.' L E '.';
Geq_op:			'.' G E '.';
Neq_op:			'.' N E '.';
Aeq_op:			'.' A E '.';		// almost equal: diff<0.0001

Symbol_name:		SYMBOL_NAME;

SPACE:			[ \t\r\n]+ -> skip;
CONTINUE:		'-'+ SPACE -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+ | R E M A R K) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | ';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+ | R E M A R K) ~[\r\n]* -> channel(HIDDEN);
//SET_VARIABLE:		Set ([\r\n]*)? ~[\r\n]* ([\r\n]*)? End -> channel(HIDDEN);

mode VECTOR_EXPR_MODE;

Equ_op_VE:		'=';

Integer_VE:		Integer;
Real_VE:		Real;
Simple_name_VE:		SIMPLE_NAME;

SPACE_VE:		[ \t]+ -> skip;
RETURN_VE:		[\r\n]+ -> popMode;

mode COMMENT_MODE;

Any_name:		~[ \t\r\n]+;

SPACE_CM:		[ \t]+ -> skip;
RETURN_CM:		[\r\n]+ -> mode(DEFAULT_MODE);

mode ATTR_MODE; // Inside of Attribute tag

// Attribute properties
Abs:			A B S;
Attr_properties:	(X | Y | Z | W M A I N? | X C O M P? | Y C O M P? | Z C O M P? | W C O M P? | D X | D Y | D Z | E C O N T? | E P C O N? T? | M A S S | C H A R G? E? | C O N S T? R? A? I? | X R E F | Y R E F | Z R E F | F B E T A? | M O V E | T Y P E | I G N O R? E? | A S P V A? L? U? E? | V D W S U? R? F? A? | A L P H A? | E F F E C? T? | R A D I U? S? | R S C A L? E? | F D I M | F D C O N? S? | F D E P | S C A '1' | S C A '2' | S C A '3' | S C A '4' | S C A '5' | S C A '6' | S C A '7' | S C A '8' | S C A '9' | Z E R O | O N E);
Comparison_ops:		(Equ_op | Lt_op | Gt_op | Leq_op | Geq_op | Neq_op | Aeq_op) -> popMode;

SPACE_AP:		[ \t\r\n]+ -> skip;

