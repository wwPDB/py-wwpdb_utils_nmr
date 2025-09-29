/*
 CHARMM MR (Magnetic Restraint) lexer grammar for ANTLR v4.10 or later
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

options { caseInsensitive=true; }

Set:			'SET' -> pushMode(VECTOR_EXPR_MODE);
End:			'END';

/* CHARMM: CONSTRAINTS - Holding atoms in place
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
Cons:			'CONS' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'?;

Harmonic:		'HARM' 'O'? 'N'? 'I'? 'C'?;
Absolute:		'ABSO' 'L'? 'U'? 'T'? 'E'?;
Bestfit:		'BEST' 'F'? 'I'? 'T'?;
Relative:		'RELA' 'T'? 'I'? 'V'? 'E'?;
Clear:			'CLEA' 'R'?;

// force-const-spec
Force:			'FORC' 'E'?;
Mass:			'MASS';
Weight:			'WEIG' 'H'? 'T'? 'I'? 'N'? 'G'?;

// absolute-specs
Exponent:		'EXPO' 'N'? 'E'? 'N'? 'T'?;
XScale:			'XSCA' 'L'? 'E'?;
YScale:			'YSCA' 'L'? 'E'?;
ZScale:			'ZSCA' 'L'? 'E'?;

// bestfit-specs
NoRotation:		'NORO' 'T'? 'A'? 'T'? 'I'? 'O'? 'N'?;
NoTranslation:		'NOTR' 'A'? 'N'? 'S'? 'L'? 'A'? 'T'? 'I'? 'O'? 'N'?;

// coordinate-spec
Main:			'MAIN';
Comp:			'COMP';
Keep:			'KEEP';

/* CHARMM: CONSTRAINTS - Holding dihedrals near selected values
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
//Cons:			'CONS' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'?;

Dihedral:		'DIHE' 'D'? 'R'? 'A'? 'L'?;
ByNumber:		'BYNU' 'M'? 'B'? 'E'? 'R'?;
//Force:		'FORC' 'E'?;
Min:			'MIN';
Period:			'PERI' 'O'? 'D'?;
//Comp:			'COMP';
Width:			'WIDT' 'H'?;
//Main:			'MAIN';

ClDh:			'CLDH';

/* CHARMM: CONSTRAINTS - Holding Internal Coordinates near selected values
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
//Cons:			'CONS' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'?;

IC:			'IC';
Bond:			'BOND';
//Exponent:		'EXPO' 'N'? 'E'? 'N'? 'T'?;
Upper:			'UPPE' 'R'?;
Angle:			'ANGL' 'E'?;
//Dihedral:		'DIHE' 'D'? 'R'? 'A'? 'L'?;
Improper:		'IMPR' 'O'? 'P'? 'E'? 'R'?;

/* CHARMM: CONSTRAINTS - The Quartic Droplet Potential
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
//Cons:			'CONS' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'?;
Droplet:		'DROP' 'L'? 'E'? 'T'?;
//Force:		'FORC' 'E'?;
//Exponent:		'EXPO' 'N'? 'E'? 'N'? 'T'?;
NoMass:			'NOMA' 'S'? 'S'?;

/* CHARMM: CONSTRAINTS - How to fix atoms rigidly in place
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
//Cons:			'CONS' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'?;
Fix:			'FIX';
Purg:			'PURG';
//Bond:			'BOND';
Thet:			'THET';
Phi:			'PHI';
Imph:			'IMPH';

/* CHARMM: CONSTRAINTS - Constrain centers of mass for selected atoms
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
//Cons:			'CONS' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'?;
Hmcm:			'HMCM';
//Force:		'FORC' 'E'?;
//Weighting:		'WEIG' 'H'? 'T'? 'I'? 'N'? 'G'?;

// reference-spec
RefX:			'REFX';
RefY:			'REFY';
RefZ:			'REFZ';

/* CHARMM: CONSTRAINTS - Fixing bond lengths or angles during dynamics
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
Shake:			'SHAK' 'E'?;
Off:			'OFF';
NoReset:		'NORE' 'S'? 'E'? 'T'?;

// shake-opt
BonH:			'BONH';
//Main:			'MANI';
Tol:			'TOL';
MxIter:			'MXIT' 'E'? 'R'?;
//Bond:			'BOND';
//Comp:			'COMP';
AngH:			'ANGH';
Parameters:		'PARA' 'M'? 'E'? 'T'? 'E'? 'R'? 'S'?;
ShkScale:		'SHKS' 'C'? 'A'? 'L'? 'E'?;
//Angl:			'ANGL';

// fast-opt
Fast:			'FAST';
Water:			'WATE' 'R'?;
NoFast:			'NOFA' 'S'? 'T'?;

Noe:			'NOE';

// noe_statement
Reset:			'RESE' 'T'?;
PNoe:			'PNOE';

Assign:			'ASSI' 'G'? 'N'?;
KMin:			'KMIN';
KMax:			'KMAX';
RMin:			'RMIN';
RMax:			'RMAX';
FMax:			'FMAX';
MinDist:		'MINDIST';
RSwi:			'RSWI';
SExp:			'SEXP';
SumR:			'SUMR';
TCon:			'TCON';
RExp:			'REXP';
CnoX:			'CNOX';
CnoY:			'CNOY';
CnoZ:			'CNOZ';

MPNoe:			'MPNO' 'E'?;
INoe:			'INOE';
TnoX:			'TNOX';
TnoY:			'TNOY';
TnoZ:			'TNOZ';

NMPNoe:			'NMPN' 'O'? 'E'?;

Read:			'READ';
Write:			'WRIT' 'E'?;
Unit:			'UNIT';

Print:			'PRIN' 'T'?;
Anal:			'ANAL';
Cut:			'CUT';

Scale:			'SCAL' 'E'?;
Temperature:		'TEMP' 'R'? 'A'? 'T'? 'U'? 'R'? 'E'?;

/* CHARMM: CONSTRAINTS - Restrained Distances
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
ResDistance:		'RESD' 'I'? 'S'? 'T'? 'A'? 'N'? 'C'? 'E'?;
//Reset:		'RESE' 'T'?;
//Scale:		'SCAL' 'E'?;
KVal:			'KVAL';
RVal:			'RVAL';
EVal:			'EVAL';
IVal:			'IVAL';
Positive:		'POSI' 'T'? 'I'? 'V'? 'E'?;
Negative:		'NEGA' 'T'? 'I'? 'V'? 'E'?;

/* CHARMM: CONSTRAINTS - External Forces
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
Pull:			'PULL';
//Force:		'FORC' 'E'?;
XDir:			'XDIR';
YDir:			'YDIR';
ZDir:			'ZDIR';
//Period:		'PERI' 'O'? 'D'?;
EField:			'EFIE' 'L'? 'D'?;
//Off:			'OFF';
List:			'LIST';
Switch:			'SWIT' 'C'? 'H'?;
SForce:			'SFOR' 'C'? 'E'?;
//Weight:		'WEIG' 'H'? 'T'?;


/* CHAMM: CONSTRAINTS - RMSD Restraints
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
//Cons:			'CONS' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'?;
RMSD:			'RMSD';
//Relative:		'RELA' 'T'? 'I'? 'V'? 'E'?;
MaxN:			'MAXN';
NPrt:			'NPRT';
Show:			'SHOW';
//Clear:		'CLEA' 'R'?;

// orient-specs
//NoRotation:		'NORO' 'T'? 'A'? 'T'? 'I'? 'O'? 'N'?;
//NoTranslation:	'NOTR' 'A'? 'N'? 'S'? 'L'? 'A'? 'T'? 'I'? 'O'? 'N'?;

// force-const-spec
//Force:		'FORC' 'E'?;
//Mass:			'MASS';
Offset:			'OFFS' 'E'? 'T'?;
BOffset:		'BOFF' 'S'? 'E'? 'T'?;

// coordinate-spec
//Main:			'MAIN';
//Comp:			'COMP';

/* CHARMM: CONSTRAINTS - Rg/RMSD Restraint
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
RGyration:		'RGYR' 'A'? 'T'? 'I'? 'O'? 'N'?;
//Force:		'FORC' 'E'?;
Reference:		'REFE' 'R'? 'E'? 'N'? 'C'? 'E'?;
//RMSD:			'RMSD';
//Comparison:		'COMP';
Orient:			'ORIE' 'N'? 'T'?;
Output:			'OUTP' 'U'? 'T'?;
NSave:			'NSAV' 'E'?;
//Reset:		'RESE' 'T'?;

/* CHARMM: CONSTRAINTS - Distance Matrix Restraint
 See also https://charmm-gui.org/charmmdoc/cons.html
*/
DMConstrain:		'DMCO' 'N'? 'S'? 'T'? 'R'? 'A'? 'I'? 'N'?;
//Force:		'FORC' 'E'?;
//Reference:		'REFE' 'R'? 'E'? 'N'? 'C'? 'E'?;
//Output:		'OUTP' 'U'? 'T'?;
//NSave:		'NSAV' 'E'?;
Cutoff:			'CUTO' 'F'? 'F'?;
NContact:		'NCON' 'T'? 'A'? 'C'? 'T'?;
//Weight:		'WEIG' 'H'? 'T'?;

