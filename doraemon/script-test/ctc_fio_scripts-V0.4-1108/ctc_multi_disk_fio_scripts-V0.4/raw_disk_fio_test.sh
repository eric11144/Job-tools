#!/bin/bash
#****************************************************************#
# Author: zhouq32@chinatelecom.cn
# Modified in 5/16/2023
# modified randwrite precondition loop=2 to loop=1 and fio --name 
# parameter in hdd_base_test_random function
# Modified in 5/18/2013
# modified hdd stress model
# add nvme bind cpus function in 7/7/2023
# modified nvme bind cpus function in 7/26/2023
#****************************************************************#

IS_SSD_STRESS=false
IS_HDD_STRESS=false
IS_HDD_BASE_SEQ=false
IS_HDD_BASE_RAND=false
IS_SSD_BASE_SEQ=false
IS_SSD_BASE_RAND=false
IO_ENGINE=libaio
IS_CPU_MAP_RESET=false
IS_NVME_BIND_CPUS_BASE_SEQ=false
IS_NVME_BIND_CPUS_BASE_RAND=false
FILE_SIZE=100%
path_to_fio=`which fio`


usage(){
	echo "$0 [-s] [-e io_engine] [-v|V] [-h] [-b|B]  [-d dev_name] [-p] [-n|N]"
	echo "-h usage"
	echo "-s ssd stress test"
	echo "-S hdd stress test"
	echo "-e ioengine type , default type is libaio"
	echo "-b ssd raw device sequence write/read test"
	echo "-B ssd raw device random write/read test"
	echo "-d the device full path(raw device) ,such as /dev/sdx"
	echo "-v hdd raw device sequence write/read test"
	echo "-V hdd raw device random write/read test"
	echo "-n NVME SSD base sequence test with numa nodes of bind cpu socket"
	echo "-N NVME SSD base random test with numa nodes of bind cpu socket"
	echo "example:"
	echo "	ssd raw device base_test_sequence: $0 -d sdx -b &"
	echo "	ssd raw device base_test_random: $0 -d sdx -B &"
	echo "	nvme raw device base_test_sequence with cpus bind: $0 -d nvmexn1 -n &"
	echo "	nvme raw device base_test_random with cpus bind: $0 -d nvmexn1 -N &"
	echo "	hdd raw device base_test_sequence: $0 -d sdx -v &"
	echo "	hdd raw device base_test_random: $0 -d sdx -V &"
	echo "	ssd raw device stress test: $0 -d sdx -s &"
	exit
}

while getopts "hsSvVbBe:d:pnN" arg
do
	case $arg in
		h)
		usage;;
		s)
		IS_SSD_STRESS=true;;
		S)
		IS_HDD_STRESS=true;;
		v)
		IS_HDD_BASE_SEQ=true;;
		V)
		IS_HDD_BASE_RAND=true;;
		b)
		IS_SSD_BASE_SEQ=true;;
		B)
		IS_SSD_BASE_RAND=true;;
		e)
		IO_ENGINE=${OPTARG};;
		d)
		DEV_LIST=${OPTARG};;
		p)
		IS_CPU_MAP_RESET=true;;
		n)
		IS_NVME_BIND_CPUS_BASE_SEQ=true;;
		N)
		IS_NVME_BIND_CPUS_BASE_RAND=true;;
	esac
done

PARA_LINE="-end_fsync=0 -group_reporting -direct=1 -ioengine=${IO_ENGINE} -thread -time_based -buffer_compress_percentage=0 -invalidate=1 \
-norandommap -randrepeat=0 -exitall -size=${FILE_SIZE}"

PARA_LINE1="-end_fsync=0 -group_reporting -direct=1 -ioengine=${IO_ENGINE} -thread -buffer_compress_percentage=0 -invalidate=1 \
-norandommap -randrepeat=0 -exitall"



ssd_fragment_sequence(){
	#Full sequential write to let ssd be stable state before sequential test
	$path_to_fio --readwrite=write --bs=128k --iodepth=128 --numjobs=1 --loop=2 ${PARA_LINE1} --name=${DEV_LIST}_write_fragment1 --filename=/dev/${DEV_LIST} \
	|tee -a ssd_${DEV_LIST}_fragment1.log
}

