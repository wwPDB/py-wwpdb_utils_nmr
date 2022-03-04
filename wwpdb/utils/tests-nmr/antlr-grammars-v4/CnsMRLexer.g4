/*
 CNS MR (Magnetic Restraint) lexer grammar for ANTLR v4.
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

lexer grammar CnsMRLexer;

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

End:			E N D;

/* CNS: Distance restraints - Syntax - noe
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Noe:			N O E;					// Noe { noe_statement } End

// noe_statement
Analysis:		A N A L Y? S? I? S;			// = Noe_analysis
Assign:			A S S I G? N?;				// selection selection Real Real Real [ Or_op selection selection ... ]
Asymptote:		A S Y M P? T? O? T? E?;			// Class_names Real
Averaging:		A V E R A? G? I? N? G?;			// Class_names Noe_avr_methods
Bgig:			B H I G;				// Class_names Real
Ceiling:		C E I L I? N? G?;			// = Real
Classification:		C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
CountViol:		C O U N T? V? I? O? L?;			// Class_name
Cv:			C V;					// = Integer
Den:			D E N;					// Initialize | ( Update Gamma = Real Kappa = Real )
Distribute:		D I S T R? I? B? U? T? E?;		// Class_name Class_name Real
Ensemble:		E N S E M? B? L? E?;			// Ensemble { ensemble_statement } End
Monomers:		M O N O M? E? R? S?;			// Class_names Integer
Ncount:			N C O U N? T?;				// Class_names Integer
Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
Outd:			O U T D;
Partition:		P A R T I? T? I? O? N?;			// = Integer
Potential:		P O T E N? T? I? A? L?;			// Class_names Noe_potential
Predict:		P R E D I? C? T?;			// { predict_statement } End
Print:			P R I N T?;
Raverage:		R A V E R? A? G? E?;			// Class_name Raverage_statement End
Threshold:		T H R E S? H? O? L? D?;			// = Real
Reset:			R E S E T?;
Rswitch:		R S W I T? C? H?;			// Class_names Real
Scale:			S C A L E?;				// Class_names Real
SoExponent:		S O E X P? O? N? E? N? T?;		// Class_names Real
SqConstant:		S Q C O O? N? S? T? A? N? T?;		// Class_names Real
SqExponent:		S Q E X P? O? N? E? N? T?;		// Class_names Real
SqOffset:		S Q O F F? S? E? T?;			// Class_names Real
Taverage:		T A V E R? A? G? E?;			// Class_name Taverage_statement End
Temperature:		T E M P E? R? A? T? U? R? E?;		// = Real

// NOE analysis
Noe_analysis:		C U R R E? N? T | T A V E R? A? G? E? | R A V E R? A? G? E?;

Initialize:		I N I T I? A? L? I? Z? E?;
Update:			U P D A T? E?;				// Gamma = Real Kappa = Real
Gamma:			G A M M A?;
Kappa:			K A P P A?;

// NOE averaging methods
Noe_avr_methods:	R '-6' | R '-3' | S U M | C E N T E? R?;

// NOE potential statement
Noe_potential:		B I H A R? M? O? N? I? C? | L O G N O? R? M? A? L? | S Q U A R? E? | S O F T S? Q? U? A? R? E? | S Y M M E? T? R? Y? | H I G H | '3' D P O;

// Predict statement
Cutoff:			C U T O F F;				// = Real
Cuton:			C U T O N;				// = Real
From:			F R O M;				// = selection
To:			T O;					// = selection

/* CNS: Dihedral angle restraints - Syntax - restranits/dihedral
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Restraints:		R E S T R? A? I? N? T? S?;		// Dihedral
Dihedral:		D I H E D? R? A? L?;			// Dihedral { dihedral_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection Real Real Real Integer
//Cv:			C V;					// = Integer
Nassign:		N A S S I? G? N?;			// = Integer
//Partition:		P A R T I? T? I? O? N?;			// = Integer
//Reset:		R E S E T?;
//Scale:		S C A L E?;				// = Real
Print_any:		'?';

/* CNS: Plane restraints - Syntax - restraints/plane
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
//Restraints:		R E S T R? A? I? N? T? S?;		// Plane
Plane:			P L A N E?;				// Plane { planar_statement } End

// planar_statement
Group:			G R O U P?;				// Group { group_statement } End
//Initialize:		I N I T I? A? L? I? Z? E?;
//Print_any:		'?';

// group_statement
Selection:		S E L E C? T? I? O? N?;			// = selection
Weight:			W E I G H? T?;				// = Real

/* CNS: Plane restraints - Syntax - restraints/harmonic
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
//Restraints:		R E S T R? A? I? N? T? S?;		// Harmonic
Harmonic:		P L A N E?;				// Harmonic { harmonic_statement } End

// harmonic_stetement
Exponent:		E X P O N? E? N? T?;			// = Integer
Normal:			N O R M A? L?;				// = vector_3d

/* CNS: Suscetibility anisotropy restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Sanisotropy:		S A N I S? O? T? R? O? P? Y?;		// Sanisotropy { sani_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real
ForceConstant:		F O R C E? C? O? N? S? T? A? N? T?;	// = Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
//Potential:		P O T E N? T? I? A? L?;			// = Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

// RDC potential statement
Rdc_potential:		S Q U A R? E? | H A R M O? N? I? C?;

/* CNS: Scalar J-coupling restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Coupling:		C O U P L? I? N? G?;			// Coupling { coupling_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection [ selection selection selection selection ] Real Real [ Real Real ]
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real Real
//Cv:			C V;					// = Integer
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real [ Real ]
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
//Partition:		P A R T I? T? I? O? N?;			// = Integer
//Potential:		P O T E N? T? I? A? L?;			// = Coupling_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class = Class_name )
//Reset:		R E S E T?;

Coupling_potential:	Rdc_potential | M U L T I? P? L? E?;

/* CNS: Carbon chemical shift restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Carbon:			C A R B O? N?;				// Carbon { carbon_shift_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
Expectation:		E X P E C? T? A? T? I? O? N?;		// Integer Integer Real Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// = Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
PhiStep:		P H I S T? E? P?;			// = Real
PsiStep:		P S I S T? E? P?;			// = Real
//Potential:		P O T E N? T? I? A? L?;			// = Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
Rcoil:			R C O I L?;				// selection Real Real
//Reset:		R E S E T?;
Zero:			Z E R O;

/* CNS: Proton chemical shift restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Proton:			P R O T O? N? S? H? I? F? T? S?;	// Proton { proton_shift_statement } End
Observed:		O B S E R? V? E? D?;			// selection [ selection ] Real [ Real ]
//Rcoil:		R C O I L?;				// selection Real
Anisotropy:		A N I S O? T? R? O? P? Y?;		// selection selection selection Co_or_Cn Logical? SC_or_BB
Amides:			A M I D E? S?;				// selection
Carbons:		C A R B O? N? S?;			// selection
Nitrogens:		N I T R O? G? E? N? S?;			// selection
Oxygens:		O X Y G E? N? S?;			// selection
RingAtoms:		R I N G A? T? O? M? S?;			// Ring_resname selection selection selection selection selection [ selection ]
AlphasAndAmides:	A L P H A? S? A? N? D? A? M? I? D? E? S?;	// selection
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
Error:			E R R O R?;				// Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real [ Real ]
//Potential:		P O T E N? T? I? A? L?;			// Coupling_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class = Class_name ) Rmsd_or_Not
//Reset:		R E S E T?;

//CO_or_CN:		C O | C N;
//SC_or_BB:		S C | B B;
//Ring_resname:		P H E | T Y R | H I S | T R P ('5' | '6') | A D E ('5' | '6') | G U A ('5' | '6') | T H Y | C Y T | U R A;
//Rmsd_or_Not:		R M S D | N O R M S? D?;

/* CNS: Conformation database restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Conformation:		C O N F O? R? M? A? T? I? O? N?;	// Conformation { conformation_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection [ selection selection selection selection ] [ selection selection selection selection ] [ selection selection selection selection ]
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
Compressed:		C O M P R? E? S? S? E? D?;
//Expectation:		E X P E C? T? A? T? I? O? N?;		// Integer [ Integer ] [ Integer ] [ Integer ] Real
//Error:		E R R O R?;				// = Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// = Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
Phase:			P H A S E?;				// Integer Integer Integer [ Integer Integer Integer ] (Integer Integer Integer ] (Integer Integer Integer ]
//Potential:		P O T E N? T? I? A? L?;			// = Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class = Class_name )
//Reset:		R E S E T?;
Size:			S I Z E;				// Dimensions Integer [ Integer ] [ Integer ] [ Integer ]
//Zero:			Z E R O;

Dimensions:		O N E D | T W O D | T H R E E D | F O U R D;

/* CNS: Diffusion anisotropy restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Danisotropy:		D A N I S? O? T? R? O? P? Y?;		// Danisotropy { diffusion_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// = Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
//Potential:		P O T E N? T? I? A? L?;			// = Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

/* CNS: One-bond coupling restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
OneBond:		O N E B O? N? D?;			// OneBond { one_bond_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real Real Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// = Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
//Potential:		P O T E N? T? I? A? L?;			// = Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

/* CNS: Angle database restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
AngleDb:		A N G L E? D? A? T? A? B? A? S? E?;	// AngleDb { bond_angle_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection selection selection selection selection selection [ selection ]
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
DerivFlag:		D E R I V? F? L? A? G?;			// On_or_Off
//Expectation:		E X P E C? T? A? T? I? O? N?;		// Integer Integer Real
//Error:		E R R O R?;				// = Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// = Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
//Potential:		P O T E N? T? I? A? L?;			// = Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class = Class_name )
//Reset:		R E S E T?;
//Size:			S I Z E;				// Angle_dihedral Integer Integer
//Zero:			Z E R O;

//On_or_Off:		O N | O F F;
Angle_dihedral:		A N G L E? | D I H E D? R? A? L?;

/* Atom selection - Syntax - identity/atom-selection
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
All:			A L L;
Around:			A R O U N? D?;				// Real (factor as subject)
Atom:			A T O M;				// Segment_names Residue_numbers Atom_names
Attribute:		A T T R I? B? U? T? E?
			-> pushMode(ATTR_MODE);			// Abs? Attr_property Comparison_ops Real
BondedTo:		B O N D E? D? T? O?;			// factor
ByGroup:		B Y G R O? U? P?;			// factor
ByRes:			B Y R E S?;				// factor
Chemical:		C H E M I? C? A? L?;			// Atom_types | Atom_type [ : Atom_type ]
Fbox:			F B O X;				// real real real real real real
Hydrogen:		H Y D R O? G? E? N?;
Id:			I D;					// Integer
Known:			K N O W N?;
Name:			N A M E;				// Atom_names | Atom_name [ : Atom_name ]
NONE:			N O N E;
//Not_op:		N O T;					// factor
Point:			P O I N T?;				// vector_3d cut Real
Cut:			C U T;
Previous:		P R E V I? O? U? S?;
Pseudo:			P S E U D? O?;
Residue:		R E S I D? U? E?;			// Residue_numbers | Residue_number [ : Residue_number ]
Resname:		R E S N A? M? E?;			// Residue_names | Residue_name [ : Residue_name ]
Saround:		S A R O U? N? D?;			// Real (factor as subject)
SegIdentifier:		S E G I D? E? N? T? I? F? I? E? R?;	// Segment_names | Segment_name [ : Segment_name ]
Sfbox:			S F B O X;				// real real real real real real
Store_1:		S T O R E '1';
Store_2:		S T O R E '2';
Store_3:		S T O R E '3';
Store_4:		S T O R E '4';
Store_5:		S T O R E '5';
Store_6:		S T O R E '6';
Store_7:		S T O R E '7';
Store_8:		S T O R E '8';
Store_9:		S T O R E '9';
Tag:			T A G;

/* Three-dimentional vectors - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Tail:			T A I L;
Head:			H E A D;

// Logical operations
Or_op:			O R;
And_op:			A N D;
Not_op:			N O T;

/* Numbers and Strings - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Comma:			',';
Complex:		L_paren Real Comma Real R_paren;
Integer:		('+' | '-')? DECIMAL;
Logical:		'TRUE' | 'FALSE' | 'ON' | 'OFF';
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) (E ('+' | '-')? DECIMAL)?;
Double_quote_string:	'"' ~'"'+ '"';
fragment DEC_DOT_DEC:	DECIMAL '.' DECIMAL | DECIMAL '.' | '.' DECIMAL;
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

Simple_name:		SIMPLE_NAME;
Simple_names:		WILDCARD | WILDCARD? SIMPLE_NAME WILDCARD;
Integers:		WILDCARD | WILDCARD? Integer WILDCARD;
//Class_name:		SIMPLE_NAME;
//Class_names:		WILDCARD | WILDCARD? SIMPLE_NAME WILDCARD;
//Segment_name:		SIMPLE_NAME;
//Segment_names:	WILDCARD | WILDCARD? SIMPLE_NAME WILDCARD;
//Residue_number:	Integer;
//Residue_numbers:	WILDCARD | WILDCARD? Residue_number WILDCARD;
//Residue_name:		SIMPLE_NAME;
//Residue_names:	WILDCARD | WILDCARD? SIMPLE_NAME WILDCARD;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;
//Atom_names:		WILDCARD | WILDCARD? Atom_name WILDCARD;
//Atom_type:		ALPHA ATM_TYPE_CHAR*;
//Atom_types:		WILDCARD | WILDCARD? Atom_type WILDCARD;

/* Wildcard - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
fragment WILDCARD:	'*' | '%' | '#' | '+';

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.';
fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment ATM_TYPE_CHAR:	ALPHA_NUM | '-' | '+';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

L_paren:		'(';
R_paren:		')';
Colon:			':';
Equ_op:			'=';
Lt_op:			'<';
Gt_op:			'>';
Leq_op:			'<=';
Geq_op:			'>=';
Neq_op:			'#';

SPACE:			[ \t\r\n]+ -> skip;
COMMENT:		'{*' (COMMENT | .)*? '*}' -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!') ~[\r\n]* -> channel(HIDDEN);

mode ATTR_MODE; // Inside of Attribute tag

// Attribute properties
Abs:			A B S;
Attr_properties:	(B | B C O M P? | C H A R G? E? | D X | D Y | D Z | F B E T A? | H A R M | M A S S | Q | Q C O M P? | R E F X | R E F Y | R E F Z | R M S D | V X | V Y | V Z | X | X C O M P? | Y | Y C O M P? | Z | Z C O M P? | S C A T T E R '_' A '1' | S C A T T E R '_' A '2' | S C A T T E R '_' A '3' | S C A T T E R '_' A '4' | S C A T T E R '_' B '1' | S C A T T E R '_' B '2' | S C A T T E R '_' B '3' | S C A T T E R '_' B '4' | S C A T T E R '_' C | S C A T T E R '_' F P | S C A T T E R '_' F D P);
Comparison_ops:		(Equ_op | Lt_op | Gt_op | Leq_op | Geq_op | Neq_op)
			-> popMode;

WS:			[ \t\r\n]+ -> skip;

