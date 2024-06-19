#!/bin/bash

if [[ $# -ne 1 ]];then
	echo "usage:$0 devname"
	echo "usage:$0 sdb"
	exit 1
fi

devname=$1
#Sequence read/write test
./disk_fio_test.sh -b -d ${devname}
sleep 30s

#Random read/write test
./disk_fio_test.sh -r -d ${devname}
sleep 30s
