/*
 Bare PK (Spectral peak list) parser grammar for ANTLR v4.
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
	RETURN
	)*
	EOF;

peak_list_2d:
	peak_2d+;

peak_2d:
	Simple_name Integer Simple_name Simple_name Float
	Simple_name Integer Simple_name Simple_name Float
	number* (RETURN | EOF);

peak_list_3d:
	peak_3d+;

peak_3d:
	Simple_name Integer Simple_name Simple_name Float
	Simple_name Integer Simple_name Simple_name Float
	Simple_name Integer Simple_name Simple_name Float
	number* (RETURN | EOF);

peak_list_4d:
	peak_4d+;

peak_4d:
	Simple_name Integer Simple_name Simple_name Float
	Simple_name Integer Simple_name Simple_name Float
	Simple_name Integer Simple_name Simple_name Float
	Simple_name Integer Simple_name Simple_name Float
	number* (RETURN | EOF);

peak_list_wo_chain_2d:
	peak_wo_chain_2d+;

peak_wo_chain_2d:
	Integer Simple_name Simple_name Float
	Integer Simple_name Simple_name Float
	number* (RETURN | EOF);

peak_list_wo_chain_3d:
	peak_wo_chain_3d+;

peak_wo_chain_3d:
	Integer Simple_name Simple_name Float
	Integer Simple_name Simple_name Float
	Integer Simple_name Simple_name Float
	number* (RETURN | EOF);

peak_list_wo_chain_4d:
	peak_wo_chain_4d+;

peak_wo_chain_4d:
	Integer Simple_name Simple_name Float
	Integer Simple_name Simple_name Float
	Integer Simple_name Simple_name Float
	Integer Simple_name Simple_name Float
	number* (RETURN | EOF);

/* number expression in peak list */
number:	Float | Real | Integer;

