#!/bin/bash

if [[ $# -ne 1 ]];then
	echo "usage:$0 devname"
	echo "example:$0 sdb"
	echo "example:$0 nvme0n1"
	exit 1
fi

devname=$1

# Sequence write/read test of ssd with binding cpus automatically
./raw_disk_fio_test.sh -d $devname -n  
wait

# Random write/read test of ssd with binding cpus autimatically
./raw_disk_fio_test.sh -d $devname -N
wait