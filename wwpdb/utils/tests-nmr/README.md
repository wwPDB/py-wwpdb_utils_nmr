# How to set up standalone mode for wwpdb.utils.nmr package

## Requirements
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

- If your Python version is less than 3.10, downgrade urllib3 from v2 to v1. Otherwise, [the urllib3 v2 requires OpenSSL 1.1.1+](https://github.com/urllib3/urllib3/issues/2168).
```bash
    pip install urllib3==1.26.18  # Only for Python 3.6, 3.7, 3.8, and 3.9 users.
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

