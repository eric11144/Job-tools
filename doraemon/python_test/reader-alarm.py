from datetime import timedelta

from libqurrent_py import (
    Service,
    StreamId)

reading_subscriber = Service.instance().create_reading_subscriber(1, StreamId("alarm"))

while True:
    if not reading_subscriber.wait(timedelta(seconds=3)):
        continue

    device_reading_list = reading_subscriber.read()

    for device_reading in device_reading_list:
        print(device_reading)
