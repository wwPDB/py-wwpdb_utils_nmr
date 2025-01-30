/*
 XwinNmr PK (Spectral peak list) parser grammar for ANTLR v4.
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

parser grammar XwinNmrPKParser;

options { tokenVocab=XwinNmrPKLexer; }

xwinnmr_pk:
	RETURN?
	(
	comment |
	dimension |
	peak_2d+ |
	peak_3d+ |
	peak_4d+
	)*
	EOF;

comment:
	COMMENT Any_name* (RETURN_CM | EOF);

dimension:
	Num_of_dim Integer_ND RETURN_ND;

peak_2d:
	Integer
	Float Float
	Float Float
	Float Float? Annotation* (RETURN | EOF);

peak_3d:
	Integer
	Float Float Float
	Float Float Float
	Float Float? Annotation* (RETURN | EOF);

peak_4d:
	Integer
	Float Float Float Float
	Float Float Float Float
	Float Float? Annotation* (RETURN | EOF);

