#!/usr/bin/env python3
# -*- coding: utf-8 -*-


f = open('testtime.txt')
for line in f.readlines():
    line = round(int(line) / 100000 * 0.1, 2)
    with open('testtime_transfer.txt', 'a+') as f:
        print(line)
        f.write( str(line) + '\n')