# How to set up standalone mode for wwpdb.utils.nmr package

## Requirements
- python 3.6 or later

- pip packages to be installed:
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

- linux command:
	- aria2c

- shared library:
	- alignlib.so (locate the shared library in wwpdb/utils/nmr/align) 

## How to set up
1. Set enviromnent variable PYTHONPATH 
```bash
    export PYTHONPATH=$PYTHONPATH:(path to wwpdb/utils)  # Required only the first time.
```

2. Update CCD periodically
```bash
    cd wwpdb/utils/nmr ; ./update_ccd.sh ; ./deploy_ccd.sh  # You must run this command every Wednesday UTC+00:00.
```

3. Import test
```pathon
    from nmr.NmrDpUtility import NmrDpUtility
```

4. Run unit tests in wwpdb/utils/tests-nmr
- Make sure that import path starts with **nmr**, instead of **wwpdb.utils.nmr**.
