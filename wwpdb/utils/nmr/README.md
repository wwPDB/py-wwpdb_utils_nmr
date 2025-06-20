﻿# NmrDpUtility - NMR data processing utility for OneDep system

[NmrDpUtility class](NmrDpUtility.py) is backend tool of OneDep system utilized for NMR deposition and validation. It accepts a coordinate file and various NMR data files, and generates combined NMR data file in either NEF or NMR-STAR format. Data processing status is reported through a JSON file. The software package can run outside of the OneDep system, called as standalone mode, for which see [instruction](#standalone-mode) for details.

## How to use

1. Instantiate NmrDpUtility class

```python
try:
    from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility  # OneDep system environment
except ImportError:
    from nmr.NmrDpUtility import NmrDpUtility  # Standalone mode

    util = NmrDpUtility()
```

2. Set primary NMR data source file and log file path (when you already have unified NMR data file in NEF or NMR-STAR format)

NmrDpUtility accepts unified NMR data file as primary data source by default. The unified NMR data file must contain assigned chemical shifts and restraints in a file. The validation results for the data source is reported into designated log file.

```python
    data_dir_path = 'wwpdb/utils/tests-nmr/mock-data/'
    entry_id = '2l9r'
    util.setSource(data_dir_path + entry_id + '.nef')  # primary data source must be unified NMR data
    util.setLog(data_dir_path + entry_id + '-nef-consistency-log.json')
    util.op('nmr-nef-consistency-check')
```
where **setSource()** and **setLog()** are methods to add unified NMR data file and log file. The last **op()** runs designated tasks. The other source files, such as coordinate file, chemical shift files, and restraint files, should be set through the following method. NmrDpUtility supports combining assigned chemical shifts and NMR restraints into single NMR data file.

3. Add input file path and parameters

Any input file paths and parameters should be set through **addInput()** method:

```python
   def addInput(self, name=None, value=None, type='file')
```

The **name** argument should be chosen from effective names shown in a table below, and the **type** argument should be chosen from (`param`, `file`, `file_list`, and `file_dict_list`). At first, 'param' is used to set a named parameter, Next, `file` and `file_list` are used to specify single file path and multiple file paths respectively, whereas their file types are automatically decided by the **name**. For example, `pdbx` for coordinate file and `nmr-star` for chemical shift file(s). Finally, `file_dict_list` indicates **value** is a list of dictionary,
```python
    {'file_name': ?, 'file_type': ?, 'original_file_name' (optional): ?}
```
, and used to set multiple file paths with each file type and optionally the author provided original file name.

name|type|description
----|--------------|-----------
`coordinate_file_path`|`file`|Set a PDBx/mmCIF coordinate file. The file type is `pdbx` by default.
`proc_coord_file_path`|`file`|Set spare coordinate file for the case `coordinate_file_path` is not accessible. Otherwise, it is **unnecessary**,
`chem_shift_file_path_list`|`file_list`, `file_dict_list`|Set chemical shift file(s), formally we accepted multiple chemical shift files. The file type is `nmr-star`.
`restraint_file_path_list`|`file_list`, `file_dict_list`|Set NMR restraint files in NMR-STAR format so that the file type is `nmr-star`.
`atypical_restraint_file_path_list`|`file_dict_list`|Set software-native formatted NMR restraint files or spectral peak list files. The file types are set by the dictionary as described above. `ignore_error': bool value can be set in `file_dict_list` to ignore the file when syntac error occurs.
`atypical_chem_shift_file_path_list`|`file_dict_list`|Set software-native formatted chemical shift files. NOTE: used for standalone NMR data conversion service
`report_file_path`|`file`|Set input report file path of generated by the previous data checking task (`cs-mr-merge`, `nmr-nef-consistency-check`, `nmr-str-consistency-check`, `nmr-cs-nef-consistency-check`, `nmr-cs-str-consistency-check`).
`nmr_cif_file_path`|`file`|Set CIF formatted NMR unified data file path. NOTE: used for BMRB internal processing.
`nmrif_file_path`|`file`|Set CIF formatted NMR metadata (aka. NMRIF) file path. NOTE: used only for OneDep workflow (`nmr-if-merge-merge-deposit`)
`remediation`|`param`|Boolean value. True for legacy separated data file deposition. False for native NMR unified data file deposition.
`internal`|`param`|Boolean value. Set internal mode. NOTE: used for internal only.
`bmrb_only`|`param`|Boolean value. Set BMRB only mode. NOTE: used for BMRB only.
`bmrb_id`|`param`|Set BMRB ID. NOTE: used for BMRB only.
`merge_any_pk_as_is`|`param`|Boolean value. True until NMR data remediation (Phase 2). NOTE: used only for OneDep workflow
`nonblk_anomalous_cs`|`param`|Boolean value. True for OneDep system because any anomalous chemical shift values should not be blocker.
`nonblk_bad_nterm`|`param`|Boolean value. True for OneDep system because biocurator can handle atom name inconsistency of N-terminus residue.
`update_poly_seq`|`param`|Boolean value. True for OneDep system.
`resolve_conflict`|`param`|Boolean value. True for OneDep system.
`check_mandatory_tag`|`param`|Boolean value. True for OneDep system.
`check_auth_seq`|`param`|Boolean value. False for OneDep system.
`validation_server`|`param`|Boolean value. False for OneDep system. True for standalone validation server.
`conversion_server`|`param`|Boolean value, False for OneDep system. True for standalone NMR data conversion server.
`transl_pseudo_name`|`param`|Boolean value. False for OneDep system. Whether to convert pseudo atom nomenclature in NMR unified data file.
`tolerant_seq_align`|`param`|Boolean value. Set True for `nmr-str-consistency-check`, `nmr-str2str-deposit`, `nmr-str2cif-deposit`, `nmr-str2nef-release`, and `nmr-str2cif-annotate` workflow operations. Whether to ignore sequence alignment error due to residue variant.
`fix_format_issue`|`param`|Boolean value. True for legacy separated file data file deposition or release mode.
`excl_missing_data`|`param`|Boolean value. True for legacy separated file data file deposition. Whether to exclude missing mandatory data.
`cmpl_missing_data`|`param`|Boolean value. True for legacy separated file data file deposition. Whether to complement missing data. (add missing pseudo atoms in NMR restraints in actual)
`trust_pdbx_nmr_ens`|`param`|Boolean value. True for release mode. Whether to trust pdbx_nmr_ensemble to get total number of models.
`rmsd_not_superimposed`|`param`|Positive floating-point value. Criterion for detection of not superimposed model. (default value is 2.0 Å)
`rmsd_overlaid_exactly`|`param`|Positive floating-potnt value. Criterion for detection of exactly overlaid models. (default value is 0.01 Å)

4. Add primary output file path, other output file path and parameters

NmrDpUtility outputs processed primary input data source set by **setSource()** as primary output file, which is specified by **setDestination()** method. When you select NEF as the input resource, the primary output should be converted NEF file. The other output file paths (e.g. NMR-STAR and CIF formatted NMR-STAR) and parameters should be set through **addOutput()** method:

```python
    def addOutput(self, name=None, value=None, type='file')
```

The argument **name** should be chosen from effective names shown in a table below, and the **type** argument should be chosen from (`param` and `file`). At first, `param` is used to set a named parameter, Next, `file` is used to specify output file path.

name|type|description
----|--------------|-----------
`nmr_cif_file_path`|`file`|Set CIF formatted NMR-STAR unified data file. Effective in `nmr-nef2cif-deposit`, `nmr-str2cif-deposit`, and `nmr-str2cif-annotate` workflow operations.
`nmr-star_file_path`|`file`|Set NMR-STAR unified data file. Effective in `nmr-nef2str-deposit`, and `nmr-nef2cif-deposit` workflow operations.
`nmrif_file_path`|`file`|Set CIF formatted NMR metadata (aka. NMRIF) file path. NOTE: used only for OneDep workflows (`nmr-cs-mr-merge`, `nmr-str2str-deposit`, and `nmr-str2cif-deposit`, `nmr-nef2str-deposit`, `nmr-nef2cif-deposit`)
`report_file_path`|`file`|Set auxiliary report file path when setLog() is occupied for the previous main task.
`entry_id`|`param`|Set entry ID. (default value is extracted from coordinate file if available, otherwise, 'UNNAMED')
`retain_original`|`param`|Boolean value. True by default. Whether to retain original content if possible.
`leave_intl_note`|`param`|Boolean value. True by default. Whether to leave internal commentary note in processed NMR-STAR file.
`reduced_atom_notation`|`param`|Boolean value. True by default. Whether to use reduced atom notation in warning/error message.

5. Invoke defined workflow operation

After the input and output resources are complete, calling **op()** for a particular workflow operation performs a series of data processing.

workflow operation|role|primary output file(s) and its file path API
------------------|----|-----------------------------------------
`nmr-nef-consistency-check`|Validate NEF file|Report file: **addOutput('`report_file_path`', '`file`', file_path)**
`nmr-str-consistency-check`|Validate NMR-STAR file|Report file: **addOutput('`report_file_path`', '`file`', file_path)**
`nmr-nef2str-deposit`|Convert NEF file to NMR-STAR file|NMR-STAR file: **addOutput('`report_file_path`', '`file`', file_path)**
`nmr-nef2cif-deposit`|Convert NEF file to NMR-STAR and generate CIF formatted NMR-STAR file for OneDep system|NMR-STAR file: **setDestination(file_path)**,<br />CIF formatted NMR-STAR file: **addOutput('`nmr_cif_file_path`', '`file`', file_path)**
`nmr-str2str-deposit`|Convert NMR-STAR file|NMR-STAR file: **setDestination(file_path)**
`nmr-str2cif-deposit`|Convert NMR-STAR file and generate CIF formatted NMR-STAR file for OneDep system|NMR-STAR file: **setDestination(file_path)**,<br />CIF formatted NMR-STAR file: **addOutput('`nmr_cif_file_path`', '`file`', file_path)**
`nmr-str2nef-release`|Convert NMR-STAR file to NEF file for OneDep release module.|NEF file: **setDestination(file_path)**
`nmr-cs-nef-consistency-check`|**Deprecated.**|Report file: **addOutput('`report_file_path`', '`file`', file_path)**
`nmr-cs-str-consistency-check`|**Deprecated.**|Report file: **addOutput('`report_file_path`', '`file`', file_path)**
`nmr-cs-mr-merge`|Combine assigned chemical shifts and NMR restraints. Optionally, validate spectral peak lists and insert them as raw text data using `_Spectral_peak_list.Text_data` tag, otherwise convert them using regular NMR-STAR loops and tags|NMR-STAR file: **setDestination(file_path)**,<br />CIF formatted NMR-STAR file: **addOutput('`nmr_cif_file_path`', '`file`', file_path)**
`nmr-str2cif-annotate`|OneDep system only, Update NMR-STAR file based on annotated model file|CIF formatted NMR-STAR file: **addOutput('`nmr_cif_file_path`', '`file`', file_path)**
`nmr-if-merge-deposit`|Merge available NMR metadata (aka. NMRIF) to NMR-STAR file|CIF formatted NMR-STAR file: **addOutput('`nmr_cif_file_path`', '`file`', file_path)**

## Typical workflow operations

As of now, OneDep supports (a) single NMR data file deposition using NMR unified data file in NEF or NMR-STAR and (b) conventional separated NMR data file deposition requiring assigned chemical shift file and set of NMR restraint files.

### (a) Single NMR data file deposition

At first, NMR unified data file must be validated and cross-checked by given coordinate file. Then, file conversion workflow will follow where report file generated by data checking workflow is required as input source.

For example, NEF to CIF formatted NMR-STAR file conversion

```python
    util.setSource(data_dir_path + entry_id + '.nef)
    util.addInput(name='coordinate_file_path', value=data_dir_path + entry_id + '.cif', type='file')
    util.addInput(name='nonblk_anomalous_cs', value=True, type='param')
    util.addInput(name='nonblk_bad_nterm', value=True, type='param')
    util.addInput(name='resolve_conflict', value=True, type='param')
    util.addInput(name='check_mandatory_tag', value=True, type='param')
    util.setLog(data_dir_path + entry_id + '-nef-consistency-log.json')  # this report file is reused in successive data conversion workflow
    util.setVerbose(False)

    util.op('nmr-nef-consistency-check')

    util.setSource(data_dir_path + entry_id + '.nef)
    util.addInput(name='coordinate_file_path', value=data_dir_path + entry_id + '.cif', type='file')
    util.addInput(name='report_file_path', value=data_dir_path + entry_id '-nef-consistency-log.json', type='file')  # take report file of the 'nmr-nef-consistency-check' workflow operation
    util.addInput(name='nonblk_anomalous_cs', value=True, type='param')
    util.addInput(name='nonblk_bad_nterm', value=True, type='param')
    util.addInput(name='resolve_conflict', value=True, type='param')
    util.addInput(name='check_mandatory_tag', value=True, type='param')
    util.setLog(data_dir_path + entry_id '-nef2cif-deposit-log.json')  # report file for data conversion
    util.setDestination(data_dir_path + entry_id '-next.nef')  # the primary destination is the converted NEF file of the original data source
    util.addOutput(name='nmr-star_file_path', value=data_dir_path + entry + '-nef2cif.str', type='file')  # converted NMR-STAR file
    util.addOutput(name='nmr_cif_file_path', value=data_dir_path + entry_id + '-nef2cif.cif', type='file')  # converted CIF formatted NMR-STAR file
    util.addOutput(name='report_file_path', value=data_dir_path + entry_id + '-nef2cif-str-deposit-log.json', type='file')  # report file for the obtained NMR-STAR file
    util.addOutput(name='entry_id', value=entry_id, type='param')
    util.addOutput(name='leave_intl_note', value=False, type='param')
    util.setVerbose(False)

    util.op('nmr-nef2cif-deposit')
```

As for NMR-STAR (NMR unified data) to CIF formatted NMR-STAR file conversion

```python
    util.setSource(data_dir_path + entry_id + '.str)
    util.addInput(name='coordinate_file_path', value=data_dir_path + entry_id + '.cif', type='file')
    util.addInput(name='nonblk_anomalous_cs', value=True, type='param')
    util.addInput(name='nonblk_bad_nterm', value=True, type='param')
    util.addInput(name='resolve_conflict', value=True, type='param')
    util.addInput(name='check_mandatory_tag', value=True, type='param')
    util.setLog(data_dir_path + entry_id + '-str-consistency-log.json')  # this report file is reused in successive data conversion workflow
    util.setVerbose(False)

    util.op('nmr-str-consistency-check')

    util.setSource(data_dir_path + entry_id + '.str)
    util.addInput(name='coordinate_file_path', value=data_dir_path + entry_id + '.cif', type='file')
    util.addInput(name='report_file_path', value=data_dir_path + entry_id '-str-consistency-log.json', type='file')  # take report file of the 'nmr-str-consistency-check' workflow operation
    util.addInput(name='nonblk_anomalous_cs', value=True, type='param')
    util.addInput(name='nonblk_bad_nterm', value=True, type='param')
    util.addInput(name='resolve_conflict', value=True, type='param')
    util.addInput(name='check_mandatory_tag', value=True, type='param')
    util.setLog(data_dir_path + entry_id '-str2cif-deposit-log.json')  # report file for data conversion
    util.setDestination(data_dir_path + entry_id '-next.str')  # the primary destination is the converted NMR-STAR file of the original data source
    util.addOutput(name='nmr_cif_file_path', value=data_dir_path + entry_id + '-str2cif.cif', type='file')  # converted CIF formatted NMR-STAR file
    util.addOutput(name='report_file_path', value=data_dir_path + entry_id + '-str2cif-str-deposit-log.json', type='file')  # report file for the obtained NMR-STAR file
    util.addOutput(name='entry_id', value=entry_id, type='param')
    util.addOutput(name='leave_intl_note', value=False, type='param')
    util.setVerbose(False)

    util.op('nmr-str2cif-deposit')
```

### (b) Separated NMR data file deposition

Conventional NMR deposition requires assigned chemical shift file and software native formatted restraint files. The OneDep system can combine these NMR data into an NMR unified data file that is achived by running `nmr-cs-mr-merge` workflow operation.

```python
    model_file_path = 'D_1000259961_model-upload_P1.cif.V1'
    cs_path_list = [{'file_name': 'D_1000259961_cs-upload_P1.str.V1', 'file_type': 'nmr-star', 'original_file_name': 'TGM1D3.str'}]
    mr_file_type = ['nm-res-xpl', 'nm-res-xpl', 'nm-res-xpl', 'nm-res-xpl', 'nm-res-xpl']
    mr_file_path = ['HBDA-5.tbl', 'jhnhacoup3.tbl', 'tgmd3_rdc_caco_ave_v3.tbl', 'tgmd3_rdc_caha_ave_v4.tbl', 'tgmd3_rdc_nh_CHB.tbl']
    ar_path_list = []
    for i, ar_path in enumerate(mr_file_path):
        ar_path_list.append({'file_name': data_dir_path + ar_path, 'file_type': mr_file_type[i], 'original_file_name': ar_path})

    util.addInput(name='chem_shift_file_path_list', value=cs_path_list, type='file_dict_list')
    util.addInput(name='atypical_restraint_file_path_list', value=ar_path_list, type='file_dict_list')
    util.addInput(name='coordinate_file_path', value=data_dir_path + model_file_path, type='file')
    util.addInput(name='nonblk_anomalous_cs', value=True, type='param')
    util.addInput(name='nonblk_bad_nterm', value=True, type='param')
    util.addInput(name='resolve_conflict', value=True, type='param')
    util.addInput(name='check_mandatory_tag', value=False, type='param')
    util.addInput(name='remediation', value=True, type='param')  # turn on remediation mode
    util.setLog(data_dir_path + entry_id + '-cs-str-consistency-log.json')
    util.setDestination(data_dir_path + entry_id + '_cs_mr_merged.str')  # combined NMR-STAR file
    util.setVerbose(False)

    util.op('nmr-cs-mr-merge')
```

The result combined NMR-STAR file will be validated as if NMR unified data file deposition by the following `nmr-str-consistency-check` and `nmr-str2cif-deposit` workflow operations. Please note that the `atypical_restraint_file_path_list` argument accepcts any software-native restraints and spectral peak lists in supported software native formats except for NMR-STAR format and use the `restraint_file_path_list` argument to incorporate restraints and spectral peak lists in NMR-STAR format. The usage of `restraint_file_path_list` and `atypical_restraint_file_path_list` is the same.

NmrDpUtility class can absorb differences between NMR-STAR file and CIF formatted NMR-STAR file so that you can directly use the CIF formatted NMR-STAR file as input resource file. To get **CIF formatted NMR-STAR** file as output, please append output file path with name `nmr_cif_file_path` as follows.

```python
    util.addOutput(name='nmr_cif_file_path', value=path_to_pdbx_nmr_data_file, type='file')
```

### Support for Stereo-Array Isotope Labeling (SAIL)

NmrDpUtility class can notice the Stereo Array Isotope Labeling (SAIL) method. This is a trigger that prevents to generate atom names in the same atom group from fanning out for a given atom name. To turn off fan-out mode, you must add one of the following metadata to your upload file. Here are four cases (a, b, c, and d):

- NMR-STAR
	- 1. Create `_Systematic_chem_shift_offset` loop in `_Assiged_chem_shift_list` saveframe and set proper description in `_Systematic_chem_shift_offset.Type` data item
	- 2. Create '_Sample_component' loop in `_Sample` saveframe and set proper description in `_Sample_component.Isotopic_labeling` data item for target entity
For example,
```
    _Systematic_chem_shift_offset.Type 'stereo-array isotope labeling'
    _Systematic_chem_shift_offset.Type SAIL
    _Sample_component.Isotopic_labeling 'stereo-array isotope labeling'
    _Sample_component.Isotopic_labeling SAIL
```
- PDBx/mmCIF (coordinates)
	- 3. Add proper description in `_struct_keywords.text` data item
	- 4. Set proper description in `_pdbx_nmr_exptl_sample.isotopic_labeling` data item for target entity
For example,
```
    _struct_keywords.text 'stereo-array isotope labeling'
    _struct_keywords.text SAIL
    _pdbx_nmr_exptl_sample.isotopic_labeling 'stereo-array isotope labeling'
    _pdbx_nmr_exptl_sample.isotopic_labeling SAIL
```

## Schema of NMR data processing report file

[NmrDpReport class](NmrDpReport.py) handles writing and reading the report file. Document structure of the report file is defined in [JSON Schema file](../tests-nmr/json-schema/nmr-data-procesing-report-schema-v4.json).

## Standalone mode

### Requirements

- python 3.6 or later

- pip packages:
	- pynmrstar (3.2.0 or later)
	- wwpdb.utils.align
	- munkres
	- mmcif
	- numpy
	- packaging
	- rmsd
	- chardet
	- scikit-learn
	- antlr4-python3-runtime
	- typing_extensions
	- striprtf
	- datetime

- If your Python version is less than 3.10, downgrade urllib3 from v2 to v1. Otherwise, [the urllib3 v2 requires OpenSSL 1.1.1+](https://github.com/urllib3/urllib3/issues/2168).
```bash
    pip install urllib3==1.26.18  # Only for Python 3.6, 3.7, 3.8, and 3.9 users.
```

### How to set up

1. Set enviromnent variable PYTHONPATH
```bash
    export PYTHONPATH=$PYTHONPATH:(path to wwpdb/utils)  # Required only the first time.
```

2. Update CCD periodically
```bash
    cd wwpdb/utils/nmr ; ./update_ccd.sh ; ./deploy_ccd.sh  # You must run this command every Wednesday UTC+00:00.
```

3. Test importing modules
```python
    from nmr.NmrDpUtility import NmrDpUtility
```

4. Run unit tests in wwpdb/utils/tests-nmr
```bash
   python test_ChemCompUtil.py
   python test_BMRBChemShiftStat.py  # Run twice test_BMRBChemShiftStat.py just in case.
```

## Appendix

The codes used for specifying each file type in NmrDpUtility are compatible with OneDep system as follows:

NmrDpUtility|OneDep&nbsp;(DepUI)|OneDep (content type / format)|description
------------|--------------|----------------------------|-----------
`nmr-star`|`nm-shi`,<br/>`nm-uni-str`|`nmr-chemical-shifts` / `nmr-star`,<br/>`nmr-data-str` / `nmr-star`|NMR data file in NMR-STAR format
`nef`|`nm-uni-nef`|`nmr-data-nef` / `nmr-star`|NMR data file in NEF (NMR Exchange Format)
`pdbx`|`co-cif`|`model` / `pdbx`|Coordinates file in PDBx/mmCIF format
`nm-aux-amb`|`nm-aux-amb`|`nmr-restraints` / `any`|Topology file in AMBER format
`nm-res-amb`|`nm-res-amb`|`nmr-restraints` / `amber`|Restraint file in AMBER format
`nm-res-ari`|`nm-res-ari`|`nmr-restraints` / `aria`|Restraint file in ARIA format
`nm-res-bio`|`nm-res-bio`|`nmr-restraints` / `biosym`|Restraint file in BIOSYM format
`nm-aux-cha`|`nm-aux-cha`|`nmr-restraints` / `any`|Topology file in CHARMM format (aka. CHARMM extended CRD)
`nm-res-cha`|`nm-res-cha`|`nmr-restraints` / `charmm`|Restraint file in CHARMM format
`nm-res-cns`|`nm-res-cns`|`nmr-restraints` / `cns`|Restraint file in CNS format
`nm-res-cya`|`nm-res-cya`|`nmr-restraints` / `cyana`|Restraint file in CYANA format
`nm-res-dyn`|`nm-res-dyn`|`nmr-restraints` / `dynamo`|Restraint file in DYNAMO/PALES/TALOS format
`nm-aux-gro`|`nm-aux-gro`|`nmr-restraints` / `any`|Topology file in GROMACS format
`nm-res-gro`|`nm-res-gro`|`nmr-restraints` / `gromacs`|Restraint file in GROMACS format
`nm-res-isd`|`nm-res-isd`|`nmr-restraints` / `isd`|Restraint file in ISD format
`nm-res-noa`|`nm-res-cya`,<br/>`nm-res-oth`|`nmr-restraints` / `cyana`|Restraint file in CYANA NOA format
`nm-res-ros`|`nm-res-ros`|`nmr-restraints` / `rosetta`|Restraint file in ROSETTA format
`nm-res-syb`|`nm-res-syb`|`nmr-restraints` / `sybyl`|Restraint file in SYBYL format
`nm-res-xpl`|`nm-res-xpl`|`nmr-restraints` / `xplor-nih`|Restraint file in XPLOR-NIH format
`nm-res-oth`|`nm-res-oth`|`nmr-restraints` / `any`|Restraint file in other format
`nm-res-mr`|**internal use**|`nmr-restraints` / `pdb-mr`|Restraint file in PDB-MR format
`nm-res-sax`|**internal use**|`nmr-restraints` / `any`|SAX CSV file
`nm-pea-ari`|`nm-pea-any`|`nmr-peaks` / `any`|Spectral peak list file in ARIA format
`nm-pea-bar`|**internal use**|`nmr-peaks` / `any`|Bare WSV/TSV spectral peak list file with a header
`nm-pea-ccp`|`nm-pea-any`|`nmr-peaks` / `any`|Spectral peak list file in CCPN format
`nm-pea-pip`|`nm-pea-any`|`nmr-peaks` / `any`|Spectral peak list file in NMRPIPE/PIPP format
`nm-pea-pon`|`nm-pea-any`|`nmr-peaks` / `any`|Spectral peak list file in PONDEROSA format
`nm-pea-spa`|`nm-pea-any`|`nmr-peaks` / `any`|Spectral peak list file in SPARKY format
`nm-pea-sps`|`nm-pea-any`|`nmr-peaks` / `any`|Spectral peak list file in SPARKY's `save` format (aka. ornament)
`nm-pea-top`|`nm-pea-any`|`nmr-peaks` / `any`|Spectral peak list file in TOPSPIN format
`nm-pea-vie`|`nm-pea-any`|`nmr-peaks` / `any`|Spectral peak list file in NMRVIEW format
`nm-pea-vnm`|`nm-pea-any`|`nmr-peaks` / `any`|Spectral peak list file in VNMR format
`nm-aux-xea`|`nm-pea-any`|`nmr-peaks` / `any`|Assignment file in XEASY format (aka. XEASY PROT)
`nm-pea-xea`|`nm-pea-any`|`nmr-peaks` / `any`|Spectral peak list file in XEASY format
`nm-pea-xwi`|`nm-pea-any`|`nmr-peaks` / `any`|Spectral peak list file in XWINNMR format
`nm-pea-any`|`nm-pea-any`|`nmr-peaks` / `any`|Any spectral peak list file
`nmrif`|**internal use**|`nmrif` / `pdbx`|NMR metadata file in PDBx/mmCIF format (aka. NMRIF)
`nm-shi-ari`|**internal use**|`nmr-chemical-shifts` / `any`|ARIA chemical shift file
`nm-shi-bar`|**internal use**|`nmr-chemical-shifts` / `any`|Bare WSV/TSV/CSV chemical shift file (residue per line, atom per line, SPARKY's resonance list)
`nm-shi-gar`|**internal use**|`nmr-chemical-shifts` / `any`|GARRET chemical shift file (CAMRA)
`nm-shi-npi`|**internal use**|`nmr-chemical-shifts` / `any`|NMRPIPE chemical shift file
`nm-shi-pip`|**internal use**|`nmr-chemical-shifts` / `any`|PIPP chemical shift file
`nm-shi-ppm`|**internal use**|`nmr-chemical-shifts` / `any`|PPM chemical shift file (NMRVIEW, CAMRA)
`nm-shi-st2`|**internal use**|`nmr-chemical-shifts` / `any`|NMR-STAR V2.1 chemical shift file (loop only)
`nm-shi-xea`|**internal use**|`nmr-chemical-shifts` / `any`|XEASY chemical shift file same as `nm-aux-xea`
