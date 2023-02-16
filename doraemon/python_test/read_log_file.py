#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

path = 'test.log'
data_list = []
data_list_1 = []
matplotlib_count = []
matplotlib_element = []

# read log file
f = open(path,'r')

# output log file
output_path = 'output.txt'
output_f = open(output_path, 'w')

for line in f.readlines():
    data_list.append(line.split())

# remove ada0
for element in range(len(data_list)):
    if "ada0" not in data_list[element]:
        # remove KB/t
        if "KB/t" not in data_list[element]:
            data_list_1.append(data_list[element])

# output MB/s log file
for element in range(len(data_list_1)-1):
    output_f.write(data_list_1[element][2])
    output_f.write("\n")

# get MB/s 
for element in range(1000):
    matplotlib_element.append(float(data_list_1[element][2]))

# make count 
for element in range(1000):
    matplotlib_count.append(element)

plt.figure(figsize=[50,100],dpi=96,facecolor='white',edgecolor='white',frameon=True,tight_layout=False)

# make label
xmax = max(matplotlib_count)
ymax = int(max(matplotlib_element))+100

plt.xlim([0,xmax])
plt.ylim([0,ymax])

# draw plot
plt.plot(matplotlib_count,matplotlib_element, marker='o')

# set x label name
plt.xlabel("count")

# set y label name
plt.ylabel("speed MB/s")

# show the plot with grid
plt.grid(True)

# show the plot
plt.show()