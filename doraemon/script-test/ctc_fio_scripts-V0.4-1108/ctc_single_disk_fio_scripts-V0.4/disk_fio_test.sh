#!/bin/bash
#********************************************************************************#
# Author: zhouqing
# This script is fio test for block device with different io pattern traversal
# Modified in 5/16/2023
# modified randwrite precondition loop=2 to loop=1
#********************************************************************************#

IS_SSD_STRESS=false
IS_HDD_STRESS=false
IS_SSD_BASE_SEQ=false
IS_SSD_BASE_RAND=false
IS_HDD_BASE_SEQ=false
IS_HDD_BASE_RAND=false
IO_ENGINE=libaio
FILE_SIZE=100%
path_to_fio=`which fio`

usage(){
	echo "$0 [-S|D] [-e io_engine] [-b|r] [-h] [-B|R]  [-d dev_name]"
	echo "-h usage"
	echo "-S ssd stress test"
	echo "-D hdd stress test"
	echo "-e ioengine type , default type is libaio"
	echo "-b hdd raw device sequence write/read test"
	echo "-r hdd raw device random write/read test"
	echo "-d the device full path(raw device) ,such as /dev/sdx"
	echo "-B ssd raw device sequence read/write test"
	echo "-R ssd raw device random read/write test"
	echo "example:"
	echo "	ssd raw device base_test_sequence:  nohup &>/dev/null $0 -B -d sdx &"
	echo "	ssd raw device base_test_random:  nohup &>/dev/null $0 -R -d sdx &"
	echo "	hdd raw device base_test_sequence:  nohup &>/dev/null $0 -b -d sdx &"
	echo "	hdd raw device base_test_random:  nohup &>/dev/null $0 -r -d sdx &"
	echo "	ssd raw device stress test:  nohup &>/dev/null $0 -S -d sdx &"
	echo "	hdd raw device stress test:  nohup &>/dev/null $0 -D -d sdx &"
	exit
}


while getopts "hSDbrBRe:d:" arg
do
	case $arg in
		h)
		usage;;
		S)
		IS_SSD_STRESS=true;;
		D)
		IS_HDD_STRESS=true;;
		b)
		IS_HDD_BASE_SEQ=true;;
		r)
		IS_HDD_BASE_RAND=true;;
		B)
		IS_SSD_BASE_SEQ=true;;
		R)
		IS_SSD_BASE_RAND=true;;
		e)
		IO_ENGINE=${OPTARG};;
		d)
		DEV_LIST=${OPTARG};;
	esac
done

PARA_LINE="--end_fsync=0 --group_reporting --direct=1 --ioengine=${IO_ENGINE}  -thread --time_based -buffer_compress_percentage=0 --invalidate=1 \
--norandommap --randrepeat=0 --exitall --size=${FILE_SIZE}"

PARA_LINE1="--end_fsync=0 --group_reporting --direct=1 --ioengine=${IO_ENGINE}  -thread --time_based -buffer_compress_percentage=0 --invalidate=1 \
--norandommap --randrepeat=0 --exitall"

ssd_fragment_sequence(){
    rm -f ${DEV_LIST}_fragment1.log
    #Full sequential write to let ssd be stable state before sequential test
    $path_to_fio --readwrite=write --bs=128k --iodepth=128 --numjobs=1 --loop=2 ${PARA_LINE1} --name=${DEV_LIST}_write_fragment1 --filename=/dev/${DEV_LIST} \
    |tee -a ssd_${DEV_LIST}_fragment1.log
}

ssd_fragment_random(){
    rm -f ${DEV_LIST}_fragment2.log
    #Full random write to let ssd be stable state before random test
    $path_to_fio --readwrite=randwrite --bs=$1 --iodepth=128 --numjobs=4 --runtime=6h ${PARA_LINE1} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_$1\_randwrite_fragment2 \
    |tee -a ssd_${DEV_LIST}_fragment2.log
}