ssd_fragment_random(){
	#Full random write to let ssd be stable state before random test
	$path_to_fio --readwrite=randwrite --bs=$1 --iodepth=128 --numjobs=4 --runtime=6h --time_based ${PARA_LINE1} --filename=/dev/${DEV_LIST} \
	--name=${DEV_LIST}_$1\_randwrite_fragment2 |tee -a ssd_${DEV_LIST}_fragment2.log
}

get_nvmebind_node_id()
{
	local nvme_block_symbol=$1
	local cpu_socket=$(grep $nvme_block_symbol cpu_numa_nvme_topo |awk '{print $1}' |sort -u)
	local nvmebind_node_id=$(grep $cpu_socket cpu_numa_nvme_topo |awk '{print $2}' |awk -F"=" '{print $2}' |sort -u |xargs |sed 's/[ ]/,/g')
	echo $nvmebind_node_id
}

cpubind_nvme_base_test_sequence_with_numa_constraint(){
	rm -f ${DEV_LIST}_fragment1.log ssd_${DEV_LIST}_read.log ssd_${DEV_LIST}_write.log
	#sequence precondition
	ssd_fragment_sequence
	wait
	
	local bind_node_id=$(get_nvmebind_node_id $DEV_LIST)
	for RW in read write
	do
		for BS in 128k
		do
			for THREADS in 1 
			do
				for depth in 32 64 128 256 512
				do
					numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=${BS} --numjobs=${THREADS} --iodepth=${depth} --ramp_time=60s \
					--runtime=300s ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${RW}_${BS}_${THREADS}_${depth} | tee -a ssd_${DEV_LIST}_${RW}.log
					sleep 30s
				done
			done
		done
		
		for BS in 4k 64k 256k 1m
		do
			for THREADS in 2
			do
				for depth in 32
				do
					numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=${BS} --numjobs=${THREADS} --iodepth=${depth} --ramp_time=60s \
					--runtime=300s ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${RW}_${BS}_${THREADS}_${depth} | tee -a ssd_${DEV_LIST}_${RW}.log
					sleep 30s
				done
			done
		done				
	done
}

cpubind_nvme_base_test_random_with_numa_constraint(){
	rm -f ${DEV_LIST}_fragment2.log ssd_${DEV_LIST}_randread.log ssd_${DEV_LIST}_randwrite.log
	#4k randwrite precondition
	ssd_fragment_random 4k
	wait

	local bind_node_id=$(get_nvmebind_node_id $DEV_LIST)
	for RW in randread randwrite
	do
		local nj=1
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=4k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=1 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_${nj}_1 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=4k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=32 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_${nj}_32 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s	
		
		local nj=2
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=4k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=32 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_${nj}_32 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=4k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=256 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_${nj}_256 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		
		local nj=4
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=4k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=32 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_${nj}_32 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=4k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=64 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_${nj}_64  | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		
		local nj=8		
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=4k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=1 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_8_1 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=4k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=32 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_8_32 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=4k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=64 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_8_64 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=4k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=256 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_8_256 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		
		local nj=16
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=4k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=64 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_16_64 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
	done

	#8k randwrite precondition
	ssd_fragment_random 8k
	wait		
	for RW in randread randwrite
	do
		local nj=1
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=8k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=32 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_8k_1_32 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		
		local nj=4
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=8k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=64 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_8k_4_64 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		
		local nj=8
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=8k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=1 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_8k_8_1 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=8k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=32 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_8k_8_32 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
   		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=8k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=64 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_8k_8_64 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
	done
		
	#64k randwrite precondition
	ssd_fragment_random 64k
	wait
	for RW in randread randwrite
	do
		local nj=2
   		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=64k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=32 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_64k_2_32 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
	done


	#128k randwrite precondition
	ssd_fragment_random 128k  
	wait
	for RW in randread randwrite
	do
		local nj=2
   		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=128k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=64 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_128k_2_64 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
	done
	
	#256k randwrite precondition
	ssd_fragment_random 256k 
	wait
	for RW in randread randwrite
	do
		local nj=2
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=256k --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=32 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_256k_2_32 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
	done

	#1m randwrite precondition
	ssd_fragment_random 1m 
	wait
	for RW in randread randwrite
	do
		local nj=2
		numactl -N $bind_node_id $path_to_fio --readwrite=${RW} --bs=1m --ramp_time=60s --runtime=300s --numjobs=$nj --iodepth=32 ${PARA_LINE} \
		--filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_1m_2_32 | tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
	done
}

