##
# File: NmrVrptUtility.py
# Date: 19-Apr-2023
#
# Updates:
##
""" Wrapper class for NMR restraint validation.
    @author: Masashi Yokochi
    @note: This class is alternative implementation of wwpdb.apps.validation.src.RestraintValidation.BMRBRestraintsAnalysis
"""
import os
import sys
import gzip
import tempfile
import time
import pickle
import copy
from operator import itemgetter
import numpy as np

from mmcif.io.IoAdapterPy import IoAdapterPy

try:
    from wwpdb.utils.nmr.io.CifReader import (CifReader, LEN_MAJOR_ASYM_ID)
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                                       DIST_RESTRAINT_ERROR,
                                                       ANGLE_RESTRAINT_ERROR,
                                                       RDC_RESTRAINT_ERROR,
                                                       coordAssemblyChecker)
    from wwpdb.utils.nmr.AlignUtil import LARGE_ASYM_ID
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
except ImportError:
    from nmr.io.CifReader import (CifReader, LEN_MAJOR_ASYM_ID)
    from nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                           DIST_RESTRAINT_ERROR,
                                           ANGLE_RESTRAINT_ERROR,
                                           RDC_RESTRAINT_ERROR,
                                           coordAssemblyChecker)
    from nmr.AlignUtil import LARGE_ASYM_ID
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat

NMR_VTF_DIST_VIOL_CUTOFF = 0.1
NMR_VTF_DIHED_VIOL_CUTOFF = 1.0
NMR_VTF_DIST_ERR_BINS = (0.1, 0.2, 0.5)
NMR_VTF_DIHED_ERR_BINS = (1.0, 10.0, 20.0)

DIST_ERROR_MAX = DIST_RESTRAINT_ERROR['max_exclusive']
ANGLE_ERROR_MAX = ANGLE_RESTRAINT_ERROR['max_exclusive']
RDC_ERROR_MAX = RDC_RESTRAINT_ERROR['max_exclusive']


def uncompress_gzip_file(inPath, outPath):
    """ Uncompress a given gzip file.
    """

    with gzip.open(inPath, mode='rt') as ifh, open(outPath, 'w') as ofh:
        for line in ifh:
            ofh.write(line)


def load_from_pickle(file_name, default=None):
    """ Load object from pickle file.
    """

    if os.path.exists(file_name):

        with open(file_name, 'rb') as ifh:
            obj = pickle.load(ifh)
            return obj if obj is not None else default

    return default


def write_as_pickle(obj, file_name):
    """ Write a given object as pickle file.
    """

    if obj is not None:

        with open(file_name, 'wb') as ofh:
            pickle.dump(obj, ofh)


def distance(p0, p1):
    """ Return distance between two points.
    """

    return np.linalg.norm(p0 - p1)


def to_unit_vector(a):
    """ Return unit vector of a given vector.
    """

    return a / np.linalg.norm(a)


def dihedral_angle(p0, p1, p2, p3):
    """ Return dihedral angle from a series of four points.
    """

    b0 = -1.0 * (p1 - p0)
    b1 = p2 - p1
    b2 = p3 - p2

    # normalize b1 so that it does not influence magnitude of vector
    # rejections that come next
    b1 = to_unit_vector(b1)

    # vector rejections
    # v = projection of b0 onto plane perpendicular to b1
    #   = b0 minus component that aligns with b1
    # w = projection of b2 onto plane perpendicular to b1
    #   = b2 minus component that aligns with b1
    v = b0 - np.dot(b0, b1) * b1
    w = b2 - np.dot(b2, b1) * b1

    # angle between v and w in a plane is the torsion angle
    # v and w may not be normalized but that's fine since tan is y/x
    x = np.dot(v, w)
    y = np.dot(np.cross(b1, v), w)

    return np.degrees(np.arctan2(y, x))


def dist_inv_6_summed(r_list: [float]) -> float:
    """ Return r^−6-summed distance for a given list of distances for ambiguous restraints as recommended by NMR VTF.
        Reference:
          Calculation of Protein Structures with Ambiguous Distance Restraints. Automated Assignment of
          Ambiguous NOE Crosspeaks and Disulphide Connectivities.
          Michael Nilges.
          J. Mol. Biol. (1995) 245, 645–660.
          DOI: 10.1006/jmbi.1994.0053
        @author: Kumaran Baskaran
        @see: wwpdb.apps.validation.src.RestraintValidation.BMRBRestraintsAnalysis.r6sum
    """

    return sum(r ** (-6.0) for r in r_list) ** (-1.0 / 6.0)


def angle_error(lower_bound, upper_bound, target_value, angle):
    """ Return angle outlier for given lower_bound, upper_bound, and target_value.
        @author: Kumaran Baskaran
        @see: wwpdb.apps.validation.src.RestraintValidation.BMRBRestraintsAnalysis.angle_diff
    """

    def angle_diff(x, y):
        """ Return normalized angular difference.
        """
        if x < 0.0:
            x += 360.0
        if y < 0.0:
            y += 360.0

        a, b = sorted([x, y])

        d = b - a
        if d > 180.0:
            d = 360.0 - d

        return d

    def check_angle_range_overlap(x, y, c, g, t=0.5):
        """ Return whether angular range formed by (x, c) and (c, y) matches to a given range (g) with tolerance (t).
        """
        l = angle_diff(x, c)  # noqa: E741
        r = angle_diff(y, c)

        return abs(g - (l + r)) < t

    ld = angle_diff(lower_bound, target_value)
    rd = angle_diff(upper_bound, target_value)

    if check_angle_range_overlap(lower_bound, target_value, angle, ld, 0.5)\
       or check_angle_range_overlap(upper_bound, target_value, angle, rd, 0.5):
        return 0.0

    return min(angle_diff(upper_bound, angle), angle_diff(lower_bound, angle))


def get_violated_model_ids(viol_per_model):
    return [m for m, err in viol_per_model.items() if err is not None and err > 0.0]


def get_violation_statistics_for_each_bin(beg_err_bin, end_err_bin, total_models, viol_dict):
    viol_stat_per_model = []

    all_err_list = []
    for m in range(1, total_models + 1):
        err_list = []

        for viol_per_model in viol_dict.values():
            err = viol_per_model[m]

            if err is None or err == 0.0:
                continue

            if (end_err_bin is None and beg_err_bin < err)\
               or beg_err_bin < err <= end_err_bin\
               or (beg_err_bin is None and err < end_err_bin):
                err_list.append(err)
                all_err_list.append(err)

        if len(err_list) == 0:
            viol_stat = [None, None, None]
        else:
            viol_stat = [round(min(err_list), 2),
                         round(max(err_list), 2),
                         len(err_list)]

        viol_stat_per_model.append(viol_stat)

    if len(all_err_list) == 0:
        viol_stat_all_model = [None, None, None, None]
    else:
        viol_stat_all_model = [round(min(all_err_list), 2),
                               round(max(all_err_list), 2),
                               len(all_err_list),
                               round(float(len(all_err_list)) / float(total_models), 1)]

    return viol_stat_all_model, viol_stat_per_model


