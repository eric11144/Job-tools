import datetime
import dateutil.parser
import requests
import time

from decimal import Decimal

from libqurrent_py import (
    ChannelId,
    DeviceId,
    DeviceInfo,
    Reading,
    Service,
    Value)


CHANNEL_ID = 'value'
DEVICE_ID = 'mxe'
INSERT_PERIOD_SEC = 0.02
IPC_IP = 'localhost'

RESPONSE_DATA_LIST = []

VALUE_LIST = [
    (-2147483648, -2147483637),
    (-1147483635, -1147483626),
    (-1000010, -999990),
    (-200000, -199980),
    (-12360, -12340),
    (-9000, -8950),
    (-1000, -990),
    (-20, -1),
    (0, 1000),
    (9990, 10000),
    (565420, 565440),
    (999990, 1000010),
    (1234560, 1234570),
    (47483640, 47483650),
    (147483640, 147483650),
    (1147483640, 1147483650),
    (2147483640, 2147483647)
]


def insert_data():
    service = Service.instance()

    now = str(datetime.datetime.now())
    date_time = dateutil.parser.parse(now)

    sensor = service.create_sensor(
        DeviceInfo(
            DeviceId(DEVICE_ID)
        )
    )
    reading = Reading()
    for element in VALUE_LIST:
        for data in range(element[0], element[1]):
            reading.set(
                ChannelId('value'),
                Value(Decimal(data))
            )

            date_time += datetime.timedelta(seconds=0.5)

            time.sleep(INSERT_PERIOD_SEC)

            sensor.update(
                reading,
                date_time)

            rsp = (
                requests.get('http://' + IPC_IP + '/api/v1/devices/' + DEVICE_ID + '/channels/latest-data')
            )

            response_json = rsp.json()
            latest_data = response_json[0]['latestValue']['value']['num']

            if data != latest_data:
                raise ValueError('data is different' + str(data))

def get_response_data():
    rsp = (
        requests.get(
            'http://' + IPC_IP + '/api/v1' +
            '/devices/' + DEVICE_ID +
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
    next_data_list = []
    next_response = requests.get(response.headers['Link'][:-12])
    next_response_json = next_response.json()

    for next_data in next_response_json:
        next_data_list.append(next_data)

    if 'Link' in next_response.headers.keys():
        get_next_data(next_response)
    else:
        return next_data_list

    return next_data_list

def check_reponse_data(response_json):
    number = 0

    for row in response_json:
        RESPONSE_DATA_LIST.append(row['value']['num'])

    for element in VALUE_LIST:
        for data in range(element[0], element[1]):
            if data not in RESPONSE_DATA_LIST:
                raise ValueError(
                    str(data) + ' is not in list ')
            number += 1

def main():
    insert_data()

    response_json = get_response_data()

    if 'code' in response_json:
        raise ValueError(response_json['message'])
    else:
        check_reponse_data(response_json)

if __name__ == "__main__":
    main()




class TestUpdateReading:
    TEMPLATE_ID = 'xxx'

    @pytest.fixture
    def qonfig(
            self,
            request):
        qonfig = Qonfig(
            THE_GATEWAY_WEB_URI,
            THE_GATEWAY_WEB_USER_NAME,
            THE_GATEWAY_WEB_USER_PWD,
            3600,
            request.config.getoption('--enable-cert-verify'))

        return qonfig

    @pytest.fixture
    def virtual(
            self,
            qonfig):
        return qonfig.virtual

    @pytest.fixture
    def virtual_device(
            self,
            qonfig):
        return qonfig.virtual_device

    @pytest.fixture
    def martini(
            self,
            qonfig,
            request):
        martini = Martini(
            THE_GATEWAY_WEB_URI,
            THE_GATEWAY_WEB_USER_NAME,
            THE_GATEWAY_WEB_USER_PWD,
            3600,
            False)

        def teardown():
            qonfig.virtual.put_equipments([])
            qonfig.virtual.delete_template(TEMPLATE_ID)
            martini.delete_device(DEVICE_ID)

        request.addfinalizer(teardown)

        return martini
