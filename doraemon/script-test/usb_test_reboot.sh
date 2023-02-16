#!/bin/bash

count=1
datetime=$(date "+%Y-%m-%d %H:%M:%S")

sleep 5

while true;
do
    echo $count 
    echo $count >> log_$datetime.txt
    echo $datetime >> log_$datetime.txt
    
    get_usb_connect_info="$(df -h | grep "/mnt/ubuntu")"

    echo $get_usb_connect_info
done