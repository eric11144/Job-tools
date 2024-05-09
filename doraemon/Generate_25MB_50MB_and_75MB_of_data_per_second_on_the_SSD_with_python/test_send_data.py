import time
import os
import subprocess


def write_data_to_disk(path, total_duration_sec):
    # rates = [(25, total_duration_sec * 1/3), (50, total_duration_sec * 1/3), (75, total_duration_sec * 1/3)]
    rates = [(25, total_duration_sec), (50, total_duration_sec), (75, total_duration_sec)]
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, "test_data.bin")

    with open(filepath, 'wb') as f:
        # start_time = time.time()
        for rate, duration in rates:
            start_time = time.time()
            segment_start_time = time.time()
            segment_end_time = segment_start_time + duration
            bytes_per_second = rate * 1024 * 1024
            total_bytes_written = 0

            while time.time() < segment_end_time:
                loop_start_time = time.time()
                if segment_end_time - loop_start_time < 1:
                    # Adjust bytes_to_write if less than one second left
                    bytes_to_write = int((segment_end_time - loop_start_time) * bytes_per_second)
                else:
                    bytes_to_write = bytes_per_second

                f.write(bytearray(bytes_to_write))
                f.flush()
                os.fsync(f.fileno())
                loop_end_time = time.time()
                actual_write_time = loop_end_time - loop_start_time
                total_bytes_written += bytes_to_write

                # Sleep to maintain the target write speed
                sleep_time = 1 - actual_write_time
                if sleep_time > 0:
                    time.sleep(sleep_time)

                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                elapsed_time = loop_end_time - start_time
                percent_complete = (elapsed_time / total_duration_sec) * 100
                print(f"{current_time} - Progress: {percent_complete:.2f}% - Speed: {rate} MB/s", end='\r')
            
            segment_duration = time.time() - segment_start_time
            print(f"\nRate {rate} MB/s - Segment Duration: {segment_duration:.2f} seconds")

        total_end_time = time.time()
        total_duration = total_end_time - start_time
        print(f"\nTotal time taken: {total_duration:.2f} seconds")
        print(f"Data written to {filepath}: {total_bytes_written / 1024 / 1024:.2f} MBytes")

    return filepath

def countdown_and_reboot(seconds):
    print(f"Countdown started: {seconds} seconds until shutdown.")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up! Reboot now...")
    try:
        # reboot command
        subprocess.run(['sudo', 'reboot'], check=True)
    except subprocess.CalledProcessError:
        print("Failed to reboot the system. Ensure the script has the necessary permissions.")

def main():
    duration_sec = 13 * 60
    disk_path = "/mnt/wwn-0x524693e000000000/"  # Ensure that this path is correct and has the necessary permissions.
    boot_count_path = os.path.join(disk_path, "boot_count.txt")

    os.makedirs(disk_path, exist_ok=True)  # Ensure that the target directory exists.

    # Read and update the boot count.
    if os.path.exists(boot_count_path):
        with open(boot_count_path, 'r') as file:
            boot_count = int(file.read().strip()) + 1
    else:
        boot_count = 1  # If the file does not exist, create it and start counting.

    with open(boot_count_path, 'w') as file:
        file.write(str(boot_count))

    print(f"Boot count: {boot_count}")

    filepath = write_data_to_disk(disk_path, duration_sec)
    os.remove(filepath)  # Delete the written file.

    countdown_and_reboot(60)

if __name__ == "__main__":
    main()