/*
 DYNAMO/PALES/TALOS MR (Magnetic Restraint) parser grammar for ANTLR v4.
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

parser grammar DynamoMRParser;

options { tokenVocab=DynamoMRLexer; }

dynamo_mr:
	(
	sequence |
	distance_restraints |
	distance_restraints_sw_segid |
	distance_restraints_ew_segid |
	torsion_angle_restraints |
	torsion_angle_restraints_sw_segid |
	torsion_angle_restraints_ew_segid |
	rdc_restraints |
	rdc_restraints_sw_segid |
	rdc_restraints_ew_segid |
	coupling_restraints |
	coupling_restraints_sw_segid |
	coupling_restraints_ew_segid |
	talos_restraints
	)*
	EOF;

/* DYNAMO: Syntax
 See also https://spin.niddk.nih.gov/NMRPipe/dynamo/
*/

/* PALES: Syntax
 See also https://spin.niddk.nih.gov/bax/software/PALES/
*/

sequence:
	Data (First_resid Integer_DA | Sequence One_letter_code+) RETURN_DA;

distance_restraints:
	Vars Index Group
		Resid_I Resname_I Atomname_I
		Resid_J Resname_J Atomname_J
		D_Lo D_Hi FC W S RETURN_VA
	Format Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code Format_code RETURN_FO
	distance_restraint+;

distance_restraint:
	Integer Integer
	Integer Simple_name Simple_name
	Integer Simple_name Simple_name
	number number number number number;

distance_restraints_sw_segid:
	Vars Index Group
		Segname_I Resid_I Resname_I Atomname_I
		Segname_J Resid_J Resname_J Atomname_J
		D_Lo D_Hi FC W S RETURN_VA
	Format Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code Format_code RETURN_FO
	distance_restraint_sw_segid+;

distance_restraint_sw_segid:
	Integer Integer
	Simple_name Integer Simple_name Simple_name
	Simple_name Integer Simple_name Simple_name
	number number number number number;

distance_restraints_ew_segid:
	Vars Index Group
		Resid_I Resname_I Atomname_I Segname_I
		Resid_J Resname_J Atomname_J Segname_J
		D_Lo D_Hi FC W S RETURN_VA
	Format Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code Format_code RETURN_FO
	distance_restraint_ew_segid+;

distance_restraint_ew_segid:
	Integer Integer
	Integer Simple_name Simple_name Simple_name
	Integer Simple_name Simple_name Simple_name
	number number number number number;

torsion_angle_restraints:
	Vars Index
		Resid_I Resname_I Atomname_I
		Resid_J Resname_J Atomname_J
		Resid_K Resname_K Atomname_K
		Resid_L Resname_L Atomname_L
		Angle_Lo Angle_Hi FC RETURN_VA
	Format Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_FO
	torsion_angle_restraint+;

torsion_angle_restraint:
	Integer
		Integer Simple_name Simple_name
		Integer Simple_name Simple_name
		Integer Simple_name Simple_name
		Integer Simple_name Simple_name
		number number number;

torsion_angle_restraints_sw_segid:
	Vars Index
		Segname_I Resid_I Resname_I Atomname_I
		Segname_J Resid_J Resname_J Atomname_J
		Segname_K Resid_K Resname_K Atomname_K
		Segname_L Resid_L Resname_L Atomname_L
		Angle_Lo Angle_Hi FC RETURN_VA
	Format Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_FO
	torsion_angle_restraint_sw_segid+;

torsion_angle_restraint_sw_segid:
	Integer
		Simple_name Integer Simple_name Simple_name
		Simple_name Integer Simple_name Simple_name
		Simple_name Integer Simple_name Simple_name
		Simple_name Integer Simple_name Simple_name
		number number number;

torsion_angle_restraints_ew_segid:
	Vars Index
		Resid_I Resname_I Atomname_I Segname_I
		Resid_J Resname_J Atomname_J Segname_J
		Resid_K Resname_K Atomname_K Segname_K
		Resid_L Resname_L Atomname_L Segname_L
		Angle_Lo Angle_Hi FC RETURN_VA
	Format Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_FO
	torsion_angle_restraint_ew_segid+;

