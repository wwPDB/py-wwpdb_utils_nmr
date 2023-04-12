import os
import tarfile
import shutil
import sys
import string
import random
import optparse

from memops.api import Implementation
from memops.general.Io import loadProject
from ccp.api.nmr.NmrEntry import Entry, NmrEntryStore
from ccpnmr.format.converters.PdbFormat import PdbFormat
from pdbe.nmrStar.IO.NmrStarExport import NmrStarExport

class CcpnConversionException( Exception ):
    """
    @deprecated: This class has never been implemented.
    """

    def __init__(s,e):
        print("CCpnConversionException")
        print(e)
        s.e = e

    def __str__(s):
        return "CCpnConversionException: %s " % s.e

    def __repr__(s):
        return s.__str__()

class CcpnProject:
    """
    @deprecated: This class has never been implemented.
    """

    def __init__(s,ccpn = None, star = None, pdb = None, uniq = None):

        s.projectFile = ccpn
        s.outputPdbFile = pdb
        s.outputStarFile = star
        s.tempDir = os.path.dirname(pdb)
        s.uniq = uniq

        s.currPath = os.getcwd()

        s.status = {
            'expandProject' : None,
            'openProject'   : None,
            'exportCoordinates' : None,
            'exportShifts'  : None,
            'writeShiftMapping'  : None
            }

    def process(s):
        s.status['expandProject'] = s.expandProject()
        if not s.status['expandProject'] == 'Success': raise CcpnConversionException('expandProject')

        s.status['openProject'] = s.openProject()
        if not s.status['openProject'] == 'Success': raise CcpnConversionException('openProject')

        s.status['exportCoordinates'] = s.exportCoordinates()
        if not s.status['exportCoordinates'] == 'Success': raise CcpnConversionException('exportCoordinates')

        s.status['exportShifts'] = s.exportShifts()

        s.status['cleanup'] = s.cleanup()
        return s.status

    def cleanup(s):
        try:
            os.chdir( s.currPath )
            tempDir = s.projectPath
            shutil.rmtree(tempDir)
            s.project = None
        except:
            return "Failed to cleanup this RUN"
        return 'Success'

    def expandProject(s):
        #make new temp folder
        try:
          tempDir = os.path.join( s.tempDir, s.uniq )
          print('Making %s' % tempDir)
          if os.path.isdir(tempDir):
              shutil.rmtree(tempDir)
          os.mkdir(tempDir)
          print('Created temp dir')
        except Exception:
          return "Failed to create temporary folder"

        #Copy and extract project file
        try:
          print('Opening file %s' % s.projectFile)
          tf = tarfile.open( s.projectFile , 'r:gz')
          print('Opened file %s' % s.projectFile)
          members = tf.getmembers()
          ok = True
          for member in members:
             na = member.name
             if na[0] == '/' or na[0] == '\\' or '..' in na:
                ok = False
                break
          if not ok:
              return "Unsafe files in archive"

          for member in members:
              tf.extract(member, path = tempDir)

          #tf.extractall( tempDir )
          print('Extracted file %s' % s.projectFile)
          dirs = [d for d in os.listdir(tempDir) if os.path.isdir(os.path.join(tempDir, d))]
          print('dirs', dirs)
          if len(dirs) != 1:
              return "CCPN project file does not contain a single folder"
          s.projectPath = os.path.join( tempDir )
          s.projectName = os.path.join( dirs[0] )
          try: tf.close()
          except: pass
        except Exception as e:
          print(str(e))
          try: tf.close()
          except: pass
          return "Failed to extract CCPN project from file"

        return 'Success'

    def openProject(s):
        try:
            s.project = loadProject( os.path.join(s.projectPath,s.projectName) )
        except:
            return "Failed to open CCPN project"
        return 'Success'

    def exportCoordinates(s):
        try:
          se =  s.project.structureEnsembles
          if len(se) < 1:
              return "No structure ensembles found in the CCPN project"
          if len(se) > 1:
              return "More than 1 structure ensemble found in the CCPN project. Aborting."
          for see in se: structureList = list(see.models)
          pdbFormat = PdbFormat(s.project,None,verbose = 0)
          pdbFormat.writeCoordinates(s.outputPdbFile,
                                       structures = structureList,
                                     useOriginalData = True,
                                     resetMapping=False,
                                     minimalPrompts=True,
                                     addPdbHeader=True,
                                     version='3.20')
        except:
          return "Failed to write PDB file from CCPN project"
        return "Success"

    def exportShifts(s):
        try:
          entryStore = s.project.currentNmrEntryStore or s.project.findFirstNmrEntryStore()
          if not entryStore:
              return "No ECI entrystore found in the CCPN project"
          entry = entryStore.findFirstEntry()
          if not entry:
              return "No ECI entry found in the CCPN project"

          nmrStarExport = NmrStarExport(entry, nmrStarVersion='3.1')
          nmrStarExport.createFile(s.outputStarFile)
          nmrStarExport.writeFile()

        except:
          return "Failed to write Shifts to NMRSTAR file from CCPN project"

        return "Success"

    def writeShiftMapping(s):

        print("Writing shits mapping")
        pass

#if __name__ == "__main__":
#    parser = optparse.OptionParser( usage = 'usage: %prog [options]' )
#    parser.add_option('--ccpn', default=None, dest = 'ccpn', help='Path to input CCPN project (gzipped)')
#    parser.add_option('--pdb' , default=None, dest = 'pdb' , help='Path to output PDB file')
#    parser.add_option('--star', default=None, dest = 'star', help='Path to output NMR-STAR 3.1 file')
#    (options,args) = parser.parse_args()
#    for opt in [options.ccpn,options.pdb,options.star]:
#      if opt == None:
#          parser.print_help()
#          parser.error('Mandatory option not found...' )
#
#    uniq = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6)) + '_ccpn-convert'
#
#    CcpnProject(
#      ccpn = options.ccpn,
#      star = options.star,
#      pdb  = options.pdb,
#      uniq = uniq
#    ).process()
#
