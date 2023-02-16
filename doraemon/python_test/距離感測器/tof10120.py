#!/usr/bin/python
import time
from smbus2 import SMBus
from micropython import const

bus = SMBus(1)
time.sleep(1)

addr = const(0x52)
prev_distance = 200

def range_mm():
  bus.write_byte(addr,0)
  time.sleep(0.02)
  value = bus.read_byte(addr) << 8 | bus.read_byte(addr)
  time.sleep(0.05)
  return value

try:
  while True:
    distance = range_mm()
    print(distance)
except KeyboardInterrupt:
  bus.close()

print("Stopped")