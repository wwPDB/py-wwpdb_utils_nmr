/*
 DIANA (Assigned chemical shift) parser grammar for ANTLR v4.
 Copyright 2026 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

parser grammar DianaCSParser;

options { tokenVocab=DianaCSLexer; }

diana_cs:
	(
	comment |
	chemical_shifts
	)*
	EOF;

comment:
	COMMENT Any_name* (RETURN_CM | EOF);

/* DUANA chemical shifts (undocumented) */
chemical_shifts:
	chemical_shift+;

chemical_shift:
	Shifts Simple_name Integer
        atom_chemical_shift+
	Simple_name? Integer?;

atom_chemical_shift:
	Simple_name Float Float?;