ssd_base_test_sequence(){
	rm -f ${DEV_LIST}_fragment1.log
	#sequence precondition
	ssd_fragment_sequence
	wait
	
	for RW in read write
	do
		for BS in 128k
		do
			for THREADS in 1 
			do
				for depth in 32 64 128 256 512
				do
					$path_to_fio --readwrite=${RW} --bs=${BS} --numjobs=${THREADS} --iodepth=${depth} --runtime=300s ${PARA_LINE} --filename=/dev/${DEV_LIST} \
					--name=${RW}_${BS}_${THREADS}_${depth} | tee -a ssd_${DEV_LIST}_${RW}.log
					sleep 30s
				done
			done
		done
		
		for BS in 4k 64k 256k 1m
		do
			for THREADS in 2
			do
				for depth in 32
				do
					$path_to_fio --readwrite=${RW} --bs=${BS} --numjobs=${THREADS} --iodepth=${depth} --runtime=300s ${PARA_LINE} --filename=/dev/${DEV_LIST} \
					--name=${RW}_${BS}_${THREADS}_${depth} | tee -a ssd_${DEV_LIST}_${RW}.log
					sleep 30s
				done
			done
		done				
	done
}

ssd_base_test_random(){
	rm -f ${DEV_LIST}_fragment2.log
	#4k randwrite precondition
	ssd_fragment_random 4k
	wait	
	for RW in randread randwrite
	do		
		$path_to_fio --readwrite=${RW} --bs=4k --runtime=300s --numjobs=1 --iodepth=1 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_1_1  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s 
		$path_to_fio --readwrite=${RW} --bs=4k --runtime=300s --numjobs=1 --iodepth=32 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_1_32  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s	
		$path_to_fio --readwrite=${RW} --bs=4k --runtime=300s --numjobs=2 --iodepth=32 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_2_32  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		$path_to_fio --readwrite=${RW} --bs=4k --runtime=300s --numjobs=2 --iodepth=256 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_2_256  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		$path_to_fio --readwrite=${RW} --bs=4k --runtime=300s --numjobs=4 --iodepth=32 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_4_32  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		$path_to_fio --readwrite=${RW} --bs=4k --runtime=300s --numjobs=4 --iodepth=64 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_4_64  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		$path_to_fio --readwrite=${RW} --bs=4k --runtime=300s --numjobs=8 --iodepth=1 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_8_1  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s	
		$path_to_fio --readwrite=${RW} --bs=4k --runtime=300s --numjobs=8 --iodepth=32 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_8_32 \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		$path_to_fio --readwrite=${RW} --bs=4k --runtime=300s --numjobs=8 --iodepth=64 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_8_64  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		$path_to_fio --readwrite=${RW} --bs=4k --runtime=300s --numjobs=8 --iodepth=256 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_8_256  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		$path_to_fio --readwrite=${RW} --bs=4k --runtime=300s --numjobs=16 --iodepth=64 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_16_64  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
	done

	#8k randwrite precondition
	ssd_fragment_random 8k
	wait		
	for RW in randread randwrite
	do
   		$path_to_fio --readwrite=${RW} --bs=8k --runtime=300s --numjobs=1 --iodepth=32 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_8k_1_32  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		$path_to_fio --readwrite=${RW} --bs=8k --runtime=300s --numjobs=4 --iodepth=64 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_8k_4_64  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		$path_to_fio --readwrite=${RW} --bs=8k --runtime=300s --numjobs=8 --iodepth=1 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_8k_8_1  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
		$path_to_fio --readwrite=${RW} --bs=8k --runtime=300s --numjobs=8 --iodepth=32 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_8k_8_32  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
   		$path_to_fio --readwrite=${RW} --bs=8k --runtime=300s --numjobs=8 --iodepth=64 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_8k_8_64  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
	done
		
	#64k randwrite precondition
	ssd_fragment_random 64k
	wait
	for RW in randread randwrite
	do
   		$path_to_fio --readwrite=${RW} --bs=64k --runtime=300s --numjobs=2 --iodepth=32 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_64k_2_32  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
	done


	#128k randwrite precondition
	ssd_fragment_random 128k  
	wait
	for RW in randread randwrite
	do
   		$path_to_fio --readwrite=${RW} --bs=128k --runtime=300s --numjobs=2 --iodepth=64 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_128k_2_64  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
	done
	
	#256k randwrite precondition
	ssd_fragment_random 256k 
	wait
	for RW in randread randwrite
	do
		$path_to_fio --readwrite=${RW} --bs=256k --runtime=300s --numjobs=2 --iodepth=32 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_256k_2_32  \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
	done

	#1m randwrite precondition
	ssd_fragment_random 1m 
	wait
	for RW in randread randwrite
	do
		$path_to_fio --readwrite=${RW} --bs=1m --runtime=300s --numjobs=2 --iodepth=32 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_1m_2_32 \
		| tee -a ssd_${DEV_LIST}_${RW}.log
		sleep 30s
	done
}



