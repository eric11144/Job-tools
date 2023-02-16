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

    api.post_reading(
        device_id,
        request_body)

def main():
    device_id = 'barcode_scanner'
    barcode_index = 0

    while True:
        if index >= 86400:
            index = 0
        barcode = 'A003T-LOT' + str(index)
        request_body = {
            'at': datetime.utcnow().replace(tzinfo=timezone.utc),
            'channels': [
                {
                    'channelId': 'barcode',
                    'value': {'str': barcode},
                }
            ],
        }

        post_reading(
            device_id,
            request_body)

        time.sleep(60)
        index += 1

if __name__ == "__main__":
    main()
