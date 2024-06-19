#!/bin/bash
home_file=$HOME
log_file="$home_file/boot_times.log"
countdown=20
tput civis

while [ $countdown -gt 0 ]; do
  echo -ne "\rCount down: $countdown sec "
  sleep 1
  countdown=$((countdown - 1))
done

echo -ne "\r                    \r"

total_boot_time=$(systemd-analyze | grep 'Startup finished' | awk '{print $16}')
echo -ne  "\rTotal boot time: $total_boot_time \n"
tput cnorm
echo "Boot time on $(date): $total_boot_time" >> $log_file