hdd_base_test_sequence(){
	# Sequential write/read test
	for RW in write read
	do
		$path_to_fio --readwrite=${RW} --bs=4k --runtime=300s --numjobs=2 --iodepth=32 ${PARA_LINE} --offset_increment=80G --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_4k_2_32  \
		| tee -a hdd_${DEV_LIST}_${RW}.log
		sleep 30s
		
		$path_to_fio --readwrite=${RW} --bs=64k --runtime=300s --numjobs=2 --iodepth=32 ${PARA_LINE} --offset_increment=80G --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_64k_2_32  \
		| tee -a hdd_${DEV_LIST}_${RW}.log
		sleep 30s

		$path_to_fio --readwrite=${RW} --bs=256k --runtime=300s --numjobs=2 --iodepth=32 ${PARA_LINE} --offset_increment=80G --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_256k_2_32  \
		| tee -a hdd_${DEV_LIST}_${RW}.log
		sleep 30s

		$path_to_fio --readwrite=${RW} --bs=1m --runtime=300s --numjobs=1 --iodepth=32 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_1m_1_32  \
		| tee -a hdd_${DEV_LIST}_${RW}.log
		sleep 30s

		$path_to_fio --readwrite=${RW} --bs=1m --runtime=300s --numjobs=2 --iodepth=32 ${PARA_LINE} --offset_increment=80G --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_${RW}_1m_2_32  \
		| tee -a hdd_${DEV_LIST}_${RW}.log
		sleep 30s
	done
}

