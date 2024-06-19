#!/bin/sh


echo "start reboot"
sleep 60

datetime=$(date "+%Y-%m-%d %H:%M:%S")
get_usb_connect_info="$(lsblk | grep "sda")"

if [ -n "$get_usb_connect_info" ]; then
  if [ -f count.txt ]; then
      echo $get_usb_connect_info
      while read line ; 
      do
          count=$(($line+1)) 
      done < count.txt

      echo $count
      echo $datetime
      echo $count > count.txt
      sleep 1
      systemctl reboot -i
  else
    echo $get_usb_connect_info
    count=1
    echo $count 
    echo $datetime
    echo $count > count.txt
    sleep 1
    systemctl reboot -i
  fi
else
  echo "USB detect fail"
  exit 0
fi
