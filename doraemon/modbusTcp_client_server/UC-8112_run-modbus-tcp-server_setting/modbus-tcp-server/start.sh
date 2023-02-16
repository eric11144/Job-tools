#!/bin/bash

cd /modbus-tcp-server
. venv/bin/activate

docker-compose up --force-recreate
