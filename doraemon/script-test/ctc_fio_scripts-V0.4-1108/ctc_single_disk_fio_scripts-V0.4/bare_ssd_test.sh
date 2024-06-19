#!/bin/bash

if [[ $# -ne 1 ]];then
	echo "usage:$0 devname"
	echo "usage:$0 sdb"
	echo "usage:$0 nvme0n1"
	exit 1
fi

devname=$1
#Sequence read/write test including bandwidth/read/write 
./disk_fio_test.sh -B -d ${devname}
sleep 30s

#Random read/write test including randread/randwrite,mixrw 
./disk_fio_test.sh -R -d ${devname}
sleep 30s
