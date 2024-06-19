#!/bin/bash
# *****************************************************************************
# Version V0.1
# Author: zhouq32@chinatelecom.cn
# Filter result for single disk fio traversal test according to ctc io pattern
# *****************************************************************************
CPWD=$(cd $(dirname $0);pwd)
cd $CPWD
IS_SSD_FILTER=false
IS_HDD_FILTER=false
#IS_DISK_SEQ_RAND_FILTER=false
#IS_SSD_MIXRW_FILTER=false

usage()
{
    echo "$0 [-h help] [-S ssd_log_filter] [-D hdd_log_filter] [-d disk_symbol]"
    echo "examples:"
    echo "$0 -h, usage"
    echo "$0 -S -d nvme0n1, filter single nvme ssd fio log"
    echo "$0 -S -d sdb, filter single ssd fio log"
    echo "$0 -D -d sdb, filter single hdd fio log"
    exit 1
}
while getopts "hSDd:" arg
do
    case $arg in
        h)
        usage;;
        S)
        IS_SSD_FILTER=true;;
        D)
        IS_HDD_FILTER=true;;
        d)
        DEV_LIST=${OPTARG};;
        *)
        usage;;
    esac
done

filter_single_ssd_bandwidth_log()
{
    echo "bandwidth_test_data," >> filter_single_ssd_bandwidth.csv
    echo -e "bandwidth:bs=128k numjobs=1 iodepth=256," >> filter_single_ssd_bandwidth.csv
    for rw in read write
    do
        echo -n "${rw}," >> filter_single_ssd_bandwidth.csv
        bandWidth=$(cat ${DEV_LIST}_BW_${rw}.log |grep -A4 "${DEV_LIST}_BW_${rw}:\ (groupid=" |grep IOPS |grep -Eo "[0-9]+\.?[0-9]*[G|M|K]?B/s")
        echo -n "$bandWidth," >> filter_single_ssd_bandwidth.csv
        echo "" >> filter_single_ssd_bandwidth.csv
    done
    echo "" >> filter_single_ssd_bandwidth.csv
}

