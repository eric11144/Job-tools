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
    DeviceInfo(DeviceId("NA-600FN")))

index = 0
while True:
    reading = Reading()
    reading.set(
        ChannelId("X3"),
        Value(Decimal("5")))
    reading.set(
        ChannelId("X7"),
        Value(index))
    reading.set(
        ChannelId("X8"),
        Value(Decimal("0")))
    reading.set(
        ChannelId("X9"),
        Value(Decimal("0")))
    reading.set(
        ChannelId("X1C"),
        Value(Decimal("1000")))
    reading.set(
        ChannelId("X1D"),
        Value(Decimal("800")))
    reading.set(
        ChannelId("X1E"),
        Value(Decimal("1")))
    reading.set(
        ChannelId("Y2"),
        Value(Decimal("24")))
    reading.set(
        ChannelId("Y3"),
        Value(Decimal("1")))
    reading.set(
        ChannelId("Y4"),
        Value(Decimal("0")))
    reading.set(
        ChannelId("Y5"),
        Value(Decimal("0")))
    reading.set(
        ChannelId("Y13"),
        Value(Decimal("0")))
    reading.set(
        ChannelId("Y14"),
        Value(Decimal("0")))
    reading.set(
        ChannelId("Y15"),
        Value(Decimal("1")))
    reading.set(
        ChannelId("R30F"),
        Value(Decimal("0")))
    reading.set(
        ChannelId("R310"),
        Value(Decimal("0")))
    reading.set(
        ChannelId("R31B"),
        Value(Decimal("0")))
    reading.set(
        ChannelId("DT530"),
        Value(index))
    reading.set(
        ChannelId("DT630"),
        Value(Decimal("5")))
    reading.set(
        ChannelId("DT631"),
        Value(Decimal("500")))
    reading.set(
        ChannelId("DT632"),
        Value(Decimal("5000")))
    reading.set(
        ChannelId("DT633"),
        Value(Decimal("30")))
    reading.set(
        ChannelId("DT634"),
        Value(Decimal("1.414")))
    reading.set(
        ChannelId("DT2018"),
        Value(Decimal("0")))
    reading.set(
        ChannelId("DT2020"),
        Value(Decimal("0")))
    reading.set(
        ChannelId("DT2028"),
        Value(Decimal("0")))
    reading.set(
        ChannelId("DT2030"),
        Value(Decimal("0")))

    sensor.update(reading)

    sleep(5)

    index += 1
