import sys
import os
import platform

HERE = os.path.abspath(os.path.dirname(__file__))
TOPDIR = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
TESTOUTPUT = os.path.join(HERE, "test-output", platform.python_version())
if not os.path.exists(TESTOUTPUT):
    os.makedirs(TESTOUTPUT)

# We do this here - as unittest loads all at once - need to insure common

try:
    from unittest.mock import Mock, MagicMock
except ImportError:
    from mock import Mock, MagicMock

configInfo = {
    "SITE_REFDATA_PROJ_NAME_CC": "ligand-dict-v3",
    "REFERENCE_PATH": os.path.join(HERE, "data"),
}

configInfoMockConfig = {
    "return_value": configInfo,
}

configMock = MagicMock(**configInfoMockConfig)

# Returns a dictionary by default - which has a get operator
sys.modules["wwpdb.utils.config.ConfigInfo"] = Mock(ConfigInfo=configMock)
