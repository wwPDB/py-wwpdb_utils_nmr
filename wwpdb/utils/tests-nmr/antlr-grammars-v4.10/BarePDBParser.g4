/*
 Bare PDB parser grammar for ANTLR v4.
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

parser grammar BarePDBParser;

options { tokenVocab=BarePDBLexer; }

bare_pdb:
	(
	comment |
	coordinates |
	terminal |
	End
	)*
	EOF;

comment:
	COMMENT Any_name* (RETURN_CM | EOF);

coordinates:
	atom_coordinate+;

atom_coordinate:
	atom_num Simple_name Simple_name (Integer Integer | Simple_name? Integer | Simple_name) xyz (Float Float)? non_float? non_float?;

atom_num:
	(Atom Integer | Hetatm Integer | Hetatm_decimal);

xyz:
	(Float Float Float | Float Float_concat_2 | Float_concat_2 Float | Float_concat_3);

non_float:
	Simple_name | Integer;

terminal:
	Ter Any_name* (RETURN_CM | EOF);
