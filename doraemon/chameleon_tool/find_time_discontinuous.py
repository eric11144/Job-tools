#!/usr/bin/python
import datetime
import dateutil.parser

a = []

with open('date', 'rt') as f:
    for line in f:
        a.append(dateutil.parser.parse(line))

list_len = len(a)

try:
    for num in range(list_len):
        sec = a[num+1] - a[num]

        if (sec.seconds) != 1:
            print(a[num])

except IndexError:
    pass
