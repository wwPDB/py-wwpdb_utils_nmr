/*
 GROMACS PT (Parameter Topology) lexer grammar for ANTLR v4.
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

lexer grammar GromacsPTLexer;

L_brkt:			'[';
R_brkt:			']';

/* GROMACS 2022.1 Referece Manual - Topology
 See also https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
Default:		'default';			// nbfunc comb-rule gen-pairs fudgeLJ fudgeQQ
Moleculetype:		'moleculetype';			// name nrexcl
Atomtypes:		'atomtypes';			// name at.num mass charge ptype V W
Pairtypes:		'pairtypes';			// i j func cs6 cs12
Bondtypes:		'bondtypes';			// i j func b0 kb
Angletypes:		'angletypes';			// i j k func th0 cth
Dihedraltypes:		'dihedraltypes';		// j k func (c{2} multi?) | c{6}
Constrainttypes:	'constrainttypes';		// i j func b0
Nonbond_params:		'nonbond_params';		// i j func V W | c{3}
Atoms:			'atoms';			// nr type resnr residu atom cgnr charge (mass) (typeB) (chargeB) (massB)
Bonds:			'bonds';			// ai aj funct c{0,2,3}
Pairs:			'pairs';			// ai aj funct c{2,5}
Pairs_nb:		'pairs_nb';			// ai aj funct qi, qj, V, W
Angles:			'angles';			// ai aj ak funct c{2,3,4,6}
Dihedrals:		'dihedrals';			// ai aj ak al funct c{2,3,5,6}
Exclusions:		'exclusions';			// ai a{1,}
Constraints:		'constraints';			// ai aj funct b0
Settles:		'settles';			// ai funct dsc_oh dsc_hh
Virtual_sites1:		'virtual_sites1';		// ai aj funct
Virtual_sites2:		'virtual_sites2';		// ai aj ak funct c
Virtual_sites3:		'virtual_sites3';		// ai aj ak aj funct c{2,3}
Virtual_sites4:		'virtual_sites4';		// ai aj ak aj al funct a b c
Virtual_sitesn:		'virtual_sitesn';		// ai funct a{1:} w?

System:			'system' -> pushMode(STR_ARRAY_MODE);	// any_string
Molecules:		'molecules';			// name number

/* GROMACS 2022.1 Referece Manual - Position restraints
 See also https://manual.gromacs.org/documentation/current/reference-manual/functions/restraints.html#position-restraints
          https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
Position_restraints:	'position_restraints';		// ai funct=1 kx ky kz
							// ai funct=2 g r k

Intermolecular_interactions:
			'inter' '-'? 'molecular' ('_' | '-') 'interactions';


Integer:		('+' | '-')? DECIMAL;
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) (('E' | 'e') ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;
//Atom_type:		ALPHA ATM_TYPE_CHAR*;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"' | '*' | '#';
fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment ATM_TYPE_CHAR:	ALPHA_NUM | '-' | '+';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t\r\n]+ -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* -> channel(HIDDEN);

mode STR_ARRAY_MODE;

R_brkt_AA:		']' ' '* [\r\n]+;

SECTION_COMMENT_AA:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_AA:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK') ~[\r\n]* [\r\n]+ -> channel(HIDDEN);

Simple_name_AA:		SIMPLE_NAME;

SPACE_AA:		[ \t]+ -> skip;
RETURN_AA:		[\r\n]+ -> popMode;