/* CHARMM: Atom selection
 See also https://charmm-gui.org/charmmdoc/select.html
*/
Selection:		'SELE' 'C'? 'T'? 'I'? 'O'? 'N'?;
//Show:			'SHOW';
//End:			'END';

// factor
Or_op:			'.OR.';
And_op:			'.AND.';
Not_op:			'.NOT.';

Around:			'.AROUND.';
Subset:			'.SUBSET.';
Bonded:			'.BONDED.';
ByRes:			'.BYRES.';
ByGroup:		'.BYGROUP.';

// token
SegIdentifier:		'SEGI' 'D'?;
ISeg:			'ISEG';
Residue:		'RESI' 'D';
IRes:			'IRES';
Resname:		'RESN' 'A'? 'M'? 'E'?;
IGroup:			'IGRO' 'U'? 'P'?;
Type:			'TYPE';
Chemical:		'CHEM' 'I'? 'C'? 'A'? 'L'?;
Atom:			'ATOM';
Property:		'PROP' 'E'? 'R'? 'T'? 'Y'? -> pushMode(ATTR_MODE);
Point:			'POIN' 'T'?;
//Cut:			'CUT';
//Periodic:		'PERI' 'O'? 'D'? 'I'? 'C'?;
//ByNumber:		'BYNU' 'M'? 'B'? 'E'? 'R'?;
Initial:		'INIT' 'I'? 'A'? 'L'?;
Lone:			'LONE';
Hydrogen:		'HYDR' 'O'? 'G'? 'E'? 'N'?;
User:			'USER';
Previous:		'PREV' 'I'? 'O'? 'U'? 'S'?;
Recall:			'RECA' 'L'? 'L'?;
All:			'ALL';
NONE:			'NONE';

