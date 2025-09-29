/*
 NmrPipe PK (Spectral peak list) parser grammar for ANTLR v4.
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

parser grammar NmrPipePKParser;

options { tokenVocab=NmrPipePKLexer; }

nmrpipe_pk:
	RETURN?
	(
	data_label |
	peak_list_2d |
	peak_list_3d |
	peak_list_4d |
	pipp_label |
	pipp_peak_list_2d |
	pipp_peak_list_3d |
	pipp_peak_list_4d |
	pipp_row_peak_list_2d |
	pipp_row_peak_list_3d |
	pipp_row_peak_list_4d |
	RETURN
	)*
	EOF;

/* NmrPipe: Syntax
 See also https://spin.niddk.nih.gov/NMRPipe/
*/

data_label:
	Data (X_axis_DA | Y_axis_DA | Z_axis_DA | A_axis_DA)
	Simple_name_DA Integer_DA Integer_DA
	Ppm_value_DA Ppm_value_DA RETURN_DA;

peak_list_2d:
	Vars Index
		X_axis Y_axis
		Dx Dy
		X_ppm Y_ppm
		X_hz Y_hz
		Xw Yw
		Xw_hz Yw_hz
		X1 X3 Y1 Y3
		Height DHeight Vol
		Pchi2 Type Ass?
		ClustId Memcnt Trouble? RETURN_VA
	Format Format_code
		Format_code Format_code
		Format_code Format_code
		Format_code Format_code
		Format_code Format_code
		Format_code Format_code
		Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code?
		Format_code Format_code Format_code? RETURN_FO
	(Null_value Any_name_NV RETURN_NV)?
	(Null_string Any_name_NS RETURN_NS)?
	peak_2d+;

peak_2d:
	Integer
	number number
	number number
	number number
	number number
	number number
	number number
	Integer Integer Integer Integer
	number number number
	number Integer Any_name?
	Integer Integer Integer? (RETURN | EOF);

peak_list_3d:
	Vars Index
		X_axis Y_axis Z_axis
		Dx Dy Dz
		X_ppm Y_ppm Z_ppm
		X_hz Y_hz Z_hz
		Xw Yw Zw
		Xw_hz Yw_hz Zw_hz
		X1 X3 Y1 Y3 Z1 Z3
		Height DHeight Vol
		Pchi2 Type Ass?
		ClustId Memcnt Trouble? RETURN_VA
	Format Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code?
		Format_code Format_code Format_code? RETURN_FO
	(Null_value Any_name_NV RETURN_NV)?
	(Null_string Any_name_NS RETURN_NS)?
	peak_3d+;

peak_3d:
	Integer
	number number number
	number number number
	number number number
	number number number
	number number number
	number number number
	Integer Integer Integer Integer Integer Integer
	number number number
	number Integer Any_name?
	Integer Integer Integer? (RETURN | EOF);

peak_list_4d:
	Vars Index
		X_axis Y_axis Z_axis A_axis
		Dx Dy Dz Dz
		X_ppm Y_ppm Z_ppm A_ppm
		X_hz Y_hz Z_hz A_hz
		Xw Yw Zw Aw
		Xw_hz Yw_hz Zw_hz Aw_hz
		X1 X3 Y1 Y3 Z1 Z3 A1 A3
		Height DHeight Vol
		Pchi2 Type Ass?
		ClustId Memcnt Trouble? RETURN_VA
	Format Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code?
		Format_code Format_code Format_code? RETURN_FO
	(Null_value Any_name_NV RETURN_NV)?
	(Null_string Any_name_NS RETURN_NS)?
	peak_4d+;

peak_4d:
	Integer
	number number number number
	number number number number
	number number number number
	number number number number
	number number number number
	number number number number
	Integer Integer Integer Integer Integer Integer Integer Integer
	number number number
	number Integer Any_name?
	Integer Integer Integer? (RETURN | EOF);

/* pipp */

pipp_label:
	Data Dim_count_DA Integer_DA RETURN_DA
	pipp_axis+;

pipp_axis:
	Data (X_axis_DA | Y_axis_DA | Z_axis_DA | A_axis_DA) Integer_DA Float_DA Float_DA Float_DA (Ppm_DA | Hz_DA) Float_DA RETURN_DA;

pipp_peak_list_2d:
	Format Format_code+ RETURN_FO
	Vars PkID X Y Intensity (Assign | Assign1 Assign2)? RETURN_VA
	pipp_peak_2d+;

pipp_peak_2d:
	Integer number number number+ (RETURN | EOF);

pipp_peak_list_3d:
	Format Format_code+ RETURN_FO
	Vars PkID Sl_Z? X Y Z Intensity (Assign | Assign1 Assign2)? RETURN_VA
	pipp_peak_3d+;

pipp_peak_3d:
	Integer Integer? number number number number+ (RETURN | EOF);

pipp_peak_list_4d:
	Format Format_code+ RETURN_FO
	Vars PkID Sl_A? Sl_Z? X Y Z A Intensity (Assign | Assign1 Assign2)? RETURN_VA
	pipp_peak_4d+;

pipp_peak_4d:
	Integer Integer? Integer? number number number number number+ (RETURN | EOF);

pipp_row_peak_list_2d:
	pipp_row_peak_2d+;

pipp_row_peak_2d:
	L_paren Float_PR Comma Float_PR Semicolon
	Number_sign Integer_PR Semicolon
	(Assignments_PR | L_brkt Float_PR Comma Float_PR R_brkt)
	Caret Real_PR Semicolon
	Percent_sign Integer_PR Semicolon
	R_paren (RETURN_PR | EOF);

pipp_row_peak_list_3d:
	pipp_row_peak_3d+;

pipp_row_peak_3d:
	L_paren Float_PR Comma Float_PR Comma Float_PR Semicolon
	Number_sign Integer_PR Semicolon
	(Assignments_PR | L_brkt Float_PR Comma Float_PR Comma Float_PR R_brkt)
	Caret Real_PR Semicolon
	Percent_sign Integer_PR Semicolon
	R_paren (RETURN_PR | EOF);

pipp_row_peak_list_4d:
	pipp_row_peak_4d+;

pipp_row_peak_4d:
	L_paren Float_PR Comma Float_PR Comma Float_PR Comma Float_PR Semicolon
	Number_sign Integer_PR Semicolon
	(Assignments_PR | L_brkt Float_PR Comma Float_PR Comma Float_PR Comma Float_PR R_brkt)
	Caret Real_PR Semicolon
	Percent_sign Integer_PR Semicolon
	R_paren (RETURN_PR | EOF);

/* number expression in peak list */
number:	Integer | Float | Real | Any_name;

