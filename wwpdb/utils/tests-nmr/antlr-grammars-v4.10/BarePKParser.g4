/*
 Bare PK (Spectral peak list - WSV/TSV with a header) parser grammar for ANTLR v4.
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

parser grammar BarePKParser;

options { tokenVocab=BarePKLexer; }

bare_pk:
	RETURN?
	(
	peak_list_2d |
	peak_list_3d |
	peak_list_4d |
	peak_list_wo_chain_2d |
	peak_list_wo_chain_3d |
	peak_list_wo_chain_4d |
	raw_format_2d |
	raw_format_3d |
	raw_format_4d |
	rev_raw_format_2d |
	rev_raw_format_3d |
	rev_raw_format_4d |
	RETURN
	)*
	EOF;

peak_list_2d:
	peak_2d+;

peak_2d:
	Simple_name Integer Simple_name Simple_name position
	Simple_name Integer Simple_name Simple_name position
	number* (RETURN | EOF);

peak_list_3d:
	peak_3d+;

peak_3d:
	Simple_name Integer Simple_name Simple_name position
	Simple_name Integer Simple_name Simple_name position
	Simple_name Integer Simple_name Simple_name position
	number* (RETURN | EOF);

peak_list_4d:
	peak_4d+;

peak_4d:
	Simple_name Integer Simple_name Simple_name position
	Simple_name Integer Simple_name Simple_name position
	Simple_name Integer Simple_name Simple_name position
	Simple_name Integer Simple_name Simple_name position
	number* (RETURN | EOF);

peak_list_wo_chain_2d:
	peak_wo_chain_2d+;

peak_wo_chain_2d:
	Integer Simple_name Simple_name position
	Integer Simple_name Simple_name position
	number* (RETURN | EOF);

peak_list_wo_chain_3d:
	peak_wo_chain_3d+;

peak_wo_chain_3d:
	Integer Simple_name Simple_name position
	Integer Simple_name Simple_name position
	Integer Simple_name Simple_name position
	number* (RETURN | EOF);

peak_list_wo_chain_4d:
	peak_wo_chain_4d+;

peak_wo_chain_4d:
	Integer Simple_name Simple_name position
	Integer Simple_name Simple_name position
	Integer Simple_name Simple_name position
	Integer Simple_name Simple_name position
	number* (RETURN | EOF);

raw_format_2d:
	Peak X_ppm Y_ppm Amplitude? Volume? Label? Comment? RETURN_FO
	peak_list_raw_2d+;

raw_format_3d:
	Peak X_ppm Y_ppm Z_ppm Amplitude? Volume? Label? Comment? RETURN_FO
	peak_list_raw_3d+;

raw_format_4d:
	Peak X_ppm Y_ppm Z_ppm A_ppm Amplitude? Volume? Label? Comment? RETURN_FO
	peak_list_raw_4d+;

rev_raw_format_2d:
	Peak Y_ppm X_ppm Amplitude? Volume? Label? Comment? RETURN_FO
	peak_list_raw_2d+;

rev_raw_format_3d:
	Peak Z_ppm Y_ppm X_ppm Amplitude? Volume? Label? Comment? RETURN_FO
	peak_list_raw_3d+;

rev_raw_format_4d:
	Peak A_ppm Z_ppm Y_ppm X_ppm Amplitude? Volume? Label? Comment? RETURN_FO
	peak_list_raw_4d+;

peak_list_raw_2d:
	Integer position position number* Simple_name* (RETURN | EOF);

peak_list_raw_3d:
	Integer position position position number* Simple_name* (RETURN | EOF);

peak_list_raw_4d:
	Integer position position position position number* Simple_name* (RETURN | EOF);

/* position expression in peak list */
position: Float | Integer | Ambig_float;

/* number expression in peak list */
number:	Float | Real | Integer;

