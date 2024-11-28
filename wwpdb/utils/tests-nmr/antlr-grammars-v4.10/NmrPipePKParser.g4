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
	(
	data_label |
	peak_list_2d |
	peak_list_3d |
	peak_list_4d
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
	Vars
		Index
		X_axis Y_axis
		Dx Dy
		X_ppm Y_ppm
		X_hz Y_hz
		Xw Yw
		Xw_hz Yw_hz
		X1 X3 Y1 Y3
		Height DHeight Vol
		Pchi2 Type Ass
		ClustId Memcnt RETURN_VA
	Format Format_code
		Format_code Format_code
		Format_code Format_code
		Format_code Format_code
		Format_code Format_code
		Format_code Format_code
		Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code RETURN_FO
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
	number number number number
	number number number
	number Integer Simple_name
	Integer Integer;

peak_list_3d:
	Vars
		Index
		X_axis Y_axis Z_axis
		Dx Dy Dz
		X_ppm Y_ppm Z_ppm
		X_hz Y_hz Z_hz
		Xw Yw Zw
		Xw_hz Yw_hz Zw_hz
		X1 X3 Y1 Y3 Z1 Z3
		Height DHeight Vol
		Pchi2 Type Ass
		ClustId Memcnt RETURN_VA
	Format Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code RETURN_FO
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
	number number number number number number
	number number number
	number Integer Simple_name
	Integer Integer;

peak_list_4d:
	Vars
		Index
		X_axis Y_axis Z_axis A_axis
		Dx Dy Dz Dz
		X_ppm Y_ppm Z_ppm A_ppm
		X_hz Y_hz Z_hz A_hz
		Xw Yw Zw Aw
		Xw_hz Yw_hz Zw_hz Aw_hz
		X1 X3 Y1 Y3 Z1 Z3 A1 A3
		Height DHeight Vol
		Pchi2 Type Ass
		ClustId Memcnt RETURN_VA
	Format Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code Format_code Format_code Format_code Format_code Format_code
		Format_code Format_code Format_code
		Format_code Format_code RETURN_FO
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
	number number number number number number number number
	number number number
	number Integer Simple_name
	Integer Integer;

/* number expression in peak list */
number: Float | Real | Integer | Simple_name;

