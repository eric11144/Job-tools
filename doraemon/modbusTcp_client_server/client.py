#!/usr/bin/env python
'''
Pymodbus Synchronous Client Examples
--------------------------------------------------------------------------

The following is an example of how to use the synchronous modbus client
implementation from pymodbus.

It should be noted that the client can also be used with
the guard construct that is available in python 2.5 and up::

    with ModbusClient('127.0.0.1') as client:
        result = client.read_coils(1,10)
        print result
'''
#---------------------------------------------------------------------------#
# import the various server implementations
#---------------------------------------------------------------------------#
from pymodbus.client.sync import ModbusTcpClient as ModbusTCPClient
#from pymodbus.client.sync import ModbusUdpClient as ModbusUDPClient
#from pymodbus.client.sync import ModbusSerialClient as ModbusRTUClient

#---------------------------------------------------------------------------#
# configure the client logging
#---------------------------------------------------------------------------#
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

#---------------------------------------------------------------------------#
# choose the client you want
#---------------------------------------------------------------------------#
# make sure to start an implementation to hit against. For this
# you can use an existing device, the reference implementation in the tools
# directory, or start a pymodbus server.
#
# If you use the UDP or TCP clients, you can override the framer being used
# to use a custom implementation (say RTU over TCP). By default they use the
# socket framer::
#
#    client = ModbusClient('localhost', port=5020, framer=ModbusRtuFramer)
#
# It should be noted that you can supply an ipv4 or an ipv6 host address for
# both the UDP and TCP clients.
#
# There are also other options that can be set on the client that controls
# how transactions are performed. The current ones are:
#
# * retries - Specify how many retries to allow per transaction (default = 3)
# * retry_on_empty - Is an empty response a retry (default = False)
# * source_address - Specifies the TCP source address to bind to
#
# Here is an example of using these options::
#
#    client = ModbusClient('localhost', retries=3, retry_on_empty=True)
#---------------------------------------------------------------------------#
client = ModbusTCPClient('0.0.0.0', port=1502)
#client = ModbusClient(method='ascii', port='/dev/pts/2', timeout=1)
#client = ModbusRTUClient(method='rtu', port='/dev/ttyUSB0', timeout=1)
client.connect()

#---------------------------------------------------------------------------#
# example requests
#---------------------------------------------------------------------------#
# simply call the methods that you would like to use. An example session
# is displayed below along with some assert checks. Note that some modbus
# implementations differentiate holding/input discrete/coils and as such
# you will not be able to write to these, therefore the starting values
# are not known to these tests. Furthermore, some use the same memory
# blocks for the two sets, so a change to one is a change to the other.
# Keep both of these cases in mind when testing as the following will
# _only_ pass with the supplied async modbus server (script supplied).
#---------------------------------------------------------------------------#

#rq = client.write_coils(1, [True]*8)
rr = client.read_coils(1,8,unit=1)
print "Response:", rr.bits
rr = client.read_coils(1,8,unit=2)
print "Response:", rr.bits
#rr = client.read_coils(1,8,unit=2)
#print "Response:", rr.bits
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rr.bits == [True]*8)         # test the expected value

#rq = client.write_coils(1, [False]*8)
rr = client.read_discrete_inputs(1,8,unit=2)
print "Response:", rr.bits
rr = client.read_discrete_inputs(1,8,unit=3)
print "Response:", rr.bits
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rr.bits == [False]*8)        # test the expected value

#rq = client.write_register(1, 10)
rr = client.read_holding_registers(1,8,unit=3)
print "Response:", rr.registers
rr = client.read_holding_registers(1,8,unit=4)
print "Response:", rr.registers
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rr.registers[0] == 10)       # test the expected value

#rq = client.write_registers(1, [10]*8)
rr = client.read_input_registers(1,8,unit=4)
print "Response:", rr.registers
rr = client.read_input_registers(1,8,unit=5)
print "Response:", rr.registers
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rr.registers == [10]*8)      # test the expected value

#---------------------------------------------------------------------------#
# close the client
#---------------------------------------------------------------------------#
client.close()
