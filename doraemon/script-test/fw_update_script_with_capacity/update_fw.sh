#!/bin/bash

echo "Update FW"


user_input="n"
device_path="/dev/nvme0n1"
fw_path="./DLC/"

get_model_name=$(./iSMART/sample/iSMART_64 -d $device_path | grep "Model Name" | cut -d ':' -f2 | cut -d '(' -f2 | cut -d ')' -f1)
get_fw_version=$(./iSMART/sample/iSMART_64 -d $device_path | grep "FW Version" | cut -d ':' -f2 | cut -d 'V' -f2 | cut -d ' ' -f1)
get_disk_capacity=$(./iSMART/sample/iSMART_64 -d $device_path | grep "Capacity" | cut -d ':' -f2 | cut -d ' ' -f2)

disk_capacity_int=${get_disk_capacity%.*}

echo "Disk capacity $get_disk_capacity"

echo "FW version $get_fw_version"
echo "make sure to update FW version[N/y]?"

read user_input

if [ "y" == ${user_input} -o "Y" == ${user_input} ]; then
    echo "start updating ..."
else
    echo "Current FW version is $get_fw_version"
    exit
fi

if [ "$get_fw_version" = "21118" ] || [ "$get_fw_version" = "2111880" ] || [ "$get_fw_version" = "2111881" ] || [ "$get_fw_version" = "2111803" ] || [ "$get_fw_version" = "2111804" ] ; then
    echo ""
elif [ "$get_fw_version" = "2111884" ]; then 
    echo "FW version is 2111884"
    exit 0
else
    echo "FW version $get_fw_version"
    exit 0
fi

if [[ "$get_model_name" = "P42" ]]; then
    echo "Device is P42"
    if [[ "$disk_capacity_int" -ge 50 ]] && [[ "$disk_capacity_int" -le 64 ]]; then
        echo "P42 - 64GB"
        nvme fw-download -f $fw_path"2242/REIJCDBC.bin"  $device_path
    elif [[ "$disk_capacity_int" -ge 64 ]] && [[ "$disk_capacity_int" -le 128 ]]; then
        echo "P42 - 128GB"
        nvme fw-download -f $fw_path"2242/REIJCDDC.bin"  $device_path
    elif [[ "$disk_capacity_int" -ge 128 ]] && [[ "$disk_capacity_int" -le 256 ]]; then
        echo "P42 - 256GB"
        nvme fw-download -f $fw_path"2242/REIJCDLC.bin"  $device_path
    elif [[ "$disk_capacity_int" -ge 512 ]] && [[ "$disk_capacity_int" -le 1024 ]]; then
        echo "P42 - 1TB"
        nvme fw-download -f $fw_path"2242/TETNCELC.bin"  $device_path
    else
        echo "Do nothing"
    fi

elif [[ "$get_model_name" = "P80" ]]; then 
    echo "Device is P80"
    if [[ "$disk_capacity_int" -ge 50 ]] && [[ "$disk_capacity_int" -le 64 ]]; then
        echo "P80 - 64GB"
        nvme fw-download -f $fw_path"2280/REIJCDBC.bin"  $device_path
    elif [[ "$disk_capacity_int" -ge 64 ]] && [[ "$disk_capacity_int" -le 128 ]]; then
        echo "P80 - 128GB"
        nvme fw-download -f $fw_path"2280/REIJCDDC.bin"  $device_path
    elif [[ "$disk_capacity_int" -ge 256 ]] && [[ "$disk_capacity_int" -le 512 ]]; then
        echo "P80 - 512GB"
        nvme fw-download -f $fw_path"2280/REIJCD2C.bin"  $device_path
    elif [[ "$disk_capacity_int" -ge 512 ]] && [[ "$disk_capacity_int" -le 1024 ]]; then
        echo "P80 - 1TB"
        nvme fw-download -f $fw_path"2280/REIJCE2C.bin"  $device_path
    elif [[ "$disk_capacity_int" -ge 1024 ]] && [[ "$disk_capacity_int" -le 2048 ]]; then
        echo "P80 - 2TB"
        nvme fw-download -f $fw_path"2280/REKJCE2C.bin"  $device_path
    else
        echo "Do nothing"    
    fi

else
    echo "SSD Series is incompatible"
    exit 0
fi

echo "FW commit now, Please wait"
nvme fw-commit /dev/nvme0 -s 1
echo "Disk FW update finish"
echo "Please turn off the power and remove the usb flash"
