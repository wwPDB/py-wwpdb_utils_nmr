/*
 Sparky NPK (Non-spectral peak list) parser grammar for ANTLR v4.
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

parser grammar SparkyNPKParser;

options { tokenVocab=SparkyPKLexer; }

sparky_npk:
	RETURN?
	(
	data_label |
	peak_2d+ |
	peak_3d+ |
	peak_4d+
	)*
	EOF;

data_label:
	Assignment W1_LA W2_LA W3_LA? W4_LA? Dummy_H_LA? Height_LA? Volume_LA? S_N_LA? Note_LA? RETURN_LA RETURN?;
//	(peak_2d+ | peak_3d+ | peak_4d+);

peak_2d:
	Assignment_2d_ex Float Float Simple_name? (RETURN | EOF);

peak_3d:
	Assignment_3d_ex Float Float Float Simple_name? (RETURN | EOF);

peak_4d:
	Assignment_4d_ex Float Float Float Float Simple_name? (RETURN | EOF);

