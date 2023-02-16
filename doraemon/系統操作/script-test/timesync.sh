#!/bin/sh

set -x

NTP_HOST=time.google.com

echo "$(date '+%Y%m%d%H%M%S timesync start')" >> /var/log/cron.txt

ntpdate $NTP_HOST > /dev/null 2>&1

if [ "$?" -ne "0" ]; then
    hwclock -s

    if [ "$?" -eq 0 ]; then
        echo "set system clock with hwclock"
    else
        echo "set system clock with hwclock: failed"
    fi

else 
    echo "timesync is successfull."
fi
