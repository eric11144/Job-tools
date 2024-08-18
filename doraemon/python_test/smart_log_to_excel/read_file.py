from os import listdir


mypath = "./2022-09-02_log/"
file_list = []

files = listdir(mypath)

# print(files)

for file_name in files:
    print(file_name)
    file_list.append(file_name)

file_list.sort()
print(file_list)