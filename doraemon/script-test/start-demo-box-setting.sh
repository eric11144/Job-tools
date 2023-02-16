#!/bin/sh
set -x

IPC_IP='192.168.11.181'
GATEWAY_USERNAME='admin'
GATEWAY_PASSWORD='p@55w0rd'

ACCESS_TOKEN=$(curl -H 'Content-Type: application/json' POST -d "{\"username\": \"${GATEWAY_USERNAME}\", \"password\": \"${GATEWAY_PASSWORD}\"}" http://${IPC_IP}/api/v1/auth  | jq -r .access_token)

curl -H 'Content-Type: application/json' -H "Authorization: JWT ${ACCESS_TOKEN}" -i -X PUT http://${IPC_IP}/api/v1/config/fins/templates/cj2m-cpu32 \
--data-binary @- <<EOF
{
    "channels": [
        {
            "category": [
                "data"
            ],
            "channelId": "temp_C",
            "conversion": {
                "asType": "uint16",
                "multiplier": 0.02
            },
            "raw": {
                "wordAddress": {
                    "address": 0,
                    "memoryArea": "D",
                    "quantity": 1
                }
            }
        },
        {
            "category": [
                "data"
            ],
            "channelId": "humidity_Percent",
            "conversion": {
                "asType": "uint16",
                "multiplier": 0.025
            },
            "raw": {
                "wordAddress": {
                    "address": 1,
                    "memoryArea": "D",
                    "quantity": 1
                }
            }
        },
        {
            "category": [
                "alarm"
            ],
            "channelId": "loader_abnormal",
            "conversion": {
                "asType": "uint16"
            },
            "raw": {
                "bitAddress": {
                    "address": 100,
                    "bit": 7,
                    "memoryArea": "W",
                    "quantity": 1
                }
            }
        },
        {
            "category": [
                "alarm"
            ],
            "channelId": "motor_overload",
            "conversion": {
                "asType": "uint16"
            },
            "raw": {
                "bitAddress": {
                    "address": 100,
                    "bit": 8,
                    "memoryArea": "W",
                    "quantity": 1
                }
            }
        }
    ],
    "commands": [
        {
            "command": "read-word",
            "wordAddress": {
                "address": 0,
                "memoryArea": "D",
                "quantity": 2
            }
        },
        {
            "bitAddress": {
                "address": 100,
                "bit": 7,
                "memoryArea": "W",
                "quantity": 2
            },
            "command": "read-bit"
        }
    ],
    "templateId": "cj2m-cpu32"
}
EOF

curl -H 'Content-Type: application/json' -H "Authorization: JWT ${ACCESS_TOKEN}" -i -X PUT http://${IPC_IP}/api/v1/config/fins/equipments \
--data-binary @- <<EOF
[
    {
        "connection": {
            "tcp": {
                "host": "192.168.20.57",
                "port": 9600
            }
        },
        "equipment": {
            "equipmentId": "cj2m",
            "templateId": "cj2m-cpu32"
        },
        "pollingPeriodMS": 1000,
        "requestTimeoutMS": 200
    }
]
EOF

curl -H 'Content-Type: application/json' -H "Authorization: JWT ${ACCESS_TOKEN}" -X PUT http://${IPC_IP}/api/v1/config/melsec/templates/fx3u-ht \
--data-binary @- <<EOF
{
    "channels": [
        {
            "category": [
                "data"
            ],
            "channelId": "temp_C",
            "channelName": "\u6eab\u5ea6",
            "conversion": {
                "asType": "uint16",
                "multiplier": 0.0375
            },
            "raw": {
                "address": 8260,
                "quantity": 1,
                "registerType": "D"
            }
        },
        {
            "category": [
                "data"
            ],
            "channelId": "humidity_Percent",
            "channelName": "\u6fd5\u5ea6",
            "conversion": {
                "asType": "uint16",
                "multiplier": 0.0675
            },
            "raw": {
                "address": 8261,
                "quantity": 1,
                "registerType": "D"
            }
        },
        {
            "category": [
                "data",
                "alarm"
            ],
            "channelId": "test-node",
            "channelName": "alarm",
            "conversion": {
                "asType": "uint16",
                "multiplier": 0.1
            },
            "raw": {
                "address": 8262,
                "quantity": 1,
                "registerType": "D"
            }
        },
        {
            "category": [
                "data",
                "alarm"
            ],
            "channelId": "Alarm",
            "channelName": "Alarm-test",
            "conversion": {
                "asType": "uint16"
            },
            "raw": {
                "address": 8013,
                "quantity": 1,
                "registerType": "M"
            }
        },
        {
            "category": [
                "data",
                "alarm"
            ],
            "channelId": "M801_4",
            "conversion": {
                "asType": "uint16"
            },
            "raw": {
                "address": 8014,
                "quantity": 1,
                "registerType": "M"
            }
        }
    ],
    "commands": [
        {
            "address": 8260,
            "command": "read-word",
            "quantity": 3,
            "registerType": "D"
        },
        {
            "address": 8013,
            "command": "read-bit",
            "quantity": 2,
            "registerType": "M"
        }
    ],
    "templateId": "fx3u-ht"
}
EOF

curl -H 'Content-Type: application/json' -H "Authorization: JWT ${ACCESS_TOKEN}" -i -X PUT http://${IPC_IP}/api/v1/config/melsec/equipments \
--data-binary @- <<EOF
[
    {
        "connection": {
            "tcp": {
                "host": "192.168.20.51",
                "port": 9600
            }
        },
        "equipmentList": [
            {
                "equipmentId": "fx3u",
                "templateId": "fx3u-ht"
            }
        ],
        "pollingPeriodMS": 1000,
        "protocol": "1E:ascii",
        "requestTimeoutMS": 200
    }
]
EOF

curl -H 'Content-Type: application/json' -H "Authorization: JWT ${ACCESS_TOKEN}" -i -X PUT http://${IPC_IP}/api/v1/config/modbus/templates/iologik \
--data-binary @- <<EOF
{
    "channels": [
        {
            "category": [
                "data"
            ],
            "channelId": "Temperature",
            "channelName": "\u6eab\u5ea6",
            "conversion": {
                "asType": "uint16",
                "multiplier": 0.0007,
                "rounding": {
                    "mode": "round",
                    "position": -2
                }
            },
            "raw": {
                "quantity": 1,
                "reference": 300001
            }
        },
        {
            "category": [
                "data"
            ],
            "channelId": "Humidity",
            "channelName": "\u6fd5\u5ea6",
            "conversion": {
                "asType": "uint16",
                "multiplier": 0.0015,
                "rounding": {
                    "mode": "round",
                    "position": -2
                }
            },
            "raw": {
                "quantity": 1,
                "reference": 300002
            }
        },
        {
            "category": [
                "data"
            ],
            "channelId": "CO_Concentration",
            "channelName": "CO\u6fc3\u5ea6",
            "conversion": {
                "asType": "uint16",
                "multiplier": 0.0015
            },
            "raw": {
                "quantity": 1,
                "reference": 300003
            }
        },
        {
            "category": [
                "data"
            ],
            "channelId": "CO2_Concentration",
            "channelName": "CO2\u6fc3\u5ea6",
            "conversion": {
                "asType": "uint16",
                "multiplier": 0.0305,
                "rounding": {
                    "mode": "round",
                    "position": -2
                }
            },
            "raw": {
                "quantity": 1,
                "reference": 300004
            }
        },
        {
            "category": [
                "data"
            ],
            "channelId": "Water_Depth",
            "channelName": "\u6c34\u4f4d\u6df1\u5ea6",
            "conversion": {
                "asType": "uint16",
                "multiplier": 0.00305
            },
            "raw": {
                "quantity": 1,
                "reference": 300005
            }
        },
        {
            "category": [
                "data"
            ],
            "channelId": "Water_Pressure",
            "channelName": "\u6c34\u58d3",
            "conversion": {
                "asType": "uint16",
                "multiplier": 3e-06
            },
            "raw": {
                "quantity": 1,
                "reference": 300005
            }
        }
    ],
    "commands": [
        {
            "address": 0,
            "command": "read-input-registers",
            "quantity": 8
        }
    ],
    "templateId": "iologik"
}
EOF

curl -H 'Content-Type: application/json' -H "Authorization: JWT ${ACCESS_TOKEN}" -i -X PUT http://${IPC_IP}/api/v1/config/modbus/templates/tgp03_thp03 \
--data-binary @- <<EOF
{
    "channels": [
        {
            "category": [
                "data"
            ],
            "channelId": "temperature",
            "conversion": {
                "asType": "float32",
                "byteOrder": "CDAB",
                "rounding": {
                    "mode": "round",
                    "position": -2
                }
            },
            "raw": {
                "quantity": 2,
                "reference": 400001
            }
        },
        {
            "category": [
                "data"
            ],
            "channelId": "humidity",
            "conversion": {
                "asType": "float32",
                "byteOrder": "CDAB",
                "rounding": {
                    "mode": "round",
                    "position": -2
                }
            },
            "raw": {
                "quantity": 2,
                "reference": 400003
            }
        },
        {
            "category": [
                "data"
            ],
            "channelId": "CO2",
            "conversion": {
                "asType": "float32",
                "byteOrder": "CDAB"
            },
            "raw": {
                "quantity": 2,
                "reference": 400005
            }
        },
        {
            "category": [
                "data"
            ],
            "channelId": "particulate_matter_measurement",
            "conversion": {
                "asType": "float32",
                "byteOrder": "CDAB"
            },
            "raw": {
                "quantity": 2,
                "reference": 400007
            }
        }
    ],
    "commands": [
        {
            "address": 0,
            "command": "read-holding-registers",
            "quantity": 8
        }
    ],
    "templateId": "tgp03_thp03"
}
EOF

curl -H 'Content-Type: application/json' -H "Authorization: JWT ${ACCESS_TOKEN}" -i -X PUT http://${IPC_IP}/api/v1/config/modbus/equipments \
--data-binary @- <<EOF
[
    {
        "endPoint": {
            "host": "192.168.20.64",
            "port": 502
        },
        "equipments": [
            {
                "equipmentId": "modbus",
                "id": 1,
                "templateId": "iologik"
            }
        ],
        "pollingPeriodMS": 200,
        "requestTimeoutMS": 500
    },
    {
        "endPoint": {
            "host": "127.0.0.1",
            "port": 502
        },
        "equipments": [
            {
                "equipmentId": "air_quality_sensor",
                "id": 1,
                "templateId": "tgp03_thp03"
            }
        ],
        "pollingPeriodMS": 200,
        "requestTimeoutMS": 500
    }
]
EOF

curl -H 'Content-Type: application/json' -H "Authorization: JWT ${ACCESS_TOKEN}" -i -X PUT http://${IPC_IP}/api/v1/modbusgateways \
--data-binary @- <<EOF
[
    {
        "config": {
            "baudrate": "9600",
            "intercharTimeoutMS": 100,
            "interframeDelayMS": 0,
            "parity": "none",
            "requestTimeoutMS": 500,
            "stopbits": "one"
        },
        "env": {
            "device": "/dev/ttyS4",
            "modbusTcpPort": 502
        }
    }
]
EOF

curl -H 'Content-Type: application/json' -H "Authorization: JWT ${ACCESS_TOKEN}" -i -X PUT http://${IPC_IP}/api/v1/safeboxes/meta-data \
--data-binary @- <<EOF
[
    {
        "equipmentId": "Omron",
        "equipmentType": 1
    },
    {
        "equipmentId": "FX3U",
        "equipmentType": 0
    },
    {
        "equipmentId": "modbus",
        "equipmentType": "4"
    },
    {
        "equipmentId": "AQ_sensor",
        "equipmentType": 1
    },
    {
        "equipmentId": "cj2m",
        "equipmentType": 1
    },
    {
        "equipmentId": "air_quality_sensor",
        "equipmentType": 1
    },
    {
        "equipmentId": "fx3u",
        "equipmentType": 0
    }
]
EOF

curl -H 'Content-Type: application/json' -H "Authorization: JWT ${ACCESS_TOKEN}" -i -X PUT http://${IPC_IP}/api/v1/safeboxes/line-data \
--data-binary @- <<EOF
[
    {
        "dequips": [
            "modbus",
            "fx3u"
        ],
        "title": "\u7522\u7dda 1"
    },
    {
        "dequips": [
            "cj2m",
            "air_quality_sensor"
        ],
        "title": "\u7522\u7dda 2"
    }
]
EOF
