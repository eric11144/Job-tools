#!/bin/sh

date '+%Y%m%d-%H%M%S ntpdate-hwclock-writeback executed'

NTP_SERVER=$(yq r /etc/chameleon-datetime/ntp.yml ntp-server)

if [ "$?" -ne "0" ]; then
    echo "running yq error"
    exit 1
fi

if [ "$NTP_SERVER" = "null" ]; then
    echo "parsing config error"
    exit 1
fi

/usr/sbin/ntpdate "$NTP_SERVER" >/dev/null 2>&1

if [ "$?" -ne "0" ]; then
    /sbin/hwclock -s -u

    if [ "$?" -eq 0 ]; then
        echo "set system time with hwclock"
    else
        echo "set system time with hwclock: failure"
    fi
else
    /sbin/hwclock -w -u

    if [ "$?" -eq 0 ]; then
        echo "set hwclock with system time"
    else
        echo "set hwclock with system time: failure"
    fi
fi
