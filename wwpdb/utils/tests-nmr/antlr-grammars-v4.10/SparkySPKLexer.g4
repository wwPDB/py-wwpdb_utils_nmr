/*
 Sparky PK (Spectral peak list - Save file) lexer grammar for ANTLR v4.
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

lexer grammar SparkySPKLexer;

Sparky_save_file:	'<sparky save file>';
Version:		'<version ' [.0-9]+ '>';

User:			'<user>' -> pushMode(USER_MODE);

Spectrum:		'<spectrum>' -> pushMode(SPECTRUM_MODE);

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' | '+' | '.' | '*' | '?';
fragment NAME_CHAR:	START_CHAR | '\'' | '"' | ',' | ';' | '#' | '%';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t\r\n]+ -> skip;

mode USER_MODE;

End_user:		'<end user>' -> popMode;

Set:			'set';

Mode_US:		'mode';
Save_prompt:		'saveprompt';
Save_interval:		'saveinterval';
Resize_views:		'resizeViews';
Key_timeout:		'keytimeout';
Cache_size:		'cachesize';
Contour_graying:	'contourgraying';

Default:		'default';

Print:			'print';
Command:		'command';
File:			'file';
Options:		'options';

Integer_US:		Integer;
Float_US:		Float;
Simple_name_US:		SIMPLE_NAME;

SPACE_US:		[ \t]+ -> skip;
RETURN_US:		[\r\n]+;

mode SPECTRUM_MODE;

Attached_data:		'<attached data>' -> pushMode(ATTACHED_DATA_MODE);
View:			'<view>' -> pushMode(VIEW_MODE);
Ornament:		'<ornament>' -> pushMode(ORNAMENT_MODE);

End_spectrum:		'<end spectrum>' -> popMode;

Name_SP:		'name';
Path_name:		'pathname';
Dimension:		'dimension';
Shift:			'shift';
Points:			'points';

Assign_multi_axis_guess:	'assignMultiAxisGuess';
Assign_guess_threshhold:	'assignGuessThreshold';
Assign_relation:		'assignRelation';
Assign_range:			'assignRange';
Assign_format:			'assignFormat';

List_tool:		'listTool';
Sort_by:		'sortBy';
Name_type:		'nameType';
Sort_axis:		'sortAxis';
Show_flags:		'showFlags';

Integrate_overlapped_sep:	'integrate.overlapped_sep';
Integrate_methods:		'integrate.methods';
Integrate_allow_motion:		'integrate.allow_motion';
Integrate_adjust_linewidths:	'integrate.adjust_linewidths';
Integrate_motion_range:		'integrate.motion_range';
Integrate_min_linewidth:	'integrate.min_linewidth';
Integrate_max_linewidth:	'integrate.max_linewidth';
Integrate_fit_baseline:		'integrate.fit_baseline';
Integrate_subtract_peaks:	'integrate.subtract_peaks';
Integrate_contoured_data:	'integrate.contoured_data';
Integrate_rectangle_data:	'integrate.rectangle_data';
Integrate_max_iterations:	'integrate.maxiterations';
Integrate_tolerance:		'integrate.tolerance';

Peak_pick:			'peak.pick';
Peak_pick_minimum_linewidth:	'peak.pick-minimum-linewidth';
Peak_pick_minimum_dropoff:	'peak.pick-minimum-dropoff';

Noise_sigma:			'noise.sigma';

Ornament_labe_size:		'ornament.label.size';
Ornament_line_size:		'ornament.line.size';
Ornament_peak_size:		'ornament.peak.size';
Ornament_grid_size:		'ornament.grid.size';
Ornament_peak_group_size:	'ornament.peakgroup.size';
Ornament_select_size:		'ornament.selectsize';
Ornament_pointer_size:		'ornament.pointersize';
Ornament_line_end_size:		'ornament.lineendsize';

Format_ex:		'%' SIMPLE_NAME ('-%' SIMPLE_NAME)+;

Integer_SP:		Integer;
Float_SP:		Float;
Simple_name_SP:		SIMPLE_NAME;

Any_name_SP:		 ~[ \t\r\n]+;

SPACE_SP:		[ \t]+ -> skip;
RETURN_SP:		[\r\n]+;

mode ATTACHED_DATA_MODE;

End_attached_data:	'<end attached data>' -> popMode;

Any_name_AD:		~[ \t\r\n]+;

SPACE_AD:		[ \t\r\n]+ -> skip;

mode VIEW_MODE;

Params:			'<params>' -> pushMode(PARAMS_MODE);
End_view:		'<end view>' -> popMode;

Name_VI:		'name';
Precision:		'precision';
Precision_by_units:	'precision_by_units';
View_mode:		'viewmode';
Show:			'show';
Axis_type:		'axistype';
Flags_VI:		'flags';

Contour_pos:		'contour.pos';
Contour_neg:		'contour.neg';

Integer_VI:		Integer;
Float_VI:		Float;
Real_VI:		Real;
Simple_name_VI:		SIMPLE_NAME;

SPACE_VI:		[ \t]+ -> skip;
RETURN_VI:		[\r\n]+;

mode PARAMS_MODE;

End_params:		'<end params>' -> popMode;

Orientation:		'orientation';
Location:		'location';
Size:			'size';
Offset:			'offset';
Scale:			'scale';
Zoom:			'zoom';
Flags_PA:		'flags';

Integer_PA:		Integer;
Float_PA:		Float;
Simple_name_PA:		SIMPLE_NAME;

SPACE_PA:		[ \t]+ -> skip;
RETURN_PA:		[\r\n]+;

mode ORNAMENT_MODE;

L_brakt:		'[' -> pushMode(LABEL_MODE);
End_ornament:		'<end ornament>' -> popMode;

Type_OR:		'type';
Peak:			'peak';
Grid:			'grid';
Color_OR:		'color';
Flags_OR:		'flags';
Id:			'id';
Pos_OR:			'pos';
Height:			'height';
Line_width:		'linewidth';
Integral:		'integral';
Fr:			'fr';
Rs:			'rs';

Rs_ex:			'|' SIMPLE_NAME? ('|' SIMPLE_NAME?)+ '|';

Integer_OR:		Integer;
Float_OR:		Float;
Real_OR:		Real;
Simple_name_OR:		SIMPLE_NAME;

SPACE_OR:		[ \t]+ -> skip;
RETURN_OR:		[\r\n]+;

mode LABEL_MODE;

R_brakt:		']' -> popMode;

Type_LA:		'type';
Label:			'label';
Color_LA:		'color';
Flags_LA:		'flags';
Mode_LA:		'mode';
Pos_LA:			'pos';
Xy:			'xy';

fragment ASS_EACH_AXIS:	SIMPLE_NAME ([:;&/,.] SIMPLE_NAME)*;

Assignment_2d_ex:	ASS_EACH_AXIS '-' ASS_EACH_AXIS;
Assignment_3d_ex:	ASS_EACH_AXIS '-' ASS_EACH_AXIS '-' ASS_EACH_AXIS;
Assignment_4d_ex:	ASS_EACH_AXIS '-' ASS_EACH_AXIS '-' ASS_EACH_AXIS '-' ASS_EACH_AXIS;

Xy_pos:			Float ',' Float;

Integer_LA:		Integer;
Float_LA:		Float;
Simple_name_LA:		SIMPLE_NAME;

SPACE_LA:		[ \t]+ -> skip;
RETURN_LA:		[\r\n]+;

