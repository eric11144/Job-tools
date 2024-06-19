#!/bin/bash

if [[ $# -ne 1 ]];then
	echo "usage:$0 devname"
	echo "example:$0 sdb"
	echo "example:$0 nvme0n1"
	exit 1
fi

devname=$1
#Sequence write/read test of ssd
./raw_disk_fio_test.sh -b -d $devname  
sleep 30s

#Random write/read test of ssd
./raw_disk_fio_test.sh -B -d $devname
sleep 30s
