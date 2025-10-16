/*
 CYANA NOE (NOE Assignment) lexer grammar for ANTLR v4.10 or later
 Copyright 2024 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

lexer grammar CyanaNOALexer;

Peak:			'Peak';
From:			'from' -> pushMode(FILE_NAME_MODE);
Ppm_SC:			'ppm;';
Increased_from:		'increased from';
Decreased_from:		'decreased from';
Diagonal:		'diagonal';

Out_of:			'out of';
Assignments_used:	'assignments used' | 'assignment used';
Quality:		'quality';

Ok:			'OK';
Lone:			'lone';
Poor:			'poor';
Far:			'far';

Distance_range:		Float '-' Float;

Violated_in:		'Violated in';
Structures_by:		'structures by';

Average_quality:	'Average quality of peak assignments';
Average_number:		'Average number of used assignments';
Peaks_inc_upl:		'Peaks with increased upper limit';
Peaks_dec_upl:		'Peaks with decreased upper limit';

Protons_used_in_less:	'Protons used in less than 30% of expected peaks';
Peak_obs_dist:		'Peak observation distance';

Atom:			'Atom';
Residue:		'Residue';
Peaks:			'Peaks';
Shift:			'Shift';
Used:			'Used';
Expect:			'Expect';

Selected:		'selected';
Assigned:		'assigned';
Unassigned:		'unassigned';
Without_possibility:	'without assignment possibility';
With_viol_below:	'with violation below';
With_viol_between:	'with violation between';
With_viol_above:	'with violation above';
With_diagonal:		'with diagonal assignment';
And:			'and';

Cross_peaks:		'Cross peaks';
With_off_diagonal:	'with off-diagonal assignment';
With_unique:		'with unique assignment';
With_short_range:	'with short-range assignment';
With_medium_range:	'with medium-range assignment';
With_long_range:	'with long-range assignment';

Short_range_ex:		'|i-j|<=1';
Medium_range_ex:	'1<|i-j|<5';
Long_range_ex:		'|i-j|>=5';

L_paren:		'(';
R_paren:		')';
Colon:			':';
Period:			'.';
Comma:			',';
Equ_op:			'=';
Add_op:			'+';
Sub_op:			'-';
Div_op:			'/';

Angstrome:		Float ' A';

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

Numerical_report1:	Float Equ_op Integer (NR_EXT)? Comma?;
Numerical_report2:	Float Div_op Integer Equ_op Integer (NR_EXT)? Comma?;
Numerical_report3:	Integer Div_op Float Equ_op Integer (NR_EXT)? Comma?;
Numerical_report4:	'~' Integer Equ_op Integer (NR_EXT)? Comma?;
fragment NR_EXT:	'...(' Integer ')';

COMMENT:		('#' | '!')+ -> mode(COMMENT_MODE);

fragment ALPHA:		[A-Z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"' | '*' | '#' | '|';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

Simple_name:		SIMPLE_NAME;

SPACE:			[ \t\r\n]+ -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		('\\' | '&' | '<' | '>' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ~[\r\n]* -> channel(HIDDEN);

mode FILE_NAME_MODE;

File_name:		~[ \t\r\n]+ -> popMode;

SPACE_FN:		[ \t]+ -> skip;

mode COMMENT_MODE;

Any_name:		~[ \t\r\n]+;

SPACE_CM:		[ \t]+ -> skip;
RETURN_CM:		[\r\n]+ -> mode(DEFAULT_MODE);

