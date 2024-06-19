#!/bin/bash
#****************************************************************#
# Author: zhouq32@chinatelecom.cn
# merge parallel nvme/ssd/hdd fio test with arguments option
# add log filter function after fio test 
# add multi nvme ssds fio with cpusbind functions
#****************************************************************#

CPWD=$(cd $(dirname $0);pwd)
cd $CPWD
rm -f ssd_symbol_set hdd_symbol_set nvme_symbol_set filter_multi*.csv

IS_NVME_PARALLEL=false
IS_SSD_PARALLEL=false
IS_NVME_PARALLER_WITH_CPUSBIND=false
IS_HDD_PARALLEL=false
IS_NVME_PARALLEL_STRESS=false
IS_SSD_PARALLEL_STRESS=false
IS_HDD_PARALLEL_STRESS=false

usage()
{
    echo "$0 [-h help] [-N nvme_fio_and_log_filter] [-S ssd_fio_and_log_filter] [-H hdd_fio_and_log_filter]"
    echo "$0 [-C nvme_fio_with_cpusbind and log filter] [-n nvme_fio_stress] [-s ssd_fio_stress] [-d hdd_fio_stress]"
    echo "examples:"
    echo "$0 -h, usage"
    echo "$0 -N, multi nvme ssds fio test and log filter"
	echo "$0 -C, multi nvme ssds fio test with cpusbind and log filter"
    echo "$0 -S, multi ssds fio test and log filter"
    echo "$0 -H, multi hdds fio test and log filter"
    echo "$0 -n, multi nvme ssds fio stress test"
    echo "$0 -s, multi ssds fio stress test"
    echo "$0 -d, multi hdds fio stress test"
    exit 1
}

while getopts "hNSCHnsd" arg
do
    case $arg in
        h)
        usage;;
        N)
        IS_NVME_PARALLEL=true;;
        S)
        IS_SSD_PARALLEL=true;;
        C)
        IS_NVME_PARALLER_WITH_CPUSBIND=true;;
        H)
        IS_HDD_PARALLEL=true;;
        n)
        IS_NVME_PARALLEL_STRESS=true;;
        s)
        IS_SSD_PARALLEL_STRESS=true;;
        d)
        IS_HDD_PARALLEL_STRESS=true;;  
        *)
        usage;;
    esac
done

check_tool_installed()
{
    cmds="fio smartctl nvme numactl lstopo-no-graphics"
    for cmd in $cmds;do
        if ! which $cmd &> /dev/null;then
                echo -e "You must install relative packages for fio(libaio and fio),smartctl(smartmontools),nvme(nvme-cli),numactl,lstopo-no-graphics(hwloc)"
            exit 1
        fi
    done
}

filter_ssd_hdd_nvme_set()
{
    rm -f ssd_symbol_set hdd_symbol_set nvme_symbol_set raid_symbol_set
    os_disk_symbol=$(echo $(lsblk |grep -B1 -E "part|boot" |grep -E "^sd[a-z]+|^nvme|^vd[a-z]+" |awk '{print $1}') |sed 's/ /|/')
    non_os_disk_set=$(lsscsi -g |grep -E "ATA|TOSHIBA" |awk '{print $(NF-1)}' |grep -Evw $os_disk_symbol)
    if [[ -n $non_os_disk_set ]];then
        for i in $(echo "$non_os_disk_set")
        do
            rotationRate=$(smartctl -i $i |awk -F":" '/Rotation Rate/{print $2}')
            if [[ $rotationRate =~ "Solid State Device" ]];then
                echo $i |awk -F"/" '{print $3}' >> ssd_symbol_set
            elif [[ $rotationRate =~ "rpm" ]];then
                echo $i |awk -F"/" '{print $3}' >> hdd_symbol_set
	    else
		echo $i |awk -F"/" '{print $3}' >> raid_symbol_set
            fi
       done
    fi
	
    is_os_nvme=$(echo "$os_disk_symbol" |grep nvme)
    if [[ -n $is_os_nvme ]];then
        os_nvme_symbol=$(echo "$is_os_nvme" |grep -Eo "nvme[0-9]+n1")
    else
        os_nvme_symbol=null
    fi
    nvme_info_set=$(nvme list |grep -E "nvme[0-9]+n1" |grep -v $os_nvme_symbol)
    if [[ -n $nvme_info_set ]];then
        echo "$nvme_info_set" |awk '{print $1}' |awk -F"/" '{print $3}' > nvme_symbol_set
    fi
}

