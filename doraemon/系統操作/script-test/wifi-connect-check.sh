#!/bin/sh

CONN_NAME=wifi-setup
DEVNAME=wlan0
REMOTE_HOST=192.168.3.1

CHECK_CONNECTION=ping -I ${DEVNAME} -i 1 -W 3 -c 10 ${REMOTE_HOST}

echo "checking connection" $(date '+%Y%m%d%H%M%S')
${CHECK_CONNECTION}
if [ $? -ne 0 ]; then
    echo "reconnecting..."
    nmcli connection down ${CONN_NAME}
    nmcli -w 90 connection up ${CONN_NAME}

    ${CHECK_CONNECTION}
    while [ $? -ne 0 ]
        do
            nmcli connection down ${CONN_NAME}
            nmcli -w 90 connection up ${CONN_NAME}

            ${CHECK_CONNECTION}
            if [ $? -eq 0 ]; then
                echo "reconnect: suceeded"
            else
                echo "reconnect: failed"
            fi
        done

else
    echo "still connected"
fi
