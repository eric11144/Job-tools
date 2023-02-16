from time import sleep
from decimal import Decimal

from libqurrent_py import (
    ChannelId,
    DeviceId,
    DeviceInfo,
    Service,
    Reading,
    Value)

# prepare reading schema
sensor = Service.instance().create_sensor(
    DeviceInfo(DeviceId('barcode_scanner')))

index = 0
while True:
    if index >= 86400:
        index = 0

    str_ = 'A003T-LOT' + str(index)

    reading = Reading()
    reading.set(
        ChannelId('barcode'),
        Value(str_))

    sensor.update(reading)
    sleep(30)

    index += 1
