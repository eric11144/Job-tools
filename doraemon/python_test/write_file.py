import datetime
import time
import os


home_directory = os.path.expanduser("~")
folder_path = home_directory + '/test/'  # 要写入文件的文件夹路径
test_file_prefix = 'file'  # 文件名前缀
reboot_file_path = home_directory + 'reboot_log/'
reboot_log_file = "reboot_count.txt"
disk_limit = 80  # 磁盘使用率限制，当超过该百分比时触发删除操作
runtime = 3600  # 运行时间（秒），即1小时
file_count = 1

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
    
    file_path = os.path.join(folder_path, f'{test_file_prefix}{counter}.txt')
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
        # delete file
        os.remove(file_path)

    # Update file number and runtime.
    counter += 1
    file_count += 1
    with open(counter_file, 'w') as f:
        f.write(str(counter) + '\n')
        f.write(current_time_string)

    # Add the idle time, when the file count is 5000, it will trigger.
    if file_count >= 5000:
        time.sleep(180)
        file_count = 1

    # Check if the runtime exceeds the set value.
    if start_time_int - current_time_int >= runtime:
        wait_time = 60
        # Restart system
        
        # Check reboot file is exists or not.
        if not os.path.exists(reboot_file_path):
            os.makedirs(reboot_file_path)

            log.insert(0, "Reboot count: 1\n")
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log.append(f"Rebooted at: {current_time}\n")

            with open(reboot_log_file, 'w') as f:
                f.writelines(log)
        # Read reboot log file with reboot count
        else:
            with open(reboot_log_file, 'r') as f:
                log = f.readlines()
            
            if log and "Reboot count:" in log[0]:
                count = int(log[0].split(":")[1].strip()) + 1
                log[0] = f"Reboot count: {count}\n"
            else:
                log.insert(0, "Reboot count: 1\n")

            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log.append(f"Rebooted at: {current_time}\n")

            with open(reboot_log_file, 'w') as f:
                f.writelines(log)
        
        while True:
            mins, secs = divmod(wait_time, 60)
            timer = '{:02d}'.format(secs)
            print("restart_time : " + str(timer), end="\r")
            time.sleep(1)
            wait_time -= 1
            if wait_time == 0:
                print("restart system")
                break;
            
        os.system("reboot")

    time.sleep(0.05)
