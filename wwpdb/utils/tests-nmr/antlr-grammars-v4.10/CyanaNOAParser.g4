/*
 CYANA NOA (NOE Assignment) parser grammar for ANTLR v4.
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

parser grammar CyanaNOAParser;

options { tokenVocab=CyanaNOALexer; }

cyana_noa:
	(
	comment |
	noe_peaks |
	noe_stat |
	peak_stat
	)*
	EOF;

comment:
	COMMENT Any_name* (RETURN_CM | EOF);

noe_peaks:
	peak_header
	peak_quality
	noe_assignments?;

peak_header:
	Peak Integer From File_name L_paren Float Comma Float Ppm_SC
	(Angstrome | (Angstrome (Increased_from | Decreased_from) Angstrome) | Diagonal) R_paren Colon;

peak_quality:
	Integer Out_of Integer Assignments_used Comma Quality Equ_op Float Colon;

noe_assignments:
	noe_assignment+
	(Violated_in Integer Structures_by Angstrome Period)?;

noe_assignment:
	Simple_name Simple_name Integer (Add_op | Sub_op) Simple_name Simple_name Integer (Ok | Lone | Poor | Far) Integer
	numerical_report;

numerical_report:
	Integer (Integer | Sub_op) (Integer | Sub_op) Distance_range? extended_report?;

extended_report:
	(Numerical_report1 | Numerical_report2 | Numerical_report3 | Numerical_report4) extended_report?;

noe_stat:
	Average_quality Colon Float
	Average_number Colon Float
	Peaks_inc_upl Colon Integer
	Peaks_dec_upl Colon Integer

	Protons_used_in_less Colon
	Peak_obs_dist Colon Angstrome
	Atom Residue Shift Peaks Used Expect
	list_of_proton*;

list_of_proton:
	Simple_name Simple_name Integer Float Integer Integer Integer;

peak_stat:
	Peaks Colon
	Selected Colon Integer
	Assigned Colon Integer
	Unassigned Colon Integer
	(Without_possibility Colon Integer)?
	(With_viol_below Angstrome Colon Integer)?
	(With_viol_between Float And Angstrome Colon Integer)?
	(With_viol_above Angstrome Colon Integer)?
	With_diagonal Colon Integer

	Cross_peaks Colon
	With_off_diagonal Colon Integer
	With_unique Colon Integer
	With_short_range Short_range_ex Colon Integer
	With_medium_range Medium_range_ex Colon Integer
	With_long_range Long_range_ex Colon Integer;

