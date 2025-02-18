/*
 Ponderosa PK (Spectral peak list) parser grammar for ANTLR v4.
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

parser grammar PonderosaPKParser;

options { tokenVocab=PonderosaPKLexer; }

ponderosa_pk:
	RETURN?
	(
	peak_list_2d |
	peak_list_3d |
	peak_list_4d |
	RETURN
	)*
	EOF;

peak_list_2d:
	Noesy_type Integer_NT Simple_name_NT RETURN_NT
	Axis_order Integer_AO Simple_name_AO RETURN_AO
	peak_2d+;

peak_2d:
	Float Float number Simple_name Simple_name (RETURN | EOF);

peak_list_3d:
	Noesy_type Integer_NT Simple_name_NT RETURN_NT
	Axis_order Integer_AO Simple_name_AO RETURN_AO
	peak_3d+;

peak_3d:
	Float Float Float number Simple_name Simple_name Simple_name (RETURN | EOF);

peak_list_4d:
	Noesy_type Integer_NT Simple_name_NT RETURN_NT
	Axis_order Integer_AO Simple_name_AO RETURN_AO
	peak_4d+;

peak_4d:
	Float Float Float Float number Simple_name Simple_name Simple_name Simple_name (RETURN | EOF);

/* number expression in peak list */
number:	Float | Real;

