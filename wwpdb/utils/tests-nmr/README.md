# How to set up standalone mode for wwpdb.utils.nmr package

## Requirements
- python 3.6 or later

- pip packages to be installed:
	- wwpdb.utils.align
	- pynmrstar
	- munkres
	- mmcif
	- numpy
	- packaging
	- rmsd
	- chardet
	- scikit-learn
	- antlr4-python3-runtime
	- typing_extensions

- linux commands:
	- aria2c

## How to set up
- 1. Set path of PYTHONPATH.
```bash
    export PYTHONPATH=$PYTHONPATH:(path to wwpdb/utils)  # Required only the first time.
```

- 2. Update CCD periodically.
```bash
    cd wwpdb/utils/nmr ; ./update_ccd.sh ; ./deploy_ccd.sh  # You must run this command every Wednesday UTC+00:00.
```

- 3. Run unit tests in wwpdb/utils/tests-nmr

