/*
 NMRPIPE CS (Assigned chemical shift) parser grammar for ANTLR v4.
 Copyright 2025 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

parser grammar NmrPipeCSParser;

options { tokenVocab=NmrPipeCSLexer; }

nmrpipe_cs:
	(
	sequence |
	chemical_shifts |
	chemical_shifts_sw_segid |
	chemical_shifts_ew_segid
	)*
	EOF;

/* NmrPipe: Syntax
 See also https://spin.niddk.nih.gov/NMRPipe/
*/

sequence:
	Data
		(
		First_resid Integer_DA RETURN_DA |
		Sequence One_letter_code+ RETURN_SQ |
		Db_name Simple_name_DA RETURN_DA |
		Tab_name Simple_name_DA* RETURN_DA |
		Tab_id Integer_DA RETURN_DA
		);

chemical_shifts:
	Vars Resid Resname Atomname Shift RETURN_VA
	Format Format_code Format_code Format_code Format_code RETURN_FO
	chemical_shift+;

chemical_shift:
	Integer Simple_name Simple_name number;

chemical_shifts_sw_segid:
	Vars Segname Resid Resname Atomname Shift RETURN_VA
	Format Format_code Format_code Format_code Format_code Format_code RETURN_FO
	chemical_shift_sw_segid+;

chemical_shift_sw_segid:
	Simple_name Integer Simple_name Simple_name number;

chemical_shifts_ew_segid:
	Vars Resid Resname Atomname Segname Shift RETURN_VA
	Format Format_code Format_code Format_code Format_code Format_code RETURN_FO
	chemical_shift_ew_segid+;

chemical_shift_ew_segid:
	Integer Simple_name Simple_name Simple_name number;

/* number expression in restrains */
number:	Float | Float_DecimalComma | Integer;

