#!/bin/sh

CONN_NAME=wifi-setup
DEVNAME=wlan0

set -e

if [ $# -ne 5 ]; then
    printf "usage: <ssid> <ascii-psk> <address> <gateway> <dns-server>\n" >&2
    exit 1
fi

SSID=$1
PSK=$2
IP_ADDRESS=$3
GATEWAY_ADDRESS=$4
DNS_ADDRESS=$5

# remove existing configuration
nmcli connection delete ${CONN_NAME} || true

nmcli connection add con-name ${CONN_NAME} \
    type wifi \
    ifname ${DEVNAME} \
    ssid ${SSID} \
    -- \
    wifi-sec.key-mgmt wpa-psk \
    wifi-sec.psk ${PSK} \
    ipv4.method manual \
    ipv4.address ${IP_ADDRESS} \
    ipv4.gateway ${GATEWAY_ADDRESS} \
    ipv4.dns ${DNS_ADDRESS} \
    connection.autoconnect no
