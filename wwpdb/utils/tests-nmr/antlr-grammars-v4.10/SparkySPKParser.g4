/*
 Sparky PK (Spectral peak list - Save file) parser grammar for ANTLR v4.
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

parser grammar SparkySPKParser;

options { tokenVocab=SparkySPKLexer; }

sparky_spk:
	(
	Sparky_save_file
	Version
	user_block
	spectrum_block
	)+
	EOF;

user_block:
	User user_statement* End_user;

user_statement:
	RETURN_US |
	Set Mode_US Integer_US RETURN_US |
	Set Save_prompt Integer_US RETURN_US |
	Set Save_interval Integer_US RETURN_US |
	Set Resize_views Integer_US RETURN_US |
	Set Key_timeout Integer_US RETURN_US |
	Set Cache_size Integer_US RETURN_US |
	Set Contour_graying Integer_US RETURN_US |
	Default Print Command (Print | Simple_name_US) RETURN_US |
	Default Print File Simple_name_US? RETURN_US |
	Default Print Options Integer_US Integer_US Float_US Float_US RETURN_US;

spectrum_block:
	Spectrum spectrum_statement* End_spectrum;

spectrum_statement:
	RETURN_SP |
	Name_SP	spectrum_name* RETURN_SP |
	Path_name Any_name_SP RETURN_SP |
	Dimension Integer_SP RETURN_SP |
	Shift Float_SP+ RETURN_SP |
	Points Integer_SP+ RETURN_SP |
	Assign_multi_axis_guess Integer_SP RETURN_SP |
	Assign_guess_threshhold Float_SP RETURN_SP |
	Assign_relation Integer_SP+ RETURN_SP |
	Assign_range Integer_SP Float_SP RETURN_SP |
	Assign_format Format_ex RETURN_SP |
	List_tool Sort_by Simple_name_SP RETURN_SP |
	List_tool Name_type Simple_name_SP RETURN_SP |
	List_tool Sort_axis Simple_name_SP RETURN_SP |
	List_tool Show_flags Simple_name_SP* RETURN_SP |
	Integrate_overlapped_sep Float_SP+ RETURN_SP |
	Integrate_methods Integer_SP+ RETURN_SP |
	Integrate_allow_motion Integer_SP RETURN_SP |
	Integrate_adjust_linewidths Integer_SP RETURN_SP |
	Integrate_motion_range Float_SP+ RETURN_SP |
	Integrate_min_linewidth Float_SP+ RETURN_SP |
	Integrate_max_linewidth Float_SP+ RETURN_SP |
	Integrate_fit_baseline Integer_SP RETURN_SP |
	Integrate_subtract_peaks Integer_SP RETURN_SP |
	Integrate_contoured_data Integer_SP RETURN_SP |
	Integrate_rectangle_data Integer_SP RETURN_SP |
	Integrate_max_iterations Integer_SP RETURN_SP |
	Integrate_tolerance Float_SP RETURN_SP |
	Peak_pick Float_SP+ Integer_SP RETURN_SP |
	Peak_pick_minimum_linewidth Float_SP+ RETURN_SP |
	Peak_pick_minimum_dropoff Float_SP RETURN_SP |
	Noise_sigma Float_SP RETURN_SP |
	Ornament_labe_size Float_SP RETURN_SP |
	Ornament_line_size Float_SP RETURN_SP |
	Ornament_peak_size Float_SP RETURN_SP |
	Ornament_grid_size Float_SP RETURN_SP |
	Ornament_peak_group_size Float_SP RETURN_SP |
	Ornament_select_size Float_SP RETURN_SP |
	Ornament_pointer_size Float_SP RETURN_SP |
	Ornament_line_end_size Float_SP RETURN_SP |
	attached_data RETURN_SP |
	view RETURN_SP |
	ornament RETURN_SP;

spectrum_name:
	Integer_SP | Float_SP | Simple_name_SP | Any_name_SP;

attached_data:
	Attached_data attached_data_statement* End_attached_data;

attached_data_statement:
	Any_name_AD;

view:
	View view_statement* End_view;

view_statement:
	RETURN_VI |
	Name_VI view_name* RETURN_VI |
	Precision Integer_VI RETURN_VI |
	Precision_by_units Integer_VI+ RETURN_VI |
	View_mode Integer_VI RETURN_VI |
	Show Integer_VI Simple_name_VI* RETURN_VI |
	Axis_type Integer_VI RETURN_VI |
	Flags_VI Simple_name_VI* RETURN_VI |
	Contour_pos Integer_VI view_number Float_VI Float_VI Simple_name_VI+ RETURN_VI |
	Contour_neg Integer_VI view_number Float_VI Float_VI Simple_name_VI+ RETURN_VI |
	params RETURN_VI;

view_name:
	Integer_VI | Float_VI | Real_VI | Simple_name_VI;

view_number:
	Integer_VI | Float_VI | Real_VI;

params:
	Params params_statement* End_params;

params_statement:
	RETURN_PA |
	Orientation Integer_PA+ RETURN_PA |
	Location Integer_PA+ RETURN_PA |
	Size Integer_PA+ RETURN_PA |
	Offset Float_PA+ RETURN_PA |
	Scale Float_PA+ RETURN_PA |
	Zoom Float_PA RETURN_PA |
	Flags_PA Integer_PA RETURN_PA;

ornament:
	Ornament ornament_statement* End_ornament;

ornament_statement:
	RETURN_OR |
	Type_OR Peak RETURN_OR |
	Type_OR Grid RETURN_OR |
	Color_OR Integer_OR+ Simple_name_OR+ RETURN_OR |
	Flags_OR Integer_OR+ RETURN_OR |
	Id Integer_OR RETURN_OR |
	Pos_OR ornament_position+ RETURN_OR |
	Height Float_OR+ RETURN_OR |
	Line_width Float_OR+ Simple_name_OR? RETURN_OR |
	Integral Real_OR Simple_name_OR? RETURN_OR |
	Fr Float_OR RETURN_OR |
	Rs Rs_ex+ RETURN_OR |
	label RETURN_OR;

ornament_position:
	Integer_OR | Float_OR;

label:
	L_brakt label_statement* R_brakt;

label_statement:
	RETURN_LA |
	Type_LA Label RETURN_LA |
	Color_LA Integer_LA+ Simple_name_LA+ RETURN_LA |
	Flags_LA Integer_LA+ RETURN_LA |
	Mode_LA Integer_LA RETURN_LA |
	Pos_LA label_position+ RETURN_LA |
	Label (Assignment_2d_ex | Assignment_3d_ex | Assignment_4d_ex) RETURN_LA |
	Xy Xy_pos+ RETURN_LA;

label_position:
	Integer_LA | Float_LA;

