#!/bin/bash

IPC_IP=localhost
DEVICE_ID=Q00

echo "$(date '+%Y%m%d%H%M%S check chameleon status start')"

curl -f "http://$IPC_IP/api/v1/status/devices" > /dev/null 2>&1
echo "$?"

curl -f "http://$IPC_IP/api/v1/devices/$DEVICE_ID/channels/latest-data" > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "request fail"
    systemctl restart chameleon.service
fi
