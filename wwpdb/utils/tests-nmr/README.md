# How to set up standalone mode for wwpdb.utils.nmr package

## Requirements
- python 3.6 or 3.7

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
	- alignlib.so is a softlink to alignlib.cpython-37m-x86_64-linux-gnu.so by default, Python 3.6 user must use alignlib.cpython-36m-x86_64-linux-gnu.so, instead by editing the softlink.

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
