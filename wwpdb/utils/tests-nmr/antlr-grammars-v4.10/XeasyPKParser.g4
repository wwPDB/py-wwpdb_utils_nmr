/*
 Xeasy PK (Spectral peak list) parser grammar for ANTLR v4.
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

parser grammar XeasyPKParser;

options { tokenVocab=XeasyPKLexer; }

xeasy_pk:
	(
	dimension |
	format |
	iname |
	cyana_format |
	spectrum |
	tolerance |
	peak_list_2d |
	peak_list_3d |
	peak_list_4d
	)*
	EOF;

dimension:
	Num_of_dim Integer_ND RETURN_ND;

format:
	Format Simple_name_FO RETURN_FO;

iname:
	Iname Integer_IN Simple_name_IN RETURN_IN;

cyana_format:
	Cyana_format Simple_name_CY RETURN_CY;

spectrum:
	Spectrum Simple_name_SP+ RETURN_SP;

tolerance:
	Tolerance Float_TO+ RETURN_TO;

peak_list_2d:
	peak_2d+;

peak_2d:
	Integer
	Float Float
	Integer Simple_name
	number number
	Simple_name Integer
	assign assign RETURN
	(assign assign RETURN)*;

peak_list_3d:
	peak_3d+;

peak_3d:
	Integer
	Float Float Float
	Integer Simple_name
	number number
	Simple_name Integer
	assign assign assign RETURN
	(assign assign assign RETURN)*;

peak_list_4d:
	peak_4d+;

peak_4d:
	Integer
	Float Float Float Float
	Integer Simple_name
	number number
	Simple_name Integer
	assign assign assign assign RETURN
	(assign assign assign assign RETURN)*;

/* number expression in peak list */
number: Float | Real | Integer | Simple_name;

/* assignment expression in peak list */
assign: Integer | (Simple_name Integer?);

