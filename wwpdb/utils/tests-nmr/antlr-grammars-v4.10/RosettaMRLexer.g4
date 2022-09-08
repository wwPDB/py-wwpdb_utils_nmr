/*
 ROSETTA MR (Magnetic Restraint) lexer grammar for ANTLR v4.
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

lexer grammar RosettaMRLexer;

/* Rosetta Constraint File - Constraint Types - Single constraints
 See also https://www.rosettacommons.org/docs/latest/rosetta_basics/file_types/constraint-file
*/
AtomPair:		'AtomPair';		// Atom1_Name Atom1_ResNum Atom2_Name Atom2_ResNum Func_Type Func_Def
NamedAtomPair:		'NamedAtomPair';	// Atom1_Name Atom1_ResNum Atom2_Name Atom2_ResNum Func Type Func_Def (Errata: Func_Type is missing in the reference manual)
Angle:			'Angle';		// Atom1_Name Atom1_ResNum Atom2_Name Atom2_ResNum Atom3_Name Atom3_ResNum Func_Type Func_Def
NamedAngle:		'NamedAngle';		// Atom1_Name Atom1_ResNum Atom2_Name Atom2_ResNum Atom3_Name Atom3_ResNum Func_Type Func_Def
Dihedral:		'Dihedral';		// Atom1_Name Atom1_ResNum Atom2_Name Atom2_ResNum Atom3_Name Atom3_ResNum Atom4_Name Atom4_ResNum Func_Type Func_Def
DihedralPair:		'DihedralPair';		// Atom1_Name Atom1_ResNum Atom2_Name Atom2_ResNum Atom3_Name Atom3_ResNum Atom4_Name Atom4_ResNum\
						// Atom5_Name Atom5_ResNum Atom6_Name Atom6_ResNum Atom7_Name Atom7_ResNum Atom8_Name Atom8_ResNum Func_Type Func_Def
CoordinateConstraint:	'CoordinateConstraint';	// Atom1_Name Atom1_ResNum[Atom1_ChainID] Atom2_Name Atom2_ResNum[Atom2_ChainID]\
						// Atom1_target_X_coordinate Atom1_target_Y_coordinate Atom1_target_Z_coordinate Func_Type Func_Def
LocalCoordinateConstraint:
		'LocalCoordinateConstraint';	// Atom1_Name Atom1_ResNum Atom2_Name Atom3_Name Atom4_Name Atom234_ResNum\
						// Atom1_target_X_coordinate Atom1_target_Y_coordinate Atom1_target_Z_coordinate Func_Type Func_Def
AmbiguousNMRDistance:	'AmbiguousNMRDistance';	// Atom1_Name Atom1_ResNum Atom2_Name Atom2_ResNum Func_Type Func_Def
SiteConstraint:		'SiteConstraint';	// Atom1_Name Atom1_ResNum Opposing_chain Func_Type Func_Def
SiteConstraintResidues:
		'SiteConstraintResidues';	// Atom1_ResNum Atom1_Name Res2 Res3 Func_Type Func_Def (Atom1_resnum and Atom1_Name are swapped in the reference manual?)
MinResidueAtomicDistance:
		'MinResidueAtomicDistance';	// res1 res2 dist
BigBin:			'BigBin';		// res_number bin_char sdev

/* Rosetta Constraint File - Constraint Types - Nested constraints
 See also https://www.rosettacommons.org/docs/latest/rosetta_basics/file_types/constraint-file
*/
MultiConstraint:	'MultiConstraint';	// Constraint_Type1 Constraint_Def1 [Constraint_Type2 Constraint_Def2 [...]] END
AmbiguousConstraint:	'AmbiguousConstraint';	// Constraint_Type1 Constraint_Def1 [Constraint_Type2 Constraint_Def2 [...]] END
KofNConstraint:		'KofNConstraint';	// k Constraint_Type1 Constraint_Def1 [Constraint_Type2 Constraint_Def2 [...]] END (where k is integer)
END:			'END';

