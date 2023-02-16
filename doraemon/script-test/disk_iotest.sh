#!/bin/sh

count=1

datetime=$(date "+%Y-%m-%d %H:%M:%S")

while true;
do
    echo $count 
    echo $count >> log_$datetime.txt
    echo $datetime >> log_$datetime.txt
    
    get_error_msg="$(dmesg | grep "SATA link")"
    
    dd if=/dev/sdb of=/dev/null bs=1M status=progress
    
    save_error_msg="$(dmesg | grep "SATA link" >> log.txt)"

    if [ -z "$get_error_msg" ]; then
        exit 0
    else
       echo "\n"
       echo "\n" >> log.txt
       count=$(($count+1)) 
    fi
done
