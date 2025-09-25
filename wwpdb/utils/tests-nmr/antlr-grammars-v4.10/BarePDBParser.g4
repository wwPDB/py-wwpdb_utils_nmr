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
	end
	)*
	EOF;

comment:
	COMMENT Any_name* (RETURN_CM | EOF);

coordinates:
	atom_coordinate+;

atom_coordinate:
	atom_num atom_name Simple_name (Integer Integer | Simple_name? (Integer | Integer_concat_alt) | Simple_name) xyz (number number | Float_concat_2)? undefined? undefined?;

atom_num:
	(Atom Integer | Hetatm Integer | Hetatm_decimal);

atom_name:
	Simple_name | Integer_concat_alt;

xyz:
	(number number number | x_yz | xy_z | x_y_z);

x_yz:
	number Float_concat_2;

xy_z:
	Float_concat_2 number;

x_y_z:
	Float_concat_3;

undefined:
	Simple_name | Integer | Float | Null_value;

number:
	Float | Integer;

terminal:
	Atom? Hetatm? Ter Any_name* (RETURN_CM | EOF);

end:	End Any_name* (RETURN_CM | EOF);
