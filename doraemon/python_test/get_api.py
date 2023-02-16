import json
import pprint
import requests


CHANNEL_ID = 'value'
DEVICE_ID = 'mxe'
IPC_IP = '192.168.11.122'
NEXT_DATA_LIST = []
RESPONSE_DATA_LIST = []

# CHECK_DATA_LIST = [
#     (-2147483648, -2147483637),
#     (-1147483635, -1147483626),
#     (-1000010, -999990),
#     (-200000, -199980),
#     (-12360, -12340),
#     (-9000, -8950),
#     (-1000, -990),
#     (-20, -1),
#     (0, 1000),
#     (9990, 10000),
#     (565420, 565440),
#     (999990, 1000010),
#     (1234560, 1234570),
#     (47483640, 47483650),
#     (147483640, 147483650),
#     (1147483640, 1147483650),
#     (2147483640, 2147483647)
# ]

CHECK_DATA_LIST = [
    (0, 2000)
    ]

def get_response_data():
    next_data = None
    base_path = 'http://' + IPC_IP + '/api/v1'

    rsp = (
        requests.get(
            base_path + '/devices/' + DEVICE_ID +
            '/channels/' + CHANNEL_ID +
            '/data?sort=ASC&pageSize=1000')
    )

    response_json = rsp.json()

    if 'Link' in rsp.headers.keys():
        next_data = get_next_data(rsp)
        for data in next_data:
            response_json.append(data)
    else :
        return response_json

    return response_json

def get_next_data(response):
    next_response = requests.get(response.headers['Link'][:-12])
    next_response_json = next_response.json()

    for next_data in next_response_json:
        NEXT_DATA_LIST.append(next_data)

    if 'Link' in next_response.headers.keys():
        get_next_data(next_response)
    else:
        return NEXT_DATA_LIST

    return NEXT_DATA_LIST

def check_reponse_data(response_json):
    number = 0

    for row in response_json:
        RESPONSE_DATA_LIST.append(row['value']['num'])

    for element in CHECK_DATA_LIST:
        for data in range(element[0], element[1]):
            if data not in RESPONSE_DATA_LIST:
            #    continue
                print(str(number) + " : " + str(data))
            number += 1

def main():
    response_json = get_response_data()

    if 'code' in response_json:
        raise ValueError(response_json['message'])
    else:
        check_reponse_data(response_json)


if __name__ == "__main__":
    main()
