import collections
import operator
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

from pylab import *

def type_table(item):
    result = {}
    if 'a' in item.keys():
        money = 21709 * item['a']
        return money
    if 'b' in item.keys():
        money = 31.04 * item['b']
        return money
    if 'c' in item.keys():
        money = 13028 * item['c']
        return money
    if 'd' in item.keys():
        money = 0 * item['d']
        return money
    if 'e' in item.keys():
        money = 21709 * item['e']
        return money
    if 'f' in item.keys():
        money = 3028 * item['f']
        return money

def print_result(result_list):
    x1 = ['9/1', '9/2', '9/3', '9/4', '9/5']
    y1 = [result_list[1]*1.5, result_list[1]*3.5, result_list[1]*6.5, result_list[1]*9.5, result_list[1]*12.5]
    fig, ax = plt.subplots(figsize=(10, 6))
    pl.plot(x1, y1, '.-', label=result_list[0])
    pl.legend()

    pl.title(str(result_list[0]) + 'Repair Budget')# give plot a title
    pl.xlabel('Date') # make axis labels
    pl.ylabel('Money')
    plt.grid(True)
    pl.savefig(str(result_list[0]) + '.png')
    pl.show()

def main():
    result_dict = {}
    fix_item = [
        {'A Road':{'a':2}}, 
        {'B Road':{'b':10}}, 
        {'C Road':{'a':15}}, 
        {'D Road':{'c':5}}, 
        {'E Road_A':{'e':4}}, 
        {'E Road_B':{'f':4}}
    ]
    for i in range(len(fix_item)):
        item = fix_item[i]
        data = list(fix_item[i].keys())
        category = item[data[0]]
        result = type_table(category)
        result_dict[data[0]] = result
    result_sort = sorted(result_dict.items(), key=lambda x: x[1], reverse=True) 
    print(result_sort)
    for i in range(len(result_sort)):
        print_result(result_sort[i])


if __name__ == "__main__":
    main()
