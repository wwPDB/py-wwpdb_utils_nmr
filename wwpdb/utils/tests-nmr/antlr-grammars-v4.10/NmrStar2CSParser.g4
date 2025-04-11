/*
 NMR-STAR V2.1 CS (Assigned chemical shift) parser grammar for ANTLR v4.
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

parser grammar NmrStar2CSParser;

options { tokenVocab=NmrStar2CSLexer; }

nmrstar2_cs:
	RETURN?
	(
	seq_loop |
	cs_loop |
	RETURN
	)*
	EOF;

seq_loop:
	Loop RETURN
	seq_tags+
	seq_data+
	Stop (RETURN | EOF)?;

seq_tags:
	(Residue_seq_code | Residue_label) RETURN;

seq_data:
	any+ RETURN;

cs_loop:
	Loop RETURN
	cs_tags+
	cs_data+
	Stop (RETURN | EOF)?;

cs_tags:
	(
	Atom_shift_assign_ID |
	Residue_author_seq_code |
	Residue_seq_code |
	Residue_label |
	Atom_name |
	Atom_type |
	Chem_shift_value |
	Chem_shift_value_error |
	Chem_shift_ambiguity_code
	) RETURN;

cs_data:
	any+ RETURN;

/* any data expression in peak list */
any:	Float | Integer | Simple_name | Double_quote_string | Single_quote_string;

