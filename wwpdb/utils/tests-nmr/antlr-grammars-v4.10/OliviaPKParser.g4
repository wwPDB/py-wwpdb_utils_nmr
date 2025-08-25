/*
 Olivia PK (Spectral peak list) parser grammar for ANTLR v4.
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

parser grammar OliviaPKParser;

options { tokenVocab=OliviaPKLexer; }

olivia_pk:
	RETURN?
	(
	comment |
	idx_peak_list_2d |
	idx_peak_list_3d |
	idx_peak_list_4d |
	ass_peak_list_2d |
	ass_peak_list_3d |
	ass_peak_list_4d |
	RETURN
	)*
	EOF;

comment:
	COMMENT Any_name* (RETURN_CM | EOF);

idx_peak_list_2d:
	Typedef Idx_tbl_2d RETURN_TD
	Separator (Tab | Comma | Space) RETURN_SE
	Format
	 Index
	 (def_2d_axis_order_ppm | tp_2d_axis_order_ppm | def_2d_axis_order_hz | tp_2d_axis_order_hz)
	 Amplitude Volume Vol_err
	 X_chain X_resname X_seqnum X_assign
	 Y_chain Y_resname Y_seqnum Y_assign
	 Eval Status User_memo Update_time
	RETURN_FO
	Printf_string
	Printf_string Printf_string
	Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	RETURN_PF
	idx_peak_2d+
	Unformat;

idx_peak_2d:
	Integer
	number number
	number number number
	string string integer string
	string string integer string
	Integer Integer memo Integer RETURN;

idx_peak_list_3d:
	Typedef Idx_tbl_3d RETURN_TD
	Separator (Tab | Comma | Space) RETURN_SE
	Format
	 Index
	 (def_3d_axis_order_ppm | tp_3d_axis_order_ppm | def_3d_axis_order_hz | tp_3d_axis_order_hz)
	 Amplitude Volume Vol_err
	 X_chain X_resname X_seqnum X_assign
	 Y_chain Y_resname Y_seqnum Y_assign
	 Z_chain Z_resname Z_seqnum Z_assign
	 Eval Status User_memo Update_time
	RETURN_FO
	Printf_string
	Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	RETURN_PF
	idx_peak_3d+
	Unformat;

idx_peak_3d:
	Integer
	number number number
	number number number
	string string integer string
	string string integer string
	string string integer string
	Integer Integer memo Integer RETURN;

idx_peak_list_4d:
	Typedef Idx_tbl_4d RETURN_TD
	Separator (Tab | Comma | Space) RETURN_SE
	Format
	 Index
	 (def_4d_axis_order_ppm | tp_4d_axis_order_ppm | def_4d_axis_order_hz | tp_4d_axis_order_hz)
	 Amplitude Volume Vol_err
	 X_chain X_resname X_seqnum X_assign
	 Y_chain Y_resname Y_seqnum Y_assign
	 Z_chain Z_resname Z_seqnum Z_assign
	 A_chain A_resname A_seqnum A_assign
	 Eval Status User_memo Update_time
	RETURN_FO
	Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	RETURN_PF
	idx_peak_4d+
	Unformat;

idx_peak_4d:
	Integer
	number number number number
	number number number
	string string integer string
	string string integer string
	string string integer string
	string string integer string
	Integer Integer memo Integer RETURN;

ass_peak_list_2d:
	Typedef Ass_tbl_2d RETURN_TD
	Separator (Tab | Comma | Space) RETURN_SE
	Format
	 X_chain X_resname X_seqnum X_assign
	 Y_chain Y_resname Y_seqnum Y_assign
	 Index
	 (def_2d_axis_order_ppm | tp_2d_axis_order_ppm | def_2d_axis_order_hz | tp_2d_axis_order_hz)
	 Amplitude Volume Vol_err
	 Eval Status User_memo Update_time
	RETURN_FO
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string
	Printf_string Printf_string
	Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	RETURN_PF
	ass_peak_2d+
	Unformat;

ass_peak_2d:
	string string integer string
	string string integer string
	Integer
	number number
	number number number
	Integer Integer memo Integer RETURN;

ass_peak_list_3d:
	Typedef Ass_tbl_3d RETURN_TD
	Separator (Tab | Comma | Space) RETURN_SE
	Format
	 X_chain X_resname X_seqnum X_assign
	 Y_chain Y_resname Y_seqnum Y_assign
	 Z_chain Z_resname Z_seqnum Z_assign
	 Index
	 (def_3d_axis_order_ppm | tp_3d_axis_order_ppm | def_3d_axis_order_hz | tp_3d_axis_order_hz)
	 Amplitude Volume Vol_err
	 Eval Status User_memo Update_time
	RETURN_FO
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string
	Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	RETURN_PF
	ass_peak_3d+
	Unformat;

ass_peak_3d:
	string string integer string
	string string integer string
	string string integer string
	Integer
	number number number
	number number number
	Integer Integer memo Integer RETURN;

ass_peak_list_4d:
	Typedef Ass_tbl_4d RETURN_TD
	Separator (Tab | Comma | Space) RETURN_SE
	Format
	 X_chain X_resname X_seqnum X_assign
	 Y_chain Y_resname Y_seqnum Y_assign
	 Z_chain Z_resname Z_seqnum Z_assign
	 A_chain A_resname A_seqnum A_assign
	 Index
	 (def_4d_axis_order_ppm | tp_4d_axis_order_ppm | def_4d_axis_order_hz | tp_4d_axis_order_hz)
	 Amplitude Volume Vol_err
	 Eval Status User_memo Update_time
	RETURN_FO
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string
	Printf_string Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string
	Printf_string Printf_string Printf_string Printf_string
	RETURN_PF
	ass_peak_4d+
	Unformat;

ass_peak_4d:
	string string integer string
	string string integer string
	string string integer string
	string string integer string
	Integer
	number number number number
	number number number
	Integer Integer memo Integer RETURN;

def_2d_axis_order_ppm:
	X_ppm Y_ppm;

tp_2d_axis_order_ppm:
	Y_ppm X_ppm;

def_2d_axis_order_hz:
	X_hz Y_hz;

tp_2d_axis_order_hz:
	Y_hz X_hz;

def_3d_axis_order_ppm:
	X_ppm Y_ppm Z_ppm;

tp_3d_axis_order_ppm:
	Z_ppm Y_ppm X_ppm;

def_3d_axis_order_hz:
	X_hz Y_hz Z_hz;

tp_3d_axis_order_hz:
	Z_hz Y_hz X_hz;

def_4d_axis_order_ppm:
	X_ppm Y_ppm Z_ppm A_ppm;

tp_4d_axis_order_ppm:
	A_ppm Z_ppm Y_ppm X_ppm;

def_4d_axis_order_hz:
	X_hz Y_hz Z_hz A_hz;

tp_4d_axis_order_hz:
	A_hz Z_hz Y_hz X_hz;

string:
	Simple_name | Null_string;

integer:
	Integer | Null_string;

/* number expression in peak list */
number:	Integer | Float | Real;

memo:	Double_quote_string | Single_quote_string | Simple_name;

