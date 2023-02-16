import csv
import os
import sys
import time

from datetime import (
    datetime,
    timezone,
)
from decimal import Decimal

from snake_charmer.chameleon import Chameleon


float_map = []
str_map = []


def post_reading(
        device_id,
        request_body):
    chameleon = Chameleon(
        'http://192.168.11.195/api/v1',
        'admin',
        'p@55w0rd')

    api = chameleon.virtual

    api.post_reading(
        device_id,
        request_body)


def insert_csv_data(csv_name):
    device = 'test'
    with open(csv_name, newline='', encoding='utf-8') as csvfile:
        rows = csv.DictReader(csvfile)
        # print(rows)
        while True:
            for row in rows:
                del row['datetime']
                del row['device_id']

                channels_list = []
                for channel_id, channel_value in row.items():
                    if channel_id in float_map:
                        float_dict = {
                            'channelId': channel_id,
                            'value': {'num': float(channel_value)}
                        }
                        channels_list.append(float_dict)
                    elif channel_id in str_map:
                        string_dict = {
                            'channelId': channel_id,
                            'value': {'str': str(channel_value)}
                        }
                        channels_list.append(string_dict)
                    else:
                        int_dict = {
                            'channelId': channel_id,
                            'value': {'num': int(channel_value)}
                        }
                        channels_list.append(int_dict)

                request_body = {
                    'at': datetime.utcnow().replace(tzinfo=timezone.utc),
                    'channels': channels_list
                }

                post_reading(
                    device,
                    request_body)

                time.sleep(1)

def main():
    insert_csv_name = sys.argv[1]
    csv_name = str(insert_csv_name)
    insert_csv_data(csv_name)

if __name__ == "__main__":
    main()