hdd_base_test_random(){
	# Randrom write test with different io pattern       
	$path_to_fio --readwrite=randwrite --bs=4k --ramp_time=10s --runtime=300s --numjobs=1 --iodepth=1 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_randwrite_4k_1_1  \
	| tee -a hdd_${DEV_LIST}_randwrite.log
	sleep 30s

	for BS in 4k 64k 256k 1m
	do
		for THREADS in 2
		do
			for depth in 32
			do
				$path_to_fio --readwrite=randwrite --bs=${BS} --ramp_time=10s --runtime=300s --numjobs=${THREADS} --iodepth=${depth} ${PARA_LINE} --filename=/dev/${DEV_LIST} \
				--name=${DEV_LIST}_randwrite_${BS}_${THREADS}_${depth} | tee -a hdd_${DEV_LIST}_randwrite.log
			    sleep 30s
			done
		done
	done


	# Random read test with different io pattern
	for BS in 4k
	do
		for THREADS in 1
		do
			for depth in 1 4 8 16 32
			do	
				$path_to_fio --readwrite=randread --bs=${BS} --ramp_time=10s --runtime=300s --numjobs=${THREADS} --iodepth=${depth} ${PARA_LINE} --filename=/dev/${DEV_LIST} \
				--name=${DEV_LIST}_randread_${BS}_${THREADS}_${depth} | tee -a hdd_${DEV_LIST}_randread.log
				sleep 30s
			done
		done
	done

	$path_to_fio --readwrite=randread --bs=8k --ramp_time=10s --runtime=300s --numjobs=1 --iodepth=1 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_randread_8k_1_1  \
	| tee -a hdd_${DEV_LIST}_randread.log
	sleep 30s
	
	$path_to_fio --readwrite=randread --bs=8k --ramp_time=10s --runtime=300s --numjobs=1 --iodepth=32 ${PARA_LINE} --filename=/dev/${DEV_LIST} --name=${DEV_LIST}_randread_8k_1_32  \
	| tee -a hdd_${DEV_LIST}_randread.log


	for BS in 4k 64k 256k 1m
	do
		for THREADS in 2
		do
			for depth in 32
			do
				$path_to_fio --readwrite=randread --bs=${BS} --ramp_time=10s --runtime=300s --numjobs=${THREADS} --iodepth=${depth} ${PARA_LINE} --filename=/dev/${DEV_LIST} \
				--name=${DEV_LIST}_randread_${BS}_${THREADS}_${depth} | tee -a hdd_${DEV_LIST}_randread.log
				sleep 30s
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
	--name=${DEV_LIST}_128k_read_stress | tee -a ssd_${DEV_LIST}_128k_read_stress.log
	sleep 30s
	#128k write stress for 10h
	$path_to_fio --readwrite=write --bs=128k --numjobs=1 --iodepth=128 --runtime=10h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
	--name=${DEV_LIST}_128k_write_stress | tee -a ssd_${DEV_LIST}_128k_write_stress.log
	sleep 30s
	#4k randwrite precondition
	ssd_fragment_random 4k
	wait
	#4k randread stress for 2h
	$path_to_fio --readwrite=randread --bs=4k --numjobs=8 --iodepth=128 --runtime=2h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
	--name=${DEV_LIST}_4k_randwrite_stress | tee -a ssd_${DEV_LIST}_4k_randread_stress.log
	sleep 30s
	#4k randwrite stress for 10h
	$path_to_fio --readwrite=randwrite --bs=4k --numjobs=8 --iodepth=128 --runtime=10h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
	--name=${DEV_LIST}_4k_randwrite_stress | tee -a ssd_${DEV_LIST}_4k_randwrite_stress.log
	sleep 30s
	#4k 70% mixrw stress for 2h
	$path_to_fio --readwrite=randrw --rwmixread=70 --bs=4k --numjobs=8 --iodepth=128 --runtime=2h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
	--name=${DEV_LIST}_4k_randwrite_stress | tee -a ssd_${DEV_LIST}_4k_mixrw_stress.log
	sleep 30s   	
}

hdd_stress(){
	#128k read stress for 8h
	$path_to_fio --readwrite=read --bs=128k --numjobs=1 --iodepth=128 --runtime=8h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
	--name=${DEV_LIST}_128k_read_stress | tee -a hdd_${DEV_LIST}_128k_read_stress.log
	sleep 30s
	#128k write stress for 8h
	$path_to_fio --readwrite=write --bs=128k --numjobs=1 --iodepth=128 --runtime=8h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
	--name=${DEV_LIST}_128k_write_stress | tee -a hdd_${DEV_LIST}_128k_write_stress.log
	sleep 30s
	#4k randread stress for 8h
	$path_to_fio --readwrite=randread --bs=4k --numjobs=4 --iodepth=64 --runtime=8h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
	--name=${DEV_LIST}_4k_randwrite_stress | tee -a hdd_${DEV_LIST}_4k_randread_stress.log
	sleep 30s
	#4k randwrite stress for 8h
	$path_to_fio --readwrite=randwrite --bs=4k --numjobs=4 --iodepth=64 --runtime=8h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
	--name=${DEV_LIST}_4k_randwrite_stress | tee -a hdd_${DEV_LIST}_4k_randwrite_stress.log
	sleep 30s
	#4k 70% mixrw stress for 8h
	$path_to_fio --readwrite=randrw --rwmixread=70 --bs=4k --numjobs=4 --iodepth=64 --runtime=8h ${PARA_LINE} --filename=/dev/${DEV_LIST} \
	--name=${DEV_LIST}_4k_randwrite_stress | tee -a hdd_${DEV_LIST}_4k_mixrw_stress.log
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

if ${IS_CPU_MAP_RESET};then
	cpu_map_reset
fi

if ${IS_NVME_BIND_CPUS_BASE_SEQ};then
	cpubind_nvme_base_test_sequence_with_numa_constraint
fi

if ${IS_NVME_BIND_CPUS_BASE_RAND};then
	cpubind_nvme_base_test_random_with_numa_constraint
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
