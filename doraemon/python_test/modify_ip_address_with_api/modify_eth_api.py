import re
import os
import sys

import json 
import validators
import yaml

from flask import Flask, request, make_response
from voluptuous import (
    All,
    Any,
    Length,
    Optional,
    Required,
    Schema
)

app = Flask(__name__)

#Type 1
@app.route("/network/ip", methods=['GET'])
def get_network_ip():

    try:
        import netifaces
    except ImportError:
        try:
            command_to_execute = "pip install netifaces || easy_install netifaces"
            os.system(command_to_execute)
        except OSError:
            print("Can NOT install netifaces, Aborted!")
            sys.exit(1)
        import netifaces

    routingGateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
    routingNicName = netifaces.gateways()['default'][netifaces.AF_INET][1]

    for interface in netifaces.interfaces():
        if interface == routingNicName:
            # print netifaces.ifaddresses(interface)
            routingNicMacAddr = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
            try:
                routingIPAddr = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
                # TODO(Guodong Ding) Note: On Windows, netmask maybe give a wrong result in 'netifaces' module.
                routingIPNetmask = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
            except KeyError:
                pass

    network_info = {
        "Routing_NIC_Name": routingNicName,
        "Routing_MAC_Address": routingNicMacAddr,
        "Routing_Address": routingIPAddr,
        "Routing_NetMask": routingIPNetmask,
        "Routing_Gateway": routingGateway
    }

    return json.dumps(network_info,  indent = 2)


_IPV4_CIDR_NOTATION = re.compile(
    r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}'
    + r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])'
    + r'/[0]{0,}(3[0-2]|[1-2][0-9]|[1-9])$'
)


def _ipv4_cidr_notation(value: str) -> bool:
    '''
    validate IPv4 CIDR notation (x.x.x.x/prefix-length)

    Args:
        value (str): IPv4 CIDR notation.

    Return:
        value.
    '''
    return bool(_IPV4_CIDR_NOTATION.match(value))

_PUT_NETWORK_SCHEMA = Schema(Any(
    {
        Required('addresses'): All(
            [All(str, _ipv4_cidr_notation)],
            Length(min=1, max=1)
        ),
        Optional('gateway4'): All(str, validators.ipv4),
        Optional('nameservers'): All(
            [All(str, _ipv4_cidr_notation)],
            Length(min=0, max=1)
        )
    }
))


#Type 2
@app.route("/network/ip/change", methods=['POST'])
def post_network_ip():
    '''
    POST /network/ip/change
    '''
    network_change_info = request.json

    try:
        _PUT_NETWORK_SCHEMA(network_change_info)
    except validators.MultipleInvalid as exc:
        raise validators.BadRequest(str(exc))

    netplan_info = {
        "network":{
            "version": 2,
            "renderer": "NetworkManager",
            "ethernets":{
                "enp0s3":{
                    "dhcp4": "no",
                    "addresses": network_change_info['addresses'],
                    "gateway4": network_change_info['gateway4'],
                    "nameservers": {
                        "addresses": network_change_info['nameservers']
                    }
                }
            }
        }
    }

    with open('/etc/netplan/01-network-manager-all.yaml', 'w') as f:
        yaml.dump(netplan_info, f)

    return make_response(
        netplan_info,
        200
    )


if __name__ == '__main__':
    app.debug = True
    app.run()