import time

from datetime import (
    datetime,
    timezone,
)
from decimal import Decimal
from random import randint

from snake_charmer.chameleon import Chameleon


def post_reading(
        device_id,
        request_body):
    chameleon = Chameleon(
        'http://localhost/api/v1',
        'admin',
        'p@55w0rd')

    api = chameleon.virtual
    print(api)
    api.post_reading(
        device_id,
        request_body)


def main():
    device_id = 'sample_device'

    while True:
        for index in range(65535):
            request_body = {
                'at': datetime.utcnow().replace(tzinfo=timezone.utc),
                'channels': [
                    {
                        'channelId': 'work_order',
                        'value': {'str': '12IIA8007EX-SUB1'},
                    },
                    {
                        'channelId': 'index',
                        'value': {'num': index},
                    },
                    {
                        'channelId': 'voltage_V',
                        'value': {'num': randint(20, 30)},
                    },
                    {
                        'channelId': 'M00',
                        'value': {'num': randint(0, 200)},
                    },
                    {
                        'channelId': 'M01',
                        'value': {'num': randint(0, 200)},
                    },
                    {
                        'channelId': 'M02',
                        'value': {'num': randint(0, 200)},
                    },
                    {
                        'channelId': 'M03',
                        'value': {'num': randint(0, 200)},
                    },
                    {
                        'channelId': 'M04',
                        'value': {'num': randint(0, 200)},
                    },
                    {
                        'channelId': 'M05',
                        'value': {'num': randint(0, 200)},
                    },
                    {
                        'channelId': 'M06',
                        'value': {'num': randint(0, 1)},
                    },
                    {
                        'channelId': 'M07',
                        'value': {'num': randint(0, 1)},
                    },
                    {
                        'channelId': 'M08',
                        'value': {'num': randint(0, 1)},
                    },
                    {
                        'channelId': 'M09',
                        'value': {'num': randint(0, 1)},
                    },
                    {
                        'channelId': 'M10',
                        'value': {'num': randint(0, 1)},
                    },
                    {
                        'channelId': 'M11',
                        'value': {'num': randint(0, 200)},
                    },
                    {
                        'channelId': 'M12',
                        'value': {'num': randint(0, 200)},
                    },
                    {
                        'channelId': 'M13',
                        'value': {'num': randint(0, 200)},
                    },
                    {
                        'channelId': 'M14',
                        'value': {'num': randint(0, 200)},
                    },
                    {
                        'channelId': 'M15',
                        'value': {'num': randint(0, 200)},
                    },
                    {
                        'channelId': 'M16',
                        'value': {'num': randint(0, 200)},
                    },
                    {
                        'channelId': 'M17',
                        'value': {'num': randint(0, 1)},
                    },
                    {
                        'channelId': 'M18',
                        'value': {'num': randint(0, 1)},
                    },
                    {
                        'channelId': 'M19',
                        'value': {'num': randint(0, 1)},
                    },
                    {
                        'channelId': 'M20',
                        'value': {'num': randint(0, 1)},
                    }
                ]
            }

            post_reading(
                device_id,
                request_body)

            time.sleep(30)

if __name__ == "__main__":
    main()
