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

parser grammar CYANA_MR_Parser;

options { tokenVocab=CYANA_MR_Lexer; }

cyana_mr:
	distance_restraints*
	torsion_angle_restraints*
	rdc_restraints*
	pcs_restraints*
	EOF;

/* CYANA 3.0 Reference Manual - Distance restraint file
 See also http://www.cyana.org/wiki/index.php/Distance_restraint_file
*/
distance_restraints:
	distance_restraint+;

distance_restraint:
	Residue_number Residue_name Atom_name
	Residue_number Residue_name Atom_name
	Float;

/* CYANA 3.0 Reference Manual - Torsion angle restraint file
 See also http://www.cyana.org/wiki/index.php/Torsion_angle_restraint_file
*/
torsion_angle_restraints:
	torsion_angle_restraint+;

torsion_angle_restraint:
	Residue_number Residue_name Class_name Float Float;

/* CYANA 3.0 Reference Manual - Residual dipolar coupling restraint file
 See also http://www.cyana.org/wiki/index.php/Residual_dipolar_coupling_restraint_file
*/
rdc_restraints:
	rdc_parameter+
	rdc_restraint+;

rdc_parameter:
	Integer Float Float Integer;

rdc_restraint:
	Residue_number Residue_name Atom_name
	Residue_number Residue_name Atom_name
	Float Float Float Integer;

/* CYANA 3.0 Reference Manual - Pseudocontact shift restraint file
 See also http://www.cyana.org/wiki/index.php/Pseudocontact_shift_restraint_file
*/
pcs_restraints:
	pcs_parameter+
	pcs_restraint+;

pcs_parameter:
	Integer Float Float Integer;

pcs_restraint:
	Residue_number Residue_name Atom_name
	Float Float Float Integer;