#********************************************
# Get CPU->NUMA Node->NVME SSD Topology
#********************************************
get_cpu_numa_nvme_topo()
{
    rm -f cpu_numa_nvme_topo cpu_core numanode_core cpu_numanode_map socket_numa_nvme_map
    echo "CPU Socket->NUMA Node->NVME SSD Topology:" >> cpu_numa_nvme_topo
    lstopo-no-graphics --only socket --cpuset --taskset |sed 's/cpuset=/ /g' > cpu_core
    lscpu |grep  "NUMA node[0-9+] CPU(s)" |awk '{print $2,$4}' > numanode_core

    if which python2 > /dev/null 2>&1;then
        local python_tool=python2
    elif which python3 > /dev/null 2>&1;then
        local python_tool=python3
    else
        echo "please install python2 or python3"
        return
    fi

    rm -f cpu_numanode_map
    for frt_node_core in $(awk '{print $2}' numanode_core |awk -F"-" '{print $1}')
    do
        for cpu_socket_core in $(awk '{print $3}' cpu_core)
        do
            if [[ "$python_tool" == "python2" ]];then
                local value=$(python2 -c "print int(bool(1<<$frt_node_core & $cpu_socket_core))")
            elif [[ "$python_tool" == "python3" ]];then
                local value=$(python3 -c "print(int(bool(1<<$frt_node_core & $cpu_socket_core)))")
            fi
            if [ $value -ne 0 ];then
                local cpu_socket=$(grep -w $cpu_socket_core cpu_core |awk '{print $2}' |awk -F"#" '{print $2}')
                local numa_node=$(grep -w $frt_node_core numanode_core |awk '{print $1}' |sed -E 's/node([0-9]*)/\1/g')
                echo -e "cpu_socket=$cpu_socket numa_node=$numa_node" >> cpu_numanode_map
            fi
        done
    done

    rm -f numanode_nvme_map
    for dev in $(nvme list |awk '/nvme[0-9]*n1/{print $1}' |awk -F"/" '{print $3}' |sed 's/n1$//g')
    do
        local busInfo=$(ls -l /sys/class/nvme |grep -w $dev |awk '{print $NF}' |awk -F"/" '{print $(NF-2)}')
        local numaNode=$(cat /sys/bus/pci/devices/$busInfo/numa_node)
        echo -e "numa_node=$numaNode nvme_label=${dev}n1" >> numanode_nvme_map
    done

    rm -f socket_numa_nvme_map
    for node in $(awk '{print $2}' cpu_numanode_map)
    do
        if grep $node numanode_nvme_map >/dev/null 2>&1 ;then
            local socket=$(grep $node cpu_numanode_map |awk '{print $1}')
            for label in $(grep $node numanode_nvme_map |awk '{print $2}')
            do
                echo -e "$socket $node $label" >> socket_numa_nvme_map
            done
        else
            local socket=$(grep $node cpu_numanode_map |awk '{print $1}')
            echo -e "$socket $node nvme_label=NA" >> socket_numa_nvme_map
        fi
    done
    awk '{printf "%-15s%-15s%-15s\n",$1,$2,$3}' socket_numa_nvme_map >> cpu_numa_nvme_topo
}

nvme_format()
{
    # low format(clear FTL data) for all nvme before fio test
    for dev in $(cat nvme_symbol_set)
    do
        nvme format /dev/$dev
    done
    cd $CPWD
}

nvme_parallel_fio_test()
{
    # multi nvme ssd fio test
    if [ -s nvme_symbol_set ];then
        nvme_format
        mkdir -p nvme_fio_log
        for dev in $(cat nvme_symbol_set)
        do		
            nohup &>/dev/null ./ssd_raw_fio_test.sh $dev &
        done
        wait
	sleep 30s
        mv ssd_nvme*_*.log nvme_fio_log		
        cp multi_disk_log_filter.sh nvme_symbol_set nvme_fio_log
        cd nvme_fio_log
        ./multi_disk_log_filter.sh -N
        cd $CPWD
    fi
}

