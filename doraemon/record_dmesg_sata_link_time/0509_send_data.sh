#!/bin/bash

# Set the log file path
LOG_FILE="/mnt/wwn-0x524693e000000000/reboot_log.txt"
REBOOT_COUNT_FILE="/mnt/wwn-0x524693e000000000/reboot_count.txt"
DATA_FILE="/mnt/wwn-0x524693e000000000/datafile.bin"

# Check if the log file exists, create it if it does not.
if [ ! -f "$LOG_FILE" ]; then
    echo "Creating log file..."
    touch "$LOG_FILE"
fi

# Read and update the reboot count.
if [ ! -f "$REBOOT_COUNT_FILE" ]; then
    echo "0 - $(date)" > "$REBOOT_COUNT_FILE"
fi

COUNT=$(cut -d ' ' -f 1 < "$REBOOT_COUNT_FILE")
COUNT=$((COUNT+1))
echo "$COUNT - $(date)" > "$REBOOT_COUNT_FILE"

# Check the SATA link startup time
SATA_TIME=$(dmesg | grep "SATA link up" | grep -oP "\[\s*\K\d+\.\d+(?=\])")

# Check if it is greater than 10 seconds
if [[ $(echo "$SATA_TIME > 10" | bc) -eq 1 ]]; then
    echo "SATA link up time ($SATA_TIME) is greater than 10 seconds. Stopping the script."
    echo "SATA link up time ($SATA_TIME) stopped script at $(date)" >> $LOG_FILE
    exit 0  # Exit the script successfully
else
    echo "SATA link up time ($SATA_TIME) is not greater than 10 seconds. Running write command."
    echo $COUNT
    ./writedata -t 60GB -b 50KB $DATA_FILE

    # Wait randomly for 10 to 15 seconds
    SLEEP_TIME=$(($RANDOM % 6 + 10))
    echo "Sleeping for $SLEEP_TIME seconds..."
    sleep $SLEEP_TIME

    # Record the reboot time and count
    echo "Reboot #${COUNT} at $(date) with SATA link up time: $SATA_TIME" >> $LOG_FILE

    # reboot system
    echo "Rebooting now..."
    sudo reboot
fi
