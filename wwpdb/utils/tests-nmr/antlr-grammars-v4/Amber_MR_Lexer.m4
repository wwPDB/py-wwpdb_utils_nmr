/*
 Amber MR lexer grammar for ANTLR v4.
 Copyright 2021 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

lexer grammar Amber_MR_Lexer;

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

END:			(Ampersand E N D) | '/';

/* Amber: NMR restraints - 29.1 Distance, angle and torsional restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
RST:			Ampersand R S T;

IAT:			I A T;					// = Integer [ , Integer ] [ , Integer ] [ , Integer ] [ , Integer ] [ , Integer ] [ , Integer ] [ , Integer ]
RSTWT:			R S T W T;				// = Real [ , Real ] [ , Real ] [ , Real ]
RESTRAINT:		R E S T R A I N T;			// = " RestraintFunctionCall " [ , " RestraintFunctionCall " ]*
ATNAM:			A T N A M;				// = Quoted_atom_name [ , Quoted_atom_name ] [ , Quoted_atom_name ] [ , Quoted_atom_name ] [ , Quoted_atom_name ] [ , Quoted_atom_name ] [ , Quoted_atom_name ] [ , Quoted_atom_name ]
IRESID:			I R E S I D;				// = One_or_Zero
NSTEP1:			N S T E P '1';				// = Integer
NSTEP2:			N S T E P '2';				// = Integer
IRSTYP:			I R S T Y P;				// = One_or_Zero
IALTD:			I A L T D;				// = One_or_Zero
IFVARI:			I F V A R I;				// = Integer
NINC:			N I N C;				// = Integer
IMULT:			I M U L T;				// = One_or_Zero

R1:			R '1';					// = Real
R2:			R '2';					// = Real
R3:			R '3';					// = Real
R4:			R '4';					// = Real
RK2:			R K '2';				// = Real
RK3:			R K '3';				// = Real

R1A:			R '1' A;				// = Real
R2A:			R '2' A;				// = Real
R3A:			R '3' A;				// = Real
R4A:			R '4' A;				// = Real
RK2A:			R K '2' A;				// = Real
RK3A:			R K '3' A;				// = Real

R0:			R '0';					// = Real
K0:			K '0';					// = Real
R0A:			R '0' A;				// = Real
K0A:			K '0' A;				// = Real

RJCOEF:			R J C O E F;				// = Real, Real, Real

IGR:			I G R;
IGR1:			IGR '1';				// = Integer [ , Integer ]*
IGR2:			IGR '2';				// = Integer [ , Integer ]*
IGR3:			IGR '3';				// = Integer [ , Integer ]*
IGR4:			IGR '4';				// = Integer [ , Integer ]*
IGR5:			IGR '5';				// = Integer [ , Integer ]*
IGR6:			IGR '6';				// = Integer [ , Integer ]*
IGR7:			IGR '7';				// = Integer [ , Integer ]*
IGR8:			IGR '8';				// = Integer [ , Integer ]*

FXYZ:			F X Y Z;				// = One_or_Zero, One_or_Zero, One_or_Zero
OUTXYZ:			O U T X Y Z;				// = One_or_Zero

GRNAM:			G R N A M;
GRNAM1:			GRNAM '1';				// = Quoted_atom_name [ , Quoted_atom_name ]*
GRNAM2:			GRNAM '2';				// = Quoted_atom_name [ , Quoted_atom_name ]*
GRNAM3:			GRNAM '3';				// = Quoted_atom_name [ , Quoted_atom_name ]*
GRNAM4:			GRNAM '4';				// = Quoted_atom_name [ , Quoted_atom_name ]*
GRNAM5:			GRNAM '5';				// = Quoted_atom_name [ , Quoted_atom_name ]*
GRNAM6:			GRNAM '6';				// = Quoted_atom_name [ , Quoted_atom_name ]*
GRNAM7:			GRNAM '7';				// = Quoted_atom_name [ , Quoted_atom_name ]*
GRNAM8:			GRNAM '8';				// = Quoted_atom_name [ , Quoted_atom_name ]*

IR6:			I R '6';				// = One_or_Zero
IFNTYP:			I F N T Y P;				// = One_or_Zero

IXPK:			I X P K;				// = Integer
NXPK:			N X P K;				// = Integer

ICONSTR:		I C O N S T R;				// = Integer

One_or_Zero:		( '1' | '0' );				// IRESID = 0 for the IAT points to the atoms, IRESID = 1 for the the IAT points to the residues
								// IRSTYP = 0 for target values are used directly, IRSTYP = 1 for target values are relatively displacement from the initial coordinates
								// IALTD = 0 for the penalty energy continues to rise in case of large distance violations, IALTD = 1 for the penalty energy is flattened out in that case
								// IMULT = 0 for R2A->RK2A, R3A->RK3A change linearly, IMULT = 1 for R2A->RK2A, R3A->RK3A change multicatively
								// IR6 = 0 for center-of-mass averaging, IR6 = 1 for <r^-6>^(-1/6) averaging of all interactions
								// IFNTYP = 0 for no time-averaged restraints, IFNTYP = 1 for enabling time-averaged restraints

RstIFunctionCall:	RstIFunctionName L_paren Integer R_paren;			// = Integer
RstIFunctionName:	IAT;

RstIGFunctionCall:	RstIGFunctionName L_paren Integer R_paren;			// = Integer [ , Integer ]* | MulticativeInteger
RstIGFunctionName:	IGR;

RstRFunctionCall:	RstRFunctionName L_paren Integer R_paren;			// = Real
RstRFunctionName:	RSTWT | RJCOEF;

RstNFunctionCall:	RstNFunctionName L_paren Integer R_paren;			// = Quoted_atom_name
RstNFunctionName:	ATNAM | GRNAM;

RestraintFunctionCall:	RestraintFunctionName L_paren ( RestraintFuncExpr ( Comma? RestraintFuncExpr )* )? R_paren |
			RestraintFunctionName L_brace ( RestraintFuncExpr ( Comma? RestraintFuncExpr )* )? R_brace |
			RestraintFunctionName L_brakt ( RestraintFuncExpr ( Comma? RestraintFuncExpr )* )? R_brakt;

RestraintFunctionName:	D I S T A N C E | A N G L E | T O R S I O N | C O O R D I N A T E | P L A N E | C O M;

RestraintFuncExpr:	Integer |
			L_paren Integer R_paren |
			L_brace Integer R_brace |
			L_brakt Integer R_brakt |
			Res_atom_name |
			L_paren Res_atom_name R_paren |
			L_brace Res_atom_name R_brace |
			L_brakt Res_atom_name R_brakt |
			RestraintFunctionCall;

/* Amber: NMR restraints - 29.2. NOESY volume restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
NOEEXP:			Ampersand N O E E X P;

NPEAK:			N P E A K;				// = Integer [ , Integer ]* | MultiplicativeInteger
EMIX:			E M I X;				// = Real [ , Real ]*

NoeExpIGFunctionCall:	NoeExpIGFunctionName L_paren Integer Comma Integer R_paren;	// = Integer [ , Integer ]* | MultiplicativeInteger
NoeExpIGFunctionName:	I H P | J H P;

NoeExpRGFunctionCall:	NoeExpRGFunctionName L_paren Integer Comma Integer R_paren;	// = Real [ , Real ]* | MultiplicativeReal
NoeExpRGFunctionName:	A E X P | A R A N G E | A W T;

INVWT1:			I N V W T '1';				// = Real
INVWT2:			I N V W T '2';				// = Real

OMEGA:			O M E G A;				// = Real
TAUROT:			T A U R O T;				// = Real
TAUMET:			T A U M E T;				// = Real
ID2O:			I D '2' O;				// = One_or_Zero
OSCALE:			O S C A L E;				// = Real

/* Amber: NMR restraints - 29.3. Chemical shift restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
SHF:			Ampersand S H F;

NRING:			N R I N G;				// = Integer
NATR:			N A T R;				// = Integer [ , Integer ]*
IATR:			I A T R;
NAMR:			N A M R;				// = Quoted_atom_name [ , Quoted_atom_name ]*
STR:			S T R;					// = Real [ , Real ]*
IPROT:			I P R O T;				// = Integer [ , Integer ]*
OBS:			O B S;					// = Real [ , Real ]*
SHRANG:			S H R A N G;				// = Real [ , Real ]*
WT:			W T;					// = Real [ , Real ]*

SftIFunctionCall:	SftIFunctionName L_paren Integer R_paren;			// = Integer
SftIFunctionName:	NATR | IPROT;

SftIFunctionCall2:	SftIFunctionName2 L_paren Integer Comma Integer R_paren;	// = Integer
SftIFunctionName2:	IATR;

SftRFunctionCall:	SftRFunctionName L_paren Integer R_paren;			// = Real
SftRFunctionName:	OBS;

SftRGFunctionCall:	SftRGFunctionName L_paren Integer R_paren;			// = Real [ , Real ]* | MultiplicativeReal
SftRGFunctionName:	STR | SHRANG | WT;

SftNFunctionCall:	SftNFunctionName L_paren Integer R_paren;			// = Quoted_atom_name
SftNFunctionName:	NAMR;

NPROT:			N P R O T;				// = Integer
SHCUT:			S H C U T;				// = Real
NTER:			N T E R;				// = Integer
CTER:			C T E R;				// = Integer

/* Amber: NMR restraints - 29.4. Psuedocontact shift restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
PCSHF:			Ampersand P C S H F;

//NPROT:		N P R O T;				// = Integer
NME:			N M E;					// = Integer
NMPMC:			N M P M C;				// = Quoted_atom_name [ , Quoted_atom_name ]*

OPTPHI:			O P T P H I;				// = Real [ , Real ]*
OPTTET:			O P T T E T;				// = Real [ , Real ]*
OPTOMG:			O P T O M G;				// = Real [ , Real ]*
OPTA1:			O P T A '1';				// = Real [ , Real ]*
OPTA2:			O P T A '2';				// = Real [ , Real ]*
OPTKON:			O P T K O N;				// = Real
//IPROT:		I P R O T;				// = Integer [ , Integer ]*
//OBS:			O B S;					// = Real [ , Real ]*
//WT:			W T;					// = Real [ , Real ]* | MultiplicativeReal
TOLPRO:			T O L P R O;				// = Real [ , Real ]* | MultiplicativeReal
MLTPRO:			M L T P R O;				// = Integer [ , Integer ]*

PcshfIFunctionCall:	PcshfIFunctionName L_paren Integer R_paren;			// = Integer
PcshfIFunctionName:	IPROT;

PcshfIGFunctionCall:	PcshfIGFunctionName L_paren Integer R_paren;			// = Integer [ , Integer ]* | MultiplicativeInteger
PcshfIGFunctionName:	MLTPRO;

PcshfRFunctionCall:	PcshfRFunctionName L_paren Integer R_paren;			// = Real
PcshfRFunctionName:	OPTPHI | OPTTET | OPTOMG | OPTA1 | OPTA2 | OBS;

PcshfRGFunctionCall:	PcshfRGFunctionName L_paren Integer R_paren;			// = Real [ , Real ]* | MultiplicativeReal
PcshfRGFunctionName:	WT | TOLPRO;

/* Amber: NMR restraints - 29.5. Direct dipolar coupling restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
ALIGN:			Ampersand A L I G N;

NDIP:			N D I P;				// = Integer

ID:			I D;					// = Integer [ , Integer ]*
JD:			J D;					// = Integer [ , Integer ]*

DOBSL:			D O B S L;				// = Real [ , Real ]*
DOBSU:			D O B S U;				// = Real [ , Real ]*

DWT:			D W T;					// = Real [ , Real ]* | MultiplicativeReal

DATASET:		D A T A S E T;				// = Integer
NUM_DATASET:		N U M '_' D A T A S E T;		// = Integer

S11:			S '11';					// = Real [ , Real ]* | MultiplicativeReal
S12:			S '12';					// = Real [ , Real ]* | MultiplicativeReal
S13:			S '13';					// = Real [ , Real ]* | MultiplicativeReal
S22:			S '22';					// = Real [ , Real ]* | MultiplicativeReal
S23:			S '23';					// = Real [ , Real ]* | MultiplicativeReal

GIGJ:			G I G J;				// = Real [ , Real ]* | MultiplicativeReal
DIJ:			D I J;					// = Real [ , Real ]* | MultiplicativeReal
DCUT:			D C U T;				// = Real [ , Real ]* | MultiplicativeReal

FREEZEMOL:		F R E E Z E M O L;			// = Logical

AlignIFunctionCall:	AlignIFunctionName L_paren Integer R_paren;			// = Integer
AlignIFunctionName:	ID | JD;

AlignRFunctionCall:	AlignRFunctionName L_paren Integer R_paren;			// = Real
AlignRFunctionName:	DOBSL | DOBSU;

/* Amber: NMR restraints - 29.6. Residual CSA or pseudo-CSA restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
CSA:			Ampersand C S A;

NCSA:			N C S A;				// = Integer

ICSA:			I C S A;				// = Integer [ , Integer ]*
JCSA:			J C S A;				// = Integer [ , Integer ]*
KCSA:			K C S A;				// = Integer [ , Integer ]*

COBSL:			C O B S L;				// = Real [ , Real ]*
COBSU:			C O B S U;				// = Real [ , Real ]*

CWT:			C W T;					// = Real [ , Real ]* | MultiplicativeReal

DATASETC:		D A T A S E T C;			// = Integer

FIELD:			F I E L D;				// = Real [ , Real]* | MultiplicativeReal

SIGMA11:		S I G M A '11';				// = Real [ , Real ]* | MultiplicativeReal
SIGMA12:		S I G M A '12';				// = Real [ , Real ]* | MultiplicativeReal
SIGMA13:		S I G M A '13';				// = Real [ , Real ]* | MultiplicativeReal
SIGMA22:		S I G M A '22';				// = Real [ , Real ]* | MultiplicativeReal
SIGMA23:		S I G M A '23';				// = Real [ , Real ]* | MultiplicativeReal

CCUT:			C C U T;				// = Real [ , Real ]* | MultiplicativeReal

CsaIFunctionCall:	CsaIFunctionName L_paren Integer R_paren;			// = Integer
CsaIFunctionName:	ICSA | JCSA | KCSA;

CsaRFunctionCall:	CsaRFunctionName L_paren Integer R_paren;			// = Real
CsaRFunctionName:	COBSL | COBSU;

Comma:			',';
Ampersand:		'&';

Integer:		('+' | '-')? DECIMAL;
Real:			(DECIMAL | DEC_DOT_DEC) (E ('+' | '-')? DECIMAL)?;
Logical:		'.'? T R U E '.'? | '.'? F A L S E '.'?;
MultiplicativeInteger:	Integer '*' Integer;
MultiplicativeReal:	Integer '*' Real;
fragment DEC_DOT_DEC:	DECIMAL '.' DECIMAL | DECIMAL '.' | '.' DECIMAL;
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	[A-Za-z0-9];
fragment START_CHAR:	[A-Za-z0-9_];
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.';
fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment ATM_TYPE_CHAR:	ALPHA_NUM | '-' | '+';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

Class_name:		SIMPLE_NAME;
Segment_name:		SIMPLE_NAME;
Residue_number:		Integer;
Residue_name:		SIMPLE_NAME;
Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;
Atom_type:		ALPHA ATM_TYPE_CHAR*;

Quoted_atom_name:	('\'' | '"')? Atom_name Atom_name* ('\'' | '"')?;
Res_atom_name:		':' Integer '@' Atom_name;

L_paren:		'(';
R_paren:		')';
L_brace:		'{';
R_brace:		'}';
L_brakt:		'[';
R_brakt:		']';
Equ_op:			'=';
Lt_op:			'<';
Gt_op:			'>';
Leq_op:			'<=';
Geq_op:			'>=';

SPACE:			[ \t\r\n]+ -> skip;
COMMENT:		'{*' (COMMENT | .)*? '*}' -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!') ~[\r\n]* -> channel(HIDDEN);

