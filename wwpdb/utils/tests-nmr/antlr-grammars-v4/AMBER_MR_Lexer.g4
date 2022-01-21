/*
 AMBER MR (Magnetic Restraint) lexer grammar for ANTLR v4.
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

lexer grammar AMBER_MR_Lexer;

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

fragment IGR:		I G R;					// = Integer [ , Integer ]*
IGR1:			IGR '1';
IGR2:			IGR '2';
IGR3:			IGR '3';
IGR4:			IGR '4';
IGR5:			IGR '5';
IGR6:			IGR '6';
IGR7:			IGR '7';
IGR8:			IGR '8';

FXYZ:			F X Y Z;				// = One_or_Zero, One_or_Zero, One_or_Zero
OUTXYZ:			O U T X Y Z;				// = One_or_Zero

fragment GRNAM:		G R N A M;				// = Quoted_atom_name [ , Quoted_atom_name ]*
GRNAM1:			GRNAM '1';
GRNAM2:			GRNAM '2';
GRNAM3:			GRNAM '3';
GRNAM4:			GRNAM '4';
GRNAM5:			GRNAM '5';
GRNAM6:			GRNAM '6';
GRNAM7:			GRNAM '7';
GRNAM8:			GRNAM '8';

IR6:			I R '6';				// = One_or_Zero
IFNTYP:			I F N T Y P;				// = One_or_Zero

IXPK:			I X P K;				// = Integer
NXPK:			N X P K;				// = Integer

ICONSTR:		I C O N S T R;				// = Integer

One_or_Zero:		'1' | '0';				// IRESID = 0 for the IAT points to the atoms, IRESID = 1 for the the IAT points to the residues
								// IRSTYP = 0 for target values are used directly, IRSTYP = 1 for target values are relatively displacement from the initial coordinates
								// IALTD = 0 for the penalty energy continues to rise in case of large distance violations, IALTD = 1 for the penalty energy is flattened out in that case
								// IMULT = 0 for R2A->RK2A, R3A->RK3A change linearly, IMULT = 1 for R2A->RK2A, R3A->RK3A change multicatively
								// IR6 = 0 for center-of-mass averaging, IR6 = 1 for <r^-6>^(-1/6) averaging of all interactions
								// IFNTYP = 0 for no time-averaged restraints, IFNTYP = 1 for enabling time-averaged restraints

fragment DISTANCE_IDX:		'1' | '2';
fragment ANGLE_IDX:		'1' | '2' | '3';
fragment TORSION_IDX:		'1' | '2' | '3' | '4';
fragment GENDISTANCE2_IDX:	'1' | '2' | '3' | '4';
fragment PLANEPOINTANG_IDX:	'1' | '2' | '3' | '4' | '5';
fragment GENDISTANCE3_IDX:	'1' | '2' | '3' | '4' | '5' | '6';
fragment PLANEPLANEANG_IDX:	'1' | '2' | '3' | '4' | '5' | '6' | '7' | '8';
fragment GENDISTANCE4_IDX:	'1' | '2' | '3' | '4' | '5' | '6' | '7' | '8';

DistanceIFunctionCall:		RstIFunctionName L_paren DISTANCE_IDX R_paren;		// = Integer
AngleIFunctionCall:		RstIFunctionName L_paren ANGLE_IDX R_paren;		// = Integer
TorsionIFunctionCall:		RstIFunctionName L_paren TORSION_IDX R_paren;		// = Integer
PlanePointAngleIFunctionCall:	RstIFunctionName L_paren PLANEPOINTANG_IDX R_paren;	// = Integer
PlanePlaneAngleIFunctionCall:	RstIFunctionName L_paren PLANEPLANEANG_IDX R_paren;	// = Integer
GeneralDistance2IFunctionCall:	RstIFunctionName L_paren GENDISTANCE2_IDX R_paren;	// = Integer
GeneralDistance3IFunctionCall:	RstIFunctionName L_paren GENDISTANCE3_IDX R_paren;	// = Integer
GeneralDistance4IFunctionCall:	RstIFunctionName L_paren GENDISTANCE4_IDX R_paren;	// = Integer
RstIFunctionName:		IAT;

DISTANCE_IGR:			IGR1 | IGR2;
ANGLE_IGR:			IGR1 | IGR2 | IGR3;
TORSION_IGR:			IGR1 | IGR2 | IGR3 | IGR4;
GENDISTANCE2_IGR:		IGR1 | IGR2 | IGR3 | IGR4;
PLANEPOINTANG_IGR:		IGR1 | IGR2 | IGR3 | IGR4 | IGR5;
GENDISTANCE3_IGR:		IGR1 | IGR2 | IGR3 | IGR4 | IGR5 | IGR6;
PLANEPLANEANG_IGR:		IGR1 | IGR2 | IGR3 | IGR4 | IGR5 | IGR6 | IGR7 | IGR8;
GENDISTANCE4_IGR:		IGR1 | IGR2 | IGR3 | IGR4 | IGR5 | IGR6 | IGR7 | IGR8;

DistanceIGFunctionCall:		DISTANCE_IGR L_paren DISTANCE_IDX R_paren;		// = IntegerArrary
AngleIGFunctionCall:		ANGLE_IGR L_paren ANGLE_IDX R_paren;			// = IntegerArrary
TorsionIGFunctionCall:		TORSION_IGR L_paren TORSION_IDX R_paren;		// = IntegerArrary
PlanePointAngleIGFunctionCall:	PLANEPOINTANG_IGR L_paren PLANEPOINTANG_IDX R_paren;	// = IntegerArrary
PlanePlaneAngleIGFunctionCall:	PLANEPLANEANG_IGR L_paren PLANEPLANEANG_IDX R_paren;	// = IntegerArrary
GeneralDistance2IGFunctionCall:	GENDISTANCE2_IGR L_paren GENDISTANCE2_IDX R_paren;	// = IntegerArrary
GeneralDistance3IGFunctionCall:	GENDISTANCE3_IGR L_paren GENDISTANCE3_IDX R_paren;	// = IntegerArrary
GeneralDistance4IGFunctionCall:	GENDISTANCE4_IGR L_paren GENDISTANCE4_IDX R_paren;	// = IntegerArrary

DistanceRFunctionCall:		RstRFunctionName L_paren DISTANCE_IDX R_paren;		// = Real
AngleRFunctionCall:		RstRFunctionName L_paren ANGLE_IDX R_paren;		// = Real
TorsionRFunctionCall:		(RstRFunctionName | RJCOEF) L_paren TORSION_IDX R_paren;// = Real
PlanePointAngleRFunctionCall:	RstRFunctionName L_paren PLANEPOINTANG_IDX R_paren;	// = Real
PlanePlaneAngleRFunctionCall:	RstRFunctionName L_paren PLANEPLANEANG_IDX R_paren;	// = Real
GeneralDistance2RFunctionCall:	RstRFunctionName L_paren GENDISTANCE2_IDX R_paren;	// = Real
GeneralDistance3RFunctionCall:	RstRFunctionName L_paren GENDISTANCE3_IDX R_paren;	// = Real
GeneralDistance4RFunctionCall:	RstRFunctionName L_paren GENDISTANCE4_IDX R_paren;	// = Real
RstRFunctionName:		RSTWT;

DISTANCE_GRNAM:			GRNAM1 | GRNAM2;
ANGLE_GRNAM:			GRNAM1 | GRNAM2 | GRNAM3;
TORSION_GRNAM:			GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4;
GENDISTANCE2_GRNAM:		GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4;
PLANEPOINTANG_GRNAM:		GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5;
GENDISTANCE3_GRNAM:		GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5 | GRNAM6;
PLANEPLANEANG_GRNAM:		GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5 | GRNAM6 | GRNAM7 | GRNAM8;
GENDISTANCE4_GRNAM:		GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5 | GRNAM6 | GRNAM7 | GRNAM8;

DistanceNFunctionCall:		(ATNAM | DISTANCE_GRNAM) L_paren DISTANCE_IDX R_paren;		// = Quoted_atom_name
AngleNFunctionCall:		(ATNAM | ANGLE_GRNAM) L_paren ANGLE_IDX R_paren;		// = Quoted_atom_name
TorsionNFunctionCall:		(ATNAM | TORSION_GRNAM) L_paren TORSION_IDX R_paren;		// = Quoted_atom_name
PlanePointAngleNFunctionCall:	(ATNAM | PLANEPOINTANG_GRNAM) L_paren PLANEPOINTANG_IDX R_paren;// = Quoted_atom_name
PlanePlaneAngleNFunctionCall:	(ATNAM | PLANEPLANEANG_GRNAM) L_paren PLANEPLANEANG_IDX R_paren;// = Quoted_atom_name
GeneralDistance2NFunctionCall: 	(ATNAM | GENDISTANCE2_GRNAM) L_paren GENDISTANCE2_IDX R_paren;	// = Quoted_atom_name
GeneralDistance3NFunctionCall:	(ATNAM | GENDISTANCE3_GRNAM) L_paren GENDISTANCE3_IDX R_paren;	// = Quoted_atom_name
GeneralDistance4NFunctionCall:	(ATNAM | GENDISTANCE4_GRNAM) L_paren GENDISTANCE4_IDX R_paren;	// = Quoted_atom_name

fragment DISTANCE_F:		D I S T A N C E;
fragment ANGLE_F:		A N G L E;
fragment TORSION_F:		T O R S I O N;
fragment COORDINATE_F:		C O O R D I N A T E;
fragment PLANE_F:		P L A N E;
fragment COM_F:			C O M;

DistanceRstFunctionCall:	DISTANCE_F L_paren RestraintFuncExpr Comma? RestraintFuncExpr R_paren |
				DISTANCE_F L_brace RestraintFuncExpr Comma? RestraintFuncExpr R_brace |
				DISTANCE_F L_brakt RestraintFuncExpr Comma? RestraintFuncExpr R_brakt;

AngleRstFunctionCall:		ANGLE_F L_paren RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr R_paren |
				ANGLE_F L_brace RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr R_brace |
				ANGLE_F L_brakt RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr R_brakt;

TorsionRstFunctionCall:		TORSION_F L_paren RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr R_paren |
				TORSION_F L_brace RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr R_brace |
				TORSION_F L_brakt RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr R_brakt;

Coordinate2RstFunctionCall:	COORDINATE_F L_paren DistanceRstFunctionCall Comma? Real Comma? DistanceRstFunctionCall Comma? Real R_paren |
				COORDINATE_F L_brace DistanceRstFunctionCall Comma? Real Comma? DistanceRstFunctionCall Comma? Real R_brace |
				COORDINATE_F L_brakt DistanceRstFunctionCall Comma? Real Comma? DistanceRstFunctionCall Comma? Real R_brakt;

Coordinate3RstFunctionCall:	COORDINATE_F L_paren DistanceRstFunctionCall Comma? Real Comma? DistanceRstFunctionCall Comma? Real Comma?
								DistanceRstFunctionCall Comma? Real R_paren |
				COORDINATE_F L_brace DistanceRstFunctionCall Comma? Real Comma? DistanceRstFunctionCall Comma? Real Comma?
								DistanceRstFunctionCall Comma? Real R_brace |
				COORDINATE_F L_brakt DistanceRstFunctionCall Comma? Real Comma? DistanceRstFunctionCall Comma? Real Comma?
								DistanceRstFunctionCall Comma? Real R_brakt;

Coordinate4RstFunctionCall:	COORDINATE_F L_paren DistanceRstFunctionCall Comma? Real Comma? DistanceRstFunctionCall Comma? Real Comma?
								DistanceRstFunctionCall Comma? Real Comma? DistanceRstFunctionCall Comma? Real R_paren |
				COORDINATE_F L_brace DistanceRstFunctionCall Comma? Real Comma? DistanceRstFunctionCall Comma? Real Comma?
								DistanceRstFunctionCall Comma? Real Comma? DistanceRstFunctionCall Comma? Real R_brace |
				COORDINATE_F L_brakt DistanceRstFunctionCall Comma? Real Comma? DistanceRstFunctionCall Comma? Real Comma?
								DistanceRstFunctionCall Comma? Real Comma? DistanceRstFunctionCall Comma? Real R_brakt;

PlaneRstFunctionCall:		PLANE_F L_paren RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr R_paren |
				PLANE_F L_brace RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr R_brace |
				PLANE_F L_brakt RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr Comma? RestraintFuncExpr R_brakt;

ComRstFunctionCall:		COM_F L_paren RestraintFuncExpr (Comma? RestraintFuncExpr)* R_paren |
				COM_F L_brace RestraintFuncExpr (Comma? RestraintFuncExpr)* R_brace |
				COM_F L_brakt RestraintFuncExpr (Comma? RestraintFuncExpr)* R_brakt;

RestraintFuncExpr:	Integer |
			L_paren Integer R_paren |
			L_brace Integer R_brace |
			L_brakt Integer R_brakt |
			Res_atom_name |
			L_paren Res_atom_name R_paren |
			L_brace Res_atom_name R_brace |
			L_brakt Res_atom_name R_brakt |
			PlaneRstFunctionCall |
			ComRstFunctionCall;

/* Amber: NMR restraints - 29.2. NOESY volume restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
NOEEXP:			Ampersand N O E E X P;

NPEAK:			N P E A K;				// = IntegerArray
EMIX:			E M I X;				// = Real [ , Real ]*

NoeExpIGFunctionCall:	NoeExpIGFunctionName L_paren Integer Comma Integer R_paren;	// = IntegerArray
NoeExpIGFunctionName:	I H P | J H P;

NoeExpRGFunctionCall:	NoeExpRGFunctionName L_paren Integer Comma Integer R_paren;	// = RealArray
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

SftRGFunctionCall:	SftRGFunctionName L_paren Integer R_paren;			// = RealArray
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
//IPROT:		I P R O T;				// = Integer
//OBS:			O B S;					// = Real
//WT:			W T;					// = RealArray
TOLPRO:			T O L P R O;				// = RealArray
MLTPRO:			M L T P R O;				// = IntegerArray

PcshfIFunctionCall:	PcshfIFunctionName L_paren Integer R_paren;			// = Integer
PcshfIFunctionName:	IPROT;

PcshfIGFunctionCall:	PcshfIGFunctionName L_paren Integer R_paren;			// = IntegerArray
PcshfIGFunctionName:	MLTPRO;

PcshfRFunctionCall:	PcshfRFunctionName L_paren Integer R_paren;			// = Real
PcshfRFunctionName:	OPTPHI | OPTTET | OPTOMG | OPTA1 | OPTA2 | OBS;

PcshfRGFunctionCall:	PcshfRGFunctionName L_paren Integer R_paren;			// = RealArray
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

DWT:			D W T;					// = RealArray

DATASET:		D A T A S E T;				// = Integer
NUM_DATASET:		N U M '_' D A T A S E T;		// = Integer

S11:			S '11';					// = Real
S12:			S '12';					// = Real
S13:			S '13';					// = Real
S22:			S '22';					// = Real
S23:			S '23';					// = Real
SNN:			S11 | S12 | S13 | S22 | S23;

GIGJ:			G I G J;				// = RealArray
DIJ:			D I J;					// = Real
DCUT:			D C U T;				// = Real

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

CWT:			C W T;					// = RealArray

DATASETC:		D A T A S E T C;			// = Integer

FIELD:			F I E L D;				// = Real

SIGMA11:		S I G M A '11';				// = Real
SIGMA12:		S I G M A '12';				// = Real
SIGMA13:		S I G M A '13';				// = Real
SIGMA22:		S I G M A '22';				// = Real
SIGMA23:		S I G M A '23';				// = Real
SIGMANN:		SIGMA11 | SIGMA12 | SIGMA13 | SIGMA22 | SIGMA23;

CCUT:			C C U T;				// = Real

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
IntegerArray:		Integer (Comma Integer)* | MultiplicativeInteger;
RealArray:		Real (Comma Real)* | MultiplicativeReal;
fragment DEC_DOT_DEC:	DECIMAL '.' DECIMAL | DECIMAL '.' | '.' DECIMAL;
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

fragment ALPHA_NUM:	[A-Za-z0-9];
fragment START_CHAR:	[A-Za-z0-9_];
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.';
fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';

Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

Quoted_atom_name:	('\'' | '"')? Atom_name Atom_name* ('\'' | '"')?;
Res_atom_name:		':' Integer '@' Atom_name;		// ambmask format

L_paren:		'(';
R_paren:		')';
L_brace:		'{';
R_brace:		'}';
L_brakt:		'[';
R_brakt:		']';
Equ_op:			'=';

QUOT:			'"';
SPACE:			[ \t\r\n]+ -> skip;
COMMENT:		'{*' (COMMENT | .)*? '*}' -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!') ~[\r\n]* -> channel(HIDDEN);