nvme_parallel_fio_test_with_cpusbind()
{
    # multi nvme ssd fio test with cpusbind
    if [ -s nvme_symbol_set ];then
	get_cpu_numa_nvme_topo
        nvme_format
        mkdir -p cpusbind_nvme_fio_log
        for dev in $(cat nvme_symbol_set)
        do
            nohup &>/dev/null ./nvme_raw_fio_test_with_cpubind.sh $dev &
        done
        wait
	sleep 30s
        mv ssd_nvme*_*.log cpusbind_nvme_fio_log		
        cp multi_disk_log_filter.sh nvme_symbol_set cpusbind_nvme_fio_log
        cd cpusbind_nvme_fio_log
        ./multi_disk_log_filter.sh -N
        cd $CPWD
    fi
}

nvme_parallel_fio_stress_test()
{
    # multi nvme ssd fio test
    if [ -s nvme_symbol_set ];then
        mkdir -p nvme_fio_stress_log
        for dev in $(cat nvme_symbol_set)
        do
            nohup &>/dev/null ./ssd_fio_stress_test.sh $dev &
        done
        wait
	sleep 30s
        mv ssd_nvme*_stress.log nvme_fio_stress_log
    fi
}

raid_parallel_fio_test()
{
    # multi raids combined with sata ssd fio test
    if [ -s raid_symbol_set ];then
        mkdir -p ssd_raid_fio_log
        for dev in $(cat raid_symbol_set)
        do
            nohup &>/dev/null ./ssd_raw_fio_test.sh $dev &
        done
        wait
        sleep 30s
        mv raid_sd*_*.log ssd_raid_fio_log
        cp multi_disk_log_filter.sh raid_symbol_set ssd_raid_fio_log
        cd raid_ssd_fio_log
        ./multi_disk_log_filter.sh -S
        cd $CPWD
    fi    
}

ssd_parallel_fio_test()
{
    # multi sata ssd fio test
    if [ -s ssd_symbol_set ];then
        mkdir -p ssd_fio_log
        for dev in $(cat ssd_symbol_set)
        do
            nohup &>/dev/null ./ssd_raw_fio_test.sh $dev &
        done
        wait
	sleep 30s
        mv ssd_sd*_*.log ssd_fio_log
        cp multi_disk_log_filter.sh ssd_symbol_set ssd_fio_log
        cd ssd_fio_log
        ./multi_disk_log_filter.sh -S
        cd $CPWD
    fi
}

ssd_parallel_fio_stress_test()
{
    # multi sata/sas ssd fio test
    if [ -s ssd_symbol_set ];then
        mkdir -p ssd_fio_stress_log
        for dev in $(cat ssd_symbol_set)
        do
            nohup &>/dev/null ./ssd_fio_stress_test.sh $dev &
        done
        wait
	sleep 30s
        mv ssd*_stress.log ssd_fio_stress_log
    fi
}   

hdd_parallel_fio_test()
{
    # multi hdd fio test
    if [ -s hdd_symbol_set ];then
        mkdir -p hdd_fio_log
        for dev in $(cat hdd_symbol_set)
        do
            nohup &>/dev/null ./hdd_raw_fio_test.sh $dev &
        done
        wait
	sleep 30s
        mv hdd_sd*_*.log hdd_fio_log
        cp multi_disk_log_filter.sh hdd_symbol_set hdd_fio_log
        cd hdd_fio_log
        ./multi_disk_log_filter.sh -H
        cd $CPWD
    fi
} 

hdd_parallel_fio_stress_test()
{
    # multi sata/sas hdd fio stress test
    if [ -s hdd_symbol_set ];then
        mkdir -p hdd_fio_stress_log
        for dev in $(cat hdd_symbol_set)
        do
            nohup &>/dev/null ./hdd_fio_stress_test.sh $dev &
        done
        wait
	sleep 30s
        mv hdd*_stress.log hdd_fio_stress_log
    fi
}

if [[ $# -eq 0 ]];then
	usage
fi
check_tool_installed
filter_ssd_hdd_nvme_set

if ${IS_NVME_PARALLEL};then
    nvme_parallel_fio_test  
fi

if ${IS_NVME_PARALLER_WITH_CPUSBIND};then
	nvme_parallel_fio_test_with_cpusbind
fi

if ${IS_SSD_PARALLEL};then
    ssd_parallel_fio_test
fi
	
if ${IS_HDD_PARALLEL};then
    hdd_parallel_fio_test
fi

if ${IS_NVME_PARALLEL_STRESS};then
    nvme_parallel_fio_stress_test
fi

if ${IS_SSD_PARALLEL_STRESS};then
    ssd_parallel_fio_stress_test
fi

if ${IS_HDD_PARALLEL_STRESS};then
    hdd_parallel_fio_stress_test
fi
