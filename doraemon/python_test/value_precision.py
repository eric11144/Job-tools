import pytest
import time

from datetime import datetime
from decimal import Decimal
from snake_charmer.martini.martini import Martini
from snake_charmer.logger import set_logger_callback
from snake_charmer.qonfig.qonfig import Qonfig
from snake_charmer.types import Sort

from chameleon_api_test.env import (
    THE_GATEWAY_WEB_URI,
    THE_GATEWAY_WEB_USER_NAME,
    THE_GATEWAY_WEB_USER_PWD,
    THE_SERVER_WEB_URI,
    THE_SERVER_WEB_USER_NAME,
    THE_SERVER_WEB_USER_PWD
)
from chameleon_api_test.pytest import log_message


class CommonTest:
    CHANNEL_ID = 'value'
    DEVICE_ID = 'mxe'
    TEMPLATE_ID = 'mxe'

    VALUE_LIST = [
        (-2147483648, -2147483640),
        (-147483643, -147483640),
        (-47483643, -47483640),
        (-1234570, -1234567),
        (-565430, -565427),
        (-10003, -10000),
        (-9993, -9990)
        (-993, -990),
        (-13, -10),
        (-5, -1),
        (1, 5),
        (10, 13),
        (990, 993)
        (9990, 9993),
        (10000, 10003),
        (565427, 565430),
        (1234567, 1234570),
        (47483640, 47483643),
        (147483640, 147483643),
        (2147483640, 2147483647)]

    @classmethod
    def setup_virtual_equipment_config(
            cls,
            virtual):
        virtual.post_templates(
            {
                'templateId': cls.TEMPLATE_ID,
                'channels': [
                    {
                        'channelId': cls.CHANNEL_ID,
                        'category': ['data'],
                        'valueType': 'integer'
                    }
                ]
            })

        virtual.put_equipments(
            [
                {
                    "equipmentId": cls.DEVICE_ID,
                    "templateId": cls.TEMPLATE_ID
                }
            ])

        time.sleep(3)

    @pytest.fixture
    def qonfig(
            self,
            request):
        raise NotImplementedError

    @pytest.fixture
    def martini(
            self,
            qonfig,
            request):
        raise NotImplementedError

    @pytest.fixture
    def virtual_device(
            self,
            qonfig):
        return qonfig.virtual_device

    def test_insert_channel_value_CheckWithLatestData(
            self,
            martini,
            virtual_device):
        # act
        set_logger_callback(log_message)
        for element in self.VALUE_LIST:
            for data in range(element[0], element[1]):
                virtual_device.post_virtual_device_reading(
                    self.DEVICE_ID,
                    {
                        "at": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                        "channels":
                        [
                            {
                                "channelId": self.CHANNEL_ID,
                                "value":{"num": data}
                            }
                        ]
                    })

                time.sleep(2)

                # assert
                assert data == martini.get_device_latest_data(self.DEVICE_ID)[0]['latestValue']['value']['num']
        set_logger_callback()

    def test_insert_channel_value_CheckWithHistoryData(
            self,
            martini,
            virtual_device):
        # arrange
        channel_data_list = []
        row_data_list = []

        for element in self.VALUE_LIST:
            for data in range(element[0], element[1]):
                virtual_device.post_virtual_device_reading(
                    self.DEVICE_ID,
                    {
                        "at": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                        "channels":
                        [
                            {
                                "channelId": self.CHANNEL_ID,
                                "value":{"num": data}

                            }
                        ]
                    })
                time.sleep(2)

        # act
        set_logger_callback(log_message)
        rsp, next_data = martini.get_device_channel_data(
            self.DEVICE_ID,
            self.CHANNEL_ID,
            since=datetime.utcnow().strftime('%Y-%m-%dT00:00:00.%fZ'),
            until=datetime.utcnow().strftime('%Y-%m-%dT23:59:59.%fZ'),
            sort=Sort.ASC)

        for element in self.VALUE_LIST:
            for data in range(element[0], element[1]):
                row_data_list.append(data)

        while next_data is not None:
            data, next_data = next_data()
            rsp.extend(data)

        for chaneel_data in rsp:
            channel_data_list.append(chaneel_data['value']['num'])

        # assert
        assert row_data_list == channel_data_list
        set_logger_callback()


class GatewayTest(CommonTest):

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

        self.setup_virtual_equipment_config(qonfig.virtual)

        return qonfig

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
            request.config.getoption('--enable-cert-verify'))

        def teardown():
            qonfig.virtual.put_equipments([])
            qonfig.virtual.delete_template(self.TEMPLATE_ID)
            martini.delete_device(self.DEVICE_ID)

        request.addfinalizer(teardown)

        return martini


# class ServerTest(CommonTest):

#     @pytest.fixture
#     def qonfig(
#             self,
#             request):
#         qonfig = Qonfig(
#             THE_SERVER_WEB_URI,
#             THE_SERVER_WEB_USER_NAME,
#             THE_SERVER_WEB_USER_PWD,
#             3600,
#             request.config.getoption('--enable-cert-verify'))

#         qonfig.readings_filter.put_readings_filter_configuration(
#             {
#                 'mode': 'allow-listed',
#                 'devices': [self.DEVICE_ID]
#             })

#         return qonfig
