/*
 PPM (Assigned chemical shift) parser grammar for ANTLR v4.
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

parser grammar PpmCSParser;

options { tokenVocab=PpmCSLexer; }

ppm_cs:
	RETURN?
	ppm_list+
	RETURN*
	EOF;

ppm_list:
	(Simple_name | Atom_selection_2d_ex | Atom_selection_3d_ex) number Integer? (RETURN | EOF)?;

/* number expression in chemical shift */
number: Float | Integer | Simple_name;

