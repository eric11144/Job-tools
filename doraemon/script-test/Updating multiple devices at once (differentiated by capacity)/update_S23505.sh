#!/bin/bash

echo "Starting Update FW"
echo -e "\n"

ssd_devices=($(lsblk -d -o NAME,MODEL,SIZE | grep -i "SSD\|M.2\|InnoDisk\|mSATA\|Generic_FCR_SATA_Loader" | awk '{print "/dev/"$1}'))

num_ssd_devices=${#ssd_devices[@]}

if [ $num_ssd_devices -gt 0 ]; then
    count=1
    
    for ssd_device in "${ssd_devices[@]}"; do
        get_disk_capacity=$(./iSMART_64 -d $ssd_device | grep "Capacity" | cut -d ':' -f2 | cut -d ' ' -f2)
        disk_capacity_int=${get_disk_capacity%.*}
        
        if [[ "$disk_capacity_int" -ge 64 ]] && [[ "$disk_capacity_int" -le 128 ]]; then
            echo "Item "$count
            ./DLMicro_64 -d $ssd_device -f S23505_128GB.bin
            echo -e "\n"
            count=$(($count+1))
        elif [[ "$disk_capacity_int" -ge 128 ]] && [[ "$disk_capacity_int" -le 256 ]]; then
            echo "Item "$count
            ./DLMicro_64 -d $ssd_device -f S23505_256GB.bin
            echo -e "\n"
            count=$(($count+1))
        elif [[ "$disk_capacity_int" -ge 256 ]] && [[ "$disk_capacity_int" -le 512 ]]; then
            echo "Item "$count
            ./DLMicro_64 -d $ssd_device -f S23505_512GB.bin
            echo -e "\n"
            count=$(($count+1))
        else
            echo $ssd_device "-> This SSD does not meet the update requirements."
            echo -e "\n"
        fi
    done
fi