ssd_base_test_sequence(){
    rm -f ${DEV_LIST}_fragment1.log ${DEV_LIST}_BW_read.log ${DEV_LIST}_BW_write.log ${DEV_LIST}_read.log ${DEV_LIST}_write.log
    #sequence precondition
    ssd_fragment_sequence
    wait
	
    #Bandwidth TEST
    $path_to_fio --readwrite=read --bs=128k --runtime=1800s --numjobs=1 --iodepth=256 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_BW_read |tee -a ${DEV_LIST}_BW_read.log
    sleep 30s
    $path_to_fio --readwrite=write --bs=128k --runtime=1800s --numjobs=1 --iodepth=256 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_BW_write |tee -a ${DEV_LIST}_BW_write.log
    sleep 30s

    #Block test with different BS,THREADS,QD 
    for BS in 4k 8k 16k 32k 64k 128k 256k 512k 1m
    do      
        for RW in read write
        do
            for THREADS in 1 2 4 8
            do
                for depth in 1 2 4 8 16 32 64 128 256
                do
                    $path_to_fio --readwrite=${RW} --bs=${BS} --numjobs=${THREADS} --iodepth=${depth} --ramp_time=60s --runtime=300s ${PARA_LINE} --filename=/dev/${DEV_LIST} \
		    --name=${RW}_${BS}_${THREADS}_${depth} | tee -a ${DEV_LIST}_${RW}.log
                    sleep 30s
                done
            done
        done
    done
}

ssd_base_test_random(){
    rm -f ${DEV_LIST}_fragment2.log ${DEV_LIST}_randread.log ${DEV_LIST}_randwrite.log ${DEV_LIST}_*_mixrw_iops.log
    #Block random wrire/read test with different BS,THREADS,QD 
    for BS in 4k 8k 16k 32k 64k 128k 256k 512k 1m
    do
        #<BS> randomwrite precondition
        ssd_fragment_random $BS
        wait
        for RW in randread randwrite
        do
            for THREADS in 1 2 4 8
            do
                for depth in 1 2 4 8 16 32 64 128 256
                do
                    $path_to_fio --readwrite=${RW} --bs=${BS} --numjobs=${THREADS} --iodepth=${depth} --ramp_time=60s --runtime=300s ${PARA_LINE} --filename=/dev/${DEV_LIST} \
		    --name=${RW}_${BS}_${THREADS}_${depth} | tee -a ${DEV_LIST}_${RW}.log
                    sleep 30s
                done
            done
        done
    done
	
    for blocksize in 4k 8k 16k 32k
    do
        ssd_fragment_random $blocksize
        wait 
        #mixed readwrite test		
        for ratio in 10 20 30 40 50 60 70 80 90
        do
            $path_to_fio --readwrite=randrw --rwmixread=${ratio} --bs=${blocksize} --ramp_time=60s --runtime=1800s --numjobs=4 --iodepth=64 ${PARA_LINE}  \
            --filename=/dev/${DEV_LIST} --name=${blocksize}_${ratio}_mixrw_iops | tee -a ${DEV_LIST}_${blocksize}_${ratio}_mixrw_iops.log
            sleep 30s
        done
    
        #consistency Test
        for RW in randread randwrite
        do
            iostat -xm 1 > ${DEV_LIST}_$blocksize\_$RW\_iops &
            $path_to_fio --readwrite=${RW} --bs=$blocksize --ramp_time=60s --runtime=3600s --numjobs=4 --iodepth=64 ${PARA_LINE}  --filename=/dev/${DEV_LIST} \
            --name=${DEV_LIST}_$blocksize\_$RW\_iops  | tee -a ${DEV_LIST}_$blocksize\_$RW\_iops.log
            kill `pidof iostat` > /dev/null
            sleep 30s
        done
    done
}

hdd_base_test_sequence(){
    rm -f ${DEV_LIST}_write.log ${DEV_LIST}_read.log
    # Sequential write/read test
    for RW in write read
    do
        for BS in 4k 8k 16k 32k 64k 128k 256k 512k 1m
        do
            for THREADS in 1 2 4 8
            do
                for depth in 1 2 4 8 16 32 64 128 256
                do
                    $path_to_fio --readwrite=${RW} --bs=${BS} --numjobs=${THREADS} --iodepth=${depth} --ramp_time=60s --runtime=300s ${PARA_LINE} --offset_increment=80G --filename=/dev/${DEV_LIST} \
                    --name=${RW}_${BS}_${THREADS}_${depth} | tee -a ${DEV_LIST}_${RW}.log
                    sleep 30s
                done
            done
        done
    done
}