class NmrVrptUtility:
    """ Wrapper class for NMR restraint validation.
    """

    def __init__(self, verbose=False, log=sys.stderr,
                 ccU=None, csStat=None):
        self.__verbose = verbose
        self.__lfh = log

        self.__debug = False

        # auxiliary input resource
        self.__inputParamDict = {}

        # auxiliary output resource
        self.__outputParamDict = {}

        # sub-directory name for cache file
        self.__sub_dir_name_for_cache = 'utils_nmr'

        # CIF file path
        self.__cifPath = None

        # NMR data file path
        self.__nmrDataPath = None

        # current working directory
        self.__dirPath = None

        # directory for cache files
        self.__cacheDirPath = None

        # hash code of the coordinate file
        self.__cifHashCode = None

        # hash code of the NMR data file
        self.__nmrDataHashCode = None

        # cache file name for results
        self.__resultsCacheName = None

        # CIF reader
        self.__cR = None

        # NMR data reader
        self.__rR = None

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat(verbose, log, self.__ccU) if csStat is None else csStat

        # ParserListerUtil.coordAssemblyChecker()
        self.__caC = None

        # representative model id
        self.__representative_model_id = REPRESENTATIVE_MODEL_ID
        # total number of models
        self.__total_models = 0

        # atom id list for each model_id and atom key (auth_asym_id, auth_seq_id, auth_comp_id, auth_atom_id, PDB_ins_code)
        self.__atomIdList = None
        # coordinates for each model_id and atom key
        self.__coordinates = None

        # distance restraints for each restraint key (list_id, restraint_id)
        self.__distRestDict = None
        # distance restraint keys for each sequence key (auth_asym_id, auth_seq_id, auth_comp_id)
        self.__distRestSeqDict = None

        # dihedral angle restraints for each restraint key (list_id, restraint_id)
        self.__dihedRestDict = None
        # dihedral angle restraint keys for each sequence key (auth_asym_id, auth_seq_id, auth_comp_id)
        self.__dihedRestSeqDict = None

        # RDC restraints for each restraint key (list_id, restraint_id)
        self.__rdcRestDict = None
        # RDC restraint keys for each sequence key (auth_asym_id, auth_seq_id, auth_comp_id)
        self.__rdcRestSeqDict = None

        # distance restraint violations for each restraint key
        self.__distRestViolDict = None
        # list of restraint key of unmapped distance restraints
        self.__distRestUnmapped = None
        # combination keys (Combination_ID/Mmember_ID) of violated_distance restraints for each restraint key
        self.__distRestViolCombKeyDict = None

        # dihedral angle restraint violations for each restraint key
        self.__dihedRestViolDict = None
        # list of restraint key of unmapped dihedral angle restraints
        self.__dihedRestUnmapped = None
        # combination key (Combination_ID) of violated_distance angle restraints for each restraint key
        self.__dihedRestViolCombKeyDict = None

        # summarized restraint validation results
        self.__results = None

        # whether the previous results have been retrieved
        self.__has_prev_results = False

        # list of known workflow operations
        self.__workFlowOps = ('nmr-restraint-validation')

        __checkTasks = [self.__parseCoordinate,
                        self.__parseNmrData,
                        self.__checkPreviousResultsIfAvailable,
                        self.__retrieveCoordAssemblyChecker,
                        self.__extractCoordAtomSite,
                        self.__extractGenDistConstraint,
                        self.__extractTorsionAngleConstraint,
                        self.__extractRdcConstraint,
                        self.__calculateDistanceRestraintViolations,
                        self.__calculateDihedralAngleRestraintViolations,
                        self.__summarizeCommonResults,
                        self.__summarizeDistanceRestraintValidation,
                        self.__summarizeDihedralAngleRestraintValidation,
                        self.__outputResultsAsPickleFileIfPossible]

        # dictionary of processing tasks of each workflow operation
        self.__procTasksDict = {'nmr-restraint-validation': __checkTasks}

    def setVerbose(self, verbose):
        """ Set verbose mode.
        """

        self.__verbose = verbose
        self.__debug = verbose

    def getResults(self):
        """ Return NMR restraint validation result.
        """

        return self.__results

    def addInput(self, name=None, value=None, type='file'):  # pylint: disable=redefined-builtin
        """ Add a named input and value to the dictionary of input parameters.
        """

        try:

            if type == 'param':
                self.__inputParamDict[name] = value
            elif type == 'file':
                self.__inputParamDict[name] = os.path.abspath(value)
            else:
                raise ValueError(f"+NmrVrptUtility.addInput() ++ Error  - Unknown input type {type}.")

        except Exception as e:
            raise ValueError("+NmrVrptUtility.addInput() ++ Error  - " + str(e))

    def addOutput(self, name=None, value=None, type='file'):  # pylint: disable=redefined-builtin
        """ Add a named input and value to the dictionary of output parameters.
        """

        try:

            if type == 'param':
                self.__outputParamDict[name] = value
            elif type == 'file':
                self.__outputParamDict[name] = os.path.abspath(value)
            else:
                raise ValueError(f"+NmrVrptUtility.addOutput() ++ Error  - Unknown output type {type}.")

            return True

        except Exception as e:
            raise ValueError("+NmrVrptUtility.addOutput() ++ Error  - " + str(e))

    def op(self, op):
        """ Perform a series of tasks for a given workflow operation.
        """

        if self.__verbose:
            self.__lfh.write(f"+NmrVrptUtility.op() starting op {op}\n")

        if op not in self.__workFlowOps:
            raise KeyError(f"+NmrVrptUtility.op() ++ Error  - Unknown workflow operation {op}.")

        if op in self.__procTasksDict:

            for task in self.__procTasksDict[op]:

                if self.__verbose:
                    self.__lfh.write(f"+NmrVrptUtility.op() starting op {op} - task {task.__name__}\n")

                start_time = time.time()

                if not task():
                    break

                if self.__debug:
                    end_time = time.time()
                    if end_time - start_time > 1.0:
                        self.__lfh.write(f"op: {op}, task: {task.__name__}, elapsed time: {end_time - start_time:.1f} sec\n")

        return self.__results

    def __parseCoordinate(self):
        """ Parse coordinates.
        """

        if not self.__checkCoordInputSource():

            if 'coordinate_file_path' in self.__inputParamDict:

                err = f"No such {self.__inputParamDict['coordinate_file_path']!r} file."

                if self.__verbose:
                    self.__lfh.write(f"+NmrVrptUtility.__parseCoordinate() ++ Error  - {err}\n")

            return False

        file_name = os.path.basename(self.__cifPath)

        try:

            if self.__cifPath is None:

                err = f"{file_name!r} is invalid PDBx/mmCIF file."

                if self.__verbose:
                    self.__lfh.write(f"+NmrVrptUtility.__parseCoordinate() ++ Error  - {err}\n")

                return False

            self.__total_models = 0

            ensemble = self.__cR.getDictList('pdbx_nmr_ensemble')

            if len(ensemble) > 0 and 'conformers_submitted_total_number' in ensemble[0]:

                try:
                    self.__total_models = int(ensemble[0]['conformers_submitted_total_number'])
                except ValueError:
                    pass

            if len(ensemble) == 0:

                ensemble = self.__cR.getDictList('rcsb_nmr_ensemble')

                if len(ensemble) > 0 and 'conformers_submitted_total_number' in ensemble[0]:

                    try:
                        self.__total_models = int(ensemble[0]['conformers_submitted_total_number'])
                    except ValueError:
                        pass

                else:

                    try:

                        model_num_name = 'pdbx_PDB_model_num' if self.__cR.hasItem('atom_site', 'pdbx_PDB_model_num') else 'ndb_model'

                        model_ids = self.__cR.getDictListWithFilter('atom_site',
                                                                    [{'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                                                                     ])

                        if len(model_ids) > 0:
                            model_ids = set(c['model_id'] for c in model_ids)

                            self.__representative_model_id = min(model_ids)
                            self.__total_models = len(model_ids)

                    except Exception as e:

                        if self.__verbose:
                            self.__lfh.write(f"+NmrVrptUtility.__parseCoordinate() ++ Error  - {str(e)}\n")

            return True

        except Exception:
            return False

    def __checkCoordInputSource(self):
        """ Check input source of the coordinates.
        """

        if self.__cifPath is not None:
            return True

        if 'coordinate_file_path' in self.__inputParamDict:

            fPath = self.__inputParamDict['coordinate_file_path']

            if fPath.endswith('.gz'):

                _fPath = os.path.splitext(fPath)[0]

                if not os.path.exists(_fPath):

                    try:

                        uncompress_gzip_file(fPath, _fPath)

                    except Exception as e:

                        if self.__verbose:
                            self.__lfh.write(f"+NmrVrptUtility.__checkCoordInputSource() ++ Error  - {str(e)}\n")

                        return False

                fPath = _fPath

            try:

                if self.__dirPath is None:
                    self.__dirPath = os.path.dirname(fPath)

                self.__cacheDirPath = os.path.join(self.__dirPath, self.__sub_dir_name_for_cache)

                if not os.path.isdir(self.__cacheDirPath):
                    os.makedirs(self.__cacheDirPath)

                self.__cR = CifReader(self.__verbose, self.__lfh,
                                      use_cache=True,
                                      sub_dir_name_for_cache=self.__sub_dir_name_for_cache)

                if self.__cR.parse(fPath):
                    self.__cifPath = fPath
                    self.__cifHashCode = self.__cR.getHashCode()
                    return True

            except Exception:
                pass

        if 'coord_cif_reader_object' in self.__inputParamDict:

            self.__cR = self.__inputParamDict['coord_cif_reader_object']

            self.__cifPath = self.__cR.getFilePath()

            if self.__dirPath is None:
                self.__dirPath = os.path.dirname(self.__cifPath)

            self.__sub_dir_name_for_cache = self.__cR.__sub_dir_name_for_cache  # pylint: disable=protected-access

            self.__cacheDirPath = os.path.join(self.__dirPath, self.__sub_dir_name_for_cache)

            if not os.path.isdir(self.__cacheDirPath):
                os.makedirs(self.__cacheDirPath)

            self.__cifHashCode = self.__cR.getHashCode()

            return True

        return False

    def __parseNmrData(self):
        """ Parse NMR data.
        """

        if not self.__checkNmrDataInputSource():

            if 'nmr_cif_file_path' in self.__inputParamDict:

                err = f"No such {self.__inputParamDict['nmr_cif_file_path']!r} file."

                if self.__verbose:
                    self.__lfh.write(f"+NmrVrptUtility.__parseNmrData() ++ Error  - {err}\n")

            return False

        return True

    def __checkNmrDataInputSource(self):
        """ Check input source of NMR data.
        """

        if self.__nmrDataPath is not None:
            return True

        if 'nmr_cif_file_path' in self.__inputParamDict:

            fPath = self.__inputParamDict['nmr_cif_file_path']

            if fPath.endswith('.gz'):

                _fPath = os.path.splitext(fPath)[0]

                if not os.path.exists(_fPath):

                    try:

                        uncompress_gzip_file(fPath, _fPath)

                    except Exception as e:

                        if self.__verbose:
                            self.__lfh.write(f"+NmrVrptUtility.__checkNmrDataInputSource() ++ Error  - {str(e)}\n")

                        return False

                fPath = _fPath

            try:

                self.__rR = CifReader(self.__verbose, self.__lfh,
                                      use_cache=False)

                if self.__rR.parse(fPath):
                    self.__nmrDataPath = fPath
                    self.__nmrDataHashCode = self.__rR.getHashCode()
                    return True

            except Exception:
                pass

        if 'nmr_cif_reader_object' in self.__inputParamDict:

            self.__rR = self.__inputParamDict['nmr_cif_reader_object']

            self.__nmrDataPath = self.__rR.getFilePath()

            self.__nmrDataHashCode = self.__rR.getHashCode()

            return True

        def get_tempfile_name(suffix=''):
            return os.path.join(tempfile.gettempdir(), f"{next(tempfile._get_candidate_names())}{suffix}")  # pylint: disable=protected-access

        if 'nmr_str_file_path' in self.__inputParamDict:

            fPath = self.__inputParamDict['nmr_str_file_path']

            _fPath = get_tempfile_name('.str2cif')

            try:

                myIo = IoAdapterPy(False, self.__lfh)
                containerList = myIo.readFile(fPath)

                if containerList is not None and len(containerList) > 1:

                    if self.__verbose:
                        self.__lfh.write(f"Input container list is {[(c.getName(), c.getType()) for c in containerList]!r}\n")

                    for c in containerList:
                        c.setType('data')

                    myIo.writeFile(_fPath, containerList=containerList[1:])

                    self.__rR = CifReader(self.__verbose, self.__lfh,
                                          use_cache=False)

                    if self.__rR.parse(_fPath, self.__dirPath):
                        self.__nmrDataPath = _fPath
                        self.__nmrDataHashCode = self.__rR.getHashCode()
                        return True

            except Exception as e:
                self.__lfh.write(f"+NmrVrptUtility.__checkNmrDataInputSource() ++ Error  - {str(e)}\n")
            finally:
                try:
                    if os.path.exists(_fPath):
                        os.remove(_fPath)
                except OSError:
                    pass

        if 'pynmrstar_object' in self.__inputParamDict:

            master_entry = self.__inputParamDict['pynmrstar_object']

            _fPath = get_tempfile_name('.str')
            __fPath = _fPath + '.str2cif'

            try:

                master_entry.write_to_file(_fPath, show_comments=False, skip_empty_loops=True, skip_empty_tags=False)

                myIo = IoAdapterPy(False, self.__lfh)
                containerList = myIo.readFile(_fPath)

                if containerList is not None and len(containerList) > 1:

                    if self.__verbose:
                        self.__lfh.write(f"Input container list is {[(c.getName(), c.getType()) for c in containerList]!r}\n")

                    for c in containerList:
                        c.setType('data')

                    myIo.writeFile(__fPath, containerList=containerList[1:])

                    self.__rR = CifReader(self.__verbose, self.__lfh,
                                          use_cache=False)

                    if self.__rR.parse(__fPath, self.__dirPath):
                        self.__nmrDataPath = __fPath
                        self.__nmrDataHashCode = self.__rR.getHashCode()
                        return True

            except Exception as e:
                self.__lfh.write(f"+NmrVrptUtility.__checkNmrDataInputSource() ++ Error  - {str(e)}\n")
            finally:
                try:
                    if os.path.exists(_fPath):
                        os.remove(_fPath)
                    if os.path.exists(__fPath):
                        os.remove(__fPath)
                except OSError:
                    pass

        return False

    def __checkPreviousResultsIfAvailable(self):
        """ Retrieve the previous results using the identical data sources, if available.
        """

        if self.__cifHashCode is not None and self.__nmrDataHashCode is not None:
            self.__resultsCacheName = f"{self.__cifHashCode}_{self.__nmrDataHashCode}_vrpt_results.pkl"
            cache_path = os.path.join(self.__cacheDirPath, self.__resultsCacheName)

            self.__results = load_from_pickle(cache_path)

            self.__has_prev_results = self.__results is not None

        return True

    def __retrieveCoordAssemblyChecker(self):
        """ Wrapper function for ParserListenerUtil.coordAssemblyChecker.
        """

        if self.__has_prev_results:
            return True

        cache_path = None
        if self.__cifHashCode is not None:
            cache_path = os.path.join(self.__cacheDirPath, f"{self.__cifHashCode}_asm_chk.pkl")
            self.__caC = load_from_pickle(cache_path)

            if self.__caC is not None:
                return True

        self.__caC = coordAssemblyChecker(self.__verbose, self.__lfh,
                                          self.__representative_model_id,
                                          self.__cR, None)

        if self.__caC is not None and cache_path:
            write_as_pickle(self.__caC, cache_path)

        return True

    def __extractCoordAtomSite(self):
        """ Extract atom_site of coordinate file.
            @author: Masashi Yokochi
            @note: Derived from wwpdb.apps.validation.src.RestraintValidation.BMRBRestraintsAnalysis.get_coordinates,
                   written by Kumaran Baskaran
            @change: class method, use of wwpdb.utils.nmr.io.CifReader, use PDB_ins_code for atom identification, performance optimization
        """

        if self.__has_prev_results:
            return True

        if self.__cifPath is None:
            return False

        vrpt_atom_id_cache_path = vrpt_atom_site_cache_path = None

        if self.__cifHashCode is not None:
            vrpt_atom_id_cache_path = os.path.join(self.__cacheDirPath, f"{self.__cifHashCode}_vrpt_atom_id.pkl")
            self.__atomIdList = load_from_pickle(vrpt_atom_id_cache_path, None)

            vrpt_atom_site_cache_path = os.path.join(self.__cacheDirPath, f"{self.__cifHashCode}_vrpt_atom_site.pkl")
            self.__coordinates = load_from_pickle(vrpt_atom_site_cache_path, None)

            if self.__atomIdList is not None and self.__coordinates is not None:
                return True

        data_items = [{'name': 'auth_asym_id', 'type': 'str'},
                      {'name': 'auth_seq_id', 'type': 'int'},
                      {'name': 'auth_comp_id', 'type': 'str'},
                      {'name': 'auth_atom_id', 'type': 'str'},
                      {'name': 'label_asym_id', 'type': 'str'},
                      {'name': 'label_seq_id', 'type': 'int'},
                      {'name': 'label_comp_id', 'type': 'str'},
                      {'name': 'label_atom_id', 'type': 'str'},
                      {'name': 'label_entity_id', 'type': 'int'},
                      {'name': 'label_alt_id', 'type': 'str', 'default': '.'},
                      {'name': 'pdbx_PDB_ins_code', 'type': 'str', 'default': '?'},
                      {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                      {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                      {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                      ]

        _filter_items = []  # {'name': 'label_alt_id', 'type': 'enum', 'enum': ('A')}]

        if len(self.__caC['polymer_sequence']) >= LEN_MAJOR_ASYM_ID:
            _filter_items.append({'name': 'auth_asym_id', 'type': 'enum', 'enum': LARGE_ASYM_ID,
                                  'fetch_first_match': True})  # to process large assembly avoiding forced timeout

        self.__atomIdList = {}
        self.__coordinates = {}

        try:

            for model_id in range(1, self.__total_models + 1):
                filter_items = copy.copy(_filter_items)
                filter_items.append({'name': 'pdbx_PDB_model_num', 'type': 'int',
                                     'value': model_id})

                coord = self.__cR.getDictListWithFilter('atom_site', data_items, filter_items)

                atom_id_list_per_model = {}
                coordinates_per_model = {}

                for c in coord:
                    atom_key = (c['auth_asym_id'], c['auth_seq_id'], c['auth_comp_id'],
                                c['auth_atom_id'], c['pdbx_PDB_ins_code'])

                    # tokens = ("ent_", "said_", "resname_", "seq_", "resnum_", "altcode_", "icode_", "chain_")

                    atom_id_list_per_model[atom_key] =\
                        (c['label_entity_id'], c['label_asym_id'], c['label_comp_id'], c['label_seq_id'],
                         c['auth_seq_id'], c['label_alt_id'], c['pdbx_PDB_ins_code'], c['auth_asym_id'])

                    coordinates_per_model[atom_key] = np.asarray([c['x'], c['y'], c['z']], dtype=float)

                self.__atomIdList[model_id] = atom_id_list_per_model
                self.__coordinates[model_id] = coordinates_per_model

            if self.__cifHashCode is not None:
                write_as_pickle(self.__atomIdList, vrpt_atom_id_cache_path)
                write_as_pickle(self.__coordinates, vrpt_atom_site_cache_path)

            return True

        except Exception as e:
            self.__lfh.write(f"+NmrVrptUtility.__extractCoordAtomSite() ++ Error  - {str(e)}\n")

            self.__atomIdList = self.__coordinates = None

        return False

    def __extractGenDistConstraint(self):
        """ Extract Gen_dist_constraint category of NMR data file.
            @author: Masashi Yokochi
            @note: Derived from wwpdb.apps.validation.src.RestraintValidation.BMRBRestraintsAnalysis.get_restraints2,
                   written by Kumaran Baskaran
            @change: class method, use of wwpdb.utils.nmr.io.CifReader, improve readability of restraints,
                     support combinational restraints (_Gen_dist_constraint.Combination_ID, Member_ID)
        """

        if self.__has_prev_results:
            return True

        if self.__nmrDataPath is None:
            return False

        self.__distRestDict = {}
        self.__distRestSeqDict = {}

        try:

            for dBlock in self.__rR.getDataBlockList():

                if not self.__rR.hasCategory('Gen_dist_constraint', dBlock.getName()):
                    continue

                sf_tag = self.__rR.getDictList('Gen_dist_constraint_list')

                list_id = int(sf_tag[0]['ID'])

                data_items = [{'name': 'ID', 'type': 'int', 'alt_name': 'id'},
                              {'name': 'Combination_ID', 'type': 'int', 'alt_name': 'combination_id'},
                              {'name': 'Member_logic_code', 'type': 'enum', 'alt_name': 'member_logic_code',
                               'enum': ('OR', 'AND')},
                              {'name': 'Entity_assembly_ID_1', 'type': 'str', 'alt_name': 'entity_asm_id_1'},
                              {'name': 'Auth_asym_ID_1', 'type': 'str', 'alt_name': 'auth_asym_id_1'},
                              {'name': 'Auth_seq_ID_1', 'type': 'int', 'alt_name': 'auth_seq_id_1'},
                              {'name': 'Comp_ID_1', 'type': 'str', 'alt_name': 'comp_id_1'},
                              {'name': 'Atom_ID_1', 'type': 'str', 'alt_name': 'atom_id_1'},
                              {'name': 'Entity_assembly_ID_2', 'type': 'str', 'alt_name': 'entity_asm_id_2'},
                              {'name': 'Auth_asym_ID_2', 'type': 'str', 'alt_name': 'auth_asym_id_2'},
                              {'name': 'Auth_seq_ID_2', 'type': 'int', 'alt_name': 'auth_seq_id_2'},
                              {'name': 'Comp_ID_2', 'type': 'str', 'alt_name': 'comp_id_2'},
                              {'name': 'Atom_ID_2', 'type': 'str', 'alt_name': 'atom_id_2'},
                              {'name': 'Distance_lower_bound_val', 'type': 'float', 'alt_name': 'lower_bound'},
                              {'name': 'Distance_upper_bound_val', 'type': 'float', 'alt_name': 'upper_bound'}
                              ]

                has_member_id = self.__rR.hasItem('Gen_dist_constraint', 'Member_ID')
                has_pdb_ins_code_1 = self.__rR.hasItem('Gen_dist_constraint', 'PDB_ins_code_1')
                has_pdb_ins_code_2 = self.__rR.hasItem('Gen_dist_constraint', 'PDB_ins_code_2')

                if has_member_id:
                    data_items.append({'name': 'Member_ID', 'type': 'int', 'alt_name': 'member_id'})
                if has_pdb_ins_code_1:
                    data_items.append({'name': 'PDB_ins_code_1', 'type': 'str', 'alt_name': 'ins_code_1', 'default': '?'})
                if has_pdb_ins_code_2:
                    data_items.append({'name': 'PDB_ins_code_2', 'type': 'str', 'alt_name': 'ins_code_2', 'default': '?'})

                filter_items = [{'name': 'Gen_dist_constraint_list_ID', 'type': 'int', 'value': list_id}]

                rest = self.__rR.getDictListWithFilter('Gen_dist_constraint',
                                                       data_items,
                                                       filter_items)

                for r in rest:
                    rest_key = (list_id, r['id'])

                    if rest_key not in self.__distRestDict:
                        self.__distRestDict[rest_key] = []

                    auth_asym_id_1 = r['auth_asym_id_1']
                    auth_asym_id_2 = r['auth_asym_id_2']
                    auth_seq_id_1 = r['auth_seq_id_1']
                    auth_seq_id_2 = r['auth_seq_id_2']
                    comp_id_1 = r['comp_id_1']
                    comp_id_2 = r['comp_id_2']
                    atom_id_1 = r['atom_id_1']
                    atom_id_2 = r['atom_id_2']
                    member_id = r['member_id'] if has_member_id else None
                    ins_code_1 = r['ins_code_1'] if has_pdb_ins_code_1 else '?'
                    ins_code_2 = r['ins_code_2'] if has_pdb_ins_code_2 else '?'

                    offset = abs(auth_seq_id_1 - auth_seq_id_2)

                    if r['entity_asm_id_1'] != r['entity_asm_id_2']:
                        distance_type = 'interchain'
                    elif offset == 0:
                        distance_type = 'intraresidue'
                    elif offset == 1:
                        distance_type = 'sequential'
                    elif 1 < offset < 5:
                        distance_type = 'medium'
                    else:
                        distance_type = 'long'

                    bb_atoms_1 = self.__csStat.getBackBoneAtoms(comp_id_1)
                    bb_atoms_2 = self.__csStat.getBackBoneAtoms(comp_id_2)

                    if atom_id_1 in bb_atoms_1 and atom_id_2 in bb_atoms_2:
                        distance_sub_type = 'backbone-backbone'
                    elif atom_id_1 in bb_atoms_1 or atom_id_2 in bb_atoms_2:
                        distance_sub_type = 'backbone-sidechain'
                    else:
                        distance_sub_type = 'sidechain-sidechain'

                    if 'O' in (atom_id_1[0], atom_id_2[0]):
                        bond_flag = 'hbond'
                    elif 'SG' in (atom_id_1, atom_id_2):
                        bond_flag = 'sbond'
                    else:
                        bond_flag = None

                    lower_bound = r['lower_bound']
                    upper_bound = r['upper_bound']

                    if lower_bound is None and upper_bound is None:
                        if self.__verbose:
                            self.__lfh.write(f"+NmrVrptUtility.__extractGenDistConstraint() ++ Warning  - distance restraint {rest_key} {r} is not interpretable.\n")
                        continue

                    self.__distRestDict[rest_key].append({'atom_key_1': (auth_asym_id_1, auth_seq_id_1, comp_id_1,
                                                                         atom_id_1, ins_code_1),
                                                          'atom_key_2': (auth_asym_id_2, auth_seq_id_2, comp_id_2,
                                                                         atom_id_2, ins_code_2),
                                                          'combination_id': r['combination_id'],
                                                          'member_id': member_id,
                                                          'distance_type': distance_type,
                                                          'distance_sub_type': distance_sub_type,
                                                          'bond_flag': bond_flag,
                                                          'lower_bound': r['lower_bound'],
                                                          'upper_bound': r['upper_bound']})

                    seq_key_1 = (auth_asym_id_1, auth_seq_id_1, comp_id_1)
                    seq_key_2 = (auth_asym_id_2, auth_seq_id_2, comp_id_2)

                    seq_keys = set([seq_key_1, seq_key_2])

                    for seq_key in seq_keys:
                        if seq_key not in self.__distRestSeqDict:
                            self.__distRestSeqDict[seq_key] = []
                        self.__distRestSeqDict[seq_key].append(rest_key)

            for v in self.__distRestSeqDict.values():
                v = list(set(v))

            if len(self.__distRestDict) == 0:
                self.__distRestDict = self.__distRestSeqDict = None

            return True

        except Exception as e:
            self.__lfh.write(f"+NmrVrptUtility.__extractGenDistConstraint() ++ Error  - {str(e)}\n")

            self.__distRestDict = self.__distRestSeqDict = None

        return False

    def __extractTorsionAngleConstraint(self):
        """ Extract Torsion_angle_constraint category of NMR data file.
            @author: Masashi Yokochi
            @note: Derived from wwpdb.apps.validation.src.RestraintValidation.BMRBRestraintsAnalysis.get_restraints2,
                   written by Kumaran Baskaran
            @change: class method, use of wwpdb.utils.nmr.io.CifReader, improve readability of restraints,
                     support combinational restraints (_Torsion_angle_constraint.Combination_ID)
        """

        if self.__has_prev_results:
            return True

        if self.__nmrDataPath is None:
            return False

        self.__dihedRestDict = {}
        self.__dihedRestSeqDict = {}

        try:

            for dBlock in self.__rR.getDataBlockList():

                if not self.__rR.hasCategory('Torsion_angle_constraint', dBlock.getName()):
                    continue

                sf_tag = self.__rR.getDictList('Torsion_angle_constraint_list')

                list_id = int(sf_tag[0]['ID'])

                data_items = [{'name': 'ID', 'type': 'int', 'alt_name': 'id'},
                              {'name': 'Torsion_angle_name', 'type': 'str', 'alt_name': 'angle_type'},
                              {'name': 'Combination_ID', 'type': 'int', 'alt_name': 'combination_id'},
                              {'name': 'Auth_asym_ID_1', 'type': 'str', 'alt_name': 'auth_asym_id_1'},
                              {'name': 'Auth_seq_ID_1', 'type': 'int', 'alt_name': 'auth_seq_id_1'},
                              {'name': 'Comp_ID_1', 'type': 'str', 'alt_name': 'comp_id_1'},
                              {'name': 'Atom_ID_1', 'type': 'str', 'alt_name': 'atom_id_1'},
                              {'name': 'Auth_asym_ID_2', 'type': 'str', 'alt_name': 'auth_asym_id_2'},
                              {'name': 'Auth_seq_ID_2', 'type': 'int', 'alt_name': 'auth_seq_id_2'},
                              {'name': 'Comp_ID_2', 'type': 'str', 'alt_name': 'comp_id_2'},
                              {'name': 'Atom_ID_2', 'type': 'str', 'alt_name': 'atom_id_2'},
                              {'name': 'Auth_asym_ID_3', 'type': 'str', 'alt_name': 'auth_asym_id_3'},
                              {'name': 'Auth_seq_ID_3', 'type': 'int', 'alt_name': 'auth_seq_id_3'},
                              {'name': 'Comp_ID_3', 'type': 'str', 'alt_name': 'comp_id_3'},
                              {'name': 'Atom_ID_3', 'type': 'str', 'alt_name': 'atom_id_3'},
                              {'name': 'Auth_asym_ID_4', 'type': 'str', 'alt_name': 'auth_asym_id_4'},
                              {'name': 'Auth_seq_ID_4', 'type': 'int', 'alt_name': 'auth_seq_id_4'},
                              {'name': 'Comp_ID_4', 'type': 'str', 'alt_name': 'comp_id_4'},
                              {'name': 'Atom_ID_4', 'type': 'str', 'alt_name': 'atom_id_4'},
                              {'name': 'Angle_lower_bound_val', 'type': 'float', 'alt_name': 'lower_bound'},
                              {'name': 'Angle_upper_bound_val', 'type': 'float', 'alt_name': 'upper_bound'},
                              {'name': 'Angle_target_val', 'type': 'float', 'alt_name': 'target_value'}
                              ]

                has_pdb_ins_code_1 = self.__rR.hasItem('Torsion_angle_constraint', 'PDB_ins_code_1')
                has_pdb_ins_code_2 = self.__rR.hasItem('Torsion_angle_constraint', 'PDB_ins_code_2')
                has_pdb_ins_code_3 = self.__rR.hasItem('Torsion_angle_constraint', 'PDB_ins_code_3')
                has_pdb_ins_code_4 = self.__rR.hasItem('Torsion_angle_constraint', 'PDB_ins_code_4')

                if has_pdb_ins_code_1:
                    data_items.append({'name': 'PDB_ins_code_1', 'type': 'str', 'alt_name': 'ins_code_1', 'default': '?'})
                if has_pdb_ins_code_2:
                    data_items.append({'name': 'PDB_ins_code_2', 'type': 'str', 'alt_name': 'ins_code_2', 'default': '?'})
                if has_pdb_ins_code_3:
                    data_items.append({'name': 'PDB_ins_code_3', 'type': 'str', 'alt_name': 'ins_code_3', 'default': '?'})
                if has_pdb_ins_code_4:
                    data_items.append({'name': 'PDB_ins_code_4', 'type': 'str', 'alt_name': 'ins_code_4', 'default': '?'})

                filter_items = [{'name': 'Torsion_angle_constraint_list_ID', 'type': 'int', 'value': list_id}]

                rest = self.__rR.getDictListWithFilter('Torsion_angle_constraint',
                                                       data_items,
                                                       filter_items)

                for r in rest:
                    rest_key = (list_id, r['id'])

                    if rest_key not in self.__dihedRestDict:
                        self.__dihedRestDict[rest_key] = []

                    auth_asym_id_1 = r['auth_asym_id_1']
                    auth_asym_id_2 = r['auth_asym_id_2']
                    auth_asym_id_3 = r['auth_asym_id_3']
                    auth_asym_id_4 = r['auth_asym_id_4']
                    auth_seq_id_1 = r['auth_seq_id_1']
                    auth_seq_id_2 = r['auth_seq_id_2']
                    auth_seq_id_3 = r['auth_seq_id_3']
                    auth_seq_id_4 = r['auth_seq_id_4']
                    comp_id_1 = r['comp_id_1']
                    comp_id_2 = r['comp_id_2']
                    comp_id_3 = r['comp_id_3']
                    comp_id_4 = r['comp_id_4']
                    atom_id_1 = r['atom_id_1']
                    atom_id_2 = r['atom_id_2']
                    atom_id_3 = r['atom_id_3']
                    atom_id_4 = r['atom_id_4']
                    ins_code_1 = r['ins_code_1'] if has_pdb_ins_code_1 else '?'
                    ins_code_2 = r['ins_code_2'] if has_pdb_ins_code_2 else '?'
                    ins_code_3 = r['ins_code_3'] if has_pdb_ins_code_3 else '?'
                    ins_code_4 = r['ins_code_4'] if has_pdb_ins_code_4 else '?'

                    lower_bound = r['lower_bound']
                    upper_bound = r['upper_bound']
                    target_value = r['target_value']

                    if (lower_bound is None and upper_bound is None) or target_value is None:
                        if self.__verbose:
                            self.__lfh.write(f"+NmrVrptUtility.__extractTorsionAngleConstraint() ++ Warning  - dihedral angle restraint {rest_key} {r} is not interpretable.\n")
                        continue

                    self.__dihedRestDict[rest_key].append({'atom_key_1': (auth_asym_id_1, auth_seq_id_1, comp_id_1,
                                                                          atom_id_1, ins_code_1),
                                                           'atom_key_2': (auth_asym_id_2, auth_seq_id_2, comp_id_2,
                                                                          atom_id_2, ins_code_2),
                                                           'atom_key_3': (auth_asym_id_3, auth_seq_id_3, comp_id_3,
                                                                          atom_id_3, ins_code_3),
                                                           'atom_key_4': (auth_asym_id_4, auth_seq_id_4, comp_id_4,
                                                                          atom_id_4, ins_code_4),
                                                           'combination_id': r['combination_id'],
                                                           'angle_type': r['angle_type'],
                                                           'lower_bound': lower_bound,
                                                           'upper_bound': upper_bound,
                                                           'target_value': target_value})

                    seq_key_1 = (auth_asym_id_1, auth_seq_id_1, comp_id_1)
                    seq_key_2 = (auth_asym_id_2, auth_seq_id_2, comp_id_2)
                    seq_key_3 = (auth_asym_id_3, auth_seq_id_3, comp_id_3)
                    seq_key_4 = (auth_asym_id_4, auth_seq_id_4, comp_id_4)

                    seq_keys = set([seq_key_1, seq_key_2, seq_key_3, seq_key_4])

                    for seq_key in seq_keys:
                        if seq_key not in self.__dihedRestSeqDict:
                            self.__dihedRestSeqDict[seq_key] = []
                        self.__dihedRestSeqDict[seq_key].append(rest_key)

            for v in self.__dihedRestSeqDict.values():
                v = list(set(v))

            if len(self.__dihedRestDict) == 0:
                self.__dihedRestDict = self.__dihedRestSeqDict = None

            return True

        except Exception as e:
            self.__lfh.write(f"+NmrVrptUtility.__extractTorsionAngleConstraint() ++ Error  - {str(e)}\n")

            self.__dihedRestDict = self.__dihedRestSeqDict = None

        return False

    def __extractRdcConstraint(self):
        """ Extract RDC_constraint category of NMR data file.
        """

        if self.__has_prev_results:
            return True

        if self.__nmrDataPath is None:
            return False

        self.__rdcRestDict = {}
        self.__rdcRestSeqDict = {}

        try:

            for dBlock in self.__rR.getDataBlockList():

                if not self.__rR.hasCategory('RDC_constraint', dBlock.getName()):
                    continue

                sf_tag = self.__rR.getDictList('RDC_constraint_list')

                list_id = int(sf_tag[0]['ID'])

                data_items = [{'name': 'ID', 'type': 'int', 'alt_name': 'id'},
                              {'name': 'Combination_ID', 'type': 'int', 'alt_name': 'combination_id'},
                              {'name': 'Auth_asym_ID_1', 'type': 'str', 'alt_name': 'auth_asym_id_1'},
                              {'name': 'Auth_seq_ID_1', 'type': 'int', 'alt_name': 'auth_seq_id_1'},
                              {'name': 'Comp_ID_1', 'type': 'str', 'alt_name': 'comp_id_1'},
                              {'name': 'Atom_ID_1', 'type': 'str', 'alt_name': 'atom_id_1'},
                              {'name': 'Auth_asym_ID_2', 'type': 'str', 'alt_name': 'auth_asym_id_2'},
                              {'name': 'Auth_seq_ID_2', 'type': 'int', 'alt_name': 'auth_seq_id_2'},
                              {'name': 'Comp_ID_2', 'type': 'str', 'alt_name': 'comp_id_2'},
                              {'name': 'Atom_ID_2', 'type': 'str', 'alt_name': 'atom_id_2'},
                              {'name': 'Target_value', 'type': 'float', 'alt_name': 'target_value'},
                              {'name': 'Target_value_uncertainty', 'type': 'float', 'alt_name': 'target_value_uncertainty'}
                              ]

                has_lower_bound = self.__rR.hasItem('RDC_constraint', 'RDC_lower_bound_val')
                has_upper_bound = self.__rR.hasItem('RDC_constraint', 'RDC_upper_bound_val')
                has_pdb_ins_code_1 = self.__rR.hasItem('RDC_constraint', 'PDB_ins_code_1')
                has_pdb_ins_code_2 = self.__rR.hasItem('RDC_constraint', 'PDB_ins_code_2')

                if has_lower_bound:
                    data_items.append({'name': 'RDC_lower_bound_val', 'type': 'float', 'alt_name': 'lower_bound'})
                if has_upper_bound:
                    data_items.append({'name': 'RDC_upper_bound_val', 'type': 'float', 'alt_name': 'upper_bound'})
                if has_pdb_ins_code_1:
                    data_items.append({'name': 'PDB_ins_code_1', 'type': 'str', 'alt_name': 'ins_code_1', 'default': '?'})
                if has_pdb_ins_code_2:
                    data_items.append({'name': 'PDB_ins_code_2', 'type': 'str', 'alt_name': 'ins_code_2', 'default': '?'})

                filter_items = [{'name': 'RDC_constraint_list_ID', 'type': 'int', 'value': list_id}]

                rest = self.__rR.getDictListWithFilter('RDC_constraint',
                                                       data_items,
                                                       filter_items)

                for r in rest:
                    rest_key = (list_id, r['id'])

                    if rest_key not in self.__rdcRestDict:
                        self.__rdcRestDict[rest_key] = []

                    auth_asym_id_1 = r['auth_asym_id_1']
                    auth_asym_id_2 = r['auth_asym_id_2']
                    auth_seq_id_1 = r['auth_seq_id_1']
                    auth_seq_id_2 = r['auth_seq_id_2']
                    comp_id_1 = r['comp_id_1']
                    comp_id_2 = r['comp_id_2']
                    atom_id_1 = r['atom_id_1']
                    atom_id_2 = r['atom_id_2']
                    ins_code_1 = r['ins_code_1'] if has_pdb_ins_code_1 else '?'
                    ins_code_2 = r['ins_code_2'] if has_pdb_ins_code_2 else '?'

                    target_value = r['target_value']
                    lower_bound = r['lower_bound'] if has_lower_bound else None
                    upper_bound = r['upper_bound'] if has_upper_bound else None

                    if target_value is None and lower_bound is None and upper_bound is None:
                        if self.__verbose:
                            self.__lfh.write(f"+NmrVrptUtility.__extractRdcConstraint() ++ Warning  - RDC restraint {rest_key} {r} is not interpretable.\n")
                        continue

                    self.__rdcRestDict[rest_key].append({'atom_key_1': (auth_asym_id_1, auth_seq_id_1, comp_id_1,
                                                                        atom_id_1, ins_code_1),
                                                         'atom_key_2': (auth_asym_id_2, auth_seq_id_2, comp_id_2,
                                                                        atom_id_2, ins_code_2),
                                                         'combination_id': r['combination_id'],
                                                         'lower_bound': lower_bound,
                                                         'upper_bound': upper_bound,
                                                         'target_value': target_value,
                                                         'target_value_uncertainty': r['target_value_uncertainty']})

                    seq_key_1 = (auth_asym_id_1, auth_seq_id_1, comp_id_1)
                    seq_key_2 = (auth_asym_id_2, auth_seq_id_2, comp_id_2)

                    seq_keys = set([seq_key_1, seq_key_2])

                    for seq_key in seq_keys:
                        if seq_key not in self.__rdcRestSeqDict:
                            self.__rdcRestSeqDict[seq_key] = []
                        self.__rdcRestSeqDict[seq_key].append(rest_key)

            for v in self.__rdcRestSeqDict.values():
                v = list(set(v))

            if len(self.__rdcRestDict) == 0:
                self.__rdcRestDict = self.__rdcRestSeqDict = None

            return True

        except Exception as e:
            self.__lfh.write(f"+NmrVrptUtility.__extractRdcConstraint() ++ Error  - {str(e)}\n")

            self.__rdcRestDict = self.__rdcRestSeqDict = None

        return False

    def __calculateDistanceRestraintViolations(self):
        """ Calculate distance restraint violations.
            @author: Masashi Yokochi
            @note: Derived from wwpdb.apps.validation.src.RestraintValidation.BMRBRestraintsAnalysis.calculate_distance_violations,
                   written by Kumaran Baskaran
            @change: class method,
                     support combinational restraints (_Gen_dist_constraint.Combination_ID, Member_ID)
        """

        if self.__distRestDict is None or self.__has_prev_results:
            return True

        if self.__coordinates is None:
            return False

        self.__distRestViolDict = {}
        self.__distRestViolCombKeyDict = {}
        self.__distRestUnmapped = []

        try:

            def calc_dist_rest_viol(rest_key, restraints):

                error_per_model = {}

                for model_id in self.__coordinates:

                    dist_list = []

                    for r in restraints:
                        atom_key_1 = r['atom_key_1']
                        atom_key_2 = r['atom_key_2']
                        lower_bound = r['lower_bound']
                        upper_bound = r['upper_bound']

                        atom_present = True

                        try:
                            pos_1 = self.__coordinates[model_id][atom_key_1]
                        except KeyError:
                            if self.__verbose:
                                self.__lfh.write(f"Atom (auth_asym_id: {atom_key_1[0]}, auth_seq_id: {atom_key_1[1]}, "
                                                 f"comp_id: {atom_key_1[2]}, atom_id: {atom_key_1[3]}) "
                                                 f"not found in the coordinates for distance restraint {rest_key}.")
                            atom_present = False

                        try:
                            pos_2 = self.__coordinates[model_id][atom_key_2]
                        except KeyError:
                            if self.__verbose:
                                self.__lfh.write(f"Atom (auth_asym_id: {atom_key_2[0]}, auth_seq_id: {atom_key_2[1]}, "
                                                 f"comp_id: {atom_key_2[2]}, atom_id: {atom_key_2[3]}) "
                                                 f"not found in the coordinates for distance restraint {rest_key}.")
                            atom_present = False

                        if atom_present:
                            d = distance(pos_1, pos_2)
                            dist_list.append(d)
                        else:
                            self.__distRestUnmapped.append(rest_key)

                    error = None

                    if len(dist_list) > 0:
                        avr_d = dist_inv_6_summed(dist_list)

                        if lower_bound is not None and upper_bound is not None:
                            if lower_bound <= avr_d <= upper_bound:
                                error = 0.0
                            elif avr_d > upper_bound:
                                error = abs(avr_d - upper_bound)
                            else:
                                error = abs(avr_d - lower_bound)

                        elif upper_bound is not None:
                            if avr_d <= upper_bound:
                                error = 0.0
                            elif avr_d > upper_bound:
                                error = abs(avr_d - upper_bound)

                        elif lower_bound is not None:
                            if lower_bound <= avr_d:
                                error = 0.0
                            else:
                                error = abs(avr_d - lower_bound)

                    error_per_model[model_id] = error

                return error_per_model

            def fill_smaller_error_for_each_model(error_per_model, min_error_per_model,
                                                  combination_id, member_id, min_comb_key_per_model):
                for model_id in range(1, self.__total_models + 1):
                    error = error_per_model[model_id]

                    if error is not None and error < min_error_per_model[model_id]:
                        min_error_per_model[model_id] = error
                        min_comb_key_per_model[model_id]['combination_id'] = combination_id
                        min_comb_key_per_model[model_id]['member_id'] = member_id

            def get_viol_per_model(min_error_per_model, min_comb_key_per_model):
                viol_per_model = {}
                comb_key_per_model = {}

                for model_id in range(1, self.__total_models + 1):
                    error = min_error_per_model[model_id]
                    comb_key = min_comb_key_per_model[model_id]

                    if NMR_VTF_DIST_VIOL_CUTOFF < error < DIST_ERROR_MAX:
                        viol_per_model[model_id] = round(error, 2)
                        comb_key_per_model[model_id] = comb_key
                    else:
                        viol_per_model[model_id] = None
                        comb_key_per_model[model_id] = None

                return viol_per_model, comb_key_per_model

            for rest_key, restraints in self.__distRestDict.items():

                has_combination_id = any(r for r in restraints if r['combination_id'] is not None)
                has_member_id = any(r for r in restraints if r['member_id'] is not None)

                min_error_per_model = {model_id: DIST_ERROR_MAX for model_id in range(1, self.__total_models + 1)}
                min_comb_key_per_model = {model_id: {'combination_id': None, 'member_id': None}
                                          for model_id in range(1, self.__total_models + 1)}

                if not has_combination_id and not has_member_id:
                    error_per_model = calc_dist_rest_viol(rest_key, restraints)

                    fill_smaller_error_for_each_model(error_per_model, min_error_per_model,
                                                      None, None, min_comb_key_per_model)

                elif not has_combination_id and has_member_id:
                    member_ids = set(r['member_id'] for r in restraints)

                    for member_id in member_ids:
                        _restraints = [r for r in restraints if r['member_id'] == member_id]

                        _error_per_model = calc_dist_rest_viol(rest_key, _restraints)

                        fill_smaller_error_for_each_model(_error_per_model, min_error_per_model,
                                                          None, member_id, min_comb_key_per_model)

                elif has_combination_id and not has_member_id:
                    combination_ids = set(r['combination_id'] for r in restraints)

                    for combination_id in combination_ids:
                        _restraints = [r for r in restraints if r['combination_id'] == combination_id]

                        _error_per_model = calc_dist_rest_viol(rest_key, _restraints)

                        fill_smaller_error_for_each_model(_error_per_model, min_error_per_model,
                                                          combination_id, None, min_comb_key_per_model)

                else:
                    combination_ids = set(r['combination_id'] for r in restraints)
                    member_ids = set(r['member_id'] for r in restraints)

                    for combination_id in combination_ids:
                        for member_id in member_ids:
                            _restraints = [r for r in restraints
                                           if r['combination_id'] == combination_id
                                           and r['member_id'] == member_id]

                            _error_per_model = calc_dist_rest_viol(rest_key, _restraints)

                            fill_smaller_error_for_each_model(_error_per_model, min_error_per_model,
                                                              combination_id, member_id,
                                                              min_comb_key_per_model)

                self.__distRestViolDict[rest_key], self.__distRestViolCombKeyDict[rest_key] =\
                    get_viol_per_model(min_error_per_model, min_comb_key_per_model)

            self.__distRestUnmapped = list(set(self.__distRestUnmapped))

            return True

        except Exception as e:
            self.__lfh.write(f"+NmrVrptUtility.__calculateDistanceRestraintViolations() ++ Error  - {str(e)}\n")

            self.__distRestViolDict = self.__distRestUnmapped = None

        return False

    def __calculateDihedralAngleRestraintViolations(self):
        """ Calculate dihedral angle restraint violations.
            @author: Masashi Yokochi
            @note: Derived from wwpdb.apps.validation.src.RestraintValidation.BMRBRestraintsAnalysis.calculate_angle_violations,
                   written by Kumaran Baskaran
            @change: class method,
                     support combinational restraints (_Torsion_angle_constraint.Combination_ID)
        """

        if self.__dihedRestDict is None or self.__has_prev_results:
            return True

        if self.__coordinates is None:
            return False

        self.__dihedRestViolDict = {}
        self.__dihedRestViolCombKeyDict = {}
        self.__dihedRestUnmapped = []

        try:

            def calc_dihed_rest_viol(rest_key, restraints):

                error_per_model = {}

                for model_id in self.__coordinates:

                    angle_list = []

                    for r in restraints:
                        atom_key_1 = r['atom_key_1']
                        atom_key_2 = r['atom_key_2']
                        atom_key_3 = r['atom_key_3']
                        atom_key_4 = r['atom_key_4']
                        lower_bound = r['lower_bound']
                        upper_bound = r['upper_bound']
                        target_value = r['target_value']

                        atom_present = True

                        try:
                            pos_1 = self.__coordinates[model_id][atom_key_1]
                        except KeyError:
                            if self.__verbose:
                                self.__lfh.write(f"Atom (auth_asym_id: {atom_key_1[0]}, auth_seq_id: {atom_key_1[1]}, "
                                                 f"comp_id: {atom_key_1[2]}, atom_id: {atom_key_1[3]}) "
                                                 f"not found in the coordinates for dihedral angle restraint {rest_key}.")
                            atom_present = False

                        try:
                            pos_2 = self.__coordinates[model_id][atom_key_2]
                        except KeyError:
                            if self.__verbose:
                                self.__lfh.write(f"Atom (auth_asym_id: {atom_key_2[0]}, auth_seq_id: {atom_key_2[1]}, "
                                                 f"comp_id: {atom_key_2[2]}, atom_id: {atom_key_2[3]}) "
                                                 f"not found in the coordinates for dihedral angle restraint {rest_key}.")
                            atom_present = False

                        try:
                            pos_3 = self.__coordinates[model_id][atom_key_3]
                        except KeyError:
                            if self.__verbose:
                                self.__lfh.write(f"Atom (auth_asym_id: {atom_key_3[0]}, auth_seq_id: {atom_key_3[1]}, "
                                                 f"comp_id: {atom_key_3[2]}, atom_id: {atom_key_3[3]}) "
                                                 f"not found in the coordinates for dihedral angle restraint {rest_key}.")
                            atom_present = False

                        try:
                            pos_4 = self.__coordinates[model_id][atom_key_4]
                        except KeyError:
                            if self.__verbose:
                                self.__lfh.write(f"Atom (auth_asym_id: {atom_key_4[0]}, auth_seq_id: {atom_key_4[1]}, "
                                                 f"comp_id: {atom_key_4[2]}, atom_id: {atom_key_4[3]}) "
                                                 f"not found in the coordinates for dihedral angle restraint {rest_key}.")
                            atom_present = False

                        if atom_present:
                            a = dihedral_angle(pos_1, pos_2, pos_3, pos_4)
                            angle_list.append(a)
                        else:
                            self.__dihedRestUnmapped.append(rest_key)

                    error = None

                    if len(angle_list) > 0:
                        avr_a = np.mean(np.array(angle_list))

                        error = angle_error(lower_bound, upper_bound, target_value, avr_a)

                    error_per_model[model_id] = error

                return error_per_model

            def fill_smaller_error_for_each_model(error_per_model, min_error_per_model,
                                                  combination_id, min_comb_key_per_model):
                for model_id in range(1, self.__total_models + 1):
                    error = error_per_model[model_id]

                    if error is not None and error < min_error_per_model[model_id]:
                        min_error_per_model[model_id] = error
                        min_comb_key_per_model[model_id]['combination_id'] = combination_id

            def get_viol_per_model(min_error_per_model, min_comb_key_per_model):
                viol_per_model = {}
                comb_key_per_model = {}

                for model_id in range(1, self.__total_models + 1):
                    error = min_error_per_model[model_id]
                    comb_key = min_comb_key_per_model[model_id]

                    if NMR_VTF_DIHED_VIOL_CUTOFF < error < ANGLE_ERROR_MAX:
                        viol_per_model[model_id] = round(error, 2)
                        comb_key_per_model[model_id] = comb_key
                    else:
                        viol_per_model[model_id] = None
                        comb_key_per_model[model_id] = None

                return viol_per_model, comb_key_per_model

            for rest_key, restraints in self.__dihedRestDict.items():

                has_combination_id = any(r for r in restraints if r['combination_id'] is not None)

                min_error_per_model = {model_id: ANGLE_ERROR_MAX for model_id in range(1, self.__total_models + 1)}
                min_comb_key_per_model = {model_id: {'combination_id': None}
                                          for model_id in range(1, self.__total_models + 1)}

                if not has_combination_id:
                    error_per_model = calc_dihed_rest_viol(rest_key, restraints)

                    fill_smaller_error_for_each_model(error_per_model, min_error_per_model,
                                                      None, min_comb_key_per_model)

                else:
                    combination_ids = set(r['combination_id'] for r in restraints)

                    for combination_id in combination_ids:
                        _restraints = [r for r in restraints if r['combination_id'] == combination_id]

                        _error_per_model = calc_dihed_rest_viol(rest_key, _restraints)

                        fill_smaller_error_for_each_model(_error_per_model, min_error_per_model,
                                                          combination_id, min_comb_key_per_model)

                self.__dihedRestViolDict[rest_key], self.__dihedRestViolCombKeyDict[rest_key] =\
                    get_viol_per_model(min_error_per_model, min_comb_key_per_model)

            self.__dihedRestUnmapped = list(set(self.__dihedRestUnmapped))

            return True

        except Exception as e:
            self.__lfh.write(f"+NmrVrptUtility.__calculateDistanceRestraintViolations() ++ Error  - {str(e)}\n")

            self.__dihedRestViolDict = self.__dihedRestUnmapped = None

        return False

    def __summarizeCommonResults(self):
        """ Summarize common results.
        """

        if self.__has_prev_results:
            return True

        self.__results = {'max_models': self.__total_models, 'atom_ids': self.__atomIdList, 'key_lists': {}}

        for dBlock in self.__rR.getDataBlockList():

            if not self.__rR.hasCategory('Chem_comp_assembly', dBlock.getName()):
                continue

            self.__results['seq_length'] = self.__rR.getRowLength('Chem_comp_assembly')

            break

        return True

    def __summarizeDistanceRestraintValidation(self):
        """ Summarize distance restraint validation results.
            @author: Masashi Yokochi
            @note: Derived from wwpdb.apps.validation.src.RestraintValidation.BMRBRestraintsAnalysis.generate_output,
                   written by Kumaran Baskaran
            @change: class method, improve readability of restraints, support combinational restraints, performance optimization
        """

        if self.__has_prev_results:
            return True

        try:

            self.__results['distance'] = self.__distRestViolDict is not None and len(self.__distRestViolDict) > 0

            if not self.__results['distance']:
                return True

            self.__results['dist_seq_dict'] = self.__distRestSeqDict
            self.__results['unmapped_dist'] = self.__distRestUnmapped

            any_type = 'total'

            distance_type = ('intraresidue', 'sequential', 'medium', 'long', 'interchain', any_type)
            distance_sub_type = ('backbone-backbone', 'backbone-sidechain', 'sidechain-sidechain')
            bond_flag = ('hbond', 'sbond', None)

            self.__results['key_lists']['distance_type'] = distance_type
            self.__results['key_lists']['distance_sub_type'] = distance_sub_type
            self.__results['key_lists']['bond_flag'] = bond_flag

            distance_summary = {}
            distance_violation = {}

            consistent_distance_violation = {}
            distance_violations_vs_models = {}
            distance_violations_in_models = {}

            for m in range(1, self.__total_models + 1):
                distance_violations_in_models[m] = {}

                for t in distance_type:
                    distance_summary[t] = {}
                    distance_violation[t] = {}
                    consistent_distance_violation[t] = {}
                    distance_violations_vs_models[t] = {}
                    distance_violations_in_models[m][t] = {}

                    for s in distance_sub_type:
                        distance_summary[t][s] = {}
                        distance_violation[t][s] = {}
                        consistent_distance_violation[t][s] = {}
                        distance_violations_vs_models[t][s] = {}
                        distance_violations_in_models[m][t][s] = {}

                        for b in bond_flag:
                            distance_summary[t][s][b] = 0
                            distance_violation[t][s][b] = 0
                            consistent_distance_violation[t][s][b] = 0
                            distance_violations_vs_models[t][s][b] = [0] * (self.__total_models + 1)
                            distance_violations_in_models[m][t][s][b] = []

            for rest_key, restraints in self.__distRestDict.items():
                comb_key = self.__distRestViolCombKeyDict[rest_key][self.__representative_model_id]
                if comb_key is not None:
                    combination_id = comb_key['combination_id']
                    member_id = comb_key['member_id']

                    r = next(r for r in restraints
                             if r['combination_id'] == combination_id and r['member_id'] == member_id)
                else:
                    r = restraints[0]

                t = r['distance_type']
                s = r['distance_sub_type']
                b = r['bond_flag']

                distance_summary[t][s][b] += 1
                distance_summary[any_type][s][b] += 1

                len_vm = len(get_violated_model_ids(self.__distRestViolDict[rest_key]))

                if len_vm > 0:
                    distance_violation[t][s][b] += 1
                    distance_violation[any_type][s][b] += 1

                if len_vm == self.__total_models:
                    consistent_distance_violation[t][s][b] += 1
                    consistent_distance_violation[any_type][s][b] += 1

                distance_violations_vs_models[t][s][b][len_vm] += 1
                distance_violations_vs_models[any_type][s][b][len_vm] += 1

            self.__results['distance_summary'] = distance_summary
            self.__results['distance_violation'] = distance_violation
            self.__results['consistent_distance_violation'] = consistent_distance_violation
            self.__results['distance_violations_vs_models'] = distance_violations_vs_models

            for rest_key, viol_per_model in self.__distRestViolDict.items():
                for m in range(1, self.__total_models + 1):
                    err = viol_per_model[m]

                    if err is not None and err > 0.0:
                        comb_key = self.__distRestViolCombKeyDict[rest_key][m]
                        combination_id = comb_key['combination_id']
                        member_id = comb_key['member_id']

                        r = next(r for r in self.__distRestDict[rest_key]
                                 if r['combination_id'] == combination_id and r['member_id'] == member_id)
                        t = r['distance_type']
                        s = r['distance_sub_type']
                        b = r['bond_flag']

                        distance_violations_in_models[m][t][s][b].append(err)
                        distance_violations_in_models[m][any_type][s][b].append(err)

            self.__results['distance_violations_in_models'] = distance_violations_in_models

            dist_range = []

            residual_distance_violation = {}
            for idx, beg_err_bin in enumerate(NMR_VTF_DIST_ERR_BINS):
                if idx == len(NMR_VTF_DIST_ERR_BINS) - 1:
                    end_err_bin = None
                    dist_err_range = f">{beg_err_bin}"
                else:
                    end_err_bin = NMR_VTF_DIST_ERR_BINS[idx + 1]
                    dist_err_range = f"{beg_err_bin}-{end_err_bin}"

                dist_range.append(dist_err_range)
                residual_distance_violation[dist_err_range] =\
                    get_violation_statistics_for_each_bin(beg_err_bin, end_err_bin,
                                                          self.__total_models,
                                                          self.__distRestViolDict)

            self.__results['key_lists']['dist_range'] = dist_range
            self.__results['residual_distance_violation'] = residual_distance_violation

            most_violated_distance = []
            for rest_key, viol_per_model in self.__distRestViolDict.items():
                vm = get_violated_model_ids(viol_per_model)

                if len(vm) > 1:
                    e = np.array([err for err in viol_per_model.values() if err is not None and err > 0.0])

                    comb_keys = set()
                    for _m in set(vm):
                        comb_key = self.__distRestViolCombKeyDict[rest_key][_m]
                        combination_id = comb_key['combination_id']
                        member_id = comb_key['member_id']
                        comb_keys.add((combination_id, member_id))

                    for r in self.__distRestDict[rest_key]:
                        comb_key = (r['combination_id'], r['member_id'])

                        if comb_key in comb_keys:
                            most_violated_distance.append([rest_key,
                                                           r['atom_key_1'],
                                                           r['atom_key_2'],
                                                           r['distance_type'],
                                                           r['distance_sub_type'],
                                                           r['bond_flag'],
                                                           len(vm),
                                                           vm,
                                                           np.min(e),
                                                           np.max(e),
                                                           np.mean(e),
                                                           np.std(e),
                                                           np.median(e)])

            self.__results['most_violated_distance'] =\
                sorted(most_violated_distance, reverse=True, key=itemgetter(6, 10))

            all_distance_violations = []
            for rest_key, viol_per_model in self.__distRestViolDict.items():
                for m in range(1, self.__total_models + 1):
                    err = viol_per_model[m]

                    if err is not None and err > 0.0:
                        comb_key = self.__distRestViolCombKeyDict[rest_key][m]
                        combination_id = comb_key['combination_id']
                        member_id = comb_key['member_id']

                        for r in self.__distRestDict[rest_key]:
                            if r['combination_id'] == combination_id and r['member_id'] == member_id:
                                all_distance_violations.append([rest_key,
                                                                r['atom_key_1'],
                                                                r['atom_key_2'],
                                                                m,
                                                                r['distance_type'],
                                                                r['distance_sub_type'],
                                                                r['bond_flag'],
                                                                err])

            self.__results['all_distance_violations'] =\
                sorted(all_distance_violations, reverse=True, key=itemgetter(7, 0))

            dist_violation_seq = {}
            for seq_key, rest_keys in self.__distRestSeqDict.items():
                for m in range(1, self.__total_models + 1):
                    _seq_key = (seq_key[0], seq_key[1], seq_key[2], m)

                    if _seq_key not in dist_violation_seq:
                        dist_violation_seq[_seq_key] = []

                    for rest_key in rest_keys:
                        comb_key = self.__distRestViolCombKeyDict[rest_key][m]
                        if comb_key is None:
                            continue
                        combination_id = comb_key['combination_id']
                        member_id = comb_key['member_id']

                        atom_ids_1 = atom_ids_2 = []
                        distance_type = None

                        for r in self.__distRestDict[rest_key]:
                            if r['combination_id'] == combination_id and r['member_id'] == member_id:
                                atom_ids_1.append(r['atom_key_1'][3])
                                seq_key_1 = (r['atom_key_1'][0], r['atom_key_1'][1], r['atom_key_1'][2])
                                atom_ids_2.append(r['atom_key_2'][3])
                                seq_key_2 = (r['atom_key_2'][0], r['atom_key_2'][1], r['atom_key_2'][2])

                                if distance_type is None:
                                    distance_type = r['distance_type']
                                    distance_sub_type = r['distance_sub_type']
                                    bond_flag = r['bond_flag']

                        atom_ids_1 = list(set(atom_ids_1))
                        atom_ids_2 = list(set(atom_ids_2))

                        if seq_key_1 == seq_key_2:
                            atom_ids = atom_ids_1 + atom_ids_2
                        elif seq_key_1 == seq_key:
                            atom_ids = atom_ids_1
                        elif seq_key_2 == seq_key:
                            atom_ids = atom_ids_2
                        else:
                            if self.__verbose:
                                self.__lfh.write(f"Nothing matches with sequence, {seq_key_1}, {seq_key_2}, {atom_ids_1}, {atom_ids_2}, {seq_key}\n")
                            continue

                        err = self.__distRestViolDict[rest_key][m]

                        if err is not None and err > 0.0:
                            dist_violation_seq[_seq_key].append([rest_key[0],
                                                                 rest_key[1],
                                                                 atom_ids,
                                                                 distance_type,
                                                                 distance_sub_type,
                                                                 bond_flag,
                                                                 err])

            self.__results['dist_violation_seq'] = dist_violation_seq

            return True

        except Exception as e:
            self.__lfh.write(f"+NmrVrptUtility.__summarizeDistanceRestraintValidation() ++ Error  - {str(e)}\n")

        return False

    def __summarizeDihedralAngleRestraintValidation(self):
        """ Summarize dihedral angle restraint validation results.
            @author: Masashi Yokochi
            @note: Derived from wwpdb.apps.validation.src.RestraintValidation.BMRBRestraintsAnalysis.generate_output,
                   written by Kumaran Baskaran
            @change: class method, improve readability of restraints, support combinational restraints, performance optimization
        """

        if self.__has_prev_results:
            return True

        try:

            self.__results['angle'] = self.__dihedRestViolDict is not None and len(self.__dihedRestViolDict) > 0

            if not self.__results['angle']:
                return True

            self.__results['angle_seq_dict'] = self.__dihedRestSeqDict
            self.__results['unmapped_angle'] = self.__dihedRestUnmapped

            any_type = 'Total'

            try:
                angle_type = list(set(r_list[0]['angle_type'] for r_list in self.__dihedRestDict.values())) + [any_type]
            except IndexError:
                self.__lfh("Restraints validation failed due to data error in the dihedral angle restraints.\n")
                return False

            self.__results['key_lists']['angle_type'] = angle_type

            angle_summary = {}
            angle_violation = {}

            consistent_angle_violation = {}
            angle_violations_vs_models = {}
            angle_violations_in_models = {}

            for m in range(1, self.__total_models + 1):
                angle_violations_in_models[m] = {}

                for t in angle_type:
                    angle_summary[t] = 0
                    angle_violation[t] = 0
                    consistent_angle_violation[t] = 0
                    angle_violations_vs_models[t] = [0] * (self.__total_models + 1)
                    angle_violations_in_models[m][t] = []

            for rest_key, restraints in self.__dihedRestDict.items():
                comb_key = self.__dihedRestViolCombKeyDict[rest_key][self.__representative_model_id]
                if comb_key is not None:
                    combination_id = comb_key['combination_id']

                    r = next(r for r in restraints
                             if r['combination_id'] == combination_id)
                else:
                    r = restraints[0]

                t = r['angle_type']

                angle_summary[t] += 1
                angle_summary[any_type] += 1

                len_vm = len(get_violated_model_ids(self.__dihedRestViolDict[rest_key]))

                if len_vm > 0:
                    angle_violation[t] += 1
                    angle_violation[any_type] += 1

                if len_vm == self.__total_models:
                    consistent_angle_violation[t] += 1
                    consistent_angle_violation[any_type] += 1

                angle_violations_vs_models[t][len_vm] += 1
                angle_violations_vs_models[any_type][len_vm] += 1

            self.__results['angle_summary'] = angle_summary
            self.__results['angle_violation'] = angle_violation
            self.__results['consistent_angle_violation'] = consistent_angle_violation
            self.__results['angle_violations_vs_models'] = angle_violations_vs_models

            for rest_key, viol_per_model in self.__dihedRestViolDict.items():
                for m in range(1, self.__total_models + 1):
                    err = viol_per_model[m]

                    if err is not None and err > 0.0:
                        comb_key = self.__dihedRestViolCombKeyDict[rest_key][m]
                        combination_id = comb_key['combination_id']

                        r = next(r for r in self.__dihedRestDict[rest_key]
                                 if r['combination_id'] == combination_id)
                        t = r['angle_type']

                        angle_violations_in_models[m][t].append(err)
                        angle_violations_in_models[m][any_type].append(err)

            self.__results['angle_violations_in_models'] = angle_violations_in_models

            angle_range = []

            residual_angle_violation = {}
            for idx, beg_err_bin in enumerate(NMR_VTF_DIHED_ERR_BINS):
                if idx == len(NMR_VTF_DIHED_ERR_BINS) - 1:
                    end_err_bin = None
                    dihed_err_range = f">{beg_err_bin}"
                else:
                    end_err_bin = NMR_VTF_DIHED_ERR_BINS[idx + 1]
                    dihed_err_range = f"{beg_err_bin}-{end_err_bin}"

                angle_range.append(dihed_err_range)
                residual_angle_violation[dihed_err_range] =\
                    get_violation_statistics_for_each_bin(beg_err_bin, end_err_bin,
                                                          self.__total_models,
                                                          self.__dihedRestViolDict)

            self.__results['key_lists']['angle_range'] = angle_range
            self.__results['residual_angle_violation'] = residual_angle_violation

            most_violated_angle = []
            for rest_key, viol_per_model in self.__dihedRestViolDict.items():
                vm = get_violated_model_ids(viol_per_model)

                if len(vm) > 1:
                    e = np.array([err for err in viol_per_model.values() if err is not None and err > 0.0])

                    comb_keys = set()
                    for _m in set(vm):
                        comb_key = self.__dihedRestViolCombKeyDict[rest_key][_m]
                        combination_id = comb_key['combination_id']
                        comb_keys.add(combination_id)

                    for r in self.__dihedRestDict[rest_key]:
                        comb_key = r['combination_id']

                        if comb_key in comb_keys:
                            most_violated_angle.append([rest_key,
                                                        r['atom_key_1'],
                                                        r['atom_key_2'],
                                                        r['atom_key_3'],
                                                        r['atom_key_4'],
                                                        r['angle_type'],
                                                        len(vm),
                                                        vm,
                                                        np.min(e),
                                                        np.max(e),
                                                        np.mean(e),
                                                        np.std(e),
                                                        np.median(e)])

            self.__results['most_violated_angle'] =\
                sorted(most_violated_angle, reverse=True, key=itemgetter(6, 10))

            all_angle_violations = []
            for rest_key, viol_per_model in self.__dihedRestViolDict.items():
                for m in range(1, self.__total_models + 1):
                    err = viol_per_model[m]

                    if err is not None and err > 0.0:
                        comb_key = self.__dihedRestViolCombKeyDict[rest_key][m]
                        combination_id = comb_key['combination_id']

                        for r in self.__dihedRestDict[rest_key]:
                            if r['combination_id'] == combination_id:
                                all_angle_violations.append([rest_key,
                                                            r['atom_key_1'],
                                                            r['atom_key_2'],
                                                            r['atom_key_3'],
                                                            r['atom_key_4'],
                                                            m,
                                                            r['angle_type'],
                                                            err])

            self.__results['all_angle_violations'] =\
                sorted(all_angle_violations, reverse=True, key=itemgetter(7, 0))

            angle_violation_seq = {}
            for seq_key, rest_keys in self.__dihedRestSeqDict.items():
                for m in range(1, self.__total_models + 1):
                    _seq_key = (seq_key[0], seq_key[1], seq_key[2], m)

                    if _seq_key not in angle_violation_seq:
                        angle_violation_seq[_seq_key] = []

                    for rest_key in rest_keys:
                        comb_key = self.__dihedRestViolCombKeyDict[rest_key][m]
                        if comb_key is None:
                            continue
                        combination_id = comb_key['combination_id']

                        atom_ids = []
                        angle_type = None

                        for r in self.__dihedRestDict[rest_key]:
                            if r['combination_id'] == combination_id:
                                seq_key_1 = (r['atom_key_1'][0], r['atom_key_1'][1], r['atom_key_1'][2])
                                if seq_key_1 == seq_key:
                                    atom_ids.append(r['atom_key_1'][3])
                                seq_key_2 = (r['atom_key_2'][0], r['atom_key_2'][1], r['atom_key_2'][2])
                                if seq_key_2 == seq_key:
                                    atom_ids.append(r['atom_key_2'][3])
                                seq_key_3 = (r['atom_key_3'][0], r['atom_key_3'][1], r['atom_key_3'][2])
                                if seq_key_3 == seq_key:
                                    atom_ids.append(r['atom_key_3'][3])
                                seq_key_4 = (r['atom_key_4'][0], r['atom_key_4'][1], r['atom_key_4'][2])
                                if seq_key_4 == seq_key:
                                    atom_ids.append(r['atom_key_4'][3])

                                if angle_type is None:
                                    angle_type = r['angle_type']

                        err = self.__dihedRestViolDict[rest_key][m]

                        if err is not None and err > 0.0:
                            angle_violation_seq[_seq_key].append([rest_key[0],
                                                                  rest_key[1],
                                                                  atom_ids,
                                                                  angle_type,
                                                                  err])

            self.__results['angle_violation_seq'] = angle_violation_seq

            return True

        except Exception as e:
            self.__lfh.write(f"+NmrVrptUtility.__summarizeDihedralAngleRestraintValidation() ++ Error  - {str(e)}\n")

        return False

    def __outputResultsAsPickleFileIfPossible(self):
        """ Output results if 'result_pickle_file_path' was set in output parameter.
        """

        cache_path = None
        if self.__resultsCacheName is not None:
            cache_path = os.path.join(self.__cacheDirPath, self.__resultsCacheName)

            if not os.path.exists(cache_path):
                write_as_pickle(self.__results, cache_path)

        if 'result_pickle_file_path' in self.__outputParamDict:
            pickle_file = self.__outputParamDict['result_pickle_file_path']

            if cache_path is None:
                write_as_pickle(self.__results, pickle_file)
                return True

            if os.path.exists(pickle_file):
                os.remove(pickle_file)

            os.symlink(cache_path, pickle_file)

        return True