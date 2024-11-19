#!/bin/bash


for disk in $(lsblk -d -n -o NAME | grep -v '^loop'); do
    model_info=$(sudo ./iSMART_64 -d /dev/$disk | grep "Model Name")
    echo "$model_info"
    if echo "$model_info" | grep -q "mSATA"; then
        echo "This model is mSATA."
        sudo mkfs.ext4 /dev/sda
        sudo mkdir -p /mnt/testdisk
        sudo mount /dev/sda /mnt/testdisk
        echo "Finish disk mount"
        sudo fio "seqrw-C.fio"
        echo "Finish FIO SEQ write"
        sudo dd if=/dev/zero of=/dev/sda bs=1M status=progress
        echo "Finish erase disk"
    else
        echo "This model is not mSATA."
    fi
done