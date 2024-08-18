import os
from openpyxl import Workbook
from os import listdir


smart_list = []
test_list = []
log_list = []
mypath = "./2022-09-02_log/"

files = listdir(mypath)
files.sort()
# print(files)

for file_name in files:
    print(file_name)

    file = open(mypath + file_name, 'rb')

    wb = Workbook() # creates a workbook object.
    ws = wb.active # creates a worksheet object.

    # for smart_log_line in file.readlines()[42:]:
    for smart_log_line in file.readlines():
        smart_log_line = smart_log_line.decode("utf-8")
        smart_log_line = smart_log_line.strip('------------------------------------------------------------')
        try:
            smart_log_line = smart_log_line.strip()
            smart_list.append(smart_log_line.replace('\t', ' '))
        except IndexError:
            continue 

    for element in smart_list:
        if element != '':
            log_list.append(element)
        elif log_list == []:
            continue
        else:
            ws.append(log_list)
            log_list = []

wb.save('smart_log.xlsx')
