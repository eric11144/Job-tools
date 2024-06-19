#!/bin/bash
#********************************************************************************************************************************
#make sure result_single_ssd_traversal_log_filter.sh and single_disk_traversal_log_filter.sh is located in same path of testlog
#********************************************************************************************************************************
if [[ $# -ne 1 ]];then
    echo "$0 devname"
    echo "example:"
    echo "$0 nvme0n1"
    echo "$0 sdb"
    exit 1
fi

dev=$1
rm -f filter_single*.csv
./single_disk_traversal_log_filter.sh -S -d $1
cat filter_single_ssd_bandwidth.csv filter_single_disk_read.csv filter_single_disk_write.csv filter_single_disk_randread.csv \
filter_single_disk_randwrite.csv filter_single_ssd_mixrw.csv > filter_single_ssd_Result.csv
