#!/bin/bash

echo "Input runtime number: $1"

echo "Start hdparm test"

speed=0
total=0

for((i=1; i<= $1; ++i))
do 
    echo "Runtime: $i"
    speed=$(hdparm -t --direct /dev/nvme0n1 | grep "seconds" | cut -d '=' -f2 | cut -d ' ' -f2)
    speed_unit=$(hdparm -t --direct /dev/nvme0n1 | grep "seconds" | cut -d '=' -f2 | cut -d ' ' -f3)
    echo "Current: $speed $speed_unit"
    total=$(awk 'BEGIN{printf "%.2f\n", ('$total'+'$speed')}')
done

average=$(echo "scale=2; $total / $1" | bc)

echo "Average: $average $speed_unit"
echo "hdparm test finish"
