/*
 GROMACS PT (Parameter Topology) parser grammar for ANTLR v4.
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

parser grammar GromacsPTParser;

options { tokenVocab=GromacsPTLexer; }

gromacs_pt:
	(
	default_statement |
	moleculetype_statement |
	atoms_statement |
	bonds_statement |
	pairs_statement |
	pairs_nb_statement |
	angles_statement |
	dihedrals_statement |
	exclusions_statement |
	constraints_statement |
	settles_statement |
	virtual_sites1_statement |
	virtual_sites2_statement |
	virtual_sites3_statement |
	virtual_sites4_statement |
	virtual_sitesn_statement |
	system_statement |
	molecules_statement
	)*
	EOF;

/* GROMACS 2022.1 Referece Manual - Topology
 See also https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html
*/
default_statement:
	L_brkt Default R_brkt
	Integer Integer Simple_name Float Float;	// nbfunc comb-rule gen-pairs fudgeLJ fudgeQQ

moleculetype_statement:
	L_brkt Moleculetype R_brkt
	moleculetype+;

moleculetype:
	Simple_name Integer;				// name nrexcl

atoms_statement:
	L_brkt Atoms R_brkt
	atoms+;

atoms:
	Integer Simple_name Integer Simple_name Simple_name
	Integer number (number (Simple_name number number)?)?;
							// nr type resnr residu atom cgnr charge (mass) (typeB) (chargeB) (massB)

bonds_statement:
	L_brkt Bonds R_brkt
	bonds*;

bonds:
	Integer Integer Integer (number number number?)?;
							// ai aj funct c{0,2,3}

pairs_statement:
	L_brkt Pairs R_brkt
	pairs*;

pairs:
	Integer Integer Integer number number (number number number)?;
							// ai aj funct c{2,5}

pairs_nb_statement:
	L_brkt Pairs_nb R_brkt
	pairs_nb*;

pairs_nb:
	Integer Integer Integer number number number number;
							// ai aj funct qi, qj, V, W

angles_statement:
	L_brkt Angles R_brkt
	angles*;

angles:
	Integer Integer Integer Integer number number
	(number (number (number number)?)?)?;		// ai aj ak funct c{2,3,4,6}

dihedrals_statement:
	L_brkt Dihedrals R_brkt
	dihedrals*;

dihedrals:
	Integer Integer Integer Integer Integer number number
	(number (number number number?)?)?;		// ai aj ak al funct c{2,3,5,6}

exclusions_statement:
	L_brkt Exclusions R_brkt
	exclusions*;

exclusions:
	Integer Integer+;				// ai a{1,}

constraints_statement:
	L_brkt Constraints R_brkt
	constraints*;

constraints:
	Integer Integer Integer number;			// ai aj funct b0

settles_statement:
	L_brkt Settles R_brkt
	settles*;

settles:
	Integer Integer number number;			// ai funct dsc_oh dsc_hh

virtual_sites1_statement:
	L_brkt Virtual_sites1 R_brkt
	virtual_sites1*;

virtual_sites1:
	Integer Integer Integer;			// ai aj funct

virtual_sites2_statement:
	L_brkt Virtual_sites2 R_brkt
	virtual_sites2*;

virtual_sites2:
	Integer Integer Integer Integer number;		// ai aj ak funct c

virtual_sites3_statement:
	L_brkt Virtual_sites3 R_brkt
	virtual_sites3*;

virtual_sites3:
	Integer Integer Integer Integer Integer
	number number number?;				// ai aj ak aj funct c{2,3}

virtual_sites4_statement:
	L_brkt Virtual_sites4 R_brkt
	virtual_sites4*;

virtual_sites4:
	Integer Integer Integer Integer Integer Integer
	number number number;				// ai aj ak aj al funct a b c

virtual_sitesn_statement:
	L_brkt Virtual_sitesn R_brkt
	virtual_sitesn*;

virtual_sitesn:
	Integer Integer Integer+ number?;		// ai funct a{1:} w?

system_statement:
	L_brkt System R_brkt_A
	Simple_name_A* RETURN_A;

molecules_statement:
	L_brkt Molecules R_brkt
	molecules+;

molecules:
	Simple_name Integer;				// name number

/* number expression in restrains */
number:	Float | Integer;

