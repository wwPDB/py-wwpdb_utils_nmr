/*
 PALES (DYNAMO) MR (Magnetic Restraint) parser grammar for ANTLR v4.
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

parser grammar PalesMRParser;

options { tokenVocab=PalesMRLexer; }

pales_mr:
	(
	sequence |
	distance_restraints |
	distance_restraints_w_segid |
	torsion_angle_restraints |
	torsion_angle_restraints_w_segid |
	rdc_restraints |
	rdc_restraints_w_segid |
	coupling_restraints |
	coupling_restraints_w_segid
	)*
	EOF;

/* PALES: Syntax
 See also https://spin.niddk.nih.gov/bax/software/PALES/
*/

/* DYNAMO: Syntax
 See also https://spin.niddk.nih.gov/NMRPipe/dynamo/
*/

sequence:
	Data Sequence One_letter_code+ RETURN_D;

distance_restraints:
	Vars Index Group
		Resid_I Resname_I Atomname_I
		Resid_J Resname_J Atomname_J
		D_Lo D_Hi FC W S RETURN_V
	Format Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code Format_code RETURN_F
	distance_restraint+;

distance_restraint:
	Integer Integer
	Integer Simple_name Simple_name
	Integer Simple_name Simple_name
	number number number number number;

distance_restraints_w_segid:
	Vars Index Group
		Segname_I Resid_I Resname_I Atomname_I
		Segname_J Resid_J Resname_J Atomname_J
		D_Lo D_Hi FC W S RETURN_V
	Format Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code Format_code RETURN_F
	distance_restraint_w_segid+;

distance_restraint_w_segid:
	Integer Integer
	Simple_name Integer Simple_name Simple_name
	Simple_name Integer Simple_name Simple_name
	number number number number number;

torsion_angle_restraints:
	Vars Index
		Resid_I Resname_I Atomname_I
		Resid_J Resname_J Atomname_J
		Resid_K Resname_K Atomname_K
		Resid_L Resname_L Atomname_L
		Angle_Lo Angle_Hi FC RETURN_V
	Format Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_F
	torsion_angle_restraint+;

torsion_angle_restraint:
	Integer
		Integer Simple_name Simple_name
		Integer Simple_name Simple_name
		Integer Simple_name Simple_name
		Integer Simple_name Simple_name
		number number number;

torsion_angle_restraints_w_segid:
	Vars Index
		Segname_I Resid_I Resname_I Atomname_I
		Segname_J Resid_J Resname_J Atomname_J
		Segname_K Resid_K Resname_K Atomname_K
		Segname_L Resid_L Resname_L Atomname_L
		Angle_Lo Angle_Hi FC RETURN_V
	Format Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_F
	torsion_angle_restraint_w_segid+;

torsion_angle_restraint_w_segid:
	Integer
		Simple_name Integer Simple_name Simple_name
		Simple_name Integer Simple_name Simple_name
		Simple_name Integer Simple_name Simple_name
		Simple_name Integer Simple_name Simple_name
		number number number;

rdc_restraints:
	Vars
		Resid_I Resname_I Atomname_I
		Resid_J Resname_J Atomname_J
		D DD W RETURN_V
	Format
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_F
	rdc_restraint+;

rdc_restraint:
	Integer Simple_name Simple_name
	Integer Simple_name Simple_name
	number number number;

rdc_restraints_w_segid:
	Vars
		Segname_I Resid_I Resname_I Atomname_I
		Segname_J Resid_J Resname_J Atomname_J
		D DD W RETURN_V
	Format
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_F
	rdc_restraint_w_segid+;

rdc_restraint_w_segid:
	Simple_name Integer Simple_name Simple_name
	Simple_name Integer Simple_name Simple_name
	number number number;

coupling_restraints:
	Vars Index
		Resid_I Resname_I Atomname_I
		Resid_J Resname_J Atomname_J
		Resid_K Resname_K Atomname_K
		Resid_L Resname_L Atomname_L
		A B C
		Phase ObsJ FC RETURN_V
	Format Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_F
	coupling_restraint+;

coupling_restraint:
	Integer
		Integer Simple_name Simple_name
		Integer Simple_name Simple_name
		Integer Simple_name Simple_name
		Integer Simple_name Simple_name
		number number number
		number number number;

coupling_restraints_w_segid:
	Vars Index
		Segname_I Resid_I Resname_I Atomname_I
		Segname_J Resid_J Resname_J Atomname_J
		Segname_K Resid_K Resname_K Atomname_K
		Segname_L Resid_L Resname_L Atomname_L
		A B C
		Phase ObsJ FC RETURN_V
	Format Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_F
	coupling_restraint_w_segid+;

coupling_restraint_w_segid:
	Integer
		Simple_name Integer Simple_name Simple_name
		Simple_name Integer Simple_name Simple_name
		Simple_name Integer Simple_name Simple_name
		Simple_name Integer Simple_name Simple_name
		number number number
		number number number;

/* number expression in restrains */
number:	Float | Integer;

