/*
 Bare MR (Assigned chemical shift - WSV/TSV/CSV) parser grammar for ANTLR v4.
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

parser grammar BareMRParser;

options { tokenVocab=BareMRLexer; }

bare_mr:
	RETURN?
	(
	mr_raw_format |
	RETURN
	)*
	EOF;

mr_raw_format:
	(Simple_name+ | Double_quote_string+) RETURN
	mr_raw_list+;

mr_raw_list:
	any+ (RETURN | EOF);

/* any data expression in peak list */
any:	Float | Integer | Simple_name | Double_quote_float | Double_quote_integer | Double_quote_string;