/* Numbers and Strings - Syntax
*/
Integer:		'-'? DECIMAL;
//Logical:		'TRUE' | 'FALSE' | 'ON' | 'OFF';
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ('E' ('+' | '-')? DECIMAL)?;
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
fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;
fragment POST_WC_CHAR:	DEC_DIGIT | '\'' | 'P';
fragment SYMBOL_NAME:	'@' START_CHAR+;

L_paren:		'(';
R_paren:		')';
Colon:			':';
Equ_op:			'.EQ.';
Lt_op:			'.LT.';
Gt_op:			'.GT.';
Leq_op:			'.LE.';
Geq_op:			'.GE.';
Neq_op:			'.NE.';
Aeq_op:			'.AE.';		// almost equal: diff<0.0001

Symbol_name:		SYMBOL_NAME;

SPACE:			[ \t\r\n]+ -> skip;
CONTINUE:		'-'+ SPACE -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+ | 'REMARK' 'S'?) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		(';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+ | 'REMARK' 'S'?) ~[\r\n]* -> channel(HIDDEN);
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
Abs:			'ABS';
Attr_properties:	('X' | 'Y' | 'Z' | 'WMAI' 'N'? | 'XCOM' 'P'? | 'YCOM' 'P'? | 'ZCOM' 'P'? | 'WCOM' 'P'? | 'DX' | 'DY' | 'DZ' | 'ECON' 'T'? | 'EPCO' 'N'? 'T'? | 'MASS' | 'CHAR' 'G'? 'E'? | 'CONS' 'T'? 'R'? 'A'? 'I'? | 'XREF' | 'YREF' | 'ZREF' | 'FBET' 'A'? | 'MOVE' | 'TYPE' | 'IGNO' 'R'? 'E'? | 'ASPV' 'A'? 'L'? 'U'? 'E'? | 'VDWS' 'U'? 'R'? 'F'? 'A'? | 'ALPH' 'A'? | 'EFFE' 'C'? 'T'? | 'RADI' 'U'? 'S'? | 'RSCA' 'L'? 'E'? | 'FDIM' | 'FDCO' 'N'? 'S'? | 'FDEP' | 'SCA1' | 'SCA2' | 'SCA3' | 'SCA4' | 'SCA5' | 'SCA6' | 'SCA7' | 'SCA8' | 'SCA9' | 'ZERO' | 'ONE');
Comparison_ops:		(Equ_op | Lt_op | Gt_op | Leq_op | Geq_op | Neq_op | Aeq_op) -> popMode;

SPACE_AP:		[ \t\r\n]+ -> skip;

