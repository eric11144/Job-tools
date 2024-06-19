#!/bin/bash

if [[ $# -eq 0 ]];then
	echo "usage: ssd fio stress test"
	echo "usage:$0 devname"
	echo "usage:$0 sdb"
	exit 1
fi

devname=$1
#hddfio stress test
./disk_fio_test.sh -D -d ${devname}
