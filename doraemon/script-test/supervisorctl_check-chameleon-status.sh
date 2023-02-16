#!/bin/bash

IPC_IP=localhost
DEVICE_ID=Modbus-RTU
CHANNEL_ID=40009

echo "$(date '+%Y%m%d%H%M%S check chameleon status start')"

# curl request
info=`curl -i "http://$IPC_IP/api/v1/devices/$DEVICE_ID/channels/$CHANNEL_ID/data"`

# Reponse code
code=`echo $info|grep "HTTP"|awk '{print $2}'`

# Check reponse code
if [ "$code" -eq "200" ] ; then
    echo "request sucessful，response:$code"
else
    echo `supervisorctl restart "the-gateway"`
fi
