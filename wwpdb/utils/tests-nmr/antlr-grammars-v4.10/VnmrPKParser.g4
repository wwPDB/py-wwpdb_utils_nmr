/*
 Vnmr PK (Spectral peak list) parser grammar for ANTLR v4.
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

parser grammar VnmrPKParser;

options { tokenVocab=VnmrPKLexer; }

vnmr_pk:
	RETURN?
	(
	comment |
	format |
	data_label |
	peak_2d+ |
	peak_3d+ |
	peak_4d+ |
	RETURN
	)*
	EOF;

/* VNMR: ll2d peak list format */

comment:
	COMMENT Any_name* (RETURN_CM | EOF);

format:
	Format Peak_number X_ppm Y_ppm Z_ppm? A_ppm? Intensity Volume?
	(Linewidth_X | FWHM_X)? (Linewidth_Y | FWHM_Y)? (Linewidth_Z | FWHM_Z)? (Linewidth_A | FWHM_A)? Comment? RETURN_FO
	(peak_ll2d+ | peak_ll3d+ | peak_ll4d+);

peak_ll2d:
	Integer Float Float number number? number? number? Double_quote_string? (RETURN | EOF);

peak_ll3d:
	Integer Float Float Float number number? number? number? number? Double_quote_string? (RETURN | EOF);

peak_ll4d:
	Integer Float Float Float Float number number? number? number? number? number? Double_quote_string? (RETURN | EOF);

/* VNMR: Peak list format
 See also https://sites.google.com/site/ccpnwiki/home/documentation/contributed-software/bruce-d-ray-utility-programs/readme
*/

data_label:
	Peak_id Dim_0_ppm Dev_0 Dim_1_ppm Dev_1 (Dim_2_ppm Dev_2 (Dim_3_ppm Dev_3)?)? (Amplitude | Intensity_LA) Volume_LA? Assignment? RETURN_LA;

peak_2d:
	Integer Float Float Float Float number Assignment_2d_ex? (RETURN | EOF);

peak_3d:
	Integer Float Float Float Float Float Float number Assignment_3d_ex? (RETURN | EOF);

peak_4d:
	Integer Float Float Float Float Float Float Float Float number Assignment_4d_ex? (RETURN | EOF);

/* number expression in peak list */
number:	Real | Float | Integer;

