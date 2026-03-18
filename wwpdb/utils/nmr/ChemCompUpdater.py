##
# File: ChemCompUpdater.py
# Date: 02-Dec-2025
#
# Updates:
##
""" Chemical component dictionary updater for standalone mode of wwpdb.utils.nmr package.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"

import argparse
import datetime
import gzip
import logging
import os
import shutil

from dateutil.parser import parse as parsedate

from mmcif.io.PdbxReader import PdbxReader
from mmcif.io.PdbxWriter import PdbxWriter

import requests


def uncompress_gzip_file(inPath: str, outPath: str):
    """ Uncompress a given gzip file.
    """

    with gzip.open(inPath, mode='rt') as ifh, \
         open(outPath, 'w', encoding='utf-8') as ofh:
        for line in ifh:
            ofh.write(line)


class ChemCompUpdater:
    """ Update chemical component dictionary (CCD) and locate them OneDep compatible directory trees.
    """

    def __init__(self, force: bool = False):
        self.__components_cif = 'components.cif'
        self.__components_cif_gz = self.__components_cif + '.gz'
        self.__components_cif_path = os.path.join(os.path.dirname(__file__), self.__components_cif)
        self.__components_cif_gz_path = os.path.join(os.path.dirname(__file__), self.__components_cif_gz)
        self.__url_for_components = 'https://files.wwpdb.org/pub/pdb/data/monomers/' + self.__components_cif_gz
        self.__work_dir = os.path.join(os.path.dirname(__file__), 'ligand_dict')

        # DATAQUALITY-2203
        # self.__src_gsh_cif = os.path.join(self.__work_dir, 'GSH.cif')
        # self.__has_gsh_cif = os.path.exists(self.__src_gsh_cif)

        # if self.__has_gsh_cif:
        #     self.__dst_gsh_cif = os.path.join(self.__work_dir, 'G', 'GSH', 'GSH.cif')
        #     self.__tmp_gsh_cif = os.path.join(os.path.dirname(__file__), 'GSH.cif')

        self.__force = force

        self.update()

    def deploy(self):
        """ Deploy chemical component dictionary (CCD) into OneDep compatible directory trees.
        """

        try:

            # if self.__has_gsh_cif:
            #     shutil.copyfile(self.__src_gsh_cif, self.__tmp_gsh_cif)

            if os.path.isdir(self.__work_dir):
                shutil.rmtree(self.__work_dir)

            os.mkdir(self.__work_dir)

            # if self.__has_gsh_cif:
            #     shutil.copyfile(self.__tmp_gsh_cif, self.__src_gsh_cif)

            print(f'Uncompressing {self.__components_cif_gz!r} ...')

            uncompress_gzip_file(self.__components_cif_gz_path, self.__components_cif_path)

            print(f'Deplying CCD to {self.__work_dir!r} ...')

            dBlockList = []

            with open(self.__components_cif_path, 'r', encoding='utf-8') as ifh:
                pRd = PdbxReader(ifh)
                pRd.read(dBlockList)

            for dBlock in dBlockList:
                compId = dBlock.getName()

                subDir = os.path.join(self.__work_dir, compId[-2:] if len(compId) > 3 else compId[0], compId)

                os.makedirs(subDir, exist_ok=True)

                outPath = os.path.join(subDir, compId + '.cif')

                with open(outPath, 'w', encoding='utf-8') as ofh:
                    pdbxW = PdbxWriter(ofh)
                    pdbxW.write([dBlock])

            # if self.__has_gsh_cif:
            #     shutil.move(self.__src_gsh_cif, self.__dst_gsh_cif)

            os.remove(self.__components_cif_path)

            print(f'{self.__work_dir!r} is up-to-date.')

        except IOError as e:
            logging.error(str(e))

    def download(self):
        """ Download Chemical Component Dictionary (CCD),
        """

        try:
            print(f'Downloading {self.__url_for_components} ...')

            r = requests.get(self.__url_for_components, timeout=300.0)
            with open(os.path.join(self.__components_cif_gz_path), 'wb') as f:
                f.write(r.content)

        except Exception as e:  # pylint: disable=broad-exception-caught
            logging.error(str(e))

    def update(self):
        """ Update Chemical Component Dictionary (CCD) with time-stamp check.
        """

        try:
            print(f'HEAD {self.__url_for_components}')

            r = requests.head(self.__url_for_components, timeout=5.0)

            if r.status_code != 200:
                raise RuntimeError(f'Request to {self.__url_for_components} returned status code {r.status_code}')

        except Exception as e:  # pylint: disable=broad-exception-caught
            logging.error(str(e))
            return

        url_last_modified = parsedate(r.headers['Last-Modified']).astimezone()

        if os.path.exists(self.__components_cif_gz_path):
            file_last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(self.__components_cif_gz_path)).astimezone()
            if url_last_modified > file_last_modified:
                self.download()
                self.deploy()

            elif not os.path.isdir(self.__work_dir) or self.__force:
                self.deploy()

            else:
                print(f"{self.__components_cif_gz!r} is up-to-date. (use '--force' argument)")

        else:
            self.download()
            self.deploy()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', help='force update', action='store_true')

    parse_args = parser.parse_args()

    updater = ChemCompUpdater(parse_args.force)
