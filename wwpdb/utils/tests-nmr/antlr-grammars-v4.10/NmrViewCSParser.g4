/*
 NmrView (Assigned chemical shift) parser grammar for ANTLR v4.
 Copyright 2026 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

parser grammar NmrViewCSParser;

options { tokenVocab=NmrViewCSLexer; }

nmrview_cs:
	RETURN?
	res_def_list+
	RETURN*
	EOF;

res_def_list:
	res_id_def RETURN
	res_type_def RETURN
	(prev_type_def RETURN)?
	spin_system_def RETURN
	heterogeneity_def RETURN
	(shift_list RETURN)+
	End_Res_Def (RETURN | EOF)?;

res_id_def:
	Res_ID Integer;

res_type_def:
	Res_Type Simple_name;

prev_type_def:
	Prev_Type Type_pred+;

spin_system_def:
	Spin_System_ID Integer;

heterogeneity_def:
	Heterogeneity Integer;

shift_list:
	Simple_name Float Float? (Single_note | Note_begin Note_middle* Note_end)?;
