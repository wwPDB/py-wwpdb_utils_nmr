/*
 Olivia CS (Assigned chemical shift) parser grammar for ANTLR v4.
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

parser grammar OliviaCSParser;

options { tokenVocab=OliviaCSLexer; }

olivia_cs:
	RETURN?
	(
	comment |
	sequence |
	chemical_shifts |
	RETURN
	)*
	EOF;

sequence:
	Typedef Sequence RETURN_TD
	Separator (Tab | Comma | Space) RETURN_SE
	Format
	 Chain Resname Seqnum
	RETURN_FO
	Printf_string Printf_string Printf_string
	RETURN_PF
	residue+
	Unformat;

residue:
	Simple_name Simple_name Integer RETURN;

chemical_shifts:
	Typedef (Ass_tbl_h2o | Ass_tbl_tro | Ass_tbl_d2o) RETURN_TD
	Separator (Tab | Comma | Space) RETURN_SE
	Format
	 Chain Resname Seqnum Atomname Shift Stddev
	RETURN_FO
	Printf_string Printf_string Printf_string Printf_string Printf_string Printf_string
	RETURN_PF
	chemical_shift+
	Unformat;

chemical_shift:
	Simple_name Simple_name Integer Simple_name number number RETURN;

/* number expression in chemical shift */
number:	Integer | Float | Real;

comment:
	COMMENT Any_name* RETURN_CM;

