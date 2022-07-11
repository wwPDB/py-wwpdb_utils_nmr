/*
 CYANA MR (Magnetic Restraint) parser grammar for ANTLR v4.
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

parser grammar CyanaMRParser;

options { tokenVocab=CyanaMRLexer; }

cyana_mr:
	(
	distance_restraints |
	fixres_distance_restraints |
	fixresw_distance_restraints |
	fixresw2_distance_restraints |
	fixatm_distance_restraints |
	fixatmw_distance_restraints |
	fixatmw2_distance_restraints |
	torsion_angle_restraints |
	rdc_restraints |
	pcs_restraints |
	cco_restraints |
	ssbond_macro
	)*
	EOF;

/* CYANA 3.0 Reference Manual - Distance restraint file
 See also http://www.cyana.org/wiki/index.php/Distance_restraint_file
*/
distance_restraints:
	distance_restraint+;

distance_restraint:
	Integer Simple_name Simple_name
	Integer Simple_name Simple_name
	number number? number?
	number? number? number?;	// extensions for .cco file

/* CYANA 3.0 Reference Manual - Torsion angle restraint file
 See also http://www.cyana.org/wiki/index.php/Torsion_angle_restraint_file
*/
torsion_angle_restraints:
	torsion_angle_restraint+;

torsion_angle_restraint:
	Integer Simple_name Simple_name number number number? (Type Equ_op Integer)? Or?;

/* CYANA 3.0 Reference Manual - Residual dipolar coupling restraint file
 See also http://www.cyana.org/wiki/index.php/Residual_dipolar_coupling_restraint_file
*/
rdc_restraints:
	rdc_parameter+
	rdc_restraint+;

rdc_parameter:
	Integer Float Float Integer;

rdc_restraint:
	Integer Simple_name Simple_name
	Integer Simple_name Simple_name
	number number number Integer;

/* CYANA 3.0 Reference Manual - Pseudocontact shift restraint file
 See also http://www.cyana.org/wiki/index.php/Pseudocontact_shift_restraint_file
*/
pcs_restraints:
	pcs_parameter+
	pcs_restraint+;

pcs_parameter:
	Integer Float Float Integer;

pcs_restraint:
	Integer Simple_name Simple_name
	number number number Integer;

/* CYANA (undocumented) - ambiguous (fixed residue) distance restraint
 77 VAL #
        H  73  HIS  O  2.20
        H  73  HIS  C  3.50
        N  73  HIS  O  3.30
        N  73  HIS  C  4.60
*/
fixres_distance_restraints:
	fixres_distance_restraint+;

fixres_distance_restraint:
	Integer Simple_name
	(Simple_name Integer Simple_name Simple_name number)+;

/* with weight value or upper limit value */
fixresw_distance_restraints:
	fixresw_distance_restraint+;

fixresw_distance_restraint:
	Integer Simple_name
	(Simple_name Integer Simple_name Simple_name number number)+;

/* with lol, upl, weight value */
fixresw2_distance_restraints:
	fixresw2_distance_restraint+;

fixresw2_distance_restraint:
	Integer Simple_name
	(Simple_name Integer Simple_name Simple_name number number number)+;

/* CYANA (undocumented) - ambiguous (fixed atom) distance restraint
 77 VAL H  #
           73  HIS  O  2.20
           73  HIS  C  3.50
*/
fixatm_distance_restraints:
	fixatm_distance_restraint+;

fixatm_distance_restraint:
	Integer Simple_name Simple_name
	(Integer Simple_name Simple_name number)+;

/* with weight value or upper limit value */
fixatmw_distance_restraints:
	fixatmw_distance_restraint+;

fixatmw_distance_restraint:
	Integer Simple_name Simple_name
	(Integer Simple_name Simple_name number number)+;

/* with lol, upl, weight value */
fixatmw2_distance_restraints:
	fixatmw2_distance_restraint+;

fixatmw2_distance_restraint:
	Integer Simple_name Simple_name
	(Integer Simple_name Simple_name number number number)+;

/* CYANA (undocumented) - Scalar coupling constant restraint
*/
cco_restraints:
	cco_restraint+;

cco_restraint:
	Integer Simple_name Simple_name Simple_name number number? number?;

/* CYANA (macro) - ssbond
*/
ssbond_macro:
	Ssbond Ssbond_resids;

/* number expression in restrains */
number:	Float | Integer;