filter_single_disk_seq_rand_rw_log()
{   
    for rw in read write randread randwrite
    do
        echo "${rw}_test_data," >> filter_single_disk_${rw}.csv  
        # ******************************************
        # start to filter rw iops
        echo -e "iops:bs_thread_iodepth," >> filter_single_disk_${rw}.csv
        echo -n "bs," >> filter_single_disk_${rw}.csv
        for thread in 1 2 4 8
        do
            for iodepth in 1 2 4 8 16 32 64 128 256
            do
                echo -n "${thread}_${iodepth}," >> filter_single_disk_${rw}.csv
            done
        done
        echo "" >> filter_single_disk_${rw}.csv
        # filter rw iops
        for bs in 4k 8k 16k 32k 64k 128k 256k 1m
        do
            echo -n "$bs," >> filter_single_disk_${rw}.csv
            for thread in 1 2 4 8
            do
                for iodepth in 1 2 4 8 16 32 64 128 256
                do
                    iops=$(cat ${DEV_LIST}_${rw}.log |grep -A10 "${rw}_${bs}_${thread}_${iodepth}:\ (groupid=" |grep IOPS |tr -d ' ' \
					|awk -F"," '{print $1}' |awk -F"=" '{print $2}')
                    echo -n "${iops}," >> filter_single_disk_${rw}.csv
                done
            done
            echo "" >> filter_single_disk_${rw}.csv
        done
        # *******************************************
        # start to filter rw latency
        echo -e "latency:bs_thread_iodepth," >> filter_single_disk_${rw}.csv
        echo -n "bs," >> filter_single_disk_${rw}.csv
        for thread in 1 2 4 8
        do
            for iodepth in 1 2 4 8 16 32 64 128 256
            do
                echo -n "${thread}_${iodepth}," >> filter_single_disk_${rw}.csv
            done
        done
        echo "" >> filter_single_disk_${rw}.csv
        for bs in 4k 8k 16k 32k 64k 128k 256k 1m
        do
            echo -n "${bs}_min_lat," >> filter_single_disk_${rw}.csv
            # filter min latency
            for thread in 1 2 4 8
            do
                for iodepth in 1 2 4 8 16 32 64 128 256
                do         
                    minLatValue=$(cat ${DEV_LIST}_${rw}.log |grep -A10 "${rw}_${bs}_${thread}_${iodepth}:\ (groupid=" |grep -w lat |tr -d ' ' \
                    |awk -F"," '{print $1}' |awk -F"=" '{print $2}')
                    latUnit=$(cat ${DEV_LIST}_${rw}.log |grep -A10 "${rw}_${bs}_${thread}_${iodepth}:\ (groupid=" |grep -w lat |tr -d ' ' \
                    |awk -F"," '{print $1}' |grep -Eo "[u|m|n]?sec")
                    minLat=${minLatValue}${latUnit}
                    echo -n "$minLat," >> filter_single_disk_${rw}.csv
                done
            done
            echo "" >> filter_single_disk_${rw}.csv
            # *******************************************
            # filter average latency
            echo -n "${bs}_avg_lat," >> filter_single_disk_${rw}.csv
            for thread in 1 2 4 8
            do
                for iodepth in 1 2 4 8 16 32 64 128 256
                do
                    avgLatValue=$(cat ${DEV_LIST}_${rw}.log |grep -A10 "${rw}_${bs}_${thread}_${iodepth}:\ (groupid=" |grep -w lat |tr -d ' ' \
                    |awk -F"," '{print $(NF-1)}' |awk -F"=" '{print $2}')
                    avgLat=${avgLatValue}${latUnit}
                    echo -n "$avgLat," >> filter_single_disk_${rw}.csv
                done
            done
            echo "" >> filter_single_disk_${rw}.csv
            # ********************************************
            # filter average latency
            echo -n "${bs}_max_lat," >> filter_single_disk_${rw}.csv
            for thread in 1 2 4 8
            do
                for iodepth in 1 2 4 8 16 32 64 128 256
                do
                    maxLatValue=$(cat ${DEV_LIST}_${rw}.log |grep -A10 "${rw}_${bs}_${thread}_${iodepth}:\ (groupid=" |grep -w lat |tr -d ' ' \
                    |awk -F"," '{print $2}' |awk -F"=" '{print $2}')
                    maxLat=${avgLatValue}${latUnit}
                    echo -n "$maxLat," >> filter_single_disk_${rw}.csv
                done
            done
            echo "" >> filter_single_disk_${rw}.csv
            # *********************************************
            # filter 99.99th Qos latency
            echo -n "${bs}_99.99th_lat," >> filter_single_disk_${rw}.csv
            for thread in 1 2 4 8
            do
                for iodepth in 1 2 4 8 16 32 64 128 256
                do
                    qos49LatValue=$(cat ${DEV_LIST}_${rw}.log |sed -n "/${rw}_${bs}_${thread}_${iodepth}:\ (groupid=/,/bw/p" \
					|grep -Eo "99.99th=[[[:space:]]*[0-9]+]" |awk -F"=" '{print $2}' |sed -e 's/\[//' -e 's/\]//' -e 's/[ ]*//')
                    qos49LatUnit=$(cat ${DEV_LIST}_${rw}.log |grep -A10 "${rw}_${bs}_${thread}_${iodepth}:\ (groupid=" \
					|grep "clat percentiles" |grep -Eo "[u|m|n]?sec")
                    qos49Lat=${qos49LatValue}${qos49LatUnit}
                    echo -n "$qos49Lat," >> filter_single_disk_${rw}.csv
                done
            done
            echo "" >> filter_single_disk_${rw}.csv
        done
        echo "" >> filter_single_disk_${rw}.csv
    done  
}

filter_single_ssd_mixrw_log()
{
    echo "mixrw_test_data," >> filter_single_ssd_mixrw.csv
    echo -e "iops:mixed read|write thread_iodepth," >> filter_single_ssd_mixrw.csv
    echo "bs_ratio,read_8_128,write_8_128," >> filter_single_ssd_mixrw.csv
    for bs in 4k 8k 16k 32k
    do
        for ratio in 10 20 30 40 50 60 70 80 90
        do
            readIops=$(cat ${DEV_LIST}_${bs}_${ratio}_mixrw_iops.log |grep "read:" |grep IOPS |tr -d ' ' |awk -F"," '{print $1}' |awk -F"=" '{print $2}')
            writeIops=$(cat ${DEV_LIST}_${bs}_${ratio}_mixrw_iops.log |grep "write:" |grep IOPS |tr -d ' ' |awk -F"," '{print $1}' |awk -F"=" '{print $2}')
            echo -n "${bs}_${ratio},$readIops,$writeIops," >> filter_single_ssd_mixrw.csv
            echo "" >> filter_single_ssd_mixrw.csv
        done       
    done
    echo "" >> filter_single_ssd_mixrw.csv
}

if [[ $# -eq 0 ]];then
    usage
fi

if ${IS_SSD_FILTER};then
    filter_single_ssd_bandwidth_log
    filter_single_disk_seq_rand_rw_log
    filter_single_ssd_mixrw_log
fi

if ${IS_HDD_FILTER};then
    filter_single_disk_seq_rand_rw_log
fi
