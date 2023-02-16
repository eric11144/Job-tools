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

HOST = os.environ.get("MODBUS_TCP_SERVER_HOST", "192.168.11.196")
PORT = int(os.environ.get("MODBUS_TCP_SERVER_PORT", 1502))

DATA_LENGTH = int(os.environ.get("MODBUS_TCP_SERVER_DATA_LENGTH", 200))
UPDATE_FREQUENCY_SEC = int(os.environ.get(
    "MODBUS_TCP_SERVER_UPDATE_FREQUENCY_SEC", 3))

# --------------------------------------------------------------------------- #
# define callback process
# --------------------------------------------------------------------------- #
def updating_writer(a):
    context  = a[0]
    begin_address = 0x00

    # values = context[slave_id].getValues(input_registers, address, count=5)
    word_max_values = [
        0x8000, # int16_max -32767
        0x7FFF, # int16_min -32768
        0x8000, 0x0000, # int32_min -2147483648
        0x7FFF, 0xFFFF, # int32_max 2147483647
        0x7FFF, 0xFFFF, 0xFFFF, 0xFFFF, # int64_max 9223372036854775807
        0x8000, 0x0000, 0x0000, 0x0000, # int64_min -9223372036854775808
        0, # uint min 0
        0xFFFF, # uint16 max 65535
        0xFFFF,0xFFFF, # uint32 max 4294967295
        0xFFFF,0xFFFF,0xFFFF,0xFFFF, # uint64 max 18446744073709551615
        0x0000, 0x1, # float32 positive number min 1.4e-45
        0x7F7F, 0xc99e, # float32 positive number max 3.4e+38
        0xFF7F, 0xc99e, # float32 negative number min -3.4e+38
        0x8000, 0x0001, # float32 negative number max -1.4e-45
        0x0000, 0x0000, 0x0000, 0x0001, # float64 positive number min 4.94065e-324
        0x7FEF, 0xFFFF, 0xFFFF, 0xFFFF, # float64 positive number max 1.8e+308
        0xFFEF, 0xFFFF, 0xFFFF, 0xFFFF, # float64 negative number min -1.8e+308
        0x8000, 0x0000, 0x0000, 0x0001, # float64 negative number max -4.9e-324
        0x7FFF, 0xFFFE, # int32 2147483646
        0x7FFF, 0xFFFD, # int32 2147483645
        0x8000, 0x0001, # int32 -2147483647
        0x8000, 0x0002, # int32 -2147483646
        0xFFFF,0xFFFE, # uint32 4294967294
        0xFFFF,0xFFFD, # uint32 4294967293
        0x7FFF, 0xFFFF, 0xFFFF, 0xFFFE, # int64 9223372036854775806
        0x7FFF, 0xFFFF, 0xFFFF, 0xFFFD, # int64 9223372036854775805
        0x8000, 0x0000, 0x0000, 0x0001, # int64 -9223372036854775807
        0x8000, 0x0000, 0x0000, 0x0002, # int64 -9223372036854775806
        0xFFFF,0xFFFF,0xFFFF,0xFFFE, # uint64 18446744073709551614
        0xFFFF,0xFFFF,0xFFFF,0xFFFD, # uint64 18446744073709551613
        0xFFFF, 0xFFFF,
        0x0000, 0x0001,
        0x1000, 0x0000
    ]

    random_begin = len(word_max_values)

    word_values = [random.randint(0, 20) for i in range(random_begin, DATA_LENGTH)]
    print(word_values)
    bit_values = [random.randint(0, 1) for i in range(DATA_LENGTH)]
    print(bit_values)

    context[0].setValues(1, begin_address, bit_values)  # coils
    context[0].setValues(2, begin_address, bit_values)  # discrete_inputs
    context[0].setValues(3, begin_address, word_max_values) # holding_registers
    context[0].setValues(3, random_begin, word_values) # holding_registers
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

