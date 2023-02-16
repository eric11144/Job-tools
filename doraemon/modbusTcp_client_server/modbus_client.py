#!/usr/bin/env python
# -*- coding: utf-8 -*-
# install pyModbusTCP ref: https://pypi.org/project/pyModbusTCP/

from pyModbusTCP.client import ModbusClient
import time
HOST1 = "127.0.0.1"
PORT1 = 502


c1 = ModbusClient()

# uncomment this line to see debug message
#c1.debug(True)

# define modbus server host, port
c1.host(HOST1)
c1.port(PORT1)
#set UID to 1
c1.unit_id(1)


while True:
    # open or reconnect TCP to server
    if not c1.is_open():
        if not c1.open():
            print("unable to connect to "+HOST1+":"+str(PORT1))

    # if open() is ok, read register (modbus function 0x03)
    if c1.is_open():
        # read 32 registers at address 0, store result in regs list
        regs = c1.read_holding_registers(0, 32)
        print(regs[0])

    # sleep 2s before next polling
    time.sleep(2)