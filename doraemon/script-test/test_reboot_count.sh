#!/bin/sh

count=1
datetime=$(date "+%Y-%m-%d %H:%M:%S")
filename="/home/ubuntu/log.txt"

# Check if the reboot log file exists.
if [ -f "$filename" ]; then
    count=$(tail -n 1 $filename | awk '{print $1'}) # Get reboot count
    count=$(($count+1)) 
    echo $count 
    echo $count ' ' $datetime >> $filename
    reboot
else
    # If the reboot log file does not exist, then create it by using the 'touch' command.
    touch "/home/ubuntu/log.txt"
    echo $count 
    echo $count ' ' $datetime >> $filename
    reboot
fi