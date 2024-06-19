#!/bin/bash

if [[ $# -eq 0 ]];then
	echo "usage: ssd fio stress test"
	echo "usage:$0 devname"
	echo "usage:$0 sdb"
	echo "usage:$0 nvme0n1"
	exit 1
fi

devname=$1
#ssd fio stress test
./disk_fio_test.sh -S -d ${devname}
