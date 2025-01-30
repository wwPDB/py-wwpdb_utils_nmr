/*
 Xeasy PROT parser grammar for ANTLR v4.
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

parser grammar XeasyPROTParser;

options { tokenVocab=XeasyPROTLexer; }

xeasy_prot:
	RETURN?
	prot+
	RETURN*
	EOF;

prot:
	Integer Float Float Simple_name residue (RETURN | EOF);
	
residue:
	Integer | Simple_name;

