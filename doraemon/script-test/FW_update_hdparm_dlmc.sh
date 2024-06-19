#!/bin/bash

dmesg -n 1
echo -ne "\033[9;0]"


hdparm_update_main() {
    clear

    limit_firmware="S16425"    # Conditions for the firmware version
    limit_firmware_1="S17411"  # Conditions for the firmware version 1 
    update_firmware="S23222"   # New firmware version
    loader_firmware="01.01001" # Conditions for the Model name
        
    txt_color # Call txt color
    echo -e "${menu}Execute DLMirco code (hdparm)...${normal}"
    printf "\n"
    
    # 1. Get all SSD devices.
    ssd_devices=($(lsblk -d -o NAME,MODEL | grep -i "SSD\|M.2\|InnoDisk\|mSATA\|Generic_FCR_SATA_Loader" | awk '{print "/dev/"$1}'))
    num_ssd_devices=${#ssd_devices[@]}
    updated_devices=()
    not_updated_devices=()

    if [ $num_ssd_devices -gt 0 ]; then
        for ssd_device in "${ssd_devices[@]}"; do
            # 2. Get SSD model name and firmware version
            model=$(smartctl -i "${ssd_device}" | sed '2d; /Device Model:/!d; s/.*: *//')
            ssd_version=$(smartctl -i "${ssd_device}" | awk '/Firmware Version:/ {print $NF}')

            # 3. Print all SSD information
            echo "${ssd_device}, ${model}, firmware: ${ssd_version}"
            
            # 4. SSD firmware version = limit_firmware
            if [ "${ssd_version}" == "${limit_firmware}" ]; then
            
                # 4-1. Exceute hdparm command
                echo -e "${number}Loading ${fgred}${update_firmware}_${limit_firmware}.bin ${number}file and updating firmware version to ${update_firmware} for ${ssd_device}...${normal}"
                
                # Select folder
                cd /mnt/DLM # from USB dongle
                #cd /home/inno/Desktop/Scripts/USB_dongle_8GB_Ubuntu18.04/mnt/DLM # from X86 platform for verify
                
		hdparm --yes-i-know-what-i-am-doing --please-destroy-my-drive --fwdownload "${update_firmware}"_"${limit_firmware}".bin "${ssd_device}"
                updated_devices+=("${ssd_device}")
 
            # 5. SSD firmware version = limit_firmware_1                             
            elif [ "${ssd_version}" == "${limit_firmware_1}" ]; then
            
                # 5-1. Exceute hdparm command
                echo -e "${number}Loading ${fgred}${update_firmware}_${limit_firmware_1}.bin ${number}file and updating firmware version to ${update_firmware} for ${ssd_device}...${normal}"
                
                # Select folder
                cd /mnt/DLM # from USB dongle
                #cd /home/inno/Desktop/Scripts/USB_dongle_8GB_Ubuntu18.04/mnt/DLM # from X86 platform for verify
             
		hdparm --yes-i-know-what-i-am-doing --please-destroy-my-drive --fwdownload "${update_firmware}"_"${limit_firmware_1}".bin "${ssd_device}"
                updated_devices+=("${ssd_device}")
            
            # 6. SSD firmware version = loader mode  
            elif [ "${ssd_version}" == "${loader_firmware}" ]; then
            
                # 6-1. Exceute JMMP write code command
                echo -e "${number} --> ${model} was in the ROM code, and we will recover it...${normal}"

                # Select folder
                cd /mnt/DLM/WriteCode # from USB dongle
                #cd /home/inno/Desktop/Scripts/USB_dongle_8GB_Ubuntu18.04/mnt/DLM/WriteCode # from X86 platform for verify                
                
                ./mp_64 -d "${ssd_device}" -c 1 -u -k
                updated_devices+=("${ssd_device}")   
                
            else
            # 7. Others 
                not_updated_devices+=("${ssd_device}")
            fi
        done

        if [ ${#updated_devices[@]} -gt 0 ]; then
            	printf "\n"
    		echo -e "${pass}The SSDs firmware has been updated:${normal}"
    		for device in "${updated_devices[@]}"; do
       		 model=$(smartctl -i "${device}" | sed '2d; /Device Model:/!d; s/.*: *//')
       		 ssd_version=$(smartctl -i "${device}" | awk '/Firmware Version:/ {print $NF}')
        		echo "${device} is ${model}, firmware is ${ssd_version}"
    		done
    		printf "\n\n\n"
    		echo -e "${number}The system will be shutdown in 10 seconds... ${normal}"
    		sleep 10
    		shutdown now
	else
    		echo -e "${fgred}No SSD need to be updated because firmware is not ${limit_firmware}/${limit_firmware_1}/ROM code. ${normal}"
	fi
    else
        echo -e "${fgred}Cannot found any SSD.${normal}"
    fi

    printf "\n\n\n"
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
hdparm_update_main