/* Rosetta Constraint File - Function Types
 See also https://www.rosettacommons.org/docs/latest/rosetta_basics/file_types/constraint-file
*/
CIRCULARHARMONIC:	'CIRCULARHARMONIC';	// x0 sd
PERIODICBOUNDED:	'PERIODICBOUNDED';	// period lb ub sd rswitch tag (rswith and tag is not optional, tag is not numeric)
OFFSETPERIODICBOUNDED:	'OFFSETPERIODICBOUNDED';// offset period lb ub sd rswitch tag (rswith and tag is not optional, tag is not numeric)
AMBERPERIODIC:		'AMBERPERIODIC';	// x0 n_period k
CHARMMPERIODIC:		'CHARMMPERIODIC';	// x0 n_period k
CIRCULARSIGMOIDAL:	'CIRCULARSIGMOIDAL';	// xC m o1 o2
CIRCULARSPLINE:		'CIRCULARSPLINE';	// weight [36 energy values]
HARMONIC:		'HARMONIC';		// x0 sd
FLAT_HARMONIC:		'FLAT_HARMONIC';	// x0 sd tol
BOUNDED:		'BOUNDED';		// lb ub sd rswitch tag (if tag is not numeric, rswitch will be omitted and set 0.5 by default)
GAUSSIANFUNC:		'GAUSSIANFUNC';		// mean sd tag WEIGHT weight
WEIGHT:			'WEIGHT';
SOGFUNC:		'SOGFUNC';		// n_funcs [mean1 sdev1 weight1 [mean2 sdev2 weight2 [...]]] (repeat n_funcs times)
MIXTUREFUNC:		'MIXTUREFUNC';		// anchor gaussian_param exp_param mixture_param bg_mean bg_sd
CONSTANTFUNC:		'CONSTANTFUNC';		// return_val
IDENTITY:		'IDENTITY';
SCALARWEIGHTEDFUNC:	'SCALARWEIGHTEDFUNC';	// weight Func_Type Func_Def
SUMFUNC:		'SUMFUNC';		// n_funcs Func_Type1 Func_Def1 [Func_Type2 Func_Def2 [...]] (repeat n_funcs times)
SPLINE:			'SPLINE';		// description histogram_file_path experimental_value weight bin_size |
						// description experimental_value weight bin_size |
						// description NONE experimental_value weight bin_size x_axis <val1> ...
NONE:			'NONE';
FADE:			'FADE';			// lb ub d wd [ wo ]
SIGMOID:		'SIGMOID';		// x0 m
SQUARE_WELL:		'SQUARE_WELL';		// x0 depth
SQUARE_WELL2:		'SQUARE_WELL2';		// x0 width depth [DEGREES]
DEGREES:		'DEGREES';
LINEAR_PENALTY:		'LINEAR_PENALTY';	// x0 depth width slope
KARPLUS:		'KARPLUS';		// A B C D x0 sd
SOEDINGFUNC:		'SOEDINGFUNC';		// w1 mean1 sd1 w2 mean2 sda
TOPOUT:			'TOPOUT';		// weight x0 limit
ETABLE:			'ETABLE';		// min max [many numbers]
USOG:			'USOG';			// num_gaussians mean1 sd1 mean2 sd2...
SOG:			'SOG';			// num_gaussians mean1 sd1 weight1 mean2 sd2 weight2...

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
//SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

COMMENT:		';'+ -> mode(COMMENT_MODE);

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;
//Atom_type:		ALPHA ATM_TYPE_CHAR*;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"' | '*' | '#' | ':';
fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment ATM_TYPE_CHAR:	ALPHA_NUM | '-' | '+';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t\r\n]+ -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

mode COMMENT_MODE;

Atom_pair_selection:	ALPHA+ DECIMAL SIMPLE_NAME '-' ALPHA+ DECIMAL SIMPLE_NAME;
Any_name:		~[ \t\r\n]+;

SPACE_CM:		[ \t]+ -> skip;
RETURN_CM:		[\r\n]+ -> mode(DEFAULT_MODE);

