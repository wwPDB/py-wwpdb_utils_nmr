/*
 ARIA MR (Magnetic Restraint) parser grammar for ANTLR v4.
 Copyright 2024 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

parser grammar AriaMRParser;

options { tokenVocab=AriaMRLexer; }

aria_mr:
	(
	distance_restraints
	)*
	EOF;

/* ARIA - Distance restraints
*/
distance_restraints:
	distance_restraint+;

distance_restraint:
	RefSpec RefSpecName RefPeak Integer Id Integer
	D number U number UViol number PViol number
	Viol ViolFlag Reliable ReliableFlag AType ATypeFlag
	contribution+;

contribution:
	atom_pair (D number_c PlusMinus number_c Weight number_c)?;

atom_pair:
	atom_selection Hyphen atom_selection;

atom_selection:
	Simple_name Simple_name Simple_name?;

/* number expression in restrains */
number:	Float | Integer;

/* number expression in contributions */
number_c: Float | Integer;

