/*
 SYBYL MR (Magnetic Restraint) parser grammar for ANTLR v4.
 Copyright 2022 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

parser grammar SybylMRParser;

options { tokenVocab=SybylMRLexer; }

sybyl_mr:
	distance_restraints*
	EOF;

/* SYBYL - Distance restraints
*/
distance_restraints:
	Atom1 Atom2 Lower Upper
	distance_restraint+;

distance_restraint:
	Atom_selection Atom_selection
	number number;

/* number expression in restrains */
number:	Float | Float_DecimalComma | Integer;

