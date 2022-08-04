/*
 GROMACS MR (Magnetic Restraint) lexer grammar for ANTLR v4.
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

lexer grammar GromacsMRLexer;

L_brkt:			'[';
R_brkt:			']';

/* GROMACS 2022.1 Referece Manual - Distance restraints
 See also https://manual.gromacs.org/documentation/current/reference-manual/functions/restraints.html#distance-restraints
          https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
Distance_restraints:	'distance_restraints';		// ai aj funct=1 index type low up1 up2 kfac

/* GROMACS 2022.1 Referece Manual - Dihedral restraints
 See also https://manual.gromacs.org/documentation/current/reference-manual/functions/restraints.html#dihedral-restraints
          https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
Dihedral_restraints:	'dihedral_restraints';		// ai aj ak al funct=1 phi0 dphi kd

/* GROMACS 2022.1 Referece Manual - Orientation restraints
 See also https://manual.gromacs.org/documentation/current/reference-manual/functions/restraints.html#orientation-restraints
          https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
Orientation_restraints:	'orientation_restraints';	// ai aj funct=1 exp index alpha const obs weight

/* GROMACS 2022.1 Referece Manual - Angle restraints
 See also https://manual.gromacs.org/documentation/current/reference-manual/functions/restraints.html#angle-restraints
          https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
Angle_restraints:	'angle_restraints';		// ai aj ak al funct=1 theta0 kc mult

Angle_restraints_z:	'angle_restraints_z';		// ai aj funct=1 theta0 kc mult

/* GROMACS 2022.1 Referece Manual - Position restraints
 See also https://manual.gromacs.org/documentation/current/reference-manual/functions/restraints.html#position-restraints
          https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
Position_restraints:	'position_restraints';		// ai funct=1 kx ky kz
							// ai funct=2 g r k

Intermolecular_interactions:
			'inter' '-'? 'molecular' ('_' | '-') 'interactions';

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
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

