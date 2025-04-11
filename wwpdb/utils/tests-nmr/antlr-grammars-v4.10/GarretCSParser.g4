/*
 Garret (Assigned chemical shift) parser grammar for ANTLR v4.
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

parser grammar GarretCSParser;

options { tokenVocab=GarretCSLexer; }

garret_cs:
	RETURN?
	residue_list+
	RETURN*
	EOF;

residue_list:
	Integer Simple_name RETURN
	shift_list+
	SMCLN_COMMENT;

shift_list:
	Simple_name number RETURN?;

/* number expression in chemical shift */
number: Float | Integer | Simple_name;

