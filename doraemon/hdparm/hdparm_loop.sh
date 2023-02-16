#!/bin/bash

echo "Input runtime number: $1"

echo "hdparm test loop"

speed=0
total=0

for((i=1; i<= $1; ++i))
do 
    echo "Runtime: $i"
    speed=$(hdparm -t --direct /dev/sda1 | grep "seconds" | cut -d '=' -f2 | cut -d ' ' -f2)
    echo $speed
    total=$(awk 'BEGIN{printf "%.2f\n", ('$total'+'$speed')}')
done

echo "scale=2; $total / $1" | bc
echo "hdparm test finish"