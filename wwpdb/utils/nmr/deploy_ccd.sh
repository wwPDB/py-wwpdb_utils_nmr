#!/bin/bash

SRC_DIR=$PWD/ftp.pdbj.org/pub/pdb/refdata/chem_comp

if [ ! -d $SRC_DIR ] ; then
 ./update_ccd.sh
fi

DST_DIR=ligand_dict

if [ ! -d $DST_DIR ] ; then
 mkdir $DST_DIR
fi

function mk_div_dir() {
 if [ ! -d $1 ] ; then
  [ -e $1 ] && rm -f $1
  mkdir -p $1
 fi
}

function gunzip_in_div_dir() {
 cp -f $1 $2 && gunzip -f $2/`basename $1`
}

find $SRC_DIR -name *.cif > file_list

while read cif_file
do

 cc=`basename $cif_file .cif`
 div_dir=$DST_DIR/${cc:0:1}/$cc

 if [ ! -L $div_dir/$cc.cif ] || [ ! -e $div_dir/$cc.cif ] ; then
  rm -f $div_dir/$cc.cif
 fi

 if [ ! -e $div_dir/$cc.cif ] ; then

  mk_div_dir $div_dir
  ( cd $div_dir ; ln -s $cif_file . )

 fi

done < file_list

rm -f file_list

