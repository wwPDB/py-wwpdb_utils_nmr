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
	peak_list_4d |
	peak_list_wo_eju_2d |
	peak_list_wo_eju_3d |
	peak_list_wo_eju_4d
	)*
	EOF;

/* NMRView: Peak list format
 See also https://github.com/onemoonsci/nmrfxprocessordocs/blob/master/pages/02.viewer/08.refcmds/01.ref/docs.md
*/

data_label:
	Label Dataset Sw Sf RETURN_LA
	labels RETURN_LA
	Simple_name_LA RETURN_LA
	labels RETURN_LA
	labels RETURN_LA;

labels:
	label+;

peak_list_2d:
	L_name P_name W_name B_name E_name J_name U_name
	L_name P_name W_name B_name E_name J_name U_name
	Vol Int Stat Comment? Flag0 RETURN?
	peak_2d+;

peak_2d:
	Integer
	ENCLOSE_DATA Float Float Float Simple_name ENCLOSE_DATA ENCLOSE_DATA
	ENCLOSE_DATA Float Float Float Simple_name ENCLOSE_DATA ENCLOSE_DATA
	Float Float Integer ENCLOSE_DATA? Integer RETURN;

peak_list_3d:
	L_name P_name W_name B_name E_name J_name U_name
	L_name P_name W_name B_name E_name J_name U_name
	L_name P_name W_name B_name E_name J_name U_name
	Vol Int Stat Comment? Flag0 RETURN?
	peak_3d+;

peak_3d:
	Integer
	ENCLOSE_DATA Float Float Float Simple_name ENCLOSE_DATA ENCLOSE_DATA
	ENCLOSE_DATA Float Float Float Simple_name ENCLOSE_DATA ENCLOSE_DATA
	ENCLOSE_DATA Float Float Float Simple_name ENCLOSE_DATA ENCLOSE_DATA
	Float Float Integer ENCLOSE_DATA? Integer RETURN;

peak_list_4d:
	L_name P_name W_name B_name E_name J_name U_name
	L_name P_name W_name B_name E_name J_name U_name
	L_name P_name W_name B_name E_name J_name U_name
	L_name P_name W_name B_name E_name J_name U_name
	Vol Int Stat Comment? Flag0 RETURN?
	peak_4d+;

peak_4d:
	Integer
	ENCLOSE_DATA Float Float Float Simple_name ENCLOSE_DATA ENCLOSE_DATA
	ENCLOSE_DATA Float Float Float Simple_name ENCLOSE_DATA ENCLOSE_DATA
	ENCLOSE_DATA Float Float Float Simple_name ENCLOSE_DATA ENCLOSE_DATA
	ENCLOSE_DATA Float Float Float Simple_name ENCLOSE_DATA ENCLOSE_DATA
	Float Float Integer ENCLOSE_DATA? Integer RETURN;

peak_list_wo_eju_2d:
	L_name P_name W_name B_name
	L_name P_name W_name B_name
	Vol Int Stat Comment? Flag0 RETURN?
	peak_wo_eju_2d+;

peak_wo_eju_2d:
	Integer
	ENCLOSE_DATA Float Float Float
	ENCLOSE_DATA Float Float Float
	Float Float Integer ENCLOSE_DATA? Integer RETURN;

peak_list_wo_eju_3d:
	L_name P_name W_name B_name
	L_name P_name W_name B_name
	L_name P_name W_name B_name
	Vol Int Stat Comment? Flag0 RETURN?
	peak_wo_eju_3d+;

peak_wo_eju_3d:
	Integer
	ENCLOSE_DATA Float Float Float
	ENCLOSE_DATA Float Float Float
	ENCLOSE_DATA Float Float Float
	Float Float Integer ENCLOSE_DATA? Integer RETURN;

peak_list_wo_eju_4d:
	L_name P_name W_name B_name
	L_name P_name W_name B_name
	L_name P_name W_name B_name
	L_name P_name W_name B_name
	Vol Int Stat Comment? Flag0 RETURN?
	peak_wo_eju_4d+;

peak_wo_eju_4d:
	Integer
	ENCLOSE_DATA Float Float Float
	ENCLOSE_DATA Float Float Float
	ENCLOSE_DATA Float Float Float
	ENCLOSE_DATA Float Float Float
	Float Float Integer ENCLOSE_DATA? Integer RETURN;

label:
	Float_LA | Simple_name_LA | ENCLOSE_DATA_LA;

