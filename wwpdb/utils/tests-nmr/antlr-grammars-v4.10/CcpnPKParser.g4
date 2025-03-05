/*
 Ccpn PK (Spectral peak list) parser grammar for ANTLR v4.
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

parser grammar CcpnPKParser;

options { tokenVocab=CcpnPKLexer; }

/* CCPN: Peak list format
 See also https://sites.google.com/site/ccpnwiki/home/documentation/ccpnmr-analysis/popup-reference/peaks-peak-lists
*/

ccpn_pk:
	RETURN?
	(
	peak_list_2d |
	peak_list_3d |
	peak_list_4d |
	RETURN
	)*
	EOF;

peak_list_2d:
	Number? (Id | Id_)
	(((Position_F1 | Shift_F1) (Position_F2 | Shift_F2) Assign_F1 Assign_F2) |
	 (Assign_F1 Assign_F2 (Position_F1 | Shift_F1) (Position_F2 | Shift_F2)))
	Height Volume?
	Line_width_F1? Line_width_F2?
	Merit?
	Details? Fit_method? Vol_method? RETURN_VARS
	peak_2d+;

peak_2d:
	Integer? Integer
	((position position Simple_name Simple_name) |
	 (Simple_name Simple_name position position))
	number number?
	position? position?
	position?
	note* (RETURN | EOF);

peak_list_3d:
	Number? (Id | Id_)
	(((Position_F1 | Shift_F1) (Position_F2 | Shift_F2) (Position_F3 | Shift_F3) Assign_F1 Assign_F2 Assign_F3) |
	 (Assign_F1 Assign_F2 Assign_F3 (Position_F1 | Shift_F1) (Position_F2 | Shift_F2) (Position_F3 | Shift_F3)))
	Height Volume?
	Line_width_F1? Line_width_F2? Line_width_F3?
	Merit?
	Details? Fit_method? Vol_method? RETURN_VARS
	peak_3d+;

peak_3d:
	Integer? Integer
	((position position position Simple_name Simple_name Simple_name) |
	 (Simple_name Simple_name Simple_name position position position))
	number number?
	position? position? position?
	position?
	note* (RETURN | EOF);

peak_list_4d:
	Number? (Id | Id_)
	(((Position_F1 | Shift_F1) (Position_F2 | Shift_F2) (Position_F3 | Shift_F3) (Position_F4 | Shift_F4) Assign_F1 Assign_F2 Assign_F3 Assign_F4) |
	 (Assign_F1 Assign_F2 Assign_F3 Assign_F4 (Position_F1 | Shift_F1) (Position_F2 | Shift_F2) (Position_F3 | Shift_F3) (Position_F4 | Shift_F4)))
	Height Volume?
	Line_width_F1? Line_width_F2? Line_width_F3? Line_width_F4?
	Merit?
	Details? Fit_method? Vol_method? RETURN_VARS
	peak_4d+;

peak_4d:
	Integer? Integer
	((position position position position Simple_name Simple_name Simple_name Simple_name) |
	 ( Simple_name Simple_name Simple_name Simple_name position position position position))
	number number?
	position? position? position? position?
	position?
	note* (RETURN | EOF);

/* position expression in peak list */
position: Float | Real | Integer | Simple_name;

/* number expression in peak list */
number:	Float | Real | Integer | Simple_name;

/* note expression in peak list */
note:	Float | Real | Integer | Simple_name | Any_name;