hdd_base_test_random(){
    rm -f ${DEV_LIST}_randwrite.log ${DEV_LIST}_randread.log
    # Randrom write/read test with different io pattern       
    for RW in randwrite randread
    do
        for BS in 4k 8k 16k 32k 64k 128k 256k 512k 1m
        do
            for THREADS in 1 2 4 8
            do
                for depth in 1 2 4 8 16 32 64 128 256
                do
                    $path_to_fio --readwrite=${RW} --bs=${BS} --numjobs=${THREADS} --iodepth=${depth} --ramp_time=60s --runtime=300s ${PARA_LINE} --filename=/dev/${DEV_LIST} \
                    --name=${RW}_${BS}_${THREADS}_${depth} | tee -a ${DEV_LIST}_${RW}.log
                    sleep 30s
                done
            done
        done
    done
}

ssd_stress(){
    #sequence precondition
    ssd_fragment_sequence
    wait
    #128k read stress for 2h
    $path_to_fio --readwrite=read --bs=128k --numjobs=1 --iodepth=128 --runtime=2h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
    --name=${DEV_LIST}_128k_read_stress | tee -a ${DEV_LIST}_128k_read_stress.log
    sleep 30s
    #128k write stress for 10h
    $path_to_fio --readwrite=write --bs=128k --numjobs=1 --iodepth=128 --runtime=10h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
    --name=${DEV_LIST}_128k_write_stress | tee -a ${DEV_LIST}_128k_write_stress.log
    sleep 30s
    #4k randwrite precondition
    ssd_fragment_random 4k
    wait
    #4k randread stress for 2h
    $path_to_fio --readwrite=randread --bs=4k --numjobs=8 --iodepth=128 --runtime=2h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
    --name=${DEV_LIST}_4k_randwrite_stress | tee -a ${DEV_LIST}_4k_randread_stress.log
    sleep 30s
    #4k randwrite stress for 10h
    $path_to_fio --readwrite=randwrite --bs=4k --numjobs=128 --iodepth=128 --runtime=10h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
    --name=${DEV_LIST}_4k_randwrite_stress | tee -a ${DEV_LIST}_4k_randwrite_stress.log
    sleep 30s
    #4k 70% mixrw stress for 2h
    $path_to_fio --readwrite=randrw --rwmixread=70 --bs=4k --numjobs=8 --iodepth=128 --runtime=2h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
    --name=${DEV_LIST}_4k_randwrite_stress | tee -a ${DEV_LIST}_4k_mixrw_stress.log
    sleep 30s 
}

hdd_stress(){
    #128k read stress for 8h
    $path_to_fio --readwrite=randread --bs=128k --numjobs=1 --iodepth=128 --runtime=8h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
    --name=${DEV_LIST}_128k_read_stress | tee -a ssd_${DEV_LIST}_128k_read_stress.log
    sleep 30s
    #128k write stress for 8h
    $path_to_fio --readwrite=randwrite --bs=128k --numjobs=1 --iodepth=128 --runtime=8h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
    --name=${DEV_LIST}_128k_write_stress | tee -a ssd_${DEV_LIST}_128k_write_stress.log
    sleep 30s
    #4k randread stress for 8h
    $path_to_fio --readwrite=randread --bs=4k --numjobs=4 --iodepth=64 --runtime=8h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
    --name=${DEV_LIST}_4k_randwrite_stress | tee -a ssd_${DEV_LIST}_4k_randread_stress.log
    sleep 30s
    #4k randwrite stress for 8h
    $path_to_fio --readwrite=randwrite --bs=4k --numjobs=4 --iodepth=64 --runtime=8h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
    --name=${DEV_LIST}_4k_randwrite_stress | tee -a ssd_${DEV_LIST}_4k_randwrite_stress.log
    sleep 30s
    #4k 70% mixrw stress for 8h
    $path_to_fio --readwrite=randrw --rwmixread=70 --bs=4k --numjobs=4 --iodepth=64 --runtime=8h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
    --name=${DEV_LIST}_4k_randwrite_stress | tee -a ssd_${DEV_LIST}_4k_mixrw_stress.log
    sleep 30s   	
}

if [[ $# -eq 0 ]];then
    usage
fi

if ${IS_SSD_BASE_SEQ};then
    ssd_base_test_sequence
fi

if ${IS_SSD_BASE_RAND};then
    ssd_base_test_random
fi

if ${IS_HDD_BASE_SEQ};then
    hdd_base_test_sequence
fi

if ${IS_HDD_BASE_RAND};then
    hdd_base_test_random
fi

if ${IS_SSD_STRESS};then
    ssd_stress
fi

if ${IS_HDD_STRESS};then
    hdd_stress
fi
