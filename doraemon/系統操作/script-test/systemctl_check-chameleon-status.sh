#!/bin/bash

IPC_IP=localhost
DEVICE_ID=FX3G
PLC_IP=192.168.60.1

CHECK_PLC_CONNECTION="ping -i 1 -W 3 -c 10 ${PLC_IP}"

echo "$(date '+%Y%m%d%H%M%S check chameleon status start')"
${CHECK_PLC_CONNECTION} > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "plc not connected"
    exit 1
fi
# curl request

curl -f "http://$IPC_IP/api/v1/devices/$DEVICE_ID/channels/latest-data" > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "request fail"
    systemctl restart chameleon.service
fi
