from datetime import datetime
from influxdb import InfluxDBClient
from pymodbus.client.sync import ModbusSerialClient
from time import sleep

DELAY=0.03

def get_fields():
    client = ModbusSerialClient(
        method='rtu',
        port='/dev/ttyM0',
        baudrate=9600,
        timeout=0.5)
    
    fields = {}
    result = client.read_holding_registers(0, 1)
    fields['voltage_V'] = float(result.registers[0]) / 10
    
    sleep(DELAY)
    result = client.read_holding_registers(1, 2)
    fields['current_A'] = float(result.registers[0]) / 10
    fields['frequency_Hz'] = float(result.registers[1]) / 100
    
    sleep(DELAY)
    result = client.read_holding_registers(3, 2)
    fields['kW'] = float(result.registers[0]) / 100
    fields['kVA'] = float(result.registers[1]) / 100

    sleep(DELAY)
    result = client.read_holding_registers(6, 1)
    fields['power-factor'] = float(result.registers[0]) / 1000
    
    sleep(DELAY)
    result = client.read_holding_registers(7, 2)
    fields['kWh'] = float(int(result.registers[0]) * 65536 + result.registers[1]) / 100

    return fields


HOST = '192.168.3.78'
PORT = 8086
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'home'


def update():
    time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    fields = get_fields()

    client = InfluxDBClient(
        HOST,
        PORT,
        USERNAME,
        PASSWORD,
        DATABASE)
    client.create_database(DATABASE)

    client.write_points([{
        'measurement': 'baw-2c',
        'time': time,
        'fields': fields}])


if __name__ == '__main__':
    update()
