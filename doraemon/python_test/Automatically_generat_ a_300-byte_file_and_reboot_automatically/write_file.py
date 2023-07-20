import datetime
import time
import os

folder_path = '/home/ubuntu/test/'  # 要写入文件的文件夹路径
file_prefix = 'file'  # 文件名前缀
reboot_file_path = "/home/ubuntu/reboot_count.txt"
disk_limit = 80  # 磁盘使用率限制，当超过该百分比时触发删除操作
runtime = 3600  # 运行时间（秒），即1小时

current_time = datetime.datetime.now()
current_time_int = int(round(current_time.timestamp()))
current_time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 获取上次写入的文件编号和运行时间
counter_file = os.path.join(folder_path, 'time.txt')

print('Start to write file')

if os.path.exists(counter_file):
    with open(counter_file, 'r') as f:
        counter = int(f.readline())
        print("current_count : " + str(counter))
else:
    counter = 1
    start_time = datetime.datetime.now()
    print("start_time : " + start_time.strftime("%Y-%m-%d %H:%M:%S"))

while True:
    print("current_time : " + current_time_string)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, f'{file_prefix}{counter}.txt')
    data = os.urandom(300)
    
    with open(file_path, 'wb') as file:
        file.write(data)  # 300 Byte

    # 获取磁盘使用率
    statvfs = os.statvfs('/')
    disk_usage = int((1 - (statvfs.f_bavail / statvfs.f_blocks)) * 100)
    print("disk_usage : " + str(disk_usage) + "%")

    start_time = datetime.datetime.now()
    start_time_int = int(round(start_time.timestamp()))
    print("start_time : " + start_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("current_count : " + str(counter))
    print('**************************************************************')

    if disk_usage > disk_limit:
        # 删除文件
        os.remove(file_path)

    # 更新文件编号和运行时间
    counter += 1
    with open(counter_file, 'w') as f:
        f.write(str(counter) + '\n')
        f.write(current_time_string)

    # 检查运行时间是否超过设定值
    if start_time_int - current_time_int >= runtime:
        wait_time = 60
        # 重启系统
        count=0
        reboot_current_time = datetime.datetime.now()
        filename="/home/ubuntu/log.txt"
        
        # read_reboot_count      
        try:
            with open(filename, 'r') as file:
                count = int(file.read().strip())
        except (FileNotFoundError, ValueError):
                pass
        
        # 更新重開機次數
        count += 1

        with open(filename, 'w') as file:
            file.write(str(count))

        print("Reboot_count : " + str(count))
        
        while True:
            mins, secs = divmod(wait_time, 60)
            timer = '{:02d}'.format(secs)
            print("restart_time : " + str(timer), end="\r")
            time.sleep(1)
            wait_time -= 1
            if wait_time == 0:
                print("restart system")
                break;
            
        os.system("sudo reboot")

    time.sleep(5)
