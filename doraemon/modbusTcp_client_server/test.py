#!/usr/bin/env python
'''
Pymodbus Synchronous Server Example
--------------------------------------------------------------------------

The synchronous server is implemented in pure python without any third
party libraries (unless you need to use the serial protocols which require
pyserial). This is helpful in constrained or old environments where using
twisted just is not feasable. What follows is an examle of its use:
'''
#---------------------------------------------------------------------------#
# import the various server implementations
#---------------------------------------------------------------------------#
from pymodbus.server.sync import StartTcpServer
from pymodbus.server.sync import StartUdpServer
from pymodbus.server.sync import StartSerialServer
import os
import random

# --------------------------------------------------------------------------- #
# import the modbus libraries we need
# --------------------------------------------------------------------------- #
from pymodbus.server.async import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# --------------------------------------------------------------------------- #
# import the twisted libraries we need
# --------------------------------------------------------------------------- #
from twisted.internet.task import LoopingCall

# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

HOST = os.environ.get("MODBUS_TCP_SERVER_HOST", "192.168.20.193")
PORT = int(os.environ.get("MODBUS_TCP_SERVER_PORT", 502))

DATA_LENGTH = int(os.environ.get("MODBUS_TCP_SERVER_DATA_LENGTH", 1000))
UPDATE_FREQUENCY_SEC = int(os.environ.get(
    "MODBUS_TCP_SERVER_UPDATE_FREQUENCY_SEC", 3))

# --------------------------------------------------------------------------- #
# define callback process
# --------------------------------------------------------------------------- #
def updating_writer(a):
    context  = a[0]
    begin_address = 0x00

    word_values = [random.randint(0, 20) for i in range(DATA_LENGTH)]
    print(word_values)
    bit_values = [random.randint(0, 1) for i in range(DATA_LENGTH)]
    print(bit_values)

    context[0].setValues(1, begin_address, bit_values)  # coils
    context[0].setValues(2, begin_address, bit_values)  # discrete_inputs
    context[0].setValues(3, begin_address, word_values) # holding_registers
    context[0].setValues(3, begin_address, word_values) # holding_registers
    context[0].setValues(4, begin_address, word_values) # input_registers

def main():
    # ----------------------------------------------------------------------- #
    # initialize your data store
    # ----------------------------------------------------------------------- #
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17]*DATA_LENGTH),
        co=ModbusSequentialDataBlock(0, [17]*DATA_LENGTH),
        hr=ModbusSequentialDataBlock(0, [17]*DATA_LENGTH),
        ir=ModbusSequentialDataBlock(0, [17]*DATA_LENGTH))
    context = ModbusServerContext(slaves=store, single=True)

    # ----------------------------------------------------------------------- #
    # initialize the server information
    # ----------------------------------------------------------------------- #
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/bashwork/pymodbus/'
    identity.ProductName = 'pymodbus Server'
    identity.ModelName = 'pymodbus Server'
    identity.MajorMinorRevision = '1.0'

    #---------------------------------------------------------------------------#
    # run the modbus server
    #---------------------------------------------------------------------------#
    loop = LoopingCall(f=updating_writer, a=(context,))
    loop.start(UPDATE_FREQUENCY_SEC, now=False)
    StartTcpServer(context, identity=identity, address=(HOST, PORT))

if __name__ == "__main__":
    main()

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

from pymodbus.transaction import ModbusRtuFramer
#---------------------------------------------------------------------------#
# configure the service logging
#---------------------------------------------------------------------------#
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

#---------------------------------------------------------------------------#
# initialize your data store
#---------------------------------------------------------------------------#
# The datastores only respond to the addresses that they are initialized to.
# Therefore, if you initialize a DataBlock to addresses of 0x00 to 0xFF, a
# request to 0x100 will respond with an invalid address exception. This is
# because many devices exhibit this kind of behavior (but not all)::
#
#     block = ModbusSequentialDataBlock(0x00, [0]*0xff)
#
# Continuing, you can choose to use a sequential or a sparse DataBlock in
# your data context.  The difference is that the sequential has no gaps in
# the data while the sparse can. Once again, there are devices that exhibit
# both forms of behavior::
#
#     block = ModbusSparseDataBlock({0x00: 0, 0x05: 1})
#     block = ModbusSequentialDataBlock(0x00, [0]*5)
#
# Alternately, you can use the factory methods to initialize the DataBlocks
# or simply do not pass them to have them initialized to 0x00 on the full
# address range::
#
#     store = ModbusSlaveContext(di = ModbusSequentialDataBlock.create())
#     store = ModbusSlaveContext()
#
# Finally, you are allowed to use the same DataBlock reference for every
# table or you you may use a seperate DataBlock for each table. This depends
# if you would like functions to be able to access and modify the same data
# or not::
#
#     block = ModbusSequentialDataBlock(0x00, [0]*0xff)
#     store = ModbusSlaveContext(di=block, co=block, hr=block, ir=block)
#
# The server then makes use of a server context that allows the server to
# respond with different slave contexts for different unit ids. By default
# it will return the same context for every unit id supplied (broadcast
# mode). However, this can be overloaded by setting the single flag to False
# and then supplying a dictionary of unit id to context mapping::
#
#     slaves  = {
#         0x01: ModbusSlaveContext(...),
#         0x02: ModbusSlaveContext(...),
#         0x03: ModbusSlaveContext(...),
#     }
#     context = ModbusServerContext(slaves=slaves, single=False)
#
# The slave context can also be initialized in zero_mode which means that a
# request to address(0-7) will map to the address (0-7). The default is
# False which is based on section 4.4 of the specification, so address(0-7)
# will map to (1-8)::
#
#     store = ModbusSlaveContext(..., zero_mode=True)
#---------------------------------------------------------------------------#
store = {
	0x01: ModbusSlaveContext(
	    di = ModbusSequentialDataBlock(0, [20]*800),
	    co = ModbusSequentialDataBlock(0, [19]*800),
	    ir = ModbusSequentialDataBlock(0, [15]*200),
	    hr = ModbusSequentialDataBlock(0, [100]*1000),
	),

	0x02: ModbusSlaveContext(
	    di = ModbusSequentialDataBlock(0, [55]*200),
	    co = ModbusSequentialDataBlock(0, [30]*200),
	    hr = ModbusSequentialDataBlock(0, [18]*200),
	    ir = ModbusSequentialDataBlock(0, [15]*200)
	),

	0x03: ModbusSlaveContext(
	    di = ModbusSequentialDataBlock(0, [20]*100),
	    co = ModbusSequentialDataBlock(0, [19]*100),
	    hr = ModbusSequentialDataBlock(0, [50]*100),
	    ir = ModbusSequentialDataBlock(0, [15]*100)
	)

}
context = ModbusServerContext(slaves=store, single=False)

#---------------------------------------------------------------------------#
# initialize the server information
#---------------------------------------------------------------------------#
# If you don't set this or any fields, they are defaulted to empty strings.
#---------------------------------------------------------------------------#
identity = ModbusDeviceIdentification()
identity.VendorName  = 'Pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl   = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'Pymodbus Server'
identity.ModelName   = 'Pymodbus Server'
identity.MajorMinorRevision = '1.0'

#---------------------------------------------------------------------------#
# run the server you want
#---------------------------------------------------------------------------#
# Tcp:
#StartSerialServer(context, identity=identity, port='/dev/ttyUSB1', timeout=1)
StartTcpServer(context, address=('192.168.20.196', 502))
