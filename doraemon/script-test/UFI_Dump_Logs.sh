#!/bin/bash
#
# Author: FAE-Jay
# Date: 2024/07/10
#

dmesg -n 1
echo -ne "\033[9;0]"

hdparm_update_main() {
    clear
    
    current_model="M.2 (S42) 3IE4"
    loader_model="MRVL"
        
    txt_color # Call txt color
    echo -e "${menu}i. Automatically executing dump elog/SMART Info/dmesg... ${normal}"
    printf "\n"
    
    # Set path
    SMART_path="/home/aaa/Desktop/UFI/iSMART_6.4.17/"
    eLog_path="/home/aaa/Desktop/UFI/ELog_M41_V1.1.0_x86_x84/"
    logs_path="/home/aaa/Desktop/UFI/Logs/"    
    
    # 1. Get all SSD devices matching the specified model.
    ssd_devices=($(lsblk -d -o NAME,MODEL | grep -i "$current_model\|$loader_model" | awk '{print "/dev/"$1}'))
    num_ssd_devices=${#ssd_devices[@]}
    updated_devices=()
    not_updated_devices=()

    if [ $num_ssd_devices -gt 0 ]; then
        for ssd_device in "${ssd_devices[@]}"; do
            # 2. Get SSD model name and firmware version
            model=$(smartctl -i "${ssd_device}" | sed '2d; /Device Model:/!d; s/.*: *//')
            ssd_version=$(smartctl -i "${ssd_device}" | awk '/Firmware Version:/ {print $NF}')
            ssd_serial=$(smartctl -i "${ssd_device}" | awk '/Serial Number:/ {print $NF}')
            
            # 3. Print all SSD information
            echo -e "${number}Step 1. Device list...${normal}"
            echo "${ssd_device}, ${model}, firmware: ${ssd_version}, SN: ${ssd_serial}" 
            sleep 1
            
            # 4. Check if SSD model matches current_model or loader_model
            if [ "${model}" == "${current_model}" ]; then
                # 5. Create the folder by SN
                if mkdir -p "${logs_path}${ssd_serial}"; then
    			echo -e "${pass} --> Created the folder. ${normal}"
		else
    			echo -e "${fgred}Failed to create folder ${logs_path}${ssd_serial}${normal}"
    		exit 1  
		fi
                sleep 1
                printf "\n"
                
                # 6. Dump eLog (Step 1.)
                echo -e "${number}Step 2. Dump elog...${normal}"
                cd "${eLog_path}"
                ./ELog_64 -d "${ssd_device}" > /dev/null 2>&1
                echo -e "${pass} --> Done. The elog was saved. ${normal}"

                # 6-1. Move eLog to Logs folder 
                mv *.log "${logs_path}${ssd_serial}/"
		
		sleep 1
		printf "\n"  
                
                # 7. Get the SMART Info (Step 2.)
                echo -e "${number}Step 3. Get SMART Info...${normal}"
                cd "${SMART_path}"
                ./iSMART_64 -d "${ssd_device}" >> "${logs_path}${ssd_serial}/${ssd_serial}_iSMART.log"
                echo -e "${pass} --> Done. The SMART log was saved. ${normal}"
                sleep 1
                printf "\n"
                
                # 8. Dump dmesg (Step 3.)
                echo -e "${number}Step 4. Dump dmesg...${normal}"
                dmesg >> "${logs_path}${ssd_serial}/${ssd_serial}_dmesg.log"
                echo -e "${pass} --> Done. The dmesg was saved. ${normal}"                    
                sleep 1
                printf "\n"    
                
                # 9. Clear dmesg
                dmesg -C
                
                echo -e "${pass}The logs have all been saved at ${logs_path}${ssd_serial} :) ${normal}" 
                cd ${logs_path}${ssd_serial}
                echo -e "$(ls)" 
                printf "\n" 
                                
            elif [ "${model}" == "${loader_model}" ]; then
                echo -e "${fgred}The SSD is in loader mode !!!... @@ ${normal}"    
                echo -e "${fgred}Please report it to PE engineer for troubleshooting!!! ${normal}"           
            else
                not_updated_devices+=("${ssd_device}")  
                echo -e "${fgred}No SSD needs to dump logs, or the SSD was in loader mode... ${normal}"    
                echo -e "${number} --> Please report it to PE-Hank #5165 for troubleshooting!!! ${normal}"
                sleep 1
                printf "\n"
            fi
            
            # 10. Prompt operator to remove the current SSD
            echo -e "${menu}Please remove the current SSD. Insert the next SSD when ready...${normal}"

        done
    else
        echo -e "${fgred}Cannot find any SSD.${normal}"
        echo -e "${number} --> Please report it to PE-Hank #5165 for troubleshooting!!! ${normal}"
        sleep 1
        printf "\n"
    fi
}

txt_color(){
    normal=`echo "\033[m"` #White
    menu=`echo "\033[36m"` #Blue
    number=`echo "\033[33m"` #Yellow
    fgred=`echo "\033[31m"` #Red
    pass=`echo "\033[32m"` #Green
}
clear

txt_color

# Monitor for SSD plug in/out events
monitor_ssd() {
    echo -e "${menu}Monitoring for SSD plug in/out events...${normal}"
    sleep 1
    printf "\n"
    
    udevadm monitor --subsystem-match=block --property | while read -r line; do
        if [[ "$line" == *"add"* ]]; then
            echo -e "${pass}SSD inserted.${normal}"
            sleep 1
            printf "\n"
        elif [[ "$line" == *"remove"* ]]; then
            echo -e "${fgred}SSD removed.${normal}"
            sleep 1
            printf "\n"
        fi
    done
}

# Initial call to hdparm_update_main to show initial output
hdparm_update_main

# Main loop
while true; do
    echo -e "${menu} *** Press Enter to continue...*** ${normal}"
    read -r
    hdparm_update_main
done