torsion_angle_restraint_ew_segid:
	Integer
		Integer Simple_name Simple_name Simple_name
		Integer Simple_name Simple_name Simple_name
		Integer Simple_name Simple_name Simple_name
		Integer Simple_name Simple_name Simple_name
		number number number;

rdc_restraints:
	Vars
		Resid_I Resname_I Atomname_I
		Resid_J Resname_J Atomname_J
		D DD W RETURN_VA
	Format
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_FO
	rdc_restraint+;

rdc_restraint:
	Integer Simple_name Simple_name
	Integer Simple_name Simple_name
	number number number;

rdc_restraints_sw_segid:
	Vars
		Segname_I Resid_I Resname_I Atomname_I
		Segname_J Resid_J Resname_J Atomname_J
		D DD W RETURN_VA
	Format
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_FO
	rdc_restraint_sw_segid+;

rdc_restraint_sw_segid:
	Simple_name Integer Simple_name Simple_name
	Simple_name Integer Simple_name Simple_name
	number number number;

rdc_restraints_ew_segid:
	Vars
		Resid_I Resname_I Atomname_I Segname_I
		Resid_J Resname_J Atomname_J Segname_J
		D DD W RETURN_VA
	Format
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_FO
	rdc_restraint_ew_segid+;

rdc_restraint_ew_segid:
	Integer Simple_name Simple_name Simple_name
	Integer Simple_name Simple_name Simple_name
	number number number;

coupling_restraints:
	Vars Index
		Resid_I Resname_I Atomname_I
		Resid_J Resname_J Atomname_J
		Resid_K Resname_K Atomname_K
		Resid_L Resname_L Atomname_L
		A B C
		Phase ObsJ FC RETURN_VA
	Format Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_FO
	coupling_restraint+;

coupling_restraint:
	Integer
		Integer Simple_name Simple_name
		Integer Simple_name Simple_name
		Integer Simple_name Simple_name
		Integer Simple_name Simple_name
		number number number
		number number number;

coupling_restraints_sw_segid:
	Vars Index
		Segname_I Resid_I Resname_I Atomname_I
		Segname_J Resid_J Resname_J Atomname_J
		Segname_K Resid_K Resname_K Atomname_K
		Segname_L Resid_L Resname_L Atomname_L
		A B C
		Phase ObsJ FC RETURN_VA
	Format Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_FO
	coupling_restraint_sw_segid+;

coupling_restraint_sw_segid:
	Integer
		Simple_name Integer Simple_name Simple_name
		Simple_name Integer Simple_name Simple_name
		Simple_name Integer Simple_name Simple_name
		Simple_name Integer Simple_name Simple_name
		number number number
		number number number;

coupling_restraints_ew_segid:
	Vars Index
		Resid_I Resname_I Atomname_I Segname_I
		Resid_J Resname_J Atomname_J Segname_J
		Resid_K Resname_K Atomname_K Segname_K
		Resid_L Resname_L Atomname_L Segname_L
		A B C
		Phase ObsJ FC RETURN_VA
	Format Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_FO
	coupling_restraint_ew_segid+;

coupling_restraint_ew_segid:
	Integer
		Integer Simple_name Simple_name Simple_name
		Integer Simple_name Simple_name Simple_name
		Integer Simple_name Simple_name Simple_name
		Integer Simple_name Simple_name Simple_name
		number number number
		number number number;

talos_restraints:
	Vars Resid Resname
		Phi Psi Dphi Dpsi Dist S2
		Count Cs_count Class RETURN_VA
	Format Format_code Format_code
		Format_code Format_code Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code RETURN_FO
	talos_restraint+;

talos_restraint:
	Integer Simple_name
		number number number number number number
		Integer Integer Simple_name;

/* number expression in restrains */
number:	Float | Integer;
