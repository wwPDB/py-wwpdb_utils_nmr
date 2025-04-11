/*
 PIPP (Assigned chemical shift) parser grammar for ANTLR v4.
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

parser grammar PippCSParser;

options { tokenVocab=PippCSLexer; }

pipp_cs:
	RETURN?
	(
	pipp_format |
	RETURN
	)*
	EOF;

pipp_format:
	Shift_fl_frmt Res_siad RETURN
	First_res_in_seq Integer RETURN
	ext_peak_pick_tbl?
	residue_list+;

ext_peak_pick_tbl:
	Exp_peak_pick_tbl RETURN_ET
	Label Exp_par_fl Peak_pick_fl Cross_ref RETURN_ET
	ext_peak_pick_tbl_row+;

ext_peak_pick_tbl_row:
	Simple_name_ET Simple_name_ET Simple_name_ET Simple_name_ET RETURN_ET;

residue_list:
	(Res_ID | Res_ID_) Integer RETURN
	Res_type Simple_name RETURN
	Spin_system_ID Integer RETURN
	Heterogeneity Integer RETURN
	shift_list+
	End_res_def (RETURN | EOF);

shift_list:
	Simple_name number L_paren Simple_name+ R_paren RETURN;

/* number expression in chemical shift */
number: Float | Integer | Simple_name;

