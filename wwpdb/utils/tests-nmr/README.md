# How to set up standalone mode for wwpdb.utils.nmr package

## Requirements
- python 3.6 or later

- pip packages:
	- pynmrstar (3.2.0 or later)
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

- If your Python version is less than 3.10, downgrade urllib3 from v2 to v1. Otherwise, [the urllib3 v2 requires OpenSSL 1.1.1+](https://github.com/urllib3/urllib3/issues/2168).
```bash
    pip install urllib3==1.26.18  # Only for Python 3.6, 3.7, 3.8, and 3.9 users.
```

- shared library:
	- wwpdb/utils/nmr/align/alignlib.so, a shared library of [py-wwpdb_utils_align](https://github.com/wwPDB/py-wwpdb_utils_align) package
	- Python 3.6, 3.7, and 3.8 compatible shared libraries are included by default.
	  	- Python 3.6 users must link alignlib.cpython-36m-x86_64-linux-gnu.so to alignlib.so
	  	- Python 3.7 users must link alignlib.cpython-37m-x86_64-linux-gnu.so to alignlib.so
	  	- Python 3.8 users must link alignlib.cpython-38-x86_64-linux-gnu.so to alignlib.so (default)
	- For other environments, the shared library is avaialble by following instuctions:
	```bash
		cd py-wwpdb_utils_nmr/wwpdb/utils/nmr/align
		pip install wwpdb.utils.align
		cp ~/.pyenv/versions/3.x.y/lib/python3.x/site-packages/wwpdb/utils/align/alignlib.cpython-3x-x86_64-linux-gnu.so .  # Please replace 'x' and 'y' with proper digits.
		rm -f alignlib.so ; ln -s alignlib.cpython-3x-x86_64-linux-gnu.so alignlib.so  # Please replace 'x' with proper digit.
		pip uninstall wwpdb.utils.align  # Uninstall wwpdb.utils.align package without affecting the standalone mode.
	```

## How to set up
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

Please see [instruction](../nmr/README.md) about NmrDpUtility class for details.

