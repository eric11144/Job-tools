import csv
import datetime
import dateutil.parser
from decimal import Decimal
import gzip
import os
from pytz import timezone
import shutil
import sys
import time

from libqurrent_py import (
    ChannelId,
    DeviceId,
    DeviceInfo,
    Reading,
    Service,
    Value)


INSERT_PERIOD_SEC = 0.1


def insert_csv_to_libqurrent(file_path):
    service = Service.instance()

    sensor = None
    reading = Reading()

    with gzip.open(file_path, 'rt') as read_csv_gz:
        rows = csv.DictReader(read_csv_gz)

        for row in rows:
            if sensor is None:
                sensor = service.create_sensor(
                    DeviceInfo(
                        DeviceId(row['device_id'])
                    )
                )

            # TODO timezone
            date_time = dateutil.parser.parse(row['datetime'])
            data_utc_date = date_time.astimezone(timezone('UTC'))

            del row['device_id']
            del row['datetime']

            # SET channel id & channel value
            for channel_id, channel_value in row.items():
                if isinstance(channel_value, int):
                    value = Decimal(channel_value)
                elif isinstance(channel_value, float):
                    value = Decimal(str(channel_value))
                else:
                    assert isinstance(channel_value, str)
                    value = channel_value

                reading.set(
                    ChannelId(channel_id),
                    Value(value)
                )

            time.sleep(INSERT_PERIOD_SEC)

            sensor.update(
                reading,
                data_utc_date)

def main():
    assert len(sys.argv) == 2

    file_path = sys.argv[1]
    insert_csv_to_libqurrent(file_path)

if __name__ == "__main__":
    main()
