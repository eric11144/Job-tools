import os
import datetime


filename = "/home/hunt/reboot_log/"
LOG_FILE = filename + "log.txt"
count = 0
log = []
# while count == 0:
#     try:
#         with open(filename, 'r') as file:
#             count = int(file.readline().split(":")[1].strip())
#             print(count)
#     except (FileNotFoundError, ValueError):
#         pass

#     print(count)

#     # Reboot count
#     # count += 1

#     with open(filename, 'w') as file:
#         file.writelines("Reboot count: " + str(count))
if not os.path.exists(filename):
    os.makedirs(filename)

    log.insert(0, "Reboot count: 1\n")
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log.append(f"Rebooted at: {current_time}\n")

    with open(LOG_FILE, 'w') as f:
        f.writelines(log)
else:
    with open(LOG_FILE, 'r') as f:
        log = f.readlines()
    
    if log and "Reboot count:" in log[0]:
        count = int(log[0].split(":")[1].strip()) + 1
        log[0] = f"Reboot count: {count}\n"
    else:
        log.insert(0, "Reboot count: 1\n")

    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log.append(f"Rebooted at: {current_time}\n")

    with open(LOG_FILE, 'w') as f:
        f.writelines(log)
