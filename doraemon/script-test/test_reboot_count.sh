#!/bin/sh

count=1
datetime=$(date "+%Y-%m-%d %H:%M:%S")
filename="/home/ubuntu/log.txt"

# Check if the reboot log file exists.
if [ -f "$filename" ]; then
    count=$(tail -n 1 $filename)
    count=$(($count+1)) 
    echo $count 
    echo $count >> $filename
    echo $datetime >> $filename
    reboot
else
    touch "/home/ubuntu/log.txt"
fi