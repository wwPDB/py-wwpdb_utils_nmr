/*
 GROMACS MR (Magnetic Restraint) parser grammar for ANTLR v4.
 Copyright 2022 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

parser grammar GromacsMRParser;

options { tokenVocab=GromacsMRLexer; }

gromacs_mr:
	(
	distance_restraints |
	dihedral_restraints |
	orientation_restraints |
	angle_restraints |
	angle_restraints_z |
	position_restraints |
	L_brkt Intermolecular_interactions R_brkt
	)*
	EOF;

/* GROMACS 2022.1 Referece Manual - Distance restraints
 See also https://manual.gromacs.org/documentation/current/reference-manual/functions/restraints.html#distance-restraints
          https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
distance_restraints:
	L_brkt Distance_restraints R_brkt
	distance_restraint+;

distance_restraint:
	Integer Integer Integer Integer Integer number number number number
							// ai aj funct=1 index type low up1 up2 kfac
	Simple_name?;

/* GROMACS 2022.1 Referece Manual - Dihedral restraints
 See also https://manual.gromacs.org/documentation/current/reference-manual/functions/restraints.html#dihedral-restraints
          https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
dihedral_restraints:
	L_brkt Dihedral_restraints R_brkt
	dihedral_restraint+;

dihedral_restraint:
	Integer Integer Integer Integer Integer number number number
							// ai aj ak al funct=1 phi0 dphi kd
	Simple_name?;

/* GROMACS 2022.1 Referece Manual - Orientation restraints
 See also https://manual.gromacs.org/documentation/current/reference-manual/functions/restraints.html#orientation-restraints
          https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
orientation_restraints:
	L_brkt Orientation_restraints R_brkt
	orientation_restraint+;

orientation_restraint:
	Integer Integer Integer Integer Integer number number number number
							// ai aj funct=1 exp index alpha const obs weight
	Simple_name?;

/* GROMACS 2022.1 Referece Manual - Angle restraints
 See also https://manual.gromacs.org/documentation/current/reference-manual/functions/restraints.html#angle-restraints
          https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
angle_restraints:
	L_brkt Angle_restraints R_brkt
	angle_restraint+;

angle_restraint:
	Integer Integer Integer Integer Integer number number Integer
							// ai aj ak al funct=1 theta0 kc mult
	Simple_name?;

angle_restraints_z:
	L_brkt Angle_restraints_z R_brkt
	angle_restraint_z+;

angle_restraint_z:
	Integer Integer Integer number number Integer	// ai aj funct=1 theta0 kc mult
	Simple_name?;

/* GROMACS 2022.1 Referece Manual - Position restraints
 See also https://manual.gromacs.org/documentation/current/reference-manual/functions/restraints.html#position-restraints
          https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
position_restraints:
	L_brkt Position_restraints R_brkt
	position_restraint+;

position_restraint:
	Integer Integer number number number		// ai funct=1 kx ky kz
							// ai funct=2 g r k
	Simple_name?;

/* number expression in restrains */
number:	Float | Integer;

