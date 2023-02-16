#!/bin/sh

count=1
datetime=$(date "+%Y-%m-%d %H:%M:%S")
filename="/home/ubuntu/log.txt"

if [ -f "$filename" ]; then
    count=$(tail -n 1 $filename)
    count=$(($count+1)) 
    echo $count 
    echo $datetime >> $filename
    echo $count >> $filename
else
    echo $datetime >> $filename
    echo $count >> $filename
fi