import os,sys,traceback
import shutil
from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility

def getNmrDataNefFile(workingDirPath, pdb_id, inputNmrDataStrFile, outputNmrDataNetFile):
    """ get nmr-data-nef file
    """
    try:
        logOutPath1 = os.path.join(workingDirPath, pdb_id + "-logstrstr.json")
        logOutPath2 = os.path.join(workingDirPath, pdb_id + "-logstrnef.json")
        #
        for filePath in ( logOutPath1, logOutPath2 ):
            if os.access(filePath, os.F_OK):
                os.remove(filePath)
            #
        #
        np = NmrDpUtility()
        np.setSource(inputNmrDataStrFile)
        np.addOutput(name="nef_file_path", value=outputNmrDataNetFile, type="file")
        np.addOutput(name="report_file_path", value=logOutPath2, type="file")
        np.addOutput(name="insert_entry_id_to_loops", value=True, type="param")
        np.addOutput(name="resolve_conflict", value=True, type="param")
        np.setDestination(inputNmrDataStrFile + "~")
        np.setLog(logOutPath1)
        np.setVerbose(False)
        np.op("nmr-str2nef-release")
    except:
        traceback.print_exc(file=sys.stderr)
    #

if __name__ == '__main__':
    dirPath = os.getcwd()
    shutil.copy(os.path.join(dirPath, "0037_nmr-data.str.bk"), os.path.join(dirPath, "0037_nmr-data.str"))
    getNmrDataNefFile(dirPath, "0037", os.path.join(dirPath, "0037_nmr-data.str"), os.path.join(dirPath, "0037_nmr-data.nef"))

