#!/bin/bash

MAXPROCS=`cat /proc/cpuinfo 2> /dev/null | grep 'cpu cores' | wc -l 2> /dev/null`

if [ $MAXPROCS = 0 ] ; then
 MAXPROCS=1
fi

CC_CIF_URL=ftp.pdbj.org/pub/pdb/refdata/chem_comp
MMCIF_CC=pub/pdb/refdata/chem_comp

if [ ! `which aria2c` ] ; then

 echo "aria2c: command not found..."
 echo "Please install aria2 (https://aria2.github.io)."
 exit 1

fi

MTIME=

ARGV=`getopt --long -o "m:" "$@"`
eval set -- "$ARGV"
while true ; do
 case "$1" in
 -m)
  MTIME=$2
  shift
 ;;
 *)
  break
 ;;
 esac
 shift
done

DB_NAME=chem_comp

SRC_DIR=$CC_CIF_URL

weekday=`date -u +"%w"`

PDB_MIRROR=ftp.pdbj.org

mkdir -p $SRC_DIR

if [ $weekday -ge 1 ] && [ $weekday -le 4 ] ; then

 components_cif=components.cif
 components_cif_all=components_cif_all
 components_cif_old=components_cif_old
 components_cif_del=components_cif_del
 components_cif_new=components_cif_new
 components_cif_list=components_cif_list
 components_cif_url=${SRC_DIR//\//\\\/}

 rm -f $components_cif* $components_cif_url

 wget ftp://$PDB_MIRROR/pub/pdb/data/monomers/$components_cif.gz && gunzip $components_cif.gz
 grep '^data_' $components_cif | cut -d '_' -f 2 | sort > $components_cif_all
 find $SRC_DIR -name '*.cif' -size 0 -delete
 find $SRC_DIR -name '*.cif' | cut -d '/' -f 6 | cut -d '.' -f 1 | sort > $components_cif_old
 comm -23 $components_cif_all $components_cif_old > $components_cif_new

 comm -13 $components_cif_all $components_cif_old > $components_cif_del

 rm -f $components_cif_list
 while read cc_id
 do
  echo ftp://$SRC_DIR/${cc_id: -1}/${cc_id}/${cc_id}.cif >> $components_cif_list
 done < $components_cif_new
 if [ -e $components_cif_list ] ; then
  aria2c -i $components_cif_list -j $MAXPROCS -d $SRC_DIR --allow-overwrite=true --auto-file-renaming=false
 fi

 rm -f $components_cif $components_cif_list $components_cif_all $components_cif_old $components_cif_new $components_cif_del

fi

cif_file_total=cif_cc_file_total

if [ -z $MTIME ] ; then
 MTIME=-4
fi

updated=`find $SRC_DIR -name "*.cif" -mtime $MTIME | wc -l 2> /dev/null`

if [ $updated = 0 ] || [ ! -e $cif_file_total ] ; then

 last=0

 if [ -e $cif_file_total ] ; then
  last=`cat $cif_file_total`
 fi

 total=`find $SRC_DIR -name '*.cif' | wc -l 2> /dev/null`

 if [ $total = $last ] ; then

  echo $DB_NAME" ("$SRC_DIR") is up-to-date."

 else

  echo $total > $cif_file_total

 fi

fi

