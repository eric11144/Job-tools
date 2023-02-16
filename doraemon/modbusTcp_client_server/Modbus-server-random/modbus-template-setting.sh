#!/bin/sh

IPC_IP='192.168.11.127'
GATEWAY_USERNAME='admin'
GATEWAY_PASSWORD='p@55w0rd'

ACCESS_TOKEN=$(curl -H 'Content-Type: application/json' POST -d "{\"username\": \"${GATEWAY_USERNAME}\", \"password\": \"${GATEWAY_PASSWORD}\"}" http://${IPC_IP}/api/v1/auth  | jq -r .access_token)

curl -H 'Content-Type: application/json' -H "Authorization: JWT ${ACCESS_TOKEN}" -i -X PUT -d @modbus_templates.json http://${IPC_IP}/api/v1/config/modbus/templates/agile-metech-baw
curl -H 'Content-Type: application/json' -H "Authorization: JWT ${ACCESS_TOKEN}" -i -X PUT -d @modbus_equipments.json http://${IPC_IP}/api/v1/config/modbus/equipments
