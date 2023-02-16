#!/usr/bin/python
a=[]
with open('test', 'rt') as f:
    for line in f:
        if line in a:
            print(line)

        a.append(line)

