/*
 NmrView PK (Spectral peak list) parser grammar for ANTLR v4.
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

parser grammar NmrViewPKParser;

options { tokenVocab=NmrViewPKLexer; }

nmrview_pk:
	(
	data_label |
	peak_list_2d |
	peak_list_3d |
	peak_list_4d
	)*
	EOF;

data_label:
	Label Dataset Sw Sf RETURN_LA
	labels RETURN_LA
	Simple_name_LA RETURN_LA
	widths RETURN_LA
	freqs RETURN_LA
	vars;

labels:
	Simple_name_LA+;

widths:
	Float_LA+;

freqs:
	Float_LA+;

vars:
	vars_per_axis+
	Vol Int Stat Comment Flag0;

vars_per_axis:
	L_name P_name W_name B_name E_name J_name U_name;

peak_list_2d:
	Integer
	ENCLOSE_COMMENT Float Float Float Simple_name ENCLOSE_COMMENT ENCLOSE_COMMENT
	ENCLOSE_COMMENT Float Float Float Simple_name ENCLOSE_COMMENT ENCLOSE_COMMENT
	Float Float Integer ENCLOSE_COMMENT Integer;

peak_list_3d:
	Integer
	ENCLOSE_COMMENT Float Float Float Simple_name ENCLOSE_COMMENT ENCLOSE_COMMENT
	ENCLOSE_COMMENT Float Float Float Simple_name ENCLOSE_COMMENT ENCLOSE_COMMENT
	ENCLOSE_COMMENT Float Float Float Simple_name ENCLOSE_COMMENT ENCLOSE_COMMENT
	Float Float Integer ENCLOSE_COMMENT Integer;

peak_list_4d:
	Integer
	ENCLOSE_COMMENT Float Float Float Simple_name ENCLOSE_COMMENT ENCLOSE_COMMENT
	ENCLOSE_COMMENT Float Float Float Simple_name ENCLOSE_COMMENT ENCLOSE_COMMENT
	ENCLOSE_COMMENT Float Float Float Simple_name ENCLOSE_COMMENT ENCLOSE_COMMENT
	ENCLOSE_COMMENT Float Float Float Simple_name ENCLOSE_COMMENT ENCLOSE_COMMENT
	Float Float Integer ENCLOSE_COMMENT Integer;

