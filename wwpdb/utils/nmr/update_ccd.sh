#!/bin/bash

CC_CIF_URL=data.pdbj.org::ftp/refdata/chem_comp

DST_DIR=chem_comp

DELETE=

ARGV=`getopt --long -o "d" "$@"`
eval set -- "$ARGV"
while true ; do
 case "$1" in
 -d)
  DELETE=--delete
 ;;
 *)
  break
 ;;
 esac
 shift
done

rsync -avz $DELETE $CC_CIF_URL/* $DST_DIR

cif_file_total=cif_cc_file_total

if [ ! -e $cif_file_total ] ; then

 last=0

 if [ -e $cif_file_total ] ; then
  last=`cat $cif_file_total`
 fi

 total=`find $DST_DIR -name '*.cif' | wc -l 2> /dev/null`

 if [ $total = $last ] ; then

  echo $DST_DIR" is up-to-date."

 else

  echo $total > $cif_file_total

 fi

fi

