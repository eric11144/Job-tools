import csv
import dateutil.parser
import gzip
import os
import shutil
import sys
import time

from datetime import (
    datetime
)
from decimal import Decimal
from pytz import timezone

from snake_charmer.chameleon import Chameleon


float_map = [
    'D110',
    'D112',
    'D114',
    'D201'
]
str_map = [
    'Address_Name',
    'Dev_Address',
    'Dev_ID',
    'Dev_Name'
]

device_map = {
    'Address_virtual': 'Address_virtual',
    '21DFPLAM001_virtual': 'L21DFPLAM001_virtual',
    '21DFPLAM002_virtual': 'L21DFPLAM002_virtual',
    '21DFPLAM003_virtual': 'L21DFPLAM003_virtual'
}

def post_reading(
        device_id,
        request_body):
    chameleon = Chameleon(
        'http://192.168.11.197/api/v1',
        'admin',
        'p@55w0rd')

    api = chameleon.virtual

    api.post_reading(
        device_id,
        request_body)


def get_csv_list(file_dir):
    file_list = []

    for files in os.listdir(file_dir):
        file_list.append(files)
    
    file_list.sort(reverse=False)

    return file_list

def insert_csv_data(path, csv_name_list):
    os.makedirs('finish', exist_ok=True)
    number_of_file  = len(csv_name_list)
 
    for csv_name in csv_name_list:
        print(number_of_file)
        print(datetime.now())
        print(csv_name)
        channels_quantity = 0

        with gzip.open(path + csv_name, 'rt') as csvfile:
            rows = csv.DictReader(csvfile)

            for row in rows:
                device = device_map[row['device_id']]
                del row['device_id']
                
                date_time = dateutil.parser.parse(row['datetime'])
                data_utc_date = date_time.astimezone(timezone('UTC'))
                del row['datetime']

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
                    'at': data_utc_date,
                    'channels': channels_list
                }

                post_reading(
                    device,
                    request_body)

                # time.sleep(1)
                channels_quantity += 1
            
                print(channels_quantity)
            
            shutil.move(path + csv_name, 'finish')

            number_of_file -= 1

            print(number_of_file)
            print(str(datetime.now())  + ' finish \n')

def main():
    csv_path = sys.argv[1:]
    csv_path_str = str(csv_path[0])
    csv_name_list = get_csv_list(csv_path_str)
    insert_csv_data(csv_path_str, csv_name_list)

if __name__ == "__main__":
    main()
